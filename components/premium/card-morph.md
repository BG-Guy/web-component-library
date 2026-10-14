# Card-to-Detail Morph

A grid of case-study cards that open into a full project view. Choosing a card morphs it into a dialog with the View Transitions API: the card surface grows into the panel, the photo widens into a hero and the title flies into place, then the Budget, Duration and Rating row, the story and a "Book a similar project" button rise in. Closing morphs the panel back into its card. On phones the detail opens as a full-screen sheet. Depends on `tokens/variables.css`.

**Motion:** View Transition container morph: panel, hero and title groups glide (`--dur-5`, `--ease-out`) while card and panel contents cross-fade (`--dur-3` out, `--dur-4` in) · stats, copy and CTA rise in, staggered (`--dur-4`, `--stagger`) and fade out first on close (`--dur-2`) · fallback scale and fade via `@starting-style` (`--dur-3`, `--ease-spring`) · card lift and image zoom (`--dur-3`/`--dur-5`) · open-arrow pop and close-button spin (`--ease-spring`).

## HTML

```html
<section class="card-morph" aria-labelledby="card-morph-heading" data-card-morph>
  <div class="card-morph__inner">
    <header class="card-morph__head">
      <p class="card-morph__eyebrow">Case studies</p>
      <h2 id="card-morph-heading" class="card-morph__title">Recent work around Springfield</h2>
      <p class="card-morph__intro">Three jobs, start to finish. Open one for the numbers.</p>
    </header>

    <ul class="card-morph__grid" role="list">
      <li class="card-morph__card" data-card-morph-part="panel">
        <div class="card-morph__frame" data-card-morph-part="hero">
          <img class="card-morph__media" src="westlake-kitchen.jpg" alt="" width="800" height="600" loading="lazy" decoding="async">
        </div>
        <div class="card-morph__meta">
          <ul class="card-morph__chips" role="list"><li class="card-morph__chip">Plumbing</li><li class="card-morph__chip">Westlake</li></ul>
          <h3 class="card-morph__name" data-card-morph-part="title"><a class="card-morph__link" href="#card-morph-westlake">Westlake kitchen re-pipe</a></h3>
          <p class="card-morph__result">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M3 17l6-6 4 4 8-8M15 7h6v6" /></svg>
            Water pressure up 40%, done in a day.
          </p>
        </div>
        <span class="card-morph__open" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
      </li>
      <li class="card-morph__card" data-card-morph-part="panel">
        <div class="card-morph__frame" data-card-morph-part="hero">
          <img class="card-morph__media" src="northside-panel.jpg" alt="" width="800" height="600" loading="lazy" decoding="async">
        </div>
        <div class="card-morph__meta">
          <ul class="card-morph__chips" role="list"><li class="card-morph__chip">Electrical</li><li class="card-morph__chip">Northside</li></ul>
          <h3 class="card-morph__name" data-card-morph-part="title"><a class="card-morph__link" href="#card-morph-northside">Northside panel upgrade</a></h3>
          <p class="card-morph__result">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M3 17l6-6 4 4 8-8M15 7h6v6" /></svg>
            100 A to 200 A, ready for an EV charger.
          </p>
        </div>
        <span class="card-morph__open" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
      </li>
      <li class="card-morph__card" data-card-morph-part="panel">
        <div class="card-morph__frame" data-card-morph-part="hero">
          <img class="card-morph__media" src="riverside-boiler.jpg" alt="" width="800" height="600" loading="lazy" decoding="async">
        </div>
        <div class="card-morph__meta">
          <ul class="card-morph__chips" role="list"><li class="card-morph__chip">Heating</li><li class="card-morph__chip">Riverside</li></ul>
          <h3 class="card-morph__name" data-card-morph-part="title"><a class="card-morph__link" href="#card-morph-riverside">Riverside boiler swap</a></h3>
          <p class="card-morph__result">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M3 17l6-6 4 4 8-8M15 7h6v6" /></svg>
            Gas bills down 23% the first winter.
          </p>
        </div>
        <span class="card-morph__open" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
      </li>
    </ul>

    <div class="card-morph__details">
      <article class="card-morph__detail" id="card-morph-westlake" aria-labelledby="card-morph-westlake-title">
        <img class="card-morph__hero" data-card-morph-part="hero" src="westlake-kitchen.jpg" alt="New copper supply lines running along the back of a kitchen cabinet" width="1600" height="700" loading="lazy" decoding="async">
        <div class="card-morph__body">
          <ul class="card-morph__chips" role="list"><li class="card-morph__chip">Plumbing</li><li class="card-morph__chip">Westlake</li></ul>
          <h3 id="card-morph-westlake-title" class="card-morph__heading" data-card-morph-part="title">Westlake kitchen re-pipe</h3>
          <dl class="card-morph__stats" data-card-morph-part="stats">
            <div class="card-morph__stat"><dt>Budget</dt><dd>$4,850</dd></div>
            <div class="card-morph__stat"><dt>Duration</dt><dd>1 day</dd></div>
            <div class="card-morph__stat"><dt>Rating</dt><dd>5.0 <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg></dd></div>
          </dl>
          <div class="card-morph__copy" data-card-morph-part="copy">
            <p>The Hendersons' 1960s galvanised pipes had narrowed to a trickle, and their new kitchen floor had gone down the week before. We re-routed the supply through the cabinets and the basement ceiling instead, so not a single board came up.</p>
            <p>Two technicians, one day, and a pressure test signed off before dinner. The old pipe went to the recycler, not the landfill.</p>
          </div>
          <div class="card-morph__actions" data-card-morph-part="cta">
            <a class="card-morph__cta" href="#book">
              Book a similar project
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
            <a class="card-morph__back" href="#card-morph-heading">Back to all projects</a>
          </div>
        </div>
      </article>

      <article class="card-morph__detail" id="card-morph-northside" aria-labelledby="card-morph-northside-title">
        <img class="card-morph__hero" data-card-morph-part="hero" src="northside-panel.jpg" alt="Open electrical panel with neatly labelled new breakers" width="1600" height="700" loading="lazy" decoding="async">
        <div class="card-morph__body">
          <ul class="card-morph__chips" role="list"><li class="card-morph__chip">Electrical</li><li class="card-morph__chip">Northside</li></ul>
          <h3 id="card-morph-northside-title" class="card-morph__heading" data-card-morph-part="title">Northside panel upgrade</h3>
          <dl class="card-morph__stats" data-card-morph-part="stats">
            <div class="card-morph__stat"><dt>Budget</dt><dd>$3,200</dd></div>
            <div class="card-morph__stat"><dt>Duration</dt><dd>6 hours</dd></div>
            <div class="card-morph__stat"><dt>Rating</dt><dd>4.9 <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg></dd></div>
          </dl>
          <div class="card-morph__copy" data-card-morph-part="copy">
            <p>A new heat pump and an EV on order meant the old 100-amp panel couldn't keep up. We pulled the permit, booked the utility shut-off for a weekday morning and had the lights back on by early afternoon.</p>
            <p>The charger circuit is already in, labelled and inspected, so fitting the charger is a twenty-minute job when the car arrives.</p>
          </div>
          <div class="card-morph__actions" data-card-morph-part="cta">
            <a class="card-morph__cta" href="#book">
              Book a similar project
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
            <a class="card-morph__back" href="#card-morph-heading">Back to all projects</a>
          </div>
        </div>
      </article>

      <article class="card-morph__detail" id="card-morph-riverside" aria-labelledby="card-morph-riverside-title">
        <img class="card-morph__hero" data-card-morph-part="hero" src="riverside-boiler.jpg" alt="Wall-mounted condensing boiler with new insulated pipework" width="1600" height="700" loading="lazy" decoding="async">
        <div class="card-morph__body">
          <ul class="card-morph__chips" role="list"><li class="card-morph__chip">Heating</li><li class="card-morph__chip">Riverside</li></ul>
          <h3 id="card-morph-riverside-title" class="card-morph__heading" data-card-morph-part="title">Riverside boiler swap</h3>
          <dl class="card-morph__stats" data-card-morph-part="stats">
            <div class="card-morph__stat"><dt>Budget</dt><dd>$6,400</dd></div>
            <div class="card-morph__stat"><dt>Duration</dt><dd>2 days</dd></div>
            <div class="card-morph__stat"><dt>Rating</dt><dd>5.0 <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg></dd></div>
          </dl>
          <div class="card-morph__copy" data-card-morph-part="copy">
            <p>A 25-year-old boiler, a cold back bedroom and bills that kept climbing. We sized a condensing combi to the house rather than to the old unit, balanced every radiator and added a smart thermostat.</p>
            <p>The first winter's gas bill came in 23% lower, and the back bedroom finally keeps up with the rest of the house.</p>
          </div>
          <div class="card-morph__actions" data-card-morph-part="cta">
            <a class="card-morph__cta" href="#book">
              Book a similar project
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
            <a class="card-morph__back" href="#card-morph-heading">Back to all projects</a>
          </div>
        </div>
      </article>
    </div>
  </div>

  <dialog class="card-morph__dialog" data-card-morph-part="panel">
    <button class="card-morph__close" type="button" aria-label="Close project details" autofocus>
      <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
    </button>
    <div class="card-morph__sheet"></div>
  </dialog>
</section>
```

