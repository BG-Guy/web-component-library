# Card Variants

Six standalone card layouts that go beyond the feature, review and pricing cards in `components/cards-and-grids.md`. Depends on `tokens/variables.css`.

| #  | Pattern                                                                         | JS   |
| -- | ------------------------------------------------------------------------------- | ---- |
| 1  | **Article card**: image, category tag, title, excerpt, date and read time; whole card links | none |
| 2  | **Product / package card**: image, badge, rating, "from" price and its own quote button | none |
| 3  | **Horizontal media card**: image beside text, stacks when its own width is narrow | none |
| 4  | **Image overlay card**: title and text on a scrim over a full-bleed photo; whole card links | none |
| 5  | **Glass card**: frosted panel on a token gradient, with a solid fallback        | none |
| 6  | **Profile card**: avatar or initials, name, role, bio, and Call and Email buttons | none |

## 1. Article card

Blog or guide teaser. Its title link stretches over the card, so the whole card is one tab stop named by the title. Grid: 1 column on phones, up to 3 at `--container-max`. Place inside your page container.

### HTML

```html
<ul class="article-card-grid" role="list">
  <li>
    <article class="article-card">
      <img class="article-card__img" src="gutter-cleaning.jpg" alt="" width="800" height="450" loading="lazy">
      <div class="article-card__body">
        <h3 class="article-card__title">
          <a class="article-card__link" href="https://example.com/blog/fall-gutter-checklist">A 10-minute fall gutter checklist</a>
        </h3>
        <p class="article-card__tag">Maintenance</p>
        <p class="article-card__excerpt">Clear clogs before the first freeze and spot the small leaks that turn into big repairs.</p>
        <p class="article-card__meta">
          <time datetime="2026-09-28">Sep 28, 2026</time> <span aria-hidden="true">·</span> 4 min read
        </p>
      </div>
    </article>
  </li>
  <!-- repeat per article -->
</ul>
```

### CSS

```css
/* Grid: auto-fit columns, no media queries */
.article-card-grid {
  display: grid; gap: var(--space-lg);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  margin: 0; padding: 0; list-style: none;
}

/* Card: positioned so the title link's ::after can cover it. No overflow: hidden, or the focus ring is clipped */
.article-card {
  position: relative; display: flex; flex-direction: column; box-sizing: border-box; height: 100%;
  background: var(--surface-light); border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);
  transition: transform var(--transition-smooth), box-shadow var(--transition-smooth);
}
.article-card__img {
  display: block; width: 100%; height: auto; aspect-ratio: 16 / 9; object-fit: cover;
  border-radius: calc(var(--radius-lg) - 1px) calc(var(--radius-lg) - 1px) 0 0; background: var(--border-subtle);
}
.article-card__body { flex: 1; display: flex; flex-direction: column; gap: var(--space-sm); padding: var(--space-lg); }

/* Tag follows the title in source, shown above it */
.article-card__tag {
  order: -1; align-self: flex-start; margin: 0; padding: var(--space-xs) var(--space-sm);
  border-radius: var(--radius-sm); background: color-mix(in srgb, var(--primary) 10%, var(--surface-light));
  color: var(--text-main); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase;
}

/* Stretched title link; the focus ring is drawn on the card-sized ::after */
.article-card__title { margin: 0; font-size: 1.125rem; line-height: 1.35; }
.article-card__link { color: var(--text-main); text-decoration: none; }
.article-card__link::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-lg); }
.article-card__link:focus-visible { outline: 2px solid transparent; }
.article-card__link:focus-visible::after { box-shadow: var(--focus-ring); }

.article-card__excerpt { flex: 1; margin: 0; line-height: 1.6; color: var(--text-muted); }
.article-card__meta { margin: 0; font-size: 0.875rem; color: var(--text-muted); }

/* Lift only where hover exists */
@media (hover: hover) {
  .article-card:hover { transform: translateY(calc(-1 * var(--space-xs))); box-shadow: var(--shadow-lg); }
  .article-card:hover .article-card__link { text-decoration: underline; }
}
```

### Notes

