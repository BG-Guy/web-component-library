# Live Job Tracker

A "your technician is on the way" card on a light surface: on a stylised map of streets, a park and a river, a van drives its route (`offset-path`) toward the home pin, drawing the route behind it. The ETA rolls down minute by minute while a five-stage stepper fills its line and draws each check; the demo picks up mid-journey, plays through to Done, and has Pause and Restart controls. On phones the map runs edge to edge and the panel stacks, with the stepper as a vertical timeline. Depends on `tokens/variables.css`.

**Motion:** van along `offset-path` with eased driving (rAF, paused off-screen) · route draw-in (`stroke-dasharray`) · ETA roll (translate + blur) · stepper line fill (`--dur-5`, `--ease-out`) and check draw (`--dur-4`) · home-pin pulse and current-step ring (2.4s loops, pausable) · completion card rise (`--ease-spring`).

## HTML

```html
<section class="job-tracker" aria-labelledby="job-tracker-title" data-job-tracker data-stage="2" data-start-stage="2" data-start-t="0.4" style="--job-tracker-progress: 0.256; --job-tracker-sub: 0.4">
  <div class="job-tracker__inner">
    <div class="job-tracker__card">
      <header class="job-tracker__head">
        <div>
          <p class="job-tracker__eyebrow">Job #4821 · Leak repair · 14 Birch Ct, Westlake</p>
          <h2 id="job-tracker-title" class="job-tracker__title">Track your visit</h2>
          <p class="job-tracker__status" role="status">Sam is on the way. We'll text when he's 5 minutes out.</p>
        </div>
        <div class="job-tracker__controls">
          <button class="job-tracker__ctl job-tracker__pause" type="button" aria-pressed="false" hidden>
            <svg class="job-tracker__icon-pause" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
            <svg class="job-tracker__icon-play" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
            Pause<span class="job-tracker__sr"> live demo</span>
          </button>
          <button class="job-tracker__ctl job-tracker__restart" type="button" hidden>
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M3 12a9 9 0 1 0 3-6.7L3 8" /><path d="M3 3v5h5" /></svg>
            Restart<span class="job-tracker__sr"> demo</span>
          </button>
        </div>
      </header>

      <div class="job-tracker__body">
        <div class="job-tracker__map" aria-hidden="true">
          <svg class="job-tracker__svg" viewBox="0 0 400 260" focusable="false">
            <rect class="job-tracker__land" width="400" height="260" />
            <g class="job-tracker__blocks">
              <rect x="-8" y="-8" width="56" height="101" rx="8" /><rect x="-8" y="117" width="56" height="76" rx="8" /><rect x="-8" y="217" width="56" height="51" rx="8" />
              <rect x="72" y="-8" width="66" height="101" rx="8" /><rect x="72" y="117" width="66" height="76" rx="8" /><rect x="72" y="217" width="66" height="51" rx="8" />
              <rect x="162" y="-8" width="52" height="101" rx="8" /><rect x="162" y="217" width="80" height="51" rx="8" />
              <rect x="262" y="-8" width="56" height="101" rx="8" /><rect x="282" y="117" width="36" height="76" rx="8" /><rect x="292" y="217" width="26" height="51" rx="6" />
              <rect x="342" y="-8" width="66" height="54" rx="8" /><rect x="342" y="70" width="66" height="23" rx="6" /><rect x="342" y="117" width="66" height="76" rx="8" /><rect x="342" y="217" width="66" height="51" rx="8" />
            </g>
            <rect class="job-tracker__park" x="162" y="117" width="60" height="76" rx="10" />
            <g class="job-tracker__trees">
              <circle cx="176" cy="132" r="6" /><circle cx="192" cy="128" r="4.5" /><circle cx="207" cy="136" r="6.5" /><circle cx="180" cy="153" r="4" />
              <circle cx="211" cy="158" r="4.5" /><circle cx="174" cy="178" r="5.5" /><circle cx="196" cy="182" r="4" /><circle cx="210" cy="177" r="3.5" />
            </g>
            <path class="job-tracker__river" d="M228 -10C262 50 214 118 256 168S282 236 266 272" />
            <path class="job-tracker__ripple" d="M228 -10C262 50 214 118 256 168S282 236 266 272" />
            <path class="job-tracker__road-case job-tracker__road-case--minor" d="M60 0V260M150 0V260M330 0V260M330 58H376" />
            <path class="job-tracker__road-case" d="M0 105H400M0 205H400" />
            <path class="job-tracker__road job-tracker__road--minor" d="M60 0V260M150 0V260M330 0V260M330 58H376" />
            <path class="job-tracker__road" d="M0 105H400M0 205H400" />
            <circle class="job-tracker__culdesac" cx="378" cy="58" r="8" />
            <text class="job-tracker__label" x="76" y="208">MAIN ST</text>
            <text class="job-tracker__label" x="6" y="108">ELM ST</text>
            <text class="job-tracker__label" transform="translate(153 52) rotate(-90)" text-anchor="middle">OAK AVE</text>
            <text class="job-tracker__label" transform="translate(63 160) rotate(-90)" text-anchor="middle">PINE AVE</text>
            <text class="job-tracker__label" transform="translate(333 160) rotate(-90)" text-anchor="middle">LAKE RD</text>
            <text class="job-tracker__label job-tracker__label--park" x="192" y="168" text-anchor="middle">PARK</text>
            <text class="job-tracker__label job-tracker__label--water" transform="translate(246 36) rotate(70)">Mill River</text>
            <path class="job-tracker__route-base" d="M36 205H138Q150 205 150 193V117Q150 105 162 105H318Q330 105 330 93V70Q330 58 342 58H352" />
            <path class="job-tracker__route-glow" d="M36 205H138Q150 205 150 193V117Q150 105 162 105H318Q330 105 330 93V70Q330 58 342 58H352" pathLength="1" />
            <path class="job-tracker__route-done" d="M36 205H138Q150 205 150 193V117Q150 105 162 105H318Q330 105 330 93V70Q330 58 342 58H352" pathLength="1" />
            <g transform="translate(36 205)">
              <circle class="job-tracker__depot" r="7" /><circle class="job-tracker__depot-core" r="2.5" />
            </g>
            <text class="job-tracker__label job-tracker__label--strong" x="20" y="229">BRAND HQ</text>
            <g class="job-tracker__home" transform="translate(352 58)">
              <circle class="job-tracker__pulse" r="13" /><circle class="job-tracker__pulse" r="13" />
              <path class="job-tracker__pin" d="M0 0C-1-6-10-10-10-17A10 10 0 0 1 10-17C10-10 1-6 0 0Z" />
              <path class="job-tracker__pin-house" d="M-4.5-16.5 0-20.5 4.5-16.5V-12H-4.5Z" />
            </g>
            <text class="job-tracker__label job-tracker__label--strong" x="345" y="84">HOME</text>
          </svg>
          <div class="job-tracker__layer">
            <span class="job-tracker__van" style="offset-path: path('M36 205H138Q150 205 150 193V117Q150 105 162 105H318Q330 105 330 93V70Q330 58 342 58H352')"><span class="job-tracker__van-body"></span></span>
          </div>
          <span class="job-tracker__chip"><span class="job-tracker__chip-dot"></span>Live · Westlake</span>
        </div>

        <div class="job-tracker__side">
          <p class="job-tracker__eta">
            <span class="job-tracker__eta-label">Arriving in · ETA 2:07 PM</span>
            <span class="job-tracker__eta-clip"><strong class="job-tracker__eta-value">8<small>min</small></strong></span>
          </p>

          <div class="job-tracker__tech">
            <span class="job-tracker__avatar" aria-hidden="true">SK</span>
            <div class="job-tracker__who">
              <p class="job-tracker__name">Sam Kowalski</p>
              <p class="job-tracker__meta">
                <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
                <span><span class="job-tracker__sr">Rated </span>4.9<span class="job-tracker__sr"> out of 5</span> · 312 jobs</span>
              </p>
              <p class="job-tracker__vehicle">White Ford Transit <span class="job-tracker__plate">7KLM 204</span></p>
            </div>
            <div class="job-tracker__contact">
              <a class="job-tracker__icon-btn" href="tel:+15555550123">
                <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
                <span class="job-tracker__btn-text">Call Sam</span>
              </a>
              <a class="job-tracker__icon-btn" href="sms:+15555550123">
                <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" /></svg>
                <span class="job-tracker__btn-text">Message Sam</span>
              </a>
            </div>
          </div>

          <ol class="job-tracker__steps" role="list" aria-label="Job progress">
            <li class="job-tracker__step is-done" data-ms="1600" data-min="25" data-say="Your visit is booked for today, 1 to 3 PM.">
              <span class="job-tracker__node" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg></span>
              <span class="job-tracker__step-label">Booked<span class="job-tracker__sr job-tracker__state">, completed</span></span>
              <span class="job-tracker__time">1:20 PM</span>
            </li>
            <li class="job-tracker__step is-done" data-ms="2200" data-min="10" data-say="Sam K. is assigned and loading the van.">
              <span class="job-tracker__node" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg></span>
              <span class="job-tracker__step-label">Assigned<span class="job-tracker__sr job-tracker__state">, completed</span></span>
              <span class="job-tracker__time">1:45 PM</span>
            </li>
            <li class="job-tracker__step is-current" aria-current="step" data-ms="12000" data-min="12" data-say="Sam is on the way. We'll text when he's 5 minutes out.">
              <span class="job-tracker__node" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg></span>
              <span class="job-tracker__step-label">On the way<span class="job-tracker__sr job-tracker__state"></span></span>
              <span class="job-tracker__time">1:55 PM</span>
            </li>
            <li class="job-tracker__step" data-ms="5000" data-min="35" data-say="Sam has arrived and started work.">
              <span class="job-tracker__node" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg></span>
              <span class="job-tracker__step-label">Working<span class="job-tracker__sr job-tracker__state"></span></span>
              <span class="job-tracker__time"></span>
            </li>
            <li class="job-tracker__step" data-say="All done. Your invoice is ready.">
              <span class="job-tracker__node" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg></span>
              <span class="job-tracker__step-label">Done<span class="job-tracker__sr job-tracker__state"></span></span>
              <span class="job-tracker__time"></span>
            </li>
          </ol>

          <div class="job-tracker__done" hidden>
            <p><strong>Job complete.</strong> Invoice #1042 · $149, paid by card.</p>
            <a class="job-tracker__done-link" href="#review">Rate your visit</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section and card */
.job-tracker {
  --job-tracker-pad: 1rem;
  --job-tracker-grad: linear-gradient(135deg, var(--primary), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
  background:
    radial-gradient(50% 45% at 0% 0%, color-mix(in srgb, var(--primary) 9%, transparent), transparent 70%),
    radial-gradient(45% 45% at 100% 100%, color-mix(in srgb, var(--primary-2) 10%, transparent), transparent 70%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
.job-tracker__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(3rem, 8vw, 6rem) var(--gutter); }
:where(.job-tracker) svg:not(.job-tracker__svg) { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.job-tracker :is(a, button):focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.job-tracker__card {
  position: relative; padding: var(--job-tracker-pad); border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}

/* Header: title, live status line, demo controls */
.job-tracker__head { display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 1rem 1.5rem; margin-bottom: 1.25rem; padding: 0.25rem 0.25rem 0; }
.job-tracker__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.04em; }
.job-tracker__title { margin: 0.5rem 0 0; font: 600 clamp(1.75rem, 1.3rem + 1.8vw, 2.5rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); }
.job-tracker__status { max-width: 34rem; margin: 0.625rem 0 0; color: var(--text-muted); font-size: 1rem; line-height: 1.5; }
.job-tracker__controls { display: flex; gap: 0.5rem; }
.job-tracker__ctl {
  display: inline-flex; align-items: center; gap: 0.375rem; height: 2.5rem; padding: 0 0.875rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--surface-muted); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle); font: 600 0.8125rem var(--font-sans);
  transition: background-color var(--dur-2), color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.job-tracker__ctl[hidden] { display: none; }
.job-tracker__ctl:hover { background: var(--border-subtle); }
.job-tracker__ctl:active { transform: scale(0.96); }
.job-tracker__pause svg { fill: currentColor; }
.job-tracker__icon-play, .job-tracker__pause[aria-pressed="true"] .job-tracker__icon-pause { display: none; }
.job-tracker__pause[aria-pressed="true"] .job-tracker__icon-play { display: block; }
.job-tracker__pause[aria-pressed="true"] { background: var(--text-main); color: var(--surface-light); box-shadow: none; }

.job-tracker__body { display: grid; gap: 1.25rem; }

/* Map: SVG streets in a 400×260 space; the van rides an HTML layer scaled to the same space */
.job-tracker__map {
  position: relative; container-type: inline-size; aspect-ratio: 400 / 260; overflow: hidden;
  margin-inline: calc(var(--job-tracker-pad) * -1); background: color-mix(in srgb, var(--primary-2) 7%, var(--surface-muted));
}
.job-tracker__map::after { content: ""; position: absolute; inset: 0; border-radius: inherit; box-shadow: inset 0 1px 0 var(--border-subtle), inset 0 -1px 0 var(--border-subtle); pointer-events: none; }
.job-tracker__svg { display: block; width: 100%; height: 100%; }
.job-tracker__land { fill: color-mix(in srgb, var(--primary-2) 7%, var(--surface-muted)); }
.job-tracker__blocks { fill: color-mix(in srgb, var(--surface-light) 75%, transparent); }
.job-tracker__park { fill: color-mix(in srgb, var(--primary-2) 20%, var(--surface-light)); }
.job-tracker__trees { fill: color-mix(in srgb, var(--primary-2) 38%, var(--surface-light)); }
.job-tracker__river { fill: none; stroke: color-mix(in srgb, var(--primary) 20%, var(--surface-light)); stroke-width: 26; stroke-linecap: round; }
.job-tracker__ripple { fill: none; stroke: color-mix(in srgb, var(--surface-light) 70%, transparent); stroke-width: 1.5; stroke-dasharray: 5 9; stroke-linecap: round; }
.job-tracker__road-case { fill: none; stroke: var(--border-subtle); stroke-width: 15; }
.job-tracker__road { fill: none; stroke: var(--surface-light); stroke-width: 12; }
.job-tracker__road-case--minor { stroke-width: 11; }
.job-tracker__road--minor { stroke-width: 8; }
.job-tracker__culdesac { fill: var(--surface-light); }
.job-tracker__label { fill: color-mix(in srgb, var(--text-muted) 75%, transparent); font: 600 7px var(--font-mono); letter-spacing: 0.14em; }
.job-tracker__label--park { fill: color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)); }
.job-tracker__label--water { fill: color-mix(in srgb, var(--primary) 55%, var(--surface-light)); font: italic 500 8px var(--font-sans); letter-spacing: 0.04em; }
.job-tracker__label--strong { fill: var(--text-main); }

/* Route: a dotted plan, then a solid line drawn up to the van */
.job-tracker__route-base { fill: none; stroke: color-mix(in srgb, var(--primary) 50%, transparent); stroke-width: 2.5; stroke-dasharray: 0.5 6; stroke-linecap: round; }
.job-tracker__route-glow, .job-tracker__route-done { fill: none; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: var(--job-tracker-progress, 0) 1; }
.job-tracker__route-glow { stroke: color-mix(in srgb, var(--primary) 20%, transparent); stroke-width: 11; }
.job-tracker__route-done { stroke: var(--primary); stroke-width: 4; }
.job-tracker__depot { fill: var(--text-main); stroke: var(--surface-light); stroke-width: 2.5; }
.job-tracker__depot-core { fill: var(--surface-light); }
.job-tracker__pin { fill: var(--primary); stroke: var(--surface-light); stroke-width: 2; }
.job-tracker__pin-house { fill: var(--surface-light); }
.job-tracker__pulse { fill: color-mix(in srgb, var(--primary) 30%, transparent); opacity: 0; transform-box: fill-box; transform-origin: center; }
.job-tracker--js[data-stage="2"] .job-tracker__pulse { animation: job-tracker-pulse 2.4s var(--ease-out) infinite; }
.job-tracker--js[data-stage="2"] .job-tracker__pulse + .job-tracker__pulse { animation-delay: 1.2s; }

/* The van: a top-down body that follows the route and turns with it */
.job-tracker__layer { position: absolute; top: 0; left: 0; width: 400px; height: 260px; transform-origin: 0 0; scale: tan(atan2(100cqw, 400px)); pointer-events: none; }
.job-tracker__van { position: absolute; top: 0; left: 0; width: 22px; height: 12px; offset-distance: calc(var(--job-tracker-progress, 0) * 100%); offset-rotate: auto; }
.job-tracker__van::before { content: ""; position: absolute; inset: -10px -9px; border-radius: 50%; background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 28%, transparent), transparent); }
.job-tracker__van-body {
  position: absolute; inset: 0; border-radius: 3px 5px 5px 3px; background: linear-gradient(90deg, var(--primary-hover), var(--primary));
  box-shadow: 0 0 4px color-mix(in srgb, var(--surface-deep) 35%, transparent), inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 25%, transparent);
}
.job-tracker__van-body::before { content: ""; position: absolute; top: 2px; right: 2px; bottom: 2px; width: 4px; border-radius: 1px 3px 3px 1px; background: color-mix(in srgb, var(--surface-light) 80%, var(--primary)); }
.job-tracker__van-body::after { content: ""; position: absolute; top: 4px; right: 8px; bottom: 4px; left: 3px; border-radius: 1px; background: color-mix(in srgb, var(--surface-light) 25%, transparent); }
.job-tracker__chip {
  position: absolute; top: 0.75rem; left: 0.75rem; display: inline-flex; align-items: center; gap: 0.4375rem; padding: 0.375rem 0.625rem; border-radius: var(--radius-full);
  background: var(--glass); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm); font: 600 0.75rem/1 var(--font-sans);
}
@supports (backdrop-filter: blur(1px)) { .job-tracker__chip { backdrop-filter: blur(var(--blur-md)) saturate(1.4); } }
.job-tracker__chip-dot { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 25%, transparent); }

/* Side panel: ETA, technician, stepper */
.job-tracker__side { container-type: inline-size; display: grid; gap: 1.25rem; align-content: start; }
.job-tracker__eta { display: grid; gap: 0.375rem; margin: 0; }
.job-tracker__eta-label { color: var(--text-muted); font: 500 0.75rem/1.3 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.job-tracker__eta-clip { display: block; overflow: hidden; }
.job-tracker__eta-value { display: inline-block; font: 600 clamp(2.75rem, 2.2rem + 2vw, 3.5rem)/1.05 var(--font-display); font-variant-numeric: tabular-nums; letter-spacing: var(--tracking-display); }
.job-tracker__eta-value small { margin-left: 0.375rem; color: var(--text-muted); font: 500 1.125rem var(--font-sans); letter-spacing: 0; }

.job-tracker__tech { display: flex; flex-wrap: wrap; align-items: center; gap: 0.875rem; padding: 0.875rem; border-radius: var(--radius-xl); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.job-tracker__avatar {
  position: relative; flex: none; display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: 50%;
  background: var(--job-tracker-grad); color: var(--text-inverse); font: 600 1rem var(--font-display);
  box-shadow: 0 8px 18px -8px color-mix(in srgb, var(--primary) 70%, transparent);
}
.job-tracker__avatar::after { content: ""; position: absolute; right: 0; bottom: 0; width: 0.75rem; height: 0.75rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 2px var(--surface-muted); }
.job-tracker__who { flex: 1; min-width: 9rem; }
.job-tracker__name { margin: 0; font-weight: 600; }
.job-tracker__meta, .job-tracker__vehicle { display: flex; flex-wrap: wrap; align-items: center; gap: 0.375rem; margin: 0.1875rem 0 0; color: var(--text-muted); font-size: 0.8125rem; }
.job-tracker__meta svg { color: var(--warning); fill: currentColor; }
.job-tracker__plate { padding: 0.0625rem 0.375rem; border-radius: var(--radius-sm); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle); color: var(--text-main); font: 600 0.6875rem var(--font-mono); letter-spacing: 0.08em; }
.job-tracker__contact { display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; width: 100%; }
.job-tracker__icon-btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; height: 2.75rem; padding: 0 0.875rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--primary-hover); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  font-size: 0.875rem; font-weight: 600; text-decoration: none; transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2);
}
.job-tracker__icon-btn:hover { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 40%, var(--border-subtle)), var(--shadow-md); }
.job-tracker__icon-btn:active { transform: scale(0.94); }

/* Stepper: a vertical timeline by default; per-step connectors fill, checks draw */
.job-tracker__steps { display: grid; margin: 0; padding: 0; list-style: none; }
.job-tracker__step { position: relative; display: grid; grid-template-columns: 1.75rem minmax(0, 1fr) auto; align-items: center; column-gap: 0.75rem; min-height: 3rem; color: var(--text-muted); transition: color var(--dur-3); }
.job-tracker__step::before, .job-tracker__step::after { content: ""; position: absolute; top: calc(50% + 0.875rem); left: calc(0.875rem - 1px); width: 2px; height: calc(100% - 1.75rem); border-radius: 2px; }
.job-tracker__step::before { background: var(--border-subtle); }
.job-tracker__step::after { background: var(--primary); transform: scaleY(0); transform-origin: top; transition: transform var(--dur-5) var(--ease-out); }
.job-tracker__step:last-child::before, .job-tracker__step:last-child::after { content: none; }
.job-tracker__step.is-done::after { transform: scaleY(1); }
.job-tracker__step.is-current::after { transform: scaleY(var(--job-tracker-sub, 0)); transition: none; }
.job-tracker__node {
  position: relative; z-index: 1; display: grid; place-items: center; width: 1.75rem; height: 1.75rem; border-radius: 50%;
  background: var(--surface-light); box-shadow: inset 0 0 0 2px var(--border-subtle);
  transition: background-color var(--dur-3), box-shadow var(--dur-3), transform var(--dur-4) var(--ease-spring);
}
.job-tracker__node > *, .job-tracker__node::before { grid-area: 1 / 1; }
.job-tracker__node svg { width: 0.875rem; height: 0.875rem; color: var(--text-inverse); stroke-width: 3; stroke-dasharray: 1; stroke-dashoffset: 1; transition: stroke-dashoffset var(--dur-4) var(--ease-out) var(--dur-2); }
.job-tracker__step.is-current .job-tracker__node { box-shadow: inset 0 0 0 2px var(--primary); transform: scale(1.08); }
.job-tracker__step.is-current .job-tracker__node::before { content: ""; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--primary); }
.job-tracker__step.is-current .job-tracker__node::after { content: ""; position: absolute; inset: -4px; border-radius: 50%; box-shadow: 0 0 0 2px color-mix(in srgb, var(--primary) 35%, transparent); opacity: 0; }
.job-tracker--js .job-tracker__step.is-current:not(.is-done) .job-tracker__node::after { animation: job-tracker-ring 2.4s var(--ease-out) infinite; }
.job-tracker__step.is-done .job-tracker__node { background: var(--primary); box-shadow: 0 6px 12px -6px color-mix(in srgb, var(--primary) 80%, transparent); transform: none; }
.job-tracker__step.is-done .job-tracker__node::before { content: none; }
.job-tracker__step.is-done .job-tracker__node svg { stroke-dashoffset: 0; }
.job-tracker__step.is-done, .job-tracker__step.is-current { color: var(--text-main); }
.job-tracker__step-label { font-size: 0.9375rem; font-weight: 600; }
.job-tracker__time { color: var(--text-muted); font: 500 0.75rem var(--font-mono); font-variant-numeric: tabular-nums; }

.job-tracker__done {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem 1rem; padding: 0.875rem 1rem; border-radius: var(--radius-xl);
  background: color-mix(in srgb, var(--success) 8%, var(--surface-light)); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--success) 30%, transparent);
  animation: job-tracker-rise var(--dur-4) var(--ease-spring) backwards;
}
.job-tracker__done[hidden] { display: none; }
.job-tracker__done p { margin: 0; font-size: 0.9375rem; }
.job-tracker__done strong { color: var(--success); }
.job-tracker__done-link { display: inline-flex; align-items: center; min-height: 2.5rem; padding: 0 1rem; border-radius: var(--radius-full); background: var(--success); color: var(--surface-light); font-size: 0.875rem; font-weight: 600; text-decoration: none; }

.job-tracker__sr { position: absolute; width: 1px; height: 1px; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* Wider panels: icon-only contact buttons, a horizontal stepper */
@container (min-width: 24rem) {
  .job-tracker__contact { display: flex; width: auto; }
  .job-tracker__icon-btn { position: relative; width: 2.75rem; padding: 0; }
  .job-tracker__btn-text { position: absolute; width: 1px; height: 1px; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }
}
@container (min-width: 34rem) {
  .job-tracker__steps { grid-template-columns: repeat(5, minmax(0, 1fr)); }
  .job-tracker__step { grid-template-columns: minmax(0, 1fr); justify-items: center; align-content: start; row-gap: 0.375rem; min-height: 0; text-align: center; }
  .job-tracker__step::before, .job-tracker__step::after { top: calc(0.875rem - 1px); left: calc(50% + 0.875rem); width: calc(100% - 1.75rem); height: 2px; }
  .job-tracker__step::after { transform: scaleX(0); transform-origin: left; }
  .job-tracker__step.is-done::after { transform: scaleX(1); }
  .job-tracker__step.is-current::after { transform: scaleX(var(--job-tracker-sub, 0)); }
}
@media (min-width: 768px) {
  .job-tracker { --job-tracker-pad: 1.75rem; }
  .job-tracker__map { margin-inline: 0; border-radius: var(--radius-xl); }
  .job-tracker__map::after { box-shadow: inset 0 0 0 1px var(--border-subtle); }
}
@media (min-width: 1024px) {
  .job-tracker__body { grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr); gap: 1.75rem; align-items: start; }
}

/* Paused or off-screen: freeze the loops (the script stops its clock too) */
.job-tracker[data-paused] *, .job-tracker[data-paused] *::before, .job-tracker[data-paused] *::after,
.job-tracker[data-offscreen] *, .job-tracker[data-offscreen] *::before, .job-tracker[data-offscreen] *::after { animation-play-state: paused !important; }

@media (prefers-reduced-motion: reduce) {
  .job-tracker__pulse, .job-tracker__done, .job-tracker__node::after { animation: none !important; }
}
@keyframes job-tracker-pulse { from { opacity: 0.85; transform: scale(0.35); } to { opacity: 0; transform: scale(1.7); } }
@keyframes job-tracker-ring { 0% { opacity: 0.9; transform: scale(0.85); } 70%, 100% { opacity: 0; transform: scale(1.5); } }
@keyframes job-tracker-rise { from { opacity: 0; transform: translateY(0.75rem) scale(0.97); } }
```