## CSS

```css
/* Section and heading */
.card-morph { background: var(--surface-muted); color: var(--text-main); font-family: var(--font-sans); }
.card-morph__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.card-morph__head { display: grid; gap: 0.75rem; max-width: 40rem; margin-bottom: clamp(2rem, 5vw, 3.5rem); }
.card-morph__eyebrow { margin: 0; color: var(--primary); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.card-morph__title { margin: 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.card-morph__intro { margin: 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }

/* Cards: the title link stretches over the whole card */
.card-morph__grid { display: grid; gap: 1.25rem; margin: 0; padding: 0; list-style: none; }
.card-morph__card {
  position: relative; display: flex; flex-direction: column; padding: 0.5rem; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.card-morph__card:hover { transform: translateY(-4px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl); }
.card-morph__card:active { transform: scale(0.985); }
.card-morph__frame, .card-morph__hero {
  border-radius: var(--radius-xl);
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 22%, var(--surface-muted)), color-mix(in srgb, var(--primary-2) 26%, var(--surface-muted)));
}
.card-morph__frame { position: relative; overflow: hidden; }
.card-morph__media { display: block; width: 100%; height: auto; aspect-ratio: 4 / 3; object-fit: cover; transition: transform var(--dur-5) var(--ease-out); }
.card-morph__card:hover .card-morph__media { transform: scale(1.04); }
.card-morph__open {
  position: absolute; top: 1rem; right: 1rem; display: grid; place-items: center; width: 2.25rem; height: 2.25rem; border-radius: 50%; pointer-events: none;
  background: color-mix(in srgb, var(--surface-light) 88%, transparent); color: var(--text-main); box-shadow: var(--shadow-md);
  transition: opacity var(--dur-2) var(--ease-out), scale var(--dur-3) var(--ease-spring);
}
@media (hover: hover) {
  .card-morph__open { opacity: 0; scale: 0.7; }
  .card-morph__card:is(:hover, :focus-within) .card-morph__open { opacity: 1; scale: 1; }
}
.card-morph__meta { display: grid; gap: 0.5rem; padding: 1rem 0.75rem 0.75rem; }
.card-morph__name { justify-self: start; margin: 0.25rem 0 0; font: 600 1.25rem/1.25 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.card-morph__link { color: inherit; text-decoration: none; }
.card-morph__link::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-2xl); }
.card-morph__link:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
@supports selector(:has(*)) {
  .card-morph__link:focus-visible { outline: none; }
  .card-morph__card:has(.card-morph__link:focus-visible) { outline: 2px solid var(--primary); outline-offset: 3px; }
}
.card-morph__result { display: flex; align-items: flex-start; gap: 0.5rem; margin: 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.5; }
.card-morph__result svg { flex: none; margin-top: 0.0625rem; color: var(--success); }

/* Chips */
.card-morph__chips { display: flex; flex-wrap: wrap; gap: 0.375rem; margin: 0; padding: 0; list-style: none; }
.card-morph__chip {
  padding: 0.25rem 0.625rem; border-radius: var(--radius-full); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle);
  color: var(--text-muted); font: 500 0.6875rem/1.4 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
}
.card-morph__chip:first-child {
  background: color-mix(in srgb, var(--primary) 10%, var(--surface-light)); color: var(--primary-hover);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 22%, transparent);
}

/* Details: a static list below the grid without JS; one at a time inside the dialog with it */
.card-morph__details { display: grid; gap: 1.5rem; margin-top: clamp(3rem, 8vw, 5rem); }
.card-morph__details[hidden] { display: none; }
.card-morph__detail {
  padding: 0.5rem; border-radius: var(--radius-2xl); scroll-margin-top: 1.5rem;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
}
.card-morph__detail:target { box-shadow: inset 0 0 0 2px var(--primary), var(--shadow-xl); }
.card-morph__sheet .card-morph__detail { padding: 0; border-radius: 0; background: none; box-shadow: none; }
.card-morph__hero { display: block; width: 100%; height: auto; aspect-ratio: 4 / 3; object-fit: cover; }
.card-morph__body { display: grid; gap: 1.25rem; padding: 1.5rem 1rem 1.75rem; }
.card-morph__heading { margin: 0; font: 600 clamp(1.875rem, 1.3rem + 2.2vw, 2.75rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.card-morph__stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); margin: 0; border-block: 1px solid var(--border-subtle); }
.card-morph__stat { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.375rem; padding: 1rem 0.5rem 1rem 0; }
.card-morph__stat + .card-morph__stat { padding-left: 1rem; border-left: 1px solid var(--border-subtle); }
.card-morph__stat dt { color: var(--text-muted); font: 500 0.6875rem/1.3 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.card-morph__stat dd { display: flex; align-items: center; gap: 0.25rem; margin: 0; font: 600 clamp(1.25rem, 1rem + 1vw, 1.625rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.card-morph__stat svg { flex: none; color: var(--accent); fill: currentColor; stroke: currentColor; stroke-width: 1.5; stroke-linejoin: round; }
.card-morph__copy { display: grid; gap: 0.875rem; max-width: 42rem; color: var(--text-muted); font-size: 1rem; line-height: 1.65; }
.card-morph__copy p { margin: 0; }
.card-morph__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.25rem; }
.card-morph__cta {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font: 600 0.9375rem/1.2 var(--font-sans); text-decoration: none;
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 12px 28px -12px var(--primary);
  transition: transform var(--dur-2) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.card-morph__cta:hover { transform: translateY(-2px); box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 16px 32px -12px var(--primary); }
.card-morph__cta:active { transform: scale(0.97); }
.card-morph__back { display: inline-flex; align-items: center; min-height: 2.75rem; color: var(--primary); font-size: 0.9375rem; font-weight: 600; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 0.3em; }
.card-morph__dialog .card-morph__back { display: none; }
.card-morph :is(.card-morph__result, .card-morph__open, .card-morph__cta, .card-morph__close) svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.card-morph__cta svg { transition: transform var(--dur-3) var(--ease-spring); }
.card-morph__cta:hover svg { transform: translateX(3px); }
.card-morph :is(.card-morph__cta, .card-morph__back):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Dialog: a full-screen sheet on phones, a centred panel from 768px */
.card-morph__dialog {
  width: 100%; max-width: 100%; height: 100vh; height: 100dvh; max-height: 100vh; max-height: 100dvh; margin: 0; padding: 0; border: 0; border-radius: 0; overflow: hidden;
  background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
  box-shadow: 0 40px 100px -24px color-mix(in srgb, var(--surface-deep) 55%, transparent);
}
.card-morph__dialog::backdrop { background: color-mix(in srgb, var(--surface-deep) 55%, transparent); -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md)); }
html:has(.card-morph__dialog[open]) { overflow: hidden; scrollbar-gutter: stable; }
.card-morph__sheet { height: 100%; max-height: inherit; padding: 0.5rem; overflow-y: auto; overscroll-behavior: contain; }
.card-morph__close {
  position: absolute; top: 1rem; right: 1rem; z-index: 2; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: color-mix(in srgb, var(--surface-light) 82%, transparent); color: var(--text-main);
  box-shadow: var(--shadow-md), inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 60%, transparent);
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2) var(--ease-out);
}
.card-morph__close:hover { transform: rotate(90deg); background: var(--surface-light); }
.card-morph__close:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; box-shadow: 0 0 0 5px var(--surface-light), var(--shadow-md); }

/* Fallback without View Transitions: scale and fade in */
.card-morph__dialog--fade[open] { transition: opacity var(--dur-3) var(--ease-out), scale var(--dur-4) var(--ease-spring); }
.card-morph__dialog--fade[open]::backdrop { transition: opacity var(--dur-3) var(--ease-out); }
@starting-style {
  .card-morph__dialog--fade[open] { opacity: 0; scale: 0.94; }
  .card-morph__dialog--fade[open]::backdrop { opacity: 0; }
}

/* The morph: names exist only while it runs (set by JS on click) */
::view-transition-group(card-morph-panel),
::view-transition-group(card-morph-hero),
::view-transition-group(card-morph-title) { animation-duration: var(--dur-5); animation-timing-function: var(--ease-out); }
::view-transition-group(card-morph-panel) { overflow: clip; border-radius: var(--radius-2xl); background: var(--surface-light); box-shadow: var(--shadow-xl); }
::view-transition-group(card-morph-hero) { overflow: clip; border-radius: var(--radius-xl); }
::view-transition-old(card-morph-hero),
::view-transition-new(card-morph-hero) { height: 100%; object-fit: cover; }
::view-transition-old(card-morph-title),
::view-transition-new(card-morph-title) { width: 100%; height: 100%; object-fit: none; object-position: left top; }
::view-transition-old(card-morph-panel),
::view-transition-old(card-morph-title) { mix-blend-mode: normal; animation: card-morph-fade-out var(--dur-3) var(--ease-out) both; }
::view-transition-new(card-morph-panel),
::view-transition-new(card-morph-title) { mix-blend-mode: normal; animation: card-morph-fade-in var(--dur-4) var(--ease-out) var(--dur-2) both; }
::view-transition-new(card-morph-stats),
::view-transition-new(card-morph-copy),
::view-transition-new(card-morph-cta) { animation: card-morph-rise var(--dur-4) var(--ease-out) var(--dur-3) both; }
::view-transition-new(card-morph-copy) { animation-delay: calc(var(--dur-3) + var(--stagger) * 2); }
::view-transition-new(card-morph-cta) { animation-delay: calc(var(--dur-3) + var(--stagger) * 4); }
::view-transition-old(card-morph-stats),
::view-transition-old(card-morph-copy),
::view-transition-old(card-morph-cta) { animation: card-morph-fade-out var(--dur-2) var(--ease-out) both; }
@keyframes card-morph-fade-in { from { opacity: 0; } }
@keyframes card-morph-fade-out { to { opacity: 0; } }
@keyframes card-morph-rise { from { opacity: 0; transform: translateY(0.75rem); } }
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(card-morph-panel), ::view-transition-group(card-morph-hero), ::view-transition-group(card-morph-title),
  ::view-transition-old(card-morph-panel), ::view-transition-new(card-morph-panel),
  ::view-transition-old(card-morph-title), ::view-transition-new(card-morph-title),
  ::view-transition-old(card-morph-stats), ::view-transition-new(card-morph-stats),
  ::view-transition-old(card-morph-copy), ::view-transition-new(card-morph-copy),
  ::view-transition-old(card-morph-cta), ::view-transition-new(card-morph-cta) { animation: none !important; }
}

@media (min-width: 768px) {
  .card-morph__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .card-morph__hero { aspect-ratio: 16 / 7; }
  .card-morph__body { padding: 2rem 1.75rem 2.25rem; }
  .card-morph__dialog { width: min(56rem, 100% - 3rem); height: auto; max-height: min(52rem, 100dvh - 3rem); margin: auto; border-radius: var(--radius-2xl); }
}
```

