# Focus List

A huge typographic list of services on a deep surface, set in `--font-display` between 2.5 and 5rem. The signature: as you scroll, whichever item crosses the middle of the viewport lights up in gradient type with an arrow sliding in, while its neighbours dim, soften and shrink continuously with distance, so the list reads like a lens racking focus. On desktop a sticky card beside the list previews the lit service (icon tile, starting price, availability chip and a line illustration that draws itself) and springs to the next one with a vertical cross-slide. On phones the card is dropped and the lit item opens a compact price-and-availability row instead. Depends on `tokens/variables.css`.

**Motion:** per-item distance (rAF) drives opacity, blur and scale, retargeted with a short `--dur-2` `--ease-out` transition · lit item: gradient fill fade (`--dur-4`), arrow slide (`--dur-4`, `--ease-spring`), hairline sweep (`--dur-5`) · preview cross-slide (`--dur-4`, `--ease-spring`) with stroke draw-in (`--dur-5`, `--ease-out`) · smooth scroll to centre on keyboard focus · intro hint bobs three times.

## HTML

```html
<div class="focus-list-demo">
  <p class="focus-list-demo__copy">Six jobs we do every single day.</p>
  <p class="focus-list-demo__hint">Scroll slowly
    <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
  </p>
</div>

<section class="focus-list" aria-labelledby="focus-list-title" data-focus-list>
  <div class="focus-list__inner">
    <header class="focus-list__head">
      <p class="focus-list__eyebrow"><span class="focus-list__dot" aria-hidden="true"></span>Services</p>
      <h2 id="focus-list-title" class="focus-list__title">What can we fix today?</h2>
      <p class="focus-list__lead">Upfront prices, licensed technicians and same-day slots across Westlake, Northside and Riverside.</p>
    </header>

    <div class="focus-list__body">
      <div>
        <ul class="focus-list__list" role="list">
          <li class="focus-list__item">
            <a class="focus-list__link" href="#leak-repair">
              <span class="focus-list__num" aria-hidden="true">01</span>
              <span class="focus-list__name">Leak repair</span><span class="focus-list__sr">, from $129, same-day</span>
              <span class="focus-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
              <span class="focus-list__meta" aria-hidden="true">from $129<span class="focus-list__meta-chip">Same-day</span></span>
            </a>
          </li>
          <li class="focus-list__item">
            <a class="focus-list__link" href="#panel-upgrades">
              <span class="focus-list__num" aria-hidden="true">02</span>
              <span class="focus-list__name">Panel upgrades</span><span class="focus-list__sr">, from $1,450, next-day survey</span>
              <span class="focus-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
              <span class="focus-list__meta" aria-hidden="true">from $1,450<span class="focus-list__meta-chip">Next-day</span></span>
            </a>
          </li>
          <li class="focus-list__item">
            <a class="focus-list__link" href="#heat-pumps">
              <span class="focus-list__num" aria-hidden="true">03</span>
              <span class="focus-list__name">Heat pumps</span><span class="focus-list__sr">, from $3,900, free survey</span>
              <span class="focus-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
              <span class="focus-list__meta" aria-hidden="true">from $3,900<span class="focus-list__meta-chip">Free survey</span></span>
            </a>
          </li>
          <li class="focus-list__item">
            <a class="focus-list__link" href="#roof-inspections">
              <span class="focus-list__num" aria-hidden="true">04</span>
              <span class="focus-list__name">Roof inspections</span><span class="focus-list__sr">, from $149, same-day</span>
              <span class="focus-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
              <span class="focus-list__meta" aria-hidden="true">from $149<span class="focus-list__meta-chip">Same-day</span></span>
            </a>
          </li>
          <li class="focus-list__item">
            <a class="focus-list__link" href="#water-heaters">
              <span class="focus-list__num" aria-hidden="true">05</span>
              <span class="focus-list__name">Water heaters</span><span class="focus-list__sr">, from $1,100, same-day</span>
              <span class="focus-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
              <span class="focus-list__meta" aria-hidden="true">from $1,100<span class="focus-list__meta-chip">Same-day</span></span>
            </a>
          </li>
          <li class="focus-list__item">
            <a class="focus-list__link" href="#smart-thermostats">
              <span class="focus-list__num" aria-hidden="true">06</span>
              <span class="focus-list__name">Smart thermostats</span><span class="focus-list__sr">, from $189, same-day</span>
              <span class="focus-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
              <span class="focus-list__meta" aria-hidden="true">from $189<span class="focus-list__meta-chip">Same-day</span></span>
            </a>
          </li>
        </ul>
        <p class="focus-list__foot">Not on the list? <a class="focus-list__call" href="tel:+15555550123">Call (555) 555-0123</a></p>
      </div>

      <div class="focus-list__preview" aria-hidden="true">
        <div class="focus-list__card">
          <div class="focus-list__slide">
            <div class="focus-list__slide-top"><span class="focus-list__tile"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M12 2.7 17.7 8.3a8 8 0 1 1-11.3 0z" /></svg></span><span class="focus-list__count">01 / 06</span></div>
            <p class="focus-list__slide-name">Leak repair</p>
            <div class="focus-list__slide-row"><p class="focus-list__price"><small>from</small>$129</p><span class="focus-list__chip"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></svg>Same-day</span></div>
            <div class="focus-list__art">
              <svg viewBox="0 0 160 96" focusable="false"><path pathLength="1" d="M6 28h148M6 44h148" /><rect pathLength="1" x="66" y="20" width="28" height="32" rx="4" /><path pathLength="1" d="M74 20v32M86 20v32" /><path class="focus-list__hot focus-list__fill" pathLength="1" d="M80 60c-5 7-7 10-7 13a7 7 0 0 0 14 0c0-3-2-6-7-13z" /><path class="focus-list__hot" pathLength="1" d="M58 90h44" /></svg>
            </div>
            <p class="focus-list__note">Average visit 1–2 h · 1-year warranty</p>
          </div>
          <div class="focus-list__slide">
            <div class="focus-list__slide-top"><span class="focus-list__tile"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z" /></svg></span><span class="focus-list__count">02 / 06</span></div>
            <p class="focus-list__slide-name">Panel upgrades</p>
            <div class="focus-list__slide-row"><p class="focus-list__price"><small>from</small>$1,450</p><span class="focus-list__chip focus-list__chip--blue"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></svg>Next-day</span></div>
            <div class="focus-list__art">
              <svg viewBox="0 0 160 96" focusable="false"><rect pathLength="1" x="40" y="6" width="68" height="84" rx="8" /><path class="focus-list__bold" pathLength="1" d="M52 22h16M80 22h16M52 38h16M80 38h16M52 54h16M80 54h16M52 70h16M80 70h16" /><path class="focus-list__hot focus-list__fill" pathLength="1" d="M134 16 122 42h10l-4 24 16-30h-10l6-20z" /></svg>
            </div>
            <p class="focus-list__note">Up to 200 A · permit and inspection included</p>
          </div>
          <div class="focus-list__slide">
            <div class="focus-list__slide-top"><span class="focus-list__tile"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M9.6 4.6A2 2 0 1 1 11 8H2m10.6 11.4A2 2 0 1 0 14 16H2m15.7-8.3A2.5 2.5 0 1 1 19.5 12H2" /></svg></span><span class="focus-list__count">03 / 06</span></div>
            <p class="focus-list__slide-name">Heat pumps</p>
            <div class="focus-list__slide-row"><p class="focus-list__price"><small>from</small>$3,900</p><span class="focus-list__chip focus-list__chip--teal"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></svg>Free survey</span></div>
            <div class="focus-list__art">
              <svg viewBox="0 0 160 96" focusable="false"><rect pathLength="1" x="16" y="12" width="128" height="66" rx="10" /><circle pathLength="1" cx="58" cy="45" r="24" /><path class="focus-list__hot" pathLength="1" d="M58 41c-2-9 2-15 9-15M62 45c9-2 15 2 15 9M58 49c2 9-2 15-9 15M54 45c-9 2-15-2-15-9" /><path pathLength="1" d="M98 30h32M98 40h32M98 50h32M98 60h32M32 78v8M128 78v8" /></svg>
            </div>
            <p class="focus-list__note">Rebates applied on the quote · 10-year parts</p>
          </div>
          <div class="focus-list__slide">
            <div class="focus-list__slide-top"><span class="focus-list__tile"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" /><path d="M9 22V12h6v10" /></svg></span><span class="focus-list__count">04 / 06</span></div>
            <p class="focus-list__slide-name">Roof inspections</p>
            <div class="focus-list__slide-row"><p class="focus-list__price"><small>from</small>$149</p><span class="focus-list__chip"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></svg>Same-day</span></div>
            <div class="focus-list__art">
              <svg viewBox="0 0 160 96" focusable="false"><path pathLength="1" d="M10 54 62 16l52 38" /><path pathLength="1" d="M22 46v42h80V46M52 88V66h20v22M90 36V20h10v24" /><circle class="focus-list__hot" pathLength="1" cx="124" cy="58" r="15" /><path class="focus-list__hot" pathLength="1" d="m135 69 13 13M117 58l5 5 9-10" /></svg>
            </div>
            <p class="focus-list__note">Drone photos and a written report</p>
          </div>
          <div class="focus-list__slide">
            <div class="focus-list__slide-top"><span class="focus-list__tile"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4.1 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3a2.5 2.5 0 0 0 2.5 2.5z" /></svg></span><span class="focus-list__count">05 / 06</span></div>
            <p class="focus-list__slide-name">Water heaters</p>
            <div class="focus-list__slide-row"><p class="focus-list__price"><small>from</small>$1,100</p><span class="focus-list__chip"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></svg>Same-day</span></div>
            <div class="focus-list__art">
              <svg viewBox="0 0 160 96" focusable="false"><path pathLength="1" d="M70 10V2M90 10V2" /><rect pathLength="1" x="58" y="10" width="44" height="80" rx="16" /><circle pathLength="1" cx="80" cy="34" r="8" /><path pathLength="1" d="m80 34 5-4" /><path class="focus-list__hot focus-list__fill" pathLength="1" d="M80 82c-5 0-8-3-8-7 0-5 5-7 6-12 3 3 4 5 4 8 1-1 2-3 2-4 3 2 4 5 4 8 0 4-3 7-8 7z" /><path class="focus-list__hot" pathLength="1" d="M38 34c-5 5 5 9 0 14s5 9 0 14M122 34c-5 5 5 9 0 14s5 9 0 14" /></svg>
            </div>
            <p class="focus-list__note">Tank or tankless · old unit hauled away</p>
          </div>
          <div class="focus-list__slide">
            <div class="focus-list__slide-top"><span class="focus-list__tile"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M14 14.8V4a2 2 0 0 0-4 0v10.8a4 4 0 1 0 4 0z" /></svg></span><span class="focus-list__count">06 / 06</span></div>
            <p class="focus-list__slide-name">Smart thermostats</p>
            <div class="focus-list__slide-row"><p class="focus-list__price"><small>from</small>$189</p><span class="focus-list__chip"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></svg>Same-day</span></div>
            <div class="focus-list__art">
              <svg viewBox="0 0 160 96" focusable="false"><circle pathLength="1" cx="80" cy="48" r="40" /><path pathLength="1" d="M58.8 69.2A30 30 0 1 1 101.2 69.2" /><path class="focus-list__hot focus-list__arc" pathLength="1" d="M58.8 69.2A30 30 0 1 1 106 33" /><circle class="focus-list__hot focus-list__fill" pathLength="1" cx="106" cy="33" r="4" /><text x="80" y="56" text-anchor="middle">21°</text></svg>
            </div>
            <p class="focus-list__note">Fitted in about an hour · app set up for you</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="focus-list-demo">
  <p class="focus-list-demo__copy">Every price is fixed before we start.</p>
  <p class="focus-list-demo__hint">Scroll back up to refocus</p>
</div>
```

