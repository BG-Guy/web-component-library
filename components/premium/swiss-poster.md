# Swiss Editorial Section

An International Typographic Style "about / our numbers" section laid out like a printed poster: paper grain, crop marks, a strict column grid with visible hairlines, mono metadata, rotated vertical captions and a giant "25" in Geist 800 that is cropped by a rule. On entry the hairlines draw in column by column, the numeral rises out of its crop line and a red square and circle slide in along grid lines with stagger; hovering or focusing the numbered key slides a single red index marker. Phones get a 4-column version of the same grid, with the square and circle re-pinned to its lines. Depends on `tokens/variables.css`.

**Motion:** hairline draw-in (`--dur-5`, `--ease-out`, `--stagger` per column) · rules wipe in · numeral rises out of its crop · square and circle slide along grid lines · copy fades up in sequence · index marker glide (`--dur-4`, `--ease-spring`) · label nudge on hover (`--dur-3`).

## HTML

```html
<section class="swiss-grid" aria-labelledby="swiss-grid-title" data-swiss-grid>
  <div class="swiss-grid__inner">
    <div class="swiss-grid__poster">
      <div class="swiss-grid__lines" aria-hidden="true">
        <span class="swiss-grid__line" style="--swiss-grid-i: 0"></span><span class="swiss-grid__line" style="--swiss-grid-i: 1"></span><span class="swiss-grid__line" style="--swiss-grid-i: 2"></span><span class="swiss-grid__line" style="--swiss-grid-i: 3"></span><span class="swiss-grid__line" style="--swiss-grid-i: 4"></span><span class="swiss-grid__line" style="--swiss-grid-i: 5"></span><span class="swiss-grid__line" style="--swiss-grid-i: 6"></span><span class="swiss-grid__line" style="--swiss-grid-i: 7"></span><span class="swiss-grid__line" style="--swiss-grid-i: 8"></span><span class="swiss-grid__line" style="--swiss-grid-i: 9"></span><span class="swiss-grid__line" style="--swiss-grid-i: 10"></span><span class="swiss-grid__line" style="--swiss-grid-i: 11"></span><span class="swiss-grid__line" style="--swiss-grid-i: 12"></span>
      </div>

      <ul class="swiss-grid__meta swiss-grid__reveal" role="list" style="--swiss-grid-i: 2">
        <li>Est. 2001 — Springfield</li>
        <li>About / Our numbers</li>
        <li>Plumbing · Heating · Electrical</li>
        <li>Nº 02</li>
      </ul>
      <span class="swiss-grid__rule swiss-grid__rule--a" aria-hidden="true" style="--swiss-grid-i: 1"></span>

      <h2 id="swiss-grid-title" class="swiss-grid__title swiss-grid__reveal" style="--swiss-grid-i: 7">Twenty-five years of keeping Springfield's homes in working order.</h2>
      <p class="swiss-grid__figure" aria-hidden="true"><span class="swiss-grid__numeral" style="--swiss-grid-i: 4">25</span></p>
      <p class="swiss-grid__caption swiss-grid__caption--years swiss-grid__reveal" style="--swiss-grid-i: 8">Years in service</p>
      <span class="swiss-grid__square" aria-hidden="true" style="--swiss-grid-i: 9"></span>
      <span class="swiss-grid__rule swiss-grid__rule--b" aria-hidden="true" style="--swiss-grid-i: 3"></span>
      <span class="swiss-grid__circle" aria-hidden="true" style="--swiss-grid-i: 11"></span>

      <p class="swiss-grid__caption swiss-grid__caption--fig swiss-grid__reveal" style="--swiss-grid-i: 9">Fig. 2 — How we work</p>
      <div class="swiss-grid__body swiss-grid__reveal" style="--swiss-grid-i: 10">
        <p>Brand began in 2001 with one van, one toolbox and a simple rule: turn up when you said you would. The van is now a fleet. The rule hasn't changed.</p>
        <p>Every technician is licensed and trained in-house, every price is agreed before work starts, and every repair carries a two-year guarantee.</p>
      </div>

      <div class="swiss-grid__index swiss-grid__reveal" style="--swiss-grid-i: 11">
        <ol class="swiss-grid__key" role="list">
          <li><a class="swiss-grid__key-link" href="#reviews"><span class="swiss-grid__key-no">01</span><span class="swiss-grid__key-label">Homes serviced</span><span class="swiss-grid__key-value">18,400</span></a></li>
          <li><a class="swiss-grid__key-link" href="#team"><span class="swiss-grid__key-no">02</span><span class="swiss-grid__key-label">Licensed technicians</span><span class="swiss-grid__key-value">42</span></a></li>
          <li><a class="swiss-grid__key-link" href="#areas"><span class="swiss-grid__key-no">03</span><span class="swiss-grid__key-label">Average arrival</span><span class="swiss-grid__key-value">54 min</span></a></li>
          <li><a class="swiss-grid__key-link" href="#guarantee"><span class="swiss-grid__key-no">04</span><span class="swiss-grid__key-label">Customers who come back</span><span class="swiss-grid__key-value">71%</span></a></li>
        </ol>
        <span class="swiss-grid__marker" aria-hidden="true"></span>
      </div>
      <span class="swiss-grid__rule swiss-grid__rule--c" aria-hidden="true" style="--swiss-grid-i: 5"></span>

      <ul class="swiss-grid__foot swiss-grid__reveal" role="list" style="--swiss-grid-i: 12">
        <li><a href="tel:+15555550123">(555) 555-0123</a></li>
        <li><a href="mailto:hello@example.com">hello@example.com</a></li>
        <li>Westlake / Northside / Riverside</li>
        <li class="swiss-grid__foot-mark">Brand Home Services <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="5" /><path d="M12 2v20M2 12h20" /></svg></li>
      </ul>
    </div>
  </div>
</section>
```

