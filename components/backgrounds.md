# Backgrounds

Decorative section backgrounds, from pure-CSS gradients and patterns to photo and video layers under contrast-safe scrims. Depends on `tokens/variables.css`.

| #  | Pattern                                                               | JS        |
| -- | --------------------------------------------------------------------- | --------- |
| 1  | **Gradient mesh**: layered token glows mixed with `color-mix()`       | none      |
| 2  | **Animated gradient**: slow pastel pan with a pause button            | ~9 lines  |
| 3  | **Dot grid**: repeating dots from one `radial-gradient` tile          | none      |
| 4  | **Line grid with fade**: square grid that fades out toward the edges  | none      |
| 5  | **Grain overlay**: subtle SVG film grain for any background           | none      |
| 6  | **Aurora blobs**: blurred, drifting color blobs with a pause button   | ~9 lines  |
| 7  | **Image with scrim**: real `<img>` under a scrim for inverse text     | none      |
| 8  | **Section dividers**: wave, curve and angle edges between sections    | none      |
| 9  | **Video background**: muted loop under a scrim, with play/pause       | ~17 lines |

## 1. Gradient mesh

Four soft glows mixed from `--primary` and `--accent` with `color-mix()`, layered over a flat base. Pure CSS, so it scales with the section at any width. Add `bgfx-mesh--dark` for an inverted band.

### HTML

```html
<section class="bgfx-mesh">
  <div class="bgfx-mesh__inner">
    <h2>Home repairs, done right the first time</h2>
    <p>Licensed Springfield crews, upfront pricing and a 5-year workmanship warranty.</p>
  </div>
</section>
```

### CSS

```css
/* Mesh: one glow per corner over a flat base; --bgfx-mesh-mix sets their strength */
.bgfx-mesh {
  --bgfx-mesh-mix: 22%;
  padding-block: var(--space-2xl);
  color: var(--text-main);
  background-color: var(--surface-light); /* also the fallback without color-mix() */
  background-image:
    radial-gradient(at 0% 0%, color-mix(in srgb, var(--primary) var(--bgfx-mesh-mix), transparent), transparent 55%),
    radial-gradient(at 100% 0%, color-mix(in srgb, var(--accent) var(--bgfx-mesh-mix), transparent), transparent 50%),
    radial-gradient(at 100% 100%, color-mix(in srgb, var(--primary-hover) var(--bgfx-mesh-mix), transparent), transparent 55%),
    radial-gradient(at 0% 100%, color-mix(in srgb, color-mix(in oklch, var(--primary), var(--accent)) var(--bgfx-mesh-mix), transparent), transparent 50%);
}

/* Dark band: stronger glows on --surface-dark */
.bgfx-mesh--dark { --bgfx-mesh-mix: 35%; color: var(--text-inverse); background-color: var(--surface-dark); }

.bgfx-mesh__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
```

### Notes

- `--text-main` stays above 8:1 even where glows overlap, but `--text-muted` drops below 4.5:1 on a 22% glow, so keep copy `--text-main`. On `--dark`, use `--text-inverse` only; `--text-inverse-muted` fails over the amber glow.
- `color-mix()`: Chrome 111, Safari 16.2, Firefox 113. Without it the gradient layer is dropped and the flat `background-color` shows.
- The fourth glow mixes the two brand tokens in `oklch`, which gives a clean in-between hue instead of the muddy gray an `srgb` mix of blue and amber produces.
- Stack 5. Grain overlay on top with `class="bgfx-mesh bgfx-grain"`.

## 2. Animated gradient

A pastel gradient pans back and forth over 20s. It moves only when JS runs and the visitor allows motion, and a pause button (WCAG 2.2.2) appears with it. Otherwise the gradient stays still and the button stays hidden.

### HTML

