# Content Blocks

Content-level sections for service pages: feature rows, team, company timeline, comparison table, pricing toggle, contact details with a map, and a pull quote. Depends on `tokens/variables.css`.

| #  | Pattern                                                                                     | JS   |
| -- | ------------------------------------------------------------------------------------------- | ---- |
| 1  | **Alternating feature rows**: zigzag image/text rows with a checklist and a text link        | none |
| 2  | **Team grid**: auto-fit member cards with photo, role, bio and optional social links         | none |
| 3  | **Timeline**: milestones with a left line on mobile, alternating sides from 768px            | none |
| 4  | **Comparison table**: Brand vs typical contractor, scrollable region with sticky first column | none |
| 5  | **Pricing toggle**: monthly/yearly segmented switch that swaps plan prices with `:has()`     | none |
| 6  | **Contact block**: phone, email, address and opening hours beside a lazy map embed           | none |
| 7  | **Pull quote**: large testimonial with star rating, avatar and location                      | none |

## 1. Alternating feature rows

Zigzag image/text rows. Stacked image-first on mobile; from 768px each row splits into two columns and even rows move the image to the right. The flip is visual only, so reading order never changes. Place inside your page container.

### HTML

```html
<div class="feature-rows">
  <div class="feature-rows__row">
    <img class="feature-rows__img" src="estimate.jpg" alt="Estimator going over a printed quote with a homeowner at her kitchen table"
         width="800" height="600" loading="lazy">
    <div class="feature-rows__body">
      <p class="feature-rows__eyebrow">Free estimates</p>
      <h3 class="feature-rows__title">Know the price before we start</h3>
      <p class="feature-rows__text">We measure and price every job on site, then send a written quote the same day.</p>
      <ul class="feature-rows__list" role="list">
        <li class="feature-rows__item">Itemized, fixed-price quote</li>
        <li class="feature-rows__item">No charge for the visit</li>
        <li class="feature-rows__item">Valid for 30 days</li>
      </ul>
      <a class="feature-rows__link" href="https://example.com/estimates">
        How our estimates work
        <svg class="feature-rows__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
    </div>
  </div>
  <div class="feature-rows__row">
    <img class="feature-rows__img" src="crew.jpg" alt="Two technicians fitting a new water heater in a basement"
         width="800" height="600" loading="lazy">
    <div class="feature-rows__body">
      <p class="feature-rows__eyebrow">Our own crew</p>
      <h3 class="feature-rows__title">Every job done by Brand staff</h3>
      <p class="feature-rows__text">No subcontractors. The team that quotes your job is the team that shows up.</p>
      <ul class="feature-rows__list" role="list">
        <li class="feature-rows__item">Background-checked technicians</li>
        <li class="feature-rows__item">Licensed and fully insured</li>
        <li class="feature-rows__item">Clean-up included</li>
      </ul>
      <a class="feature-rows__link" href="https://example.com/team">
        Meet the team
        <svg class="feature-rows__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
    </div>
  </div>
  <!-- repeat .feature-rows__row; even rows flip from 768px -->
</div>
```

### CSS

