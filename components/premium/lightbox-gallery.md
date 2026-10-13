# Lightbox Gallery

Project gallery whose thumbnails morph into a full-screen viewer and back. With the View Transitions API the clicked photo grows from its exact spot in the grid into the viewer, and closing flies it home. Inside the viewer: arrow keys, buttons, or swipe with a drag-follow to move between photos; the full-size image swaps in once loaded. Browsers without View Transitions get a clean fade-and-scale. Without JS, each thumbnail links to its full image. Depends on `tokens/variables.css`.

**Motion:** shared-element morph thumbnail ↔ viewer (View Transitions) · backdrop blur fade · directional slide between photos · drag-follow swipe · thumbnail zoom and expand-icon reveal on hover.

## HTML

```html
<section class="morph-lightbox" aria-labelledby="morph-lightbox-title" data-morph-lightbox>
  <div class="morph-lightbox__inner">
    <header class="morph-lightbox__head">
      <p class="morph-lightbox__eyebrow">Gallery</p>
      <h2 id="morph-lightbox-title" class="morph-lightbox__title">See the craft before you call.</h2>
      <p class="morph-lightbox__lead">Every photo is a finished Brand job. Tap one to look closer.</p>
    </header>

    <ul class="morph-lightbox__grid" role="list">
      <li class="morph-lightbox__item morph-lightbox__item--tall"><a class="morph-lightbox__thumb" href="gallery-kitchen-large.jpg" data-caption="Open-plan kitchen remodel · Westlake"><img src="gallery-kitchen.jpg" alt="Open-plan kitchen with oak cabinets and a quartz island" width="800" height="1000" loading="lazy"></a></li>
      <li class="morph-lightbox__item"><a class="morph-lightbox__thumb" href="gallery-shower-large.jpg" data-caption="Walk-in shower · Riverside"><img src="gallery-shower.jpg" alt="Walk-in shower with large grey tiles and a glass screen" width="800" height="600" loading="lazy"></a></li>
      <li class="morph-lightbox__item"><a class="morph-lightbox__thumb" href="gallery-boiler-large.jpg" data-caption="Boiler install · Northside"><img src="gallery-boiler.jpg" alt="New wall-mounted boiler with neat copper pipework" width="800" height="600" loading="lazy"></a></li>
      <li class="morph-lightbox__item morph-lightbox__item--wide"><a class="morph-lightbox__thumb" href="gallery-deck-large.jpg" data-caption="Cedar deck with built-in seating · Westlake"><img src="gallery-deck.jpg" alt="Cedar deck with built-in benches at dusk" width="1200" height="600" loading="lazy"></a></li>
      <li class="morph-lightbox__item morph-lightbox__item--tall"><a class="morph-lightbox__thumb" href="gallery-stairs-large.jpg" data-caption="Stair lighting · Downtown"><img src="gallery-stairs.jpg" alt="Oak staircase with warm LED strip lighting" width="800" height="1000" loading="lazy"></a></li>
      <li class="morph-lightbox__item"><a class="morph-lightbox__thumb" href="gallery-laundry-large.jpg" data-caption="Laundry room · Riverside"><img src="gallery-laundry.jpg" alt="Laundry room with stacked machines and a deep sink" width="800" height="600" loading="lazy"></a></li>
    </ul>
  </div>

  <dialog class="morph-lightbox__dialog" aria-label="Photo viewer">
    <div class="morph-lightbox__stage">
      <figure class="morph-lightbox__figure">
        <img class="morph-lightbox__image" alt="" draggable="false">
        <figcaption class="morph-lightbox__caption"></figcaption>
      </figure>
    </div>
    <p class="morph-lightbox__count" aria-live="polite"></p>
    <button class="morph-lightbox__btn morph-lightbox__close" type="button" aria-label="Close photo viewer">
      <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
    </button>
    <button class="morph-lightbox__btn morph-lightbox__nav morph-lightbox__nav--prev" type="button" aria-label="Previous photo">
      <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="m15 18-6-6 6-6" /></svg>
    </button>
    <button class="morph-lightbox__btn morph-lightbox__nav morph-lightbox__nav--next" type="button" aria-label="Next photo">
      <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="m9 18 6-6-6-6" /></svg>
    </button>
  </dialog>
</section>
```

## CSS

