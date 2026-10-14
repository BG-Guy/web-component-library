# Skeuomorphic Thermostat

An HVAC promo, "Find your comfort plan", built around a tactile round thermostat on a brushed-metal wall plate: a conic-and-radial brushed bezel, a knurled ring, a glossy dark glass face with SVG ticks, a cool-to-heat arc, and a big readout whose digits roll like an odometer. The signature moment is turning it: drag around the dial (the pointer's angle sets the value), use the wheel while it's focused, or use the keys, and the ring snaps from detent to detent with a spring and a tiny click scale while the arc, the glowing cap and the page tint follow. Heat / Cool / Auto are latching rocker keys with LEDs, the fan is a metal toggle, and the recommended plan swaps with the mode. On phones the plate sits between the heading and the plan card. Depends on `tokens/variables.css`.

**Motion:** ring and cap snap per detent (`--dur-3`, `--ease-spring`) · arc sweep via a registered `--thermostat-sweep` (`--dur-3`, `--ease-spring`) · detent click scale (180ms, WAAPI, skipped under reduced motion) · rolling digits (`--dur-4`, `--ease-spring`) · rocker press (`--dur-1`) and LED glow (`--dur-3`) · fan knob and blade spin (`--dur-3`/`--dur-5`, `--ease-spring`) · plan swap fade-up (`--dur-4`, `--ease-out`) · section tint follows the mode (`--dur-5`).

## HTML

```html
<section class="thermostat" aria-labelledby="thermostat-title" data-thermostat>
  <div class="thermostat__inner">
    <header class="thermostat__head">
      <p class="thermostat__eyebrow">Heating &amp; cooling plans</p>
      <h2 id="thermostat-title" class="thermostat__title">Find your comfort plan</h2>
      <p class="thermostat__lead">Turn the dial to the temperature you like and pick how your home runs. We'll match a maintenance plan that keeps it there all year.</p>
    </header>

    <form class="thermostat__device" action="#thermostat-plans" method="get" aria-label="Comfort settings">
      <div class="thermostat__dial" style="--thermostat-angle: -5.4deg; --thermostat-sweep: 129.6deg">
        <span class="thermostat__bezel" aria-hidden="true"></span>
        <span class="thermostat__ring" aria-hidden="true"></span>
        <span class="thermostat__face" aria-hidden="true">
          <span class="thermostat__track"></span>
          <span class="thermostat__glow"><span class="thermostat__arc"></span></span>
          <svg class="thermostat__ticks" viewBox="0 0 200 200" aria-hidden="true" focusable="false">
            <path class="thermostat__ticks-minor" d="M46.46 164.72A84 84 0 1 1 153.54 164.72" pathLength="26" />
            <path class="thermostat__ticks-major" d="M46.46 164.72A84 84 0 1 1 153.54 164.72" pathLength="26" />
            <text x="63" y="168" text-anchor="middle">60</text>
            <text x="137" y="168" text-anchor="middle">85</text>
          </svg>
          <span class="thermostat__cap"></span>
          <span class="thermostat__readout">
            <span class="thermostat__mode-label">Heating to</span>
            <span class="thermostat__digits">
              <span class="thermostat__digit" style="--thermostat-d: 7"><span class="thermostat__strip"><span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span></span></span>
              <span class="thermostat__digit" style="--thermostat-d: 2"><span class="thermostat__strip"><span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span></span></span>
              <span class="thermostat__deg">°F</span>
            </span>
            <span class="thermostat__indoor">Indoor 68° · 41% RH</span>
          </span>
          <span class="thermostat__gloss"></span>
        </span>
        <label class="thermostat__fallback">
          Set temperature
          <input class="thermostat__range" type="range" name="temp" min="60" max="85" step="1" value="72">
          <span class="thermostat__range-scale" aria-hidden="true"><span>60°</span><span>85°</span></span>
        </label>
      </div>
      <p class="thermostat__hint" hidden>Drag the ring or use the arrow keys</p>

      <fieldset class="thermostat__modes">
        <legend class="thermostat__legend">Mode</legend>
        <div class="thermostat__rockers">
          <label class="thermostat__rocker thermostat__rocker--heat"><input class="thermostat__radio" type="radio" name="mode" value="heat" checked><span class="thermostat__led" aria-hidden="true"></span>Heat</label>
          <label class="thermostat__rocker thermostat__rocker--cool"><input class="thermostat__radio" type="radio" name="mode" value="cool"><span class="thermostat__led" aria-hidden="true"></span>Cool</label>
          <label class="thermostat__rocker thermostat__rocker--auto"><input class="thermostat__radio" type="radio" name="mode" value="auto"><span class="thermostat__led" aria-hidden="true"></span>Auto</label>
        </div>
      </fieldset>

      <label class="thermostat__fan">
        <svg class="thermostat__fan-icon" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M10.83 16.38a6.08 6.08 0 0 1-8.62-7l5.41 1.45a6.08 6.08 0 0 1 7-8.62l-1.45 5.41a6.08 6.08 0 0 1 8.62 7l-5.41-1.45a6.08 6.08 0 0 1-7 8.62zM12 12v.01" /></svg>
        <span class="thermostat__fan-label">Fan always on</span>
        <input class="thermostat__fan-input" type="checkbox" role="switch" name="fan">
        <span class="thermostat__fan-track" aria-hidden="true"><span class="thermostat__fan-knob"></span></span>
      </label>
    </form>

    <div class="thermostat__plans" id="thermostat-plans">
      <article class="thermostat__plan thermostat__plan--heat">
        <p class="thermostat__plan-kicker">Recommended for heating</p>
        <h3 class="thermostat__plan-name">Furnace Care</h3>
        <p class="thermostat__plan-price"><strong>$15</strong> / month</p>
        <ul class="thermostat__plan-list" role="list">
          <li>Annual furnace tune-up and carbon monoxide check</li>
          <li>Priority heating repairs, even on holidays</li>
          <li>15% off parts and labour</li>
        </ul>
        <a class="thermostat__plan-cta" href="#plans">Choose Furnace Care</a>
      </article>
      <article class="thermostat__plan thermostat__plan--cool">
        <p class="thermostat__plan-kicker">Recommended for cooling</p>
        <h3 class="thermostat__plan-name">AC Care</h3>
        <p class="thermostat__plan-price"><strong>$15</strong> / month</p>
        <ul class="thermostat__plan-list" role="list">
          <li>Spring AC tune-up and refrigerant check</li>
          <li>Priority cooling repairs within 24 hours</li>
          <li>15% off parts and labour</li>
        </ul>
        <a class="thermostat__plan-cta" href="#plans">Choose AC Care</a>
      </article>
      <article class="thermostat__plan thermostat__plan--auto">
        <p class="thermostat__plan-kicker">Recommended for year-round comfort</p>
        <h3 class="thermostat__plan-name">Comfort Plus</h3>
        <p class="thermostat__plan-price"><strong>$24</strong> / month</p>
        <ul class="thermostat__plan-list" role="list">
          <li>Spring and fall tune-ups for both systems</li>
          <li>Priority repairs with no overtime fees</li>
          <li>20% off parts and labour, filters included</li>
        </ul>
        <a class="thermostat__plan-cta" href="#plans">Choose Comfort Plus</a>
      </article>
    </div>
  </div>
</section>
```

## CSS

```css
@property --thermostat-sweep { syntax: "<angle>"; inherits: true; initial-value: 0deg; }
@property --thermostat-tint { syntax: "<color>"; inherits: true; initial-value: transparent; }

/* Palette: tokens plus local metal, heat, cool (and an auto LED); the light section takes a mode tint */
.thermostat {
  --thermostat-metal-hi: #f5f6f8;
  --thermostat-metal-mid: #c8ccd3;
  --thermostat-metal-lo: #9097a2;
  --thermostat-metal-dk: #5d636d;
  --thermostat-heat: #ff7a2f;
  --thermostat-cool: #38bdf8;
  --thermostat-auto: #4ade80;
  --thermostat-tint: var(--thermostat-heat);
  background:
    radial-gradient(45% 55% at 78% 45%, color-mix(in srgb, var(--thermostat-tint) 16%, transparent), transparent 72%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
  transition: --thermostat-tint var(--dur-5) var(--ease-out);
}
.thermostat:has(.thermostat__radio[value="cool"]:checked) { --thermostat-tint: var(--thermostat-cool); }
.thermostat:has(.thermostat__radio[value="auto"]:checked) { --thermostat-tint: var(--thermostat-auto); }
.thermostat__inner {
  display: grid; gap: 2.75rem; grid-template-areas: "head" "device" "plans";
  max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter);
}

/* Heading */
.thermostat__head { grid-area: head; max-width: 34rem; }
.thermostat__eyebrow { margin: 0; color: var(--primary); font: 600 0.8125rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.thermostat__title { margin: 0.75rem 0 0; font: 600 clamp(2.25rem, 1.4rem + 3.2vw, 3.5rem)/1.04 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.thermostat__lead { margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }

/* Wall plate with two mounting screws */
.thermostat__device {
  grid-area: device; position: relative; display: grid; justify-items: center; gap: 1.25rem;
  width: min(100%, 22rem); margin: 0 auto; padding: 2.5rem 1.5rem 2.25rem; border-radius: var(--radius-2xl);
  background: linear-gradient(160deg, var(--thermostat-metal-hi), color-mix(in srgb, var(--thermostat-metal-mid) 70%, var(--thermostat-metal-hi)));
  box-shadow: var(--shadow-xl), var(--highlight), inset 0 0 0 1px color-mix(in srgb, var(--thermostat-metal-lo) 35%, transparent);
}
.thermostat__device::before, .thermostat__device::after {
  content: ""; position: absolute; left: 50%; width: 0.625rem; aspect-ratio: 1; translate: -50% 0; border-radius: 50%;
  background:
    linear-gradient(45deg, transparent 42%, var(--thermostat-metal-dk) 42% 58%, transparent 58%),
    radial-gradient(circle at 35% 35%, var(--thermostat-metal-hi), var(--thermostat-metal-lo));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--thermostat-metal-dk) 50%, transparent), 0 1px 0 var(--thermostat-metal-hi);
}
.thermostat__device::before { top: 0.875rem; }
.thermostat__device::after { bottom: 0.875rem; }

/* Dial: the slider. Bezel (static sheen), knurled ring (rotates), glass face */
.thermostat__dial {
  position: relative; width: min(100%, 17rem); aspect-ratio: 1; border-radius: 50%;
  container-type: inline-size; -webkit-user-select: none; user-select: none;
}
.thermostat--js .thermostat__dial { cursor: grab; touch-action: none; }
.thermostat__dial.is-dragging { cursor: grabbing; }
.thermostat__dial:focus-visible { outline: 2px solid var(--primary); outline-offset: 4px; }
.thermostat__bezel {
  position: absolute; inset: 0; border-radius: 50%;
  background:
    repeating-radial-gradient(circle, color-mix(in srgb, var(--thermostat-metal-hi) 45%, transparent) 0 1px, transparent 1px 3px),
    conic-gradient(from 30deg, var(--thermostat-metal-hi), var(--thermostat-metal-lo) 12%, var(--thermostat-metal-hi) 26%, var(--thermostat-metal-mid) 40%, var(--thermostat-metal-hi) 52%, var(--thermostat-metal-lo) 64%, var(--thermostat-metal-hi) 78%, var(--thermostat-metal-mid) 90%, var(--thermostat-metal-hi));
  box-shadow:
    0 1.5rem 2.5rem -1rem color-mix(in srgb, var(--surface-deep) 45%, transparent),
    0 0.375rem 0.75rem -0.25rem color-mix(in srgb, var(--surface-deep) 30%, transparent),
    inset 0 2px 1px color-mix(in srgb, var(--surface-light) 85%, transparent),
    inset 0 -3px 6px color-mix(in srgb, var(--thermostat-metal-dk) 45%, transparent);
}
.thermostat__ring {
  position: absolute; inset: 0; border-radius: 50%; rotate: var(--thermostat-angle, 0deg);
  background: repeating-conic-gradient(color-mix(in srgb, var(--thermostat-metal-dk) 50%, transparent) 0deg 1.25deg, color-mix(in srgb, var(--surface-light) 45%, transparent) 1.25deg 2.5deg, transparent 2.5deg 4deg);
  -webkit-mask: radial-gradient(closest-side, transparent 80%, black calc(80% + 1px) 96%, transparent calc(96% + 1px));
  mask: radial-gradient(closest-side, transparent 80%, black calc(80% + 1px) 96%, transparent calc(96% + 1px));
  transition: rotate var(--dur-3) var(--ease-spring);
}
.thermostat__ring::after { /* set-point notch */
  content: ""; position: absolute; left: 50%; top: 3%; width: 2.4%; height: 8%; translate: -50% 0; border-radius: var(--radius-full);
  background: var(--thermostat-tint); box-shadow: 0 0 6px var(--thermostat-tint);
}
.thermostat__face {
  position: absolute; inset: 13%; overflow: hidden; border-radius: 50%;
  background: radial-gradient(circle at 50% 30%, color-mix(in srgb, var(--surface-deep) 78%, var(--thermostat-metal-lo)), var(--surface-deep) 72%);
  box-shadow:
    0 0 0 3px color-mix(in srgb, var(--thermostat-metal-dk) 80%, var(--surface-deep)),
    0 0 0 4px color-mix(in srgb, var(--surface-light) 60%, transparent),
    inset 0 0.75rem 1.5rem color-mix(in srgb, var(--surface-deep) 85%, transparent);
}

/* Arc: a conic cool → heat gradient masked to a band, revealed up to the set point */
.thermostat__track, .thermostat__arc {
  --thermostat-band: radial-gradient(closest-side, transparent 65%, black calc(65% + 1px) 74%, transparent calc(74% + 1px));
  position: absolute; inset: 0; border-radius: 50%;
}
.thermostat__track {
  background: color-mix(in srgb, var(--text-inverse) 10%, transparent);
  -webkit-mask: var(--thermostat-band), conic-gradient(from 225deg, black 270deg, transparent 0);
  -webkit-mask-composite: source-in;
  mask: var(--thermostat-band), conic-gradient(from 225deg, black 270deg, transparent 0);
  mask-composite: intersect;
}
.thermostat__glow { position: absolute; inset: 0; filter: drop-shadow(0 0 0.375rem color-mix(in srgb, var(--thermostat-tint) 55%, transparent)); }
.thermostat__arc {
  background: conic-gradient(from 225deg, var(--thermostat-cool), color-mix(in srgb, var(--thermostat-cool) 50%, var(--thermostat-heat)) 135deg, var(--thermostat-heat) 270deg);
  -webkit-mask: var(--thermostat-band), conic-gradient(from 225deg, black var(--thermostat-sweep), transparent 0);
  -webkit-mask-composite: source-in;
  mask: var(--thermostat-band), conic-gradient(from 225deg, black var(--thermostat-sweep), transparent 0);
  mask-composite: intersect;
  transition: --thermostat-sweep var(--dur-3) var(--ease-spring);
}
.thermostat__ticks { position: absolute; inset: 0; width: 100%; height: 100%; }
.thermostat__ticks path { fill: none; }
.thermostat__ticks-minor { stroke: color-mix(in srgb, var(--text-inverse) 30%, transparent); stroke-width: 6; stroke-dasharray: 0.07 0.93; stroke-dashoffset: -0.465; }
.thermostat__ticks-major { stroke: color-mix(in srgb, var(--text-inverse) 75%, transparent); stroke-width: 11; stroke-dasharray: 0.12 4.88; stroke-dashoffset: -0.44; }
.thermostat__ticks text { fill: var(--text-inverse-muted); font: 500 9px var(--font-mono); }
.thermostat__cap { position: absolute; inset: 0; rotate: var(--thermostat-angle, 0deg); transition: rotate var(--dur-3) var(--ease-spring); }
.thermostat__cap::before {
  content: ""; position: absolute; left: 50%; top: 15%; width: 7%; aspect-ratio: 1; translate: -50% -50%; border-radius: 50%;
  background: var(--surface-light);
  box-shadow: 0 0 0 2px var(--thermostat-tint), 0 0 12px 2px color-mix(in srgb, var(--thermostat-tint) 70%, transparent);
}

/* Readout with odometer digits */
.thermostat__readout { position: absolute; inset: 0; display: grid; place-content: center; justify-items: center; gap: 0.25rem; color: var(--text-inverse); }
.thermostat__mode-label, .thermostat__indoor { color: var(--text-inverse-muted); font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.thermostat__indoor { font-weight: 500; letter-spacing: 0.04em; }
.thermostat__digits { display: flex; align-items: flex-start; font: 600 3.5rem/1 var(--font-display); font-size: 21cqi; letter-spacing: -0.04em; font-variant-numeric: tabular-nums; }
.thermostat__digit { display: block; height: 1em; overflow: hidden; }
.thermostat__strip { display: block; translate: 0 calc(var(--thermostat-d) * -1em); transition: translate var(--dur-4) var(--ease-spring); }
.thermostat__strip > span { display: block; height: 1em; }
.thermostat__deg { margin-left: 0.06em; color: var(--text-inverse-muted); font-size: 0.3em; font-weight: 500; line-height: 1.7; letter-spacing: 0; }
.thermostat__gloss {
  position: absolute; left: 12%; right: 12%; top: 3%; height: 46%; border-radius: 50% / 60% 60% 40% 40%;
  background: linear-gradient(color-mix(in srgb, var(--surface-light) 18%, transparent), transparent 70%);
}

/* No JS: a native range in place of the face. Hidden while scripting is on; a 3s failsafe shows it if the script never runs */
.thermostat__fallback {
  position: absolute; inset: 13%; z-index: 1; display: grid; place-content: center; justify-items: center; gap: 0.5rem; padding: 0 14%;
  border-radius: 50%; background: var(--surface-deep); color: var(--text-inverse); font: 600 0.8125rem/1.3 var(--font-sans); text-align: center;
}
.thermostat__range { width: 100%; min-height: 1.5rem; margin: 0; accent-color: var(--thermostat-heat); }
.thermostat__range:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.thermostat__range-scale { display: flex; justify-content: space-between; width: 100%; color: var(--text-inverse-muted); font: 500 0.6875rem var(--font-mono); }
@media (scripting: enabled) {
  .thermostat__fallback { visibility: hidden; animation: thermostat-failsafe 1ms 3s forwards; }
}
.thermostat--js .thermostat__fallback { display: none; }
.thermostat__hint { margin: -0.25rem 0 0; color: color-mix(in srgb, var(--text-main) 78%, var(--thermostat-metal-mid)); font: 500 0.75rem/1.3 var(--font-mono); }
.thermostat__hint[hidden] { display: none; }

/* Mode rockers: latching keys in a recessed tray, LEDs glow when on */
.thermostat__modes { width: 100%; min-width: 0; margin: 0; padding: 0; border: 0; }
.thermostat__legend { margin-bottom: 0.5rem; padding: 0; color: color-mix(in srgb, var(--text-main) 80%, var(--thermostat-metal-dk)); font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }
.thermostat__rockers {
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.375rem; padding: 0.375rem; border-radius: var(--radius-lg);
  background: linear-gradient(var(--thermostat-metal-lo), var(--thermostat-metal-mid));
  box-shadow: inset 0 2px 4px color-mix(in srgb, var(--surface-deep) 35%, transparent), 0 1px 0 color-mix(in srgb, var(--surface-light) 80%, transparent);
}
.thermostat__rocker {
  position: relative; display: grid; justify-items: center; align-content: center; gap: 0.4375rem; min-height: 3.5rem; border-radius: var(--radius-md);
  background: linear-gradient(var(--thermostat-metal-hi), var(--thermostat-metal-mid));
  box-shadow: 0 2px 0 var(--thermostat-metal-dk), 0 4px 6px -2px color-mix(in srgb, var(--surface-deep) 40%, transparent), inset 0 1px 0 var(--surface-light);
  color: var(--text-main); font: 600 0.875rem/1 var(--font-sans); cursor: pointer;
  transition: translate var(--dur-1) var(--ease-out);
}
.thermostat__rocker--heat { --thermostat-led: var(--thermostat-heat); }
.thermostat__rocker--cool { --thermostat-led: var(--thermostat-cool); }
.thermostat__rocker--auto { --thermostat-led: var(--thermostat-auto); }
.thermostat__radio { position: absolute; inset: 0; z-index: 1; width: 100%; height: 100%; margin: 0; opacity: 0; cursor: pointer; }
.thermostat__rocker:active { translate: 0 2px; }
.thermostat__rocker:has(:checked) {
  translate: 0 2px; background: linear-gradient(var(--thermostat-metal-mid), var(--thermostat-metal-hi));
  box-shadow: 0 0 0 var(--thermostat-metal-dk), inset 0 2px 4px color-mix(in srgb, var(--surface-deep) 30%, transparent);
}
.thermostat__rocker:has(:focus-visible) { outline: 2px solid var(--primary); outline-offset: 3px; }
@supports not selector(:has(*)) {
  .thermostat__radio:focus-visible + .thermostat__led { outline: 2px solid var(--primary); outline-offset: 4px; }
}
.thermostat__led {
  position: relative; width: 0.5rem; height: 0.5rem; border-radius: 50%;
  background: color-mix(in srgb, var(--thermostat-metal-dk) 75%, var(--surface-deep));
  box-shadow: inset 0 1px 1px color-mix(in srgb, var(--surface-deep) 60%, transparent), 0 1px 0 color-mix(in srgb, var(--surface-light) 70%, transparent);
  transition: background-color var(--dur-2) var(--ease-out);
}
.thermostat__led::after {
  content: ""; position: absolute; inset: -0.4375rem; border-radius: 50%;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--thermostat-led) 75%, transparent), transparent);
  opacity: 0; transition: opacity var(--dur-3) var(--ease-out);
}
.thermostat__radio:checked + .thermostat__led { background: var(--thermostat-led); }
.thermostat__radio:checked + .thermostat__led::after { opacity: 1; }

/* Fan toggle: recessed track, metal knob, blades turn when on */
.thermostat__fan { position: relative; display: flex; align-items: center; gap: 0.75rem; width: 100%; min-height: 2.75rem; cursor: pointer; font: 600 0.875rem var(--font-sans); }
.thermostat__fan-icon { flex: none; fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; transition: rotate var(--dur-5) var(--ease-spring); }
.thermostat__fan:has(:checked) .thermostat__fan-icon { rotate: 180deg; }
.thermostat__fan-label { flex: 1; }
.thermostat__fan-input { position: absolute; width: 1px; height: 1px; margin: 0; opacity: 0; pointer-events: none; }
.thermostat__fan-track {
  position: relative; flex: none; width: 3.25rem; height: 1.75rem; border-radius: var(--radius-full);
  background: linear-gradient(var(--thermostat-metal-lo), var(--thermostat-metal-mid));
  box-shadow: inset 0 2px 4px color-mix(in srgb, var(--surface-deep) 40%, transparent), 0 1px 0 var(--surface-light);
}
.thermostat__fan-knob {
  position: absolute; top: 0.1875rem; left: 0.1875rem; width: 1.375rem; height: 1.375rem; border-radius: 50%;
  background: radial-gradient(circle at 35% 30%, var(--thermostat-metal-hi), var(--thermostat-metal-mid));
  box-shadow: 0 2px 3px color-mix(in srgb, var(--surface-deep) 40%, transparent), inset 0 1px 0 var(--surface-light);
  transition: translate var(--dur-3) var(--ease-spring);
}
.thermostat__fan-input:checked + .thermostat__fan-track { background: linear-gradient(color-mix(in srgb, var(--thermostat-cool) 65%, var(--thermostat-metal-dk)), var(--thermostat-cool)); }
.thermostat__fan-input:checked + .thermostat__fan-track .thermostat__fan-knob { translate: 1.5rem 0; }
.thermostat__fan-input:focus-visible + .thermostat__fan-track { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Recommended plan: one card per mode, swapped with :has(); all three show where :has() is missing */
.thermostat__plans { grid-area: plans; }
.thermostat__plan {
  position: relative; overflow: hidden; padding: 1.75rem 1.5rem 1.5rem; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: var(--shadow-xl), inset 0 0 0 1px var(--border-subtle);
}
.thermostat__plan + .thermostat__plan { margin-top: 1rem; }
.thermostat__plan::before { content: ""; position: absolute; inset: 0 0 auto; height: 4px; background: linear-gradient(90deg, var(--thermostat-cool), var(--thermostat-heat)); }
.thermostat__plan-kicker { margin: 0; color: var(--text-muted); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.thermostat__plan-name { margin: 0.625rem 0 0; font: 600 1.75rem/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.thermostat__plan-price { margin: 0.375rem 0 0; color: var(--text-muted); }
.thermostat__plan-price strong { color: var(--text-main); font: 600 1.375rem var(--font-display); }
.thermostat__plan-list { display: grid; gap: 0.625rem; margin: 1.25rem 0 0; padding: 0; list-style: none; }
.thermostat__plan-list li { position: relative; padding-left: 1.75rem; line-height: 1.45; }
.thermostat__plan-list li::before {
  content: ""; position: absolute; left: 0; top: 0.0625rem; width: 1.25rem; height: 1.25rem; border-radius: 50%;
  background: color-mix(in srgb, var(--primary) 12%, transparent);
}
.thermostat__plan-list li::after {
  content: ""; position: absolute; left: 0.4375rem; top: 0.25rem; width: 0.3125rem; height: 0.625rem;
  border: solid var(--primary); border-width: 0 2px 2px 0; rotate: 45deg;
}
.thermostat__plan-cta {
  display: inline-flex; align-items: center; justify-content: center; min-height: 3rem; margin-top: 1.5rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font-weight: 600; text-decoration: none;
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 10px 24px -10px var(--primary);
  transition: translate var(--dur-2) var(--ease-spring), scale var(--dur-1) var(--ease-out);
}
.thermostat__plan-cta:hover { translate: 0 -1px; }
.thermostat__plan-cta:active { scale: 0.97; }
.thermostat__plan-cta:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
@supports selector(:has(*)) {
  .thermostat__plan { display: none; }
  .thermostat__plan + .thermostat__plan { margin-top: 0; }
  .thermostat:has(.thermostat__radio[value="heat"]:checked) .thermostat__plan--heat,
  .thermostat:has(.thermostat__radio[value="cool"]:checked) .thermostat__plan--cool,
  .thermostat:has(.thermostat__radio[value="auto"]:checked) .thermostat__plan--auto { display: block; animation: thermostat-plan-in var(--dur-4) var(--ease-out); }
}

@media (min-width: 768px) {
  .thermostat__inner { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); grid-template-areas: "head device" "plans device"; column-gap: 3rem; align-items: start; }
  .thermostat__device { align-self: center; }
}
@media (min-width: 1024px) {
  .thermostat__inner { grid-template-columns: 1fr 1.05fr; column-gap: 5rem; }
  .thermostat__dial { width: min(100%, 18.5rem); }
  .thermostat__device { width: min(100%, 24rem); }
}
@media (prefers-reduced-motion: reduce) {
  .thermostat__plan { animation: none !important; }
}
@keyframes thermostat-failsafe { to { visibility: visible; } }
@keyframes thermostat-plan-in { from { opacity: 0; translate: 0 0.5rem; filter: blur(4px); } }
```

## JS

```js
const MIN = 60;
const MAX = 85;
const SWEEP = 270; // degrees of travel, centred on 12 o'clock
const MODES = { heat: ['heating', 'Heating to'], cool: ['cooling', 'Cooling to'], auto: ['on auto', 'Holding at'] };

document.querySelectorAll('[data-thermostat]').forEach((root) => {
  const form = root.querySelector('.thermostat__device');
  const dial = root.querySelector('.thermostat__dial');
  const ring = root.querySelector('.thermostat__ring');
  const range = root.querySelector('.thermostat__range');
  const label = root.querySelector('.thermostat__mode-label');
  const digits = [...root.querySelectorAll('.thermostat__digit')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const spring = getComputedStyle(root).getPropertyValue('--ease-spring').trim() || 'ease-out';
  let value = Number(range.value);

  // Enhance: the dial becomes the slider; the native range steps aside but stays in sync for form posts
  root.classList.add('thermostat--js');
  root.querySelector('.thermostat__hint').hidden = false;
  dial.tabIndex = 0;
  Object.entries({ role: 'slider', 'aria-label': 'Target temperature', 'aria-valuemin': MIN, 'aria-valuemax': MAX })
    .forEach(([name, val]) => dial.setAttribute(name, val));

  const render = () => {
    const sweep = ((value - MIN) / (MAX - MIN)) * SWEEP;
    const [word, prefix] = MODES[form.elements.mode.value] || MODES.heat;
    dial.style.setProperty('--thermostat-angle', `${sweep - SWEEP / 2}deg`);
    dial.style.setProperty('--thermostat-sweep', `${sweep}deg`);
    String(value).split('').forEach((d, i) => digits[i]?.style.setProperty('--thermostat-d', d));
    label.textContent = prefix;
    dial.setAttribute('aria-valuenow', value);
    dial.setAttribute('aria-valuetext', `${value} degrees, ${word}`);
    range.value = value;
  };

  // Snap to a detent: the ring springs there in CSS, and a tiny scale dip reads as the click
  const set = (next) => {
    next = Math.min(MAX, Math.max(MIN, Math.round(next)));
    if (next === value) return;
    value = next;
    render();
    if (!reduce.matches) ring.animate([{ scale: '0.975' }, { scale: '1' }], { duration: 180, easing: spring });
  };

  // Drag around the dial: the pointer's angle (0° at 12 o'clock) maps onto the 270° scale.
  // The centre and the gap at the bottom are dead zones, so the value never jumps end to end.
  const fromPointer = ({ clientX, clientY }) => {
    const r = dial.getBoundingClientRect();
    const x = clientX - (r.left + r.width / 2);
    const y = clientY - (r.top + r.height / 2);
    const deg = (Math.atan2(x, -y) * 180) / Math.PI;
    if (Math.hypot(x, y) < r.width * 0.15 || Math.abs(deg) > SWEEP / 2 + 5) return;
    set(MIN + ((deg + SWEEP / 2) / SWEEP) * (MAX - MIN));
  };
  let frame = 0;
  let last = null;
  dial.addEventListener('pointerdown', (e) => {
    if (e.button !== 0) return;
    dial.setPointerCapture(e.pointerId);
    dial.focus({ preventScroll: true });
    dial.classList.add('is-dragging');
    fromPointer(e);
  });
  dial.addEventListener('pointermove', (e) => {
    if (!dial.hasPointerCapture(e.pointerId)) return;
    last = e;
    frame ||= requestAnimationFrame(() => { frame = 0; fromPointer(last); });
  }, { passive: true });
  const stop = () => dial.classList.remove('is-dragging');
  dial.addEventListener('pointerup', stop);
  dial.addEventListener('pointercancel', stop);

  // APG slider keys: arrows ±1, Page Up/Down ±5, Home/End to the ends
  dial.addEventListener('keydown', (e) => {
    const step = { ArrowUp: 1, ArrowRight: 1, ArrowDown: -1, ArrowLeft: -1, PageUp: 5, PageDown: -5 }[e.key];
    if (step) set(value + step);
    else if (e.key === 'Home') set(MIN);
    else if (e.key === 'End') set(MAX);
    else return;
    e.preventDefault();
  });

  // Wheel turns the dial only while it has focus, so scrolling past it never changes the temperature
  let wheel = 0;
  dial.addEventListener('wheel', (e) => {
    if (document.activeElement !== dial) return;
    e.preventDefault();
    wheel += e.deltaMode === 1 ? e.deltaY * 40 : e.deltaY;
    if (Math.abs(wheel) < 40) return;
    set(value - Math.sign(wheel));
    wheel = 0;
  }, { passive: false });

  form.addEventListener('change', (e) => { if (e.target.name === 'mode') render(); });
  render();
});
```

## Notes

- APG slider: the dial is `role="slider"` with `aria-valuemin/max/now` and an `aria-valuetext` such as "72 degrees, heating" that also updates when the mode changes. Arrows step ±1, Page Up/Down ±5, Home/End jump to 60/85. The modes are native radios in a `fieldset` (arrow keys built in) and the fan is a native checkbox with `role="switch"`.
- No JS: a native range input (`name="temp"`) replaces the face inside the bezel, and the form still posts temperature, mode and fan. With scripting on, that range is hidden from first paint, and a 3s CSS failsafe brings it back if the script never runs. The plan swap is pure CSS `:has()`; browsers without `:has()` list all three plans.
- Input: drag anywhere on the dial (the pointer's angle, rAF-throttled, with dead zones at the centre and the bottom gap), the wheel while the dial is focused (a non-passive listener, so it never hijacks page scroll), or the keys. The dial has `touch-action: none`, so on touch screens page scrolling starts outside it.
- Reduced motion: the detent spring, digit roll, arc sweep and tint changes become instant through the duration tokens, and the click scale is skipped.
- Contrast: the readout uses `--text-inverse` on the glass (14:1+) and labels use `--text-inverse-muted` (5.7:1). Rocker labels, the legend and the hint sit on the light metal at 6:1 or better. Heat, cool and auto colours only drive arcs, LEDs and glows, never text.
- Support: `@property` animates the arc sweep and the section tint (without it they switch instantly); container query units size the readout (rem fallback); `mask-composite` shapes the arc band. Retheme with the four metal and three mode variables.