```css
/* Rows stack image-first; images keep a fixed ratio */
.feature-rows { display: grid; gap: var(--space-2xl); }
.feature-rows__row { display: grid; gap: var(--space-lg); align-items: center; }
.feature-rows__img {
  display: block; width: 100%; height: auto; aspect-ratio: 4 / 3; object-fit: cover;
  border-radius: var(--radius-lg); background: var(--border-subtle);
}

/* Text column */
.feature-rows__eyebrow {
  margin: 0 0 var(--space-xs); color: var(--primary);
  font-size: 0.8125rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
}
.feature-rows__title { margin: 0 0 var(--space-sm); color: var(--text-main); font-size: 1.5rem; line-height: 1.25; }
.feature-rows__text { margin: 0 0 var(--space-md); color: var(--text-muted); line-height: 1.6; }

/* Checklist with a CSS-drawn tick (a rotated L) */
.feature-rows__list { display: grid; gap: var(--space-sm); margin: 0 0 var(--space-lg); padding: 0; list-style: none; }
.feature-rows__item { position: relative; padding-left: var(--space-xl); color: var(--text-main); line-height: 1.5; }
.feature-rows__item::before {
  content: ""; position: absolute; top: 0.25em; left: 0.375rem;
  width: 0.375rem; height: 0.75rem; transform: rotate(45deg);
  border: solid var(--success); border-width: 0 2px 2px 0;
}

/* Text link; the arrow nudges on hover */
.feature-rows__link {
  display: inline-flex; align-items: center; gap: var(--space-xs); min-height: 1.5rem;
  border-radius: var(--radius-sm); color: var(--primary); font-weight: 600;
  text-decoration: underline; text-underline-offset: 0.2em;
}
.feature-rows__link:hover { color: var(--primary-hover); }
.feature-rows__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.feature-rows__icon {
  width: 1.125rem; height: 1.125rem; transition: transform var(--transition-fast);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
@media (hover: hover) {
  .feature-rows__link:hover .feature-rows__icon { transform: translateX(var(--space-xs)); }
}

/* 768px+: two columns; even rows move the image right (visual only) */
@media (min-width: 768px) {
  .feature-rows__row { grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: var(--space-2xl); }
  .feature-rows__row:nth-child(even) .feature-rows__img { order: 1; }
  .feature-rows__title { font-size: 1.75rem; }
}
```

### Notes

- Every row keeps the same source order (image, then text). Only `order` changes on even rows, and the image isn't focusable, so reading and tab order stay the same on every screen.
- The tick is drawn with borders, so the list text alone carries the meaning. `role="list"` restores list semantics that Safari drops with `list-style: none`.
- Use specific link text ("How our estimates work"). Several "Learn more" links are ambiguous in a screen reader's links list.
- Give purely decorative photos `alt=""`.

## 2. Team grid

Member cards with a photo, name, role, short bio and optional social links. The auto-fit grid goes from 1 column to as many as fit. Icon links are labelled with the person's name. Place inside your page container.

### HTML

```html
<ul class="team-grid" role="list">
  <li class="team-grid__card">
    <img class="team-grid__photo" src="team-maria.jpg" alt="" width="480" height="480" loading="lazy">
    <div class="team-grid__body">
      <h3 class="team-grid__name">Maria Lopez</h3>
      <p class="team-grid__role">Founder &amp; lead estimator</p>
      <p class="team-grid__bio">Twenty years in residential remodeling. Still prices every kitchen job herself.</p>
      <!-- Optional. Generic icons: swap in each network's own mark -->
      <ul class="team-grid__social" role="list">
        <li>
          <a class="team-grid__social-link" href="https://www.linkedin.com/in/example" aria-label="Maria Lopez on LinkedIn">
            <svg class="team-grid__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
          </a>
        </li>
        <li>
          <a class="team-grid__social-link" href="mailto:maria@example.com" aria-label="Email Maria Lopez">
            <svg class="team-grid__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>
          </a>
        </li>
      </ul>
    </div>
  </li>
  <li class="team-grid__card">
    <img class="team-grid__photo" src="team-jordan.jpg" alt="" width="480" height="480" loading="lazy">
    <div class="team-grid__body">
      <h3 class="team-grid__name">Jordan Lee</h3>
      <p class="team-grid__role">Lead technician</p>
      <p class="team-grid__bio">Licensed plumber and our go-to for water heaters and emergency call-outs.</p>
    </div>
  </li>
  <!-- repeat per member -->
</ul>
```

### CSS

```css
/* Auto-fit grid: cards stretch to fill the row */
.team-grid {
  display: grid; gap: var(--space-lg);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
  margin: 0; padding: 0; list-style: none;
}

/* Card: square photo on top, body fills the remaining height */
.team-grid__card {
  display: flex; flex-direction: column; overflow: hidden;
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  background: var(--surface-light); box-shadow: var(--shadow-sm);
}
.team-grid__photo { display: block; width: 100%; height: auto; aspect-ratio: 1; object-fit: cover; background: var(--border-subtle); }
.team-grid__body { display: flex; flex: 1; flex-direction: column; gap: var(--space-xs); padding: var(--space-lg); }
.team-grid__name { margin: 0; color: var(--text-main); font-size: 1.125rem; }
.team-grid__role { margin: 0; color: var(--primary); font-size: 0.875rem; font-weight: 600; }
.team-grid__bio { margin: var(--space-xs) 0 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.6; }

/* Social links pinned to the card bottom; 44px icon targets */
.team-grid__social { display: flex; gap: var(--space-sm); margin: auto 0 0; padding: var(--space-md) 0 0; list-style: none; }
.team-grid__social-link {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem;
  border: 1px solid var(--border-subtle); border-radius: var(--radius-full); color: var(--text-muted);
  transition: color var(--transition-fast), border-color var(--transition-fast);
}
.team-grid__social-link:hover { color: var(--primary); border-color: var(--primary); }
.team-grid__social-link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.team-grid__icon {
  width: 1.25rem; height: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
```