## JS

```js
document.querySelectorAll('[data-card-morph]').forEach((root) => {
  const dialog = root.querySelector('.card-morph__dialog');
  const sheet = dialog.querySelector('.card-morph__sheet');
  const store = root.querySelector('.card-morph__details');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const canMorph = typeof document.startViewTransition === 'function';
  let opener = null;

  // Enhance: the static details leave the page and open one at a time in the dialog
  store.hidden = true;
  if (!canMorph) dialog.classList.add('card-morph__dialog--fade');

  // view-transition-names exist only during a morph, so cards never collide
  const tag = (scope, on) => {
    [scope, ...scope.querySelectorAll('[data-card-morph-part]')].forEach((el) => {
      if (el.dataset.cardMorphPart) el.style.viewTransitionName = on ? `card-morph-${el.dataset.cardMorphPart}` : '';
    });
  };
  const morph = (from, to, change) => {
    if (!canMorph || reduce.matches) return change();
    tag(from, true);
    const transition = document.startViewTransition(() => { tag(from, false); change(); tag(to, true); });
    transition.finished.finally(() => tag(to, false));
  };

  const open = async (link) => {
    const detail = document.getElementById(link.hash.slice(1));
    if (!detail || dialog.open) return;
    // The hero is the card's photo: decode it first so it never morphs in blank
    const hero = detail.querySelector('.card-morph__hero');
    if (hero) { hero.loading = 'eager'; await hero.decode().catch(() => {}); }
    if (dialog.open) return;
    opener = link;
    morph(link.closest('.card-morph__card'), dialog, () => {
      if (sheet.firstElementChild && sheet.firstElementChild !== detail) store.append(sheet.firstElementChild);
      sheet.append(detail);
      sheet.scrollTop = 0;
      dialog.setAttribute('aria-labelledby', detail.querySelector('.card-morph__heading').id);
      dialog.showModal();
    });
  };

  const close = () => {
    if (!dialog.open) return;
    const done = () => { dialog.close(); opener?.focus(); };
    if (canMorph || reduce.matches) return morph(dialog, opener.closest('.card-morph__card'), done);
    // Fallback exit mirrors the @starting-style entrance
    const ms = parseFloat(getComputedStyle(dialog).getPropertyValue('--dur-3')) || 0;
    dialog.animate({ opacity: [1, 0], scale: [1, 0.96] }, { duration: ms, easing: 'ease-in' }).finished.then(done);
  };

  root.querySelectorAll('.card-morph__link').forEach((link) => link.addEventListener('click', (e) => {
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    e.preventDefault();
    open(link);
  }));
  dialog.addEventListener('cancel', (e) => { e.preventDefault(); close(); });
  dialog.addEventListener('click', (e) => {
    if (e.target === dialog || e.target.closest('.card-morph__close')) close();
  });
});
```

