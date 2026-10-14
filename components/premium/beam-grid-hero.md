# Beam Grid Hero

A dark, technical hero set on a fine square grid that fades out radially. Light beams with fading tails race along the grid lines, horizontally and vertically, snapped to the cells; under a mouse, a brighter local grid follows the cursor and the nearby intersections glow. Centred copy scans in line by line, then a glass "Live dispatch" card lifts into place below. On phones the grid tightens, the CTAs stack full width and the card condenses to map plus jobs. Depends on `tokens/variables.css`.

**Motion:** grid boots outward from the centre (`@property` mask radius, `--dur-5` × 2, `--ease-out`) · pill, headline lines, copy, CTAs and trust row rise in sequence (`--dur-5`, `--stagger`) with a clip-path scan on the headline · card lifts with a perspective tilt, job rows and route draw follow · beams travel the grid lines (WAAPI, linear, snapped to `--beam-hero-cell`) · light band flows round the pill border · cursor spotlight fades with `--dur-4`. A pause button and an off-screen observer freeze every loop.

## HTML

```html
<section class="beam-hero" aria-labelledby="beam-hero-title" data-beam-hero>
  <div class="beam-hero__bg" aria-hidden="true">
    <span class="beam-hero__glow"></span>
    <div class="beam-hero__field">
      <span class="beam-hero__grid"></span>
      <span class="beam-hero__lit"></span>
      <span class="beam-hero__beam"></span>
      <span class="beam-hero__beam beam-hero__beam--short beam-hero__beam--teal"></span>
      <span class="beam-hero__beam beam-hero__beam--teal"></span>
      <span class="beam-hero__beam beam-hero__beam--short"></span>
      <span class="beam-hero__beam beam-hero__beam--wide"></span>
      <span class="beam-hero__beam beam-hero__beam--short beam-hero__beam--teal beam-hero__beam--wide"></span>
    </div>
  </div>

  <div class="beam-hero__inner">
    <a class="beam-hero__pill" href="#heat-pumps">
      <span class="beam-hero__pill-tag">New</span>
      <span class="beam-hero__pill-text">Same-day heat pump installs</span>
      <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
    </a>

    <h1 id="beam-hero-title" class="beam-hero__title">
      <span class="beam-hero__line" style="--beam-hero-i: 1">Home repairs,</span>
      <span class="beam-hero__line" style="--beam-hero-i: 2">dispatched <span class="beam-hero__grad">in minutes.</span></span>
    </h1>
    <p class="beam-hero__lead" style="--beam-hero-i: 3">Brand routes the nearest licensed technician to your door, with upfront flat-rate pricing and live arrival tracking across Springfield.</p>

    <div class="beam-hero__actions" style="--beam-hero-i: 4">
      <a class="beam-hero__btn beam-hero__btn--primary" href="#book">
        Book a technician
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </a>
      <a class="beam-hero__btn beam-hero__btn--glass" href="tel:+15555550123">
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
        (555) 555-0123
      </a>
    </div>

    <ul class="beam-hero__trust" role="list" style="--beam-hero-i: 5">
      <li><svg class="beam-hero__star" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg><span><strong>4.9/5</strong> from 2,300 reviews</span></li>
      <li><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 3l7 3v6c0 4.5-3 7.6-7 9-4-1.4-7-4.5-7-9V6zM9 12l2 2 4-4" /></svg><span>Licensed &amp; insured</span></li>
      <li><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0zM12 7v5l3 2" /></svg><span>Avg. arrival <strong>47 min</strong></span></li>
    </ul>

    <div class="beam-hero__stage" aria-hidden="true">
      <div class="beam-hero__card">
        <div class="beam-hero__card-head">
          <span class="beam-hero__card-title"><span class="beam-hero__live"></span>Live dispatch</span>
          <span class="beam-hero__card-meta"><span class="beam-hero__card-city">Springfield · </span>14 techs online</span>
        </div>
        <div class="beam-hero__card-body">
          <div class="beam-hero__map">
            <svg viewBox="0 0 320 200" preserveAspectRatio="xMidYMid slice" focusable="false">
              <path class="beam-hero__river" d="M-10 160c50-24 94 14 152-6s98-48 188-16" />
              <path class="beam-hero__roads" d="M0 64h320M0 120h320M88 0v200M216 0v200M164 0l-46 200" />
              <path class="beam-hero__route beam-hero__route--glow" d="M60 168v-48h156V64h44" pathLength="1" />
              <path class="beam-hero__route" d="M60 168v-48h156V64h44" pathLength="1" />
              <rect class="beam-hero__hub" x="53" y="161" width="14" height="14" rx="4" />
              <circle class="beam-hero__pin" cx="126" cy="36" r="4" />
              <circle class="beam-hero__pin" cx="284" cy="150" r="4" />
              <circle class="beam-hero__ping" cx="260" cy="64" r="7" />
              <circle class="beam-hero__dest" cx="260" cy="64" r="6" />
              <circle class="beam-hero__van" cx="216" cy="96" r="5" />
              <rect class="beam-hero__eta" x="226" y="84" width="46" height="18" rx="9" />
              <text class="beam-hero__eta-text" x="249" y="96.5">8 MIN</text>
              <text class="beam-hero__area" x="14" y="28">NORTHSIDE</text>
              <text class="beam-hero__area" x="236" y="40">WESTLAKE</text>
              <text class="beam-hero__area" x="132" y="188">RIVERSIDE</text>
            </svg>
          </div>
          <div class="beam-hero__side">
            <ol class="beam-hero__jobs" role="list">
              <li style="--beam-hero-i: 0">
                <span class="beam-hero__job-icon"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M12 12c0-3 1-6 4-6s3 3 0 4.5M12 12c3 0 6 1 6 4s-3 3-4.5 0M12 12c0 3-1 6-4 6s-3-3 0-4.5M12 12c-3 0-6-1-6-4s3-3 4.5 0" /></svg></span>
                <span class="beam-hero__job"><strong>Heat pump install</strong><small>Westlake · Dana P.</small></span>
                <span class="beam-hero__status beam-hero__status--route">ETA 8 min</span>
              </li>
              <li style="--beam-hero-i: 1">
                <span class="beam-hero__job-icon"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M13 2 4 14h7l-1 8 9-12h-7z" /></svg></span>
                <span class="beam-hero__job"><strong>Panel upgrade</strong><small>Northside · Luis M.</small></span>
                <span class="beam-hero__status beam-hero__status--on">On site</span>
              </li>
              <li style="--beam-hero-i: 2">
                <span class="beam-hero__job-icon"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M12 3s6 6.2 6 11a6 6 0 0 1-12 0c0-4.8 6-11 6-11z" /></svg></span>
                <span class="beam-hero__job"><strong>Leak repair</strong><small>Riverside · Ana K.</small></span>
                <span class="beam-hero__status">2–4 pm</span>
              </li>
            </ol>
            <dl class="beam-hero__stats">
              <div><dt>Jobs today</dt><dd>128</dd></div>
              <div><dt>On time</dt><dd>98%</dd></div>
              <div><dt>Avg. rating</dt><dd>4.9</dd></div>
            </dl>
          </div>
        </div>
      </div>
    </div>
  </div>

  <button class="beam-hero__pause" type="button" aria-pressed="false" aria-label="Pause animation" hidden>
    <svg class="beam-hero__icon-pause" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
    <svg class="beam-hero__icon-play" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
  </button>
</section>
```