## CSS

```css
/* Demo scroll room above and below */
.focus-list-demo {
  display: grid; place-content: center; justify-items: center; gap: 0.875rem; min-height: 70vh; padding: 3rem var(--gutter);
  background: var(--surface-deep); color: var(--text-inverse-muted); font-family: var(--font-sans); text-align: center;
}
.focus-list-demo__copy { margin: 0; color: var(--text-inverse); font: 600 clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.focus-list-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.focus-list-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: focus-list-bob 1.4s var(--ease-in-out) 600ms 3; }

/* Section: deep surface, brand light behind the preview */
.focus-list { position: relative; isolation: isolate; overflow: clip; background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans); }
.focus-list::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background:
    radial-gradient(40% 35% at 85% 35%, color-mix(in srgb, var(--primary) 22%, transparent), transparent 70%),
    radial-gradient(45% 35% at 10% 85%, color-mix(in srgb, var(--primary-2) 14%, transparent), transparent 70%);
}
.focus-list__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.focus-list__head { max-width: 38rem; margin-bottom: clamp(2rem, 5vw, 3.5rem); }
.focus-list__eyebrow { display: flex; align-items: center; gap: 0.625rem; margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.focus-list__dot { flex: none; width: 0.5rem; height: 0.5rem; border-radius: var(--radius-full); background: var(--gradient-brand); box-shadow: 0 0 0.75rem color-mix(in srgb, var(--primary-2) 80%, transparent); }
.focus-list__title { margin: 0.875rem 0 0; font: 600 clamp(1.875rem, 1.3rem + 2.2vw, 2.75rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.focus-list__lead { margin: 1rem 0 0; color: var(--text-inverse-muted); font-size: 1.0625rem; line-height: 1.6; }
.focus-list__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }

/* The list: ruled rows; the lit row's hairline sweeps in with the brand gradient */
.focus-list__list { position: relative; container-type: inline-size; margin: 0; padding: 0; list-style: none; }
.focus-list__item { position: relative; border-top: 1px solid var(--border-inverse); }
.focus-list__item:last-child { border-bottom: 1px solid var(--border-inverse); }
.focus-list__item::before {
  content: ""; position: absolute; inset: -1px 0 auto; height: 1px; pointer-events: none;
  background: linear-gradient(90deg, var(--primary), var(--primary-2) 45%, transparent);
  transform: scaleX(0); transform-origin: left; transition: transform var(--dur-5) var(--ease-out);
}
.focus-list__item.is-active::before { transform: scaleX(1); }
.focus-list__link {
  position: relative; display: grid; grid-template-columns: 1.75rem minmax(0, 1fr); align-items: center; gap: 0.5rem clamp(0.75rem, 2vw, 1.5rem);
  padding-block: 1rem; color: var(--text-inverse); text-decoration: none; transform-origin: left center;
}
.focus-list__link:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; border-radius: var(--radius-md); }
.focus-list__num { align-self: start; margin-top: 0.625rem; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.06em; transition: color var(--dur-3) var(--ease-out); }
.focus-list__item.is-active .focus-list__num { color: color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse)); }

/* Names: the gradient is always there; lighting an item fades its solid fill away to reveal it */
.focus-list__name {
  justify-self: start; padding-bottom: 0.06em;
  font-family: var(--font-display); font-weight: 600; line-height: 1; letter-spacing: var(--tracking-display); text-wrap: balance;
  font-size: clamp(2.5rem, 1.6rem + 3.4vw, 4.25rem); font-size: clamp(2.5rem, 8.6cqi, 5rem);
  background: linear-gradient(95deg, var(--text-inverse) 5%, color-mix(in srgb, var(--primary) 45%, var(--text-inverse)) 50%, color-mix(in srgb, var(--primary-2) 75%, var(--text-inverse)) 95%);
  -webkit-background-clip: text; background-clip: text; color: var(--text-inverse);
  transition: color var(--dur-4) var(--ease-out);
}
.focus-list__item.is-active .focus-list__name { color: transparent; }
.focus-list__arrow {
  grid-row: 2; grid-column: 2; justify-self: end; display: grid; place-items: center; width: 2.25rem; aspect-ratio: 1; border-radius: var(--radius-full);
  background: var(--gradient-brand); color: var(--text-inverse); box-shadow: var(--highlight-inverse), var(--shadow-glow);
  opacity: 0; translate: -0.75rem 0; scale: 0.7;
  transition: opacity var(--dur-3) var(--ease-out), translate var(--dur-4) var(--ease-spring), scale var(--dur-4) var(--ease-spring);
}
.focus-list__arrow svg { fill: none; stroke: currentColor; stroke-width: 2.25; stroke-linecap: round; stroke-linejoin: round; }
.focus-list__item.is-active .focus-list__arrow, .focus-list__link:is(:hover, :focus-visible) .focus-list__arrow { opacity: 1; translate: 0 0; scale: 1; }

/* Phones and tablets: the lit item opens a compact price row (a visual duplicate of the sr text) */
.focus-list__meta {
  grid-row: 2; grid-column: 2; justify-self: start; display: flex; align-items: center; gap: 0.625rem; height: 1.5rem;
  color: var(--text-inverse-muted); font: 500 0.8125rem var(--font-mono);
  opacity: 0; translate: 0 0.375rem; transition: opacity var(--dur-3) var(--ease-out), translate var(--dur-4) var(--ease-spring);
}
.focus-list__meta-chip { padding: 0.125rem 0.5rem; border-radius: var(--radius-full); background: color-mix(in srgb, var(--success) 26%, transparent); color: var(--text-inverse); font-size: 0.6875rem; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; }
.focus-list__item.is-active .focus-list__meta, .focus-list:not(.focus-list--js) .focus-list__meta { opacity: 1; translate: 0 0; }

/* Focus by distance: JS writes --focus-list-d (0 on the centre line, 1 far away) on each item */
.focus-list--js .focus-list__link {
  opacity: calc(1 - var(--focus-list-d, 0) * 0.62);
  filter: blur(calc(var(--focus-list-d, 0) * 4px));
  scale: calc(1 - var(--focus-list-d, 0) * 0.06);
  transition: opacity var(--dur-2) var(--ease-out), filter var(--dur-2) var(--ease-out), scale var(--dur-2) var(--ease-out);
}
.focus-list--js .focus-list__link:is(:hover, :focus-visible) { opacity: 1; filter: none; scale: 1; }

.focus-list__foot { margin: 1.75rem 0 0; color: var(--text-inverse-muted); font-size: 0.9375rem; }
.focus-list__call {
  color: var(--text-inverse); font-weight: 600; text-decoration: underline; text-decoration-thickness: 2px; text-decoration-color: color-mix(in srgb, var(--primary-2) 70%, transparent); text-underline-offset: 0.25em;
  transition: text-decoration-color var(--dur-2) var(--ease-out);
}
.focus-list__call:hover { text-decoration-color: var(--text-inverse); }
.focus-list__call:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; border-radius: var(--radius-sm); }

/* Preview card (desktop, JS only): slides stack in one cell and cross-slide vertically */
.focus-list__preview { display: none; }
.focus-list__card {
  position: sticky; top: max(1.5rem, calc(50vh - 12.5rem)); display: grid; overflow: clip; padding: 1.5rem; border-radius: var(--radius-2xl);
  background: linear-gradient(160deg, color-mix(in srgb, var(--text-inverse) 8%, transparent), color-mix(in srgb, var(--text-inverse) 3%, transparent));
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 40px 80px -32px color-mix(in srgb, var(--surface-deep) 90%, transparent), 0 0 90px -40px color-mix(in srgb, var(--primary) 70%, transparent);
}
.focus-list__slide {
  grid-area: 1 / 1; display: grid; align-content: start; gap: 1rem;
  opacity: 0; translate: 0 2.5rem; scale: 0.96; filter: blur(6px); visibility: hidden;
  transition: opacity var(--dur-3) var(--ease-out), translate var(--dur-4) var(--ease-spring), scale var(--dur-4) var(--ease-spring), filter var(--dur-3) var(--ease-out), visibility 0s linear var(--dur-4);
}
.focus-list__slide.is-before { translate: 0 -2.5rem; }
.focus-list__slide.is-active { opacity: 1; translate: 0 0; scale: 1; filter: none; visibility: visible; transition-delay: 0s; }
.focus-list__slide-top { display: flex; align-items: center; justify-content: space-between; }
.focus-list__tile {
  display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: var(--radius-xl); background: var(--gradient-brand); color: var(--text-inverse);
  box-shadow: var(--highlight-inverse), 0 12px 28px -12px color-mix(in srgb, var(--primary) 90%, transparent);
}
.focus-list__tile svg, .focus-list__chip svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.focus-list__count { color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; }
.focus-list__slide-name { margin: 0.25rem 0 0; font: 600 1.625rem/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.focus-list__slide-row { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem; }
.focus-list__price { display: flex; align-items: baseline; gap: 0.375rem; margin: 0; font: 600 2.25rem/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }
.focus-list__price small { color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.focus-list__chip {
  display: inline-flex; align-items: center; gap: 0.375rem; padding: 0.3125rem 0.625rem; border-radius: var(--radius-full); font-size: 0.75rem; font-weight: 600;
  background: color-mix(in srgb, var(--success) 26%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--success) 50%, transparent);
}
.focus-list__chip--blue { background: color-mix(in srgb, var(--primary) 30%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 60%, transparent); }
.focus-list__chip--teal { background: color-mix(in srgb, var(--primary-2) 28%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 60%, transparent); }

/* Illustration board: brand light, dot grid, strokes that draw in when their slide arrives */
.focus-list__art {
  display: grid; place-items: center; height: 8.5rem; padding: 0.75rem; border-radius: var(--radius-xl);
  background:
    radial-gradient(60% 80% at 15% 0%, color-mix(in srgb, var(--primary) 30%, transparent), transparent 70%),
    radial-gradient(60% 80% at 100% 100%, color-mix(in srgb, var(--primary-2) 26%, transparent), transparent 70%),
    radial-gradient(circle, color-mix(in srgb, var(--text-inverse) 10%, transparent) 1px, transparent 1.5px) 0 0 / 14px 14px,
    color-mix(in srgb, var(--surface-deep) 70%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse);
}
.focus-list__art svg { width: 100%; max-width: 13rem; height: 100%; fill: none; stroke: color-mix(in srgb, var(--text-inverse) 72%, transparent); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
.focus-list__art :is(path, rect, circle) { stroke-dasharray: 1; }
.focus-list__art .focus-list__hot { stroke: color-mix(in srgb, var(--primary-2) 60%, var(--text-inverse)); }
.focus-list__art .focus-list__fill { fill: color-mix(in srgb, var(--primary-2) 30%, transparent); }
.focus-list__art .focus-list__bold { stroke-width: 6; }
.focus-list__art .focus-list__arc { stroke-width: 5; }
.focus-list__art text { fill: var(--text-inverse); stroke: none; font: 600 1.375rem var(--font-display); letter-spacing: -0.03em; }
.focus-list__slide.is-active .focus-list__art :is(path, rect, circle) { animation: focus-list-draw var(--dur-5) var(--ease-out) 120ms both; }
.focus-list__note { margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1.5 var(--font-mono); }

/* From 768px the arrow moves up beside the name; on phones it shares the reveal row so names get the full width */
@media (min-width: 768px) {
  .focus-list__link { grid-template-columns: 1.75rem minmax(0, 1fr) auto; padding-block: 1.25rem; }
  .focus-list__arrow { grid-row: 1; grid-column: 3; justify-self: auto; width: clamp(2.5rem, 1.9rem + 1.6vw, 3.5rem); }
}
@media (min-width: 1024px) {
  .focus-list--js .focus-list__body { display: grid; grid-template-columns: minmax(0, 1.55fr) minmax(19rem, 1fr); gap: clamp(2.5rem, 5vw, 4.5rem); }
  .focus-list--js .focus-list__preview { display: block; }
  .focus-list--js .focus-list__meta { display: none; }
}

/* Reduced motion: no fade, blur or scale; the lit item keeps its gradient against muted neighbours */
@media (prefers-reduced-motion: reduce) {
  .focus-list--js .focus-list__link { opacity: 1; filter: none; scale: none; }
  .focus-list--js .focus-list__name { color: var(--text-inverse-muted); }
  .focus-list *, .focus-list *::before, .focus-list *::after,
  .focus-list-demo *, .focus-list-demo *::before, .focus-list-demo *::after { animation: none !important; }
}
@keyframes focus-list-draw { from { stroke-dashoffset: 1; } }
@keyframes focus-list-bob { 50% { transform: translateY(4px); } }
```