```html
<section class="bgfx-shift">
  <div class="bgfx-shift__inner">
    <h2>Spring tune-up season is here</h2>
    <p>Book your AC check before the first heat wave and skip the summer wait list.</p>
  </div>
  <button class="bgfx-shift__toggle" type="button" aria-label="Pause background animation">
    <svg class="bgfx-shift__icon bgfx-shift__icon--pause" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M9 5v14M15 5v14" /></svg>
    <svg class="bgfx-shift__icon bgfx-shift__icon--play" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M7 4v16l13-8z" /></svg>
  </button>
</section>
```

### CSS

```css
/* Animated gradient: light token tints on a 3x-wide canvas so it can pan */
.bgfx-shift {
  position: relative;
  padding-block: var(--space-2xl) calc(var(--space-2xl) + var(--space-lg)); /* room for the button */
  color: var(--text-main);
  background-color: var(--surface-muted);
  background-image: linear-gradient(120deg,
    color-mix(in srgb, var(--primary) 18%, var(--surface-light)),
    color-mix(in srgb, var(--accent) 22%, var(--surface-light)),
    var(--surface-muted),
    color-mix(in srgb, var(--primary) 12%, var(--surface-light)));
  background-size: 300% 300%;
}
.bgfx-shift__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }

/* Pause/play button: hidden until JS starts the animation; light-surface focus ring */
.bgfx-shift__toggle {
  display: none; position: absolute; inset-block-end: var(--space-md); inset-inline-end: var(--space-md);
  place-items: center; width: 2.75rem; height: 2.75rem; padding: 0;
  border: 1px solid var(--text-muted); border-radius: var(--radius-full);
  background-color: var(--surface-light); color: var(--text-main); cursor: pointer;
  transition: background-color var(--transition-fast);
}
.bgfx-shift__toggle:hover { background-color: color-mix(in srgb, var(--primary) 8%, var(--surface-light)); }
.bgfx-shift__toggle:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.bgfx-shift__icon { width: 1.25rem; height: 1.25rem; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.bgfx-shift__icon--play,
.bgfx-shift--paused .bgfx-shift__icon--pause { display: none; }
.bgfx-shift--paused .bgfx-shift__icon--play { display: block; }

/* Motion: only with JS (.bgfx-shift--ready) and no reduced-motion preference */
@keyframes bgfx-shift-pan {
  from { background-position: 0% 50%; }
  to { background-position: 100% 50%; }
}
@media (prefers-reduced-motion: no-preference) {
  .bgfx-shift--ready { animation: bgfx-shift-pan 20s ease-in-out infinite alternate; }
  .bgfx-shift--ready .bgfx-shift__toggle { display: grid; }
  .bgfx-shift--paused { animation-play-state: paused; }
}
```

### JS

```js
// Animated gradient: start the pan, and show its pause button, only when JS runs and motion is allowed
document.querySelectorAll('.bgfx-shift').forEach((el) => {
  const btn = el.querySelector('.bgfx-shift__toggle');
  if (!btn || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  el.classList.add('bgfx-shift--ready');
  btn.addEventListener('click', () => {
    const paused = el.classList.toggle('bgfx-shift--paused');
    btn.setAttribute('aria-label', paused ? 'Play background animation' : 'Pause background animation');
  });
});
```

### Notes

- The pause button is the safer option. The pan never ends, so WCAG 2.2.2's 5-second rule applies even though the change is soft and decorative. With no JS or with reduced motion nothing moves, so there's no button either.
- Every stop is a light tint, so `--text-main` stays above 10:1. `--text-muted` falls to about 3.7:1 on the blue stop.
- `background-position` animations repaint every frame. Use one per page; on heavy pages, pan an oversized `::before` with `transform` instead.

## 3. Dot grid

A repeating dot pattern drawn by one `radial-gradient` tile. It's a plain background, so assistive tech and pointer events never see it.

### HTML

```html
<section class="bgfx-dots">
  <div class="bgfx-dots__inner">
    <h2>How we price every job</h2>
    <p>One flat quote after a free visit. No hourly surprises, no hidden fees.</p>
  </div>
</section>
```

### CSS

