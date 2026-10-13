# Trust & Stats

Social-proof strips that usually sit right below the hero. Depends on `tokens/variables.css`. Place inside your page container.

- **A. Stats row:** 3–4 headline numbers. 2 columns on phones, one row from 768px.
- **B. Badge strip:** certification, association or partner logos in a centered, wrapping row.

## HTML

### A. Stats row

`<dl>` pairs each number with its label. The number shows above the label but is read after it ("Years in business, 15+").

```html
<dl class="stats">
  <div class="stats__item"><dt>Years in business</dt><dd>15+</dd></div>
  <div class="stats__item"><dt>Jobs completed</dt><dd>12,000</dd></div>
  <div class="stats__item"><dt>Average rating</dt><dd>4.9/5</dd></div>
  <div class="stats__item"><dt>Emergency service</dt><dd>24/7</dd></div>
</dl>
```

### B. Badge strip

```html
<div class="badges">
  <p class="badges__label">Licensed, certified and insured</p>
  <ul class="badges__list" role="list">
    <li><img src="badge-accredited.svg" alt="Accredited business, A+ rating" width="120" height="48" loading="lazy"></li>
    <li><img src="badge-license.svg" alt="State-licensed contractor" width="120" height="48" loading="lazy"></li>
    <li><img src="badge-lead-safe.svg" alt="Lead-safe certified firm" width="120" height="48" loading="lazy"></li>
    <li><img src="badge-installer.svg" alt="Manufacturer-certified installer" width="120" height="48" loading="lazy"></li>
  </ul>
</div>
```

## CSS

```css
/* A. Stats row: column-reverse puts the number on top; source order stays label → value */
.stats {
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: var(--space-lg) var(--space-md); margin: 0;
}
.stats__item { display: flex; flex-direction: column-reverse; gap: var(--space-xs); text-align: center; }
.stats__item dt { font-size: 0.9375rem; color: var(--text-muted); }
.stats__item dd {
  margin: 0; font-size: clamp(2rem, 1.5rem + 2vw, 2.75rem); font-weight: 700;
  line-height: 1.1; letter-spacing: -0.02em; font-variant-numeric: tabular-nums;
  color: var(--primary);
}

/* B. Badge strip: muted logos that regain color on hover */
.badges { text-align: center; }
.badges__label {
  margin: 0 0 var(--space-md); font-size: 0.875rem; font-weight: 600;
  letter-spacing: 0.05em; text-transform: uppercase; color: var(--text-muted);
}
.badges__list {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: center;
  gap: var(--space-lg) var(--space-xl); margin: 0; padding: 0; list-style: none;
}
.badges__list img {
  display: block; width: auto; height: 3rem; max-width: 9rem; object-fit: contain;
  filter: grayscale(1); opacity: 0.75;
  transition: filter var(--transition-fast), opacity var(--transition-fast);
}
.badges__list img:hover { filter: none; opacity: 1; }

/* Desktop: one equal-width row with dividers, whatever the item count */
@media (min-width: 768px) {
  .stats { grid-template-columns: none; grid-auto-flow: column; grid-auto-columns: minmax(0, 1fr); column-gap: 0; }
  .stats__item { padding-inline: var(--space-md); }
  .stats__item + .stats__item { border-left: 1px solid var(--border-subtle); }
}
```

## Notes

- Publish only accurate, current numbers, and use the same rating that appears on your review cards.
- Skip animated count-up numbers. They add JS, and the first value people see (0) is wrong.
- Badge `alt` text names what the badge certifies, not "logo". If the issuer offers a verification page, wrap the image in a link to it and keep the alt.
- **React:** static markup; `class` → `className`.
- **Tailwind (v4):** stats `grid grid-cols-2 gap-6 md:grid-cols-none md:grid-flow-col md:auto-cols-fr`. Items `flex flex-col-reverse text-center`.
