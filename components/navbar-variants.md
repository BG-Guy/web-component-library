# Navbar Variants

A base sticky navbar with an in-flow mobile panel (an alternative to the off-canvas drawer in `components/navigation.md`), plus seven variants that build on it. Depends on `tokens/variables.css`.

| #  | Pattern                                                                                   | JS               |
| -- | ----------------------------------------------------------------------------------------- | ---------------- |
| 1  | **Base navbar**: sticky bar; links + CTA from 768px, toggle and slide-down panel below     | ~19 lines        |
| 2  | **Transparent overlay navbar**: see-through over a dark hero, solid once it scrolls past   | ~7 lines + 1     |
| 3  | **Auto-hide navbar**: slides away on scroll down, returns on scroll up                     | ~16 lines + 1    |
| 4  | **Split navbar**: centered logo with links split left and right                            | 1 only           |
| 5  | **Dropdown navbar**: disclosure submenus, nested sections in the mobile panel              | ~22 lines + 1    |
| 6  | **Mega menu**: full-width panel with 3 link columns and a promo card                       | ~17 lines + 1    |
| 7  | **Utility bar navbar**: phone, hours, area and social strip above the bar                  | 1 only           |
| 8  | **Floating pill navbar**: detached, rounded bar with a frosted translucent background      | 1 only           |

## 1. Base navbar

Sticky bar (z-index 30). From 768px: brand left, links and CTA right. Below 768px: brand + toggle, which opens an in-flow panel that pushes the page down (no backdrop, no scroll lock). One `<nav>` serves both layouts.
Disclosure pattern: `aria-expanded`/`aria-controls` on the toggle, the closed panel is `visibility: hidden`, and Escape closes it and returns focus to the toggle.

### HTML

```html
<!-- In <head>: turns on the collapsed mobile layout before first paint (no flash of an open menu) -->
<script>document.documentElement.classList.add('navbar--js');</script>

<header class="navbar">
  <div class="navbar__inner">
    <a class="navbar__brand" href="/">
      <!-- <img src="logo.svg" alt="" width="32" height="32">  Logo only? Use alt="Brand". -->
      Brand
    </a>

    <button class="navbar__toggle" type="button" aria-label="Menu"
            aria-expanded="false" aria-controls="navbar-panel">
      <svg class="navbar__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
        <path class="navbar__icon-open" d="M4 6h16M4 12h16M4 18h16" />
        <path class="navbar__icon-close" d="M6 6l12 12M18 6 6 18" />
      </svg>
    </button>

    <div class="navbar__panel" id="navbar-panel">
      <div class="navbar__body">
        <nav class="navbar__nav" aria-label="Primary">
          <ul class="navbar__links" role="list">
            <li><a class="navbar__link" href="/services" aria-current="page">Services</a></li>
            <li><a class="navbar__link" href="/about">About</a></li>
            <li><a class="navbar__link" href="/reviews">Reviews</a></li>
            <li><a class="navbar__link" href="/contact">Contact</a></li>
          </ul>
        </nav>
        <a class="navbar__cta" href="/quote">Get a quote</a>
      </div>
    </div>
  </div>
</header>
```

### CSS