- Keep the tag and meta as plain text. Anything interactive inside the card would sit under the stretched link. Link to category pages from somewhere else on the page.
- The tag comes after the `<h3>` in source and moves above it with `order: -1`. Heading navigation lands on the title, and the category is read after it.
- The image is `alt=""` because the title already names the post. The card itself doesn't clip; the image rounds its own corners so the focus ring around the card stays visible.
- Titles are `<h3>` and assume a section `<h2>` above. The motion tokens collapse the lift under `prefers-reduced-motion`.

## 2. Product / package card

A service package with a "Best seller" badge, a star rating with text for screen readers, a "from" price and its own quote button. It has no whole-card link. Place inside your page container.

### HTML

```html
<ul class="product-card-grid" role="list">
  <li>
    <article class="product-card">
      <img class="product-card__img" src="water-heater.jpg" alt="" width="800" height="600" loading="lazy">
      <div class="product-card__body">
        <h3 class="product-card__title">Tankless water heater install</h3>
        <p class="product-card__badge">Best seller</p>
        <p class="product-card__rating">
          <span class="product-card__stars" style="--product-card-rating: 4.8" aria-hidden="true">★★★★★</span>
          <span>4.8<span class="product-card__sr"> out of 5 stars,</span></span>
          <span class="product-card__count">(126 reviews)</span>
        </p>
        <p class="product-card__price">From <span class="product-card__amount">$1,850</span> installed</p>
        <a class="product-card__cta" href="/quote?package=tankless-water-heater">
          Get a quote<span class="product-card__sr"> for tankless water heater install</span>
        </a>
      </div>
    </article>
  </li>
  <!-- repeat per package; drop the badge where it doesn't apply -->
</ul>
```

### CSS

```css
/* Grid */
.product-card-grid {
  display: grid; gap: var(--space-lg);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  margin: 0; padding: 0; list-style: none;
}

/* Card: positioned only to anchor the badge */
.product-card {
  position: relative; display: flex; flex-direction: column; box-sizing: border-box; height: 100%;
  background: var(--surface-light); border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);
}
.product-card__img {
  display: block; width: 100%; height: auto; aspect-ratio: 4 / 3; object-fit: cover;
  border-radius: calc(var(--radius-lg) - 1px) calc(var(--radius-lg) - 1px) 0 0; background: var(--border-subtle);
}
.product-card__body { flex: 1; display: flex; flex-direction: column; gap: var(--space-sm); padding: var(--space-lg); }
.product-card__title { margin: 0; font-size: 1.125rem; line-height: 1.35; }

/* Badge: after the title in source, pinned over the image */
.product-card__badge {
  position: absolute; top: var(--space-sm); left: var(--space-sm); margin: 0;
  padding: var(--space-xs) var(--space-sm); border-radius: var(--radius-full); box-shadow: var(--shadow-sm);
  background: var(--accent); color: var(--text-main); font-size: 0.75rem; font-weight: 700;
}

/* Rating: decorative stars filled to --product-card-rating; the text carries the value */
.product-card__rating { display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-xs); margin: 0; font-size: 0.875rem; font-weight: 600; }
.product-card__stars {
  --product-card-rating: 5;
  font-size: 1rem; line-height: 1; letter-spacing: 0.1em;
  background: linear-gradient(90deg, var(--accent) calc(var(--product-card-rating) / 5 * 100%), var(--border-subtle) 0);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.product-card__count { font-weight: 400; color: var(--text-muted); }

/* Price and CTA pinned to the bottom so buttons line up across a row */
.product-card__price { margin: auto 0 0; padding-top: var(--space-sm); color: var(--text-muted); }
.product-card__amount { font-size: 1.5rem; font-weight: 700; color: var(--text-main); }
.product-card__cta {
  display: flex; align-items: center; justify-content: center; min-height: 2.75rem;
  padding: var(--space-sm) var(--space-lg); border-radius: var(--radius-md);
  background: var(--primary); color: var(--text-inverse); font-weight: 600; text-decoration: none;
  transition: background-color var(--transition-fast);
}
.product-card__cta:hover { background: var(--primary-hover); }
.product-card__cta:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

.product-card__sr { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
```

### Notes