## CSS

```css
/* Palette, paper grain and the 4 → 12 column grid */
.swiss-grid {
  --swiss-grid-paper: #f3f0e8;
  --swiss-grid-ink: #121212;
  --swiss-grid-red: #e5231b;
  --swiss-grid-hair: color-mix(in srgb, var(--swiss-grid-ink) 14%, transparent);
  --swiss-grid-rule-soft: color-mix(in srgb, var(--swiss-grid-ink) 30%, transparent);
  --swiss-grid-muted: color-mix(in srgb, var(--swiss-grid-ink) 70%, var(--swiss-grid-paper));
  --swiss-grid-cols: 4;
  --swiss-grid-pad: 0.625rem;   /* text inset from its column line */
  --swiss-grid-mark: 0.625rem;  /* crop-mark length */
  --swiss-grid-gap: 0.25rem;    /* crop-mark gap from the corner */
  position: relative; isolation: isolate; overflow: clip;
  background: var(--swiss-grid-paper); color: var(--swiss-grid-ink); font-family: var(--font-sans);
}
.swiss-grid::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none; opacity: 0.5; mix-blend-mode: multiply;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .22 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E");
}
.swiss-grid__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(3.5rem, 8vw, 6.5rem) var(--gutter); }
.swiss-grid__poster { position: relative; display: grid; grid-template-columns: repeat(var(--swiss-grid-cols), minmax(0, 1fr)); align-items: start; }

/* Crop marks just outside the poster's four corners */
.swiss-grid__poster::after {
  --swiss-grid-o: calc(var(--swiss-grid-mark) + var(--swiss-grid-gap));
  content: ""; position: absolute; inset: calc(var(--swiss-grid-o) * -1); pointer-events: none;
  background:
    linear-gradient(var(--swiss-grid-ink), var(--swiss-grid-ink)) left 0 top var(--swiss-grid-o) / var(--swiss-grid-mark) 1px,
    linear-gradient(var(--swiss-grid-ink), var(--swiss-grid-ink)) left var(--swiss-grid-o) top 0 / 1px var(--swiss-grid-mark),
    linear-gradient(var(--swiss-grid-ink), var(--swiss-grid-ink)) right 0 top var(--swiss-grid-o) / var(--swiss-grid-mark) 1px,
    linear-gradient(var(--swiss-grid-ink), var(--swiss-grid-ink)) right var(--swiss-grid-o) top 0 / 1px var(--swiss-grid-mark),
    linear-gradient(var(--swiss-grid-ink), var(--swiss-grid-ink)) left 0 bottom var(--swiss-grid-o) / var(--swiss-grid-mark) 1px,
    linear-gradient(var(--swiss-grid-ink), var(--swiss-grid-ink)) left var(--swiss-grid-o) bottom 0 / 1px var(--swiss-grid-mark),
    linear-gradient(var(--swiss-grid-ink), var(--swiss-grid-ink)) right 0 bottom var(--swiss-grid-o) / var(--swiss-grid-mark) 1px,
    linear-gradient(var(--swiss-grid-ink), var(--swiss-grid-ink)) right var(--swiss-grid-o) bottom 0 / 1px var(--swiss-grid-mark);
  background-repeat: no-repeat;
}

/* Column hairlines (5 on phones, 13 from 768px) and horizontal rules */
.swiss-grid__lines { position: absolute; inset: 0; pointer-events: none; }
.swiss-grid__line {
  position: absolute; inset-block: 0; left: calc(100% * var(--swiss-grid-i) / var(--swiss-grid-cols)); width: 1px;
  background: var(--swiss-grid-hair); transform-origin: top;
}
.swiss-grid__line:nth-child(n + 6) { display: none; }
.swiss-grid__rule { grid-column: 1 / -1; height: 1px; background: var(--swiss-grid-ink); transform-origin: left; }
.swiss-grid__rule--a { grid-row: 2; }
.swiss-grid__rule--b { grid-row: 4; }
.swiss-grid__rule--c { grid-row: 8; height: 2px; }

/* Mono metadata strips: equal fractions, so each cell starts on a column line */
.swiss-grid__meta, .swiss-grid__foot {
  grid-column: 1 / -1; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); row-gap: 0.5rem;
  margin: 0; padding: 0 0 0.875rem; list-style: none;
  font: 500 0.6875rem/1.35 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.swiss-grid__meta li, .swiss-grid__foot li { padding-inline: var(--swiss-grid-pad); }
.swiss-grid__meta { grid-row: 1; }
.swiss-grid__foot { grid-row: 9; align-items: center; padding: 0.875rem 0 0; }
.swiss-grid__foot a { display: inline-flex; align-items: center; min-height: 1.5rem; color: inherit; text-decoration-thickness: 1px; text-underline-offset: 3px; }
.swiss-grid__foot-mark { display: flex; align-items: center; gap: 0.5rem; }
.swiss-grid__foot-mark svg { flex: none; fill: none; stroke: currentColor; stroke-width: 1.25; }

/* The numeral: cap top pulled to the box edge, bottom cropped by rule B */
.swiss-grid__figure {
  grid-row: 3; grid-column: 1 / -1; align-self: end; height: 0.6em; margin: clamp(1.75rem, 5vw, 3.5rem) 0 0; overflow: clip;
  font: 800 min(64vw, 33rem)/1 var(--font-display); letter-spacing: -0.075em;
}
.swiss-grid__numeral { display: block; margin: -0.15em 0 0 -0.035em; }

/* Vertical captions read bottom-to-top, like a spine */
.swiss-grid__caption {
  margin: 0; padding: var(--swiss-grid-pad) 0; writing-mode: vertical-rl; rotate: 180deg; white-space: nowrap;
  font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.swiss-grid__caption--years { grid-row: 3; grid-column: 4; justify-self: end; align-self: end; margin-right: 0.25rem; }
.swiss-grid__caption--fig { grid-row: 6; grid-column: 1; justify-self: start; margin: 2rem 0 0 var(--swiss-grid-pad); }

/* Headline: flush left, ragged right */
.swiss-grid__title {
  grid-row: 5; grid-column: 1 / span 3; margin: 0; padding: 2.75rem var(--swiss-grid-pad) 0;
  font: 700 clamp(1.375rem, 1.1rem + 0.9vw, 1.75rem)/1.12 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: pretty;
}

/* Red accents pinned to grid lines; the circle overprints like a second ink */
.swiss-grid__square { grid-row: 5; grid-column: 4; aspect-ratio: 1; background: var(--swiss-grid-red); }
.swiss-grid__circle {
  position: absolute; grid-row: 4; grid-column: 3; top: 0; left: 0; width: 100%; aspect-ratio: 1;
  border-radius: 50%; background: var(--swiss-grid-red); translate: 0 -50%; mix-blend-mode: multiply;
}

/* Body copy */
.swiss-grid__body { grid-row: 6; grid-column: 2 / -1; max-width: 34rem; padding: 2rem var(--swiss-grid-pad) 0; }
.swiss-grid__body p { margin: 0 0 1rem; font-size: 1rem; line-height: 1.55; text-wrap: pretty; }
.swiss-grid__body p:first-child { font-size: 1.125rem; font-weight: 500; line-height: 1.45; }

/* Numbered key with one sliding red index marker */
.swiss-grid__index { position: relative; grid-row: 7; grid-column: 1 / -1; padding: 1.5rem 0 2.5rem; }
.swiss-grid__key { margin: 0; padding: 0; list-style: none; border-top: 1px solid var(--swiss-grid-ink); }
.swiss-grid__key-link {
  position: relative; display: grid; grid-template-columns: 2rem minmax(0, 1fr) auto; align-items: baseline; column-gap: 0.75rem;
  padding: 0.9375rem var(--swiss-grid-pad) 0.9375rem 1.25rem; border-bottom: 1px solid var(--swiss-grid-rule-soft);
  color: inherit; text-decoration: none;
}
.swiss-grid__key-no { color: var(--swiss-grid-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.06em; }
.swiss-grid__key-label { font-weight: 600; line-height: 1.3; transition: translate var(--dur-3) var(--ease-spring); }
.swiss-grid__key-value {
  font: 800 clamp(1.5rem, 1.2rem + 1.1vw, 2.25rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums;
}
.swiss-grid__key-link:is(:hover, :focus-visible) .swiss-grid__key-label { translate: 0.5rem 0; }
/* Without JS each item shows its own marker */
.swiss-grid__key-link::before {
  content: ""; position: absolute; inset: 0 auto 0 0; width: 0.375rem; background: var(--swiss-grid-red);
  transform: scaleY(0); transform-origin: top; transition: transform var(--dur-3) var(--ease-out);
}
.swiss-grid__key-link:is(:hover, :focus-visible)::before { transform: scaleY(1); }
.swiss-grid--js .swiss-grid__key-link::before { content: none; }
.swiss-grid__marker {
  display: none; position: absolute; top: 0; left: 0; width: 0.375rem; height: 1px; background: var(--swiss-grid-red);
  transform-origin: top; transform: translateY(var(--swiss-grid-y, 0px)) scaleY(var(--swiss-grid-h, 0));
  transition: transform var(--dur-4) var(--ease-spring);
}
.swiss-grid--js .swiss-grid__marker { display: block; }
.swiss-grid a:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Entrance: held back only when scripting is on and motion is allowed */
.swiss-grid__line, .swiss-grid__rule, .swiss-grid__numeral, .swiss-grid__square, .swiss-grid__circle, .swiss-grid__reveal {
  transition: transform var(--dur-5) var(--ease-out), opacity var(--dur-4) var(--ease-out);
  transition-delay: calc(var(--swiss-grid-i, 0) * var(--stagger));
}
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .swiss-grid:not(.is-in) .swiss-grid__line { transform: scaleY(0); }
  .swiss-grid:not(.is-in) .swiss-grid__rule { transform: scaleX(0); }
  .swiss-grid:not(.is-in) .swiss-grid__numeral { transform: translateY(105%); }
  .swiss-grid:not(.is-in) .swiss-grid__square { transform: translateY(-40%); opacity: 0; }
  .swiss-grid:not(.is-in) .swiss-grid__circle { transform: translateX(-300%); opacity: 0; }
  .swiss-grid:not(.is-in) .swiss-grid__reveal { transform: translateY(0.75rem); opacity: 0; }
  /* Failsafe: if the script never runs, show everything after 3s */
  .swiss-grid:not(.swiss-grid--js) :is(.swiss-grid__line, .swiss-grid__rule, .swiss-grid__numeral, .swiss-grid__square, .swiss-grid__circle, .swiss-grid__reveal) {
    animation: swiss-grid-failsafe 1ms 3s forwards;
  }
}

@media (min-width: 768px) {
  .swiss-grid { --swiss-grid-cols: 12; --swiss-grid-pad: 0.75rem; --swiss-grid-mark: 1rem; --swiss-grid-gap: 0.5rem; }
  .swiss-grid__line:nth-child(n + 6) { display: block; }
  .swiss-grid__meta, .swiss-grid__foot { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .swiss-grid__figure { grid-column: 1 / span 7; font-size: min(42vw, 33rem); }
  .swiss-grid__caption--years { grid-column: 8; justify-self: start; margin: 0 0 0 var(--swiss-grid-pad); }
  .swiss-grid__title { grid-row: 3; grid-column: 9 / -1; align-self: end; padding: 0 var(--swiss-grid-pad) 0.875rem; }
  .swiss-grid__square { grid-row: 3; grid-column: 12; }
  .swiss-grid__circle { grid-column: 7; }
  .swiss-grid__caption--fig { grid-row: 5; margin-top: 2.5rem; }
  .swiss-grid__body { grid-row: 5; grid-column: 2 / span 5; padding-top: 2.5rem; }
  .swiss-grid__index { grid-row: 5; grid-column: 8 / -1; padding: 2.5rem 0 3rem; }
  .swiss-grid__rule--c { grid-row: 6; }
  .swiss-grid__foot { grid-row: 7; }
  .swiss-grid__foot-mark { justify-content: flex-end; }
}
@media (prefers-reduced-motion: reduce) {
  .swiss-grid *, .swiss-grid *::before, .swiss-grid *::after { animation: none !important; }
}
@keyframes swiss-grid-failsafe { to { transform: none; opacity: 1; } }
```