```css
/* Bar height, shared with the overlay sentinel (2) and the anchor scroll offset */
:root { --navbar-h: 4rem; }
html:has(.navbar) { scroll-padding-top: calc(var(--navbar-h) + var(--space-md)); }

/* Shell */
.navbar {
  position: sticky; top: 0; z-index: 30;
  background: var(--surface-light); color: var(--text-main);
  border-bottom: 1px solid var(--border-subtle);
  font-family: var(--font-sans);
}
/* No JS: the panel can't collapse, so don't pin an open menu to small screens */
:where(:root:not(.navbar--js)) .navbar { position: relative; }

/* Row 1: brand + toggle. On mobile the panel wraps to row 2. */
.navbar__inner {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; column-gap: var(--space-md);
  max-width: var(--container-max); margin-inline: auto;
  padding: calc((var(--navbar-h) - 2.75rem) / 2) var(--gutter);
}
.navbar__brand {
  display: inline-flex; align-items: center; gap: var(--space-sm); min-height: 2.75rem;
  border-radius: var(--radius-sm); color: inherit; font-size: 1.25rem; font-weight: 700; text-decoration: none;
}

/* Toggle: shown only under the JS gate; the icon follows aria-expanded */
.navbar__toggle {
  display: none; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0;
  border: 0; border-radius: var(--radius-md); background: transparent; color: inherit; cursor: pointer;
  transition: background-color var(--transition-fast);
}
:where(.navbar--js) .navbar__toggle { display: grid; }
.navbar__toggle:hover { background: var(--border-subtle); }
.navbar__icon { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; }
.navbar__toggle[aria-expanded="true"] .navbar__icon-open,
.navbar__toggle[aria-expanded="false"] .navbar__icon-close { display: none; }

/* Panel: slides open via grid rows; collapses (and leaves the a11y tree) only under the JS gate */
.navbar__panel {
  flex-basis: 100%; display: grid; grid-template-rows: 1fr;
  transition: grid-template-rows var(--transition-smooth), visibility var(--transition-smooth);
}
:where(.navbar--js .navbar:not([data-open])) .navbar__panel { grid-template-rows: 0fr; visibility: hidden; }
/* Scrolls when taller than the screen; inline padding leaves room for focus rings */
.navbar__body {
  display: flex; flex-direction: column; min-height: 0;
  max-height: calc(100vh - var(--navbar-h)); max-height: calc(100dvh - var(--navbar-h));
  overflow-y: auto; overscroll-behavior: contain;
  margin-inline: calc(-1 * var(--space-xs)); padding-inline: var(--space-xs);
}

/* Links: full-width rows in the panel, inline from 768px. Also styles the menu buttons in 5 and 6. */
.navbar__links { margin: 0; padding: var(--space-xs) 0 0; list-style: none; }
.navbar__link {
  display: flex; align-items: center; min-height: 2.75rem; padding: 0 var(--space-sm);
  border: 0; border-bottom: 1px solid var(--border-subtle); border-radius: 0; background: none;
  color: inherit; font: inherit; font-size: 1.125rem; font-weight: 500;
  text-decoration: none; text-decoration-thickness: 2px; text-underline-offset: 0.35em;
  transition: color var(--transition-fast);
}
.navbar__link:hover { color: var(--primary); }
.navbar__link[aria-current="page"] { color: var(--primary); text-decoration-line: underline; }

/* CTA: full-width in the panel, compact on the bar */
.navbar__cta {
  display: flex; align-items: center; justify-content: center; min-height: 2.75rem;
  margin-block: var(--space-md); padding: var(--space-sm) var(--space-lg);
  border-radius: var(--radius-md); background: var(--primary); color: var(--text-inverse);
  font-weight: 600; text-decoration: none; white-space: nowrap;
  transition: background-color var(--transition-fast);
}
.navbar__cta:hover { background: var(--primary-hover); }

/* Focus: the transparent outline keeps a ring in forced-colors mode */
.navbar a:focus-visible, .navbar button:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

@media (min-width: 768px) {
  .navbar { position: sticky; }
  .navbar__inner { flex-wrap: nowrap; }
  .navbar__toggle { display: none; }
  .navbar__panel { display: block; flex: 1; visibility: visible; }
  .navbar__body {
    flex-direction: row; align-items: center; justify-content: flex-end; gap: var(--space-lg);
    max-height: none; overflow: visible; margin: 0; padding: 0;
  }
  .navbar__links { display: flex; align-items: center; gap: var(--space-xs); padding: 0; }
  .navbar__link { border-bottom: 0; border-radius: var(--radius-sm); font-size: 1rem; }
  .navbar__cta { margin: 0; }
}
```

### JS

```js
// Gate (fallback for the <head> snippet), then wire each toggle as a disclosure
document.documentElement.classList.add('navbar--js');
const navbarWide = matchMedia('(min-width: 768px)');

document.querySelectorAll('.navbar').forEach((nav) => {
  const toggle = nav.querySelector('.navbar__toggle');
  if (!toggle) return;
  const panel = document.getElementById(toggle.getAttribute('aria-controls'));
  const setOpen = (open) => {
    toggle.setAttribute('aria-expanded', open);
    nav.toggleAttribute('data-open', open);
  };
  toggle.addEventListener('click', () => setOpen(!nav.hasAttribute('data-open')));
  // Escape closes the panel and returns focus to the toggle
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape' || !nav.hasAttribute('data-open')) return;
    setOpen(false);
    toggle.focus();
  });
  // Following a link (including #anchors) or widening to desktop closes it
  panel.addEventListener('click', (e) => e.target.closest('a') && setOpen(false));
  navbarWide.addEventListener('change', (e) => e.matches && setOpen(false));
});
```

### Notes

- One `<nav>` serves both layouts, so the link list isn't duplicated. The closed panel is `visibility: hidden`, so its links leave the tab order and the accessibility tree. Use disclosure buttons, never `role="menu"`.
- Without JS the toggle stays hidden, the links show as an open list, and the bar isn't sticky on phones. The `<head>` snippet sets the gate before first paint. If your CSP blocks inline scripts, drop it: the module sets the gate too, but the open menu may flash first.
- `grid-template-rows: 0fr → 1fr` animates the height in Chrome 107+, Safari 16+ and Firefox 66+. Older browsers open the panel instantly.
- `scroll-padding-top` keeps anchored sections and keyboard-focused elements out from under the sticky bar (WCAG 2.4.11).
- **React:** keep `open` in state, and render `aria-expanded={open}` on the toggle and `data-open={open || undefined}` on the header.

## 2. Transparent overlay navbar

Builds on 1. Base navbar. Sits over a dark hero with a transparent background and `--text-inverse` text. It turns solid (surface, border and shadow) once the hero has scrolled under it, which an IntersectionObserver detects with a sentinel inside the hero.
A scrim band behind the text keeps contrast at 4.5:1 or better in both states.

### HTML