## JS

```js
document.querySelectorAll('[data-focus-list]').forEach((root) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const list = root.querySelector('.focus-list__list');
  const items = [...list.querySelectorAll('.focus-list__item')];
  const slides = [...root.querySelectorAll('.focus-list__slide')];
  let near = false, frame = 0, active = -1, centers = [];
  root.classList.add('focus-list--js');

  // Light one item and its preview slide; slides before it exit upward, slides after it wait below
  const setActive = (index) => {
    if (index === active) return;
    active = index;
    items.forEach((item, n) => item.classList.toggle('is-active', n === index));
    slides.forEach((slide, n) => {
      slide.classList.toggle('is-active', n === index);
      slide.classList.toggle('is-before', n < index);
    });
  };

  // Distance from the viewport's centre line: 0 on it, 1 at `reach` px or more. CSS turns it into fade, blur and scale
  const update = () => {
    frame = 0;
    const top = list.getBoundingClientRect().top;
    const mid = innerHeight / 2;
    const reach = Math.max(220, innerHeight * 0.38);
    let best = 0, bestGap = Infinity;
    centers.forEach((center, n) => {
      const gap = Math.abs(top + center - mid);
      if (gap < bestGap) { best = n; bestGap = gap; }
      items[n].style.setProperty('--focus-list-d', Math.min(1, gap / reach).toFixed(3));
    });
    setActive(best);
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(update); };

  // Item centres are layout positions (offsetTop ignores the scale), so they're measured only on resize
  const measure = () => {
    centers = items.map((item) => item.offsetTop + item.offsetHeight / 2);
    update();
  };

  // Keyboard focus brings its item to the centre line, which lights it and swaps the preview
  list.addEventListener('focusin', (e) => {
    if (!e.target.matches(':focus-visible')) return;
    e.target.closest('.focus-list__item').scrollIntoView({ block: 'center', behavior: reduce.matches ? 'auto' : 'smooth' });
  });

  new IntersectionObserver(([entry]) => { near = entry.isIntersecting; queue(); }, { rootMargin: '10% 0px' }).observe(root);
  addEventListener('scroll', queue, { passive: true });
  new ResizeObserver(measure).observe(list);
  measure();
});
```

