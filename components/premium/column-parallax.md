# Column Parallax Gallery

A tall masonry of project photos on a light surface, laid out in three columns that travel at different speeds as you scroll: the outer two rise quickly while the middle one sinks slowly, so the wall of photos shears into layers. A frosted glass panel ("Built in Springfield since 1998", copy, a quote button and the rating) holds still in the middle of the section on desktop while photos slide behind it. Each photo is a link that slowly zooms and lifts a caption on hover or focus. On phones the panel sits above a two-column grid with gentler offsets. Depends on `tokens/variables.css`.

**Motion:** column `translate` scrubbed from section progress (linear, rAF) · slow image zoom on hover/focus (`--dur-5` × 1.6, `--ease-out`) · caption rise (`--dur-4`, `--ease-spring`) · CTA arrow nudge and press (`--ease-spring`) · intro hint bobs three times.

## HTML

```html
<div class="col-parallax-demo">
  <p class="col-parallax-demo__copy">Twenty-six years of local projects.</p>
  <p class="col-parallax-demo__hint">Scroll
    <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
  </p>
</div>

<section class="col-parallax" aria-labelledby="col-parallax-title" data-col-parallax data-speed="1.15 -0.4 1.35">
  <div class="col-parallax__inner">
    <div class="col-parallax__overlay">
      <div class="col-parallax__panel">
        <p class="col-parallax__eyebrow">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z" /><circle cx="12" cy="10" r="2.5" /></svg>
          Westlake · Northside · Riverside
        </p>
        <h2 id="col-parallax-title" class="col-parallax__title">Built in Springfield since 1998</h2>
        <p class="col-parallax__copy">Kitchens, roofs, rewires and rooftop solar: 3,400 projects so far, every one finished by our own crews and backed by a five-year workmanship guarantee.</p>
        <a class="col-parallax__cta" href="#quote">
          Get a free quote
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <div class="col-parallax__rating">
          <span class="col-parallax__stars" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
            <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
            <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
            <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
            <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          </span>
          <p><strong>4.9</strong>/5 · 1,200+ Google reviews</p>
        </div>
      </div>
    </div>

    <ul class="col-parallax__grid" role="list">
      <li class="col-parallax__item" style="--col-parallax-rows: 40">
        <a class="col-parallax__card" href="#project-kitchen">
          <img src="kitchen-westlake.jpg" width="640" height="800" alt="Kitchen remodel, Westlake, 2024: white oak cabinets, a quartz island and brass pendants" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Kitchen remodel</strong><small>Westlake · 2024</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 32">
        <a class="col-parallax__card" href="#project-solar">
          <img src="solar-riverside.jpg" width="640" height="640" alt="Rooftop solar, Riverside, 2023: 8.4 kW of black panels across a south-facing roof" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Rooftop solar, 8.4 kW</strong><small>Riverside · 2023</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 34">
        <a class="col-parallax__card" href="#project-bathroom">
          <img src="bathroom-northside.jpg" width="640" height="720" alt="Bathroom refit, Northside, 2024: walk-in shower with green zellige tiles and a brass rain head" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Bathroom refit</strong><small>Northside · 2024</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 30">
        <a class="col-parallax__card" href="#project-heat-pump">
          <img src="heat-pump-westlake.jpg" width="640" height="600" alt="Heat pump install, Westlake, 2022: outdoor unit on a concrete pad beside a cedar fence" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Heat pump install</strong><small>Westlake · 2022</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 36">
        <a class="col-parallax__card" href="#project-roof">
          <img src="roof-riverside.jpg" width="640" height="760" alt="Roof replacement, Riverside, 2023: crew fitting charcoal shingles on a steep gable" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Roof replacement</strong><small>Riverside · 2023</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 38">
        <a class="col-parallax__card" href="#project-panel">
          <img src="panel-northside.jpg" width="640" height="800" alt="Panel upgrade, Northside, 2024: a neatly labelled 200-amp electrical panel" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Panel upgrade, 200 A</strong><small>Northside · 2024</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 32">
        <a class="col-parallax__card" href="#project-deck">
          <img src="deck-westlake.jpg" width="640" height="640" alt="Deck lighting, Westlake, 2021: timber deck at dusk with warm step lights" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Deck lighting</strong><small>Westlake · 2021</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 40">
        <a class="col-parallax__card" href="#project-water-heater">
          <img src="water-heater-northside.jpg" width="640" height="840" alt="Tankless water heater, Northside, 2023: wall-mounted unit with new copper pipework" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Tankless water heater</strong><small>Northside · 2023</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 30">
        <a class="col-parallax__card" href="#project-attic">
          <img src="attic-riverside.jpg" width="640" height="600" alt="Attic insulation, Riverside, 2022: fresh blown-in insulation between the joists" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Attic insulation</strong><small>Riverside · 2022</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 36">
        <a class="col-parallax__card" href="#project-ev-charger">
          <img src="ev-charger-westlake.jpg" width="640" height="760" alt="EV charger install, Westlake, 2024: wall-mounted charger in a tidy garage" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>EV charger install</strong><small>Westlake · 2024</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 30">
        <a class="col-parallax__card" href="#project-laundry">
          <img src="laundry-northside.jpg" width="640" height="600" alt="Laundry room plumbing, Northside, 2023: new utility sink beside stacked machines" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Laundry room plumbing</strong><small>Northside · 2023</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
      <li class="col-parallax__item" style="--col-parallax-rows: 34">
        <a class="col-parallax__card" href="#project-gutters">
          <img src="gutters-riverside.jpg" width="640" height="720" alt="Gutters and downpipes, Riverside, 2022: seamless dark gutters on a white clapboard house" loading="lazy" decoding="async">
          <span class="col-parallax__caption" aria-hidden="true"><span><strong>Gutters and downpipes</strong><small>Riverside · 2022</small></span><span class="col-parallax__go"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span></span>
        </a>
      </li>
    </ul>
  </div>
</section>

<div class="col-parallax-demo">
  <p class="col-parallax-demo__copy">That's a small slice of 3,400.</p>
  <p class="col-parallax-demo__hint">Scroll back up to watch the columns part</p>
</div>
```