- **No stretched link, on purpose.** The card already has an action. A card-sized link would cover the button or need z-index holes cut for it. It would also add a second tab stop per card and turn every stray tap on the card into a page change. If you need a details page, make the title an ordinary link beside the button. For the same reason there's no hover lift, because a lift suggests the whole card is clickable.
- The stars are `aria-hidden`. Screen readers announce the visible score plus the hidden "out of 5 stars". Keep `--product-card-rating` in sync with the score.
- The hidden suffix makes each CTA name unique ("Get a quote for tankless water heater install") and still starts with the visible label (WCAG 2.5.3). It's a link to the quote form; switch to `<button type="button">` only if it opens a `components/modals.md` dialog.
- The badge follows the `<h3>` in source, so it's announced with its package. `--accent` pairs with `--text-main` at about 6.8:1.

## 3. Horizontal media card

Image on the left, content on the right. A container query switches it to that layout when the card itself is at least 28rem wide, whatever the viewport. Narrower cards stack. Whole card links, as in pattern 1. Place inside your page container.

### HTML

```html
<!-- In a grid: each <li> is the card's container -->
<ul class="media-card-list" role="list">
  <li class="media-card-wrap">
    <article class="media-card">
      <div class="media-card__media">
        <img class="media-card__img" src="shower-remodel.jpg" alt="" width="640" height="480" loading="lazy">
      </div>
      <div class="media-card__body">
        <h3 class="media-card__title"><a class="media-card__link" href="/projects/walk-in-shower">Walk-in shower conversion</a></h3>
        <p class="media-card__text">We swapped a cramped tub for a curbless tiled shower with a fold-down bench in under a week.</p>
        <p class="media-card__meta">Springfield · 5 days</p>
      </div>
    </article>
  </li>
  <!-- repeat per card -->
</ul>

<!-- Standalone: wrap the card in <div class="media-card-wrap"> -->
```

### CSS

```css
/* Container: each card gets its own wrapper, so the query measures the card, not the page */
.media-card-wrap { container: media-card / inline-size; }
.media-card-list {
  display: grid; gap: var(--space-lg);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 22rem), 1fr));
  margin: 0; padding: 0; list-style: none;
}

/* Stacked by default, which is also the fallback without container queries */
.media-card {
  --media-card-inner-radius: calc(var(--radius-lg) - 1px);
  position: relative; display: grid; box-sizing: border-box; height: 100%;
  background: var(--surface-light); border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);
  transition: transform var(--transition-smooth), box-shadow var(--transition-smooth);
}
.media-card__media { position: relative; aspect-ratio: 16 / 9; }
.media-card__img {
  position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;
  border-radius: var(--media-card-inner-radius) var(--media-card-inner-radius) 0 0; background: var(--border-subtle);
}
.media-card__body { display: flex; flex-direction: column; gap: var(--space-sm); padding: var(--space-lg); }

/* Stretched title link with the focus ring on the card */
.media-card__title { margin: 0; font-size: 1.125rem; line-height: 1.35; }
.media-card__link { color: var(--text-main); text-decoration: none; }
.media-card__link::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-lg); }
.media-card__link:focus-visible { outline: 2px solid transparent; }
.media-card__link:focus-visible::after { box-shadow: var(--focus-ring); }
.media-card__text { margin: 0; line-height: 1.6; color: var(--text-muted); }
.media-card__meta { margin: auto 0 0; font-size: 0.875rem; font-weight: 600; color: var(--text-muted); }

/* Wide card: image left (40%), content right. The image fills the row and never sets its height */
@container media-card (min-width: 28rem) {
  .media-card { grid-template-columns: minmax(0, 2fr) minmax(0, 3fr); }
  .media-card__media { aspect-ratio: auto; min-height: 10rem; }
  .media-card__img { border-radius: var(--media-card-inner-radius) 0 0 var(--media-card-inner-radius); }
}

@media (hover: hover) {
  .media-card:hover { transform: translateY(calc(-1 * var(--space-xs))); box-shadow: var(--shadow-lg); }
  .media-card:hover .media-card__link { text-decoration: underline; }
}
```

### Notes

