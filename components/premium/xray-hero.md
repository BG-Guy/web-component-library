# X-Ray Reveal Hero

A dark inspection-company hero. Beside the headline sits a photo of a house, and a glass lens moves over it. Inside the lens the walls turn to x-ray: a cyan-on-blueprint schematic of supply pipes, knob-and-tube wiring, ducts and studs. A label on the lens names what's underneath ("Copper supply · 1998"). When the hero scrolls into view, the lens takes a short look around (under 5s) and settles on a hotspot. After that it follows the mouse with a little weight. On touch you drag it or tap where you want it, and keyboard users get a "Move lens" toggle and the arrow keys. On phones the copy stacks above the photo and the lens and labels scale with the photo through container units. Depends on `tokens/variables.css`.

**Motion:** copy rises out of a blur (`--dur-5`, `--ease-out`, 90ms steps) · stage fade-up and lens pop (`--ease-spring`) · one-off look-around drift (3.6s, eased, JS) · weighted lens follow (rAF lerp) · label flips sides through a registered `@property` (`--dur-4`, `--ease-spring`) and flickers in on each new hotspot (`--dur-3`).

## HTML

```html
<section class="xray" aria-labelledby="xray-title" data-xray>
  <div class="xray__inner">
    <div class="xray__copy">
      <p class="xray__eyebrow" style="--xray-i: 0"><span class="xray__eyebrow-dot"></span>Home inspections · Springfield</p>
      <h1 id="xray-title" class="xray__title" style="--xray-i: 1">See what <span class="xray__glow">others miss.</span></h1>
      <p class="xray__lead" style="--xray-i: 2">Thermal imaging, moisture meters and borescopes find the leak, the old wiring and the failing duct behind your walls before they cost you. Your report lands within 24 hours.</p>
      <div class="xray__actions" style="--xray-i: 3">
        <a class="xray__btn xray__btn--primary" href="#book">
          Book an inspection
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="xray__btn xray__btn--ghost" href="#sample">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8zM14 3v5h5M9 13h6M9 17h4" /></svg>
          See a sample report
        </a>
      </div>
      <dl class="xray__stats" style="--xray-i: 4">
        <div><dt>Homes inspected</dt><dd>2,400+</dd></div>
        <div><dt>Report turnaround</dt><dd>24 h</dd></div>
        <div><dt>Average rating</dt><dd>4.9/5</dd></div>
      </dl>
    </div>

    <figure class="xray__figure">
      <div class="xray__stage">
        <img class="xray__photo" src="house-exterior.jpg" alt="Two-storey family home in Springfield, seen from the street" width="1200" height="900" loading="eager" fetchpriority="high" decoding="async">
        <div class="xray__plan" aria-hidden="true">
          <svg class="xray__drawing" viewBox="0 0 1200 900" preserveAspectRatio="xMidYMid slice" focusable="false">
            <path class="xray__studs" d="M180 430H1020" stroke-width="220" />
            <path class="xray__studs" d="M180 650H1020" stroke-width="220" />
            <path class="xray__line" d="M140 320 600 100l460 220M180 320v440M1020 320v440M180 320h840M180 540h840M40 760h1120" />
            <path class="xray__line xray__line--dash" d="M180 760v120h840V760" />
            <path class="xray__line xray__line--thin" d="M180 70h840M180 60v20M1020 60v20" />
            <text class="xray__note" x="600" y="52" text-anchor="middle">38′–6″</text>
            <rect class="xray__box" x="226" y="790" width="64" height="80" rx="10" />
            <text class="xray__note" x="258" y="836" text-anchor="middle">WH</text>
            <path class="xray__pipe" d="M246 790v-30h54V516" />
            <path class="xray__pipe xray__pipe--hot" d="M270 790v-14h46V516" />
            <path class="xray__valve" d="m292 642 16 16v-16l-16 16z" />
            <circle class="xray__fit" cx="300" cy="760" r="6" />
            <circle class="xray__fit" cx="316" cy="776" r="6" />
            <path class="xray__line xray__line--thin" d="M240 516h170v14a12 12 0 0 1-12 12H252a12 12 0 0 1-12-12z" />
            <path class="xray__drain" d="M404 542v338M404 320V176" />
            <text class="xray__note" x="328" y="700">CU ¾″</text>
            <rect class="xray__box" x="526" y="786" width="104" height="84" rx="8" />
            <text class="xray__note" x="578" y="834" text-anchor="middle">FURNACE</text>
            <g class="xray__duct"><path d="M578 786V556H462M578 556h168M704 556V432" /><path d="M578 786V556H462M578 556h168M704 556V432" /></g>
            <path class="xray__line xray__line--thin" d="M684 416h40M684 424h40" />
            <text class="xray__note" x="470" y="598">6″ FLEX</text>
            <rect class="xray__box" x="904" y="786" width="60" height="84" rx="4" />
            <path class="xray__line xray__line--thin" d="M916 804h36M916 818h36M916 832h36M916 846h36" />
            <text class="xray__note" x="894" y="834" text-anchor="end">200A</text>
            <path class="xray__wire" d="M964 800h26V336H620" />
            <path class="xray__wire" d="M934 786V620H836v56" />
            <rect class="xray__box" x="824" y="676" width="24" height="32" rx="4" />
            <g class="xray__knobs"><circle cx="660" cy="336" r="5" /><circle cx="720" cy="336" r="5" /><circle cx="780" cy="336" r="5" /><circle cx="840" cy="336" r="5" /><circle cx="900" cy="336" r="5" /><circle cx="960" cy="336" r="5" /><circle cx="990" cy="420" r="5" /><circle cx="990" cy="500" r="5" /><circle cx="990" cy="580" r="5" /><circle cx="990" cy="660" r="5" /><circle cx="990" cy="740" r="5" /></g>
          </svg>
          <span class="xray__spot" style="--xray-sx: 25.67; --xray-sy: 71.11" data-label="Copper supply · 1998"></span>
          <span class="xray__spot" style="--xray-sx: 45; --xray-sy: 48.89" data-label="2×4 studs · 16″ centres"></span>
          <span class="xray__spot" style="--xray-sx: 68.33; --xray-sy: 37.33" data-label="Knob-and-tube wiring · 1952"></span>
          <span class="xray__spot" style="--xray-sx: 54.17; --xray-sy: 61.78" data-label="Flex duct · 2011"></span>
          <span class="xray__spot" style="--xray-sx: 21.5; --xray-sy: 92.2" data-label="Water heater · 2009"></span>
          <span class="xray__spot" style="--xray-sx: 77.83; --xray-sy: 92" data-label="Breaker panel · 200A"></span>
        </div>
        <div class="xray__lens" aria-hidden="true"></div>
        <p class="xray__label" aria-hidden="true"><span class="xray__label-dot"></span><span class="xray__label-text">Copper supply · 1998</span></p>
        <div class="xray__hud" aria-hidden="true">
          <span class="xray__chip"><span class="xray__chip-dot"></span>X-ray view</span>
          <span class="xray__chip xray__readout">X 25.7 · Y 71.1</span>
          <span class="xray__chip xray__half xray__half--photo">Photo</span>
          <span class="xray__chip xray__half xray__half--plan">X-ray</span>
        </div>
      </div>
      <figcaption class="xray__caption">
        <ul class="xray__legend" role="list" aria-label="X-ray key">
          <li><span class="xray__key xray__key--pipe"></span>Supply pipes</li>
          <li><span class="xray__key xray__key--wire"></span>Wiring</li>
          <li><span class="xray__key xray__key--duct"></span>Ducts</li>
          <li><span class="xray__key xray__key--stud"></span>Studs</li>
        </ul>
        <span class="xray__control">
          <button class="xray__toggle" type="button" aria-pressed="false" aria-describedby="xray-keys" hidden>
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 3v18M3 12h18M12 3 9 6M12 3l3 3M12 21l-3-3M12 21l3-3M3 12l3-3M3 12l3 3M21 12l-3-3M21 12l-3 3" /></svg>
            Move lens
          </button>
          <span class="xray__keys" id="xray-keys">Arrow keys move it · Esc stops</span>
        </span>
      </figcaption>
    </figure>
  </div>
  <p class="xray__live" role="status"></p>
</section>
```

