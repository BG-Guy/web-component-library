# Transitions & Effects

Motion effects for page navigation, links, cards and buttons, each with a reduced-motion fallback. Depends on `tokens/variables.css`.

| #  | Pattern                                                                                        | JS        |
| -- | ---------------------------------------------------------------------------------------------- | --------- |
| 1  | **Page transitions**: pages crossfade under a persistent header, plus an in-page swap helper   | ~18 lines |
| 2  | **Underline slide link**: underline grows from the left, across wrapped lines                  | none      |
| 3  | **Image zoom reveal**: photo zooms and a caption on a scrim fades in                           | none      |
| 4  | **Flip card**: 3D flip on hover, pinned by a toggle button                                     | ~10 lines |
| 5  | **Crossfade panels**: a radio segmented control crossfades stacked panels                      | none      |
| 6  | **Ripple effect**: ripple from the pointer, or from the center for keyboard clicks             | ~13 lines |
| 7  | **Tilt card**: subtle 3D tilt and glare that follow the mouse                                  | ~14 lines |

## 1. Page transitions

Same-origin page loads crossfade while the main content slides up slightly; the header is matched across pages and stays put. A small helper gives in-page content swaps the same treatment. Unsupported browsers and reduced-motion users get plain navigation and instant swaps.

### HTML

```html
<!-- Every page: the class on <html> scopes the transition styles -->
<html lang="en" class="fx-page">
  <body>
    <header class="fx-page__header"><!-- your site header --></header>
    <main class="fx-page__main" id="main">
      <!-- page content -->

      <!-- Same-document swap: without JS both panels show and the toggle stays hidden -->
      <div class="fx-page__region" id="fx-page-pricing" aria-live="polite">
        <div class="fx-page__panel">
          <h2 class="fx-page__title">Residential pricing</h2>
          <p class="fx-page__text">Service calls from $89, with no weekend surcharge.</p>
        </div>
        <div class="fx-page__panel">
          <h2 class="fx-page__title">Commercial pricing</h2>
          <p class="fx-page__text">Quoted per site, with priority response for contract customers.</p>
        </div>
      </div>
      <button class="fx-page__toggle" type="button" aria-controls="fx-page-pricing" aria-pressed="false" hidden>
        Show commercial pricing
      </button>
    </main>
  </body>
</html>
```

### CSS

```css
/* Opt in on every page (old and new both need it). Skipped under reduced motion. */
@media (prefers-reduced-motion: no-preference) {
  @view-transition { navigation: auto; types: fx-nav; }
}

/* Named parts: the header is matched across pages; main animates separately */
.fx-page__header { view-transition-name: fx-page-header; }
.fx-page__main { view-transition-name: fx-page-main; }

@media (prefers-reduced-motion: no-preference) {
  /* Header persists: no fade, and it stays above the sliding content */
  .fx-page::view-transition-group(fx-page-header) { z-index: 1; }
  .fx-page::view-transition-old(fx-page-header),
  .fx-page::view-transition-new(fx-page-header) { animation: none; mix-blend-mode: normal; }

  /* Main crossfades and slides, on page navigations only (the fx-nav type) */
  .fx-page:active-view-transition-type(fx-nav)::view-transition-old(fx-page-main) { animation: fx-page-out 160ms ease-in both; }
  .fx-page:active-view-transition-type(fx-nav)::view-transition-new(fx-page-main) { animation: fx-page-in 280ms ease-out both; }

  /* Same-document swaps: the helper names the changing region while it swaps */
  .fx-page::view-transition-old(fx-page-region) { animation: fx-page-out 160ms ease-in both; }
  .fx-page::view-transition-new(fx-page-region) { animation: fx-page-in 280ms ease-out both; }
}
@keyframes fx-page-out { to { opacity: 0; transform: translateY(calc(-1 * var(--space-sm))); } }
@keyframes fx-page-in { from { opacity: 0; transform: translateY(var(--space-md)); } }

/* Demo region and toggle for the same-document helper */
.fx-page__region {
  display: grid; gap: var(--space-md); padding: var(--space-lg);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  background: var(--surface-light); color: var(--text-main);
}
.fx-page__title { margin: 0 0 var(--space-xs); font-size: 1.25rem; line-height: 1.3; }
.fx-page__text { margin: 0; color: var(--text-muted); }
.fx-page__toggle {
  display: inline-flex; align-items: center; min-height: 2.75rem; margin-top: var(--space-md);
  padding: var(--space-sm) var(--space-md); border: 1px solid var(--primary); border-radius: var(--radius-md);
  background: var(--surface-light); color: var(--primary); font: inherit; font-weight: 600; cursor: pointer;
  transition: background-color var(--transition-fast), color var(--transition-fast);
}
.fx-page__toggle[hidden] { display: none; }
.fx-page__toggle[aria-pressed="true"] { background: var(--primary); color: var(--text-inverse); }
.fx-page__toggle:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
```