- Every card needs its own `.media-card-wrap`. An element can't query its own size, and a single wrapper around the whole grid would measure the grid, not each card.
- `container-type: inline-size` stops the wrapper from sizing to its content. Inside a flex row or a `fit-content` box it collapses to zero width, so give it a width there (e.g. `flex: 1`).
- Container queries work in Chrome 105+, Safari 16+ and Firefox 110+. Older browsers skip the `@container` block and keep the stacked layout, which works at any width.
- The image is absolutely positioned inside `.media-card__media`, so the text sets the row height and the photo crops to fit. Tune the 28rem threshold to your content.

## 4. Image overlay card

A full-bleed photo with the title and text on a dark scrim along the bottom. The image zooms slightly on hover and on keyboard focus. Whole card links. Place inside your page container.

### HTML

```html
<ul class="overlay-card-grid" role="list">
  <li>
    <article class="overlay-card">
      <div class="overlay-card__media">
        <img class="overlay-card__img" src="patio.jpg" alt="" width="800" height="1000" loading="lazy">
      </div>
      <div class="overlay-card__body">
        <h3 class="overlay-card__title"><a class="overlay-card__link" href="/projects/backyard-patio">Backyard patio makeover</a></h3>
        <p class="overlay-card__text">Stamped concrete, a low seating wall and path lighting in Springfield.</p>
      </div>
    </article>
  </li>
  <!-- repeat per card -->
</ul>
```

### CSS

```css
/* Grid */
.overlay-card-grid {
  display: grid; gap: var(--space-lg);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  margin: 0; padding: 0; list-style: none;
}

/* Card: content pinned to the bottom. Dark background shows while the image loads */
.overlay-card {
  --overlay-card-scrim: color-mix(in srgb, var(--surface-dark) 80%, transparent);
  position: relative; isolation: isolate;
  display: flex; flex-direction: column; justify-content: flex-end; aspect-ratio: 4 / 5;
  border-radius: var(--radius-lg); background: var(--surface-dark); box-shadow: var(--shadow-sm);
  color: var(--text-inverse);
}

/* Media layer clips the zoom, so the card itself never clips its focus ring */
.overlay-card__media { position: absolute; inset: 0; overflow: hidden; border-radius: inherit; }
.overlay-card__img { display: block; width: 100%; height: 100%; object-fit: cover; transition: transform var(--transition-smooth); }

/* Scrim: fades in over the top padding, so every line of text sits on the solid part.
   z-index works on a flex item without position, so the link's ::after still spans the whole card */
.overlay-card__body {
  z-index: 1;
  padding: var(--space-2xl) var(--space-lg) var(--space-lg);
  border-radius: 0 0 var(--radius-lg) var(--radius-lg);
  background: linear-gradient(to bottom, transparent, var(--surface-dark) var(--space-2xl));
}
/* Translucent scrim where color-mix() works: 80% --surface-dark keeps --text-inverse at 9:1 or better, even over pure white */
@supports (color: color-mix(in srgb, currentColor 50%, transparent)) {
  .overlay-card__body { background: linear-gradient(to bottom, transparent, var(--overlay-card-scrim) var(--space-2xl)); }
}

/* Stretched title link */
.overlay-card__title { margin: 0; font-size: 1.25rem; line-height: 1.3; }
.overlay-card__link { color: inherit; text-decoration: none; }
.overlay-card__link::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-lg); }
.overlay-card__link:focus-visible { outline: 2px solid transparent; }
.overlay-card__link:focus-visible::after { box-shadow: var(--focus-ring); }
.overlay-card__text { margin: var(--space-xs) 0 0; font-size: 0.9375rem; line-height: 1.5; }

/* Zoom on hover (hover devices only) and on keyboard focus */
.overlay-card:focus-within .overlay-card__img { transform: scale(1.05); }
@media (hover: hover) {
  .overlay-card:hover .overlay-card__img { transform: scale(1.05); }
  .overlay-card:hover .overlay-card__link { text-decoration: underline; }
}
```

### Notes

- **Contrast:** text only ever sits on the solid part of the scrim; the fade lives in the top padding. 80% `--surface-dark` over a pure white photo still gives `--text-inverse` about 9:1, so no image can break it. Without `color-mix()` the scrim is solid `--surface-dark`. That's done with `@supports` rather than a second declaration, because a failed `color-mix()` containing `var()` would drop the background entirely. Don't use `--text-inverse-muted` here: over a white image it falls to about 3.7:1.
- The image is `alt=""` because the title names it. Give it real alt text if it shows something the text doesn't.
- The motion tokens make the zoom instant under `prefers-reduced-motion`.
- The focus ring assumes a light page. On a dark section, give the `::after` `outline: 2px solid var(--text-inverse); outline-offset: 2px` instead of the box-shadow.

