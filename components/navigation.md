# Navigation

Sticky header with a slide-out mobile drawer. Depends on `tokens/variables.css`.

- **≥768px:** brand left · links centered · CTA right.
- **<768px:** brand + hamburger. The drawer slides in from the right, below the header, over a backdrop.
- **A11y:** disclosure pattern. A `<button aria-expanded aria-controls>` toggles a `<nav>`. The closed drawer is `visibility: hidden`, so its links leave the tab order. Escape closes it and returns focus to the toggle.

## HTML

Keep the drawer directly after `<header>` so Tab moves from the toggle into the open drawer.

```html
<header class="site-header">
  <div class="site-header__inner">
    <a class="site-header__brand" href="/">
      <!-- <img src="logo.svg" alt="" width="32" height="32">  Logo only? Use alt="Brand name". -->
      Brand
    </a>

    <nav class="site-header__nav" aria-label="Primary">
      <ul class="site-header__links" role="list">
        <li><a href="/services" aria-current="page">Services</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/reviews">Reviews</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>

    <a class="nav-cta" href="/quote">Get a quote</a>

    <button class="site-header__toggle" type="button" aria-label="Menu"
            aria-expanded="false" aria-controls="mobile-drawer">
      <svg class="icon-open" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
        <path d="M4 6h16M4 12h16M4 18h16" />
      </svg>
      <svg class="icon-close" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
        <path d="M6 6l12 12M18 6 6 18" />
      </svg>
    </button>
  </div>
</header>

<div class="nav-backdrop"></div>
<nav id="mobile-drawer" class="nav-drawer" aria-label="Mobile">
  <ul class="nav-drawer__links" role="list">
    <li><a href="/services" aria-current="page">Services</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/reviews">Reviews</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
  <a class="nav-cta" href="/quote">Get a quote</a>
</nav>
```

## CSS

```css
:root { --header-h: 4rem; } /* module-local: shared by header and drawer */

.site-header {
  position: sticky; top: 0; z-index: 30;
  background: var(--surface-light);
  border-bottom: 1px solid var(--border-subtle);
}
.site-header__inner {
  display: flex; align-items: center; justify-content: space-between; gap: var(--space-md);
  min-height: var(--header-h); max-width: var(--container-max);
  margin-inline: auto; padding-inline: var(--gutter);
}
.site-header__brand {
  display: inline-flex; align-items: center; gap: var(--space-sm); justify-self: start;
  font-size: 1.25rem; font-weight: 700; color: var(--text-main); text-decoration: none;
}

/* Links */
.site-header__links { display: flex; gap: var(--space-lg); margin: 0; padding: 0; list-style: none; }
.nav-drawer__links { margin: 0; padding: 0; list-style: none; }
.site-header__links a, .nav-drawer__links a {
  color: var(--text-main); font-weight: 500; text-decoration: none;
  transition: color var(--transition-fast);
}
.nav-drawer__links a {
  display: block; padding-block: var(--space-sm);
  font-size: 1.125rem; border-bottom: 1px solid var(--border-subtle);
}
.site-header__links a:hover, .nav-drawer__links a:hover,
.site-header__links [aria-current="page"], .nav-drawer__links [aria-current="page"] { color: var(--primary); }

/* CTA button */
.nav-cta {
  align-items: center; justify-content: center;
  min-height: 2.75rem; padding: var(--space-sm) var(--space-lg);
  border-radius: var(--radius-md);
  background: var(--primary); color: var(--text-inverse);
  font-weight: 600; text-decoration: none;
  transition: background-color var(--transition-fast);
}
.nav-cta:hover { background: var(--primary-hover); }

/* Focus: transparent outline keeps a visible ring in Windows forced-colors mode */
.site-header a:focus-visible, .site-header button:focus-visible, .nav-drawer a:focus-visible {
  outline: 2px solid transparent; box-shadow: var(--focus-ring);
}

/* Hamburger toggle: icon follows aria-expanded */
.site-header__toggle {
  display: grid; place-items: center;
  width: 2.75rem; height: 2.75rem; padding: 0; /* 44px touch target */
  border: 0; border-radius: var(--radius-md);
  background: transparent; color: var(--text-main); cursor: pointer;
  transition: background-color var(--transition-fast);
}
.site-header__toggle:hover { background: var(--border-subtle); }
.site-header__toggle svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; }
.site-header__toggle[aria-expanded="true"] .icon-open,
.site-header__toggle[aria-expanded="false"] .icon-close { display: none; }

/* Mobile: header shows brand + toggle only */
.site-header__nav, .site-header .nav-cta { display: none; }

/* Drawer + backdrop. visibility transitions with transform, so it hides only after sliding out. */
.nav-drawer {
  position: fixed; inset: var(--header-h) 0 0 auto; z-index: 20;
  box-sizing: border-box; width: min(20rem, 85vw);
  padding: var(--space-lg) var(--gutter);
  overflow-y: auto; overscroll-behavior: contain;
  background: var(--surface-light); box-shadow: var(--shadow-lg);
  transform: translateX(100%); visibility: hidden;
  transition: transform var(--transition-smooth), visibility var(--transition-smooth);
}
.nav-drawer .nav-cta { display: flex; margin-top: var(--space-lg); }
.nav-backdrop {
  position: fixed; inset: var(--header-h) 0 0; z-index: 10;
  background: color-mix(in srgb, var(--surface-dark) 50%, transparent);
  opacity: 0; visibility: hidden;
  transition: opacity var(--transition-smooth), visibility var(--transition-smooth);
}
.nav-drawer[data-open], .nav-backdrop[data-open] { transform: none; opacity: 1; visibility: visible; }

@media (max-width: 767.98px) {
  html:has(.nav-drawer[data-open]) { overflow: hidden; } /* lock page scroll while open */
}

@media (min-width: 768px) {
  .site-header__inner { display: grid; grid-template-columns: 1fr auto 1fr; }
  .site-header__nav { display: block; }
  .site-header .nav-cta { display: inline-flex; justify-self: end; }
  .site-header__toggle, .nav-drawer, .nav-backdrop { display: none; }
}
```

