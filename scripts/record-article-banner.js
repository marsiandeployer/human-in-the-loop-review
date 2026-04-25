#!/usr/bin/env node
// Record CSS-animated banner from an article to banner.mp4
// Usage: node record-article-banner.js <article-dir>
//   e.g. node record-article-banner.js /root/vibers/wordpress/wordpress-emergency-help
//
// Writes frames to /tmp/banner_frames_<slug> then runs ffmpeg to produce banner.mp4
// inside the article dir. Targets .sc-banner (falls back to #sc-banner-fallback).

const http = require('http');
const fs = require('fs');
const path = require('path');
const {spawnSync} = require('child_process');
const WebSocket = require('ws');

const CDP_PORT = 9223;
const articleDir = process.argv[2];
if (!articleDir) { console.error('Usage: node record-article-banner.js <article-dir>'); process.exit(1); }

const htmlPath = path.join(articleDir, 'index.html');
if (!fs.existsSync(htmlPath)) { console.error('Not found:', htmlPath); process.exit(1); }

const slug = path.basename(articleDir);
const FILE_URL = 'file://' + htmlPath;
const FRAMES_DIR = `/tmp/banner_frames_${slug}`;
const OUT_MP4 = path.join(articleDir, 'banner.mp4');

fs.rmSync(FRAMES_DIR, {recursive:true, force:true});
fs.mkdirSync(FRAMES_DIR, {recursive:true});

const sleep = ms => new Promise(r=>setTimeout(r,ms));

function httpPut(url){return new Promise((res,rej)=>{const u=new URL(url);const r=http.request({hostname:u.hostname,port:+u.port,path:u.pathname+(u.search||''),method:'PUT'},resp=>{let d='';resp.on('data',c=>d+=c);resp.on('end',()=>res(d))});r.on('error',rej);r.end()})}
function httpGet(url){return new Promise((res,rej)=>{http.get(url,r=>{let d='';r.on('data',c=>d+=c);r.on('end',()=>res(d))}).on('error',rej)})}

(async () => {
  const tab = JSON.parse(await httpPut(`http://localhost:${CDP_PORT}/json/new?${encodeURIComponent(FILE_URL)}`));
  console.log('[tab]', tab.id);
  await sleep(4000);

  const ws = new WebSocket(tab.webSocketDebuggerUrl);
  let msgId = 0;
  const pending = new Map();
  const frames = [];

  ws.on('message', raw => {
    const msg = JSON.parse(raw);
    if (msg.id && pending.has(msg.id)) { const cb=pending.get(msg.id); pending.delete(msg.id); cb(msg.result||{}); }
    if (msg.method === 'Page.screencastFrame') {
      frames.push(msg.params.data);
      ws.send(JSON.stringify({id:++msgId,method:'Page.screencastFrameAck',params:{sessionId:msg.params.sessionId}}));
    }
  });
  const send = (method,params={}) => new Promise(res => { const id=++msgId; pending.set(id,res); ws.send(JSON.stringify({id,method,params})); });

  await new Promise(r => ws.once('open', r));
  await send('Page.enable');
  await sleep(500);

  await send('Emulation.setDeviceMetricsOverride', {width:800, height:460, deviceScaleFactor:1, mobile:false});
  await sleep(300);

  const scroll = await send('Runtime.evaluate', {expression:`
    var b = document.querySelector('.sc-banner') || document.querySelector('#sc-banner-fallback');
    if(!b){ 'no-banner' } else {
      b.scrollIntoView({block:'start'});
      document.body.style.overflow='hidden';
      'ok'
    }
  `});
  console.log('[scroll]', scroll.result && scroll.result.value);
  if (scroll.result && scroll.result.value === 'no-banner') { ws.close(); process.exit(2); }
  await sleep(300);

  const rect = await send('Runtime.evaluate', {expression:`
    var b=document.querySelector('.sc-banner')||document.querySelector('#sc-banner-fallback');
    var r=b.getBoundingClientRect();
    JSON.stringify({h:Math.round(r.height),w:Math.round(r.width),top:Math.round(r.top)})
  `});
  console.log('[rect]', rect.result && rect.result.value);

  // Restart animations
  await send('Runtime.evaluate', {expression:`
    (function(){
      var s=document.createElement('style');
      s.textContent='.sc-banner.r, .sc-banner.r *, .sc-banner.r *::before, .sc-banner.r *::after, #sc-banner-fallback.r, #sc-banner-fallback.r *, #sc-banner-fallback.r *::before, #sc-banner-fallback.r *::after { animation:none !important; }';
      document.head.appendChild(s);
      var b=document.querySelector('.sc-banner')||document.querySelector('#sc-banner-fallback');
      b.classList.add('r'); void b.offsetWidth; b.classList.remove('r');
      document.head.removeChild(s);
      return 'reset';
    })()
  `});

  await send('Page.startScreencast', {format:'jpeg', quality:92, maxWidth:800, maxHeight:460, everyNthFrame:4});
  console.log('[recording 30s]');
  await sleep(30000);
  await send('Page.stopScreencast');
  console.log(`[captured] ${frames.length} frames`);
  ws.close();

  const useFrames = Math.min(frames.length, 412);
  for (let i=0;i<useFrames;i++) {
    fs.writeFileSync(path.join(FRAMES_DIR, `frame_${String(i+1).padStart(5,'0')}.jpg`), Buffer.from(frames[i],'base64'));
  }
  await httpGet(`http://localhost:${CDP_PORT}/json/close/${tab.id}`).catch(()=>{});

  // ffmpeg: stitch frames + crop to banner area (720x446, offset x=40 y=0)
  console.log('[ffmpeg]', OUT_MP4);
  const r = spawnSync('ffmpeg', [
    '-y', '-framerate', '14.714',
    '-i', path.join(FRAMES_DIR, 'frame_%05d.jpg'),
    '-vf', 'crop=720:446:40:0',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '22', '-preset', 'medium',
    OUT_MP4
  ], {stdio:'inherit'});
  if (r.status !== 0) { console.error('ffmpeg failed'); process.exit(3); }
  console.log('[done]', OUT_MP4);
})().catch(e => { console.error(e); process.exit(1); });