## CSS

```css
@property --xray-fx { syntax: "<number>"; inherits: false; initial-value: 0; }
@property --xray-fy { syntax: "<number>"; inherits: false; initial-value: 0; }

/* Section: deep surface, a faint blueprint grid and a cyan glow behind the photo */
.xray {
  --xray-ink: color-mix(in srgb, color-mix(in srgb, var(--primary-2), var(--primary)) 45%, var(--text-inverse));
  --xray-bright: color-mix(in srgb, var(--primary-2) 30%, var(--text-inverse));
  --xray-paper: color-mix(in srgb, var(--primary) 24%, var(--surface-deep));
  position: relative; isolation: isolate; overflow: clip;
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}
.xray::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background:
    linear-gradient(color-mix(in srgb, var(--xray-ink) 7%, transparent) 1px, transparent 1px) 0 0 / 3rem 3rem,
    linear-gradient(90deg, color-mix(in srgb, var(--xray-ink) 7%, transparent) 1px, transparent 1px) 0 0 / 3rem 3rem;
  -webkit-mask-image: radial-gradient(ellipse 80% 70% at 70% 45%, black, transparent 75%);
  mask-image: radial-gradient(ellipse 80% 70% at 70% 45%, black, transparent 75%);
}
.xray::after {
  content: ""; position: absolute; z-index: -1; top: 15%; right: -15%; width: 75%; aspect-ratio: 1; border-radius: 50%; pointer-events: none;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 30%, transparent), transparent);
}
.xray__inner {
  display: grid; gap: 3rem; align-items: center;
  max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4.5rem, 10vw, 7.5rem) var(--gutter) clamp(4rem, 8vw, 6.5rem);
}

/* Copy: rises out of a blur, in order */
.xray__eyebrow, .xray__title, .xray__lead, .xray__actions, .xray__stats {
  animation: xray-rise var(--dur-5) var(--ease-out) calc(var(--xray-i, 0) * 90ms + 100ms) both;
}
.xray__eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.375rem 0.875rem 0.375rem 0.625rem;
  border-radius: var(--radius-full); background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  color: var(--text-inverse-muted); font: 500 0.75rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
}
.xray__eyebrow-dot { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--xray-bright); box-shadow: 0 0 0 3px color-mix(in srgb, var(--xray-bright) 22%, transparent); }
.xray__title { margin: 1.25rem 0 0; font: 600 clamp(2.75rem, 1.5rem + 5vw, 5.25rem)/0.98 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.xray__glow {
  padding-bottom: 0.06em;
  background: linear-gradient(100deg, var(--text-inverse) 0%, var(--xray-bright) 45%, var(--xray-ink) 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.xray__lead { max-width: 34rem; margin: 1.5rem 0 0; color: var(--text-inverse-muted); font-size: clamp(1.0625rem, 1rem + 0.4vw, 1.25rem); line-height: 1.6; }
.xray__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2.25rem; }
.xray__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; height: 3rem; padding: 0 1.375rem;
  border-radius: var(--radius-full); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-2) var(--ease-out), box-shadow var(--dur-3) var(--ease-out), background-color var(--dur-2) var(--ease-out);
}
.xray__btn svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.xray__btn:hover { transform: translateY(-1px); }
.xray__btn:active { transform: scale(0.97); }
.xray__btn--primary { background: var(--surface-light); color: var(--text-main); box-shadow: 0 12px 40px -12px color-mix(in srgb, var(--xray-ink) 80%, transparent); }
.xray__btn--primary:hover svg { transform: translateX(3px); }
.xray__btn--ghost { background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.xray__btn--ghost:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.xray :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.xray__stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; max-width: 30rem; margin: 2.75rem 0 0; padding-top: 1.5rem; border-top: 1px solid var(--border-inverse); }
.xray__stats div { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.375rem; }
.xray__stats dt { color: var(--text-inverse-muted); font: 500 0.6875rem/1.3 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.xray__stats dd { margin: 0; font: 600 clamp(1.25rem, 1rem + 1vw, 1.625rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }

/* Stage: photo, the masked blueprint, lens, label and HUD. A size container, so the lens can use cqw/cqh */
.xray__figure { margin: 0; animation: xray-stage-in var(--dur-5) var(--ease-out) 350ms both; }
.xray__stage {
  --xray-x: 25.67; --xray-y: 71.11; --xray-r: clamp(3.5rem, 15cqw, 7rem);
  position: relative; container-type: size; width: 100%; aspect-ratio: 4 / 3; overflow: hidden;
  border-radius: var(--radius-2xl); background: var(--xray-paper); cursor: crosshair; -webkit-user-select: none; user-select: none;
  box-shadow: 0 40px 90px -40px color-mix(in srgb, var(--primary) 55%, transparent), 0 30px 60px -30px color-mix(in srgb, var(--surface-deep) 90%, transparent);
}
.xray__stage::after {
  content: ""; position: absolute; inset: 0; z-index: 2; border-radius: inherit; pointer-events: none;
  box-shadow: inset 0 0 0 1px var(--border-inverse);
  background:
    linear-gradient(to bottom, color-mix(in srgb, var(--surface-deep) 40%, transparent), transparent 22%),
    linear-gradient(to top, color-mix(in srgb, var(--surface-deep) 30%, transparent), transparent 30%);
}
.xray__photo { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; filter: saturate(0.85) contrast(1.05); }

/* Blueprint layer, seen only through a soft-edged circle at --xray-x/--xray-y */
.xray__plan {
  position: absolute; inset: 0; z-index: 1;
  background:
    linear-gradient(color-mix(in srgb, var(--xray-ink) 10%, transparent) 1px, transparent 1px) 0 0 / 5% 6.667%,
    linear-gradient(90deg, color-mix(in srgb, var(--xray-ink) 10%, transparent) 1px, transparent 1px) 0 0 / 5% 6.667%,
    radial-gradient(110% 90% at 50% 40%, color-mix(in srgb, var(--primary) 34%, var(--surface-deep)), var(--xray-paper));
  -webkit-mask-image: radial-gradient(circle var(--xray-r) at calc(var(--xray-x) * 1%) calc(var(--xray-y) * 1%), black 74%, transparent 97%);
  mask-image: radial-gradient(circle var(--xray-r) at calc(var(--xray-x) * 1%) calc(var(--xray-y) * 1%), black 74%, transparent 97%);
}
.xray__drawing {
  position: absolute; inset: 0; width: 100%; height: 100%; fill: none; stroke-linecap: round; stroke-linejoin: round;
  filter: drop-shadow(0 0 4px color-mix(in srgb, var(--xray-ink) 55%, transparent));
}
.xray__drawing :is(.xray__line, .xray__pipe, .xray__wire, .xray__drain, .xray__box, .xray__fit, .xray__knobs circle) { vector-effect: non-scaling-stroke; }
/* Studs: one very thick dashed stroke per storey draws every stud (butt caps keep them thin) */
.xray__studs { stroke: var(--xray-ink); stroke-linecap: butt; stroke-dasharray: 2 46; opacity: 0.22; }
.xray__line { stroke: var(--xray-ink); stroke-width: 1.5; opacity: 0.8; }
.xray__line--dash { stroke-dasharray: 8 6; }
.xray__line--thin { stroke-width: 1; }
.xray__pipe { stroke: var(--xray-bright); stroke-width: 3; }
.xray__pipe--hot { stroke: var(--xray-ink); }
.xray__drain { stroke: var(--xray-ink); stroke-width: 5; opacity: 0.5; }
.xray__valve { fill: var(--xray-bright); stroke: none; }
.xray__fit, .xray__knobs circle { fill: var(--xray-paper); stroke: var(--xray-bright); stroke-width: 1.5; }
.xray__knobs circle { stroke: var(--xray-ink); }
.xray__wire { stroke: var(--xray-ink); stroke-width: 1.5; stroke-dasharray: 6 4; }
.xray__box { fill: color-mix(in srgb, var(--xray-ink) 12%, transparent); stroke: var(--xray-ink); stroke-width: 1.5; }
.xray__duct path:first-child { stroke: color-mix(in srgb, var(--xray-ink) 75%, transparent); stroke-width: 26; }
.xray__duct path:last-child { stroke: var(--xray-paper); stroke-width: 21; }
.xray__note { fill: var(--xray-ink); font: 500 15px var(--font-mono); letter-spacing: 0.06em; }
.xray__spot {
  position: absolute; left: calc(var(--xray-sx) * 1%); top: calc(var(--xray-sy) * 1%); width: 1.125rem; height: 1.125rem; margin: -0.5625rem; border-radius: 50%;
  background: radial-gradient(circle, var(--xray-bright) 0 2px, transparent 2.5px);
  box-shadow: 0 0 0 1px var(--xray-bright), 0 0 0 5px color-mix(in srgb, var(--xray-bright) 18%, transparent);
}

/* Lens: glass bezel, specular highlight and crosshair ticks */
.xray__lens {
  position: absolute; top: 0; left: 0; z-index: 3; width: calc(var(--xray-r) * 2); aspect-ratio: 1; border-radius: 50%;
  translate: calc(var(--xray-x) * 1cqw - 50%) calc(var(--xray-y) * 1cqh - 50%);
  touch-action: none;
  box-shadow:
    inset 0 0 0 1px color-mix(in srgb, var(--text-inverse) 55%, transparent),
    inset 0 0 1.75rem color-mix(in srgb, var(--xray-ink) 30%, transparent),
    0 0 0 1px color-mix(in srgb, var(--surface-deep) 45%, transparent),
    0 0 2.5rem color-mix(in srgb, var(--xray-ink) 35%, transparent),
    0 1.25rem 2.5rem -0.75rem color-mix(in srgb, var(--surface-deep) 80%, transparent);
  animation: xray-lens-in var(--dur-5) var(--ease-spring) 900ms both;
}
.xray__lens::before {
  content: ""; position: absolute; inset: -0.375rem; border-radius: 50%;
  background: conic-gradient(from 210deg,
    color-mix(in srgb, var(--text-inverse) 75%, transparent),
    color-mix(in srgb, var(--xray-ink) 40%, transparent) 25%,
    color-mix(in srgb, var(--text-inverse) 15%, transparent) 50%,
    color-mix(in srgb, var(--xray-ink) 60%, transparent) 75%,
    color-mix(in srgb, var(--text-inverse) 75%, transparent));
  -webkit-mask: radial-gradient(closest-side, transparent calc(100% - 0.4375rem), black calc(100% - 0.375rem));
  mask: radial-gradient(closest-side, transparent calc(100% - 0.4375rem), black calc(100% - 0.375rem));
}
.xray__lens::after {
  content: ""; position: absolute; inset: 0; border-radius: 50%;
  background:
    radial-gradient(40% 24% at 32% 18%, color-mix(in srgb, var(--text-inverse) 26%, transparent), transparent 70%),
    radial-gradient(circle, var(--xray-ink) 0 1.5px, transparent 2px),
    linear-gradient(var(--xray-ink), var(--xray-ink)) 50% 0 / 1px 0.625rem no-repeat,
    linear-gradient(var(--xray-ink), var(--xray-ink)) 50% 100% / 1px 0.625rem no-repeat,
    linear-gradient(var(--xray-ink), var(--xray-ink)) 0 50% / 0.625rem 1px no-repeat,
    linear-gradient(var(--xray-ink), var(--xray-ink)) 100% 50% / 0.625rem 1px no-repeat;
}

/* Label rides on the lens and swings to the other side near the right or bottom edge */
.xray__label {
  --xray-fx: clamp(0, (var(--xray-x) - 58) * 100, 1);
  --xray-fy: clamp(0, (var(--xray-y) - 72) * 100, 1);
  position: absolute; top: 0; left: 0; z-index: 4; display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; white-space: nowrap; pointer-events: none;
  padding: 0.375rem 0.625rem 0.375rem 0.5rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 78%, transparent); color: var(--text-inverse); font: 500 0.75rem/1 var(--font-mono);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--xray-ink) 40%, transparent), var(--highlight-inverse);
  translate:
    calc(var(--xray-x) * 1cqw + (1 - 2 * var(--xray-fx)) * var(--xray-r) * 0.74 - var(--xray-fx) * 100%)
    calc(var(--xray-y) * 1cqh + (1 - 2 * var(--xray-fy)) * var(--xray-r) * 0.74 - var(--xray-fy) * 100%);
  transition: --xray-fx var(--dur-4) var(--ease-spring), --xray-fy var(--dur-4) var(--ease-spring);
  animation: xray-fade var(--dur-4) var(--ease-out) 1.1s both;
}
@supports (backdrop-filter: blur(1px)) {
  .xray__label, .xray__chip { backdrop-filter: blur(var(--blur-md)) saturate(1.3); }
}
.xray__label-dot { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--xray-bright); box-shadow: 0 0 0.5rem var(--xray-bright); }

/* HUD chips */
.xray__hud { position: absolute; inset: 0.875rem; z-index: 4; display: flex; justify-content: space-between; align-items: flex-start; pointer-events: none; }
.xray__chip {
  display: inline-flex; align-items: center; gap: 0.4375rem; padding: 0.3125rem 0.625rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 72%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse);
  color: var(--text-inverse); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; font-variant-numeric: tabular-nums;
}
.xray__chip-dot { width: 0.375rem; height: 0.375rem; border-radius: 50%; background: var(--xray-bright); }
.xray__half { display: none; }
@container (width < 26rem) {
  .xray__note, .xray__readout { display: none; }
}

/* Caption: key and the keyboard control */
.xray__caption { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.875rem 1.25rem; margin-top: 1rem; }
.xray__legend { display: flex; flex-wrap: wrap; gap: 0.5rem 1rem; margin: 0; padding: 0; list-style: none; color: var(--text-inverse-muted); font: 500 0.75rem/1.2 var(--font-mono); }
.xray__legend li { display: inline-flex; align-items: center; gap: 0.5rem; }
.xray__key { width: 1.25rem; height: 0.625rem; }
.xray__key--pipe { background: linear-gradient(var(--xray-bright), var(--xray-bright)) center / 100% 3px no-repeat; }
.xray__key--wire { background: repeating-linear-gradient(90deg, var(--xray-ink) 0 4px, transparent 4px 7px) center / 100% 1.5px no-repeat; }
.xray__key--duct { height: 0.5rem; box-shadow: inset 0 1.5px 0 var(--xray-ink), inset 0 -1.5px 0 var(--xray-ink); }
.xray__key--stud { background: repeating-linear-gradient(90deg, color-mix(in srgb, var(--xray-ink) 70%, transparent) 0 1px, transparent 1px 5px); }
.xray__control { display: inline-flex; flex-wrap: wrap; align-items: center; gap: 0.5rem 0.75rem; }
.xray__toggle {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 2.75rem; padding: 0 1rem 0 0.875rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse); font: 600 0.8125rem var(--font-sans);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: background-color var(--dur-2) var(--ease-out), box-shadow var(--dur-2) var(--ease-out);
}
.xray__toggle[hidden] { display: none; }
.xray__toggle:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.xray__toggle[aria-pressed="true"] { background: color-mix(in srgb, var(--xray-bright) 18%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--xray-bright) 60%, transparent); }
.xray__toggle svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.xray__keys { display: none; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); }
.xray.is-steering .xray__keys { display: inline; }
.xray__live { position: absolute; width: 1px; height: 1px; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }

/* No JS: a static half-and-half of photo and blueprint */
@media (scripting: none) {
  .xray__plan { -webkit-mask-image: none; mask-image: none; clip-path: inset(0 0 0 50%); }
  .xray__lens, .xray__label, .xray__readout { display: none; }
  .xray__half { display: inline-flex; }
  .xray__half--plan { margin-left: auto; }
  .xray__hud::before {
    content: ""; position: absolute; top: -0.875rem; bottom: -0.875rem; left: 50%; width: 2px; translate: -50% 0;
    background: var(--xray-ink); box-shadow: 0 0 1rem var(--xray-ink);
  }
  .xray__hud > :first-child { display: none; }
  .xray__stage { cursor: auto; }
}

@media (min-width: 1024px) {
  .xray__inner { grid-template-columns: 0.92fr 1.08fr; gap: 4rem; }
}
@media (prefers-reduced-motion: reduce) {
  .xray *, .xray *::before, .xray *::after { animation: none !important; }
}
@keyframes xray-rise { from { opacity: 0; transform: translateY(0.45em); filter: blur(10px); } }
@keyframes xray-stage-in { from { opacity: 0; transform: translateY(1rem) scale(0.97); filter: blur(8px); } }
@keyframes xray-lens-in { from { opacity: 0; scale: 0.6; } }
@keyframes xray-fade { from { opacity: 0; } }
```