### JS

```js
// Same-document helper: run a DOM update inside a view transition when possible, else instantly
const fxPageReduce = matchMedia('(prefers-reduced-motion: reduce)');
function fxPageSwap(region, update) {
  if (!document.startViewTransition || fxPageReduce.matches) return update();
  region.style.viewTransitionName = 'fx-page-region'; // named only while swapping, so regions never clash
  document.startViewTransition(update).finished.finally(() => { region.style.viewTransitionName = ''; });
}

// Example wiring: a toggle that swaps between the region's two panels
document.querySelectorAll('.fx-page__toggle').forEach((btn) => {
  const region = document.getElementById(btn.getAttribute('aria-controls'));
  const [base, alt] = region.children;
  alt.hidden = true;
  btn.hidden = false;
  btn.addEventListener('click', () => fxPageSwap(region, () => {
    const on = btn.getAttribute('aria-pressed') !== 'true';
    btn.setAttribute('aria-pressed', String(on));
    base.hidden = on;
    alt.hidden = !on;
  }));
});
```

### Notes

- **Support:** cross-document transitions run in Chromium 126+ and Safari 18.2+, on same-origin navigations where both pages carry the `@view-transition` rule. Other browsers just navigate normally. `document.startViewTransition` (same-document) is in Chromium 111+, Safari 18+ and Firefox 144+; elsewhere the helper applies the update instantly.
- `types: fx-nav` limits the main slide to page navigations, so an in-page swap animates only its region instead of shifting the whole page. Where transition types aren't supported, main simply crossfades.
- Each `view-transition-name` must be unique on the page or the transition is skipped; the helper names a region only while it swaps, so several regions can coexist. Named elements form stacking contexts, so a fixed overlay inside `.fx-page__main` can't rise above the header: keep drawers and sticky bars outside main, or use `<dialog>`/popover (top layer).
- **React:** change the DOM synchronously inside the callback: `fxPageSwap(el, () => flushSync(() => setView(next)))`.

## 2. Underline slide link

An underline grows from the left on hover and keyboard focus, in the link's own color. It's drawn as a background on the inline link, so it follows wrapped text line by line. `--prose` keeps a faint resting underline for links in running text; `--inverse` is for dark surfaces.

### HTML

```html
<!-- Standalone link (nav, footer, card) -->
<a class="fx-underline" href="https://example.com/service-areas">Service areas</a>

<!-- In running text: keep a resting underline -->
<p>
  Pipes frozen? <a class="fx-underline fx-underline--prose" href="https://example.com/emergency">Book an
  emergency visit anywhere in Springfield</a> and we'll call you back within 15 minutes.
</p>

<!-- On --surface-dark -->
<a class="fx-underline fx-underline--inverse" href="https://example.com/careers">Careers</a>
```

### CSS