## 5. Glass card

A frosted, translucent panel on a colorful gradient made from brand tokens. The gradient wrapper is included. Where `backdrop-filter` isn't supported, the card falls back to a solid surface. Place inside your page container.

### HTML

```html
<div class="glass-card-bg">
  <div class="glass-card">
    <p class="glass-card__eyebrow">Same-day guarantee</p>
    <h3 class="glass-card__title">Book by noon, fixed by tonight</h3>
    <p class="glass-card__text">A licensed tech is at your door the same day anywhere in Springfield, with the price agreed before work starts.</p>
    <a class="glass-card__cta" href="#quote">Book a visit</a>
  </div>
</div>
```

### CSS

```css
/* Background: decorative token gradient with color blobs for the glass to blur */
.glass-card-bg {
  padding: var(--space-xl) var(--space-md); border-radius: var(--radius-lg);
  background:
    radial-gradient(circle at 15% 20%, var(--accent), transparent 45%),
    radial-gradient(circle at 85% 85%, var(--primary), transparent 50%),
    linear-gradient(135deg, var(--primary-hover), var(--surface-dark));
}
@media (min-width: 768px) {
  .glass-card-bg { padding: var(--space-2xl); }
}

/* Fallback first: solid surface */
.glass-card {
  --glass-card-blur: 1rem;
  max-width: 28rem; margin-inline: auto; padding: var(--space-lg);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  background: var(--surface-light); color: var(--text-main); box-shadow: var(--shadow-lg);
}
/* Frosted glass: 75% --surface-light over anything, even pure black, keeps --text-main at about 8:1 */
@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) and (color: color-mix(in srgb, currentColor 50%, transparent)) {
  .glass-card {
    background: color-mix(in srgb, var(--surface-light) 75%, transparent);
    border-color: color-mix(in srgb, var(--surface-light) 60%, transparent);
    -webkit-backdrop-filter: blur(var(--glass-card-blur)) saturate(1.5);
    backdrop-filter: blur(var(--glass-card-blur)) saturate(1.5);
  }
}
/* Respect the OS "reduce transparency" setting */
@media (prefers-reduced-transparency: reduce) {
  .glass-card { background: var(--surface-light); -webkit-backdrop-filter: none; backdrop-filter: none; }
}

/* Content: --text-main only (see Notes) */
.glass-card__eyebrow { margin: 0; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; }
.glass-card__title { margin: var(--space-xs) 0 0; font-size: 1.375rem; line-height: 1.25; }
.glass-card__text { margin: var(--space-sm) 0 0; line-height: 1.6; }
.glass-card__cta {
  display: inline-flex; align-items: center; justify-content: center; min-height: 2.75rem; max-width: 100%;
  margin-top: var(--space-lg); padding: var(--space-sm) var(--space-lg); box-sizing: border-box;
  border-radius: var(--radius-md); background: var(--primary); color: var(--text-inverse);
  font-weight: 600; text-decoration: none; transition: background-color var(--transition-fast);
}
.glass-card__cta:hover { background: var(--primary-hover); }
.glass-card__cta:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
```

### Notes

- **How contrast is guaranteed:** the check doesn't rely on the gradient's colors. The worst possible backdrop is pure black, and 75% `--surface-light` over black blends to a light gray that still gives `--text-main` about 8:1. That holds for any gradient, photo or brand override behind the card. Use `--text-main` for all text on the glass: `--text-muted` and `--primary` text drop to about 3:1 when a dark color sits behind.
- **Fallback:** the solid card applies where `backdrop-filter` or `color-mix()` is missing, and under `prefers-reduced-transparency` (Chrome 118+). `color-mix()` is part of the `@supports` test because a failed `color-mix()` containing `var()` would leave the card transparent instead of solid.
- Safari before 18 needs the `-webkit-` prefix. Blur is GPU-heavy, so avoid many glass cards on one screen or glass over video.
- The gradient carries no text. For a full-bleed band, drop the radius and add an inner wrapper (`max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter)`).