## CSS

```css
/* Demo scroll room above and below */
.col-parallax-demo {
  display: grid; place-content: center; justify-items: center; gap: 0.875rem; min-height: 70vh; padding: 3rem var(--gutter);
  background: var(--surface-muted); color: var(--text-muted); font-family: var(--font-sans); text-align: center;
}
.col-parallax-demo__copy { margin: 0; color: var(--text-main); font: 600 clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.col-parallax-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.col-parallax-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: col-parallax-bob 1.4s var(--ease-in-out) 600ms 3; }

/* Section: column speeds (overridden by data-speed), travel range and masonry row unit */
.col-parallax {
  --col-parallax-s1: 1.15; --col-parallax-s2: -0.4; --col-parallax-s3: 1.35;
  --col-parallax-range: 8rem;
  --col-parallax-row: clamp(0.3rem, 0.15rem + 0.55vw, 0.6rem);
  position: relative; isolation: isolate; overflow: clip;
  background: var(--surface-muted); color: var(--text-main); font-family: var(--font-sans);
}
.col-parallax::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background:
    radial-gradient(40% 30% at 50% 22%, color-mix(in srgb, var(--primary) 9%, transparent), transparent 70%),
    radial-gradient(40% 30% at 50% 78%, color-mix(in srgb, var(--primary-2) 9%, transparent), transparent 70%);
}
.col-parallax__inner { display: grid; gap: 2rem; max-width: var(--container-max); margin-inline: auto; padding: clamp(3.5rem, 8vw, 6rem) var(--gutter); }

/* Panel: a card above the grid on small screens, sticky frosted glass over it on desktop */
.col-parallax__overlay { display: grid; justify-items: center; }
.col-parallax__panel {
  display: grid; justify-items: start; gap: 1rem; width: min(100%, 27rem); padding: clamp(1.5rem, 4vw, 2rem);
  border-radius: var(--radius-2xl); background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.col-parallax__eyebrow { display: flex; align-items: center; gap: 0.5rem; margin: 0; color: var(--primary-hover); font: 500 0.75rem var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.col-parallax__eyebrow svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.col-parallax__title { margin: 0; font: 600 clamp(1.875rem, 1.4rem + 1.8vw, 2.5rem)/1.04 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.col-parallax__copy { margin: 0; color: color-mix(in srgb, var(--text-main) 82%, var(--surface-light)); line-height: 1.6; }
.col-parallax__cta {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; margin-top: 0.25rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), var(--shadow-glow);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.col-parallax__cta:hover { transform: translateY(-1px); box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 14px 44px -12px color-mix(in srgb, var(--primary) 70%, transparent); }
.col-parallax__cta:active { transform: scale(0.97); }
.col-parallax__cta svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.col-parallax__cta:hover svg { transform: translateX(3px); }
.col-parallax__rating { display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem 0.75rem; width: 100%; padding-top: 1rem; border-top: 1px solid var(--border-subtle); font-size: 0.875rem; }
.col-parallax__rating p { margin: 0; color: color-mix(in srgb, var(--text-main) 82%, var(--surface-light)); }
.col-parallax__rating strong { color: var(--text-main); font: 600 1rem var(--font-display); }
.col-parallax__stars { display: inline-flex; gap: 0.125rem; }
.col-parallax__stars svg { fill: var(--accent); stroke: color-mix(in srgb, var(--accent) 70%, var(--warning)); stroke-width: 1; stroke-linejoin: round; }
.col-parallax__cta:focus-visible, .col-parallax__card:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Masonry: row spans + dense packing keep each column's stack independent at 2 or 3 columns */
.col-parallax__grid {
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); grid-auto-rows: var(--col-parallax-row); grid-auto-flow: dense; column-gap: 0.75rem;
  margin: 0; padding: 2.5rem 0; list-style: none;
  -webkit-mask-image: linear-gradient(transparent, black 3rem, black calc(100% - 3rem), transparent);
  mask-image: linear-gradient(transparent, black 3rem, black calc(100% - 3rem), transparent);
}
.col-parallax__item {
  grid-row: span var(--col-parallax-rows, 32); padding-bottom: 0.75rem;
  translate: 0 calc((var(--col-parallax-p, 0.5) - 0.5) * var(--col-parallax-s, 0) * var(--col-parallax-range) * -1);
  will-change: translate;
}
.col-parallax__item:nth-child(odd) { grid-column: 1; --col-parallax-s: var(--col-parallax-s1); }
.col-parallax__item:nth-child(even) { grid-column: 2; --col-parallax-s: var(--col-parallax-s2); }

/* Photo card: hairline + sheen on top, slow zoom, caption rises on hover/focus */
.col-parallax__card {
  position: relative; isolation: isolate; display: block; height: 100%; overflow: hidden; border-radius: var(--radius-2xl);
  background: linear-gradient(160deg, color-mix(in srgb, var(--primary) 28%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 34%, var(--surface-light)));
  color: var(--text-main); text-decoration: none; box-shadow: var(--shadow-lg);
  transition: box-shadow var(--dur-3) var(--ease-out);
}
.col-parallax__item:nth-child(3n+2) .col-parallax__card { background: linear-gradient(200deg, color-mix(in srgb, var(--accent) 30%, var(--surface-light)), color-mix(in srgb, var(--primary) 24%, var(--surface-light))); }
.col-parallax__card::after { content: ""; position: absolute; inset: 0; z-index: 2; border-radius: inherit; pointer-events: none; box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-main) 8%, transparent), var(--highlight); }
.col-parallax__card:hover { box-shadow: var(--shadow-xl); }
.col-parallax__card img { display: block; width: 100%; height: 100%; object-fit: cover; transition: scale calc(var(--dur-5) * 1.6) var(--ease-out); }
.col-parallax__card:is(:hover, :focus-visible) img { scale: 1.07; }
.col-parallax__caption {
  position: absolute; inset: auto 0.5rem 0.5rem; z-index: 1; display: flex; align-items: center; justify-content: space-between; gap: 0.625rem;
  padding: 0.5rem 0.625rem; border-radius: var(--radius-xl);
  background: color-mix(in srgb, var(--surface-light) 88%, transparent); box-shadow: var(--highlight), var(--shadow-md);
  opacity: 0; translate: 0 calc(100% + 0.5rem);
  transition: translate var(--dur-4) var(--ease-spring), opacity var(--dur-3) var(--ease-out);
}
@supports (backdrop-filter: blur(1px)) { .col-parallax__caption { backdrop-filter: blur(var(--blur-md)) saturate(1.5); } }
.col-parallax__caption > span:first-child { display: grid; min-width: 0; }
.col-parallax__caption strong { font: 600 0.75rem/1.25 var(--font-display); letter-spacing: -0.01em; text-wrap: balance; }
.col-parallax__caption small { display: none; color: color-mix(in srgb, var(--text-main) 75%, var(--surface-light)); font: 500 0.6875rem/1.5 var(--font-mono); letter-spacing: 0.03em; }
.col-parallax__go { flex: none; display: none; place-items: center; width: 2rem; height: 2rem; border-radius: var(--radius-full); background: var(--text-main); color: var(--surface-light); transition: rotate var(--dur-4) var(--ease-spring); }
.col-parallax__go svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.col-parallax__card:is(:hover, :focus-visible) .col-parallax__caption { opacity: 1; translate: 0 0; }
.col-parallax__card:hover .col-parallax__go { rotate: 45deg; }
@media (hover: none) { .col-parallax__caption { opacity: 1; translate: 0 0; } }

@media (min-width: 768px) {
  .col-parallax { --col-parallax-range: 18rem; }
  .col-parallax__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); column-gap: 1rem; }
  .col-parallax__item { padding-bottom: 1rem; }
  .col-parallax__item:nth-child(3n+1) { grid-column: 1; --col-parallax-s: var(--col-parallax-s1); }
  .col-parallax__item:nth-child(3n+2) { grid-column: 2; --col-parallax-s: var(--col-parallax-s2); }
  .col-parallax__item:nth-child(3n) { grid-column: 3; --col-parallax-s: var(--col-parallax-s3); }
  .col-parallax__caption { inset: auto 0.625rem 0.625rem; padding: 0.5rem 0.5rem 0.5rem 0.875rem; }
  .col-parallax__caption strong { font-size: 0.875rem; }
  .col-parallax__caption small { display: block; }
  .col-parallax__go { display: grid; }
}

/* Desktop: the panel and the grid share one cell; the panel sticks at mid-viewport */
@media (min-width: 1024px) {
  .col-parallax__overlay, .col-parallax__grid { grid-area: 1 / 1; }
  /* A block (not grid) overlay, so the sticky panel's containing block spans the whole gallery height */
  .col-parallax__overlay { z-index: 1; display: block; padding-block: 15rem; pointer-events: none; }
  .col-parallax__panel {
    position: sticky; top: 50%; translate: 0 -50%; width: 26rem; margin-inline: auto; pointer-events: auto;
    background: color-mix(in srgb, var(--surface-light) 86%, transparent);
    box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 70%, transparent), var(--highlight), 0 40px 80px -30px color-mix(in srgb, var(--text-main) 45%, transparent), var(--shadow-xl);
  }
  @supports (backdrop-filter: blur(1px)) {
    .col-parallax__panel { backdrop-filter: blur(var(--blur-md)) saturate(1.7); }
  }
}

@media (prefers-reduced-motion: reduce) {
  .col-parallax__item { translate: none; }
  .col-parallax-demo *, .col-parallax-demo *::before, .col-parallax-demo *::after { animation: none !important; }
}
@keyframes col-parallax-bob { 50% { transform: translateY(4px); } }
```