```css
/* Underline = a currentColor gradient on the inline box. Growing its width draws it
   left to right, continuing across wrapped lines in reading order. */
.fx-underline {
  --fx-underline-w: 0%;
  --fx-underline-hover: var(--primary-hover);
  color: var(--primary);
  text-decoration: none;
  background-image: linear-gradient(currentColor, currentColor);
  background-position: 0 100%;
  background-repeat: no-repeat;
  background-size: var(--fx-underline-w) 0.125em;
  transition: background-size var(--transition-smooth), color var(--transition-fast);
}
.fx-underline:hover,
.fx-underline:focus-visible { --fx-underline-w: 100%; color: var(--fx-underline-hover); }

/* Focus ring wraps each line separately */
.fx-underline:focus-visible {
  outline: 2px solid transparent; box-shadow: var(--focus-ring); border-radius: var(--radius-sm);
  -webkit-box-decoration-break: clone; box-decoration-break: clone;
}

/* Running text: a faint full-width line under the growing one, so links don't rely on color */
.fx-underline--prose {
  background-image:
    linear-gradient(currentColor, currentColor),
    linear-gradient(color-mix(in srgb, currentColor 50%, transparent), color-mix(in srgb, currentColor 50%, transparent));
  background-size: var(--fx-underline-w) 0.125em, 100% 1px;
}

/* Dark surfaces */
.fx-underline--inverse { --fx-underline-hover: var(--text-inverse); color: var(--text-inverse); }
.fx-underline--inverse:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; box-shadow: none; }
```

### Notes

- **Why a background, not `::after` + `scaleX`:** a positioned pseudo-element on a wrapped inline link covers one line box (or a box around all of them), not the text. An inline element's background is laid out across every line fragment, so the underline sits under each line and grows through them in reading order.
- Use `--prose` inside paragraphs. `--primary` against `--text-main` is under 3:1, so in running text the link needs a non-color cue at rest.
- Focus switches to `box-decoration-break: clone` so the ring wraps each line. The full-width underline looks the same either way.
- **RTL:** set `background-position: 100% 100%` so the line grows from the right.

## 3. Image zoom reveal

A project photo card: on hover or keyboard focus the image zooms and a caption on a dark scrim fades in. On touch screens (`hover: none`) the caption is always visible. The whole card is one link. Place inside your page container or a grid.

### HTML

```html
<!-- IDs must be unique per card -->
<a class="fx-zoom" href="https://example.com/projects/bathroom-remodel"
   aria-labelledby="fx-zoom-title-1" aria-describedby="fx-zoom-desc-1">
  <img class="fx-zoom__img" src="bathroom.jpg" alt="" width="800" height="600" loading="lazy">
  <span class="fx-zoom__caption">
    <span class="fx-zoom__title" id="fx-zoom-title-1">Bathroom remodel</span>
    <span class="fx-zoom__text" id="fx-zoom-desc-1">Walk-in shower with slate tile · Springfield</span>
  </span>
</a>
```

### CSS

```css
/* Card: the link clips the zooming image */
.fx-zoom {
  position: relative; display: block; overflow: hidden;
  border-radius: var(--radius-lg); background: var(--surface-dark);
  color: var(--text-inverse); text-decoration: none;
}
.fx-zoom:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.fx-zoom__img {
  display: block; width: 100%; height: auto; aspect-ratio: 4 / 3; object-fit: cover;
  transition: transform var(--transition-smooth);
}

/* Caption on a bottom scrim, near-solid behind the text so it passes 4.5:1 on any photo */
.fx-zoom__caption {
  position: absolute; inset: auto 0 0; display: grid; gap: var(--space-xs);
  padding: var(--space-2xl) var(--space-md) var(--space-md);
  background: linear-gradient(to top, color-mix(in srgb, var(--surface-dark) 85%, transparent) 60%, transparent);
  transition: opacity var(--transition-smooth), transform var(--transition-smooth), visibility var(--transition-smooth);
}
.fx-zoom__title { font-size: 1.125rem; font-weight: 600; line-height: 1.3; }
.fx-zoom__text { font-size: 0.875rem; line-height: 1.4; }

/* Mouse devices: caption hidden at rest, revealed with the zoom on hover or focus.
   Touch keeps the default (always visible). */
@media (hover: hover) {
  .fx-zoom__caption { opacity: 0; visibility: hidden; transform: translateY(var(--space-sm)); }
  .fx-zoom:is(:hover, :focus-within) .fx-zoom__caption { opacity: 1; visibility: visible; transform: none; }
  .fx-zoom:is(:hover, :focus-within) .fx-zoom__img { transform: scale(1.06); }
}
```

