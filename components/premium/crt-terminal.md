# CRT Terminal

A dispatch desk on a cream 1980s monitor. The chunky bezel and keycaps are mixed from tokens, and the curved glass has scanlines, a vignette and a phosphor glow. When the monitor scrolls into view, the tube powers on: a hot horizontal line stretches across the dark glass, the picture expands out of it, and BRAND-OS boots line by line before leaving a working prompt (`help`, `services`, `quote`, `hours`, `call`, `clear`). A sliding switch on the bezel flips between green and amber phosphor with a degauss wobble. On phones the tube becomes nearly square and the six keycaps form a 3 × 2 pad that's easy to tap. Depends on `tokens/variables.css`.

**Motion:** power-on beam and vertical expand (`--dur-5`, `--ease-out`) · settle flicker (6 × 140 ms, finite) · typed boot and output (JS timers) · block cursor that blinks 5 times and then holds · degauss wobble on the phosphor switch · thumb slide and keycap press (`--ease-spring`).
**Fonts:** VT323: https://fonts.googleapis.com/css2?family=VT323&display=swap

## HTML

```html
<section class="crt-term" aria-labelledby="crt-term-title" data-crt-term>
  <div class="crt-term__inner">
    <header class="crt-term__copy">
      <p class="crt-term__eyebrow">Dispatch terminal</p>
      <h2 id="crt-term-title" class="crt-term__title">Book a pro, the old-school way.</h2>
      <p class="crt-term__lead">Type a command or tap a key. Our dispatch desk runs on BRAND-OS: same-day slots, flat-rate prices and seven technicians on call across Springfield.</p>
      <p class="crt-term__human">
        <span class="crt-term__dot" aria-hidden="true"></span>
        Rather talk to a human? <a href="tel:+15555550123">(555) 555-0123</a>
      </p>
    </header>

    <div class="crt-term__rig">
      <div class="crt-term__monitor">
        <div class="crt-term__frame">
          <div class="crt-term__screen">
            <div class="crt-term__display">
              <div class="crt-term__log" role="log" aria-label="Terminal output">
                <p class="crt-term__line">BRAND-OS v2.4 · READY</p>
                <p class="crt-term__line">WELCOME TO BRAND DISPATCH.</p>
                <p class="crt-term__line">&nbsp;</p>
                <p class="crt-term__line">SERVICES ........ FROM</p>
                <p class="crt-term__line"> PLUMBING ........ $89</p>
                <p class="crt-term__line"> ELECTRICAL ...... $99</p>
                <p class="crt-term__line"> HEATING/AC ..... $129</p>
                <p class="crt-term__line"> ROOFING ........ $149</p>
                <p class="crt-term__line"> HANDYMAN ........ $69</p>
                <p class="crt-term__line">&nbsp;</p>
                <p class="crt-term__line">CALL <a class="crt-term__link" href="tel:+15555550123">(555) 555-0123</a></p>
              </div>
              <p class="crt-term__typing" aria-hidden="true"></p>
              <form class="crt-term__prompt" hidden>
                <span class="crt-term__ps" aria-hidden="true">&gt;</span>
                <label class="crt-term__field">
                  <span class="crt-term__sr">Command</span>
                  <input class="crt-term__input" type="text" maxlength="24" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="send">
                  <span class="crt-term__cursor" aria-hidden="true"></span>
                </label>
              </form>
            </div>
            <span class="crt-term__glass" aria-hidden="true"></span>
          </div>
        </div>

        <div class="crt-term__chin">
          <span class="crt-term__badge" aria-hidden="true">BRAND <small>Model 2400</small></span>
          <span class="crt-term__vents" aria-hidden="true"></span>
          <fieldset class="crt-term__mode">
            <legend class="crt-term__legend">Phosphor</legend>
            <span class="crt-term__track">
              <label><input type="radio" name="crt-term-phosphor" value="green" checked>Green</label>
              <label><input type="radio" name="crt-term-phosphor" value="amber">Amber</label>
            </span>
          </fieldset>
          <span class="crt-term__led" aria-hidden="true"></span>
        </div>
      </div>
      <span class="crt-term__stand" aria-hidden="true"></span>

      <div class="crt-term__keys" role="group" aria-label="Quick commands" hidden>
        <button class="crt-term__key" type="button" data-crt-term-cmd="help">Help</button>
        <button class="crt-term__key" type="button" data-crt-term-cmd="services">Services</button>
        <button class="crt-term__key" type="button" data-crt-term-cmd="quote">Quote</button>
        <button class="crt-term__key" type="button" data-crt-term-cmd="hours">Hours</button>
        <button class="crt-term__key" type="button" data-crt-term-cmd="call">Call</button>
        <button class="crt-term__key" type="button" data-crt-term-cmd="clear">Clear</button>
      </div>
    </div>
  </div>
</section>
```