### Notes

- Headshots use `alt=""` because the name sits right below. Repeating "Photo of Maria Lopez" adds noise.
- Icon-only links get an `aria-label` that names the person and the network. "LinkedIn" alone, repeated on every card, is ambiguous.
- `auto-fit` stretches cards when there are only 2–3 members. Switch to `auto-fill` to keep cards the same width.

## 3. Timeline

Company milestones as an ordered list. On mobile it's one column with the line on the left; from 768px milestones alternate sides of a center line. Pure CSS, with the line and dots drawn as pseudo-elements. Place inside your page container.

### HTML

```html
<ol class="timeline" role="list">
  <li class="timeline__item">
    <time class="timeline__year" datetime="2009">2009</time>
    <h3 class="timeline__title">Founded in Springfield</h3>
    <p class="timeline__text">Two people, one van and a promise to return every call the same day.</p>
  </li>
  <li class="timeline__item">
    <time class="timeline__year" datetime="2014">2014</time>
    <h3 class="timeline__title">1,000 homes served</h3>
    <p class="timeline__text">Added a second crew and our first full-time plumber.</p>
  </li>
  <li class="timeline__item">
    <time class="timeline__year" datetime="2019">2019</time>
    <h3 class="timeline__title">Opened our showroom</h3>
    <p class="timeline__text">Customers can now see finishes and fixtures before they choose.</p>
  </li>
  <li class="timeline__item">
    <time class="timeline__year" datetime="2024">2024</time>
    <h3 class="timeline__title">Serving three counties</h3>
    <p class="timeline__text">Thirty staff, twelve vans and the same call-back promise.</p>
  </li>
</ol>
```

### CSS

```css
/* Mobile: line on the left, one dot per milestone */
.timeline {
  --timeline-dot: 1rem;
  --timeline-indent: calc(var(--timeline-dot) + var(--space-lg));
  position: relative; display: flex; flex-direction: column; gap: var(--space-xl);
  margin: 0; padding: 0 0 0 var(--timeline-indent); list-style: none;
}
.timeline::before {
  content: ""; position: absolute; top: 0; bottom: 0; left: calc(var(--timeline-dot) / 2 - 1px);
  width: 2px; background: var(--border-subtle);
}
.timeline__item { position: relative; }
.timeline__item::before {
  content: ""; position: absolute; top: 0.125rem; left: calc(-1 * var(--timeline-indent));
  box-sizing: border-box; width: var(--timeline-dot); height: var(--timeline-dot);
  border: 3px solid var(--primary); border-radius: var(--radius-full); background: var(--surface-light);
}

/* Milestone text */
.timeline__year { display: block; color: var(--primary); font-size: 0.875rem; font-weight: 700; line-height: 1.25rem; }
.timeline__title { margin: var(--space-xs) 0; color: var(--text-main); font-size: 1.125rem; }
.timeline__text { margin: 0; color: var(--text-muted); line-height: 1.6; }

/* 768px+: center line, milestones alternate left and right */
@media (min-width: 768px) {
  .timeline { --timeline-indent: calc(var(--timeline-dot) / 2 + var(--space-xl)); padding-left: 0; }
  .timeline::before { left: calc(50% - 1px); }
  .timeline__item { box-sizing: border-box; width: 50%; padding-right: var(--timeline-indent); text-align: right; }
  .timeline__item::before { left: auto; right: calc(var(--timeline-dot) / -2); }
  .timeline__item:nth-child(even) { margin-left: 50%; padding: 0 0 0 var(--timeline-indent); text-align: left; }
  .timeline__item:nth-child(even)::before { right: auto; left: calc(var(--timeline-dot) / -2); }
}
```