### Notes

- On mouse devices the resting caption is hidden with `visibility`, not opacity alone, so the link is named with `aria-labelledby`/`aria-describedby`, which still read hidden text. Screen readers always hear "Bathroom remodel" plus the description.
- `:focus-within` reveals the caption for keyboard users, and keeps working if you wrap the link in a larger card.
- `alt=""` because the caption is the text alternative: describe the visible work in `.fx-zoom__text`. Drop `loading="lazy"` if the card is above the fold.
- The scrim is 85% `--surface-dark` behind the text, which keeps `--text-inverse` above 4.5:1 even over a white photo.

## 4. Flip card

A card that flips in 3D to show details on its back. Mouse users flip it by hovering; everyone can flip it with the visible toggle button below it (`aria-pressed`). The hidden face is always `visibility: hidden`, so it's out of the tab order and accessibility tree. Under reduced motion the faces crossfade instead of rotating. Place inside your page container.

### HTML

```html
<!-- Without JS both faces show stacked and the toggle stays hidden -->
<div class="fx-flip">
  <div class="fx-flip__inner">
    <div class="fx-flip__face fx-flip__front">
      <h3 class="fx-flip__title">Water heater repair</h3>
      <p class="fx-flip__text">Same-day service for gas and electric tanks.</p>
    </div>
    <div class="fx-flip__face fx-flip__back">
      <p class="fx-flip__title">Included with every visit</p>
      <ul class="fx-flip__list">
        <li>Upfront diagnosis and quote</li>
        <li>Common parts carried on the van</li>
        <li>1-year labor warranty</li>
      </ul>
    </div>
  </div>
  <button class="fx-flip__toggle" type="button" aria-pressed="false" hidden>
    <svg class="fx-flip__icon" aria-hidden="true" focusable="false" viewBox="0 0 24 24" width="24" height="24">
      <path d="M21 12a9 9 0 1 1-2.64-6.36L21 8M21 3v5h-5" />
    </svg>
    Show details<span class="fx-flip__sr"> for water heater repair</span>
  </button>
</div>
```

### CSS