## CSS

```css
/* Local palette: phosphors and tube glass are themed values; the plastic is mixed from tokens */
.crt-term {
  --crt-term-green: #39ff7a;
  --crt-term-green-dim: #22b257;
  --crt-term-amber: #ffb33c;
  --crt-term-amber-dim: #c98a22;
  --crt-term-tube-green: #031009;
  --crt-term-tube-amber: #120a02;
  --crt-term-black: #000201;
  --crt-term-font: "VT323", var(--font-mono);
  --crt-term-plastic: color-mix(in oklab, var(--surface-muted) 84%, var(--accent));
  --crt-term-plastic-hi: color-mix(in oklab, var(--crt-term-plastic) 45%, var(--surface-light));
  --crt-term-plastic-lo: color-mix(in oklab, var(--crt-term-plastic) 74%, var(--text-muted));
  --crt-term-recess: color-mix(in oklab, var(--surface-dark) 86%, var(--crt-term-plastic));
  --crt-term-phos: var(--crt-term-green);
  --crt-term-phos-dim: var(--crt-term-green-dim);
  --crt-term-tube: var(--crt-term-tube-green);
  position: relative; overflow: clip;
  background:
    radial-gradient(48rem 32rem at 78% 45%, color-mix(in srgb, var(--accent) 12%, transparent), transparent 70%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
/* The bezel switch re-points the phosphor, with or without JS */
.crt-term:has(.crt-term__track [value="amber"]:checked) {
  --crt-term-phos: var(--crt-term-amber);
  --crt-term-phos-dim: var(--crt-term-amber-dim);
  --crt-term-tube: var(--crt-term-tube-amber);
}

/* Layout */
.crt-term__inner {
  display: grid; gap: 3rem; align-items: center;
  max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4rem, 9vw, 7rem) var(--gutter);
}
@media (min-width: 1024px) {
  .crt-term__inner { grid-template-columns: minmax(0, 0.75fr) minmax(0, 1.25fr); gap: 4.5rem; }
}

/* Copy */
.crt-term__eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0;
  color: var(--primary); font: 600 0.8125rem/1.2 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.crt-term__eyebrow::after { content: ""; width: 0.5em; height: 1em; background: currentColor; }
.crt-term__title {
  margin: 0.875rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.crt-term__lead { max-width: 32rem; margin: 1.25rem 0 0; color: var(--text-muted); font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem); line-height: 1.6; }
.crt-term__human { display: flex; flex-wrap: wrap; align-items: center; gap: 0.25rem 0.5rem; margin: 1.75rem 0 0; color: var(--text-muted); font-size: 0.9375rem; }
.crt-term__human a { color: var(--text-main); font: 600 0.9375rem var(--font-mono); text-decoration-color: color-mix(in srgb, var(--primary) 45%, transparent); text-underline-offset: 0.25em; }
.crt-term__human a:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; border-radius: var(--radius-sm); }
.crt-term__dot { width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 20%, transparent); }

/* The monitor: putty bezel, dark recess, curved tube */
.crt-term__rig { display: flex; flex-direction: column; align-items: center; width: 100%; max-width: 46rem; margin-inline: auto; }
.crt-term__monitor {
  position: relative; z-index: 1; width: 100%;
  padding: 0.875rem 0.875rem 0.75rem; border-radius: var(--radius-2xl);
  background: linear-gradient(172deg, var(--crt-term-plastic-hi), var(--crt-term-plastic) 38%, color-mix(in oklab, var(--crt-term-plastic) 60%, var(--crt-term-plastic-lo)));
  box-shadow:
    var(--highlight), inset 0 -4px 0 color-mix(in oklab, var(--crt-term-plastic-lo) 70%, transparent),
    inset 0 0 0 1px color-mix(in srgb, var(--text-main) 8%, transparent),
    var(--shadow-xl), 0 48px 64px -36px color-mix(in srgb, var(--text-main) 45%, transparent);
}
@media (min-width: 768px) {
  .crt-term__monitor { padding: 1.5rem 1.5rem 1rem; border-radius: calc(var(--radius-2xl) * 1.35); }
}
.crt-term__frame {
  padding: clamp(0.5rem, 1.6vw, 0.875rem); border-radius: var(--radius-xl);
  background: linear-gradient(180deg, color-mix(in oklab, var(--crt-term-recess) 70%, var(--crt-term-black)), var(--crt-term-recess) 55%, color-mix(in oklab, var(--crt-term-recess) 75%, var(--crt-term-plastic-lo)));
  box-shadow: inset 0 3px 8px color-mix(in srgb, var(--crt-term-black) 60%, transparent), 0 1px 0 var(--crt-term-plastic-hi), 0 -1px 0 color-mix(in oklab, var(--crt-term-plastic-lo) 80%, var(--text-muted));
}
/* overflow: clip (not hidden) keeps aspect-ratio a minimum, so the no-JS page can grow */
.crt-term__screen {
  position: relative; isolation: isolate; overflow: clip; aspect-ratio: 1 / 1.05;
  border-radius: calc(var(--radius-2xl) + 0.25rem) / var(--radius-2xl);
  background: radial-gradient(ellipse 85% 75% at 50% 48%, color-mix(in srgb, var(--crt-term-phos) 10%, var(--crt-term-tube)), var(--crt-term-tube) 62%, var(--crt-term-black));
  color: var(--crt-term-phos);
  font: 400 clamp(1.125rem, 0.95rem + 0.55vw, 1.375rem)/1.15 var(--crt-term-font);
  text-shadow:
    0 0 1px var(--crt-term-phos),
    0 0 0.3em color-mix(in srgb, var(--crt-term-phos) 55%, transparent),
    0 0 0.9em color-mix(in srgb, var(--crt-term-phos) 25%, transparent);
  box-shadow: 0 0 0 1px color-mix(in srgb, var(--crt-term-black) 70%, transparent), 0 0 2.5rem -0.75rem color-mix(in srgb, var(--crt-term-phos) 45%, transparent);
}
@media (min-width: 768px) { .crt-term__screen { aspect-ratio: 4 / 3; } }

/* Glass: reflection, vignette over the picture, scanlines */
.crt-term__glass {
  position: absolute; inset: 0; z-index: 2; border-radius: inherit; pointer-events: none;
  background:
    radial-gradient(ellipse 60% 38% at 28% 10%, color-mix(in srgb, var(--surface-light) 10%, transparent), transparent 70%),
    radial-gradient(ellipse 120% 100% at 50% 50%, transparent 56%, color-mix(in srgb, var(--crt-term-black) 72%, transparent)),
    repeating-linear-gradient(to bottom, transparent 0 2px, color-mix(in srgb, var(--crt-term-black) 30%, transparent) 2px 3px);
  box-shadow: inset 0 0 3rem color-mix(in srgb, var(--crt-term-black) 80%, transparent), inset 0 0 0.5rem var(--crt-term-black);
}

/* Picture. Without JS it's a static page that grows to fit; with JS it's a fixed raster anchored to the bottom */
.crt-term__display { position: relative; z-index: 1; padding: 1.125rem 1.25rem; }
@media (min-width: 768px) { .crt-term__display { padding: 1.75rem 2.25rem; } }
.crt-term--js .crt-term__display { position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: flex-end; overflow: hidden; }
.crt-term__display::after {
  content: ""; position: absolute; inset: 0; z-index: 2; opacity: 0; pointer-events: none;
  background: radial-gradient(ellipse 60% 50% at 50% 50%, color-mix(in srgb, var(--crt-term-phos) 35%, var(--surface-light)), var(--crt-term-phos));
}
.crt-term__line, .crt-term__typing { margin: 0; min-height: 1.15em; white-space: pre-wrap; overflow-wrap: anywhere; }
.crt-term__typing:empty { display: none; }
.crt-term__link { color: inherit; text-decoration-thickness: 1px; text-underline-offset: 0.18em; }
.crt-term__link:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Prompt with a block cursor placed by caret column (VT323 is monospaced) */
.crt-term__prompt { display: flex; gap: 1ch; margin-top: 0.15em; border-radius: var(--radius-sm); }
.crt-term__prompt[hidden] { display: none; }
.crt-term__ps { color: var(--crt-term-phos-dim); }
.crt-term__field { position: relative; display: block; flex: 1; min-width: 0; }
.crt-term__input {
  display: block; width: 100%; padding: 0; border: 0; background: none;
  color: inherit; font: inherit; letter-spacing: 0; text-shadow: inherit; text-transform: uppercase; caret-color: transparent;
}
.crt-term__input:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
@supports selector(:has(*)) {
  .crt-term__input:focus-visible { outline: none; }
  .crt-term__prompt:has(:focus-visible) { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
}
.crt-term__cursor {
  position: absolute; top: 0.12em; left: min(calc(var(--crt-term-col, 0) * 1ch), calc(100% - 1ch));
  width: 1ch; height: 0.92em; pointer-events: none;
  background: var(--crt-term-phos); box-shadow: 0 0 0.45em color-mix(in srgb, var(--crt-term-phos) 70%, transparent);
  mix-blend-mode: difference;
  animation: crt-term-blink 1s steps(1, end) 5;
}
.crt-term__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Off until it scrolls into view. A failsafe shows the static page if the script never arrives */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .crt-term:not(.is-on) .crt-term__display { visibility: hidden; animation: crt-term-failsafe 0s 3s forwards; }
  .crt-term--js:not(.is-on) .crt-term__display { animation: none; }
  .crt-term--js:not(.is-on) .crt-term__screen {
    background: radial-gradient(ellipse 85% 75% at 50% 42%, color-mix(in oklab, var(--surface-dark) 70%, var(--text-muted)), var(--surface-dark) 72%, var(--crt-term-black));
    box-shadow: 0 0 0 1px color-mix(in srgb, var(--crt-term-black) 70%, transparent);
  }
  .crt-term--js:not(.is-on) .crt-term__led { background: color-mix(in oklab, var(--crt-term-green) 18%, var(--surface-dark)); box-shadow: none; }
}
/* Power-on: a hot line stretches across, then the picture opens out of it */
.crt-term.is-on .crt-term__display {
  transform-origin: 50% 50%;
  animation: crt-term-power calc(var(--dur-5) + 300ms) var(--ease-out) both, crt-term-flicker 140ms steps(1, end) calc(var(--dur-5) + 300ms) 6;
}
.crt-term.is-on .crt-term__display::after { animation: crt-term-beam calc(var(--dur-5) + 300ms) var(--ease-out) both; }

/* Chin: badge, vents, phosphor switch, power LED */
.crt-term__chin { display: flex; align-items: flex-end; gap: 0.5rem; margin-top: 0.75rem; padding-inline: 0.25rem; }
@media (min-width: 768px) { .crt-term__chin { gap: 0.875rem; } }
.crt-term__badge {
  flex: none; align-self: center; color: color-mix(in oklab, var(--crt-term-plastic-lo) 35%, var(--text-main));
  font: 700 0.8125rem/1 var(--font-display); letter-spacing: 0.24em; text-shadow: 0 1px 0 var(--crt-term-plastic-hi);
}
.crt-term__badge small { display: none; margin-left: 0.5em; color: var(--text-muted); font: 500 0.625rem var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }
@media (min-width: 768px) { .crt-term__badge small { display: inline; } }
.crt-term__vents {
  flex: 1 1 auto; align-self: center; min-width: 0; height: 0.75rem; border-radius: 2px;
  background: repeating-linear-gradient(90deg, color-mix(in srgb, var(--text-main) 24%, transparent) 0 2px, transparent 2px 7px);
  box-shadow: 0 1px 0 var(--crt-term-plastic-hi);
}
.crt-term__mode { display: grid; gap: 0.3125rem; min-width: 0; margin: 0; padding: 0; border: 0; }
.crt-term__legend { padding: 0; color: color-mix(in oklab, var(--text-main) 80%, var(--crt-term-plastic)); font: 600 0.625rem/1 var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase; }
.crt-term__track {
  position: relative; display: grid; grid-template-columns: 1fr 1fr; padding: 3px; border-radius: var(--radius-full);
  background: var(--crt-term-recess);
  box-shadow: inset 0 1px 3px color-mix(in srgb, var(--crt-term-black) 70%, transparent), 0 1px 0 var(--crt-term-plastic-hi);
}
.crt-term__track::before {
  content: ""; position: absolute; top: 3px; bottom: 3px; left: 3px; width: calc(50% - 3px); border-radius: var(--radius-full);
  background: repeating-linear-gradient(90deg, var(--crt-term-plastic-hi) 0 2px, var(--crt-term-plastic) 2px 4px);
  box-shadow: var(--highlight), 0 1px 3px color-mix(in srgb, var(--crt-term-black) 45%, transparent);
  transition: translate var(--dur-3) var(--ease-spring);
}
.crt-term__track:has([value="amber"]:checked)::before { translate: 100% 0; }
.crt-term__track:has(:focus-visible) { outline: 2px solid var(--primary); outline-offset: 3px; }
.crt-term__track label {
  position: relative; z-index: 1; display: flex; align-items: center; justify-content: center; gap: 0.375rem;
  min-height: 1.75rem; padding: 0 0.5rem; cursor: pointer;
  color: var(--text-inverse-muted); font: 600 0.625rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase;
  transition: color var(--dur-2);
}
@media (min-width: 768px) { .crt-term__track label { padding: 0 0.75rem; } }
.crt-term__track label:has(:checked) { color: var(--text-main); }
.crt-term__track label::before { content: ""; width: 0.375rem; height: 0.375rem; border-radius: 50%; background: var(--crt-term-green); opacity: 0.45; transition: opacity var(--dur-2); }
.crt-term__track label:last-child::before { background: var(--crt-term-amber); }
.crt-term__track label:has(:checked)::before { opacity: 1; box-shadow: 0 0 6px var(--crt-term-phos); }
.crt-term__track input { position: absolute; inset: 0; margin: 0; opacity: 0; cursor: pointer; }
.crt-term__led {
  flex: none; align-self: center; width: 0.5rem; height: 0.5rem; border-radius: 50%;
  background: var(--crt-term-green); box-shadow: 0 0 0.5rem var(--crt-term-green), inset 0 -1px 1px color-mix(in srgb, var(--crt-term-black) 35%, transparent);
  transition: background-color var(--dur-3), box-shadow var(--dur-3);
}
.crt-term__stand {
  width: 34%; height: 1.25rem;
  background: linear-gradient(180deg, color-mix(in oklab, var(--crt-term-plastic-lo) 75%, var(--text-main)), var(--crt-term-plastic-lo) 40%, var(--crt-term-plastic));
  clip-path: polygon(14% 0, 86% 0, 100% 100%, 0 100%);
}

/* Keycaps: a tappable command pad */
.crt-term__keys {
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.5rem; width: min(100%, 40rem);
  padding: 0.625rem; border-radius: var(--radius-xl);
  background: linear-gradient(180deg, var(--crt-term-plastic-lo), color-mix(in oklab, var(--crt-term-plastic) 50%, var(--crt-term-plastic-lo)));
  box-shadow: inset 0 1px 0 var(--crt-term-plastic-hi), inset 0 0 0 1px color-mix(in srgb, var(--text-main) 8%, transparent), var(--shadow-lg);
}
.crt-term__keys[hidden] { display: none; }
@media (min-width: 768px) { .crt-term__keys { grid-template-columns: repeat(6, minmax(0, 1fr)); } }
.crt-term__key {
  min-height: 2.75rem; padding: 0 0.375rem; border: 0; border-radius: var(--radius-md); cursor: pointer;
  background: linear-gradient(180deg, var(--crt-term-plastic-hi), var(--crt-term-plastic));
  color: var(--text-main); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
  box-shadow:
    inset 0 -2px 0 color-mix(in oklab, var(--crt-term-plastic-lo) 60%, transparent),
    0 3px 0 color-mix(in oklab, var(--crt-term-plastic-lo) 70%, var(--text-muted)),
    0 6px 10px -4px color-mix(in srgb, var(--text-main) 40%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2) var(--ease-out);
}
.crt-term__key:hover { transform: translateY(-1px); }
.crt-term__key:active {
  transform: translateY(3px); transition-duration: var(--dur-1);
  box-shadow: inset 0 -1px 0 color-mix(in oklab, var(--crt-term-plastic-lo) 60%, transparent), 0 0 0 transparent, 0 2px 3px -1px color-mix(in srgb, var(--text-main) 35%, transparent);
}
.crt-term__key:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) {
  .crt-term *, .crt-term *::before, .crt-term *::after { animation: none !important; }
}

@keyframes crt-term-power {
  0% { transform: scale(0.04, 0.006); filter: brightness(5); }
  35% { transform: scale(1, 0.006); filter: brightness(5); }
  70% { transform: scale(1, 1.03); filter: brightness(1.8); }
  100% { transform: none; filter: none; }
}
@keyframes crt-term-beam { 0%, 40% { opacity: 1; } 100% { opacity: 0; } }
@keyframes crt-term-flicker { 50% { opacity: 0.82; } }
@keyframes crt-term-blink { 50% { opacity: 0; } }
@keyframes crt-term-failsafe { to { visibility: visible; } }
```