## JS

```js
// The section isn't pinned, so progress runs across its whole pass through the viewport:
// 0 as the gallery's top edge enters at the bottom, 1 as its bottom edge leaves at the top
const progress = (el) => {
  const r = el.getBoundingClientRect();
  return Math.min(1, Math.max(0, (innerHeight - r.top) / (innerHeight + r.height)));
};

document.querySelectorAll('[data-col-parallax]').forEach((root) => {
  const grid = root.querySelector('.col-parallax__grid');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let near = false, frame = 0;

  // data-speed="left middle right": positive rises as you scroll down, negative sinks
  (root.dataset.speed || '').trim().split(/\s+/).forEach((speed, i) => {
    if (speed && Number.isFinite(Number(speed))) root.style.setProperty(`--col-parallax-s${i + 1}`, speed);
  });

  // One write per frame; CSS turns it into a translate per column
  const update = () => {
    frame = 0;
    if (reduce.matches) grid.style.removeProperty('--col-parallax-p');
    else grid.style.setProperty('--col-parallax-p', progress(grid).toFixed(4));
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(update); };

  new IntersectionObserver(([entry]) => { near = entry.isIntersecting; queue(); }, { rootMargin: '15% 0px' }).observe(root);
  addEventListener('scroll', queue, { passive: true });
  new ResizeObserver(queue).observe(grid);
  reduce.addEventListener('change', update);
  update();
});
```