```css
/* Base (no JS): faces stack vertically, both readable */
.fx-flip { display: grid; gap: var(--space-sm); justify-items: start; perspective: 60rem; }
.fx-flip__inner { display: grid; gap: var(--space-md); justify-self: stretch; }
.fx-flip__face {
  padding: var(--space-lg); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  background: var(--surface-light); color: var(--text-main); box-shadow: var(--shadow-sm);
}
.fx-flip__back { border-color: var(--surface-dark); background: var(--surface-dark); color: var(--text-inverse); }
.fx-flip__title { margin: 0 0 var(--space-sm); font-size: 1.125rem; font-weight: 600; line-height: 1.3; }
.fx-flip__text { margin: 0; color: var(--text-muted); }
.fx-flip__list { margin: 0; padding-left: var(--space-lg); }
.fx-flip__sr { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }

/* Toggle: outside the rotating layer, so it never moves or loses focus */
.fx-flip__toggle {
  display: inline-flex; align-items: center; gap: var(--space-sm); min-height: 2.75rem;
  padding: var(--space-sm) var(--space-md); border: 1px solid var(--text-muted); border-radius: var(--radius-md);
  background: var(--surface-light); color: var(--text-main); font: inherit; cursor: pointer;
  transition: background-color var(--transition-fast), color var(--transition-fast);
}
.fx-flip__toggle[hidden] { display: none; }
.fx-flip__toggle[aria-pressed="true"] { border-color: var(--primary); background: var(--primary); color: var(--text-inverse); }
.fx-flip__toggle:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.fx-flip__icon {
  width: 1.25rem; height: 1.25rem; fill: none; stroke: currentColor; stroke-width: 2;
  stroke-linecap: round; stroke-linejoin: round; transition: transform var(--transition-smooth);
}
.fx-flip__toggle[aria-pressed="true"] .fx-flip__icon { transform: rotate(180deg); }

/* One state drives everything: --fx-flip-p is 0 (front) or 1 (back).
   Back shows when pinned by the toggle, or while hovered on mouse devices. */
.fx-flip--ready { --fx-flip-p: 0; --fx-flip-front: visible; --fx-flip-back: hidden; }
.fx-flip--flipped { --fx-flip-p: 1; --fx-flip-front: hidden; --fx-flip-back: visible; }
@media (hover: hover) {
  .fx-flip--ready:hover { --fx-flip-p: 1; --fx-flip-front: hidden; --fx-flip-back: visible; }
}

/* JS on: faces share one grid cell and the inner layer rotates */
.fx-flip--ready .fx-flip__inner {
  transform-style: preserve-3d; transform: rotateY(calc(var(--fx-flip-p) * 180deg));
  transition: transform var(--transition-smooth);
}
.fx-flip--ready .fx-flip__face {
  grid-area: 1 / 1; backface-visibility: hidden;
  transition: visibility var(--transition-smooth), opacity var(--transition-smooth);
}
.fx-flip--ready .fx-flip__front { visibility: var(--fx-flip-front); }
.fx-flip--ready .fx-flip__back { visibility: var(--fx-flip-back); transform: rotateY(180deg); }

/* Reduced motion: no rotation, the faces crossfade in place */
@media (prefers-reduced-motion: reduce) {
  .fx-flip--ready .fx-flip__inner,
  .fx-flip--ready .fx-flip__back { transform: none; }
  .fx-flip--ready .fx-flip__front { opacity: calc(1 - var(--fx-flip-p)); }
  .fx-flip--ready .fx-flip__back { opacity: var(--fx-flip-p); }
}
```

### JS

```js
// Flip card: turn on the 3D stack, then let the toggle pin the back face
document.querySelectorAll('.fx-flip').forEach((card) => {
  const btn = card.querySelector('.fx-flip__toggle');
  card.classList.add('fx-flip--ready');
  btn.hidden = false;
  btn.addEventListener('click', () => {
    const flipped = btn.getAttribute('aria-pressed') !== 'true';
    btn.setAttribute('aria-pressed', String(flipped));
    card.classList.toggle('fx-flip--flipped', flipped);
  });
});
```

### Notes

- **State model:** visible face = back if pinned (`aria-pressed="true"`) or hovered. Each face's `visibility` comes from the same state as the rotation, so hover and the button can never disagree: the hidden face is never focusable or announced, and a hover-revealed back is fully readable. Clicking the toggle while hovering pins the back; unpinning flips it back when the pointer leaves.
- Keep links and CTAs on the back or outside the card. On mouse devices the front flips away as soon as the pointer reaches it.
- The toggle's label stays fixed and `aria-pressed` carries the state. `[hidden]` is restated in CSS because `display: inline-flex` would otherwise override it.
- Reduced motion swaps the faces by opacity. The motion tokens make that crossfade near-instant.

## 5. Crossfade panels

Two or three panels share one grid cell, switched by a segmented control made of native radio buttons. The active panel crossfades in with no JS; inactive panels are `visibility: hidden`, so they're hidden from assistive tech and the tab order. Place inside your page container.

### HTML

