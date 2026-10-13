# Cards & Grids

Feature, review and pricing cards on one responsive grid. Depends on `tokens/variables.css`. Place inside your page container.

- **Grid:** `auto-fit` columns with an 18rem minimum: 1 column on phones, 2 on tablets, 3 at `--container-max`. No media queries.
- **Feature card:** icon, title, text and an arrow link. Lifts on hover, and the whole card is clickable.
- **Review card:** star rating, quote, author with avatar or initials.
- **Pricing card:** tier, price, checklist and CTA, plus a highlighted "Most popular" variant.

## HTML

### Feature cards

```html
<ul class="card-grid" role="list">
  <li class="feature-card">
    <span class="feature-card__icon" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="24" height="24"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z" /></svg>
    </span>
    <h3 class="feature-card__title"><a href="/services/repairs">Emergency repairs</a></h3>
    <p class="feature-card__text">Fast response for leaks, outages and breakdowns, day or night.</p>
    <span class="feature-card__more" aria-hidden="true">Learn more <span class="feature-card__arrow">→</span></span>
  </li>
  <!-- repeat per service -->
</ul>
```

### Review card

```html
<ul class="card-grid" role="list">
  <li>
    <figure class="review-card">
      <div class="review-card__stars" style="--rating: 5" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
      <blockquote class="review-card__quote">
        <p>They showed up on time, explained every option and left the place spotless.</p>
      </blockquote>
      <figcaption class="review-card__author">
        <img class="review-card__avatar" src="avatar.jpg" alt="" width="48" height="48" loading="lazy">
        <!-- No photo: <span class="review-card__avatar" aria-hidden="true">ML</span> -->
        <span>
          <span class="review-card__name">Maria Lopez</span>
          <span class="review-card__meta">Verified customer · Austin, TX</span>
        </span>
      </figcaption>
    </figure>
  </li>
</ul>
```

### Pricing cards

```html
<ul class="card-grid card-grid--pricing" role="list">
  <li class="price-card">
    <h3 class="price-card__name">Basic</h3>
    <p class="price-card__price">From <span class="price-card__amount">$89</span> / visit</p>
    <p class="price-card__desc">Diagnose and fix a single issue.</p>
    <ul class="price-card__features" role="list">
      <li>On-site diagnosis</li>
      <li>Standard repair labor</li>
      <li>90-day warranty</li>
    </ul>
    <a class="price-card__cta" href="#quote">Choose Basic</a>
  </li>
  <li class="price-card price-card--featured">
    <h3 class="price-card__name">Standard</h3>
    <p class="price-card__flag">Most popular</p>
    <p class="price-card__price">From <span class="price-card__amount">$149</span> / visit</p>
    <p class="price-card__desc">Repair plus a full system check.</p>
    <ul class="price-card__features" role="list">
      <li>Everything in Basic</li>
      <li>Full system inspection</li>
      <li>Priority scheduling</li>
      <li>1-year warranty</li>
    </ul>
    <a class="price-card__cta" href="#quote">Choose Standard</a>
  </li>
  <!-- third tier: same as Basic -->
</ul>
```

## CSS

