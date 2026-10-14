# Magnifying Dock

A macOS-style dock as a floating bottom nav: six glossy app-icon tiles on a frosted glass pill. Hover with a mouse, or drag a finger along it, and the tiles swell by distance from the pointer with a smooth Gaussian falloff (about 1.6× under the pointer, 1.25× for neighbours), lift clear of the glass and show a label; a tap hops the tile on a spring and the current page carries a glowing dot. On phones the dock sits in the thumb zone above the home indicator and scales its magnification to the room it has, so it never overflows a 320px screen. Depends on `tokens/variables.css`.

**Motion:** magnification eased through a registered `--dock-nav-s` (`--dur-2`, `--ease-out`) · tile lift and label pop (`--dur-3`, `--ease-spring`) · press squash (`--ease-spring`) · tap hop that settles on `--ease-spring` · current-dot spring-in (`--dur-4`).

## HTML

```html
<div class="dock-nav-demo">
  <div class="dock-nav-demo__page">
    <header class="dock-nav-demo__top">
      <span class="dock-nav-demo__brand"><span class="dock-nav-demo__mark" aria-hidden="true"></span>Brand</span>
      <span class="dock-nav-demo__open"><span class="dock-nav-demo__led" aria-hidden="true"></span>Open now · Springfield</span>
    </header>

    <h2 class="dock-nav-demo__title">Good afternoon, Alex.</h2>
    <p class="dock-nav-demo__lead">Your boiler service is booked. Sam will text you when he's ten minutes out.</p>

    <article class="dock-nav-demo__visit">
      <div class="dock-nav-demo__art" aria-hidden="true"><span></span><span></span><span></span></div>
      <div class="dock-nav-demo__visit-body">
        <p class="dock-nav-demo__kicker">Next visit</p>
        <h3 class="dock-nav-demo__visit-title">Annual boiler service</h3>
        <p class="dock-nav-demo__meta">Thu 16 Oct · 10:00–12:00 · Westlake</p>
      </div>
    </article>

    <ul class="dock-nav-demo__stats" role="list">
      <li><strong>4.9</strong><span>Average rating</span></li>
      <li><strong>12 min</strong><span>Nearest tech</span></li>
      <li><strong>$0</strong><span>Call-out fee</span></li>
    </ul>

    <figure class="dock-nav-demo__quote">
      <blockquote>"Fixed a leak nobody else could find. Tidy, quick and the price matched the quote."</blockquote>
      <figcaption>Dana R. · Northside</figcaption>
    </figure>
  </div>

  <nav class="dock-nav" aria-label="Main" data-dock-nav data-dock-nav-demo>
    <ul class="dock-nav__list" role="list">
      <li class="dock-nav__item">
        <a class="dock-nav__link" href="/" aria-current="page">
          <span class="dock-nav__tile dock-nav__tile--home" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="24" height="24" focusable="false"><path d="M3 10.5 12 3l9 7.5" /><path d="M5.5 9v11a1 1 0 0 0 1 1H10v-6h4v6h3.5a1 1 0 0 0 1-1V9" /></svg>
          </span>
          <span class="dock-nav__label">Home</span>
          <span class="dock-nav__dot" aria-hidden="true"></span>
        </a>
      </li>
      <li class="dock-nav__item">
        <a class="dock-nav__link" href="/services">
          <span class="dock-nav__tile dock-nav__tile--services" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="24" height="24" focusable="false"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z" /></svg>
          </span>
          <span class="dock-nav__label">Services</span>
          <span class="dock-nav__dot" aria-hidden="true"></span>
        </a>
      </li>
      <li class="dock-nav__item">
        <a class="dock-nav__link" href="/book">
          <span class="dock-nav__tile dock-nav__tile--book" aria-hidden="true">
            <span class="dock-nav__cal"><small>Thu</small><b>16</b></span>
          </span>
          <span class="dock-nav__label">Book</span>
          <span class="dock-nav__dot" aria-hidden="true"></span>
        </a>
      </li>
      <li class="dock-nav__item">
        <a class="dock-nav__link" href="/reviews">
          <span class="dock-nav__tile dock-nav__tile--reviews" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="24" height="24" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          </span>
          <span class="dock-nav__label">Reviews</span>
          <span class="dock-nav__dot" aria-hidden="true"></span>
        </a>
      </li>
      <li class="dock-nav__item">
        <a class="dock-nav__link" href="/gallery">
          <span class="dock-nav__tile dock-nav__tile--gallery" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="24" height="24" focusable="false"><rect x="3" y="3" width="18" height="18" rx="3" /><circle cx="9" cy="9" r="2" /><path d="m21 15-3.1-3.1a2 2 0 0 0-2.8 0L6 21" /></svg>
          </span>
          <span class="dock-nav__label">Gallery</span>
          <span class="dock-nav__dot" aria-hidden="true"></span>
        </a>
      </li>
      <li class="dock-nav__item dock-nav__item--call">
        <a class="dock-nav__link" href="tel:+15555550123">
          <span class="dock-nav__tile dock-nav__tile--call" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="24" height="24" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          </span>
          <span class="dock-nav__label">Call us</span>
          <span class="dock-nav__dot" aria-hidden="true"></span>
        </a>
      </li>
    </ul>
  </nav>
</div>
```

