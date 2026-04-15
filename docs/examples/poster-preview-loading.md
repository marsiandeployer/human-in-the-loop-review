# Selected Poster Preview

- title: Selected Poster Preview
- summary: On the responsive layout, the selected poster did not load fully in the preview area, so users saw an incomplete image instead of the full poster they picked.
- before: https://skrinshoter.ru/s/080426/GeYapKeQ.png?view=1&name=%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82-08-04-2026%2006:32:55.png
- after: https://i.wpmix.net/image/photo/photo_1776266708284.jpg
- prompt: Fix the selected poster preview in the responsive UI. Right now when a user picks a poster, the preview does not render the full chosen image on smaller screens, so the result looks incomplete. Update the preview container and image sizing logic so the selected poster loads fully, keeps its aspect ratio, and stays clearly visible without breaking the existing desktop layout.
- proof: https://skr.sh/savGeYapKeQ
- notes: Verified and fixed. This case is meant to show a UI state bug where the chosen asset was not displayed completely after selection on adaptive layouts.