```css
/* Dot grid: one dot per tile; --bgfx-dots-gap sets density, --bgfx-dots-color the tint */
.bgfx-dots {
  --bgfx-dots-gap: var(--space-lg);
  --bgfx-dots-color: color-mix(in srgb, var(--text-muted) 35%, transparent);
  padding-block: var(--space-2xl);
  color: var(--text-main);
  background-color: var(--surface-muted);
  background-image: radial-gradient(circle, var(--bgfx-dots-color) 1px, transparent 1.5px);
  background-size: var(--bgfx-dots-gap) var(--bgfx-dots-gap);
  background-position: center;
}
.bgfx-dots__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
```

### Notes

- Keep copy `--text-main`. Where a glyph crosses a dot, `--text-muted` can fall under 4.5:1.
- The `1px` solid stop plus a `1.5px` fade keeps each dot round and anti-aliased at any zoom. `background-position: center` keeps the pattern symmetric at every width.
- For a dark band, set `background-color: var(--surface-dark)` and mix the dots from `--text-inverse-muted` at about 25%.

## 4. Line grid with fade

Square grid lines on a `::before` layer, faded toward the edges with a radial `mask-image`. The layer sits behind content (`isolation: isolate` + `z-index: -1`) and ignores pointer events.

### HTML

```html
<section class="bgfx-grid">
  <div class="bgfx-grid__inner">
    <h2>Plan your remodel with us</h2>
    <p>We draw the layout, pull the permits and schedule every trade on site.</p>
  </div>
</section>
```

### CSS

```css
/* Line grid host: isolation keeps the z-index:-1 layer above the background, below content */
.bgfx-grid {
  --bgfx-grid-size: var(--space-2xl);
  --bgfx-grid-line: var(--border-subtle);
  position: relative; isolation: isolate;
  padding-block: var(--space-2xl);
  color: var(--text-main);
  background-color: var(--surface-light);
}
/* Grid lines: one vertical and one horizontal 1px line per tile, faded by a radial mask */
.bgfx-grid::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background-image:
    linear-gradient(to right, var(--bgfx-grid-line) 1px, transparent 1px),
    linear-gradient(to bottom, var(--bgfx-grid-line) 1px, transparent 1px);
  background-size: var(--bgfx-grid-size) var(--bgfx-grid-size);
  background-position: center;
  /* Masks read alpha only, so any opaque token works as the "solid" color */
  -webkit-mask-image: radial-gradient(ellipse at center, var(--surface-dark) 30%, transparent 75%);
  mask-image: radial-gradient(ellipse at center, var(--surface-dark) 30%, transparent 75%);
}
.bgfx-grid__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
```

### Notes

- `mask-image` is unprefixed in Chrome 120, Safari 15.4 and Firefox 53; `-webkit-mask-image` covers older Chromium. Without mask support the grid runs edge to edge, which still looks fine.
- Move the bright spot with the mask position, e.g. `ellipse at 50% 0%` for a grid that glows behind the heading.
- Lines use `--border-subtle`, so copy keeps full `--text-main` contrast. For a bolder grid, mix `--primary` into `--bgfx-grid-line` at 15–20%.

## 5. Grain overlay

Grayscale SVG noise on `::before` at low opacity, behind content. Color-agnostic: use it on its own with `bgfx-grain--dark`, or stack it on another background.

### HTML

```html
<section class="bgfx-grain bgfx-grain--dark">
  <div class="bgfx-grain__inner">
    <h2>Craftsmanship you can feel</h2>
    <p>Hand-finished trim, cabinets and built-ins from our Springfield workshop.</p>
  </div>
</section>
```

### CSS

```css
/* Grain host: sets no colors, so it can sit on top of any other background class */
.bgfx-grain {
  --bgfx-grain-opacity: 0.15;
  position: relative; isolation: isolate;
}
/* Noise tile: feTurbulence, desaturated, so it only lightens or darkens the base */
.bgfx-grain::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  opacity: var(--bgfx-grain-opacity);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E");
}

/* Standalone band; skip it when stacking on another background */
.bgfx-grain--dark { color: var(--text-inverse); background-color: var(--surface-dark); }
.bgfx-grain__inner {
  max-width: var(--container-max); margin-inline: auto;
  padding: var(--space-2xl) var(--gutter);
}
```

