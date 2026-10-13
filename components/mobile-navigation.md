# Mobile Navigation

Eight standalone menus, bars and menu buttons for screens under 768px, complementing the header and right-hand drawer in `components/navigation.md`. Depends on `tokens/variables.css`.

| #  | Pattern                                                                         | JS              |
| -- | ------------------------------------------------------------------------------- | --------------- |
| 1  | **Full-screen overlay menu**: modal `<dialog>` with large, staggered links      | ~15 lines       |
| 2  | **Bottom tab bar**: fixed app-style bar of icon + label links                   | none            |
| 3  | **Accordion drawer**: left drawer with `<details>` sections of nested links     | ~24 lines       |
| 4  | **Bottom sheet menu**: modal `<dialog>` that slides up from the bottom edge     | ~15 lines       |
| 5  | **Slide-down panel**: sticky bar whose menu drops down with a height animation  | ~19 lines       |
| 6  | **Animated hamburger icons**: three CSS-only morphs keyed to `aria-expanded`    | ~5 lines (demo) |
| 7  | **Scrollable link strip**: sideways scroll-snap links with edge fades           | ~9 lines        |
| 8  | **Compact mobile top bar**: sticky menu · logo · call bar                       | none (uses 3's) |

## 1. Full-screen overlay menu

A `<dialog>` opened with `showModal()` covers the screen: the page goes inert, focus stays inside, and Escape, the close button or a link closes it, returning focus to the opener. Links fade in one after another, and page scroll is locked while it's open. From 768px the opener is hidden and an open overlay closes.

### HTML

```html
<!-- Opener: put it in your header. It ships hidden; the script reveals it. -->
<button class="mnav-overlay__open" type="button" aria-haspopup="dialog" aria-controls="mnav-overlay-1" hidden>
  <svg class="mnav-overlay__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h16" /></svg>
  Menu
</button>

<dialog id="mnav-overlay-1" class="mnav-overlay" aria-label="Menu">
  <button class="mnav-overlay__close" type="button" aria-label="Close menu">
    <svg class="mnav-overlay__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
  </button>
  <nav aria-label="Main">
    <ul class="mnav-overlay__list" role="list">
      <li class="mnav-overlay__item" style="--mnav-overlay-i: 0"><a class="mnav-overlay__link" href="/" aria-current="page">Home</a></li>
      <li class="mnav-overlay__item" style="--mnav-overlay-i: 1"><a class="mnav-overlay__link" href="/services">Services</a></li>
      <li class="mnav-overlay__item" style="--mnav-overlay-i: 2"><a class="mnav-overlay__link" href="/projects">Projects</a></li>
      <li class="mnav-overlay__item" style="--mnav-overlay-i: 3"><a class="mnav-overlay__link" href="/reviews">Reviews</a></li>
      <li class="mnav-overlay__item" style="--mnav-overlay-i: 4"><a class="mnav-overlay__link" href="/contact">Contact</a></li>
    </ul>
  </nav>
  <a class="mnav-overlay__cta mnav-overlay__item" style="--mnav-overlay-i: 5" href="tel:+15555550123">Call (555) 555-0123</a>
</dialog>
```

### CSS

```css
/* Opener: mobile only. [hidden] must beat display, so no-JS visitors never see a dead button */
.mnav-overlay__open {
  display: inline-flex; align-items: center; gap: var(--space-sm);
  min-height: 2.75rem; padding: 0 var(--space-md);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
  background: var(--surface-light); color: var(--text-main);
  font: inherit; font-weight: 600; cursor: pointer;
}
.mnav-overlay__open[hidden] { display: none; }
.mnav-overlay__open:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.mnav-overlay__icon {
  flex: none; width: 1.5rem; height: 1.5rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round;
}

/* Full-screen dark panel; showModal() lifts it into the top layer */
.mnav-overlay {
  position: fixed; inset: 0; z-index: 40;
  box-sizing: border-box; width: 100%; max-width: none; height: 100%; max-height: none;
  margin: 0; padding: var(--space-md) var(--gutter) var(--space-2xl);
  border: 0; background: var(--surface-dark); color: var(--text-inverse);
  overflow-y: auto; overscroll-behavior: contain;
}
html:has(.mnav-overlay[open]) { overflow: hidden; } /* lock page scroll */

/* Close button, large links, call CTA */
.mnav-overlay__close {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; margin-inline-start: auto; padding: 0;
  border: 0; border-radius: var(--radius-md); background: transparent; color: inherit; cursor: pointer;
}
.mnav-overlay__list { margin: var(--space-lg) 0 var(--space-xl); padding: 0; list-style: none; }
.mnav-overlay__link {
  display: block; padding-block: var(--space-sm);
  color: var(--text-inverse); font-size: 2rem; font-weight: 700; line-height: 1.2;
  text-decoration: none; overflow-wrap: anywhere;
  transition: color var(--transition-fast);
}
.mnav-overlay__link:hover { color: var(--text-inverse-muted); }
.mnav-overlay__link[aria-current="page"] {
  text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 0.2em;
}
.mnav-overlay__cta {
  display: flex; align-items: center; justify-content: center; min-height: 2.75rem;
  border-radius: var(--radius-md); background: var(--primary); color: var(--text-inverse);
  font-weight: 600; text-decoration: none;
}
/* Focus on a dark surface */
.mnav-overlay__close:focus-visible, .mnav-overlay__link:focus-visible, .mnav-overlay__cta:focus-visible {
  outline: 2px solid var(--text-inverse); outline-offset: 2px;
}

/* Staggered entrance, replayed on every open; --mnav-overlay-i is the item's index */
.mnav-overlay[open] .mnav-overlay__item {
  animation: mnav-overlay-in 400ms ease-out both;
  animation-delay: calc(var(--mnav-overlay-i, 0) * 60ms);
}
@keyframes mnav-overlay-in { from { opacity: 0; translate: 0 1rem; } }
@media (prefers-reduced-motion: reduce) {
  .mnav-overlay[open] .mnav-overlay__item { animation: none; }
}

@media (min-width: 768px) {
  .mnav-overlay__open { display: none; }
}
```

### JS

```js
// Reveal every opener that names an overlay, and open it modally
const overlays = document.querySelectorAll('dialog.mnav-overlay');
overlays.forEach((dlg) => {
  document.querySelectorAll(`[aria-controls="${dlg.id}"]`).forEach((btn) => {
    btn.hidden = false;
    btn.addEventListener('click', () => {
      dlg.showModal();
      dlg.addEventListener('close', () => btn.focus(), { once: true }); // Escape, close button or link
    });
  });
  // Close button, or a link (the page is about to change)
  dlg.addEventListener('click', (e) => {
    if (e.target.closest('.mnav-overlay__close, a')) dlg.close();
  });
});

// Past the breakpoint, close any open overlay so the page isn't left inert
const wide = matchMedia('(min-width: 768px)');
wide.addEventListener('change', () => wide.matches && overlays.forEach((dlg) => dlg.close()));
```

### Notes

- `showModal()` gives the focus trap, the inert page and Escape for free, and puts the dialog in the top layer above every z-index. `z-index: 40` only matters if you switch to a non-modal `show()`.
- The opener ships `hidden`, and the script reveals every button whose `aria-controls` names the dialog. Repeat the main links in the footer for no-JS visitors. Invoker commands (`commandfor` + `command="show-modal"`) can open the dialog with no JS at all (Chrome 135+, Firefox 144+, Safari 26.2+).
- Number the items with `--mnav-overlay-i` (0, 1, 2…). With reduced motion they all appear at once.
- The scroll lock uses `:has()`. Without it, the page behind can still scroll but stays inert.
- **React:** keep the `<dialog>` mounted and call `ref.current.showModal()` from the click handler. If you render it conditionally, you lose the close event and the focus return.

## 2. Bottom tab bar

App-style bar fixed to the bottom of the viewport: 4–5 icon + label links, with the current page marked by `aria-current="page"` (color, weight and a top indicator). `body:has()` pads the page so the bar never covers content, and `env(safe-area-inset-bottom)` clears the iPhone home indicator. From 768px the bar is hidden, so use your desktop header there.

### HTML

```html
<nav class="mnav-tabbar" aria-label="Quick links">
  <ul class="mnav-tabbar__list" role="list">
    <li>
      <a class="mnav-tabbar__link" href="/" aria-current="page">
        <svg class="mnav-tabbar__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M3 11l9-7 9 7M5 10v10h14V10" /></svg>
        <span class="mnav-tabbar__label">Home</span>
      </a>
    </li>
    <li>
      <a class="mnav-tabbar__link" href="/services">
        <svg class="mnav-tabbar__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z" /></svg>
        <span class="mnav-tabbar__label">Services</span>
      </a>
    </li>
    <li>
      <a class="mnav-tabbar__link" href="/projects">
        <svg class="mnav-tabbar__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M4 5h16v14H4zM4 16l5-5 5 5 2-2 4 4" /></svg>
        <span class="mnav-tabbar__label">Projects</span>
      </a>
    </li>
    <li>
      <a class="mnav-tabbar__link" href="/reviews">
        <svg class="mnav-tabbar__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3l-5.6 2.9 1.1-6.2L3 9.6l6.2-.9z" /></svg>
        <span class="mnav-tabbar__label">Reviews</span>
      </a>
    </li>
    <li>
      <a class="mnav-tabbar__link" href="tel:+15555550123">
        <svg class="mnav-tabbar__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5l1.5-2.5 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2" /></svg>
        <span class="mnav-tabbar__label">Call</span>
      </a>
    </li>
  </ul>
</nav>
```

### CSS

```css
:root { --mnav-tabbar-h: 3.5rem; } /* bar height before the safe area; the page padding reads it */

/* Fixed to the bottom; env() clears the iPhone home indicator */
.mnav-tabbar {
  position: fixed; inset: auto 0 0; z-index: 5;
  padding-bottom: env(safe-area-inset-bottom, 0px);
  background: var(--surface-light); border-top: 1px solid var(--border-subtle);
}
.mnav-tabbar__list {
  display: grid; grid-auto-flow: column; grid-auto-columns: minmax(0, 1fr);
  margin: 0; padding: 0; list-style: none;
}

/* Icon over label; inactive tabs use --text-muted (4.8:1) */
.mnav-tabbar__link {
  position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center;
  gap: var(--space-xs); min-height: var(--mnav-tabbar-h); padding-inline: var(--space-xs);
  color: var(--text-muted); font-size: 0.75rem; font-weight: 500; line-height: 1.2; text-decoration: none;
  transition: color var(--transition-fast);
}
.mnav-tabbar__label { max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.mnav-tabbar__icon {
  width: 1.5rem; height: 1.5rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.mnav-tabbar__link:hover { color: var(--text-main); }
.mnav-tabbar__link:focus-visible { outline: 2px solid transparent; box-shadow: inset var(--focus-ring); }

/* Current page: color, weight and a top bar, so it isn't shown by color alone */
.mnav-tabbar__link[aria-current="page"] { color: var(--primary); font-weight: 700; }
.mnav-tabbar__link[aria-current="page"]::before {
  content: ""; position: absolute; top: 0; inset-inline: 25%;
  border-top: var(--space-xs) solid; border-radius: 0 0 var(--radius-sm) var(--radius-sm);
}

/* Keep the end of the page clear of the bar (mobile only) */
@media (width < 768px) {
  body:has(.mnav-tabbar) { padding-bottom: calc(var(--mnav-tabbar-h) + env(safe-area-inset-bottom, 0px)); }
}
@media (min-width: 768px) {
  .mnav-tabbar { display: none; }
}
```

### Notes

- These are links, not ARIA tabs, so there's no `role="tablist"` and no arrow-key handling. Keep the labels visible, because icon-only tabs leave many users guessing.
- At 320px, five tabs get 64px each. Keep each label to one short word; longer ones are cut off with an ellipsis.
- `env(safe-area-inset-bottom)` is 0 unless the viewport meta includes `viewport-fit=cover`. The page padding uses `body:has()`, which works in all current browsers.
- Don't combine this bar with the `action-bar` call bar from `components/cta-sections.md`, because both use the bottom edge. Make Call one of the tabs instead.

## 3. Accordion drawer

Drawer that slides in from the left over a backdrop, with native `<details>` sections that expand to show nested links. It's a non-modal disclosure: the toggle's `aria-expanded` tracks the state, focus moves to the drawer when it opens, and Escape, the backdrop or the close button shuts it and returns focus to the toggle. Without JS it renders as a plain nav block in the page flow. From 768px it's hidden.

### HTML

```html
<!-- Toggle: put it in your header. It ships hidden; the script reveals it. -->
<button class="mnav-accordion__toggle" type="button" aria-expanded="false" aria-controls="mnav-accordion-1" hidden>
  <svg class="mnav-accordion__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h16" /></svg>
  Menu
</button>

<!-- Drawer + backdrop: anywhere in <body>, e.g. right after the header -->
<div class="mnav-accordion">
  <div class="mnav-accordion__backdrop"></div>
  <nav id="mnav-accordion-1" class="mnav-accordion__panel" aria-label="Main" tabindex="-1">
    <div class="mnav-accordion__head">
      <span class="mnav-accordion__title">Menu</span>
      <button class="mnav-accordion__close" type="button" aria-label="Close menu">
        <svg class="mnav-accordion__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
      </button>
    </div>

    <details class="mnav-accordion__section" name="mnav-accordion-sections" open>
      <summary class="mnav-accordion__summary">
        Services
        <svg class="mnav-accordion__icon mnav-accordion__chevron" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
      </summary>
      <ul class="mnav-accordion__sub" role="list">
        <li><a class="mnav-accordion__link" href="/services/roofing">Roofing</a></li>
        <li><a class="mnav-accordion__link" href="/services/gutters" aria-current="page">Gutters</a></li>
        <li><a class="mnav-accordion__link" href="/services/siding">Siding</a></li>
        <li><a class="mnav-accordion__link" href="/services">All services</a></li>
      </ul>
    </details>

    <details class="mnav-accordion__section" name="mnav-accordion-sections">
      <summary class="mnav-accordion__summary">
        Service areas
        <svg class="mnav-accordion__icon mnav-accordion__chevron" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
      </summary>
      <ul class="mnav-accordion__sub" role="list">
        <li><a class="mnav-accordion__link" href="/areas/downtown">Downtown Springfield</a></li>
        <li><a class="mnav-accordion__link" href="/areas/northside">Northside</a></li>
        <li><a class="mnav-accordion__link" href="/areas/westlake">Westlake</a></li>
      </ul>
    </details>

    <a class="mnav-accordion__top" href="/reviews">Reviews</a>
    <a class="mnav-accordion__top" href="/contact">Contact</a>
  </nav>
</div>
```

### CSS

```css
/* Toggle: mobile only, revealed by the script */
.mnav-accordion__toggle {
  display: inline-flex; align-items: center; gap: var(--space-sm);
  min-height: 2.75rem; padding: 0 var(--space-md);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
  background: var(--surface-light); color: var(--text-main);
  font: inherit; font-weight: 600; cursor: pointer;
}
.mnav-accordion__toggle[hidden] { display: none; }
.mnav-accordion__icon {
  flex: none; width: 1.5rem; height: 1.5rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}

/* Panel content. Without JS this is a plain block in the page flow */
.mnav-accordion__panel { padding: var(--space-md) var(--gutter) var(--space-xl); background: var(--surface-light); color: var(--text-main); }
.mnav-accordion__panel:focus { outline: none; } /* script focus target, not a control */
.mnav-accordion__head {
  display: flex; align-items: center; justify-content: space-between;
  min-height: 2.75rem; margin-bottom: var(--space-sm);
}
.mnav-accordion__title { font-size: 1.125rem; font-weight: 700; }
.mnav-accordion__close {
  display: none; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0;
  border: 0; border-radius: var(--radius-md); background: transparent; color: inherit; cursor: pointer;
}

/* Section rows and top-level links share one look */
.mnav-accordion__summary, .mnav-accordion__top {
  display: flex; align-items: center; justify-content: space-between; min-height: 3rem;
  border-bottom: 1px solid var(--border-subtle);
  color: var(--text-main); font-size: 1.125rem; font-weight: 600; text-decoration: none; cursor: pointer;
}
.mnav-accordion__summary { list-style: none; }
.mnav-accordion__summary::-webkit-details-marker { display: none; }
.mnav-accordion__chevron { transition: rotate var(--transition-smooth); }
.mnav-accordion__section[open] .mnav-accordion__chevron { rotate: 180deg; }
.mnav-accordion__sub {
  margin: 0; padding: var(--space-xs) 0 var(--space-sm) var(--space-md);
  border-bottom: 1px solid var(--border-subtle); list-style: none;
}
.mnav-accordion__link { display: flex; align-items: center; min-height: 2.75rem; color: var(--text-main); text-decoration: none; }
.mnav-accordion__link:hover, .mnav-accordion__top:hover { color: var(--primary); }
.mnav-accordion__link[aria-current="page"] { color: var(--primary); font-weight: 600; }
.mnav-accordion__toggle:focus-visible, .mnav-accordion__close:focus-visible, .mnav-accordion__summary:focus-visible,
.mnav-accordion__top:focus-visible, .mnav-accordion__link:focus-visible {
  outline: 2px solid transparent; box-shadow: var(--focus-ring);
}

/* Smooth expand where supported (Chromium); elsewhere sections open instantly */
@supports (interpolate-size: allow-keywords) {
  .mnav-accordion__section { interpolate-size: allow-keywords; }
  .mnav-accordion__section::details-content {
    height: 0; overflow: clip;
    transition: height var(--transition-smooth), content-visibility var(--transition-smooth) allow-discrete;
  }
  .mnav-accordion__section[open]::details-content { height: auto; }
}

/* Drawer mode (the script adds .mnav-accordion--js): fixed, off-canvas, hidden from AT until open */
.mnav-accordion__backdrop { display: none; }
.mnav-accordion--js .mnav-accordion__close { display: grid; }
.mnav-accordion--js .mnav-accordion__backdrop {
  display: block; position: fixed; inset: var(--mnav-accordion-top, 0px) 0 0; z-index: 10;
  background: color-mix(in srgb, var(--surface-dark) 50%, transparent);
  opacity: 0; visibility: hidden;
  transition: opacity var(--transition-smooth), visibility var(--transition-smooth);
}
.mnav-accordion--js .mnav-accordion__panel {
  position: fixed; inset: var(--mnav-accordion-top, 0px) auto 0 0; z-index: 20;
  box-sizing: border-box; width: min(20rem, 85vw);
  overflow-y: auto; overscroll-behavior: contain; box-shadow: var(--shadow-lg);
  translate: -100% 0; visibility: hidden;
  transition: translate var(--transition-smooth), visibility var(--transition-smooth);
}
.mnav-accordion[data-open] .mnav-accordion__panel,
.mnav-accordion[data-open] .mnav-accordion__backdrop { translate: none; opacity: 1; visibility: visible; }

/* Lock page scroll while open (mobile only) */
@media (width < 768px) {
  html:has(.mnav-accordion[data-open]) { overflow: hidden; }
}
@media (min-width: 768px) {
  .mnav-accordion, .mnav-accordion__toggle { display: none; }
}
```

### JS

```js
// One drawer can have several toggles: all are revealed and kept in sync
let opener = null;
const togglesFor = (panel) => document.querySelectorAll(`[aria-controls="${panel.id}"]`);
function setOpen(root, open, refocus) {
  const panel = root.querySelector('.mnav-accordion__panel');
  root.toggleAttribute('data-open', open);
  togglesFor(panel).forEach((btn) => btn.setAttribute('aria-expanded', open));
  if (open) panel.focus({ preventScroll: true });
  else if (refocus) opener?.focus();
}
document.querySelectorAll('.mnav-accordion').forEach((root) => {
  root.classList.add('mnav-accordion--js'); // gate: drawer CSS applies only with JS
  togglesFor(root.querySelector('.mnav-accordion__panel')).forEach((btn) => {
    btn.hidden = false;
    btn.addEventListener('click', () => { opener = btn; setOpen(root, !root.hasAttribute('data-open')); });
  });
  // Backdrop or close button: close and refocus. A link: just close (the page changes)
  root.addEventListener('click', (e) => {
    if (e.target.closest('.mnav-accordion__backdrop, .mnav-accordion__close')) setOpen(root, false, true);
    else if (e.target.closest('a')) setOpen(root, false);
  });
});
document.addEventListener('keydown', (e) => {
  const root = document.querySelector('.mnav-accordion[data-open]');
  if (e.key === 'Escape' && root) setOpen(root, false, true);
});
```

### Notes

- It's non-modal on purpose, so a toggle in a sticky bar above it (8. Compact mobile top bar) stays usable. Focus moves to the panel on open but isn't trapped. Use 1 or 4 when you need a true modal.
- The script reveals every button whose `aria-controls` names the panel, keeps `aria-expanded` in sync on all of them, and returns focus to whichever one opened the drawer. Set `--mnav-accordion-top` on `.mnav-accordion` to start the drawer and backdrop below a sticky bar.
- `<details name>` keeps one section open at a time (Chrome 120+, Safari 17.2+, Firefox 130+); older browsers allow several. Add `open` to the section that holds the current page. The smooth expand uses `interpolate-size` + `::details-content` (Chromium); other browsers open sections instantly.
- Without JS, the toggle stays hidden and the panel shows as a normal nav block wherever it sits in the page. The `<details>` sections still work.

## 4. Bottom sheet menu

A modal `<dialog>` pinned to the bottom edge that slides up when it opens (`@starting-style`) and, where supported, slides back down when it closes. A backdrop tap, the close button, Escape or a link closes it, and focus returns to the opener. Content taller than `85dvh` scrolls inside the sheet. From 768px the opener is hidden and an open sheet closes.

### HTML

```html
<!-- Opener: put it in your header. It ships hidden; the script reveals it. -->
<button class="mnav-sheet__open" type="button" aria-haspopup="dialog" aria-controls="mnav-sheet-1" hidden>
  <svg class="mnav-sheet__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h16" /></svg>
  Menu
</button>

<dialog id="mnav-sheet-1" class="mnav-sheet" aria-labelledby="mnav-sheet-1-title">
  <div class="mnav-sheet__body">
    <span class="mnav-sheet__handle" aria-hidden="true"></span>
    <div class="mnav-sheet__head">
      <h2 class="mnav-sheet__title" id="mnav-sheet-1-title">Menu</h2>
      <button class="mnav-sheet__close" type="button" aria-label="Close menu">
        <svg class="mnav-sheet__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
      </button>
    </div>
    <nav class="mnav-sheet__nav" aria-label="Main">
      <ul class="mnav-sheet__list" role="list">
        <li><a class="mnav-sheet__link" href="/" aria-current="page">Home</a></li>
        <li><a class="mnav-sheet__link" href="/services">Services</a></li>
        <li><a class="mnav-sheet__link" href="/projects">Projects</a></li>
        <li><a class="mnav-sheet__link" href="/reviews">Reviews</a></li>
        <li><a class="mnav-sheet__link" href="/contact">Contact</a></li>
      </ul>
      <a class="mnav-sheet__cta" href="tel:+15555550123">Call (555) 555-0123</a>
    </nav>
  </div>
</dialog>
```

### CSS

```css
/* Opener: mobile only, revealed by the script */
.mnav-sheet__open {
  display: inline-flex; align-items: center; gap: var(--space-sm);
  min-height: 2.75rem; padding: 0 var(--space-md);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
  background: var(--surface-light); color: var(--text-main);
  font: inherit; font-weight: 600; cursor: pointer;
}
.mnav-sheet__open[hidden] { display: none; }
.mnav-sheet__icon {
  flex: none; width: 1.5rem; height: 1.5rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round;
}

/* Sheet pinned to the bottom; the closed state sits just below the viewport */
.mnav-sheet {
  position: fixed; inset: auto 0 0; z-index: 40;
  box-sizing: border-box; width: 100%; max-width: none; max-height: none;
  margin: 0; padding: 0; border: 0; border-radius: var(--radius-lg) var(--radius-lg) 0 0;
  background: var(--surface-light); color: var(--text-main); box-shadow: var(--shadow-lg);
  overflow: hidden;
  translate: 0 100%;
  transition: translate var(--transition-smooth),
    display var(--transition-smooth) allow-discrete, overlay var(--transition-smooth) allow-discrete;
}
.mnav-sheet[open] { translate: 0 0; }
@starting-style { .mnav-sheet[open] { translate: 0 100%; } }

/* Backdrop fades with the slide */
.mnav-sheet::backdrop {
  background: color-mix(in srgb, var(--surface-dark) 50%, transparent);
  opacity: 0;
  transition: opacity var(--transition-smooth),
    display var(--transition-smooth) allow-discrete, overlay var(--transition-smooth) allow-discrete;
}
.mnav-sheet[open]::backdrop { opacity: 1; }
@starting-style { .mnav-sheet[open]::backdrop { opacity: 0; } }
html:has(.mnav-sheet[open]) { overflow: hidden; } /* lock page scroll */

/* The body fills the dialog, so a click that targets the <dialog> itself came from the backdrop */
.mnav-sheet__body {
  display: flex; flex-direction: column; max-height: 85dvh;
  padding-bottom: env(safe-area-inset-bottom, 0px);
}
.mnav-sheet__handle {
  flex: none; width: 2.5rem; height: var(--space-xs); margin: var(--space-sm) auto 0;
  border-radius: var(--radius-full); background: var(--border-subtle);
}
.mnav-sheet__head {
  display: flex; align-items: center; justify-content: space-between; gap: var(--space-md);
  padding: var(--space-xs) var(--gutter);
}
.mnav-sheet__title { margin: 0; font-size: 1.125rem; }
.mnav-sheet__close {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0;
  border: 0; border-radius: var(--radius-full); background: var(--surface-muted); color: var(--text-main); cursor: pointer;
}

/* Long menus scroll inside the sheet, not the page */
.mnav-sheet__nav { min-height: 0; padding: 0 var(--gutter) var(--space-lg); overflow-y: auto; overscroll-behavior: contain; }
.mnav-sheet__list { margin: 0; padding: 0; list-style: none; }
.mnav-sheet__link {
  display: flex; align-items: center; min-height: 3rem; border-bottom: 1px solid var(--border-subtle);
  color: var(--text-main); font-size: 1.125rem; font-weight: 500; text-decoration: none;
}
.mnav-sheet__link[aria-current="page"] { color: var(--primary); font-weight: 700; }
.mnav-sheet__cta {
  display: flex; align-items: center; justify-content: center; min-height: 2.75rem; margin-top: var(--space-lg);
  border-radius: var(--radius-md); background: var(--primary); color: var(--text-inverse);
  font-weight: 600; text-decoration: none;
}
.mnav-sheet__open:focus-visible, .mnav-sheet__close:focus-visible,
.mnav-sheet__link:focus-visible, .mnav-sheet__cta:focus-visible {
  outline: 2px solid transparent; box-shadow: var(--focus-ring);
}

@media (min-width: 768px) {
  .mnav-sheet__open { display: none; }
}
```

### JS

```js
// Reveal every opener that names a sheet, and open it modally
const sheets = document.querySelectorAll('dialog.mnav-sheet');
sheets.forEach((dlg) => {
  document.querySelectorAll(`[aria-controls="${dlg.id}"]`).forEach((btn) => {
    btn.hidden = false;
    btn.addEventListener('click', () => {
      dlg.showModal();
      dlg.addEventListener('close', () => btn.focus(), { once: true });
    });
  });
  // e.target === dlg only for backdrop taps; a close button or link also closes
  dlg.addEventListener('click', (e) => {
    if (e.target === dlg || e.target.closest('.mnav-sheet__close, a')) dlg.close();
  });
});

// Past the breakpoint, close any open sheet so the page isn't left inert
const wide = matchMedia('(min-width: 768px)');
wide.addEventListener('change', () => wide.matches && sheets.forEach((dlg) => dlg.close()));
```

### Notes

- The slide-up uses `@starting-style` (Chrome 117+, Safari 17.5+, Firefox 129+). Browsers that can't transition `overlay` (everything but Chromium) slide the sheet out at `z-index: 40` after it leaves the top layer, or simply hide it. Older browsers show and hide it without motion.
- `::backdrop` can read tokens because it inherits from its dialog (Chrome 122+, Safari 17.4+, Firefox 120+).
- The handle is decorative and `aria-hidden`. If you add swipe-to-close, keep the close button, because a drag needs a single-pointer alternative (WCAG 2.5.7).
- Backdrop detection relies on `.mnav-sheet__body` filling the dialog, so keep the dialog's padding at 0. The opener ships `hidden`, as in 1.

## 5. Slide-down panel

Sticky header (z-index 30) with a menu panel that drops down over the page, animating its height with `grid-template-rows: 0fr → 1fr`. It uses the disclosure pattern: `aria-expanded` on the toggle, and a closed panel set to `visibility: hidden`, which takes its links out of the tab order and the accessibility tree. Escape, a tap outside or a link closes it. From 768px the links sit inline in the bar.

### HTML

```html
<header class="mnav-dropdown">
  <div class="mnav-dropdown__bar">
    <a class="mnav-dropdown__brand" href="/">Brand</a>
    <!-- Ships hidden; the script reveals it -->
    <button class="mnav-dropdown__toggle" type="button" aria-expanded="false" aria-controls="mnav-dropdown-1" hidden>
      Menu
      <svg class="mnav-dropdown__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
    </button>
    <nav id="mnav-dropdown-1" class="mnav-dropdown__panel" aria-label="Main">
      <div class="mnav-dropdown__inner">
        <ul class="mnav-dropdown__list" role="list">
          <li><a class="mnav-dropdown__link" href="/services" aria-current="page">Services</a></li>
          <li><a class="mnav-dropdown__link" href="/projects">Projects</a></li>
          <li><a class="mnav-dropdown__link" href="/reviews">Reviews</a></li>
          <li><a class="mnav-dropdown__link" href="/contact">Contact</a></li>
        </ul>
      </div>
    </nav>
  </div>
</header>
```

### CSS

```css
/* Header shell. It becomes sticky only with JS, so the no-JS open list never pins over the page */
.mnav-dropdown {
  --mnav-dropdown-bar-h: 3.5rem;
  position: relative;
  background: var(--surface-light); border-bottom: 1px solid var(--border-subtle);
}
.mnav-dropdown--js { position: sticky; top: 0; z-index: 30; }
.mnav-dropdown__bar {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; column-gap: var(--space-md);
  min-height: var(--mnav-dropdown-bar-h); max-width: var(--container-max);
  margin-inline: auto; padding-inline: var(--gutter);
}
.mnav-dropdown__brand { font-size: 1.25rem; font-weight: 700; color: var(--text-main); text-decoration: none; }
.mnav-dropdown__toggle {
  display: inline-flex; align-items: center; gap: var(--space-xs);
  min-height: 2.75rem; padding: 0 var(--space-sm);
  border: 0; border-radius: var(--radius-md); background: transparent;
  color: var(--text-main); font: inherit; font-weight: 600; cursor: pointer;
}
.mnav-dropdown__toggle[hidden] { display: none; }
.mnav-dropdown__icon {
  width: 1.5rem; height: 1.5rem; transition: rotate var(--transition-smooth);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.mnav-dropdown__toggle[aria-expanded="true"] .mnav-dropdown__icon { rotate: 180deg; }

/* Links. Without JS they show as an open list under the bar */
.mnav-dropdown__panel { flex-basis: 100%; }
.mnav-dropdown__list { margin: 0; padding: 0 0 var(--space-sm); list-style: none; }
.mnav-dropdown__link {
  display: flex; align-items: center; min-height: 3rem; border-top: 1px solid var(--border-subtle);
  color: var(--text-main); font-size: 1.125rem; font-weight: 500; text-decoration: none;
}
.mnav-dropdown__link:hover, .mnav-dropdown__link[aria-current="page"] { color: var(--primary); }
.mnav-dropdown__brand:focus-visible, .mnav-dropdown__toggle:focus-visible, .mnav-dropdown__link:focus-visible {
  outline: 2px solid transparent; box-shadow: var(--focus-ring);
}

/* JS on: the panel overlays the page. 0fr -> 1fr animates to the content's real height */
.mnav-dropdown--js .mnav-dropdown__panel {
  position: absolute; top: 100%; inset-inline: 0;
  display: grid; grid-template-rows: 0fr; visibility: hidden;
  background: var(--surface-light); box-shadow: var(--shadow-lg);
  transition: grid-template-rows var(--transition-smooth), visibility var(--transition-smooth);
}
.mnav-dropdown--js .mnav-dropdown__panel[data-open] { grid-template-rows: 1fr; visibility: visible; }
.mnav-dropdown--js .mnav-dropdown__inner {
  min-height: 0; max-height: calc(100dvh - var(--mnav-dropdown-bar-h));
  overflow-y: auto; overscroll-behavior: contain;
}
.mnav-dropdown--js .mnav-dropdown__list {
  max-width: var(--container-max); margin-inline: auto; padding: var(--space-xs) var(--gutter) var(--space-sm);
}

/* From 768px: no toggle, links sit inline in the bar */
@media (min-width: 768px) {
  .mnav-dropdown__toggle { display: none; }
  .mnav-dropdown__panel, .mnav-dropdown--js .mnav-dropdown__panel {
    position: static; display: block; flex-basis: auto; visibility: visible; box-shadow: none;
  }
  .mnav-dropdown--js .mnav-dropdown__inner { max-height: none; overflow: visible; }
  .mnav-dropdown__list, .mnav-dropdown--js .mnav-dropdown__list { display: flex; gap: var(--space-lg); padding: 0; }
  .mnav-dropdown__link { min-height: 2.75rem; border: 0; font-size: 1rem; }
}
```

### JS

```js
document.querySelectorAll('.mnav-dropdown').forEach((root) => {
  const toggle = root.querySelector('.mnav-dropdown__toggle');
  const panel = document.getElementById(toggle.getAttribute('aria-controls'));
  const isOpen = () => toggle.getAttribute('aria-expanded') === 'true';
  const setOpen = (open) => {
    toggle.setAttribute('aria-expanded', open);
    panel.toggleAttribute('data-open', open);
  };
  root.classList.add('mnav-dropdown--js'); // gate: collapse + sticky apply only with JS
  toggle.hidden = false;
  toggle.addEventListener('click', () => setOpen(!isOpen()));
  panel.addEventListener('click', (e) => e.target.closest('a') && setOpen(false));
  // Escape closes and refocuses the toggle; a tap outside the header just closes
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape' || !isOpen()) return;
    setOpen(false);
    toggle.focus();
  });
  document.addEventListener('click', (e) => isOpen() && !root.contains(e.target) && setOpen(false));
});
```

### Notes

- `visibility` transitions together with the height, so the panel stays visible while it closes and only then leaves the tab order and the accessibility tree.
- The 0fr → 1fr technique needs `min-height: 0` on the inner element and no height measuring in JS. `max-height` keeps long menus scrolling inside the panel.
- Without JS, the toggle stays hidden and the header is static, with the links open under the brand. The script adds `.mnav-dropdown--js` before anything is collapsed.
- Use it instead of the drawer in `components/navigation.md`, not alongside it.

## 6. Animated hamburger icons

One 44px button with three CSS-only morphs, all driven by `[aria-expanded="true"]`: `--x` (the outer lines cross into an X), `--arrow` (the outer lines fold into a back arrow) and `--collapse` (the lines stack in the middle, then the icon turns into an X). The lines are SVG strokes in `currentColor`, so the icon follows the button's text color. Hidden from 768px, along with the menu it opens.

### HTML

```html
<!-- Pick one modifier: --x, --arrow or --collapse. Add aria-controls when it drives a real menu. -->
<button class="mnav-burger mnav-burger--x" type="button" aria-label="Menu" aria-expanded="false">
  <svg class="mnav-burger__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
    <path class="mnav-burger__line" d="M4 6h16" />
    <path class="mnav-burger__line" d="M4 12h16" />
    <path class="mnav-burger__line" d="M4 18h16" />
  </svg>
</button>

<button class="mnav-burger mnav-burger--arrow" type="button" aria-label="Menu" aria-expanded="false">
  <!-- same <svg> as above -->
</button>

<button class="mnav-burger mnav-burger--collapse" type="button" aria-label="Menu" aria-expanded="false">
  <!-- same <svg> as above -->
</button>
```

### CSS

```css
/* 44px button; the icon follows the button's text color */
.mnav-burger {
  --mnav-burger-delay: 150ms; /* pause between the two steps of --collapse */
  display: inline-grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0;
  border: 0; border-radius: var(--radius-md); background: transparent; color: var(--text-main); cursor: pointer;
  transition: background-color var(--transition-fast);
}
.mnav-burger:hover { background: var(--border-subtle); }
.mnav-burger:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.mnav-burger__icon {
  width: 1.5rem; height: 1.5rem; overflow: visible;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round;
}

/* Each line transforms around its own box; translate lengths are SVG units of the 24x24 viewBox */
.mnav-burger__line {
  transform-box: fill-box; transform-origin: center;
  transition: translate var(--transition-smooth), rotate var(--transition-smooth),
    scale var(--transition-smooth), opacity var(--transition-fast);
}

/* --x: outer lines meet in the middle and cross */
.mnav-burger--x[aria-expanded="true"] .mnav-burger__line:nth-child(1) { translate: 0 6px; rotate: 45deg; }
.mnav-burger--x[aria-expanded="true"] .mnav-burger__line:nth-child(2) { opacity: 0; }
.mnav-burger--x[aria-expanded="true"] .mnav-burger__line:nth-child(3) { translate: 0 -6px; rotate: -45deg; }

/* --arrow: outer lines halve and pivot on their left ends into a back arrow */
.mnav-burger--arrow .mnav-burger__line { transform-origin: left center; }
.mnav-burger--arrow[aria-expanded="true"] .mnav-burger__line:nth-child(1) { translate: 0 6px; rotate: -45deg; scale: 0.5 1; }
.mnav-burger--arrow[aria-expanded="true"] .mnav-burger__line:nth-child(3) { translate: 0 -6px; rotate: 45deg; scale: 0.5 1; }

/* --collapse: stack, then rotate. Each state lists its own step order; the delay sequences them */
.mnav-burger--collapse .mnav-burger__icon { transition: rotate var(--transition-fast); }
.mnav-burger--collapse .mnav-burger__line {
  transition: rotate var(--transition-fast),
    translate var(--transition-fast) var(--mnav-burger-delay), opacity var(--transition-fast) var(--mnav-burger-delay);
}
.mnav-burger--collapse[aria-expanded="true"] .mnav-burger__icon {
  rotate: 45deg; transition: rotate var(--transition-fast) var(--mnav-burger-delay);
}
.mnav-burger--collapse[aria-expanded="true"] .mnav-burger__line {
  transition: translate var(--transition-fast), opacity var(--transition-fast),
    rotate var(--transition-fast) var(--mnav-burger-delay);
}
.mnav-burger--collapse[aria-expanded="true"] .mnav-burger__line:nth-child(1) { translate: 0 6px; }
.mnav-burger--collapse[aria-expanded="true"] .mnav-burger__line:nth-child(2) { opacity: 0; }
.mnav-burger--collapse[aria-expanded="true"] .mnav-burger__line:nth-child(3) { translate: 0 -6px; rotate: 90deg; }

@media (prefers-reduced-motion: reduce) {
  .mnav-burger { --mnav-burger-delay: 0s; }
}
@media (min-width: 768px) {
  .mnav-burger { display: none; }
}
```

### JS

```js
// Demo only: flip aria-expanded and the CSS does the rest. Delete once a menu script owns the button.
document.querySelectorAll('.mnav-burger').forEach((btn) => {
  btn.addEventListener('click', () => {
    btn.setAttribute('aria-expanded', btn.getAttribute('aria-expanded') !== 'true');
  });
});
```

### Notes

- The state lives only in `aria-expanded`, so the icon can't drift from what assistive tech announces. Keep `aria-label="Menu"` in both states rather than switching it to "Close".
- It works as the toggle for 3. Accordion drawer as is: add `aria-controls` with the panel's id, add `hidden`, and delete the demo script. Pattern 3's script reveals the button and flips `aria-expanded`.
- `transform-box: fill-box` makes each line turn around its own box. It's supported in all current browsers.
- With reduced motion, the transition tokens collapse and the `--collapse` delay drops to 0, so every style switches instantly.

## 7. Scrollable link strip

A full-bleed row of category or section links that scrolls sideways with scroll snap, with edge fade masks that hint at more. `aria-current` marks the active link, and on load the script scrolls it to the middle of the strip (instantly with reduced motion). From 768px the links wrap and center, with no scrolling. Place it directly under your header.

### HTML

```html
<nav class="mnav-strip" aria-label="Service categories">
  <ul class="mnav-strip__list" role="list">
    <li><a class="mnav-strip__link" href="/services/roofing">Roofing</a></li>
    <li><a class="mnav-strip__link" href="/services/gutters">Gutters</a></li>
    <li><a class="mnav-strip__link" href="/services/siding">Siding</a></li>
    <li><a class="mnav-strip__link" href="/services/windows" aria-current="page">Windows</a></li>
    <li><a class="mnav-strip__link" href="/services/decks">Decks</a></li>
    <li><a class="mnav-strip__link" href="/services/painting">Painting</a></li>
    <li><a class="mnav-strip__link" href="/services/insulation">Insulation</a></li>
    <li><a class="mnav-strip__link" href="/services/repairs">Repairs</a></li>
  </ul>
</nav>
```

### CSS

```css
/* Full-bleed strip; the list is both the scroller and the inner wrapper */
.mnav-strip { background: var(--surface-light); border-bottom: 1px solid var(--border-subtle); }
.mnav-strip__list {
  /* Fades span the gutter, so nothing is faded at rest. Masks read alpha only: any opaque token works */
  --mnav-strip-fade: linear-gradient(to right, transparent, var(--surface-dark) var(--gutter),
    var(--surface-dark) calc(100% - var(--gutter)), transparent);
  display: flex; gap: var(--space-sm);
  max-width: var(--container-max); margin: 0 auto; padding: var(--space-sm) var(--gutter);
  list-style: none;
  overflow-x: auto; overscroll-behavior-x: contain; scrollbar-width: thin;
  scroll-snap-type: x proximity; scroll-padding-inline: var(--gutter);
  -webkit-mask-image: var(--mnav-strip-fade); mask-image: var(--mnav-strip-fade);
}

/* 44px pills; the current one is filled */
.mnav-strip__link {
  display: inline-flex; align-items: center; min-height: 2.75rem; padding: 0 var(--space-md);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-full);
  color: var(--text-main); font-weight: 500; white-space: nowrap; text-decoration: none;
  scroll-snap-align: center;
  transition: background-color var(--transition-fast), border-color var(--transition-fast);
}
.mnav-strip__link:hover { border-color: var(--text-muted); }
.mnav-strip__link[aria-current="page"], .mnav-strip__link[aria-current="true"] {
  border-color: var(--primary); background: var(--primary); color: var(--text-inverse);
}
.mnav-strip__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* From 768px: links wrap and center; no scrolling or fades */
@media (min-width: 768px) {
  .mnav-strip__list {
    flex-wrap: wrap; justify-content: center; overflow: visible;
    -webkit-mask-image: none; mask-image: none;
  }
}
```

### JS

```js
// On load, center the current link inside the strip. scrollBy on the list never moves the page.
const smooth = !matchMedia('(prefers-reduced-motion: reduce)').matches;
document.querySelectorAll('.mnav-strip__list').forEach((list) => {
  const current = list.querySelector('[aria-current="page"], [aria-current="true"]');
  if (!current) return;
  const l = list.getBoundingClientRect();
  const c = current.getBoundingClientRect();
  const left = c.left + c.width / 2 - (l.left + l.width / 2);
  list.scrollBy({ left, behavior: smooth ? 'smooth' : 'auto' }); // 'auto' is instant here
});
```

### Notes

- `scroll-snap-align: center` matches the script's centering, so proximity snapping doesn't pull the current link away again.
- The scrollbar is thin rather than hidden, for mouse users in narrow or zoomed windows. Tabbing also scrolls each link into view, and `scroll-padding` keeps it clear of the fades.
- For in-page section links, use `aria-current="true"` and move it as the sections scroll (not included).
- To pin the strip under a sticky header, add `position: sticky; top: <header height>; z-index: 5` to `.mnav-strip`.

## 8. Compact mobile top bar

A sticky bar (z-index 30) with a menu button on the left, a centered logo and a call button on the right (`tel:`). The menu button pairs with 3. Accordion drawer, whose script reveals it and keeps `aria-expanded` in sync, so the bar needs no JS of its own. Hidden from 768px, so show your desktop header (e.g. `components/navigation.md`) there.

### HTML

```html
<header class="mnav-topbar">
  <div class="mnav-topbar__inner">
    <!-- Ships hidden; the paired menu's script (3. Accordion drawer) reveals it -->
    <button class="mnav-topbar__menu" type="button" aria-label="Menu" aria-expanded="false" aria-controls="mnav-accordion-1" hidden>
      <svg class="mnav-topbar__icon mnav-topbar__icon--open" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h16" /></svg>
      <svg class="mnav-topbar__icon mnav-topbar__icon--close" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
    </button>
    <a class="mnav-topbar__logo" href="/">
      <img class="mnav-topbar__img" src="logo.svg" alt="Brand" width="120" height="32">
    </a>
    <a class="mnav-topbar__call" href="tel:+15555550123" aria-label="Call (555) 555-0123">
      <svg class="mnav-topbar__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5l1.5-2.5 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2" /></svg>
    </a>
  </div>
</header>
```

### CSS

```css
/* Sticky bar; env() clears the notch when the page uses viewport-fit=cover */
.mnav-topbar {
  position: sticky; top: 0; z-index: 30;
  padding-top: env(safe-area-inset-top, 0px);
  background: var(--surface-light); border-bottom: 1px solid var(--border-subtle);
}
/* Fixed side columns keep the logo centered, even while the menu button is hidden */
.mnav-topbar__inner {
  display: grid; grid-template-columns: 2.75rem 1fr 2.75rem; align-items: center; gap: var(--space-sm);
  min-height: 3.5rem; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter);
}
.mnav-topbar__menu { grid-column: 1; }
.mnav-topbar__logo { grid-column: 2; justify-self: center; display: flex; border-radius: var(--radius-sm); }
.mnav-topbar__img { display: block; width: auto; max-width: 100%; height: 2rem; }
.mnav-topbar__call { grid-column: 3; }

/* 44px round buttons: plain menu, filled call */
.mnav-topbar__menu, .mnav-topbar__call {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0;
  border: 0; border-radius: var(--radius-full); cursor: pointer;
  transition: background-color var(--transition-fast);
}
.mnav-topbar__menu { background: transparent; color: var(--text-main); }
.mnav-topbar__menu:hover { background: var(--border-subtle); }
.mnav-topbar__menu[hidden] { display: none; }
.mnav-topbar__call { background: var(--primary); color: var(--text-inverse); }
.mnav-topbar__call:hover { background: var(--primary-hover); }
.mnav-topbar__icon {
  width: 1.5rem; height: 1.5rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.mnav-topbar__menu:focus-visible, .mnav-topbar__logo:focus-visible, .mnav-topbar__call:focus-visible {
  outline: 2px solid transparent; box-shadow: var(--focus-ring);
}

/* Menu icon follows the drawer state */
.mnav-topbar__menu[aria-expanded="true"] .mnav-topbar__icon--open,
.mnav-topbar__menu:not([aria-expanded="true"]) .mnav-topbar__icon--close { display: none; }

@media (min-width: 768px) {
  .mnav-topbar { display: none; }
}
```

### Notes

- **Pair with 3. Accordion drawer.** Point `aria-controls` at the drawer panel's id, and set `.mnav-accordion { --mnav-accordion-top: calc(3.5rem + env(safe-area-inset-top, 0px)); }` so the drawer opens below the bar. The bar (30) stays above the drawer (20), so this button also closes it.
- To pair with 1 or 4 instead, point `aria-controls` at the dialog, replace `aria-expanded` with `aria-haspopup="dialog"`, and drop the close icon. That pattern's script reveals the button.
- Without a paired menu script, the menu button stays hidden and the logo stays centered.
- Below 768px this bar replaces `site-header` from `components/navigation.md`. Hide one of them so only one sticky bar shows. The call button is icon-only, so its `aria-label` carries the number.