### Notes

- `<ol>` tells screen readers the order and count ("list, 4 items"). The line and dots are pseudo-elements, so there's nothing extra to hide.
- `<time datetime>` makes years machine-readable. Use a fuller value (`2019-06`) when you know the month.
- Sides alternate visually only. The reading order stays top to bottom.

## 4. Comparison table

"Brand vs typical contractor" as a real `<table>` with a caption and header scopes, with the Brand column highlighted. On narrow screens the table scrolls inside a focusable, labelled region with a sticky first column. Place inside your page container.

### HTML

```html
<div class="compare-table" role="region" aria-labelledby="compare-table-caption" tabindex="0">
  <table class="compare-table__table">
    <caption class="compare-table__caption" id="compare-table-caption">Brand vs a typical contractor</caption>
    <thead>
      <tr>
        <th scope="col">What you get</th>
        <th class="compare-table__brand" scope="col">Brand</th>
        <th scope="col">Typical contractor</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Fixed-price written quote</th>
        <td class="compare-table__brand"><svg class="compare-table__icon compare-table__icon--yes" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 12l5 5L20 7"/></svg><span class="compare-table__sr">Included</span></td>
        <td><svg class="compare-table__icon compare-table__icon--no" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg><span class="compare-table__sr">Not included</span></td>
      </tr>
      <tr>
        <th scope="row">Arrival window</th>
        <td class="compare-table__brand">2 hours</td>
        <td>All day</td>
      </tr>
      <tr>
        <th scope="row">Workmanship warranty</th>
        <td class="compare-table__brand">10 years</td>
        <td>1 year</td>
      </tr>
      <tr>
        <th scope="row">Background-checked technicians</th>
        <td class="compare-table__brand"><svg class="compare-table__icon compare-table__icon--yes" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 12l5 5L20 7"/></svg><span class="compare-table__sr">Included</span></td>
        <td><svg class="compare-table__icon compare-table__icon--no" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg><span class="compare-table__sr">Not included</span></td>
      </tr>
      <tr>
        <th scope="row">Clean-up included</th>
        <td class="compare-table__brand"><svg class="compare-table__icon compare-table__icon--yes" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 12l5 5L20 7"/></svg><span class="compare-table__sr">Included</span></td>
        <td><svg class="compare-table__icon compare-table__icon--no" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg><span class="compare-table__sr">Not included</span></td>
      </tr>
    </tbody>
  </table>
</div>
```

### CSS

```css
/* Focusable scroll region: the table scrolls inside it on narrow screens */
.compare-table {
  position: relative; /* contains the absolutely positioned hidden text */
  max-width: 100%; overflow-x: auto; overscroll-behavior-x: contain;
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); background: var(--surface-light);
}
.compare-table:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.compare-table__table {
  width: 100%; min-width: 28rem; border-collapse: separate; border-spacing: 0;
  color: var(--text-main); font-size: 0.9375rem;
}
.compare-table__caption { padding: var(--space-md); text-align: left; font-size: 1.125rem; font-weight: 700; }

/* Cells */
.compare-table th,
.compare-table td { padding: var(--space-sm) var(--space-md); border-top: 1px solid var(--border-subtle); text-align: center; }
.compare-table thead th { font-size: 0.875rem; }

/* Sticky first column: narrow on mobile; opaque so cells scrolling underneath stay hidden */
.compare-table tr > :first-child {
  position: sticky; left: 0; z-index: 1; width: 9rem;
  background: var(--surface-light); box-shadow: inset -1px 0 0 var(--border-subtle);
  font-weight: 600; text-align: left;
}

/* Highlighted Brand column (solid fallback before color-mix) */
.compare-table__brand {
  background: var(--surface-muted);
  background: color-mix(in srgb, var(--primary) 8%, var(--surface-light));
  font-weight: 600;
}
.compare-table thead .compare-table__brand { background: var(--primary); color: var(--text-inverse); }

/* Check/cross icons; the hidden text carries the meaning */
.compare-table__icon {
  width: 1.5rem; height: 1.5rem; vertical-align: middle;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.compare-table__icon--yes { color: var(--success); }
.compare-table__icon--no { color: var(--text-muted); }
.compare-table__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

/* 768px+: the table fits, so the first column can widen */
@media (min-width: 768px) {
  .compare-table tr > :first-child { width: 40%; }
}
```