```html
<!-- data-transparent: start see-through (JS corrects it). data-sentinel: the sentinel's id. -->
<header class="navbar navbar--overlay" data-transparent data-sentinel="overlay-sentinel">
  <!-- .navbar__inner exactly as in 1 (aria-controls="overlay-panel", id="overlay-panel") -->
</header>

<!-- Your dark hero (e.g. components/heroes.md). It needs position: relative and at least
     var(--navbar-h) of top padding, so its content clears the bar. -->
<section aria-labelledby="hero-title">
  <!-- First child. Spans the hero minus one bar height. -->
  <div class="navbar--overlay__sentinel" id="overlay-sentinel"></div>
  <!-- hero image, scrim, <h1 id="hero-title"> … -->
</section>
```

### CSS

```css
/* Overlap the hero by the bar's height. Always applied, so loading the JS causes no layout shift. */
.navbar--overlay {
  margin-bottom: calc(-1 * var(--navbar-h) - 1px);
  box-shadow: var(--shadow-md);
  transition: background-color var(--transition-smooth), border-color var(--transition-smooth),
    box-shadow var(--transition-smooth), color var(--transition-smooth);
}
/* Scrim band: 70% --surface-dark behind the text keeps --text-inverse above 4.5:1, even over white */
.navbar--overlay::before {
  content: ""; position: absolute; inset: 0 0 calc(-1 * var(--space-xl)); z-index: -1; pointer-events: none;
  background: linear-gradient(color-mix(in srgb, var(--surface-dark) 70%, transparent) 60%, transparent);
  opacity: 0; transition: opacity var(--transition-smooth);
}

/* Transparent state: JS gate on, still over the hero, mobile panel closed */
:where(.navbar--js) .navbar--overlay[data-transparent]:not([data-open]) {
  background-color: transparent; border-bottom-color: transparent; box-shadow: none; color: var(--text-inverse);
}
:where(.navbar--js) .navbar--overlay[data-transparent]:not([data-open])::before { opacity: 1; }
/* --primary is too dark on the scrim: links stay light, and the underline marks hover and current page */
:where(.navbar--js) .navbar--overlay[data-transparent]:not([data-open]) .navbar__link { color: inherit; }
:where(.navbar--js) .navbar--overlay[data-transparent]:not([data-open]) .navbar__link:hover { text-decoration-line: underline; }
:where(.navbar--js) .navbar--overlay[data-transparent]:not([data-open]) .navbar__toggle:hover {
  background: color-mix(in srgb, var(--text-inverse) 15%, transparent);
}
/* Focus on the dark backdrop: light outline */
:where(.navbar--js) .navbar--overlay[data-transparent]:not([data-open])
  :is(.navbar__brand, .navbar__link, .navbar__toggle, .navbar__cta):focus-visible {
  outline: 2px solid var(--text-inverse); outline-offset: 2px; box-shadow: none;
}

/* Sentinel: once it scrolls out of view, the bar has passed the hero */
.navbar--overlay__sentinel { position: absolute; inset: 0 0 var(--navbar-h); pointer-events: none; }
```

### JS

```js
// Transparent while the sentinel is on screen, solid once the bar has passed the hero
document.querySelectorAll('.navbar--overlay').forEach((nav) => {
  const sentinel = document.getElementById(nav.dataset.sentinel);
  if (!sentinel) return nav.removeAttribute('data-transparent'); // no hero: stay solid
  new IntersectionObserver((entries) => {
    nav.toggleAttribute('data-transparent', entries.at(-1).isIntersecting);
  }).observe(sentinel);
});
```

### Notes

- Contrast holds in both states. Solid uses the base surface (`--text-main` at 14.6:1). Transparent puts a 70% `--surface-dark` band behind the text, so `--text-inverse` stays above 4.5:1 even over a white photo. The current page is underlined rather than colored, because `--primary` fails on dark.
- Without JS the bar stays solid, because the transparent styles need the `navbar--js` gate. It still overlaps the hero's top padding.
- The sentinel spans the hero, so jumping far down the page with an anchor link still flips the bar to solid. If the hero isn't positioned, the sentinel falls back to roughly one viewport's height.
- An open mobile panel (`[data-open]`) always renders solid.

## 3. Auto-hide navbar

Builds on 1. Base navbar. Slides up out of view when scrolling down and comes back when scrolling up, with scroll checks throttled to one per frame. It stays in view while focus is inside it or its panel is open.
Under reduced motion it moves without sliding.

### HTML

```html
<header class="navbar navbar--autohide">
  <!-- .navbar__inner exactly as in 1 (aria-controls="autohide-panel", id="autohide-panel") -->
</header>
```

### CSS

```css
/* Slide up while JS marks it hidden; focus inside or an open panel keeps it in view */
.navbar--autohide { transition: transform var(--transition-smooth); }
.navbar--autohide[data-hidden]:not([data-open], :focus-within) { transform: translateY(-100%); }

/* Reduced motion: jump instead of sliding (the token already collapses; this makes it explicit) */
@media (prefers-reduced-motion: reduce) {
  .navbar--autohide { transition: none; }
}
```

### JS

