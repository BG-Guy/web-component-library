# Infinite Pan Canvas

A dark, explorable gallery of twenty project photos in a staggered masonry of mixed ratios that wraps forever in every direction: drag it with momentum, scroll or swipe on a trackpad, or step tile to tile with the arrow keys. Tiles grow and brighten as they near the centre over a parallax dot field, and choosing one glides it into place and opens a glass caption card. A "View as grid" toggle, which is also the no-JS layout, shows a plain grid with every caption. On phones the canvas is shorter, so the page still scrolls around it. Depends on `tokens/variables.css`.

**Motion:** drag pan with exponential inertia (rAF, transforms only) · centre scale and brightness falloff · dot field parallax at half speed · glide-to-centre on focus or choice (`--dur-4`, ease-out cubic) · caption spring-in (`--dur-4`, `--ease-spring`) · hint fade (`--dur-5`, `--ease-out`).

## HTML

```html
<section class="pan-canvas" aria-labelledby="pan-canvas-title" data-pan-canvas>
  <header class="pan-canvas__head">
    <div>
      <p class="pan-canvas__eyebrow">Recent work · 2025–26</p>
      <h2 id="pan-canvas-title" class="pan-canvas__title">Twenty homes. Wander through them.</h2>
    </div>
    <button class="pan-canvas__toggle" type="button" aria-pressed="false" hidden>
      <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z" /></svg>
      View as grid
    </button>
  </header>

  <div class="pan-canvas__viewport" role="region" aria-label="Projects">
    <p id="pan-canvas-help" class="pan-canvas__sr" hidden>Project canvas. Drag, scroll, or use the arrow keys on a project to move between neighbours; the canvas wraps in every direction. Each project is a button that opens its details. Choose View as grid for a plain list.</p>
    <span class="pan-canvas__dots" aria-hidden="true"></span>

    <ul class="pan-canvas__list" role="list">
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="walnut-kitchen.jpg" width="600" height="600" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Walnut kitchen</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Westlake · 2026</p><p class="pan-canvas__desc">Walnut cabinets, a quartz island and underfloor heating, fitted in nine working days.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="spa-bathroom.jpg" width="640" height="480" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Spa bathroom</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Northside · 2026</p><p class="pan-canvas__desc">A walk-in shower, heated towel rails and a hidden linear drain.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="slate-roof.jpg" width="560" height="700" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Slate roof</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Riverside · 2025</p><p class="pan-canvas__desc">Re-roofed in reclaimed slate with new lead flashing and copper gutters.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="boiler-room.jpg" width="600" height="600" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Boiler swap</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Springfield · 2026</p><p class="pan-canvas__desc">A combi boiler with a magnetic filter and a smart thermostat, swapped in a day.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="garden-room.jpg" width="640" height="480" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Garden office</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Westlake · 2025</p><p class="pan-canvas__desc">An insulated garden office with power, data and its own heat pump.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="laundry-nook.jpg" width="640" height="480" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Laundry nook</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Riverside · 2026</p><p class="pan-canvas__desc">A stacked washer-dryer, a utility sink and new waste plumbing under the stairs.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="loft-conversion.jpg" width="560" height="700" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Loft conversion</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Northside · 2025</p><p class="pan-canvas__desc">A dormer loft with an en-suite, roof windows and fresh insulation.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="panel-upgrade.jpg" width="600" height="600" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Panel upgrade</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Springfield · 2026</p><p class="pan-canvas__desc">A 200-amp panel with surge protection and a dedicated EV charger circuit.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="heat-pump.jpg" width="600" height="600" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Heat pump</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Westlake · 2026</p><p class="pan-canvas__desc">An air-source heat pump replacing a twenty-year-old oil furnace.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="basement-tanking.jpg" width="600" height="600" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Dry basement</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Riverside · 2025</p><p class="pan-canvas__desc">Membrane tanking, a sump pump and a warm, dry finished floor.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="oak-staircase.jpg" width="560" height="700" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Oak staircase</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Northside · 2026</p><p class="pan-canvas__desc">Solid oak treads and a glass balustrade, finished on site.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="porch-rebuild.jpg" width="600" height="600" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Porch rebuild</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Springfield · 2025</p><p class="pan-canvas__desc">A new porch roof, timber posts and an LED canopy light.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="gutter-run.jpg" width="640" height="480" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Seamless gutters</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Westlake · 2026</p><p class="pan-canvas__desc">Seamless aluminium gutters with leaf guards on all four sides.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="wet-room.jpg" width="560" height="700" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Wet room</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Riverside · 2026</p><p class="pan-canvas__desc">A level-access wet room with a fold-down seat and grab rails.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="solar-array.jpg" width="600" height="600" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Solar array</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Northside · 2025</p><p class="pan-canvas__desc">A twelve-panel array with a home battery and a new consumer unit.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="utility-rewire.jpg" width="600" height="600" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Full rewire</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Springfield · 2026</p><p class="pan-canvas__desc">A complete rewire of a 1960s house, with new lighting throughout.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="pantry-kitchen.jpg" width="600" height="600" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Butler's pantry</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Westlake · 2025</p><p class="pan-canvas__desc">A walk-in pantry with a second sink and a boiling-water tap.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="radiator-swap.jpg" width="600" height="600" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Column radiators</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Riverside · 2026</p><p class="pan-canvas__desc">Twelve column radiators with thermostatic valves in every room.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="deck-lighting.jpg" width="640" height="480" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Deck lighting</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Northside · 2026</p><p class="pan-canvas__desc">Low-voltage deck and step lights on a smart timer.</p></div></li>
      <li class="pan-canvas__item"><button class="pan-canvas__tile" type="button" aria-haspopup="dialog"><img src="chimney-repair.jpg" width="560" height="700" alt="" loading="lazy" decoding="async" draggable="false"><span class="pan-canvas__label">Chimney repair</span></button><div class="pan-canvas__info"><p class="pan-canvas__meta">Springfield · 2025</p><p class="pan-canvas__desc">A repointed stack, a new cowl and a lined flue for a wood stove.</p></div></li>
    </ul>

    <p class="pan-canvas__hint" aria-hidden="true" hidden>
      <svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M8 13V5.5a1.5 1.5 0 0 1 3 0V11m0-1.5a1.5 1.5 0 0 1 3 0V11m0-.5a1.5 1.5 0 0 1 3 0V12m0-.5a1.5 1.5 0 0 1 3 0V16a6 6 0 0 1-6 6h-1.5a6 6 0 0 1-4.6-2.2L4.5 17a1.6 1.6 0 0 1 2.4-2.1L8 16" /></svg>
      Drag to explore
    </p>
    <p class="pan-canvas__keys" aria-hidden="true"><kbd>←</kbd><kbd>↑</kbd><kbd>↓</kbd><kbd>→</kbd> move · <kbd>Enter</kbd> details</p>
  </div>

  <dialog class="pan-canvas__caption" aria-labelledby="pan-canvas-caption-title">
    <div class="pan-canvas__caption-panel">
      <p class="pan-canvas__caption-meta"></p>
      <h3 id="pan-canvas-caption-title" class="pan-canvas__caption-title"></h3>
      <p class="pan-canvas__caption-text"></p>
      <div class="pan-canvas__caption-actions">
        <a class="pan-canvas__caption-link" href="#case-studies">
          View case study
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <button class="pan-canvas__caption-close" type="button">Close</button>
      </div>
    </div>
  </dialog>
</section>
```