## CSS

```css
@property --dock-nav-s { syntax: "<number>"; inherits: true; initial-value: 1; }

/* Demo page: a light app screen so the dock sits in context */
.dock-nav-demo {
  display: flex; flex-direction: column; min-height: 100vh; min-height: 100svh;
  background:
    radial-gradient(36rem 22rem at 100% 0%, color-mix(in srgb, var(--primary) 16%, transparent), transparent 70%),
    radial-gradient(30rem 20rem at 0% 60%, color-mix(in srgb, var(--primary-2) 13%, transparent), transparent 70%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
.dock-nav-demo__page { flex: 1; width: 100%; max-width: min(var(--container-max), 42rem); margin-inline: auto; padding: var(--space-lg) var(--gutter) var(--space-2xl); }
.dock-nav-demo__top { display: flex; align-items: center; justify-content: space-between; gap: var(--space-md); }
.dock-nav-demo__brand { display: inline-flex; align-items: center; gap: var(--space-sm); font: 600 1.0625rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.dock-nav-demo__mark { width: 1.5rem; height: 1.5rem; border-radius: var(--radius-md); background: var(--gradient-brand); box-shadow: var(--highlight), 0 6px 14px -6px var(--primary); }
.dock-nav-demo__open {
  display: inline-flex; align-items: center; gap: 0.4375rem; padding: 0.375rem 0.625rem; border-radius: var(--radius-full);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle); color: var(--text-muted); font: 500 0.75rem/1 var(--font-mono);
}
.dock-nav-demo__led { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 18%, transparent); }
.dock-nav-demo__title { margin: 2.5rem 0 0; font: 600 clamp(1.875rem, 1.4rem + 2.2vw, 2.75rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); }
.dock-nav-demo__lead { max-width: 30rem; margin: 0.75rem 0 0; color: var(--text-muted); font-size: 1rem; line-height: 1.55; }

.dock-nav-demo__visit { margin-top: var(--space-xl); padding: var(--space-sm) var(--space-sm) var(--space-lg); border-radius: var(--radius-2xl); background: var(--surface-light); box-shadow: 0 0 0 1px var(--border-subtle), var(--shadow-lg); }
.dock-nav-demo__art {
  position: relative; height: 9rem; overflow: hidden; border-radius: var(--radius-xl);
  background:
    radial-gradient(60% 90% at 75% 20%, color-mix(in srgb, var(--primary-2) 70%, transparent), transparent 70%),
    radial-gradient(70% 90% at 10% 100%, color-mix(in srgb, var(--primary) 80%, transparent), transparent 70%),
    var(--surface-deep);
}
.dock-nav-demo__art span { position: absolute; left: 68%; top: 58%; width: 3rem; aspect-ratio: 1; border-radius: 50%; translate: -50% -50%; box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 35%, transparent); }
.dock-nav-demo__art span:nth-child(1) { background: var(--surface-light); width: 0.75rem; box-shadow: 0 0 0 5px color-mix(in srgb, var(--surface-light) 25%, transparent), 0 0 24px 4px var(--primary-2); }
.dock-nav-demo__art span:nth-child(2) { width: 5.5rem; }
.dock-nav-demo__art span:nth-child(3) { width: 10rem; box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 18%, transparent); }
.dock-nav-demo__visit-body { padding: var(--space-md) var(--space-sm) 0; }
.dock-nav-demo__kicker { margin: 0; color: var(--primary); font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.dock-nav-demo__visit-title { margin: 0.5rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.dock-nav-demo__meta { margin: 0.375rem 0 0; color: var(--text-muted); font: 500 0.8125rem/1.4 var(--font-mono); }

.dock-nav-demo__stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-sm); margin: var(--space-md) 0 0; padding: 0; list-style: none; }
.dock-nav-demo__stats li { display: grid; gap: 0.25rem; padding: 0.875rem 0.75rem; border-radius: var(--radius-xl); background: var(--surface-light); box-shadow: 0 0 0 1px var(--border-subtle), var(--shadow-sm); }
.dock-nav-demo__stats strong { font: 600 1.25rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.dock-nav-demo__stats span { color: var(--text-muted); font-size: 0.75rem; line-height: 1.3; }
.dock-nav-demo__quote { margin: var(--space-md) 0 0; padding: var(--space-lg); border-radius: var(--radius-2xl); background: var(--surface-light); box-shadow: 0 0 0 1px var(--border-subtle), var(--shadow-sm); }
.dock-nav-demo__quote blockquote { margin: 0; font: 500 1.0625rem/1.5 var(--font-display); letter-spacing: -0.01em; }
.dock-nav-demo__quote figcaption { margin-top: 0.75rem; color: var(--text-muted); font: 500 0.75rem/1 var(--font-mono); }

/* Dock: sticky in the thumb zone, centred, grows sideways as tiles magnify */
.dock-nav {
  --dock-nav-tile: clamp(2.5rem, 2rem + 2.5vw, 3rem);
  --dock-nav-amp: 0.2; /* no-JS fallback; JS replaces it with the room-aware amount */
  position: sticky; bottom: calc(var(--space-sm) + env(safe-area-inset-bottom, 0px)); z-index: var(--z-sticky);
  width: fit-content; margin: 0 auto calc(var(--space-sm) + env(safe-area-inset-bottom, 0px));
  font-family: var(--font-sans);
}
.dock-nav__list {
  position: relative; display: flex; box-sizing: content-box; height: calc(var(--dock-nav-tile) + 0.5rem);
  margin: 0; padding: 0.25rem 0.3125rem 0.375rem; list-style: none; border-radius: var(--radius-2xl);
  background: color-mix(in srgb, var(--surface-light) 92%, transparent);
  box-shadow:
    inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 80%, transparent), var(--highlight),
    0 0 0 1px color-mix(in srgb, var(--text-main) 9%, transparent), var(--shadow-xl);
  touch-action: pan-y; -webkit-user-select: none; user-select: none;
}
@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .dock-nav__list { background: var(--glass); -webkit-backdrop-filter: blur(var(--blur-md)) saturate(1.8); backdrop-filter: blur(var(--blur-md)) saturate(1.8); }
}
.dock-nav__list::before { /* top-lit glass */
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: linear-gradient(180deg, color-mix(in srgb, var(--surface-light) 55%, transparent), transparent 60%);
}

/* Items: --dock-nav-s (1 at rest) drives size, lift and shadow; it eases because it is a registered number */
.dock-nav__item {
  --dock-nav-lift: calc((var(--dock-nav-s) - 1) * var(--dock-nav-tile) * -0.42);
  position: relative; flex: none; display: flex; align-items: flex-end;
  transition: --dock-nav-s var(--dur-2) var(--ease-out);
}
.dock-nav__item--call { margin-left: 0.3125rem; padding-left: 0.3125rem; }
.dock-nav__item--call::before { content: ""; position: absolute; left: 0; top: 20%; bottom: 20%; width: 1px; background: color-mix(in srgb, var(--text-main) 14%, transparent); }
.dock-nav__link {
  position: relative; display: block; padding: 0.25rem 0.1875rem; border-radius: var(--radius-xl);
  color: inherit; text-decoration: none; -webkit-tap-highlight-color: transparent; -webkit-touch-callout: none;
}
.dock-nav__link:focus-visible { outline: 2px solid transparent; }
.dock-nav__link:focus-visible .dock-nav__tile { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Tiles: glossy app icons built from tokens */
.dock-nav__tile {
  position: relative; display: grid; place-items: center; overflow: hidden;
  width: calc(var(--dock-nav-tile) * var(--dock-nav-s)); aspect-ratio: 1; border-radius: 27%;
  background: var(--dock-nav-fill); color: var(--dock-nav-ink, var(--text-inverse));
  box-shadow:
    inset 0 0 0 1px color-mix(in srgb, var(--text-main) 12%, transparent), var(--highlight),
    0 calc(2px + (var(--dock-nav-s) - 1) * 16px) calc(6px + (var(--dock-nav-s) - 1) * 32px) -4px color-mix(in srgb, var(--text-main) 42%, transparent);
  transform: translateY(var(--dock-nav-lift));
  transition: scale var(--dur-3) var(--ease-spring);
}
.dock-nav__tile::before { content: ""; position: absolute; inset: 0 0 50%; background: linear-gradient(180deg, color-mix(in srgb, var(--surface-light) 36%, transparent), transparent); pointer-events: none; }
.dock-nav__tile svg {
  position: relative; width: 52%; height: 52%; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
  filter: drop-shadow(0 1px 1px color-mix(in srgb, var(--text-main) 25%, transparent));
}
.dock-nav__tile--home { --dock-nav-fill: linear-gradient(150deg, color-mix(in srgb, var(--primary) 75%, var(--surface-light)), var(--primary) 45%, var(--primary-2)); }
.dock-nav__tile--services { --dock-nav-fill: radial-gradient(120% 90% at 30% 0%, color-mix(in srgb, var(--primary) 55%, var(--surface-deep)), var(--surface-deep) 72%); }
.dock-nav__tile--book { --dock-nav-fill: linear-gradient(var(--surface-light), var(--surface-muted)); --dock-nav-ink: var(--text-main); }
.dock-nav__tile--reviews { --dock-nav-fill: linear-gradient(160deg, color-mix(in srgb, var(--accent) 55%, var(--surface-light)), var(--accent) 55%, color-mix(in srgb, var(--accent) 80%, var(--danger))); --dock-nav-ink: var(--text-main); }
.dock-nav__tile--reviews svg { fill: color-mix(in srgb, var(--surface-light) 35%, transparent); filter: none; }
.dock-nav__tile--gallery { --dock-nav-fill: linear-gradient(155deg, color-mix(in srgb, var(--primary-2) 85%, var(--surface-light)), var(--primary-2) 50%, color-mix(in srgb, var(--primary-2) 60%, var(--surface-deep))); }
.dock-nav__tile--call { --dock-nav-fill: linear-gradient(170deg, color-mix(in srgb, var(--success) 75%, var(--surface-light)), var(--success) 70%); }

/* Book tile: a tiny calendar page that scales with the tile */
.dock-nav__cal { position: relative; display: grid; justify-items: center; align-content: start; width: 100%; height: 100%; font-size: calc(var(--dock-nav-tile) * var(--dock-nav-s)); }
.dock-nav__cal small { width: 100%; padding: 0.07em 0 0.05em; background: var(--danger); color: var(--text-inverse); font: 700 0.19em/1.2 var(--font-mono); letter-spacing: 0.1em; text-align: center; text-transform: uppercase; }
.dock-nav__cal b { color: var(--text-main); font: 600 0.5em/1.3 var(--font-display); letter-spacing: var(--tracking-tight); }

/* Label: a dark tooltip that rides above the lifted tile */
.dock-nav__label {
  position: absolute; bottom: calc(100% + 0.5rem); left: 50%; z-index: 1; pointer-events: none;
  padding: 0.375rem 0.625rem; border-radius: var(--radius-md);
  background: color-mix(in srgb, var(--surface-deep) 90%, transparent); color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), var(--shadow-lg);
  font: 600 0.75rem/1 var(--font-sans); white-space: nowrap;
  opacity: 0; transform: translateY(var(--dock-nav-lift)); translate: -50% 0.375rem; scale: 0.85;
  transition: opacity var(--dur-2) var(--ease-out), translate var(--dur-3) var(--ease-spring), scale var(--dur-3) var(--ease-spring);
}
.dock-nav__label::after { content: ""; position: absolute; top: 100%; left: 50%; width: 0.625rem; height: 0.3125rem; margin-left: -0.3125rem; background: inherit; clip-path: polygon(0 0, 100% 0, 50% 100%); }
.dock-nav__item.is-near .dock-nav__label,
.dock-nav__link:focus-visible .dock-nav__label { opacity: 1; translate: -50% 0; scale: 1; }

/* Current page: a glowing dot under the tile */
.dock-nav__dot {
  position: absolute; left: 50%; bottom: -0.1875rem; width: 0.25rem; height: 0.25rem; margin-left: -0.125rem; border-radius: 50%;
  background: var(--primary); opacity: 0; scale: 0;
  box-shadow: 0 0 0 2px color-mix(in srgb, var(--primary) 16%, transparent), 0 0 10px 2px color-mix(in srgb, var(--primary) 60%, transparent);
  transition: opacity var(--dur-2) var(--ease-out), scale var(--dur-4) var(--ease-spring);
}
.dock-nav__link[aria-current="page"] .dock-nav__dot { opacity: 1; scale: 1; }

/* Press squash, then a hop that settles on the spring */
.dock-nav__link:active .dock-nav__tile { scale: 0.9; }
.dock-nav__tile.is-bouncing { animation: dock-nav-hop var(--dur-4) var(--ease-out) both; }

/* Keyboard focus magnifies the focused tile and its neighbours (CSS, so it works without JS too) */
.dock-nav__item:has(> .dock-nav__link:focus-visible) { --dock-nav-s: calc(1 + var(--dock-nav-amp)); }
.dock-nav__item:has(> .dock-nav__link:focus-visible) + .dock-nav__item,
.dock-nav__item:has(+ .dock-nav__item > .dock-nav__link:focus-visible) { --dock-nav-s: calc(1 + var(--dock-nav-amp) * 0.42); }
/* Without JS, a mouse gets the same stepped magnification and labels on hover */
@media (hover: hover) {
  .dock-nav:not(.dock-nav--magnify) .dock-nav__item:hover { --dock-nav-s: calc(1 + var(--dock-nav-amp)); }
  .dock-nav:not(.dock-nav--magnify) .dock-nav__item:hover + .dock-nav__item,
  .dock-nav:not(.dock-nav--magnify) .dock-nav__item:has(+ .dock-nav__item:hover) { --dock-nav-s: calc(1 + var(--dock-nav-amp) * 0.42); }
  .dock-nav:not(.dock-nav--magnify) .dock-nav__link:hover .dock-nav__label { opacity: 1; translate: -50% 0; scale: 1; }
}
/* JS measures the resting layout with magnification switched off */
.dock-nav--measure .dock-nav__item { --dock-nav-s: 1 !important; transition: none !important; }

@media (min-width: 768px) {
  .dock-nav { bottom: calc(var(--space-md) + env(safe-area-inset-bottom, 0px)); margin-bottom: calc(var(--space-md) + env(safe-area-inset-bottom, 0px)); }
  .dock-nav__list { padding-inline: 0.4375rem; }
}

/* Reduced motion: no magnification and no hop; labels still appear on hover and focus */
@media (prefers-reduced-motion: reduce) {
  .dock-nav__item { --dock-nav-s: 1 !important; }
  .dock-nav *, .dock-nav *::before, .dock-nav *::after { animation: none !important; }
}

@keyframes dock-nav-hop {
  0% { translate: 0 0; }
  34% { translate: 0 -34%; animation-timing-function: var(--ease-spring); }
  100% { translate: 0 0; }
}
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('[data-dock-nav]').forEach((dock) => {
  const list = dock.querySelector('.dock-nav__list');
  const items = [...dock.querySelectorAll('.dock-nav__item')];
  const links = items.map((item) => item.querySelector('.dock-nav__link'));

  // Tap: the tile hops and settles on a spring. The demo (data-dock-nav-demo) moves the
  // current-page dot instead of navigating; remove that attribute on a real site.
  links.forEach((link) => link.addEventListener('click', (e) => {
    const tile = link.querySelector('.dock-nav__tile');
    tile.classList.remove('is-bouncing');
    void tile.offsetWidth;
    tile.classList.add('is-bouncing');
    if (!dock.hasAttribute('data-dock-nav-demo') || link.protocol === 'tel:') return;
    e.preventDefault();
    links.forEach((other) => (other === link ? other.setAttribute('aria-current', 'page') : other.removeAttribute('aria-current')));
  }));
  dock.addEventListener('animationend', (e) => {
    if (e.animationName === 'dock-nav-hop') e.target.classList.remove('is-bouncing');
  });

  if (reduce.matches) return; // no magnification; CSS shows labels on hover and focus
  dock.classList.add('dock-nav--magnify');

  // Resting geometry: tile centres relative to the dock's centre (the dock grows evenly
  // on both sides, so that centre never moves), measured with magnification off
  let offsets = [];
  let centre = 0;
  let sigma = 1;
  let amp = 0;
  let pointerX = null;
  let frame = 0;
  let touch = null;
  const measure = () => {
    dock.classList.add('dock-nav--measure');
    const box = list.getBoundingClientRect();
    centre = box.left + box.width / 2;
    offsets = links.map((link) => {
      const r = link.getBoundingClientRect();
      return r.left + r.width / 2 - centre;
    });
    sigma = Math.max(1, (offsets[1] - offsets[0]) * 0.75); // neighbours land near 1.25x
    // Spend only the spare width: the Gaussian adds about 1.9 tiles of width at full strength
    const tile = links[0].firstElementChild.offsetWidth;
    amp = Math.min(0.6, Math.max(0, (document.documentElement.clientWidth - 12 - box.width) / (tile * 1.9)));
    dock.style.setProperty('--dock-nav-amp', amp.toFixed(3));
    dock.classList.remove('dock-nav--measure');
  };

  // One write per frame: scale by distance with a Gaussian falloff; label the nearest tile
  const paint = () => {
    frame = 0;
    let near = -1;
    let best = Infinity;
    offsets.forEach((offset, i) => {
      const d = pointerX === null ? Infinity : Math.abs(pointerX - centre - offset);
      if (d < best) { best = d; near = i; }
      const s = 1 + amp * Math.exp(-(d * d) / (2 * sigma * sigma));
      items[i].style.setProperty('--dock-nav-s', pointerX === null ? '' : s.toFixed(3));
    });
    items.forEach((item, i) => item.classList.toggle('is-near', i === near));
  };
  const track = (x) => {
    pointerX = x;
    frame ||= requestAnimationFrame(paint);
  };

  // Mouse: hover. Touch and pen: a sideways drag (vertical swipes still scroll, via pan-y).
  list.addEventListener('pointermove', (e) => {
    if (e.pointerType === 'mouse') track(e.clientX);
    else if (touch && (touch.drag ||= Math.abs(e.clientX - touch.x) > 8)) track(e.clientX);
  }, { passive: true });
  list.addEventListener('pointerdown', (e) => {
    if (e.pointerType !== 'mouse') touch = { x: e.clientX, drag: false };
  }, { passive: true });
  const release = () => { touch = null; track(null); };
  list.addEventListener('pointerleave', (e) => { if (e.pointerType === 'mouse') track(null); });
  list.addEventListener('pointerup', (e) => { if (e.pointerType !== 'mouse') release(); });
  list.addEventListener('pointercancel', release);
  addEventListener('resize', () => { if (pointerX === null) measure(); }, { passive: true });
  measure();
});
```