### Notes

- Stack it on 1, 2 or 3 (`class="bgfx-mesh bgfx-grain"`), which leave `::before` free. Patterns 4, 6, 7 and 9 already use `::before`.
- On `--surface-dark` both inverse text tokens still pass. On light bases the grain darkens pixels slightly, so use `--text-main` there, not `--text-muted`.
- The data URI holds no colors, only filter output, and the tile is rasterized once and cached. Keep `--bgfx-grain-opacity` at 0.2 or below.

## 6. Aurora blobs

Two blurred color blobs drift slowly on a dark band, clipped to the section. The drift runs only when JS runs and the visitor allows motion, with a pause button (WCAG 2.2.2); otherwise the blobs stay still.

### HTML

```html
<section class="bgfx-aurora">
  <div class="bgfx-aurora__inner">
    <h2>Smart-home upgrades, installed in a day</h2>
    <p>EV chargers, panel upgrades and whole-home Wi-Fi, wired by licensed electricians.</p>
  </div>
  <button class="bgfx-aurora__toggle" type="button" aria-label="Pause background animation">
    <svg class="bgfx-aurora__icon bgfx-aurora__icon--pause" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M9 5v14M15 5v14" /></svg>
    <svg class="bgfx-aurora__icon bgfx-aurora__icon--play" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M7 4v16l13-8z" /></svg>
  </button>
</section>
```

### CSS

```css
/* Aurora band: clip keeps blurred blobs inside without creating a scroll container */
.bgfx-aurora {
  --bgfx-aurora-blur: 4rem;
  position: relative; isolation: isolate;
  overflow: hidden; overflow: clip;
  padding-block: var(--space-2xl) calc(var(--space-2xl) + var(--space-lg)); /* room for the button */
  color: var(--text-inverse);
  background-color: var(--surface-dark);
}
/* Blobs: blurred circles behind content; alphas capped so --text-inverse stays above 5:1 */
.bgfx-aurora::before,
.bgfx-aurora::after {
  content: ""; position: absolute; z-index: -1; pointer-events: none;
  width: min(40rem, 90%); aspect-ratio: 1; border-radius: var(--radius-full);
  filter: blur(var(--bgfx-aurora-blur));
}
.bgfx-aurora::before {
  --bgfx-aurora-x: 25%; --bgfx-aurora-y: 15%;
  top: -40%; left: -20%;
  background-color: color-mix(in srgb, var(--primary) 55%, transparent);
}
.bgfx-aurora::after {
  --bgfx-aurora-x: -25%; --bgfx-aurora-y: -10%;
  bottom: -45%; right: -20%;
  background-color: color-mix(in srgb, var(--accent) 35%, transparent);
}
.bgfx-aurora__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }

/* Pause/play button: hidden until JS starts the drift; dark-surface focus outline */
.bgfx-aurora__toggle {
  display: none; position: absolute; inset-block-end: var(--space-md); inset-inline-end: var(--space-md);
  place-items: center; width: 2.75rem; height: 2.75rem; padding: 0;
  border: 1px solid var(--text-inverse-muted); border-radius: var(--radius-full);
  background-color: var(--surface-dark); color: var(--text-inverse); cursor: pointer;
  transition: border-color var(--transition-fast);
}
.bgfx-aurora__toggle:hover { border-color: var(--text-inverse); }
.bgfx-aurora__toggle:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }
.bgfx-aurora__icon { width: 1.25rem; height: 1.25rem; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.bgfx-aurora__icon--play,
.bgfx-aurora--paused .bgfx-aurora__icon--pause { display: none; }
.bgfx-aurora--paused .bgfx-aurora__icon--play { display: block; }

/* Drift: transform only, and only with JS (.bgfx-aurora--ready) and no reduced-motion preference */
@keyframes bgfx-aurora-drift {
  to { transform: translate(var(--bgfx-aurora-x), var(--bgfx-aurora-y)) scale(1.2); }
}
@media (prefers-reduced-motion: no-preference) {
  .bgfx-aurora--ready::before,
  .bgfx-aurora--ready::after { animation: bgfx-aurora-drift 18s ease-in-out infinite alternate; will-change: transform; }
  .bgfx-aurora--ready::after { animation-duration: 24s; }
  .bgfx-aurora--paused::before,
  .bgfx-aurora--paused::after { animation-play-state: paused; }
  .bgfx-aurora--ready .bgfx-aurora__toggle { display: grid; }
}
```