### Notes

- The wrapper is a named, focusable `role="region"`, so keyboard users can scroll it with the arrow keys. `aria-labelledby` reuses the caption, so give each instance its own caption `id`.
- Icons are `aria-hidden`. Screen readers announce the hidden "Included" / "Not included" text along with the row and column headers from `scope`.
- Sticky cells need an opaque background and `border-collapse: separate`, because collapsed borders scroll away from sticky cells.
- `color-mix()` needs Chrome 111, Safari 16.2 or Firefox 113. Older browsers get the `--surface-muted` fallback.
- Keep it a real table on mobile. Rebuilding it from divs loses the header associations.

## 5. Pricing toggle

A monthly/yearly radio group styled as a segmented switch. It swaps the prices in small plan cards with CSS `:has()` and no JS. Both prices are in the DOM, and the inactive one is `display: none`. Place inside your page container.

### HTML

```html
<div class="pricing-toggle">
  <fieldset class="pricing-toggle__switch">
    <legend class="pricing-toggle__sr">Billing period</legend>
    <input class="pricing-toggle__input pricing-toggle__sr" type="radio" name="billing" id="billing-monthly" value="monthly" checked>
    <label class="pricing-toggle__option" for="billing-monthly">Monthly</label>
    <input class="pricing-toggle__input pricing-toggle__sr" type="radio" name="billing" id="billing-yearly" value="yearly">
    <label class="pricing-toggle__option" for="billing-yearly">Yearly <span class="pricing-toggle__save">Save 20%</span></label>
  </fieldset>
  <ul class="pricing-toggle__plans" role="list">
    <li class="pricing-toggle__plan">
      <h3 class="pricing-toggle__name">Seasonal tune-up</h3>
      <p class="pricing-toggle__price">
        <span class="pricing-toggle__amount pricing-toggle__amount--monthly"><strong class="pricing-toggle__figure">$19</strong> per month</span>
        <span class="pricing-toggle__amount pricing-toggle__amount--yearly"><strong class="pricing-toggle__figure">$182</strong> per year</span>
      </p>
      <p class="pricing-toggle__desc">Two heating and cooling checks a year.</p>
      <a class="pricing-toggle__cta" href="#quote">Choose Seasonal tune-up</a>
    </li>
    <li class="pricing-toggle__plan">
      <h3 class="pricing-toggle__name">Home care</h3>
      <p class="pricing-toggle__price">
        <span class="pricing-toggle__amount pricing-toggle__amount--monthly"><strong class="pricing-toggle__figure">$39</strong> per month</span>
        <span class="pricing-toggle__amount pricing-toggle__amount--yearly"><strong class="pricing-toggle__figure">$374</strong> per year</span>
      </p>
      <p class="pricing-toggle__desc">Quarterly checks, priority booking and 10% off repairs.</p>
      <a class="pricing-toggle__cta" href="#quote">Choose Home care</a>
    </li>
    <li class="pricing-toggle__plan">
      <h3 class="pricing-toggle__name">Total care</h3>
      <p class="pricing-toggle__price">
        <span class="pricing-toggle__amount pricing-toggle__amount--monthly"><strong class="pricing-toggle__figure">$69</strong> per month</span>
        <span class="pricing-toggle__amount pricing-toggle__amount--yearly"><strong class="pricing-toggle__figure">$662</strong> per year</span>
      </p>
      <p class="pricing-toggle__desc">Everything in Home care, plus plumbing and electrical checks.</p>
      <a class="pricing-toggle__cta" href="#quote">Choose Total care</a>
    </li>
  </ul>
</div>
```

### CSS