```js
// Hide on scroll down, reveal on scroll up; at most one check per frame
document.querySelectorAll('.navbar--autohide').forEach((nav) => {
  let lastY = Math.max(scrollY, 0);
  let queued = false;
  const update = () => {
    queued = false;
    const y = Math.max(scrollY, 0); // ignore iOS rubber-band overscroll
    if (Math.abs(y - lastY) < 8) return; // dead zone against jitter
    nav.toggleAttribute('data-hidden', y > lastY && y > nav.offsetHeight);
    lastY = y;
  };
  addEventListener('scroll', () => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(update);
  }, { passive: true });
});
```

### Notes

- The bar moves off-screen but deliberately stays in the tab order and accessibility tree, like a skip link. Tab or Shift+Tab into it and `:focus-within` brings it back, so focus is never hidden (WCAG 2.4.11).
- The script only toggles `data-hidden`, and the slide is a CSS transition. The motion tokens and the media query make it an instant show/hide under reduced motion, so the JS needs no `matchMedia` check.
- It only hides once scrolled past its own height, so the top of the page always shows it.
- Older browsers that don't accept a selector list inside `:not()` ignore the rule, and the bar just stays put.

## 4. Split navbar

Builds on 1. Base navbar. From 768px the logo is centered, with links split to either side and the CTA ending the right-hand list. Below 768px it's the standard brand + toggle + panel.

### HTML

```html
<header class="navbar navbar--split">
  <div class="navbar__inner">
    <a class="navbar__brand" href="/">Brand</a>
    <!-- .navbar__toggle as in 1, with aria-controls="split-panel" -->
    <div class="navbar__panel" id="split-panel">
      <div class="navbar__body">
        <nav class="navbar__nav" aria-label="Primary">
          <ul class="navbar__links navbar--split__start" role="list">
            <li><a class="navbar__link" href="/services" aria-current="page">Services</a></li>
            <li><a class="navbar__link" href="/about">About</a></li>
          </ul>
          <ul class="navbar__links navbar--split__end" role="list">
            <li><a class="navbar__link" href="/reviews">Reviews</a></li>
            <li><a class="navbar__link" href="/contact">Contact</a></li>
            <li><a class="navbar__cta" href="/quote">Get a quote</a></li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</header>
```

### CSS

```css
@media (min-width: 768px) {
  /* Equal side columns keep the brand truly centered */
  .navbar--split .navbar__inner { display: grid; grid-template-columns: 1fr auto 1fr; }
  /* Sits above the nav's box so it stays clickable */
  .navbar--split .navbar__brand { grid-area: 1 / 2; position: relative; z-index: 1; }
  /* Dissolve the wrapper divs only; the <nav> and lists keep their boxes and semantics */
  .navbar--split .navbar__panel, .navbar--split .navbar__body { display: contents; }
  /* The nav spans all three columns; flex fallback pushes the lists to the edges */
  .navbar--split .navbar__nav {
    grid-area: 1 / 1 / 2 / 4; display: flex; justify-content: space-between;
    grid-template-columns: subgrid;
  }
  .navbar--split__end { grid-column: 3; justify-content: flex-end; }
  .navbar--split__end .navbar__cta { margin-inline-start: var(--space-md); }
}

/* Subgrid lines the lists up with the side columns, so they can never run under the brand */
@supports (grid-template-columns: subgrid) {
  @media (min-width: 768px) {
    .navbar--split .navbar__nav { display: grid; }
  }
}
```

### Notes

- Subgrid works in Chrome 117+, Safari 16+ and Firefox 71+. Without it, the lists sit at the far edges with the brand centered over the gap, so keep each side short.
- `display: contents` is applied only to the two wrapper `<div>`s, never to `<nav>` or `<ul>`, because older Safari dropped landmark and list semantics on those.
- The tab order is brand, left links, then right links, while the brand sits visually in the middle. A logo-first order is the accepted convention; don't reorder links with CSS `order`.
- Balance the two sides. On mobile both lists stack into one column in the panel.

## 5. Dropdown navbar

Builds on 1. Base navbar. Top-level disclosure buttons open submenus (lists of links), one at a time. Escape closes a submenu and returns focus to its button; outside clicks and tabbing away also close it.
On mobile each submenu becomes a nested expandable section in the panel. Hover-to-open is only a mouse-and-desktop enhancement.

### HTML

```html
<!-- Inside .navbar__links from 1. Keep each menu directly after its button. -->
<li class="navbar-dropdown">
  <button class="navbar__link navbar-dropdown__toggle" type="button"
          aria-expanded="false" aria-controls="dropdown-services">
    Services
    <svg class="navbar-dropdown__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
  </button>
  <ul class="navbar-dropdown__menu" id="dropdown-services" role="list">
    <li><a class="navbar-dropdown__link" href="/services/roofing" aria-current="page">Roofing</a></li>
    <li><a class="navbar-dropdown__link" href="/services/gutters">Gutters</a></li>
    <li><a class="navbar-dropdown__link" href="/services/siding">Siding</a></li>
    <li><a class="navbar-dropdown__link" href="/services">All services</a></li>
  </ul>
</li>
<!-- --end aligns the menu to the item's right edge; use it near the right of the bar -->
<li class="navbar-dropdown navbar-dropdown--end">
  <button class="navbar__link navbar-dropdown__toggle" type="button"
          aria-expanded="false" aria-controls="dropdown-company">
    Company
    <svg class="navbar-dropdown__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
  </button>
  <ul class="navbar-dropdown__menu" id="dropdown-company" role="list">
    <li><a class="navbar-dropdown__link" href="/about">About us</a></li>
    <li><a class="navbar-dropdown__link" href="/reviews">Reviews</a></li>
    <li><a class="navbar-dropdown__link" href="/careers">Careers</a></li>
  </ul>
</li>
<li><a class="navbar__link" href="/contact">Contact</a></li>
```