## Notes

- The gallery is a `<ul role="list">` of links. Each link's name is its photo's `alt`, which leads with the project and area ("Kitchen remodel, Westlake, 2024: …"), so the hover caption is a visual duplicate (`aria-hidden`). Captions rise on hover and keyboard focus and stay visible on touch screens (`hover: none`). The panel comes first in the DOM: heading, copy and CTA are read and tabbed to before the photos.
- Progress uses the shared rAF + IntersectionObserver recipe, measured over the section's whole pass through the viewport because nothing is pinned. Rising columns start low and the sinking column starts high, so whichever edge of the gallery is on screen, its photos stay inside the padded, faded margin instead of being clipped.
- Without JS, or with `prefers-reduced-motion`, the columns don't move: you get a static masonry with the same sticky panel (pure CSS). The hover zoom and caption timings use `--dur-*`, so they collapse under reduced motion too.
- Contrast: panel text sits on ≥ 86% white glass, so even over a black photo the copy (`--text-main` 82% mix) is ≥ 5.9:1, the eyebrow (`--primary-hover`) ≥ 4.8:1 and the title ≥ 10:1. Captions sit on 88% white: title ≥ 10:1, mono meta ≥ 4.9:1. Stars are decorative; the rating is in the text.
- Adapting: `data-speed` sets the column speeds, `--col-parallax-range` sets the travel (8rem on phones, 18rem from 768px), and `--col-parallax-rows` on each item sets its height in `--col-parallax-row` units. Items alternate columns in DOM order (1-2-3 from 768px, 1-2 below), so keep the spans roughly balanced for both counts.
- Support: masonry is plain grid (`grid-auto-flow: dense` with row spans), not `masonry` rows. Panel and captions fall back to near-opaque white without `backdrop-filter`; the standalone `translate`/`scale` properties need Safari 14.1+.