```css
/* Section and heading */
.morph-lightbox { background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); }
.morph-lightbox__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.morph-lightbox__head { max-width: 40rem; margin-bottom: 2.5rem; }
.morph-lightbox__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.morph-lightbox__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.morph-lightbox__lead { margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; }

/* Grid: two columns on phones, a mosaic from 768px */
.morph-lightbox__grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); grid-auto-rows: 10rem; grid-auto-flow: dense; gap: 0.75rem; margin: 0; padding: 0; list-style: none; }
.morph-lightbox__item--tall { grid-row: span 2; }
.morph-lightbox__item--wide { grid-column: span 2; }
@media (min-width: 768px) { .morph-lightbox__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); grid-auto-rows: 13rem; gap: 1rem; } }

/* Thumbnails: zoom and an expand badge on hover */
.morph-lightbox__thumb { position: relative; display: block; height: 100%; overflow: hidden; border-radius: var(--radius-xl); background: var(--surface-muted); cursor: zoom-in; }
.morph-lightbox__thumb img { display: block; width: 100%; height: 100%; object-fit: cover; transition: transform var(--dur-5) var(--ease-out); }
.morph-lightbox__thumb::before, .morph-lightbox__thumb::after {
  content: ""; position: absolute; top: 0.75rem; right: 0.75rem; width: 2.25rem; height: 2.25rem;
  opacity: 0; transform: scale(0.8); transition: opacity var(--dur-3), transform var(--dur-4) var(--ease-spring);
}
.morph-lightbox__thumb::before { border-radius: 50%; background: var(--surface-light); box-shadow: var(--shadow-md); }
.morph-lightbox__thumb::after { /* expand icon, drawn with a mask so it takes the token colour */
  background: var(--text-main);
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7'/%3E%3C/svg%3E") center / 1rem no-repeat;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7'/%3E%3C/svg%3E") center / 1rem no-repeat;
}
@media (hover: hover) {
  .morph-lightbox__thumb:hover img { transform: scale(1.05); }
  .morph-lightbox__thumb:hover::before, .morph-lightbox__thumb:hover::after { opacity: 1; transform: none; }
}
.morph-lightbox__thumb:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Viewer */
.morph-lightbox__dialog {
  position: fixed; inset: 0; width: 100%; max-width: none; height: 100%; max-height: none; margin: 0; padding: 0;
  border: 0; background: transparent; color: var(--text-inverse); overflow: hidden;
}
.morph-lightbox__dialog::backdrop { background: color-mix(in srgb, var(--surface-deep) 92%, transparent); backdrop-filter: blur(14px); }
.morph-lightbox__stage { display: grid; place-items: center; height: 100%; padding: 4.5rem 1rem 6rem; }
.morph-lightbox__figure { display: grid; justify-items: center; gap: 1rem; margin: 0; }
.morph-lightbox__image {
  display: block; width: auto; height: auto; max-width: min(92vw, 72rem); max-height: calc(100vh - 12rem);
  border-radius: var(--radius-xl); box-shadow: 0 40px 100px -30px var(--surface-deep);
  touch-action: pan-y; user-select: none; -webkit-user-drag: none; cursor: grab;
}
.morph-lightbox__caption { color: var(--text-inverse-muted); font-size: 0.9375rem; text-align: center; }
.morph-lightbox__count { position: absolute; top: 1.5rem; left: 1.5rem; margin: 0; color: var(--text-inverse-muted); font: 500 0.875rem var(--font-mono); }

/* Round glass controls */
.morph-lightbox__btn {
  position: absolute; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse);
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.morph-lightbox__btn svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.morph-lightbox__btn:hover { background: color-mix(in srgb, var(--text-inverse) 14%, transparent); }
.morph-lightbox__btn:active { transform: scale(0.92); }
.morph-lightbox__btn:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.morph-lightbox__close { top: 1rem; right: 1rem; }
.morph-lightbox__nav { bottom: 1.5rem; }
.morph-lightbox__nav--prev { left: calc(50% - 3.25rem); }
.morph-lightbox__nav--next { right: calc(50% - 3.25rem); }
@media (min-width: 768px) {
  .morph-lightbox__nav { top: 50%; bottom: auto; translate: 0 -50%; }
  .morph-lightbox__nav--prev { left: 1.5rem; }
  .morph-lightbox__nav--next { right: 1.5rem; }
}

/* Shared-element morph (View Transitions): keep the photo's crop while it grows */
::view-transition-group(morph-lightbox-photo) { animation-duration: var(--dur-4); animation-timing-function: var(--ease-out); }
::view-transition-old(morph-lightbox-photo), ::view-transition-new(morph-lightbox-photo) { height: 100%; object-fit: cover; }

/* Fallback for browsers without View Transitions: fade and scale in */
.morph-lightbox--no-vt .morph-lightbox__dialog[open], .morph-lightbox--no-vt .morph-lightbox__dialog[open]::backdrop { transition: opacity var(--dur-3) var(--ease-out); }
.morph-lightbox--no-vt .morph-lightbox__dialog[open] .morph-lightbox__image { transition: transform var(--dur-4) var(--ease-out); }
@starting-style {
  .morph-lightbox--no-vt .morph-lightbox__dialog[open], .morph-lightbox--no-vt .morph-lightbox__dialog[open]::backdrop { opacity: 0; }
  .morph-lightbox--no-vt .morph-lightbox__dialog[open] .morph-lightbox__image { transform: scale(0.94); }
}
```