```html
<!-- Each instance needs its own radio name. Option N shows panel N. -->
<div class="fx-crossfade">
  <fieldset class="fx-crossfade__switch">
    <legend class="fx-crossfade__sr">Show services for</legend>
    <label class="fx-crossfade__option">
      <input class="fx-crossfade__radio" type="radio" name="fx-crossfade-1" value="residential" checked>
      <span class="fx-crossfade__label">Residential</span>
    </label>
    <label class="fx-crossfade__option">
      <input class="fx-crossfade__radio" type="radio" name="fx-crossfade-1" value="commercial">
      <span class="fx-crossfade__label">Commercial</span>
    </label>
    <label class="fx-crossfade__option">
      <input class="fx-crossfade__radio" type="radio" name="fx-crossfade-1" value="emergency">
      <span class="fx-crossfade__label">Emergency</span>
    </label>
  </fieldset>
  <div class="fx-crossfade__panels">
    <div class="fx-crossfade__panel">
      <h3 class="fx-crossfade__title">Home repairs and upgrades</h3>
      <p class="fx-crossfade__text">Repairs, installs and yearly tune-ups for homes across Springfield.</p>
    </div>
    <div class="fx-crossfade__panel">
      <h3 class="fx-crossfade__title">Service for local businesses</h3>
      <p class="fx-crossfade__text">Scheduled maintenance for offices, shops and rental properties.</p>
    </div>
    <div class="fx-crossfade__panel">
      <h3 class="fx-crossfade__title">24/7 emergency call-outs</h3>
      <p class="fx-crossfade__text">Call <a class="fx-crossfade__link" href="tel:+15555550123">(555) 555-0123</a>, day or night.</p>
    </div>
  </div>
</div>
```

### CSS

```css
/* Segmented control: visually hidden native radios, styled label text. Wraps on narrow screens. */
.fx-crossfade__switch {
  display: flex; flex-wrap: wrap; gap: var(--space-xs); min-inline-size: 0;
  margin: 0 0 var(--space-lg); padding: var(--space-xs);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); background: var(--surface-muted);
}
.fx-crossfade__option { position: relative; display: flex; flex: 1 1 auto; }
.fx-crossfade__label {
  display: flex; flex: 1; align-items: center; justify-content: center; min-height: 2.75rem;
  padding: var(--space-sm) var(--space-md); border-radius: var(--radius-md);
  color: var(--text-main); font-weight: 600; cursor: pointer;
  transition: background-color var(--transition-fast), color var(--transition-fast);
}
.fx-crossfade__radio:not(:checked) + .fx-crossfade__label:hover { background: var(--border-subtle); }
.fx-crossfade__radio:checked + .fx-crossfade__label { background: var(--primary); color: var(--text-inverse); }
.fx-crossfade__radio:focus-visible + .fx-crossfade__label { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.fx-crossfade__sr,
.fx-crossfade__radio { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }

/* Panel content */
.fx-crossfade__panels { display: grid; gap: var(--space-lg); }
.fx-crossfade__title { margin: 0 0 var(--space-xs); font-size: 1.25rem; line-height: 1.3; color: var(--text-main); }
.fx-crossfade__text { margin: 0; color: var(--text-muted); }
.fx-crossfade__link { color: var(--primary); font-weight: 600; }
.fx-crossfade__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); border-radius: var(--radius-sm); }

/* With :has(): panels stack in one cell (tallest sets the height); only the checked one is visible */
@supports selector(:has(*)) {
  .fx-crossfade__panel {
    grid-area: 1 / 1; opacity: 0; visibility: hidden;
    transition: opacity var(--transition-smooth), visibility var(--transition-smooth);
  }
  .fx-crossfade:has(.fx-crossfade__option:nth-of-type(1) :checked) .fx-crossfade__panel:nth-child(1),
  .fx-crossfade:has(.fx-crossfade__option:nth-of-type(2) :checked) .fx-crossfade__panel:nth-child(2),
  .fx-crossfade:has(.fx-crossfade__option:nth-of-type(3) :checked) .fx-crossfade__panel:nth-child(3) {
    opacity: 1; visibility: visible;
  }
}
```

### Notes