```css
/* Switch centered above the plan cards */
.pricing-toggle { display: grid; justify-items: center; gap: var(--space-xl); }
.pricing-toggle__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

/* Segmented switch: visually hidden radios drive the styled labels */
.pricing-toggle__switch {
  position: relative; display: none; gap: var(--space-xs); min-width: 0; max-width: 100%;
  margin: 0; padding: var(--space-xs);
  border: 1px solid var(--text-muted); border-radius: var(--radius-full); background: var(--surface-muted);
}
.pricing-toggle__option {
  display: inline-flex; align-items: center; gap: var(--space-sm); min-height: 2.75rem; padding-inline: var(--space-md);
  border-radius: var(--radius-full); color: var(--text-main); font-weight: 600; cursor: pointer;
  transition: background-color var(--transition-fast), color var(--transition-fast);
}
.pricing-toggle__input:not(:checked) + .pricing-toggle__option:hover { background: var(--border-subtle); }
.pricing-toggle__input:checked + .pricing-toggle__option { background: var(--primary); color: var(--text-inverse); }
.pricing-toggle__input:focus-visible + .pricing-toggle__option { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.pricing-toggle__save {
  padding-inline: var(--space-sm); border-radius: var(--radius-sm);
  background: var(--accent); color: var(--text-main); font-size: 0.75rem; font-weight: 700; line-height: 1.5rem;
}

/* Plan cards */
.pricing-toggle__plans {
  display: grid; gap: var(--space-lg); width: 100%;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
  margin: 0; padding: 0; list-style: none;
}
.pricing-toggle__plan {
  display: flex; flex-direction: column; gap: var(--space-sm); padding: var(--space-lg);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); background: var(--surface-light);
}
.pricing-toggle__name { margin: 0; color: var(--text-main); font-size: 1.125rem; }
.pricing-toggle__price { margin: 0; color: var(--text-muted); }
.pricing-toggle__figure { color: var(--text-main); font-size: 2rem; font-weight: 800; line-height: 1.2; }
.pricing-toggle__desc { margin: 0 0 var(--space-sm); color: var(--text-muted); font-size: 0.9375rem; }
.pricing-toggle__cta {
  display: inline-flex; align-items: center; justify-content: center; min-height: 2.75rem; margin-top: auto;
  padding-inline: var(--space-lg); border-radius: var(--radius-md);
  background: var(--primary); color: var(--text-inverse); font-weight: 600; text-decoration: none;
  transition: background-color var(--transition-fast);
}
.pricing-toggle__cta:hover { background: var(--primary-hover); }
.pricing-toggle__cta:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Fallback (no :has()): the switch stays hidden and both prices show */
.pricing-toggle__amount { display: block; }

/* With :has(): show the switch and only the selected period's price */
@supports selector(:has(*)) {
  .pricing-toggle__switch { display: inline-flex; }
  .pricing-toggle__amount--yearly,
  .pricing-toggle:has(.pricing-toggle__input[value="yearly"]:checked) .pricing-toggle__amount--monthly { display: none; }
  .pricing-toggle:has(.pricing-toggle__input[value="yearly"]:checked) .pricing-toggle__amount--yearly { display: block; }
}
```

### Notes

- Native radios in a `fieldset` with a `legend` provide the group name, arrow-key selection and "1 of 2" announcements. The radios are visually hidden rather than `display: none`, so they stay focusable. Keep each radio directly before its label, because the `+` selectors depend on it.
- The inactive price is `display: none`, so screen readers read only the selected period. Switching isn't announced; users hear the new prices when they reach the cards.
- `:has()` needs Chrome/Edge 105, Safari 15.4 or Firefox 121. Older browsers skip the `@supports` block, so the switch stays hidden and each card lists both prices.
- Give each instance its own radio `name` and `id`s.
- **React:** keep the radios uncontrolled (`defaultChecked`). CSS does the swap, so no state is needed.

## 6. Contact block

Contact details (phone, email, address and opening hours) beside a lazy-loaded map. Stacked on mobile, side by side from 768px. Place inside your page container.

### HTML