## Notes

- Every item is a real link whose text is the service name plus a visually hidden ", from $129, same-day", so the list reads the same however it's lit. The numbers, arrows, phone price rows and the whole preview card are visual duplicates and are `aria-hidden`. Keyboard focus scrolls its item to the centre line (smoothly unless reduced motion), which lights it and swaps the preview; hover and focus also bring any item back to full clarity.
- Distance is continuous: the item nearest the centre line is lit, and every item's opacity, blur and scale follow its own distance. A 200 ms retargeting transition smooths scroll jitter. Item centres come from `offsetTop`, so they're measured on resize only and each frame costs one `getBoundingClientRect`.
- Without JS, all items render at full strength, the price rows show under every name and the preview stays hidden. With `prefers-reduced-motion` there's no fade, blur or scale: the lit item keeps its gradient and neighbours drop to `--text-inverse-muted` (7:1). The preview swaps and stroke draws become instant.
- Contrast on `--surface-deep`: names in `--text-inverse` 18:1, and the gradient's darkest stop is ≥ 7.8:1. The dimmest neighbours bottom out at 38% opacity, about 3:1, the large-text minimum (names are ≥ 40px), and focus, hover or centring restores full contrast. Preview text sits on an 8% white glass card: ≥ 15:1 for `--text-inverse`, ≥ 6.5:1 for the muted labels.
- Name size scales with the list's width (`8.6cqi`, clamped 2.5–5rem, with a `vw` fallback) so "Smart thermostats" stays on one line beside the preview. Long names wrap and stay balanced on phones.
- Adapting: add or remove items and slides in matching order (the nth slide previews the nth item). Each illustration is a 160×96 line drawing whose shapes carry `pathLength="1"`; mark accent strokes with `focus-list__hot`.