### CSS

```css
/* Menu button: reuses .navbar__link; the chevron flips when open */
.navbar-dropdown__toggle { justify-content: space-between; gap: var(--space-xs); width: 100%; cursor: pointer; text-align: start; }
.navbar-dropdown__icon {
  width: 1rem; height: 1rem; fill: none; stroke: currentColor; stroke-width: 2;
  stroke-linecap: round; stroke-linejoin: round; transition: transform var(--transition-fast);
}
.navbar-dropdown__toggle[aria-expanded="true"] .navbar-dropdown__icon { transform: rotate(180deg); }

/* Submenu: a nested section in the mobile panel. Collapsed menus are display:none (JS gate). */
.navbar-dropdown__menu { margin: 0; padding: var(--space-xs) 0 var(--space-sm) var(--space-md); list-style: none; }
:where(.navbar--js) .navbar-dropdown__toggle[aria-expanded="false"] + .navbar-dropdown__menu { display: none; }
.navbar-dropdown__link {
  display: flex; align-items: center; min-height: 2.75rem; padding-inline: var(--space-sm);
  border-radius: var(--radius-sm); color: var(--text-main); text-decoration: none;
  text-decoration-thickness: 2px; text-underline-offset: 0.35em; transition: color var(--transition-fast);
}
.navbar-dropdown__link:hover { color: var(--primary); }
.navbar-dropdown__link[aria-current="page"] { color: var(--primary); text-decoration-line: underline; }

/* Desktop: a card under its button */
@media (min-width: 768px) {
  .navbar-dropdown { position: relative; }
  .navbar-dropdown__toggle { width: auto; }
  .navbar-dropdown__menu {
    position: absolute; top: 100%; left: 0; z-index: 1; min-width: 13rem;
    padding: var(--space-sm); background: var(--surface-light);
    border: 1px solid var(--border-subtle); border-radius: var(--radius-md); box-shadow: var(--shadow-lg);
  }
  .navbar-dropdown--end .navbar-dropdown__menu { left: auto; right: 0; }
  /* No-JS fallback: open on hover or keyboard focus */
  :root:not(.navbar--js) .navbar-dropdown:not(:hover, :focus-within) .navbar-dropdown__menu { display: none; }
}
```

### JS

```js
// Disclosure submenus: one open at a time; Escape, outside click and tabbing away close them
const ddToggles = [...document.querySelectorAll('.navbar-dropdown__toggle')];
const ddHover = matchMedia('(min-width: 768px) and (hover: hover)');
const ddSet = (btn, open) => {
  if (open) ddToggles.forEach((b) => b !== btn && b.setAttribute('aria-expanded', 'false'));
  btn.setAttribute('aria-expanded', open);
};

ddToggles.forEach((btn) => {
  const item = btn.closest('.navbar-dropdown');
  let hovered = false;
  // While the mouse is over the item, a click keeps it open instead of toggling it shut
  btn.addEventListener('click', () => ddSet(btn, hovered || btn.getAttribute('aria-expanded') !== 'true'));
  item.addEventListener('focusout', (e) => e.relatedTarget && !item.contains(e.relatedTarget) && ddSet(btn, false));
  // Optional enhancement: hover opens for a mouse on desktop (assignments return the new state)
  item.addEventListener('pointerenter', (e) => e.pointerType === 'mouse' && ddHover.matches && ddSet(btn, (hovered = true)));
  item.addEventListener('pointerleave', () => hovered && ddSet(btn, (hovered = false)));
});

document.addEventListener('click', (e) => e.target.closest('.navbar-dropdown') || ddToggles.forEach((b) => ddSet(b, false)));

// Capture phase: the first Escape closes the submenu (not the mobile panel) and returns focus
document.addEventListener('keydown', (e) => {
  const btn = ddToggles.find((b) => b.getAttribute('aria-expanded') === 'true');
  if (e.key !== 'Escape' || !btn) return;
  e.stopPropagation();
  if (btn.closest('.navbar-dropdown').contains(document.activeElement)) btn.focus();
  ddSet(btn, false);
}, true);
```

### Notes

- This is the WAI-ARIA APG disclosure navigation pattern: buttons plus plain link lists, with no `role="menu"` and no arrow-key roving. CSS hides each menu with `[aria-expanded="false"] + .navbar-dropdown__menu`, so the button's state is the only state and the menu must follow its button.
- Escape is handled in the capture phase and only stops there while a submenu is open. The first press closes the submenu, and the next closes the mobile panel.
- Hover opens menus only for a mouse at 768px+ with `hover: hover`. Without JS, desktop menus open on `:hover` and `:focus-within`, and phones show them expanded.
- Tabbing out of an item closes it, so an open menu never covers the next focused element (WCAG 2.4.11).