## JS

```js
document.querySelectorAll('[data-swiss-grid]').forEach((root) => {
  const index = root.querySelector('.swiss-grid__index');
  const marker = root.querySelector('.swiss-grid__marker');
  let current = index.querySelector('.swiss-grid__key > li');

  // Entrance: CSS holds the pieces back (scripting on, motion allowed); reveal once the poster is in view.
  // Already visible at load? Reveal in this same task so nothing flashes.
  root.classList.add('swiss-grid--js');
  const box = root.getBoundingClientRect();
  if (box.top < innerHeight && box.bottom > 0) root.classList.add('is-in');
  else {
    const io = new IntersectionObserver(([entry]) => {
      if (!entry.isIntersecting) return;
      root.classList.add('is-in');
      io.disconnect();
    }, { rootMargin: '0px 0px -20% 0px' });
    io.observe(root);
  }

  // Index marker: one red bar that springs to the hovered or focused key item
  const moveTo = (item, instant) => {
    if (!item) return;
    current = item;
    if (instant) marker.style.transition = 'none';
    marker.style.setProperty('--swiss-grid-y', `${item.offsetTop}px`);
    marker.style.setProperty('--swiss-grid-h', String(item.offsetHeight));
    if (instant) { void marker.offsetWidth; marker.style.transition = ''; }
  };
  index.addEventListener('pointerover', (e) => moveTo(e.target.closest('.swiss-grid__key > li')));
  index.addEventListener('focusin', (e) => moveTo(e.target.closest('.swiss-grid__key > li')));
  new ResizeObserver(() => moveTo(current, true)).observe(index);
});
```