### JS

```js
// Aurora: start the drift, and show its pause button, only when JS runs and motion is allowed
document.querySelectorAll('.bgfx-aurora').forEach((el) => {
  const btn = el.querySelector('.bgfx-aurora__toggle');
  if (!btn || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  el.classList.add('bgfx-aurora--ready');
  btn.addEventListener('click', () => {
    const paused = el.classList.toggle('bgfx-aurora--paused');
    btn.setAttribute('aria-label', paused ? 'Play background animation' : 'Pause background animation');
  });
});
```

### Notes

- Only `transform` animates. `will-change` promotes each blurred blob once, so frames are composited rather than re-blurred. Never animate `filter` or the blob color.
- Blob alphas (55% / 35%) keep `--text-inverse` above 5:1 even where the blobs overlap. Don't use `--text-inverse-muted` here.
- `overflow: clip`: Chrome 90, Safari 16, Firefox 81; older browsers fall back to `overflow: hidden`. Unlike `hidden`, `clip` doesn't break `position: sticky` inside the section.
- The drift is gated on JS because the pause button needs JS. Without it, the blobs render as a static glow.

## 7. Image with scrim

A real `<img>` fills the section behind a dark scrim, so `--text-inverse` copy reads over any photo. The image keeps its alt text, `srcset`, lazy loading and LCP priority, which a CSS `background-image` can't.

### HTML

```html
<section class="bgfx-scrim">
  <img class="bgfx-scrim__img" src="roof-crew-1600.jpg" alt=""
       srcset="roof-crew-800.jpg 800w, roof-crew-1600.jpg 1600w" sizes="100vw"
       width="1600" height="900" loading="lazy" decoding="async">
  <div class="bgfx-scrim__inner">
    <h2>Roofs built for Springfield winters</h2>
    <p>Ice-and-water shield on every job, backed by a 10-year leak warranty.</p>
  </div>
</section>
```

### CSS

```css
/* Scrim host: photo and scrim stack behind content in the isolated section */
.bgfx-scrim {
  position: relative; isolation: isolate;
  padding-block: calc(var(--space-2xl) * 2);
  color: var(--text-inverse);
  background-color: var(--surface-dark); /* shows while the photo loads, and if it fails */
}
/* Photo at 35% over --surface-dark = a 65% scrim floor: --text-inverse stays above 5:1 over any pixel */
.bgfx-scrim__img {
  position: absolute; inset: 0; z-index: -2;
  width: 100%; height: 100%; object-fit: cover; opacity: 0.35; pointer-events: none;
}
/* Gradient scrim: deepens the lower part, where copy usually sits */
.bgfx-scrim::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: linear-gradient(to top, var(--surface-dark), transparent 70%);
  opacity: 0.8;
}
.bgfx-scrim__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
```

### Notes

- As the hero, drop `loading="lazy"` and add `fetchpriority="high"`. An `<img>` is found by the preload scanner; a CSS background isn't.
- Use `alt=""` when the photo only sets the mood. Write real alt text when it shows the work.
- The 65% floor holds `--text-inverse` at about 5.3:1 even over pure white, with no `color-mix()` to fall back from. Don't raise the image `opacity` above 0.35, and don't use `--text-inverse-muted` here.

## 8. Section dividers