## 6. Mega menu

Builds on 1. Base navbar. A disclosure opens a full-width panel under the bar with three link columns and a featured promo card. It has the same keyboard and close behavior as 5: Escape returns focus, and outside clicks or tabbing away close it.
On mobile everything stacks inside the menu panel.

### HTML

```html
<!-- Inside .navbar__links from 1. Keep the panel directly after its button. -->
<li class="navbar-mega">
  <button class="navbar__link navbar-mega__toggle" type="button"
          aria-expanded="false" aria-controls="mega-services">
    Services
    <svg class="navbar-mega__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
  </button>
  <div class="navbar-mega__panel" id="mega-services">
    <div class="navbar-mega__inner">
      <div>
        <p class="navbar-mega__heading" id="mega-repairs">Repairs</p>
        <ul class="navbar-mega__list" role="list" aria-labelledby="mega-repairs">
          <li><a class="navbar-mega__link" href="/services/leaks">Leak repair</a></li>
          <li><a class="navbar-mega__link" href="/services/drains">Drain cleaning</a></li>
          <li><a class="navbar-mega__link" href="/services/water-heaters">Water heaters</a></li>
        </ul>
      </div>
      <div>
        <p class="navbar-mega__heading" id="mega-installs">Installs</p>
        <ul class="navbar-mega__list" role="list" aria-labelledby="mega-installs">
          <li><a class="navbar-mega__link" href="/services/fixtures">Fixtures</a></li>
          <li><a class="navbar-mega__link" href="/services/softeners">Water softeners</a></li>
          <li><a class="navbar-mega__link" href="/services/sump-pumps">Sump pumps</a></li>
        </ul>
      </div>
      <div>
        <p class="navbar-mega__heading" id="mega-care">Maintenance</p>
        <ul class="navbar-mega__list" role="list" aria-labelledby="mega-care">
          <li><a class="navbar-mega__link" href="/services/tune-up">Annual tune-up</a></li>
          <li><a class="navbar-mega__link" href="/services/inspections">Home inspections</a></li>
          <li><a class="navbar-mega__link" href="/services/plans">Service plans</a></li>
        </ul>
      </div>
      <a class="navbar-mega__promo" href="/offers/tune-up">
        <img class="navbar-mega__promo-img" src="tune-up.jpg" alt="" width="400" height="250" loading="lazy">
        <span class="navbar-mega__promo-title">Spring tune-up: 15% off</span>
        <span class="navbar-mega__promo-text">Book by May 31 · Springfield area</span>
      </a>
    </div>
  </div>
</li>
```

### CSS

```css
/* Menu button: reuses .navbar__link; the chevron flips when open */
.navbar-mega__toggle { justify-content: space-between; gap: var(--space-xs); width: 100%; cursor: pointer; text-align: start; }
.navbar-mega__icon {
  width: 1rem; height: 1rem; fill: none; stroke: currentColor; stroke-width: 2;
  stroke-linecap: round; stroke-linejoin: round; transition: transform var(--transition-fast);
}
.navbar-mega__toggle[aria-expanded="true"] .navbar-mega__icon { transform: rotate(180deg); }

/* Panel: stacked inside the mobile menu. Collapsed panels are display:none (JS gate). */
.navbar-mega__panel { color: var(--text-main); }
:where(.navbar--js) .navbar-mega__toggle[aria-expanded="false"] + .navbar-mega__panel { display: none; }
.navbar-mega__inner { display: grid; gap: var(--space-lg); padding: var(--space-sm) 0 var(--space-md) var(--space-md); }
.navbar-mega__heading {
  margin: 0 0 var(--space-xs); padding-inline: var(--space-sm); color: var(--text-muted);
  font-size: 0.75rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase;
}
.navbar-mega__list { margin: 0; padding: 0; list-style: none; }
.navbar-mega__link {
  display: flex; align-items: center; min-height: 2.75rem; padding-inline: var(--space-sm);
  border-radius: var(--radius-sm); color: inherit; text-decoration: none; transition: color var(--transition-fast);
}
.navbar-mega__link:hover { color: var(--primary); }

/* Promo card */
.navbar-mega__promo {
  display: grid; gap: var(--space-xs); align-content: start; padding: var(--space-md);
  border-radius: var(--radius-lg); background: var(--surface-muted); color: inherit; text-decoration: none;
}
.navbar-mega__promo-img {
  display: block; width: 100%; height: auto; aspect-ratio: 8 / 5; object-fit: cover; border-radius: var(--radius-md);
}
.navbar-mega__promo-title { font-weight: 700; transition: color var(--transition-fast); }
.navbar-mega__promo:hover .navbar-mega__promo-title { color: var(--primary); }
.navbar-mega__promo-text { color: var(--text-muted); font-size: 0.875rem; }

/* Desktop: full-width panel under the bar (positioned against the sticky .navbar) */
@media (min-width: 768px) {
  .navbar-mega__toggle { position: relative; width: auto; }
  .navbar-mega__panel {
    position: absolute; inset: 100% 0 auto; z-index: 1;
    max-height: calc(100vh - var(--navbar-h)); max-height: calc(100dvh - var(--navbar-h)); overflow-y: auto;
    background: var(--surface-light); border-top: 1px solid var(--border-subtle); box-shadow: var(--shadow-lg);
  }
  .navbar-mega__inner {
    grid-template-columns: repeat(3, minmax(0, 1fr)) minmax(0, 1.25fr); gap: var(--space-xl);
    max-width: var(--container-max); margin-inline: auto; padding: var(--space-xl) var(--gutter);
  }
  /* No-JS fallback: open on hover or keyboard focus; ::after bridges the gap down to the panel */
  :root:not(.navbar--js) .navbar-mega:not(:hover, :focus-within) .navbar-mega__panel { display: none; }
  :root:not(.navbar--js) .navbar-mega__toggle::after {
    content: ""; position: absolute; inset: 100% 0 calc(-1 * var(--space-md));
  }
}
```