## CSS

```css
/* Section: deep surface */
.pan-canvas {
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(60rem 30rem at 15% 0%, color-mix(in srgb, var(--primary) 18%, transparent), transparent 70%),
    radial-gradient(50rem 30rem at 95% 100%, color-mix(in srgb, var(--primary-2) 14%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); font-family: var(--font-sans);
}
.pan-canvas svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.pan-canvas__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.pan-canvas__head {
  display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 1rem 2rem;
  max-width: var(--container-max); margin-inline: auto; padding: clamp(2.5rem, 6vw, 4rem) var(--gutter) 1.5rem;
}
.pan-canvas__eyebrow { margin: 0; color: color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse)); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.pan-canvas__title { margin: 0.75rem 0 0; font: 600 clamp(1.75rem, 1.1rem + 2.6vw, 2.75rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.pan-canvas__toggle {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.125rem 0 0.875rem;
  border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  font: 600 0.875rem/1 var(--font-sans);
  transition: background-color var(--dur-2), color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.pan-canvas__toggle[hidden] { display: none; }
.pan-canvas__toggle:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.pan-canvas__toggle:active { transform: scale(0.96); }
.pan-canvas__toggle[aria-pressed="true"] { background: var(--text-inverse); color: var(--surface-deep); }

/* Plain grid: the no-JS layout and "View as grid" */
.pan-canvas__viewport { position: relative; max-width: var(--container-max); margin-inline: auto; padding: 0.5rem var(--gutter) clamp(3rem, 7vw, 5rem); }
.pan-canvas__list { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 15rem), 1fr)); gap: 1.5rem 1.25rem; margin: 0; padding: 0; list-style: none; }
.pan-canvas__item { display: grid; align-content: start; gap: 0.75rem; }
.pan-canvas__tile {
  position: relative; display: block; width: 100%; aspect-ratio: 4 / 3; padding: 0; overflow: hidden;
  border: 0; border-radius: var(--radius-xl); background: var(--surface-dark); color: var(--text-inverse); cursor: pointer;
  font: inherit; text-align: left;
  box-shadow: 0 24px 48px -24px color-mix(in srgb, var(--surface-deep) 90%, transparent);
  transition: opacity var(--dur-4) var(--ease-out), box-shadow var(--dur-3) var(--ease-out);
}
.pan-canvas__tile::after { content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.pan-canvas__tile img { display: block; width: 100%; height: 100%; object-fit: cover; pointer-events: none; -webkit-user-drag: none; transition: transform var(--dur-5) var(--ease-out); }
.pan-canvas__tile:hover img { transform: scale(1.05); }
.pan-canvas__label {
  position: absolute; inset: auto 0 0; padding: 2.25rem 0.875rem 0.75rem;
  background: linear-gradient(180deg, transparent, color-mix(in srgb, var(--surface-deep) 80%, transparent) 55%, color-mix(in srgb, var(--surface-deep) 90%, transparent));
  font-size: 0.875rem; font-weight: 600; line-height: 1.25;
}
.pan-canvas__info p { margin: 0; }
.pan-canvas__meta { color: var(--text-inverse-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.pan-canvas__info .pan-canvas__desc { margin-top: 0.375rem; color: var(--text-inverse-muted); font-size: 0.875rem; line-height: 1.5; }
.pan-canvas__dots, .pan-canvas__keys { display: none; }
.pan-canvas :is(.pan-canvas__tile, .pan-canvas__toggle):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Canvas: JS positions each tile with a transform and wraps it around the world */
.pan-canvas--live .pan-canvas__viewport {
  max-width: none; height: clamp(20rem, 62vh, 30rem); height: clamp(20rem, 62svh, 30rem); padding: 0;
  overflow: clip; touch-action: none; cursor: grab; user-select: none; -webkit-user-select: none;
  border-block: 1px solid var(--border-inverse);
}
.pan-canvas--live.is-dragging .pan-canvas__viewport { cursor: grabbing; }
.pan-canvas--live .pan-canvas__list { position: absolute; inset: 0; display: block; }
.pan-canvas--live .pan-canvas__item { position: absolute; top: 0; left: 0; display: block; will-change: transform; }
.pan-canvas--live .pan-canvas__item:nth-child(n + 21) { display: none; } /* the canvas lays out 5 × 4 tiles */
.pan-canvas--live .pan-canvas__tile { height: 100%; aspect-ratio: auto; border-radius: var(--radius-lg); }
.pan-canvas--live .pan-canvas__info { display: none; }
.pan-canvas--live .pan-canvas__label { padding: 1.75rem 0.75rem 0.625rem; font-size: 0.8125rem; }
.pan-canvas--live .pan-canvas__dots {
  display: block; position: absolute; inset: -32px; pointer-events: none;
  background: radial-gradient(circle at 1px 1px, color-mix(in srgb, var(--text-inverse) 14%, transparent) 1px, transparent 1.5px) 0 0 / 32px 32px;
}
.pan-canvas--live .pan-canvas__viewport::after { /* vignette */
  content: ""; position: absolute; inset: 0; z-index: 1; pointer-events: none;
  background: radial-gradient(120% 95% at 50% 50%, transparent 55%, color-mix(in srgb, var(--surface-deep) 80%, transparent));
}
.pan-canvas.is-captioned .pan-canvas__item:not(.is-selected) .pan-canvas__tile { opacity: 0.28; }
.pan-canvas__item.is-selected .pan-canvas__tile { box-shadow: 0 0 0 2px var(--text-inverse), 0 30px 60px -20px color-mix(in srgb, var(--primary) 55%, transparent); }

/* Hint (fades after the first interaction) and a key legend shown while a tile has keyboard focus */
.pan-canvas__hint {
  position: absolute; left: 50%; bottom: 1.25rem; z-index: 2; display: inline-flex; align-items: center; gap: 0.5rem; margin: 0;
  padding: 0.5rem 1rem 0.5rem 0.75rem; border-radius: var(--radius-full); pointer-events: none; translate: -50% 0;
  background: color-mix(in srgb, var(--surface-deep) 85%, transparent); color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 12px 30px -12px color-mix(in srgb, var(--surface-deep) 90%, transparent);
  font-size: 0.8125rem; font-weight: 600; white-space: nowrap;
  transition: opacity var(--dur-5) var(--ease-out), translate var(--dur-5) var(--ease-out);
}
.pan-canvas__hint[hidden], .pan-canvas:not(.pan-canvas--live) .pan-canvas__hint { display: none; }
.pan-canvas.is-explored .pan-canvas__hint { opacity: 0; translate: -50% 0.75rem; }
.pan-canvas--live .pan-canvas__keys {
  position: absolute; top: 1rem; right: 1rem; z-index: 2; display: flex; align-items: center; gap: 0.25rem; margin: 0;
  padding: 0.375rem 0.75rem; border-radius: var(--radius-full); pointer-events: none; opacity: 0;
  background: color-mix(in srgb, var(--surface-deep) 85%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse);
  color: var(--text-inverse-muted); font-size: 0.75rem; white-space: nowrap;
  transition: opacity var(--dur-3) var(--ease-out);
}
.pan-canvas__keys kbd {
  min-width: 1.375rem; padding: 0.125rem 0.3125rem; border-radius: 0.375rem; text-align: center;
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), inset 0 -1px 0 var(--border-inverse);
  color: var(--text-inverse); font: 600 0.6875rem/1.2 var(--font-mono);
}
.pan-canvas__viewport:has(.pan-canvas__tile:focus-visible) .pan-canvas__keys { opacity: 1; }
@supports (backdrop-filter: blur(1px)) {
  .pan-canvas__hint, .pan-canvas--live .pan-canvas__keys { backdrop-filter: blur(var(--blur-md)) saturate(1.3); }
}

/* Caption: a glass card that springs up from the bottom */
.pan-canvas__caption {
  position: fixed; inset: auto 0.75rem max(0.75rem, env(safe-area-inset-bottom)); width: auto; max-width: 34rem; margin: 0 auto; padding: 0;
  border: 0; border-radius: var(--radius-2xl); color: var(--text-inverse); background: color-mix(in srgb, var(--surface-dark) 90%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 30px 80px -20px color-mix(in srgb, var(--surface-deep) 90%, transparent);
  opacity: 0; transform: translateY(1.5rem) scale(0.97);
  transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring);
  transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring), overlay var(--dur-4) allow-discrete, display var(--dur-4) allow-discrete;
}
@supports (backdrop-filter: blur(1px)) {
  .pan-canvas__caption { backdrop-filter: blur(var(--blur-lg)) saturate(1.3); }
}
.pan-canvas__caption[open] { opacity: 1; transform: none; }
@starting-style {
  .pan-canvas__caption[open] { opacity: 0; transform: translateY(1.5rem) scale(0.97); }
}
.pan-canvas__caption::backdrop { background: transparent; }
.pan-canvas__caption-panel { padding: 1.25rem 1.25rem 1rem; }
.pan-canvas__caption-meta { margin: 0; color: var(--text-inverse-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.pan-canvas__caption-title { margin: 0.5rem 0 0; font: 600 1.5rem/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.pan-canvas__caption-text { margin: 0.5rem 0 0; color: var(--text-inverse-muted); font-size: 0.9375rem; line-height: 1.55; }
.pan-canvas__caption-actions { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.125rem; }
.pan-canvas__caption-link, .pan-canvas__caption-close {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.125rem;
  border-radius: var(--radius-full); font: 600 0.875rem/1 var(--font-sans); text-decoration: none; cursor: pointer;
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.pan-canvas__caption-link { flex: 1; background: var(--text-inverse); color: var(--surface-deep); }
.pan-canvas__caption-link svg { transition: transform var(--dur-3) var(--ease-spring); }
.pan-canvas__caption-link:hover svg { transform: translateX(3px); }
.pan-canvas__caption-close { border: 0; background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); }
.pan-canvas__caption-close:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.pan-canvas__caption :is(.pan-canvas__caption-link, .pan-canvas__caption-close):active { transform: scale(0.97); }
.pan-canvas__caption :is(.pan-canvas__caption-link, .pan-canvas__caption-close):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

@media (min-width: 768px) {
  .pan-canvas--live .pan-canvas__viewport { height: clamp(22rem, 100vh - 13rem, 44rem); height: clamp(22rem, 100svh - 13rem, 44rem); }
  .pan-canvas__caption { inset: auto 0 2rem; }
}

/* With scripting on, hold the canvas shape from the first paint so the grid never flashes;
   if the script never runs, the failsafe brings the plain grid back */
@media (scripting: enabled) {
  .pan-canvas:not(.pan-canvas--js) .pan-canvas__viewport {
    max-width: none; height: clamp(20rem, 62svh, 30rem); padding: 0; overflow: clip;
    animation: pan-canvas-failsafe 1ms 2.5s forwards;
  }
  .pan-canvas:not(.pan-canvas--js) .pan-canvas__list { visibility: hidden; animation: pan-canvas-reveal 1ms 2.5s forwards; }
}
@media (scripting: enabled) and (min-width: 768px) {
  .pan-canvas:not(.pan-canvas--js) .pan-canvas__viewport { height: clamp(22rem, 100svh - 13rem, 44rem); }
}
/* The failsafes are instant steps, not motion, so they stay on under prefers-reduced-motion */
@keyframes pan-canvas-failsafe { to { max-width: var(--container-max); height: auto; padding: 0.5rem var(--gutter) 3rem; overflow: visible; } }
@keyframes pan-canvas-reveal { to { visibility: visible; } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const COLS = 5;
const ROWS = 4;
// Tile heights per column in quarter tile-widths (every column sums to 16), and each column's stagger
const HEIGHTS = [[4, 3, 5, 4], [3, 5, 4, 4], [5, 4, 3, 4], [4, 4, 5, 3], [3, 4, 4, 5]];
const OFFSETS = [0, -1.5, -0.5, -2, -1];
const wrap = (value, size) => ((value % size) + size) % size;

document.querySelectorAll('[data-pan-canvas]').forEach((root) => {
  const [viewport, dots, help, toggle, hint, caption] = ['viewport', 'dots', 'sr', 'toggle', 'hint', 'caption']
    .map((part) => root.querySelector(`.pan-canvas__${part}`));
  const items = [...root.querySelectorAll('.pan-canvas__item')].slice(0, COLS * ROWS)
    .map((el) => ({ el, button: el.querySelector('.pan-canvas__tile'), img: el.querySelector('img') }));
  let panX = 0, panY = 0, vx = 0, vy = 0, W = 1, H = 1, colW = 1, maxH = 0, vw = 0, vh = 0;
  let glide = null, drag = null, opener = null, frame = 0, last = 0;
  let grid = false, started = false, engaged = false, dragged = false;
  const halt = () => { glide = null; vx = 0; vy = 0; };
  root.classList.add('pan-canvas--js');

  // Wrap every tile into the window; tiles near the centre grow a little and brighten
  const render = () => {
    const reach = Math.hypot(vw, vh) * 0.55;
    items.forEach((t) => {
      t.x = wrap(t.bx + panX, W) - colW;
      t.y = wrap(t.by + panY, H) - maxH;
      const near = Math.max(0, 1 - Math.hypot(t.x + t.w / 2 - vw / 2, t.y + t.h / 2 - vh / 2) / reach);
      t.el.style.transform = `translate3d(${t.x.toFixed(1)}px, ${t.y.toFixed(1)}px, 0) scale(${(0.93 + 0.1 * near ** 2).toFixed(3)})`;
      t.img.style.opacity = (0.4 + 0.6 * near).toFixed(3);
    });
    dots.style.transform = `translate3d(${wrap(panX / 2, 32)}px, ${wrap(panY / 2, 32)}px, 0)`;
  };
  // Sizes follow the viewport, so the wrapped world always covers it
  const layout = () => {
    vw = viewport.clientWidth; vh = viewport.clientHeight;
    colW = Math.max(176, vw / 3.6, vh / 2.4);
    const gap = Math.round(colW * 0.06), u = (colW - gap) / 4;
    W = COLS * colW; H = 16 * u + ROWS * gap; maxH = 5 * u + gap;
    items.forEach((t, i) => {
      const c = i % COLS, r = Math.floor(i / COLS);
      Object.assign(t, { w: colW - gap, h: HEIGHTS[c][r] * u, bx: c * colW + gap / 2 });
      t.by = OFFSETS[c] * u + HEIGHTS[c].slice(0, r).reduce((sum, n) => sum + n * u + gap, 0);
      Object.assign(t.el.style, { width: `${t.w}px`, height: `${t.h}px` });
    });
    if (!started) { panX = vw * 0.2 + colW; panY = vh * 0.12 + maxH; started = true; }
    render();
  };
  // One rAF loop drives dragging, inertia and glides, and stops when nothing moves
  const tick = (now) => {
    const dt = Math.min(48, now - (last || now));
    last = now;
    if (glide) {
      const p = Math.min(1, (now - glide.t0) / glide.dur), eased = 1 - (1 - p) ** 3;
      panX = glide.x0 + glide.dx * eased; panY = glide.y0 + glide.dy * eased;
      if (p === 1) glide = null;
    } else if (!drag) {
      const friction = 0.95 ** (dt / 16.7);
      panX += vx * dt; panY += vy * dt; vx *= friction; vy *= friction;
    }
    render();
    frame = drag || glide || Math.abs(vx) + Math.abs(vy) > 0.01 ? requestAnimationFrame(tick) : 0;
    if (!frame) last = 0;
  };
  // Any interaction also retires the "Drag to explore" hint
  const kick = () => { root.classList.add('is-explored'); if (!frame && !grid) frame = requestAnimationFrame(tick); };
  // Glide a tile to a point in the viewport (--dur-4 collapses under reduced motion, so it jumps)
  const bring = (t, fy = 0.5) => {
    halt();
    const dur = parseFloat(getComputedStyle(root).getPropertyValue('--dur-4')) || 560;
    glide = { x0: panX, y0: panY, dx: vw / 2 - (t.x + t.w / 2), dy: vh * fy - (t.y + t.h / 2), t0: performance.now(), dur };
    kick();
  };

  // Drag with momentum; a press that barely moves still counts as a click
  viewport.addEventListener('pointerdown', (e) => {
    if (grid || e.button !== 0) return;
    halt(); kick(); engaged = true;
    drag = { x: e.clientX, y: e.clientY, t: e.timeStamp, moved: 0, id: e.pointerId };
  });
  viewport.addEventListener('pointermove', (e) => {
    if (!drag || e.pointerId !== drag.id) return;
    const dx = e.clientX - drag.x, dy = e.clientY - drag.y, dt = Math.max(8, e.timeStamp - drag.t);
    drag.moved += Math.abs(dx) + Math.abs(dy);
    if (drag.moved > 6 && !viewport.hasPointerCapture(drag.id)) {
      viewport.setPointerCapture(drag.id);
      root.classList.add('is-dragging');
    }
    panX += dx; panY += dy;
    vx = vx * 0.5 + (dx / dt) * 0.5; vy = vy * 0.5 + (dy / dt) * 0.5;
    Object.assign(drag, { x: e.clientX, y: e.clientY, t: e.timeStamp });
  }, { passive: true });
  const release = (e) => {
    if (!drag) return;
    dragged = drag.moved > 6;
    if (!dragged || reduce.matches || e.timeStamp - drag.t > 80) { vx = 0; vy = 0; } // no inertia under reduced motion
    drag = null; root.classList.remove('is-dragging'); kick();
  };
  ['pointerup', 'pointercancel'].forEach((type) => viewport.addEventListener(type, release));
  viewport.addEventListener('pointerleave', () => { engaged = false; });
  // Wheel and trackpad: sideways swipes always pan; vertical scrolling pans only once the
  // canvas has been grabbed or focused, so the page never gets stuck
  viewport.addEventListener('wheel', (e) => {
    const sideways = Math.abs(e.deltaX) > Math.abs(e.deltaY);
    if (grid || e.ctrlKey || (!sideways && !engaged && !viewport.contains(document.activeElement))) return;
    e.preventDefault();
    const scale = [1, 16, vh][e.deltaMode] ?? 1;
    halt(); kick();
    panX -= e.deltaX * scale; panY -= e.deltaY * scale;
  }, { passive: false });

  // Focus pans a tile to the centre; arrow keys step to the neighbouring tile, wrapping
  viewport.addEventListener('focusin', (e) => {
    const t = items.find((item) => item.button === e.target);
    if (t && !grid && !drag) bring(t);
  });
  viewport.addEventListener('keydown', (e) => {
    const step = { ArrowRight: [1, 0], ArrowLeft: [-1, 0], ArrowDown: [0, 1], ArrowUp: [0, -1] }[e.key];
    const i = items.findIndex((t) => t.button === document.activeElement);
    if (!step || i < 0 || grid) return;
    e.preventDefault();
    const c = (i % COLS + step[0] + COLS) % COLS, r = (Math.floor(i / COLS) + step[1] + ROWS) % ROWS;
    items[r * COLS + c].button.focus({ preventScroll: true });
  });
  // Caption: a modal dialog filled from the tile's own caption, with the tile parked above it
  viewport.addEventListener('click', (e) => {
    const t = items.find((item) => item.button === e.target.closest('.pan-canvas__tile'));
    if (dragged || !t) { dragged = false; return; }
    for (const [to, from] of [['meta', 'meta'], ['title', 'label'], ['text', 'desc']]) {
      caption.querySelector(`.pan-canvas__caption-${to}`).textContent = t.el.querySelector(`.pan-canvas__${from}`).textContent.trim();
    }
    opener = t;
    t.el.classList.add('is-selected');
    root.classList.add('is-captioned');
    caption.showModal();
    if (!grid) bring(t, 0.38);
  });
  caption.addEventListener('click', (e) => {
    if (e.target === caption || e.target.closest('.pan-canvas__caption-close')) caption.close();
  });
  caption.addEventListener('close', () => {
    root.classList.remove('is-captioned');
    opener?.el.classList.remove('is-selected');
    opener?.button.focus({ preventScroll: true });
  });

  // "View as grid": drop the inline transforms and let the base CSS lay the list out
  const setGrid = (on) => {
    cancelAnimationFrame(frame);
    grid = on; help.hidden = on; frame = 0; last = 0; drag = null;
    halt();
    root.classList.toggle('pan-canvas--live', !on);
    toggle.setAttribute('aria-pressed', String(on));
    items.forEach((t) => { t.el.removeAttribute('style'); t.img.removeAttribute('style'); });
    if (!on) layout();
  };
  toggle.addEventListener('click', () => setGrid(!grid));
  toggle.hidden = hint.hidden = false;
  new ResizeObserver(() => { if (!grid) layout(); }).observe(viewport);
  setGrid(false);
});
```