Wave, curve and angle edges between sections of different colors. An inline SVG in the section's extra bottom padding fills with the next section's color through `currentColor` and stretches to any width. It's `aria-hidden`, so screen readers get plain sections.

### HTML

```html
<!-- Wave: dark section into a muted one -->
<section class="bgfx-divider bgfx-divider--dark" style="--bgfx-divider-next: var(--surface-muted)">
  <div class="bgfx-divider__inner">
    <h2>Storm damage? We're on call.</h2>
    <p>Emergency roof tarping anywhere in Springfield, day or night.</p>
  </div>
  <svg class="bgfx-divider__shape" viewBox="0 0 1200 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
    <path d="M0 48c200 48 400 48 600 0s400-48 600 0v72H0z" />
  </svg>
</section>

<!-- Curve: muted section into a --primary one -->
<section class="bgfx-divider" style="--bgfx-divider-next: var(--primary)">
  <div class="bgfx-divider__inner">
    <h2>Free estimates, same week</h2>
    <p>Tell us about the job and we'll visit with a written quote.</p>
  </div>
  <svg class="bgfx-divider__shape" viewBox="0 0 1200 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
    <path d="M0 0q600 160 1200 0v120H0z" />
  </svg>
</section>

<!-- Angle: --primary section into the light page background -->
<section class="bgfx-divider bgfx-divider--primary" style="--bgfx-divider-next: var(--surface-light)">
  <div class="bgfx-divider__inner">
    <h2>Licensed, bonded and insured</h2>
    <p>Every Brand crew is background-checked and covered on every Springfield job.</p>
  </div>
  <svg class="bgfx-divider__shape" viewBox="0 0 1200 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
    <path d="M0 120 1200 0v120z" />
  </svg>
</section>
```

### CSS

```css
/* Divider host: extra bottom padding holds the shape, so it never overlaps text */
.bgfx-divider {
  --bgfx-divider-h: var(--space-2xl);
  position: relative; isolation: isolate;
  padding-block: var(--space-2xl) calc(var(--space-2xl) + var(--bgfx-divider-h));
  color: var(--text-main);
  background-color: var(--surface-muted);
}
.bgfx-divider--dark { color: var(--text-inverse); background-color: var(--surface-dark); }
.bgfx-divider--primary { color: var(--text-inverse); background-color: var(--primary); }
.bgfx-divider__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }

/* Shape in the NEXT section's color; bottom -1px + 1px extra height overlaps the seam */
.bgfx-divider__shape {
  position: absolute; inset-inline: 0; bottom: -1px; z-index: -1;
  display: block; width: 100%; height: calc(var(--bgfx-divider-h) + 1px);
  color: var(--bgfx-divider-next, var(--surface-light)); fill: currentColor; pointer-events: none;
}

/* Taller edge on wider screens */
@media (min-width: 768px) {
  .bgfx-divider { --bgfx-divider-h: calc(var(--space-2xl) * 2); }
}
```

### Notes

- Set `--bgfx-divider-next` to the following section's background token. The SVG fills with it through `currentColor`, so the colors match exactly.
- Seam trick: the SVG sits at `bottom: -1px` and is 1px taller than the edge, so it overlaps the next section. Sub-pixel rounding at odd zoom levels can't leave a hairline, and `display: block` removes the inline-SVG baseline gap.
- `clip-path: polygon()` also works for the angle, but then the next section must be pulled up underneath with a negative margin. The SVG keeps sections independent.
- Flip a shape with `transform: scaleX(-1)` on the SVG.

## 9. Video background

A muted, looping video behind a scrim, with a visible play/pause button (WCAG 2.2.2). JS starts playback only when motion is allowed; otherwise the poster shows. Without JS the video never plays and the button stays hidden.

### HTML