### JS

```js
// Mega panels: one open at a time; Escape, outside click and tabbing away close them
const megaToggles = [...document.querySelectorAll('.navbar-mega__toggle')];
const megaSet = (btn, open) => btn.setAttribute('aria-expanded', open);

megaToggles.forEach((btn) => {
  const item = btn.closest('.navbar-mega');
  btn.addEventListener('click', () => megaSet(btn, btn.getAttribute('aria-expanded') !== 'true'));
  item.addEventListener('focusout', (e) => e.relatedTarget && !item.contains(e.relatedTarget) && megaSet(btn, false));
});

// A click outside an item closes it, so opening one panel closes the others
document.addEventListener('click', (e) => {
  megaToggles.forEach((b) => b.closest('.navbar-mega').contains(e.target) || megaSet(b, false));
});

// Capture phase: the first Escape closes the panel (not the mobile menu) and returns focus
document.addEventListener('keydown', (e) => {
  const btn = megaToggles.find((b) => b.getAttribute('aria-expanded') === 'true');
  if (e.key !== 'Escape' || !btn) return;
  e.stopPropagation();
  if (btn.closest('.navbar-mega').contains(document.activeElement)) btn.focus();
  megaSet(btn, false);
}, true);
```

### Notes

- The panel is positioned against the sticky `.navbar`, so it spans the full bar. Don't add `position` to the `<li>` or to the bar's wrapper `<div>`s.
- Column titles are `<p>` elements referenced by each list's `aria-labelledby`, not headings, so the page outline still starts at its `<h1>`.
- `max-height` plus scrolling keeps the panel usable on short screens. The lazy promo image loads only when the panel first shows.
- If 5 and 6 share a bar, each script's outside-click handler closes the other's menu, so only one is ever open. Mega menus are click-only: a full-width panel opening on hover gets in the way.

## 7. Utility bar navbar

Builds on 1. Base navbar. A slim dark strip above the main bar holds the phone link, hours, service area and social links. It scrolls away while the main bar sticks. On mobile only the phone link remains.

### HTML

```html
<header class="navbar">
  <div class="navbar-utility">
    <div class="navbar-utility__inner">
      <a class="navbar-utility__phone" href="tel:+15555550123">
        <svg class="navbar-utility__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
          <rect x="7" y="2" width="10" height="20" rx="2" /><path d="M11 18h2" />
        </svg>
        <span class="navbar-utility__sr">Call </span>(555) 555-0123
      </a>
      <p class="navbar-utility__item">Mon–Sat, 7am–6pm</p>
      <p class="navbar-utility__item">Serving Springfield &amp; nearby</p>
      <!-- Generic placeholder icons: swap in each network's official mark -->
      <ul class="navbar-utility__social" role="list">
        <li><a class="navbar-utility__social-link" href="https://example.com/photos" aria-label="Brand photo feed">
          <svg class="navbar-utility__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><rect x="3" y="7" width="18" height="13" rx="2" /><circle cx="12" cy="13.5" r="3" /><path d="M9 7l1-3h4l1 3" /></svg>
        </a></li>
        <li><a class="navbar-utility__social-link" href="https://example.com/videos" aria-label="Brand video channel">
          <svg class="navbar-utility__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><rect x="2" y="5" width="20" height="14" rx="3" /><path d="m10 9 5 3-5 3z" /></svg>
        </a></li>
        <li><a class="navbar-utility__social-link" href="https://example.com/community" aria-label="Brand community page">
          <svg class="navbar-utility__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z" /></svg>
        </a></li>
      </ul>
    </div>
  </div>
  <!-- .navbar__inner exactly as in 1 (aria-controls="utility-panel", id="utility-panel") -->
</header>
```

### CSS