## CSS

```css
@property --beam-hero-r { syntax: "<percentage>"; inherits: false; initial-value: 74%; }

/* Section: deep surface, the grid lives in a decorative layer behind the copy */
.beam-hero {
  --beam-hero-cell: 40px; /* px: JS snaps the beams to this */
  --beam-hero-line: color-mix(in srgb, var(--text-inverse) 7%, transparent);
  --beam-hero-lit: color-mix(in srgb, var(--primary-2) 60%, var(--primary));
  --beam-hero-in: 420ms; /* when the copy starts, just after the grid boots */
  position: relative; isolation: isolate; overflow: clip;
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}
.beam-hero__bg { position: absolute; inset: 0; z-index: -1; pointer-events: none; }
.beam-hero__glow {
  position: absolute; left: 50%; top: -16rem; width: min(72rem, 170vw); aspect-ratio: 1.5; translate: -50% 0;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 30%, transparent), color-mix(in srgb, var(--primary-2) 10%, transparent) 55%, transparent);
}

/* The field fades radially; its mask radius grows on load so the grid "boots" from the centre */
.beam-hero__field {
  position: absolute; inset: 0; overflow: hidden;
  -webkit-mask-image: radial-gradient(ellipse var(--beam-hero-r) calc(var(--beam-hero-r) * 0.8) at 50% 30%, black 20%, transparent);
  mask-image: radial-gradient(ellipse var(--beam-hero-r) calc(var(--beam-hero-r) * 0.8) at 50% 30%, black 20%, transparent);
  animation: beam-hero-boot calc(var(--dur-5) * 2) var(--ease-out) both;
}
/* Lines sit on the tile's top/left edge; the offset centres one line on the section so JS can snap to W/2 + k·cell */
.beam-hero__grid, .beam-hero__lit {
  position: absolute; inset: 0;
  background-image: linear-gradient(var(--beam-hero-line) 1px, transparent 1px), linear-gradient(90deg, var(--beam-hero-line) 1px, transparent 1px);
  background-size: var(--beam-hero-cell) var(--beam-hero-cell);
  background-position: calc(50% - var(--beam-hero-cell) / 2) calc(50% - var(--beam-hero-cell) / 2);
}
/* Cursor spotlight: a brighter copy of the grid plus glowing intersections, masked to a circle at the pointer */
.beam-hero__lit {
  --beam-hero-line: color-mix(in srgb, var(--beam-hero-lit) 55%, transparent);
  background-image:
    radial-gradient(circle, var(--text-inverse) 0 1px, color-mix(in srgb, var(--beam-hero-lit) 75%, transparent) 1.5px, transparent 4px),
    linear-gradient(var(--beam-hero-line) 1px, transparent 1px),
    linear-gradient(90deg, var(--beam-hero-line) 1px, transparent 1px);
  background-size: var(--beam-hero-cell) var(--beam-hero-cell);
  background-position:
    calc(50% + 0.5px) calc(50% + 0.5px),
    calc(50% - var(--beam-hero-cell) / 2) calc(50% - var(--beam-hero-cell) / 2),
    calc(50% - var(--beam-hero-cell) / 2) calc(50% - var(--beam-hero-cell) / 2);
  opacity: var(--beam-hero-spot, 0);
  transition: opacity var(--dur-4) var(--ease-out);
  -webkit-mask-image: radial-gradient(circle 11rem at var(--beam-hero-mx, 50%) var(--beam-hero-my, 30%), black, transparent);
  mask-image: radial-gradient(circle 11rem at var(--beam-hero-mx, 50%) var(--beam-hero-my, 30%), black, transparent);
}

/* Beams: a 1px streak with a fading tail and a hot head; JS moves and rotates them along grid lines */
.beam-hero__beam {
  --beam-hero-len: 9rem;
  position: absolute; left: 0; top: 0; width: var(--beam-hero-len); height: 1px; border-radius: 1px;
  transform: translateX(-100%); transform-origin: 0 50%; will-change: transform;
  background: linear-gradient(90deg, transparent, color-mix(in srgb, var(--primary) 70%, transparent) 60%, color-mix(in srgb, var(--primary-2) 35%, var(--text-inverse)));
}
.beam-hero__beam::after {
  content: ""; position: absolute; right: -2px; top: -2px; width: 5px; height: 5px; border-radius: 50%;
  background: var(--text-inverse);
  box-shadow: 0 0 6px 1px color-mix(in srgb, var(--primary-2) 90%, transparent), 0 0 18px 4px color-mix(in srgb, var(--primary) 55%, transparent);
}
.beam-hero__beam--short { --beam-hero-len: 5.5rem; }
.beam-hero__beam--teal { background: linear-gradient(90deg, transparent, color-mix(in srgb, var(--primary-2) 80%, transparent) 70%, var(--text-inverse)); }
.beam-hero__beam--wide { display: none; } /* extra beams for wide screens only */

/* Layout: one centred column; the dispatch card closes it */
.beam-hero__inner {
  display: flex; flex-direction: column; align-items: center; text-align: center;
  max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4rem, 11vw, 7.5rem) var(--gutter) clamp(5rem, 9vw, 7rem);
}

/* Entrance: each block rises out of a blur in order (no JS, no flash: the from-state applies at first paint) */
.beam-hero__lead, .beam-hero__actions, .beam-hero__trust {
  animation: beam-hero-rise var(--dur-5) var(--ease-out) calc(var(--beam-hero-in) + var(--beam-hero-i) * var(--stagger) * 2) both;
}

/* Announcement pill: a band of light flows along its gradient border */
.beam-hero__pill {
  display: inline-flex; align-items: center; gap: 0.625rem; max-width: 100%; min-height: 2.25rem;
  padding: 0.25rem 0.875rem 0.25rem 0.25rem; border: 1px solid transparent; border-radius: var(--radius-full);
  background:
    linear-gradient(color-mix(in srgb, var(--surface-deep) 90%, var(--primary)), color-mix(in srgb, var(--surface-deep) 90%, var(--primary))) padding-box,
    linear-gradient(90deg, transparent 40%, var(--primary-2) 47%, var(--text-inverse) 50%, var(--primary) 53%, transparent 60%) border-box,
    linear-gradient(90deg, color-mix(in srgb, var(--primary) 45%, transparent), color-mix(in srgb, var(--primary-2) 45%, transparent)) border-box;
  background-size: auto, 300% 100%, auto;
  background-position: 0 0, 100% 0, 0 0;
  background-repeat: no-repeat;
  color: var(--text-inverse-muted); font-size: 0.8125rem; line-height: 1.3; text-align: left; text-decoration: none;
  box-shadow: 0 0 24px -6px color-mix(in srgb, var(--primary) 45%, transparent);
  animation: beam-hero-rise var(--dur-5) var(--ease-out) var(--beam-hero-in) both, beam-hero-flow 5s linear 2s infinite;
  transition: color var(--dur-2);
}
.beam-hero__pill:hover { color: var(--text-inverse); }
.beam-hero__pill svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.beam-hero__pill:hover svg { transform: translateX(3px); }
.beam-hero__pill-tag {
  flex: none; padding: 0.25rem 0.5625rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--primary) 32%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 60%, transparent);
  color: var(--text-inverse); font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
}
.beam-hero__pill-text { min-width: 0; }

/* Headline: each line is scanned in left to right, like a beam writing it */
.beam-hero__title {
  margin: 1.75rem 0 0; font: 600 clamp(2.5rem, 1.1rem + 6.6vw, 6rem)/1.02 var(--font-display);
  letter-spacing: var(--tracking-display);
}
.beam-hero__line {
  display: block; width: fit-content; margin-inline: auto;
  animation: beam-hero-scan var(--dur-5) var(--ease-out) calc(var(--beam-hero-in) + var(--beam-hero-i) * var(--stagger) * 2) backwards;
}
.beam-hero__grad {
  display: inline-block; padding-bottom: 0.06em; white-space: nowrap;
  background: linear-gradient(90deg, color-mix(in srgb, var(--primary) 45%, var(--text-inverse)), color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse)) 75%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.beam-hero__lead {
  max-width: 36rem; margin: 1.5rem 0 0; color: var(--text-inverse-muted);
  font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; text-wrap: pretty;
}

/* CTAs: a glowing primary and a glass secondary; full-width stack on small phones */
.beam-hero__actions { display: grid; gap: 0.75rem; width: 100%; margin-top: 2.25rem; }
.beam-hero__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
  min-height: 3rem; padding: 0 1.5rem; border-radius: var(--radius-full);
  color: var(--text-inverse); font: 600 0.9375rem/1 var(--font-sans); text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out), background-color var(--dur-2);
}
.beam-hero__btn svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.beam-hero__btn:hover { transform: translateY(-2px); }
.beam-hero__btn:active { transform: scale(0.97); }
.beam-hero__btn--primary {
  background: linear-gradient(180deg, var(--primary), var(--primary-hover));
  box-shadow:
    inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 30%, transparent),
    inset 0 0 0 1px color-mix(in srgb, var(--primary) 70%, var(--text-inverse)),
    0 10px 30px -8px color-mix(in srgb, var(--primary) 85%, transparent),
    0 0 60px -12px color-mix(in srgb, var(--primary-2) 70%, transparent);
}
.beam-hero__btn--primary:hover {
  box-shadow:
    inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 35%, transparent),
    inset 0 0 0 1px color-mix(in srgb, var(--primary) 55%, var(--text-inverse)),
    0 14px 36px -8px color-mix(in srgb, var(--primary) 95%, transparent),
    0 0 90px -10px color-mix(in srgb, var(--primary-2) 85%, transparent);
}
.beam-hero__btn--primary:hover svg { transform: translateX(3px); }
.beam-hero__btn--glass {
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
}
.beam-hero__btn--glass:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.beam-hero :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Trust row */
.beam-hero__trust {
  display: flex; flex-wrap: wrap; justify-content: center; gap: 0.625rem 1.5rem; margin: 2rem 0 0; padding: 0; list-style: none;
  color: var(--text-inverse-muted); font-size: 0.875rem;
}
.beam-hero__trust li { display: inline-flex; align-items: center; gap: 0.5rem; }
.beam-hero__trust strong { color: var(--text-inverse); font-weight: 600; }
.beam-hero__trust svg { flex: none; fill: none; stroke: color-mix(in srgb, var(--primary-2) 50%, var(--text-inverse)); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.beam-hero__trust .beam-hero__star { fill: var(--accent); stroke: var(--accent); }

/* Live dispatch card: glass over the grid, lifts into place after the copy */
.beam-hero__stage { position: relative; width: 100%; max-width: 54rem; margin-top: clamp(3rem, 8vw, 4.5rem); perspective: 1400px; text-align: left; }
.beam-hero__stage::before {
  content: ""; position: absolute; inset: 15% -10% -20%; z-index: -1;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 26%, transparent), transparent);
}
.beam-hero__card {
  position: relative; padding: 0.875rem; border-radius: var(--radius-2xl);
  background: color-mix(in srgb, var(--surface-deep) 82%, var(--primary));
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 40px 80px -30px color-mix(in srgb, var(--surface-deep) 90%, transparent);
  transform-origin: 50% 100%;
  animation: beam-hero-lift calc(var(--dur-5) * 1.3) var(--ease-out) calc(var(--beam-hero-in) + 12 * var(--stagger)) both;
}
@supports (backdrop-filter: blur(1px)) {
  .beam-hero__card {
    background: linear-gradient(180deg, color-mix(in srgb, var(--text-inverse) 7%, transparent), color-mix(in srgb, var(--text-inverse) 2%, transparent));
    backdrop-filter: blur(var(--blur-md)) saturate(1.3);
  }
}
.beam-hero__card::before { /* a beam resting on the top edge */
  content: ""; position: absolute; top: 0; left: 14%; right: 14%; height: 1px;
  background: linear-gradient(90deg, transparent, color-mix(in srgb, var(--primary-2) 70%, var(--text-inverse)), transparent);
}
.beam-hero__card-head { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 0.25rem 0.25rem 0.875rem; }
.beam-hero__card-title { display: inline-flex; align-items: center; gap: 0.5rem; font: 600 0.9375rem var(--font-display); letter-spacing: -0.01em; }
.beam-hero__card-meta { color: var(--text-inverse-muted); font: 500 0.6875rem/1.2 var(--font-mono); letter-spacing: 0.05em; text-transform: uppercase; text-align: right; }
.beam-hero__card-city { display: none; }
.beam-hero__live { position: relative; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 10px var(--success); }
.beam-hero__live::after { content: ""; position: absolute; inset: 0; border-radius: 50%; background: var(--success); animation: beam-hero-ping 1.8s var(--ease-out) infinite; }
.beam-hero__card-body { display: grid; gap: 0.75rem; }

/* Mini map: its own fine grid echoes the hero; the route draws in once */
.beam-hero__map {
  position: relative; min-height: 10.5rem; border-radius: var(--radius-xl); overflow: hidden;
  background:
    linear-gradient(color-mix(in srgb, var(--text-inverse) 4%, transparent) 1px, transparent 1px) 0 0 / 16px 16px,
    linear-gradient(90deg, color-mix(in srgb, var(--text-inverse) 4%, transparent) 1px, transparent 1px) 0 0 / 16px 16px,
    color-mix(in srgb, var(--surface-deep) 75%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse);
}
.beam-hero__map svg { position: absolute; inset: 0; width: 100%; height: 100%; fill: none; stroke-linecap: round; stroke-linejoin: round; }
.beam-hero__river { stroke: color-mix(in srgb, var(--primary-2) 22%, transparent); stroke-width: 16; }
.beam-hero__roads { stroke: color-mix(in srgb, var(--text-inverse) 12%, transparent); stroke-width: 3; }
.beam-hero__route { stroke: color-mix(in srgb, var(--primary-2) 45%, var(--text-inverse)); stroke-width: 2.5; stroke-dasharray: 1; }
.beam-hero__route--glow { stroke: color-mix(in srgb, var(--primary) 55%, transparent); stroke-width: 8; opacity: 0.6; }
.beam-hero__route { animation: beam-hero-draw calc(var(--dur-5) * 1.8) var(--ease-out) calc(var(--beam-hero-in) + 1.2s) backwards; }
.beam-hero__hub { fill: var(--primary); stroke: var(--text-inverse); stroke-width: 2; }
.beam-hero__pin { fill: color-mix(in srgb, var(--text-inverse) 55%, transparent); }
.beam-hero__dest { fill: var(--primary-2); stroke: var(--text-inverse); stroke-width: 2; }
.beam-hero__ping { fill: color-mix(in srgb, var(--primary-2) 60%, transparent); transform-box: fill-box; transform-origin: center; animation: beam-hero-ping 2.2s var(--ease-out) infinite; }
.beam-hero__van { fill: var(--text-inverse); stroke: var(--primary); stroke-width: 3; }
.beam-hero__eta { fill: var(--primary); }
.beam-hero__eta-text { fill: var(--text-inverse); font: 600 9px var(--font-mono); text-anchor: middle; }
.beam-hero__area { fill: var(--text-inverse-muted); font: 500 8.5px var(--font-mono); letter-spacing: 0.08em; }

/* Jobs and stats */
.beam-hero__side { display: grid; gap: 0.75rem; align-content: start; }
.beam-hero__jobs { display: grid; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.beam-hero__jobs li {
  display: flex; align-items: center; gap: 0.75rem; padding: 0.625rem; border-radius: var(--radius-xl);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse);
  animation: beam-hero-rise var(--dur-4) var(--ease-out) calc(var(--beam-hero-in) + 1.1s + var(--beam-hero-i) * var(--stagger) * 2) both;
}
.beam-hero__job-icon {
  flex: none; display: grid; place-items: center; width: 2.25rem; height: 2.25rem; border-radius: var(--radius-lg);
  background: color-mix(in srgb, var(--primary) 22%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 45%, transparent);
  color: color-mix(in srgb, var(--primary) 35%, var(--text-inverse));
}
.beam-hero__job-icon svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.beam-hero__job { flex: 1; min-width: 0; }
.beam-hero__job strong { display: block; overflow: hidden; font-size: 0.875rem; font-weight: 600; white-space: nowrap; text-overflow: ellipsis; }
.beam-hero__job small { color: var(--text-inverse-muted); font-size: 0.75rem; }
.beam-hero__status {
  flex: none; padding: 0.25rem 0.5rem; border-radius: var(--radius-full); background: var(--glass-inverse);
  color: var(--text-inverse-muted); font: 600 0.6875rem/1.2 var(--font-mono); white-space: nowrap;
}
.beam-hero__status--route { background: color-mix(in srgb, var(--primary) 38%, transparent); color: var(--text-inverse); }
.beam-hero__status--on { background: color-mix(in srgb, var(--success) 30%, transparent); color: var(--text-inverse); }
.beam-hero__stats { display: none; margin: 0; }
.beam-hero__stats div { padding: 0.625rem 0.75rem; border-radius: var(--radius-lg); box-shadow: inset 0 0 0 1px var(--border-inverse); }
.beam-hero__stats dt { color: var(--text-inverse-muted); font: 500 0.625rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.beam-hero__stats dd { margin: 0.25rem 0 0; font: 600 1.125rem/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }

/* Pause control */
.beam-hero__pause {
  position: absolute; right: var(--gutter); bottom: 1rem; display: grid; place-items: center;
  width: 2.5rem; height: 2.5rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse-muted); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: color var(--dur-2), background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.beam-hero__pause:hover { color: var(--text-inverse); background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.beam-hero__pause:active { transform: scale(0.92); }
.beam-hero__pause[hidden] { display: none; }
.beam-hero__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.beam-hero__icon-play, .beam-hero__pause[aria-pressed="true"] .beam-hero__icon-pause { display: none; }
.beam-hero__pause[aria-pressed="true"] .beam-hero__icon-play { display: block; }

/* Paused or off-screen: freeze the CSS loops (JS pauses the beams) */
.beam-hero:is([data-paused], [data-offscreen]) :is(.beam-hero__pill, .beam-hero__ping),
.beam-hero[data-paused] .beam-hero__live::after,
.beam-hero[data-offscreen] .beam-hero__live::after { animation-play-state: paused; }

@media (min-width: 480px) {
  .beam-hero__actions { display: flex; flex-wrap: wrap; justify-content: center; }
  .beam-hero__card-city { display: inline; }
  .beam-hero__stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.5rem; }
}
@media (min-width: 768px) {
  .beam-hero { --beam-hero-cell: 48px; }
  .beam-hero__beam--wide { display: block; }
  .beam-hero__card { padding: 1rem; }
  .beam-hero__card-body { grid-template-columns: 1.1fr 1fr; }
  .beam-hero__map { min-height: 13rem; }
}
@media (prefers-reduced-motion: reduce) {
  .beam-hero *, .beam-hero *::before, .beam-hero *::after { animation: none !important; }
  .beam-hero__beam, .beam-hero__lit { display: none; }
}

@keyframes beam-hero-boot { from { --beam-hero-r: 8%; } }
@keyframes beam-hero-rise { from { opacity: 0; transform: translateY(14px); filter: blur(8px); } }
@keyframes beam-hero-scan { from { clip-path: inset(-0.3em 100% -0.3em -0.3em); opacity: 0.3; filter: blur(6px); } to { clip-path: inset(-0.3em -0.3em -0.3em -0.3em); } }
@keyframes beam-hero-lift { from { opacity: 0; transform: rotateX(18deg) translateY(3rem) scale(0.96); filter: blur(10px); } }
@keyframes beam-hero-flow { 0% { background-position: 0 0, 100% 0, 0 0; } 50%, 100% { background-position: 0 0, 0% 0, 0 0; } }
@keyframes beam-hero-draw { from { stroke-dashoffset: 1; } }
@keyframes beam-hero-ping { to { transform: scale(2.6); opacity: 0; } }
```