```html
<section class="bgfx-video">
  <video class="bgfx-video__media" muted playsinline loop preload="none"
         poster="crew-poster.jpg" width="1280" height="720" aria-hidden="true">
    <source src="crew-loop.webm" type="video/webm">
    <source src="crew-loop.mp4" type="video/mp4">
  </video>
  <div class="bgfx-video__inner">
    <h2>From quote to clean-up in one visit</h2>
    <p>Our crews arrive on time, protect your floors and leave the site spotless.</p>
  </div>
  <button class="bgfx-video__toggle" type="button" aria-label="Play background video">
    <svg class="bgfx-video__icon bgfx-video__icon--play" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M7 4v16l13-8z" /></svg>
    <svg class="bgfx-video__icon bgfx-video__icon--pause" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M9 5v14M15 5v14" /></svg>
  </button>
</section>
```

### CSS

```css
/* Video host: video and scrim stack behind content in the isolated section */
.bgfx-video {
  position: relative; isolation: isolate;
  padding-block: calc(var(--space-2xl) * 2);
  color: var(--text-inverse);
  background-color: var(--surface-dark);
}
/* Video (and poster) at 35% over --surface-dark = a 65% scrim floor: --text-inverse stays above 5:1 */
.bgfx-video__media {
  position: absolute; inset: 0; z-index: -2;
  width: 100%; height: 100%; object-fit: cover; opacity: 0.35; pointer-events: none;
}
/* Gradient scrim: deepens the lower part, where copy and the button sit */
.bgfx-video::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: linear-gradient(to top, var(--surface-dark), transparent 70%);
  opacity: 0.8;
}
.bgfx-video__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }

/* Play/pause button: shown once JS controls playback; dark-surface focus outline */
.bgfx-video__toggle {
  display: none; position: absolute; inset-block-end: var(--space-md); inset-inline-end: var(--space-md);
  place-items: center; width: 2.75rem; height: 2.75rem; padding: 0;
  border: 1px solid var(--text-inverse-muted); border-radius: var(--radius-full);
  background-color: var(--surface-dark); color: var(--text-inverse); cursor: pointer;
  transition: border-color var(--transition-fast);
}
.bgfx-video--ready .bgfx-video__toggle { display: grid; }
.bgfx-video__toggle:hover { border-color: var(--text-inverse); }
.bgfx-video__toggle:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }
.bgfx-video__icon { width: 1.25rem; height: 1.25rem; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.bgfx-video__icon--pause,
.bgfx-video--playing .bgfx-video__icon--play { display: none; }
.bgfx-video--playing .bgfx-video__icon--pause { display: block; }
```

### JS

```js
// Video background: JS owns playback (no autoplay attribute), so reduced motion keeps the poster
document.querySelectorAll('.bgfx-video').forEach((el) => {
  const video = el.querySelector('.bgfx-video__media');
  const btn = el.querySelector('.bgfx-video__toggle');
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  // Label and icon always mirror the real playback state
  const sync = () => {
    el.classList.toggle('bgfx-video--playing', !video.paused);
    btn.setAttribute('aria-label', video.paused ? 'Play background video' : 'Pause background video');
  };
  const play = () => video.play().catch(sync); // a blocked autoplay just leaves the poster
  video.addEventListener('play', sync);
  video.addEventListener('pause', sync);
  btn.addEventListener('click', () => (video.paused ? play() : video.pause()));
  motion.addEventListener('change', () => motion.matches && video.pause());
  el.classList.add('bgfx-video--ready');
  sync();
  if (!motion.matches && !navigator.connection?.saveData) play();
});
```

### Notes

- No `autoplay` attribute: JS starts playback only without reduced motion or Save-Data, and switching to reduced motion mid-visit pauses it. `preload="none"` spares those visitors the download; the button still lets them play it.
- The label follows the video's own `play`/`pause` events, so a blocked autoplay (e.g. iOS Low Power Mode) still reads "Play background video".
- The video is `aria-hidden` and decorative. Ship it without an audio track, keep the loop short (about 10s, under 2 MB) and put everything important in the text.
- Above the fold the poster is often the LCP element: keep it small and preload it.
- **React:** React doesn't reliably set the `muted` attribute, so set `ref.current.muted = true` before calling `play()`, or Safari refuses to start it.