## JS

```js
const LINKS = { '(555) 555-0123': 'tel:+15555550123', 'hello@example.com': 'mailto:hello@example.com' };
const BOOT = ['BRAND-OS v2.4', '(C) 1986 BRAND HOME SVC', '640K MEMORY ....... OK', 'TOOLBOX ........... OK', 'DISPATCH: SPRINGFIELD', 'TECHNICIANS ONLINE: 7', '', 'READY. TYPE HELP.'];
const CMDS = {
  help: ['COMMANDS:', ' SERVICES  WHAT WE FIX', ' QUOTE     FREE ESTIMATE', ' HOURS     OPENING TIMES', ' CALL      PHONE A HUMAN', ' CLEAR     WIPE SCREEN'],
  services: ['SERVICES ........ FROM', ' PLUMBING ........ $89', ' ELECTRICAL ...... $99', ' HEATING/AC ..... $129', ' ROOFING ........ $149', ' HANDYMAN ........ $69', 'ALL WORK: 1-YR WARRANTY'],
  quote: ['FREE QUOTE IN 3 STEPS:', ' 1. DESCRIBE THE JOB', ' 2. SNAP A PHOTO OR TWO', ' 3. GET A FLAT PRICE', 'EMAIL hello@example.com'],
  hours: ['MON-FRI   07:00-19:00', 'SAT       08:00-16:00', 'SUN       EMERGENCIES', '24/7 LINE (555) 555-0123'],
  call: ['DIALING DISPATCH...', 'CALL (555) 555-0123', 'AVG ANSWER: 9 SEC.', 'HUMANS STANDING BY.'],
};
const ALIAS = { '?': 'help', ls: 'help', cls: 'clear' };
const wait = (ms) => new Promise((done) => setTimeout(done, ms));

document.querySelectorAll('[data-crt-term]').forEach((term, n) => {
  const $ = (selector) => term.querySelector(selector);
  const [screen, log, typing, form, field, input, cursor, keys] = ['__screen', '__log', '__typing', '__prompt', '__field', '__input', '__cursor', '__keys'].map((part) => $(`.crt-term${part}`));
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const queue = [];
  const past = [];
  let busy = false;
  let on = false;
  let epoch = 0;
  let back = 0;

  term.classList.add('crt-term--js');
  keys.hidden = false;
  // One radio group per terminal, so two monitors never share a switch
  term.querySelectorAll('.crt-term__track input').forEach((radio) => { radio.name = `crt-term-phosphor-${n}`; });

  // Finished lines go into the role="log" region; the phone number and email become real links
  const print = (text) => {
    const line = document.createElement('p');
    const key = Object.keys(LINKS).find((k) => text.includes(k));
    line.className = 'crt-term__line';
    if (key) {
      const [before, after] = text.split(key);
      line.append(before, Object.assign(document.createElement('a'), { className: 'crt-term__link', href: LINKS[key], textContent: key }), after);
    } else line.textContent = text || '\u00a0';
    log.append(line);
    while (log.childElementCount > 60) log.firstElementChild.remove();
  };

  // Five blinks after any activity, then a steady cursor (WCAG 2.2.2)
  const wake = () => { cursor.style.animation = 'none'; void cursor.offsetWidth; cursor.style.animation = ''; };

  // Type each queued line into the aria-hidden span, then hand the whole line to the log
  const pump = async () => {
    if (busy) return;
    busy = true;
    while (queue.length) {
      const [text, speed] = queue.shift();
      const mine = epoch;
      for (let i = 1; speed && !reduce.matches && mine === epoch && i <= text.length; i += 1) {
        typing.textContent = text.slice(0, i);
        await wait(speed);
      }
      typing.textContent = '';
      if (mine === epoch) print(text);
      if (speed > 10 && !reduce.matches) await wait(140);
    }
    busy = false;
    form.hidden = false;
    wake();
  };
  const say = (lines, speed = 6) => { queue.push(...lines.map((text) => [text, speed])); pump(); };

  // Power on once: clear the static page, play the tube animation, then boot
  const powerOn = () => {
    if (on) return;
    on = true;
    log.replaceChildren();
    term.classList.add('is-on');
    queue.push(...BOOT.map((text) => [text, 16]));
    if (reduce.matches) { pump(); return; }
    busy = true;
    setTimeout(() => { busy = false; pump(); }, 1000);
  };

  const run = (raw) => {
    const typed = raw.trim().slice(0, 24);
    const cmd = ALIAS[typed.toLowerCase()] || typed.toLowerCase();
    powerOn();
    if (cmd === 'clear') { epoch += 1; queue.length = 0; log.replaceChildren(); typing.textContent = ''; return; }
    queue.push([`> ${typed.toUpperCase()}`, 0]);
    if (!typed) { pump(); return; }
    const shown = typed.length > 8 ? `${typed.slice(0, 8)}…` : typed;
    say(CMDS[cmd] || [`"${shown.toUpperCase()}"? NOT A COMMAND.`, 'TRY HELP, OR TAP A KEY.']);
  };

  // Caret column drives the block cursor; Up/Down recall earlier commands
  const sync = () => { field.style.setProperty('--crt-term-col', input.selectionStart ?? input.value.length); wake(); };
  ['input', 'keyup', 'click', 'focus'].forEach((type) => input.addEventListener(type, sync));
  input.addEventListener('keydown', (event) => {
    if (event.key !== 'ArrowUp' && event.key !== 'ArrowDown') return;
    event.preventDefault();
    back = Math.min(past.length, Math.max(0, back + (event.key === 'ArrowUp' ? -1 : 1)));
    input.value = past[back] || '';
  });
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (input.value.trim()) past.push(input.value.trim());
    back = past.length;
    run(input.value);
    input.value = '';
    sync();
  });
  keys.addEventListener('click', (event) => {
    const key = event.target.closest('[data-crt-term-cmd]');
    if (key) run(key.dataset.crtTermCmd);
  });
  // Clicking the glass focuses the prompt (but never steals a link click or a text selection)
  screen.addEventListener('click', (event) => {
    if (!form.hidden && !event.target.closest('a') && !String(getSelection())) input.focus({ preventScroll: true });
  });

  // Flipping the phosphor switch degausses the tube
  const degauss = [{ transform: 'none', filter: 'none' }, { transform: 'scale(1.02) skewX(1.5deg)', filter: 'hue-rotate(60deg) saturate(1.8)' }, { transform: 'scale(0.99) skewX(-1deg)', filter: 'hue-rotate(-40deg)' }, { transform: 'none', filter: 'none' }];
  $('.crt-term__track').addEventListener('change', () => {
    if (!reduce.matches) screen.animate(degauss, { duration: 650, easing: 'cubic-bezier(0.16, 1, 0.3, 1)' });
  });

  new IntersectionObserver(([entry], observer) => {
    if (!entry.isIntersecting) return;
    observer.disconnect();
    powerOn();
  }, { threshold: 0.45 }).observe(screen);
});
```

