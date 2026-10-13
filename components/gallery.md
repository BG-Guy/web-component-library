# Gallery

Project photos and before/after comparisons. Depends on `tokens/variables.css`. Place inside your page container.

- **A. Project grid:** captioned thumbnails linking to full-size images. 1 column on phones, 3 on tablets, 4 at `--container-max`. No JS.
- **B. Before/after slider:** two stacked photos with a draggable divider. A native range input drives it, so keyboard and touch work out of the box. Without JS it shows a 50/50 split.

## HTML

### A. Project grid

```html
<ul class="gallery" role="list">
  <li>
    <figure class="gallery__item">
      <a href="deck-large.jpg">
        <img src="deck.jpg" alt="Cedar deck with built-in bench seating" width="800" height="600" loading="lazy">
      </a>
      <figcaption>Cedar deck · Northside</figcaption>
    </figure>
  </li>
  <!-- repeat per project -->
</ul>
```

### B. Before/after slider

Keep the range input directly before the handle, so the handle can show the input's focus ring.

```html
<figure class="compare" style="--pos: 50%">
  <div class="compare__media">
    <img src="kitchen-before.jpg" alt="Before: kitchen with dated oak cabinets and cracked tile"
         width="1200" height="800" loading="lazy">
    <img class="compare__after" src="kitchen-after.jpg" alt="After: the same kitchen with white shaker cabinets and a new tile floor"
         width="1200" height="800" loading="lazy">
    <span class="compare__tag compare__tag--before" aria-hidden="true">Before</span>
    <span class="compare__tag compare__tag--after" aria-hidden="true">After</span>
    <input class="compare__range" type="range" min="0" max="100" value="50" aria-label="Before and after divider">
    <span class="compare__handle" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="24" height="24" focusable="false"><path d="M9 6 3 12l6 6M15 6l6 6-6 6" /></svg>
    </span>
  </div>
  <figcaption class="compare__caption">Kitchen remodel · Westlake</figcaption>
</figure>
```

## CSS

```css
/* A. Project grid: auto-fill keeps tile size consistent however many projects there are */
.gallery {
  display: grid; gap: var(--space-md);
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 14rem), 1fr));
  margin: 0; padding: 0; list-style: none;
}
.gallery__item { margin: 0; }
.gallery__item a { display: block; overflow: hidden; border-radius: var(--radius-md); background: var(--border-subtle); }
.gallery__item img {
  display: block; width: 100%; height: auto; aspect-ratio: 4 / 3; object-fit: cover;
  transition: transform var(--transition-smooth);
}
.gallery__item a:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.gallery__item figcaption { margin-top: var(--space-xs); font-size: 0.875rem; color: var(--text-muted); }
@media (hover: hover) {
  .gallery__item a:hover img { transform: scale(1.04); }
}

/* B. Before/after: both images fill the frame; the "after" image is clipped from the left at --pos */
.compare { margin: 0; }
.compare__media {
  --thumb: 2.75rem; /* grip size and touch target */
  position: relative; overflow: hidden; aspect-ratio: 3 / 2;
  border-radius: var(--radius-lg); background: var(--border-subtle);
}
.compare__media img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.compare__after { clip-path: inset(0 0 0 var(--pos)); }

/* Corner labels */
.compare__tag {
  position: absolute; top: var(--space-sm); pointer-events: none;
  padding: var(--space-xs) var(--space-sm); border-radius: var(--radius-sm);
  background: color-mix(in srgb, var(--surface-dark) 70%, transparent); color: var(--text-inverse);
  font-size: 0.75rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;
}
.compare__tag--before { left: var(--space-sm); }
.compare__tag--after { right: var(--space-sm); }

/* Invisible range input over the image. It's one thumb wider than the frame,
   so the thumb's center lines up with --pos at every value. */
.compare__range {
  position: absolute; top: 0; left: calc(var(--thumb) / -2);
  width: calc(100% + var(--thumb)); height: 100%; margin: 0;
  -webkit-appearance: none; appearance: none; background: transparent;
  opacity: 0; cursor: ew-resize;
}
/* Full-height thumb: the whole divider line is a grab strip (iOS only drags by the thumb) */
.compare__range::-webkit-slider-thumb { -webkit-appearance: none; width: var(--thumb); height: 100vh; }
.compare__range::-moz-range-thumb { width: var(--thumb); height: 100vh; border: 0; }

/* Visible divider and round grip, positioned at --pos */
.compare__handle {
  position: absolute; top: 0; bottom: 0; left: var(--pos); width: 2px; translate: -50% 0;
  background: var(--surface-light); pointer-events: none;
}
.compare__handle svg {
  position: absolute; top: 50%; left: 50%; translate: -50% -50%;
  box-sizing: border-box; width: var(--thumb); height: var(--thumb); padding: 0.625rem;
  border-radius: var(--radius-full); background: var(--surface-light); color: var(--text-main);
  box-shadow: var(--shadow-md);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.compare__range:focus-visible + .compare__handle svg { box-shadow: var(--shadow-md), var(--focus-ring); }
.compare__caption { margin-top: var(--space-sm); font-size: 0.875rem; color: var(--text-muted); }
```

## JS

```js
document.querySelectorAll('.compare').forEach((el) => {
  const range = el.querySelector('.compare__range');
  const sync = () => el.style.setProperty('--pos', `${range.value}%`);
  sync(); // also covers a value restored by the browser on back navigation
  range.addEventListener('input', sync);
});
```

## Notes

- Alt text describes what the photo shows (the finished work), not "image 1". Captions add the project and place; don't repeat the alt.
- Every gallery image gets `loading="lazy"` and `width`/`height` to prevent layout shift.
- The slider is a visual extra: both images keep full alt text, and the range is keyboard-operable (arrow keys, Home/End).
- Before/after photos need the same framing and aspect ratio, or the comparison jumps at the divider.
- For a lightbox, open the full-size image in a `components/modals.md` dialog. Keep the `href`, so the link still works without JS.
- **React:** keep the range uncontrolled or in state, and set `style={{ '--pos': `${pos}%` }}` on the figure.
- **Tailwind (v4):** grid `grid grid-cols-[repeat(auto-fill,minmax(min(100%,14rem),1fr))] gap-4`. Keep the slider CSS as-is; vendor thumb pseudo-elements don't map to utilities.