```html
<div class="contact-block">
  <div class="contact-block__details">
    <h3 class="contact-block__title">Brand Home Services</h3>
    <address class="contact-block__address">
      <dl class="contact-block__list">
        <div>
          <dt class="contact-block__term"><svg class="contact-block__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/></svg>Phone</dt>
          <dd class="contact-block__value"><a class="contact-block__link" href="tel:+15555550123">(555) 555-0123</a></dd>
        </div>
        <div>
          <dt class="contact-block__term"><svg class="contact-block__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>Email</dt>
          <dd class="contact-block__value"><a class="contact-block__link" href="mailto:hello@example.com">hello@example.com</a></dd>
        </div>
        <div>
          <dt class="contact-block__term"><svg class="contact-block__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 21s-7-6.5-7-12a7 7 0 0 1 14 0c0 5.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>Address</dt>
          <dd class="contact-block__value">123 Main Street<br>Springfield, ST 12345</dd>
        </div>
      </dl>
    </address>
    <table class="contact-block__hours">
      <caption class="contact-block__caption">Opening hours</caption>
      <tbody>
        <tr><th scope="row">Monday–Friday</th><td>7:00 am – 6:00 pm</td></tr>
        <tr><th scope="row">Saturday</th><td>8:00 am – 2:00 pm</td></tr>
        <tr><th scope="row">Sunday</th><td>Emergency calls only</td></tr>
      </tbody>
    </table>
  </div>
  <div class="contact-block__map">
    <!-- Replace src with your map provider's embed URL -->
    <iframe class="contact-block__frame" src="https://www.example.com/maps/embed?q=123+Main+Street+Springfield"
            title="Map showing Brand at 123 Main Street, Springfield" width="600" height="450" loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"></iframe>
    <a class="contact-block__link" href="https://www.example.com/maps?q=123+Main+Street+Springfield">Get directions</a>
  </div>
</div>
```

### CSS

```css
/* Stacked on mobile; details beside the map from 768px */
.contact-block { display: grid; gap: var(--space-xl); }
.contact-block__details { display: grid; gap: var(--space-lg); align-content: start; }
.contact-block__title { margin: 0; color: var(--text-main); font-size: 1.25rem; }
.contact-block__address { font-style: normal; }

/* Details list: small icon label above each value */
.contact-block__list { display: grid; gap: var(--space-md); margin: 0; }
.contact-block__term {
  display: flex; align-items: center; gap: var(--space-xs);
  color: var(--text-muted); font-size: 0.875rem; font-weight: 600;
}
.contact-block__value { margin: 0; color: var(--text-main); line-height: 1.5; overflow-wrap: anywhere; }
.contact-block__icon {
  width: 1.125rem; height: 1.125rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.contact-block__link {
  display: inline-block; min-height: 1.5rem; border-radius: var(--radius-sm);
  color: var(--primary); font-weight: 600; text-underline-offset: 0.2em;
}
.contact-block__link:hover { color: var(--primary-hover); }
.contact-block__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Opening hours: day on the left, time on the right */
.contact-block__hours { width: 100%; border-collapse: collapse; color: var(--text-main); font-size: 0.9375rem; }
.contact-block__caption { margin-bottom: var(--space-xs); text-align: left; font-weight: 700; }
.contact-block__hours th,
.contact-block__hours td { padding: var(--space-sm) 0; border-top: 1px solid var(--border-subtle); font-weight: 400; text-align: left; }
.contact-block__hours td { padding-left: var(--space-md); text-align: right; }

/* Map keeps its ratio; the directions link sits underneath */
.contact-block__map { display: grid; gap: var(--space-sm); justify-items: start; }
.contact-block__frame {
  display: block; width: 100%; height: auto; aspect-ratio: 4 / 3;
  border: 0; border-radius: var(--radius-lg); background: var(--border-subtle);
}

@media (min-width: 768px) {
  .contact-block { grid-template-columns: minmax(0, 2fr) minmax(0, 3fr); gap: var(--space-2xl); align-items: start; }
}
```

### Notes

- `tel:` and `mailto:` make phone and email one tap on mobile. Format the visible number for reading and keep the `href` in E.164 (`+15555550123`).
- `<address>` marks the business contact details. It can't contain headings, so the business name sits above it, and its default italics are reset.
- The `<iframe>` needs a `title` that describes the map, and `loading="lazy"` keeps the provider's scripts off the critical path. "Get directions" is the text alternative for anyone who can't use the embed.
- `height: auto` plus `aspect-ratio` overrides the `height` attribute, so the map scales with its column.