```css
/* Grid */
.card-grid {
  display: grid; gap: var(--space-lg);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  margin: 0; padding: 0; list-style: none;
}
.card-grid--pricing { padding-top: var(--space-md); } /* room for the "Most popular" flag */

/* Feature card */
.feature-card {
  position: relative; display: flex; flex-direction: column; gap: var(--space-sm);
  padding: var(--space-lg);
  background: var(--surface-light); border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);
  transition: transform var(--transition-smooth), box-shadow var(--transition-smooth);
}
.feature-card__icon {
  display: grid; place-items: center; width: 3rem; height: 3rem; margin-bottom: var(--space-sm);
  border-radius: var(--radius-md);
  background: color-mix(in srgb, var(--primary) 10%, var(--surface-light)); color: var(--primary);
}
.feature-card__icon svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linejoin: round; }
.feature-card__title { margin: 0; font-size: 1.125rem; }
.feature-card__title a { color: var(--text-main); text-decoration: none; }
.feature-card__title a::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-lg); } /* stretched link */
.feature-card__title a:focus-visible { outline: 2px solid transparent; }
.feature-card__title a:focus-visible::after { box-shadow: var(--focus-ring); }
.feature-card__text { flex: 1; margin: 0; line-height: 1.6; color: var(--text-muted); }
.feature-card__more { margin-top: var(--space-sm); font-size: 0.9375rem; font-weight: 600; color: var(--primary); }
.feature-card__arrow { display: inline-block; transition: transform var(--transition-fast); }

@media (hover: hover) {
  .feature-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
  .feature-card:hover .feature-card__arrow { transform: translateX(4px); }
}

/* Review card */
.review-card {
  box-sizing: border-box; height: 100%;
  display: flex; flex-direction: column; gap: var(--space-md);
  margin: 0; padding: var(--space-lg);
  background: var(--surface-light); border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);
}
.review-card__stars { /* --rating accepts decimals, e.g. 4.5 */
  --rating: 5;
  align-self: flex-start; font-size: 1.25rem; line-height: 1; letter-spacing: 0.1em;
  background: linear-gradient(90deg, var(--accent) calc(var(--rating) / 5 * 100%), var(--border-subtle) 0);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.review-card__quote { flex: 1; margin: 0; font-size: 1.0625rem; line-height: 1.6; }
.review-card__quote::before {
  content: "\201C"; content: "\201C" / ""; /* decorative: empty alt text for screen readers */
  display: block; height: 1.5rem; font-size: 3rem; line-height: 1;
  color: color-mix(in srgb, var(--primary) 35%, transparent);
}
.review-card__quote p { margin: 0; }
.review-card__author {
  display: flex; align-items: center; gap: var(--space-sm);
  padding-top: var(--space-md); border-top: 1px solid var(--border-subtle);
}
.review-card__avatar {
  display: grid; place-items: center; flex: none;
  width: 3rem; height: 3rem; border-radius: var(--radius-full); object-fit: cover;
  background: color-mix(in srgb, var(--primary) 10%, var(--surface-light));
  color: var(--primary); font-weight: 700;
}
.review-card__name { display: block; font-weight: 600; }
.review-card__meta { display: block; font-size: 0.875rem; color: var(--text-muted); }

/* Pricing card */
.price-card {
  position: relative; display: flex; flex-direction: column;
  padding: var(--space-xl) var(--space-lg);
  background: var(--surface-light); border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);
}
.price-card--featured { border: 2px solid var(--primary); box-shadow: var(--shadow-lg); }
.price-card__flag {
  position: absolute; top: 0; left: 50%; transform: translate(-50%, -50%);
  margin: 0; padding: var(--space-xs) var(--space-md); white-space: nowrap;
  border-radius: var(--radius-full); background: var(--primary); color: var(--text-inverse);
  font-size: 0.8125rem; font-weight: 700;
}
.price-card__name { margin: 0; font-size: 1.125rem; }
.price-card__price { margin: var(--space-sm) 0 0; color: var(--text-muted); }
.price-card__amount {
  font-size: 2.5rem; font-weight: 700; line-height: 1.1; letter-spacing: -0.02em; color: var(--text-main);
}
.price-card__desc { margin: var(--space-sm) 0 0; color: var(--text-muted); }
.price-card__features {
  flex: 1; display: grid; gap: var(--space-sm); align-content: start;
  margin: var(--space-lg) 0; padding: var(--space-lg) 0 0;
  border-top: 1px solid var(--border-subtle); list-style: none; line-height: 1.5;
}
.price-card__features li { position: relative; padding-left: var(--space-lg); }
.price-card__features li::before { /* CSS checkmark */
  content: ""; position: absolute; left: var(--space-xs); top: 0.35em;
  width: 0.4em; height: 0.8em;
  border: solid var(--primary); border-width: 0 0.15em 0.15em 0;
  transform: rotate(45deg);
}
.price-card__cta {
  display: flex; align-items: center; justify-content: center;
  min-height: 2.75rem; padding: var(--space-sm) var(--space-lg);
  border: 1px solid var(--primary); border-radius: var(--radius-md);
  color: var(--primary); font-weight: 600; text-decoration: none;
  transition: background-color var(--transition-fast), border-color var(--transition-fast), color var(--transition-fast);
}
.price-card__cta:hover, .price-card--featured .price-card__cta { background: var(--primary); color: var(--text-inverse); }
.price-card--featured .price-card__cta:hover { background: var(--primary-hover); border-color: var(--primary-hover); }
.price-card__cta:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
```

## Notes

- **Feature cards:** the title link stretches over the card via `::after`, so each card is one tab stop with a meaningful name. "Learn more" is `aria-hidden` to avoid repeated, vague links. Don't put other links or buttons inside a stretched card.
- The hover lift only runs on devices that can hover. The motion tokens collapse transitions under `prefers-reduced-motion`.
- **Reviews:** keep `aria-label` in sync with `--rating`. Publish only genuine, attributable reviews.
- **Pricing:** the flag comes after the `<h3>` in source, so it's announced with its tier. CTA text is unique per tier ("Choose Standard") so link lists stay meaningful.
- Card titles are `<h3>` and assume a section `<h2>` above. Adjust to fit the page outline.
- **React:** `style={{ '--rating': 4.5 }}`, `class` → `className`.
- **Tailwind (v4):** grid `grid grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))] gap-6`. Lift `hover:-translate-y-1 hover:shadow-(--shadow-lg)` (v4 `hover:` already applies only on hover-capable devices).