## JS

```js
const DRIVE = 2; // index of the "On the way" stage; the next one is "Working"
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const clock = (ms) => new Date(ms).toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' });
const ease = (t) => (t < 0.5 ? 4 * t ** 3 : 1 - (-2 * t + 2) ** 3 / 2);

document.querySelectorAll('[data-job-tracker]').forEach((root) => {
  const $ = (s) => root.querySelector(s);
  const steps = [...root.querySelectorAll('.job-tracker__step')], end = steps.length - 1;
  const plan = steps.map((li) => ({ ms: +li.dataset.ms || Infinity, min: +li.dataset.min || 0, say: li.dataset.say }));
  const startMin = plan.map((_, i) => plan.slice(0, i).reduce((sum, s) => sum + s.min, 0));
  const pause = $('.job-tracker__pause'), restart = $('.job-tracker__restart'), eta = $('.job-tracker__eta-value'), status = $('.job-tracker__status');

  // Resume from the server-rendered state (stage + fraction), so nothing jumps on load.
  // Demo clock: each stage lasts data-ms of real time and stands for data-min minutes of the day.
  const s0 = +root.dataset.startStage || 0, t0 = +root.dataset.startT || 0;
  const base = Date.now() - (startMin[s0] + t0 * plan[s0].min) * 60000;
  const at = (min) => clock(base + min * 60000);
  let elapsed = plan.slice(0, s0).reduce((sum, s) => sum + s.ms, 0) + t0 * plan[s0].ms;
  let prev = 0, raf = 0, cur = -1, paused = false, visible = true;

  root.classList.add('job-tracker--js');
  pause.hidden = restart.hidden = false;
  // The van layer scales with CSS trig functions; measure instead where they're missing
  if (!CSS.supports('scale', 'tan(atan2(1px, 2px))')) {
    new ResizeObserver(([entry]) => { $('.job-tracker__layer').style.scale = entry.contentRect.width / 400; }).observe($('.job-tracker__map'));
  }

  // ETA: the new value rolls in from above as the minutes count down
  const setEta = (value, unit, label) => {
    $('.job-tracker__eta-label').textContent = label;
    if (eta.textContent === `${value}${unit}`) return;
    eta.innerHTML = unit ? `${value}<small>${unit}</small>` : value;
    if (!reduce.matches) eta.animate({ transform: ['translateY(-60%)', 'none'], opacity: [0, 1], filter: ['blur(4px)', 'none'] }, { duration: 420, easing: 'cubic-bezier(0.16, 1, 0.3, 1)' });
  };

  // Stage change: list state (aria-current, completed text, times) and one polite status update
  const setStage = (i) => {
    if (i === cur) return;
    cur = i;
    root.dataset.stage = i;
    steps.forEach((li, n) => {
      const done = n < i || (n === end && i === end);
      li.classList.toggle('is-done', done);
      li.classList.toggle('is-current', n === i);
      if (n === i) li.setAttribute('aria-current', 'step'); else li.removeAttribute('aria-current');
      li.querySelector('.job-tracker__state').textContent = done ? ', completed' : '';
      li.querySelector('.job-tracker__time').textContent = n <= i ? at(startMin[n]) : '';
    });
    if (status.textContent !== plan[i].say) status.textContent = plan[i].say;
    $('.job-tracker__done').hidden = i < end;
  };

  // One rAF clock drives stage, van, route and ETA; it only advances while playing and on screen
  const frame = (now) => {
    raf = 0;
    if (paused || !visible) return;
    elapsed += Math.min(100, now - (prev || now));
    prev = now;
    let i = 0, start = 0;
    while (elapsed >= start + plan[i].ms) start += plan[i++].ms;
    const t = Math.min(1, (elapsed - start) / plan[i].ms);
    setStage(i);
    // Reduced motion: no gliding, the van jumps between depot, halfway and home
    root.style.setProperty('--job-tracker-progress', i < DRIVE ? 0 : i > DRIVE ? 1 : reduce.matches ? 0.5 : ease(t));
    root.style.setProperty('--job-tracker-sub', reduce.matches ? 0 : t);
    if (i < DRIVE) setEta(plan[DRIVE].min, 'min', 'Estimated arrival');
    else if (i === DRIVE) setEta(Math.max(1, Math.ceil(plan[DRIVE].min * (1 - t))), 'min', `Arriving in · ETA ${at(startMin[DRIVE + 1])}`);
    else setEta(i < end ? 'On site' : 'Done', '', i < end ? `Arrived ${at(startMin[DRIVE + 1])}` : `Finished ${at(startMin[end])}`);
    if (i < end) raf = requestAnimationFrame(frame);
  };
  const play = () => { if (!raf && !paused && visible) { prev = 0; raf = requestAnimationFrame(frame); } };

  pause.addEventListener('click', () => {
    paused = !paused;
    pause.setAttribute('aria-pressed', String(paused));
    root.toggleAttribute('data-paused', paused);
    play();
  });
  restart.addEventListener('click', () => {
    elapsed = 0;
    if (paused) pause.click(); else play();
  });
  // Off-screen: freeze the clock and the CSS loops without touching the button
  new IntersectionObserver(([entry]) => {
    visible = entry.isIntersecting;
    root.toggleAttribute('data-offscreen', !visible);
    play();
  }).observe(root);
});
```