```css
/* The header sticks at minus the strip's height, so the strip scrolls away and the main bar stays */
.navbar:has(> .navbar-utility) { --navbar-utility-h: 2.5rem; top: calc(-1 * var(--navbar-utility-h)); }

/* Slim dark strip with a fixed height */
.navbar-utility {
  height: var(--navbar-utility-h, 2.5rem);
  background: var(--surface-dark); color: var(--text-inverse-muted); font-size: 0.875rem;
}
.navbar-utility__inner {
  display: flex; align-items: center; justify-content: center; gap: var(--space-lg);
  height: 100%; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter);
  white-space: nowrap;
}
.navbar-utility__phone {
  display: inline-flex; align-items: center; gap: var(--space-xs); min-height: 2rem;
  color: var(--text-inverse); font-weight: 600; text-decoration: none;
}
.navbar-utility__phone:hover { text-decoration: underline; }
.navbar-utility__icon {
  width: 1rem; height: 1rem; fill: none; stroke: currentColor; stroke-width: 2;
  stroke-linecap: round; stroke-linejoin: round;
}

/* Mobile: phone link only */
.navbar-utility__item, .navbar-utility__social { display: none; margin: 0; }
.navbar-utility__social { padding: 0; list-style: none; }
.navbar-utility__social-link {
  display: grid; place-items: center; width: 2rem; height: 2rem; border-radius: var(--radius-sm);
  color: var(--text-inverse-muted); transition: color var(--transition-fast);
}
.navbar-utility__social-link:hover { color: var(--text-inverse); }
.navbar-utility__social-link .navbar-utility__icon { width: 1.125rem; height: 1.125rem; }

/* Focus on the dark strip: light outline */
.navbar-utility a:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; box-shadow: none; }
.navbar-utility__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

@media (min-width: 768px) {
  .navbar-utility__inner { justify-content: flex-start; }
  .navbar-utility__item { display: block; }
  .navbar-utility__social { display: flex; gap: var(--space-xs); margin-inline-start: auto; }
}
```

### Notes

- The strip sits inside `<header>`, so it's part of the banner landmark. The negative sticky `top` scrolls it away and pins the main bar. This needs `:has()` (all current browsers). Without it, the whole header sticks. Keep the strip at a fixed height (`--navbar-utility-h`) so the offset matches.
- The phone link's accessible name is "Call (555) 555-0123": a visually hidden "Call" plus the visible number, which keeps the label in the name (WCAG 2.5.3).
- The social icons are generic placeholders. Use each network's official icon and set `aria-label` to "Brand on <network>".
- `white-space: nowrap` keeps the strip on one line. If you add items, check it at 768px, or reveal the extras at 1024px.

## 8. Floating pill navbar

Builds on 1. Base navbar. A detached, rounded bar inset from the viewport edges, with a translucent blurred background (`backdrop-filter`) and a solid fallback through `@supports`. Text stays at 4.5:1 or better in both cases.

### HTML

```html
<header class="navbar navbar--pill">
  <!-- .navbar__inner exactly as in 1 (aria-controls="pill-panel", id="pill-panel") -->
</header>
```

### CSS

```css
/* Detached bar: inset from the viewport edges, rounded and elevated; slimmer than the base */
.navbar--pill {
  --navbar-h: 3.5rem;
  --navbar-pill-blur: 0.75rem;
  top: var(--space-sm);
  box-sizing: border-box; width: calc(100% - 2 * var(--space-sm)); max-width: var(--container-max);
  margin: var(--space-sm) auto 0;
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  background: var(--surface-light); /* solid fallback */
  box-shadow: var(--shadow-lg);
}
/* The open mobile panel must fit below the pill's top gap */
.navbar--pill .navbar__body {
  max-height: calc(100vh - var(--navbar-h) - var(--space-xl));
  max-height: calc(100dvh - var(--navbar-h) - var(--space-xl));
}

/* Frosted glass where supported: an 85% surface keeps --text-main above 4.5:1 over any backdrop */
@supports ((-webkit-backdrop-filter: blur(1px)) or (backdrop-filter: blur(1px))) {
  .navbar--pill {
    background: color-mix(in srgb, var(--surface-light) 85%, transparent);
    -webkit-backdrop-filter: blur(var(--navbar-pill-blur));
    backdrop-filter: blur(var(--navbar-pill-blur));
  }
}
/* People who ask for less transparency get the solid bar */
@media (prefers-reduced-transparency: reduce) {
  .navbar--pill { background: var(--surface-light); -webkit-backdrop-filter: none; backdrop-filter: none; }
}

/* --primary text can drop below 4.5:1 on glass: links keep --text-main and show state with an underline */
.navbar--pill .navbar__link:hover,
.navbar--pill .navbar__link[aria-current="page"] { color: inherit; text-decoration-line: underline; }

@media (min-width: 768px) {
  .navbar--pill {
    top: var(--space-md); width: calc(100% - 2 * var(--space-md));
    margin-top: var(--space-md); border-radius: var(--radius-full);
  }
}
```

### Notes

- `backdrop-filter` works in Chrome 76+, Safari 9+ (prefixed before 18) and Firefox 103+. Without it, or under `prefers-reduced-transparency: reduce` (Chrome 118+), the bar is solid `--surface-light`.
- Over pure black, the 85% tint still gives `--text-main` about 10:1. `--primary` text would fail, so links show hover and current page with an underline. The CTA is opaque.
- `backdrop-filter` makes the bar the containing block for `position: fixed` descendants, so keep modals and drawers outside the header.
- `--navbar-h` is overridden only inside the pill (3.5rem). The root value still drives `scroll-padding-top`, which covers the bar plus its top gap.