## 7. Pull quote

A large testimonial on a dark card, with a decorative quote mark, a star rating with hidden text, the quote, and an author with avatar and location. Place inside your page container.

### HTML

```html
<figure class="pull-quote">
  <svg class="pull-quote__mark" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M10 17H3v-6c0-4 2-6 5-6v2.5c-1.5 0-2.5 1.2-2.5 3.5H10zm11 0h-7v-6c0-4 2-6 5-6v2.5c-1.5 0-2.5 1.2-2.5 3.5H21z"/></svg>
  <p class="pull-quote__rating">
    <span class="pull-quote__stars" style="--pull-quote-stars: 5" aria-hidden="true"></span>
    <span class="pull-quote__sr">Rated 5 out of 5</span>
  </p>
  <blockquote class="pull-quote__quote">
    <p class="pull-quote__text">They quoted a price, showed up when they said, and left the kitchen cleaner than they found it. We've already booked them for the bathroom.</p>
  </blockquote>
  <figcaption class="pull-quote__caption">
    <img class="pull-quote__avatar" src="avatar-dana.jpg" alt="" width="56" height="56" loading="lazy">
    <span>
      <span class="pull-quote__author">Dana R.</span>
      <span class="pull-quote__location">Kitchen remodel · Springfield</span>
    </span>
  </figcaption>
</figure>
```

### CSS

```css
/* Dark highlight card; type steps up from 768px */
.pull-quote {
  margin: 0; padding: var(--space-xl) var(--space-lg);
  border-radius: var(--radius-lg); background: var(--surface-dark); color: var(--text-inverse);
}
.pull-quote__mark {
  display: block; width: 3.5rem; height: 3.5rem; margin-bottom: var(--space-md); color: var(--accent);
  fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linejoin: round;
}

/* Stars: a masked bar whose width is rating × star size, so 4.5 shows half a star */
.pull-quote__rating { display: flex; margin: 0 0 var(--space-md); }
.pull-quote__stars {
  --pull-quote-star: 1.25rem;
  --pull-quote-star-svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2l3 6.5 7 .8-5.2 4.8 1.4 7L12 17.6 5.8 21.1l1.4-7L2 9.3l7-.8z'/%3E%3C/svg%3E");
  display: block; width: calc(var(--pull-quote-stars, 5) * var(--pull-quote-star)); height: var(--pull-quote-star);
  background: var(--accent);
  -webkit-mask: var(--pull-quote-star-svg) 0 0 / var(--pull-quote-star) repeat-x;
  mask: var(--pull-quote-star-svg) 0 0 / var(--pull-quote-star) repeat-x;
}

/* Quote and attribution */
.pull-quote__quote { max-width: 48rem; margin: 0; }
.pull-quote__text { margin: 0; font-size: 1.25rem; font-weight: 500; line-height: 1.5; }
.pull-quote__caption { display: flex; align-items: center; gap: var(--space-md); margin-top: var(--space-lg); }
.pull-quote__avatar {
  flex-shrink: 0; width: 3.5rem; height: 3.5rem; object-fit: cover;
  border-radius: var(--radius-full); background: var(--text-inverse-muted);
}
.pull-quote__author { display: block; font-weight: 700; }
.pull-quote__location { display: block; color: var(--text-inverse-muted); font-size: 0.875rem; }
.pull-quote__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

@media (min-width: 768px) {
  .pull-quote { padding: var(--space-2xl); }
  .pull-quote__text { font-size: 1.5rem; }
}
```

### Notes

- Only the customer's words go in `<blockquote>`. The rating sits beside it and the attribution goes in `<figcaption>`, which ties it to the quote.
- The quote mark and stars are `aria-hidden`, and "Rated 5 out of 5" is visually hidden text. Change `--pull-quote-stars` and that text together (4.5 → "Rated 4.5 out of 5"). The avatar is `alt=""` because the name sits beside it.
- `--accent` stars pass contrast on `--surface-dark` but not on white (about 2:1). For a light card, color the stars `--warning` and set text to `--text-main`/`--text-muted`.
- Use real customer quotes, with permission.
- **React:** `style={{ '--pull-quote-stars': 4.5 }}`.