## JS

```js
document.querySelectorAll('[data-beam-hero]').forEach((hero) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const field = hero.querySelector('.beam-hero__field');
  const lit = hero.querySelector('.beam-hero__lit');
  const pause = hero.querySelector('.beam-hero__pause');
  const running = new Set();
  let w = 0, h = 0, cell = 48, paused = false, offscreen = false;

  const measure = () => {
    ({ width: w, height: h } = field.getBoundingClientRect());
    cell = parseFloat(getComputedStyle(hero).getPropertyValue('--beam-hero-cell')) || 48;
  };
  measure();
  new ResizeObserver(measure).observe(field);

  // A random grid line between lo and hi (fractions of the span). The CSS centres a line on the
  // section, so lines sit at span/2 + k·cell; the band keeps beams where the radial mask shows the grid.
  const snap = (span, lo, hi) => {
    const k0 = Math.ceil((span * (lo - 0.5)) / cell);
    const k1 = Math.floor((span * (hi - 0.5)) / cell);
    return span / 2 + cell * (k0 + Math.floor(Math.random() * (k1 - k0 + 1)));
  };

  // Run a beam along a random line in one of four directions, then relaunch it elsewhere
  const launch = (beam, first) => {
    if (reduce.matches || !beam.offsetWidth) return;
    const len = beam.offsetWidth;
    const dir = Math.floor(Math.random() * 4); // 0 →, 1 ←, 2 ↓, 3 ↑
    const vertical = dir > 1;
    const span = vertical ? h : w;
    const at = vertical ? snap(w, 0.14, 0.86) + 0.5 : snap(h, 0.06, 0.6);
    const [from, to] = dir % 2 ? [span + len, 0] : [-len, span];
    const rot = [0, 180, 90, -90][dir];
    const at2d = (p) => `translate3d(${vertical ? at : p}px, ${vertical ? p : at}px, 0) rotate(${rot}deg)`;
    const anim = beam.animate({ transform: [at2d(from), at2d(to)] }, {
      duration: (span + len) / (0.28 + Math.random() * 0.24), // px per ms
      delay: (first ? 1400 : 250) + Math.random() * 2600,
      fill: 'backwards',
    });
    running.add(anim);
    if (paused || offscreen) anim.pause();
    anim.onfinish = () => { running.delete(anim); launch(beam); };
  };

  // Pause button (WCAG 2.2.2) and off-screen freeze; CSS loops follow the data attributes
  const sync = () => running.forEach((a) => {
    if (paused || offscreen) a.pause();
    else if (a.playState === 'paused') a.play();
  });
  pause.hidden = reduce.matches;
  pause.addEventListener('click', () => {
    paused = hero.toggleAttribute('data-paused');
    pause.setAttribute('aria-pressed', String(paused));
    sync();
  });
  new IntersectionObserver(([entry]) => {
    offscreen = !entry.isIntersecting;
    hero.toggleAttribute('data-offscreen', offscreen);
    sync();
  }).observe(hero);
  hero.querySelectorAll('.beam-hero__beam').forEach((beam) => launch(beam, true));

  // Cursor spotlight (mouse only), one style write per frame on the leaf layer
  let frame = 0, px = 0, py = 0;
  hero.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse' || reduce.matches) return;
    px = e.clientX; py = e.clientY;
    frame ||= requestAnimationFrame(() => {
      frame = 0;
      const r = field.getBoundingClientRect();
      lit.style.setProperty('--beam-hero-mx', `${px - r.left}px`);
      lit.style.setProperty('--beam-hero-my', `${py - r.top}px`);
      lit.style.setProperty('--beam-hero-spot', '1');
    });
  }, { passive: true });
  hero.addEventListener('pointerleave', () => lit.style.setProperty('--beam-hero-spot', '0'));
});
```

## Notes

- Landmarks and order: pill link, one `<h1>`, lead, two CTAs, a trust list (`role="list"`). The grid, beams, spotlight and the "Live dispatch" card are decorative (`aria-hidden="true"`); replace the card with a product shot if you have one.
- Without JS the hero is complete: static grid, glow, CSS entrance and card. JS only adds the beams, the cursor spotlight and the pause button. Nothing is hidden behind a gate, so nothing flashes.
- Reduced motion: no beams, no spotlight, no entrance, pill light or pings. What's left is a static grid with a single glow. Beams are WAAPI animations, so the pause button calls `pause()`/`play()` on them; an `IntersectionObserver` does the same off-screen without touching the button.
- Contrast on `--surface-deep`: lead and trust text use `--text-inverse-muted` (about 8:1); the gradient phrase stays above 9:1 at both ends; the white CTA label sits on `--primary`→`--primary-hover` (5.2:1 or better).
- Retheme with `--beam-hero-cell` (keep it in px; the beams snap to it), `--beam-hero-lit` for the spotlight colour, and the number of `.beam-hero__beam` spans (`--wide` ones only run from 768px). Browsers without `@property` skip the grid's boot and show it at once.
