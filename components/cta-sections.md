# CTA Sections

Conversion blocks that push visitors to call or request a quote. Depends on `tokens/variables.css`.

- **A. CTA band:** full-width dark (or `--primary`) band with headline, supporting line and two actions. Stacked below 768px; copy left and buttons right above that.
- **B. Mobile action bar:** fixed bottom bar with "Call now" and "Free quote", on phones only. It pads the page so it never covers content.

## HTML

### A. CTA band

```html
<section class="cta-band" aria-labelledby="cta-band-title">
  <div class="cta-band__inner">
    <div>
      <h2 id="cta-band-title" class="cta-band__title">Ready to get it fixed?</h2>
      <p class="cta-band__text">Free, no-obligation quotes. Most jobs booked within 24 hours.</p>
    </div>
    <div class="cta-band__actions">
      <a class="cta-btn cta-btn--solid" href="#quote">Get a free quote</a>
      <a class="cta-btn cta-btn--outline" href="tel:+15555550123">Call (555) 555-0123</a>
    </div>
  </div>
</section>
```

Add `cta-band--primary` to the section for a brand-colored band.

### B. Mobile action bar

Place at the end of `<body>`, after the footer.

```html
<div class="action-bar">
  <a class="action-bar__btn" href="tel:+15555550123">
    <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
      <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
    </svg>
    Call now
  </a>
  <a class="action-bar__btn action-bar__btn--primary" href="#quote">Free quote</a>
</div>
```

## CSS

```css
:root { --action-bar-h: 4rem; } /* module-local: shared by the bar and the page padding */

/* A. CTA band: full-bleed background, contained content */
.cta-band { padding-block: var(--space-2xl); background: var(--surface-dark); color: var(--text-inverse); }
.cta-band--primary { background: var(--primary); }
.cta-band__inner {
  display: grid; gap: var(--space-lg);
  max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter);
}
.cta-band__title { margin: 0; font-size: clamp(1.5rem, 1rem + 2vw, 2.25rem); line-height: 1.2; text-wrap: balance; }
.cta-band__text { margin: var(--space-sm) 0 0; color: var(--text-inverse-muted); }
.cta-band--primary .cta-band__text { color: var(--text-inverse); } /* muted gray fails contrast on blue */
.cta-band__actions { display: flex; flex-wrap: wrap; gap: var(--space-sm); }

/* Band buttons: full width on mobile, natural width from 768px */
.cta-btn {
  display: inline-flex; flex: 1 1 auto; align-items: center; justify-content: center;
  min-height: 2.75rem; padding: var(--space-sm) var(--space-lg);
  border: 1px solid transparent; border-radius: var(--radius-md);
  font-weight: 600; text-decoration: none;
  transition: background-color var(--transition-fast), border-color var(--transition-fast);
}
.cta-btn:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }
.cta-btn--solid { background: var(--surface-light); color: var(--text-main); }
.cta-btn--solid:hover { background: var(--border-subtle); }
.cta-btn--outline { border-color: color-mix(in srgb, var(--text-inverse) 50%, transparent); color: var(--text-inverse); }
.cta-btn--outline:hover {
  border-color: var(--text-inverse);
  background: color-mix(in srgb, var(--text-inverse) 10%, transparent);
}

/* B. Mobile action bar: z-index 5 keeps it under the nav drawer and backdrop (10–30) */
.action-bar {
  position: fixed; inset: auto 0 0; z-index: 5;
  box-sizing: border-box; min-height: var(--action-bar-h);
  display: grid; grid-template-columns: 1fr 1fr; align-items: center; gap: var(--space-sm);
  padding: var(--space-sm) var(--gutter) calc(var(--space-sm) + env(safe-area-inset-bottom));
  background: var(--surface-light); border-top: 1px solid var(--border-subtle);
}
.action-bar__btn {
  display: flex; align-items: center; justify-content: center; gap: var(--space-xs);
  min-height: 2.75rem; padding-inline: var(--space-sm);
  border: 1px solid var(--primary); border-radius: var(--radius-md);
  color: var(--primary); font-weight: 600; text-decoration: none;
}
.action-bar__btn--primary { background: var(--primary); color: var(--text-inverse); }
.action-bar__btn:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.action-bar__btn svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* Reserve space so the bar never hides the end of the page */
@media (max-width: 767.98px) {
  body:has(.action-bar) { padding-bottom: calc(var(--action-bar-h) + env(safe-area-inset-bottom)); }
}

@media (min-width: 768px) {
  .cta-band__inner { grid-template-columns: 1fr auto; align-items: center; gap: var(--space-2xl); }
  .cta-btn { flex: none; }
  .action-bar { display: none; }
}
```

## Notes

- `tel:` links use E.164 (`+15555550123`). Keep the number identical in the hero, band, action bar and footer.
- `env(safe-area-inset-bottom)` keeps the bar clear of the iPhone home indicator. It needs `viewport-fit=cover` in the viewport meta tag; without it the value is 0 and nothing breaks.
- The bar is visible from page load so it works without JS. To reveal it only after the hero scrolls away, toggle a class from an `IntersectionObserver` on the hero.
- The band's outline button has a 50% white border; its text, not the border, identifies it as a control.
- **React:** static markup; `class` → `className`.
- **Tailwind (v4):** bar `fixed inset-x-0 bottom-0 grid grid-cols-2 gap-2 md:hidden pb-[calc(var(--space-sm)+env(safe-area-inset-bottom))]`. Band `grid gap-6 md:grid-cols-[1fr_auto] md:items-center`.