## 6. Profile card

A team member with an avatar (or an initials fallback), name, role, short bio and Call / Email buttons. Each button's accessible name includes the person's name. Place inside your page container.

### HTML

```html
<ul class="profile-card-grid" role="list">
  <li>
    <article class="profile-card">
      <img class="profile-card__avatar" src="avatar.jpg" alt="" width="96" height="96" loading="lazy">
      <!-- No photo: <span class="profile-card__avatar" aria-hidden="true">SR</span> -->
      <h3 class="profile-card__name">Sam Rivera</h3>
      <p class="profile-card__role">Lead Plumber</p>
      <p class="profile-card__bio">Fifteen years fixing leaks, re-piping older homes and installing water heaters across Springfield.</p>
      <div class="profile-card__actions">
        <a class="profile-card__btn profile-card__btn--primary" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z" /></svg>
          Call<span class="profile-card__sr"> Sam Rivera</span>
        </a>
        <a class="profile-card__btn" href="mailto:hello@example.com">
          <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="14" rx="2" /><path d="m3 7 9 6 9-6" /></svg>
          Email<span class="profile-card__sr"> Sam Rivera</span>
        </a>
      </div>
    </article>
  </li>
  <!-- repeat per person -->
</ul>
```

### CSS

```css
/* Grid */
.profile-card-grid {
  display: grid; gap: var(--space-lg);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  margin: 0; padding: 0; list-style: none;
}

/* Card: centered column, actions pinned to the bottom */
.profile-card {
  display: flex; flex-direction: column; align-items: center; box-sizing: border-box; height: 100%;
  padding: var(--space-xl) var(--space-lg); text-align: center;
  background: var(--surface-light); border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);
}

/* Avatar: the same class styles the photo and the initials fallback */
.profile-card__avatar {
  display: grid; place-items: center; flex: none; width: 6rem; height: 6rem; margin-bottom: var(--space-md);
  border-radius: var(--radius-full); object-fit: cover;
  background: color-mix(in srgb, var(--primary) 10%, var(--surface-light)); color: var(--primary);
  font-size: 1.75rem; font-weight: 700;
}
.profile-card__name { margin: 0; font-size: 1.25rem; }
.profile-card__role { margin: var(--space-xs) 0 0; font-size: 0.875rem; font-weight: 600; color: var(--primary); }
.profile-card__bio { flex: 1; margin: var(--space-md) 0 0; line-height: 1.6; color: var(--text-muted); }

/* Actions: two 44px buttons that wrap on narrow cards */
.profile-card__actions { display: flex; flex-wrap: wrap; gap: var(--space-sm); width: 100%; margin-top: var(--space-lg); }
.profile-card__btn {
  flex: 1 1 7rem; display: inline-flex; align-items: center; justify-content: center; gap: var(--space-sm);
  box-sizing: border-box; min-height: 2.75rem; padding: var(--space-sm) var(--space-md);
  border: 1px solid var(--primary); border-radius: var(--radius-md);
  color: var(--primary); font-weight: 600; text-decoration: none;
  transition: background-color var(--transition-fast), border-color var(--transition-fast), color var(--transition-fast);
}
.profile-card__btn:hover, .profile-card__btn--primary { background: var(--primary); color: var(--text-inverse); }
.profile-card__btn--primary:hover { background: var(--primary-hover); border-color: var(--primary-hover); }
.profile-card__btn:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.profile-card__btn svg {
  flex: none; width: 1.25rem; height: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}

.profile-card__sr { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
```

### Notes

- Visible "Call" plus hidden " Sam Rivera" gives the accessible name "Call Sam Rivera", which starts with the visible label (WCAG 2.5.3). Hidden text instead of `aria-label` means page translation also translates the name.
- The avatar is `alt=""` and the initials are `aria-hidden` because the name follows straight after. Initials are large bold text, so `--primary` on the tint needs only 3:1.
- No stretched link: the card has two actions of its own, so there's no hover lift either.
- Desktop browsers may have no `tel:` handler. If desktop visitors need the number, show it as text, e.g. in the role line.