## Notes

- Output is an APG log (`role="log"`, polite). The typing animation only ever touches an `aria-hidden` span, so assistive tech hears each line once, when it's complete. The prompt is a labelled text input ("Command"). The keycaps are a labelled group of real buttons, and the phosphor switch is a native radio group (legend "Phosphor"), so arrow keys work on it.
- Without JS, the tube shows a static welcome screen with the services list and a phone link, and the green/amber switch still works because it's pure CSS (`:has()`). If scripting is on but the module never loads, a 3s CSS failsafe turns the screen on.
- Under reduced motion there's no power-on, flicker, typing, cursor blink or degauss: the boot text appears instantly when the monitor comes into view. In full motion, everything that moves stops within 5s, so no pause control is needed.
- Contrast: green phosphor is 14.6:1 on the tube (11.9:1 at the lit centre) and amber is 11:1 (9.4:1). The dim prompt glyph is at least 5.7:1. Switch labels are 5.1:1 on the recess and 12.6:1 on the thumb, and the `--primary` focus ring is 4.45:1 against the bezel.
- Retheme by changing the phosphor and tube variables, or add a third switch position, such as white phosphor (`--crt-term-phos`). Add a command by adding a key to `CMDS`; phone and email text is turned into links automatically. Lines stay at 24 characters or fewer so columns hold at 320px.