## JS

```js
const clamp = (v) => Math.min(96, Math.max(4, v));
const ease = (t) => (t < 0.5 ? 4 * t ** 3 : 1 - (-2 * t + 2) ** 3 / 2);

document.querySelectorAll('[data-xray]').forEach((root) => {
  const $ = (part) => root.querySelector(`.xray__${part}`);
  const [stage, lens, pill, text, readout, toggle, live] = ['stage', 'lens', 'label', 'label-text', 'readout', 'toggle', 'live'].map($);
  const spots = [...root.querySelectorAll('.xray__spot')].map((el) => ({
    x: parseFloat(el.style.getPropertyValue('--xray-sx')),
    y: parseFloat(el.style.getPropertyValue('--xray-sy')),
    label: el.dataset.label,
  }));
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const token = (name) => getComputedStyle(root).getPropertyValue(name).trim();
  const home = spots[0];
  const pos = { x: home.x, y: home.y };
  const target = { ...pos };
  let current = text.textContent;
  let frame = 0;
  let last = 0;
  let drift = null;
  let touched = false;
  let dragging = false;
  root.classList.add('xray--js');
  toggle.hidden = false;
  const steering = () => toggle.getAttribute('aria-pressed') === 'true';

  // Name what's under the lens: the nearest hotspot (aspect-corrected), else plain wall
  const nameAt = ({ x, y }) => spots.reduce((best, s) => {
    const d = Math.hypot(s.x - x, (s.y - y) * 0.75);
    return d < best.d ? { d, label: s.label } : best;
  }, { d: 14, label: 'Insulated wall cavity' }).label;

  const paint = () => {
    stage.style.setProperty('--xray-x', pos.x.toFixed(2));
    stage.style.setProperty('--xray-y', pos.y.toFixed(2));
    readout.textContent = `X ${pos.x.toFixed(1)} · Y ${pos.y.toFixed(1)}`;
    const name = nameAt(pos);
    if (name === current) return;
    current = name;
    text.textContent = name;
    if (steering()) live.textContent = name;
    if (!reduce.matches) pill.animate([{ opacity: 0.2, filter: 'blur(3px)' }, { opacity: 1, filter: 'blur(0px)' }], { duration: parseFloat(token('--dur-3')), easing: token('--ease-out') });
  };

  // One rAF loop: walk the drift path, then ease the lens towards its target (instant under reduced motion)
  const tick = (now) => {
    frame = 0;
    const dt = last ? Math.min(64, now - last) : 16.7;
    last = now;
    if (drift) {
      const t = Math.min(1, (now - drift.start) / drift.duration);
      const p = ease(t) * (drift.path.length - 1);
      const i = Math.min(drift.path.length - 2, Math.floor(p));
      const [a, b] = [drift.path[i], drift.path[i + 1]];
      target.x = a.x + (b.x - a.x) * (p - i);
      target.y = a.y + (b.y - a.y) * (p - i);
      if (t === 1) drift = null;
    }
    const k = reduce.matches ? 1 : 1 - 0.82 ** (dt / 16.7);
    pos.x += (target.x - pos.x) * k;
    pos.y += (target.y - pos.y) * k;
    paint();
    if (drift || Math.abs(target.x - pos.x) + Math.abs(target.y - pos.y) > 0.02) frame = requestAnimationFrame(tick);
    else last = 0;
  };
  const run = () => { if (!frame) frame = requestAnimationFrame(tick); };
  const aim = (point) => { touched = true; drift = null; Object.assign(target, point); run(); };
  const toPoint = (e) => {
    const r = stage.getBoundingClientRect();
    return { x: clamp(((e.clientX - r.left) / r.width) * 100), y: clamp(((e.clientY - r.top) / r.height) * 100) };
  };

  // Mouse: the lens follows. Touch/pen: drag the lens, or tap where it should go
  stage.addEventListener('pointermove', (e) => { if (e.pointerType === 'mouse' || dragging) aim(toPoint(e)); }, { passive: true });
  stage.addEventListener('click', (e) => aim(toPoint(e)));
  lens.addEventListener('pointerdown', (e) => {
    if (e.pointerType === 'mouse') return;
    dragging = true;
    lens.setPointerCapture(e.pointerId);
  });
  ['pointerup', 'pointercancel'].forEach((type) => lens.addEventListener(type, () => { dragging = false; }));

  // Keyboard: the toggle turns arrow-key steering on; Esc or leaving the button turns it off
  const steer = (on) => {
    toggle.setAttribute('aria-pressed', String(on));
    root.classList.toggle('is-steering', on);
    if (on) live.textContent = `Lens over ${current}.`;
  };
  toggle.addEventListener('click', () => steer(!steering()));
  toggle.addEventListener('blur', () => steer(false));
  toggle.addEventListener('keydown', (e) => {
    if (!steering()) return;
    if (e.key === 'Escape') return steer(false);
    const step = e.shiftKey ? 12 : 4;
    const move = { ArrowLeft: [-step, 0], ArrowRight: [step, 0], ArrowUp: [0, -step], ArrowDown: [0, step] }[e.key];
    if (!move) return;
    e.preventDefault();
    aim({ x: clamp(target.x + move[0]), y: clamp(target.y + move[1]) });
  });

  // First time in view: a short look around (about 4s with the settle) that comes back to rest
  const io = new IntersectionObserver(([entry]) => {
    if (!entry.isIntersecting) return;
    io.disconnect();
    if (reduce.matches) return;
    setTimeout(() => {
      if (touched) return;
      drift = { start: performance.now(), duration: 3600, path: [home, ...spots.slice(1, 4), home] };
      run();
    }, 1000);
  }, { threshold: 0.5 });
  io.observe(stage);
  paint();
});
```