## Notes

- Every project is a `<button>` in a real list, in DOM order, with `aria-haspopup="dialog"`. Tab walks the list and each focused tile glides to the centre, while arrow keys jump to the neighbouring tile in the wrapped grid (focus never leaves the visible area). Enter opens the caption, a modal `<dialog>` labelled by the project title. Escape, the backdrop or Close dismiss it and focus returns to the tile. Visually hidden instructions open the canvas region (shown only in canvas mode), and a key legend appears while a tile has keyboard focus.
- "View as grid" (`aria-pressed`) swaps in a plain responsive grid with each caption printed under its photo. That grid is also the no-JS layout. With scripting on, `@media (scripting: enabled)` holds the canvas shape from the first paint so the grid never flashes, and a 2.5s CSS failsafe restores the grid if the script fails.
- Panning is rAF-driven and transform-only. The 20 tiles are positioned once per frame with modulo wrapping, and the loop stops when nothing moves. Vertical wheel scrolling pans only after the canvas has been grabbed or focused, so the page can always scroll past it, while sideways trackpad swipes always pan. On phones the canvas is shorter, so there's always page above or below it to scroll with.
- Reduced motion: no inertia, and glides jump (they use `--dur-4`, which collapses). The caption appears without its spring, and the hint simply disappears. Nothing moves on its own, so no pause control is needed.
- Contrast: tile titles sit on an 80–90% `--surface-deep` scrim, so they're 7:1 or better even over a white photo. The caption card and chips are at least 85% opaque, which keeps `--text-inverse-muted` at 5:1 or better.
- To adapt it, the canvas lays out a 5 × 4 set. Change `COLS`, `ROWS`, `HEIGHTS` (quarter tile-widths, each column summing to the same total) and `OFFSETS` for a different set, and give each `<img>` the `width`/`height` of its ratio (3 = 4:3, 4 = 1:1, 5 = 4:5).