## Notes

- One CSS grid drives both the drawn hairlines and the content (`--swiss-grid-cols`: 4 on phones, 12 from 768px), so every text block, the square and the circle sit on real column lines. The giant numeral is decorative (`aria-hidden`); the `<h2>` says "Twenty-five years" in words, and the vertical captions are real text, read in source order.
- Entrance: pieces are held back only under `@media (scripting: enabled) and (prefers-reduced-motion: no-preference)`. JS reveals them when the section enters view (in the same task if it's already visible, so nothing flashes), and a 3s CSS failsafe reveals everything if the script never runs. With no JS, reduced motion or a browser without the `scripting` query, the poster is static and complete.
- The key is a list of real links (`<ol role="list">`). Hover or focus springs one red marker to the item using transforms only, re-measured on resize; without JS each item shows its own marker instead.
- Contrast: ink on paper 16.5:1; metadata and key numbers (70% ink) 6.6:1. Swiss red (4.0:1 on paper) is only used for shapes, never for text. The circle uses `mix-blend-mode: multiply` to overprint the numeral like a second ink.
- Copy reads "EST. 2001" so that "25 years" holds in 2026; change both together. The crop is tuned for Geist (cap top at `-0.15em`, crop at `0.6em` of the numeral size); other typefaces may need those two values nudged.