- Native radios give arrow-key switching and a group name (the legend) for free. Don't add tab roles on top.
- Panels share one grid cell, so the block is as tall as its tallest panel and nothing below jumps when switching.
- Inactive panels are `visibility: hidden`: out of the accessibility tree and tab order (the tel link can't be focused while hidden), but still sizing the cell.
- Needs `:has()` (all current browsers); without it every panel shows, stacked. For a fourth panel, add a selector line.

## 6. Ripple effect

A material-style ripple spreads from where the button was clicked or tapped. Keyboard activation (Enter/Space) ripples from the center. The ripple is decorative and off under reduced motion.

### HTML

```html
<button class="fx-ripple" type="button">Get a free quote</button>
<a class="fx-ripple" href="tel:+15555550123">Call (555) 555-0123</a>
```

### CSS

```css
/* Button: clips the ripple; isolation keeps it above the background but under the label */
.fx-ripple {
  position: relative; overflow: hidden; isolation: isolate;
  display: inline-flex; align-items: center; justify-content: center;
  min-height: 2.75rem; padding: var(--space-sm) var(--space-lg);
  border: 0; border-radius: var(--radius-md); background-color: var(--primary); color: var(--text-inverse);
  font: inherit; font-weight: 600; text-decoration: none; cursor: pointer;
  transition: background-color var(--transition-fast);
}
.fx-ripple:hover { background-color: var(--primary-hover); }
.fx-ripple:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Ripple circle: centered on --fx-ripple-x/y, sized by JS to cover the farthest corner */
.fx-ripple::after {
  content: ""; position: absolute; z-index: -1; pointer-events: none;
  left: var(--fx-ripple-x, 50%); top: var(--fx-ripple-y, 50%);
  width: var(--fx-ripple-d, 200%); aspect-ratio: 1; border-radius: var(--radius-full);
  background: color-mix(in srgb, currentColor 35%, transparent);
  opacity: 0; transform: translate(-50%, -50%) scale(0);
}
.fx-ripple--active::after { animation: fx-ripple 600ms ease-out; }
@keyframes fx-ripple {
  from { opacity: 1; transform: translate(-50%, -50%) scale(0); }
  to { opacity: 0; transform: translate(-50%, -50%) scale(1); }
}

/* Reduced motion: no ripple */
@media (prefers-reduced-motion: reduce) {
  .fx-ripple--active::after { animation: none; }
}
```

### JS

```js
// Ripple: start at the pointer (keyboard and AT clicks: the center), then restart the animation
const fxRippleReduce = matchMedia('(prefers-reduced-motion: reduce)');
document.addEventListener('click', (e) => {
  const btn = e.target.closest('.fx-ripple');
  if (!btn || fxRippleReduce.matches) return;
  const r = btn.getBoundingClientRect();
  const keyboard = e.detail === 0; // Enter/Space and AT clicks carry no pointer position
  btn.style.setProperty('--fx-ripple-x', `${keyboard ? r.width / 2 : e.clientX - r.left}px`);
  btn.style.setProperty('--fx-ripple-y', `${keyboard ? r.height / 2 : e.clientY - r.top}px`);
  btn.style.setProperty('--fx-ripple-d', `${2 * Math.hypot(r.width, r.height)}px`);
  btn.classList.remove('fx-ripple--active');
  void btn.offsetWidth; // force a reflow so repeat clicks restart the animation
  btn.classList.add('fx-ripple--active');
});
```

### Notes

- One delegated `click` listener covers mouse, touch, pen and keyboard, plus buttons added later. Keyboard and assistive-tech clicks have `event.detail === 0`, so they ripple from the center.
- The ripple starts on release (`click`). For a ripple on press, listen to `pointerdown` instead and add a `keydown` handler for Enter/Space.
- The pseudo-element has no content or semantics, so screen readers ignore it. Works on `<button>` and `<a>`; keep `overflow: hidden` and `isolation: isolate` on any restyle.

## 7. Tilt card

A card that tilts slightly in 3D toward the mouse, with a soft glare that follows the pointer. It's on only for `(hover: hover) and (prefers-reduced-motion: no-preference)`; touch and keyboard users get the static card. Place inside your page container.

### HTML

```html
<article class="fx-tilt">
  <p class="fx-tilt__eyebrow">Most popular</p>
  <h3 class="fx-tilt__title">Annual maintenance plan</h3>
  <p class="fx-tilt__text">Two tune-ups a year, priority booking and 10% off repairs.</p>
  <a class="fx-tilt__link" href="https://example.com/plans">See what's included</a>
</article>
```

### CSS

```css
/* Card: dark surface so the glare reads. --fx-tilt-x/y run from -1 to 1 (set by JS). */
.fx-tilt {
  --fx-tilt-x: 0; --fx-tilt-y: 0; --fx-tilt-max: 6deg;
  position: relative; isolation: isolate;
  padding: var(--space-xl) var(--space-lg); border-radius: var(--radius-lg);
  background: var(--surface-dark); color: var(--text-inverse); box-shadow: var(--shadow-md);
}
.fx-tilt__eyebrow {
  margin: 0 0 var(--space-xs); font-size: 0.875rem; font-weight: 600;
  letter-spacing: 0.05em; text-transform: uppercase; color: var(--text-inverse-muted);
}
.fx-tilt__title { margin: 0 0 var(--space-sm); font-size: 1.25rem; line-height: 1.3; }
.fx-tilt__text { margin: 0 0 var(--space-md); color: var(--text-inverse-muted); }
.fx-tilt__link { color: var(--text-inverse); font-weight: 600; }
.fx-tilt__link:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }

/* Glare: a soft highlight under the content, centered on the pointer */
.fx-tilt::before {
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; pointer-events: none;
  background: radial-gradient(circle at calc(50% + var(--fx-tilt-x) * 50%) calc(50% + var(--fx-tilt-y) * 50%),
    color-mix(in srgb, var(--text-inverse) 12%, transparent), transparent 60%);
  opacity: 0; transition: opacity var(--transition-smooth);
}

/* Mouse users who allow motion: the side under the pointer dips away */
@media (hover: hover) and (prefers-reduced-motion: no-preference) {
  .fx-tilt {
    transform: perspective(50rem)
      rotateX(calc(var(--fx-tilt-y) * var(--fx-tilt-max) * -1))
      rotateY(calc(var(--fx-tilt-x) * var(--fx-tilt-max)));
    transition: transform var(--transition-smooth), box-shadow var(--transition-smooth);
  }
  .fx-tilt:hover { box-shadow: var(--shadow-lg); transition: transform var(--transition-fast), box-shadow var(--transition-smooth); }
  .fx-tilt:hover::before { opacity: 1; }
}
```

### JS

```js
// Tilt: write the pointer position at most once per frame; reset when the pointer leaves
if (matchMedia('(hover: hover) and (prefers-reduced-motion: no-preference)').matches) {
  document.querySelectorAll('.fx-tilt').forEach((card) => {
    let frame = 0;
    const set = (x, y) => { card.style.setProperty('--fx-tilt-x', x); card.style.setProperty('--fx-tilt-y', y); };
    card.addEventListener('pointermove', (e) => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        const r = card.getBoundingClientRect();
        set(((e.clientX - r.left) / r.width) * 2 - 1, ((e.clientY - r.top) / r.height) * 2 - 1);
      });
    });
    card.addEventListener('pointerleave', () => { cancelAnimationFrame(frame); set(0, 0); });
  });
}
```

### Notes

- Mouse-only enhancement: the transform and glare live inside the same media query the script checks, so changing the OS motion setting turns the CSS off even after the script has run.
- rAF throttling: each move cancels the pending frame, so there's at most one style write per frame, using the latest pointer position.
- Keep `--fx-tilt-max` small (6deg default); larger angles blur text and can cause discomfort. A short `--transition-fast` while hovering keeps it responsive; leaving eases back with `--transition-smooth`.
- The 12% glare keeps `--text-inverse-muted` above 4.5:1. On a light card the glare barely shows; use a faint `--primary` tint instead.