## JS

```js
document.querySelectorAll('[data-morph-lightbox]').forEach((root) => {
  const links = [...root.querySelectorAll('.morph-lightbox__thumb')];
  const dialog = root.querySelector('.morph-lightbox__dialog');
  const image = dialog.querySelector('.morph-lightbox__image');
  const caption = dialog.querySelector('.morph-lightbox__caption');
  const count = dialog.querySelector('.morph-lightbox__count');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const NAME = 'morph-lightbox-photo';
  let index = 0;
  if (!document.startViewTransition) root.classList.add('morph-lightbox--no-vt');

  const thumbAt = (i) => links[i].querySelector('img');
  // Run a DOM change inside a view transition when available
  const morph = (update) => (document.startViewTransition && !reduce.matches
    ? document.startViewTransition(update).finished
    : Promise.resolve(update()));

  // Show photo i: the loaded thumbnail first (instant), then the full-size file when ready
  const show = (i) => {
    index = (i + links.length) % links.length;
    const thumb = thumbAt(index);
    image.src = thumb.currentSrc || thumb.src;
    image.alt = thumb.alt;
    caption.textContent = links[index].dataset.caption || thumb.alt;
    count.textContent = `${index + 1} / ${links.length}`;
    const wanted = index;
    const full = new Image();
    full.onload = () => { if (index === wanted) image.src = full.src; };
    full.src = links[index].href;
  };

  const open = (i) => {
    const thumb = thumbAt(i);
    thumb.style.viewTransitionName = NAME;
    morph(() => {
      thumb.style.viewTransitionName = '';
      show(i);
      dialog.showModal();
      image.style.viewTransitionName = NAME;
    });
  };
  const close = () => {
    const thumb = thumbAt(index);
    thumb.scrollIntoView({ block: 'nearest' }); // land the morph on a visible thumbnail
    morph(() => {
      image.style.viewTransitionName = '';
      dialog.close();
      thumb.style.viewTransitionName = NAME;
    }).then(() => { thumb.style.viewTransitionName = ''; });
  };
  const step = (dir) => {
    show(index + dir);
    if (!reduce.matches) {
      image.animate([{ opacity: 0, transform: `translateX(${dir * 48}px) scale(0.98)` }, { opacity: 1, transform: 'none' }],
        { duration: 420, easing: 'cubic-bezier(0.16, 1, 0.3, 1)' });
    }
  };

  links.forEach((link, i) => link.addEventListener('click', (e) => { e.preventDefault(); open(i); }));
  dialog.querySelector('.morph-lightbox__close').addEventListener('click', close);
  dialog.querySelector('.morph-lightbox__nav--prev').addEventListener('click', () => step(-1));
  dialog.querySelector('.morph-lightbox__nav--next').addEventListener('click', () => step(1));
  dialog.addEventListener('cancel', (e) => { e.preventDefault(); close(); });
  dialog.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') step(1);
    if (e.key === 'ArrowLeft') step(-1);
  });
  dialog.addEventListener('click', (e) => { if (e.target === dialog || e.target.classList.contains('morph-lightbox__stage')) close(); });

  // Swipe: the photo follows the finger, then commits or springs back
  let startX = null;
  image.addEventListener('pointerdown', (e) => { startX = e.clientX; image.setPointerCapture(e.pointerId); });
  image.addEventListener('pointermove', (e) => { if (startX !== null) image.style.translate = `${(e.clientX - startX) * 0.6}px 0`; });
  const endSwipe = (e) => {
    if (startX === null) return;
    const dx = e.clientX - startX;
    startX = null;
    image.style.translate = '';
    if (Math.abs(dx) > 60) step(dx < 0 ? 1 : -1);
  };
  image.addEventListener('pointerup', endSwipe);
  image.addEventListener('pointercancel', endSwipe);
});
```

## Notes

- Without JS, each thumbnail is a normal link to the full-size image. The `href` is also what the viewer upgrades to, so point it at your large file.
- The viewer is a modal `<dialog>`: focus is trapped, Escape closes with the morph back, and the photo count is announced through a polite live region. Arrow keys and buttons navigate.
- Shared-element morphs need View Transitions (Chromium, Safari 18+, Firefox 144+). Elsewhere the viewer fades and scales in. Under reduced motion it opens instantly.
- `object-fit: cover` on the transition snapshots keeps the photo's crop while the thumbnail (cropped) grows into the viewer (uncropped), so nothing squashes.
- Only one element may hold the `morph-lightbox-photo` name at a time; the script hands it between thumbnail and viewer. If you have two galleries on a page, give each its own name.
- Alt text describes each photo; the caption adds project and place.