## Notes

- Each card's title is the real link (`<h3><a>`), stretched over the card, with a focus ring drawn on the whole card. The detail opens in a modal `<dialog>` via `showModal()`, labelled by its heading. Focus starts on the close button and stays trapped, the page is inert, and Escape, the close button and a backdrop click all close it with the reverse morph. Focus then returns to the card's link.
- `view-transition-name`s (`card-morph-panel`, `-hero`, `-title`, `-stats`, `-copy`, `-cta`) are set on click and removed when the morph finishes, so no two cards ever share a name. The morphing container keeps an opaque `--surface-light` fill and `--radius-2xl`, so the card-to-panel cross-fade never turns see-through. The hero uses the same file as its card and is decoded before the morph starts, so it never arrives blank.
- Without JS, cards link to `#card-morph-…` anchors and the detail articles render as a static list below the grid, with the target one outlined and a "Back to all projects" link. With JS, that list is `hidden` and each article moves into the dialog on demand.
- Without the View Transitions API, the dialog scales and fades in through `@starting-style` and fades out with a short Web Animations exit. Under reduced motion the morph is skipped, so the dialog opens and closes instantly.
- Contrast on light surfaces: body copy 4.8:1, grey chips 4.6:1, blue chips 5.8:1, the eyebrow 4.9:1, and the CTA's white text 4.9–6.4:1 across its gradient.
- To add a project, pair a card link's `href` with an article `id`, and keep `data-card-morph-part` on the matching image, title, stats, copy and CTA.