## Notes

- The stages are an ordered list (`role="list"`, labelled "Job progress"). The current step has `aria-current="step"`, completed steps carry hidden ", completed" text, and each stage change updates one sentence in a `role="status"` region; ETA ticks are not announced. The map, van and route are `aria-hidden`, and the ETA, status and stepper carry the same information as text. The contact links read "Call Sam" and "Message Sam" at every width.
- Without JS the card is a server-rendered snapshot: stage classes, the van's position (`--job-tracker-progress`) and the ETA are in the markup, there are no loops, and the demo controls stay hidden. The script resumes from `data-start-stage`/`data-start-t`, so nothing jumps on load.
- Motion runs on one rAF clock. It stops while paused (an `aria-pressed` button that also freezes the CSS loops) and while the card is off-screen or the tab is hidden. Under reduced motion the van jumps between depot, halfway and home, the loops and the completion rise are off, and line fills and check draws are instant; the stages and ETA still update as text, so the pause control stays.
- The van rides `offset-path` on a 400×260 layer scaled to the map with `scale: tan(atan2(100cqw, 400px))`, with a `ResizeObserver` fallback where CSS trig is missing. Keep the van's inline `offset-path` and the SVG route `d` identical when you redraw the map. Container queries switch the stepper to horizontal and the contact buttons to icons when the panel is wide.
- For live data, replace `frame()` with your dispatch feed: set `data-stage`/the list classes, `--job-tracker-progress` (0–1 along the route) and the ETA text. Contrast: the avatar initials sit on `--primary` → deepened teal (≥ 4.9:1), the status and labels use `--text-muted` (4.8:1), and the "Job complete" `--success` text on its 8% tint is 4.8:1.