## JS

```js
const toggle = document.querySelector('.site-header__toggle');
const drawer = document.getElementById(toggle.getAttribute('aria-controls'));
const backdrop = document.querySelector('.nav-backdrop');

function setOpen(open) {
  toggle.setAttribute('aria-expanded', open);
  drawer.toggleAttribute('data-open', open);
  backdrop.toggleAttribute('data-open', open);
}

toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
backdrop.addEventListener('click', () => setOpen(false));
drawer.addEventListener('click', (e) => e.target.closest('a') && setOpen(false));
document.addEventListener('keydown', (e) => {
  if (e.key !== 'Escape' || !drawer.hasAttribute('data-open')) return;
  setOpen(false);
  toggle.focus();
});
```

## Adapting

`aria-expanded` on the toggle and `data-open` on the drawer and backdrop are the only state. Every setup below keeps those two attributes, the `aria-controls`/`id` pair, and the Escape-returns-focus behavior.

### Vanilla HTML
- Link `tokens/variables.css`, then this CSS. Load the script with `defer` or at the end of `<body>`.
- `aria-controls` must match the drawer's `id`. Rename both together.

### React / JSX
State replaces the DOM writes. Markup, classes and CSS stay the same.

```jsx
import { useEffect, useRef, useState } from 'react';

export function SiteHeader() {
  const [open, setOpen] = useState(false);
  const toggleRef = useRef(null);
  const dataOpen = open ? '' : undefined; // renders data-open only when open

  useEffect(() => {
    if (!open) return;
    const onKey = (e) => {
      if (e.key === 'Escape') { setOpen(false); toggleRef.current.focus(); }
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, [open]);

  return (
    <>
      <header className="site-header">
        <div className="site-header__inner">
          {/* brand, nav and .nav-cta as in the HTML above */}
          <button ref={toggleRef} className="site-header__toggle" type="button" aria-label="Menu"
                  aria-expanded={open} aria-controls="mobile-drawer" onClick={() => setOpen(!open)}>
            {/* both SVGs as above */}
          </button>
        </div>
      </header>
      <div className="nav-backdrop" data-open={dataOpen} onClick={() => setOpen(false)} />
      <nav id="mobile-drawer" className="nav-drawer" aria-label="Mobile" data-open={dataOpen}
           onClick={(e) => e.target.closest('a') && setOpen(false)}>
        {/* links and .nav-cta as above */}
      </nav>
    </>
  );
}
```

- Next.js App Router: add `'use client'`. More than one header on a page: generate the id with `useId()`.

### Tailwind (v4)
- Keep the tokens file loaded and reference tokens directly: `bg-(--primary)`, `shadow-(--shadow-lg)`. For named utilities, map them: `@theme inline { --color-primary: var(--primary); }` → `bg-primary`.
- Keep the JS as-is. Tailwind targets the same attributes:
  - Icons: `group` on the button, `group-aria-expanded:hidden` on the hamburger, `hidden group-aria-expanded:block` on the X.
  - Drawer: `invisible translate-x-full data-open:visible data-open:translate-x-0 md:hidden [transition:translate_var(--transition-smooth),visibility_var(--transition-smooth)]`.
- `md:` is 768px, the library breakpoint.
- Tailwind v4 also defines `--radius-*` and `--shadow-*` theme variables. The tokens file is unlayered, so its values win. Keep it that way.

### Modal variant
For true modal semantics, put the `<nav>` inside a `<dialog>` opened with `showModal()`. That gives a built-in focus trap, Escape handling and an inert page. Add a close button inside the dialog, because the header toggle becomes inert while it's open.