## Notes

- The section owns the page's `<h1>`, and the photo has real alt text. The schematic, lens, label and HUD are `aria-hidden`; the figure's caption gives the key in text. "Move lens" is a real toggle (`aria-pressed`) with a visible hint. While it's on, arrow keys move the lens (Shift for bigger steps) and Esc or tabbing away turns it off. A polite status line names each system the lens settles on.
- With scripting available, CSS already rests the lens on the copper supply hotspot, so nothing flashes before JS runs; JS then adds the follow, drag and drift. With scripting off (`@media (scripting: none)`) the stage becomes a static half-and-half of photo and blueprint, labelled "Photo" and "X-ray".
- Reduced motion: no entrance, no look-around drift and no follow lag. The lens rests on the hotspot and jumps straight to the pointer, tap or arrow key. The drift runs once, for about 4s including the settle, so there is no pause control and nothing loops.
- Contrast: body copy is `--text-inverse-muted` on `--surface-deep` (7:1). The "others miss." gradient stays at 9:1 or more. HUD chips and the lens label put `--text-inverse` on 72–78% `--surface-deep` glass, which is above 7:1 even over a white wall in the photo.
- To adapt, swap the photo and redraw the schematic in the 1200×900 viewBox, which matches the 4:3 stage. Hotspots are `.xray__spot` elements with percentage positions and a `data-label`, and the first one is where the lens rests. Uses container units, `@property`, CSS masks and `@media (scripting)`. Browsers without `@property` flip the label instantly.