## Notes

- **Accessibility:** a labelled `<nav>` with real links in a `role="list"`; the current page has `aria-current="page"`. Each label is the link's own text, so it is always the accessible name. It's only tucked away visually until hover or focus; it isn't a hidden state. Tile art is `aria-hidden`. Keyboard focus magnifies the tile and its neighbours, shows the label and draws a `--primary` outline round the tile. Hit areas are at least 46×48px.
- **Touch:** a sideways drag magnifies under the finger and labels the nearest tile. Because the list uses `touch-action: pan-y`, vertical swipes that start on the dock still scroll the page, and a plain tap opens the link. Magnification only spends spare width: full strength at 390px, a gentle swell at 320px, so the dock never overflows.
- **No JS:** a static, working dock. Mouse hover and keyboard focus still magnify in steps through CSS (`:has()`, Firefox 121+). Without `@property`, size changes step instead of easing. Without `backdrop-filter`, the pill is near-opaque white.
- **Reduced motion:** magnification and the hop are switched off. Labels still appear on hover and focus.
- **Contrast:** label text is `--text-inverse` on 90% `--surface-deep` (over 15:1). Tile icons clear 3:1: white on the brand gradient is 3.7–5.2:1, white on `--success` is 5:1 (3.2:1 at its lightened top), and `--text-main` on `--accent` is 6.8:1.
- **Wiring:** make the nav the last child of the page wrapper. It's `position: sticky`, so it reserves its own space; switch to `position: fixed` plus bottom padding if you prefer. Add `viewport-fit=cover` to the viewport meta so the safe-area inset applies. Set `aria-current` server-side and drop `data-dock-nav-demo`. Retheme tiles through `--dock-nav-fill` and `--dock-nav-ink`.
