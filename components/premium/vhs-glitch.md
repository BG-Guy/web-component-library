# VHS Title Card

A title card that looks like a rental tape playing on a CRT. A VCR on-screen display frames the shot: "PLAY ▶" top left, "CH 03" top right, and an SP tape counter ticking in the corner, all in VT323. The headline carries red/cyan chromatic aberration that jitters now and then. Tracking bands roll down the picture, warping whatever passes beneath them, over grain, scanlines, head-switching noise and a barrel vignette. Hovering or focusing the CTA kicks the tape: the headline tears into offset slices and the OSD flashes TRACKING. A two-key VCR transport (PLAY / STOP) is the pause control. On phones the OSD shrinks and the transport and counter share the bottom row. Depends on `tokens/variables.css`.

**Motion:** tracking bands roll (7.5s and 4.9s linear loops) · film grain shimmer and head-switching jitter (`steps()` loops) · aberration jitter and title wobble (occasional, `steps()`) · CTA glitch burst (0.5s clip-path slices, `steps()`) · VCR key press (`--ease-spring`). Loops run only once JS wires the STOP key, and freeze off screen.
**Fonts:** VT323 (OSD): https://fonts.googleapis.com/css2?family=VT323&display=swap

## HTML

```html
<section class="vhs-title" aria-labelledby="vhs-title-heading" data-vhs-title>
  <div class="vhs-title__fx" aria-hidden="true">
    <span class="vhs-title__grain"></span>
    <span class="vhs-title__lines"></span>
    <span class="vhs-title__band"></span>
    <span class="vhs-title__band vhs-title__band--thin"></span>
    <span class="vhs-title__switch"></span>
    <span class="vhs-title__vignette"></span>
  </div>

  <div class="vhs-title__inner">
    <div class="vhs-title__osd vhs-title__osd--top" aria-hidden="true">
      <span class="vhs-title__mode">
        <span class="vhs-title__mode-play">PLAY <span class="vhs-title__tri"></span></span>
        <span class="vhs-title__mode-stop">STOP <span class="vhs-title__sq"></span></span>
      </span>
      <span>CH 03</span>
    </div>

    <div class="vhs-title__content">
      <p class="vhs-title__presents">Brand Home Video presents</p>
      <h2 id="vhs-title-heading" class="vhs-title__title" data-text="The leak stops here.">The leak stops here.</h2>
      <p class="vhs-title__lead">A same-day repair in three acts. Filmed on location in Springfield and rated 4.9 by 1,200 neighbours. No rewinding required.</p>
      <div class="vhs-title__actions">
        <a class="vhs-title__cta" href="#book"><span class="vhs-title__rec" aria-hidden="true"></span>Book a visit</a>
        <a class="vhs-title__call" href="tel:+15555550123">or call (555) 555-0123</a>
      </div>
    </div>

    <span class="vhs-title__osd vhs-title__tracking" aria-hidden="true">TRACKING <span class="vhs-title__meter"></span></span>

    <div class="vhs-title__bottom">
      <div class="vhs-title__deck" role="group" aria-label="Tape effects" hidden>
        <button class="vhs-title__key" type="button" aria-pressed="true" data-vhs-title-key="play"><span class="vhs-title__tri" aria-hidden="true"></span>Play</button>
        <button class="vhs-title__key vhs-title__key--stop" type="button" aria-pressed="false" data-vhs-title-key="stop"><span class="vhs-title__sq" aria-hidden="true"></span>Stop</button>
      </div>
      <span class="vhs-title__osd vhs-title__counter" aria-hidden="true">SP <span class="vhs-title__time">00:03:14</span></span>
    </div>
  </div>
</section>
```

## CSS

```css
/* Local tape palette */
.vhs-title {
  --vhs-title-tape: #07080b;
  --vhs-title-deep: #141822;
  --vhs-title-paper: #f3f0e8;
  --vhs-title-dim: #b9b8b0;
  --vhs-title-osd: #d4ffe0;
  --vhs-title-red: #ff2b4a;
  --vhs-title-cyan: #1fe4ff;
  --vhs-title-font: "VT323", var(--font-mono);
  --vhs-title-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='vhs-title-noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23vhs-title-noise)'/%3E%3C/svg%3E");
  position: relative; isolation: isolate; overflow: clip;
  background: radial-gradient(ellipse 80% 70% at 50% 45%, var(--vhs-title-deep), var(--vhs-title-tape) 72%);
  color: var(--vhs-title-paper); font-family: var(--font-sans);
}

/* Layout: OSD row, centred title, transport + counter row */
.vhs-title__inner {
  display: grid; grid-template-rows: auto 1fr auto; gap: 1.5rem; min-height: 36rem;
  max-width: var(--container-max); margin-inline: auto; padding: 1.25rem var(--gutter);
}
@media (min-width: 768px) { .vhs-title__inner { min-height: 42rem; padding-block: 1.75rem; } }
.vhs-title__content { position: relative; z-index: 1; align-self: center; max-width: 54rem; margin-inline: auto; text-align: center; }
.vhs-title__presents { margin: 0; color: var(--vhs-title-dim); font: 600 0.75rem/1.4 var(--font-mono); letter-spacing: 0.32em; text-transform: uppercase; }
.vhs-title__lead { max-width: 32rem; margin: 1.5rem auto 0; color: var(--vhs-title-dim); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }

/* Headline with chromatic aberration: two colour copies sit behind the text, a hair apart */
.vhs-title__title {
  position: relative; isolation: isolate; margin: 1rem 0 0;
  font: 800 clamp(2.5rem, 1rem + 7vw, 6.5rem)/0.95 var(--font-display); letter-spacing: var(--tracking-tight); text-transform: uppercase; text-wrap: balance;
}
.vhs-title__title::before, .vhs-title__title::after {
  content: attr(data-text);
  content: attr(data-text) / "";
  position: absolute; inset: 0; z-index: -1; pointer-events: none;
}
.vhs-title__title::before { color: var(--vhs-title-red); transform: translateX(-0.045em); }
.vhs-title__title::after { color: var(--vhs-title-cyan); transform: translateX(0.045em); }

/* Picture effects over the content (the VCR's OSD and keys sit above them) */
.vhs-title__fx { position: absolute; inset: 0; z-index: 2; overflow: hidden; pointer-events: none; }
.vhs-title__fx > * { position: absolute; }
.vhs-title__lines { inset: 0; background: repeating-linear-gradient(180deg, transparent 0 2px, color-mix(in srgb, var(--vhs-title-tape) 38%, transparent) 2px 3px); }
.vhs-title__grain {
  inset: -20%; opacity: 0.55;
  background: color-mix(in srgb, var(--vhs-title-paper) 22%, transparent);
  -webkit-mask: var(--vhs-title-noise) 0 0 / 160px 160px;
  mask: var(--vhs-title-noise) 0 0 / 160px 160px;
}
.vhs-title__band {
  --vhs-title-travel: 840%;
  left: 0; right: 0; top: 0; height: 12%; transform: translateY(-110%);
  background:
    repeating-linear-gradient(180deg, transparent 0 3px, color-mix(in srgb, var(--vhs-title-paper) 8%, transparent) 3px 4px),
    linear-gradient(180deg, transparent, color-mix(in srgb, var(--vhs-title-paper) 14%, transparent) 45% 55%, transparent);
  -webkit-backdrop-filter: blur(0.6px) brightness(1.2) contrast(1.15);
  backdrop-filter: blur(0.6px) brightness(1.2) contrast(1.15);
  transition: opacity var(--dur-3) var(--ease-out);
}
.vhs-title__band--thin { --vhs-title-travel: 2000%; height: 5%; }
.vhs-title__switch {
  left: -2%; right: -2%; bottom: 0; height: max(2.5%, 0.75rem);
  background: color-mix(in srgb, var(--vhs-title-paper) 30%, transparent);
  -webkit-mask: var(--vhs-title-noise) 0 0 / 80px 12px;
  mask: var(--vhs-title-noise) 0 0 / 80px 12px;
}
.vhs-title__vignette {
  inset: 0;
  background: radial-gradient(ellipse 90% 80% at 50% 50%, transparent 55%, color-mix(in srgb, var(--vhs-title-tape) 82%, transparent));
  box-shadow: inset 0 0 5rem color-mix(in srgb, var(--vhs-title-tape) 85%, transparent);
}

/* VCR on-screen display */
.vhs-title__osd {
  position: relative; z-index: 3; color: var(--vhs-title-osd); pointer-events: none;
  font: 400 clamp(1.25rem, 1rem + 1vw, 1.875rem)/1 var(--vhs-title-font); letter-spacing: 0.04em;
  text-shadow: 0.06em 0.06em 0 var(--vhs-title-tape), 0 0 0.35em color-mix(in srgb, var(--vhs-title-osd) 35%, transparent);
}
.vhs-title__osd--top { display: flex; justify-content: space-between; gap: 1rem; }
.vhs-title__tri, .vhs-title__sq { display: inline-block; width: 0.5em; height: 0.56em; background: currentColor; vertical-align: 0.02em; }
.vhs-title__tri { clip-path: polygon(0 0, 100% 50%, 0 100%); }
.vhs-title__sq { width: 0.5em; height: 0.5em; }
.vhs-title__mode-stop, .vhs-title[data-paused] .vhs-title__mode-play { display: none; }
.vhs-title[data-paused] .vhs-title__mode-stop { display: inline; }
.vhs-title__tracking {
  position: absolute; left: 50%; bottom: 6.5rem; display: inline-flex; align-items: center; gap: 0.5em; translate: -50% 0; visibility: hidden;
  font-size: clamp(1.125rem, 1rem + 0.5vw, 1.375rem); white-space: nowrap;
}
.vhs-title__meter { width: 5em; height: 0.5em; background: repeating-linear-gradient(90deg, currentColor 0 0.35em, transparent 0.35em 0.5em); clip-path: inset(0 30% 0 0); }

/* Bottom row: transport keys and the SP counter */
.vhs-title__bottom { position: relative; z-index: 3; display: flex; flex-wrap: wrap; align-items: end; justify-content: space-between; gap: 1rem; }
.vhs-title__counter { margin-left: auto; font-variant-numeric: tabular-nums; }
.vhs-title__deck {
  display: flex; gap: 0.375rem; padding: 0.375rem; border-radius: var(--radius-md);
  background: linear-gradient(180deg, color-mix(in srgb, var(--vhs-title-paper) 8%, var(--vhs-title-tape)), var(--vhs-title-tape));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--vhs-title-paper) 14%, transparent), 0 10px 24px -10px var(--vhs-title-tape);
}
.vhs-title__deck[hidden] { display: none; }
.vhs-title__key {
  position: relative; display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1rem 0 0.875rem;
  border: 0; border-radius: var(--radius-sm); cursor: pointer;
  background: linear-gradient(180deg, color-mix(in srgb, var(--vhs-title-paper) 16%, var(--vhs-title-deep)), var(--vhs-title-deep));
  color: var(--vhs-title-paper); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--vhs-title-paper) 22%, transparent), 0 3px 0 var(--vhs-title-tape), 0 5px 8px -3px var(--vhs-title-tape);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2) var(--ease-out), color var(--dur-2);
}
.vhs-title__key::after { content: ""; width: 0.375rem; height: 0.375rem; margin-left: 0.25rem; border-radius: 50%; background: color-mix(in srgb, var(--vhs-title-paper) 18%, transparent); transition: background-color var(--dur-2), box-shadow var(--dur-2); }
.vhs-title__key[aria-pressed="true"] {
  transform: translateY(2px); color: var(--vhs-title-osd);
  box-shadow: inset 0 2px 4px var(--vhs-title-tape), 0 1px 0 color-mix(in srgb, var(--vhs-title-paper) 10%, transparent);
}
.vhs-title__key[aria-pressed="true"]::after { background: var(--vhs-title-osd); box-shadow: 0 0 6px var(--vhs-title-osd); }
.vhs-title__key--stop[aria-pressed="true"]::after { background: var(--vhs-title-red); box-shadow: 0 0 6px var(--vhs-title-red); }
.vhs-title__key:active { transform: translateY(3px); transition-duration: var(--dur-1); }

/* CTA: tape-label paper with a REC dot; hover or focus shows an RGB split */
.vhs-title__actions { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 0.75rem 1.25rem; margin-top: 2rem; }
.vhs-title__cta {
  display: inline-flex; align-items: center; gap: 0.625rem; height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-sm);
  background: var(--vhs-title-paper); color: var(--vhs-title-tape); font: 700 0.9375rem/1 var(--font-sans); text-decoration: none;
  box-shadow: 0 0 0 transparent, 0 0 0 transparent;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2) var(--ease-out);
}
.vhs-title__cta:hover, .vhs-title__cta:focus-visible { box-shadow: -3px 0 0 var(--vhs-title-red), 3px 0 0 var(--vhs-title-cyan); }
.vhs-title__cta:active { transform: scale(0.97); }
.vhs-title__rec { width: 0.625rem; height: 0.625rem; border-radius: 50%; background: var(--vhs-title-red); box-shadow: 0 0 0.5rem color-mix(in srgb, var(--vhs-title-red) 70%, transparent); }
.vhs-title__call { display: inline-flex; align-items: center; min-height: 3rem; padding: 0 0.25rem; color: var(--vhs-title-paper); font: 600 0.9375rem var(--font-mono); text-decoration-color: color-mix(in srgb, var(--vhs-title-paper) 40%, transparent); text-underline-offset: 0.3em; }
.vhs-title :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Loops start only once JS has wired the STOP key */
.vhs-title--js .vhs-title__band { animation: vhs-title-roll 7.5s linear infinite; }
.vhs-title--js .vhs-title__band--thin { animation-duration: 4.9s; animation-delay: -2.6s; }
.vhs-title--js .vhs-title__grain { animation: vhs-title-grain 0.5s steps(1, end) infinite; }
.vhs-title--js .vhs-title__switch { animation: vhs-title-switch 0.24s steps(1, end) infinite; }
.vhs-title--js .vhs-title__title { animation: vhs-title-wobble 6.1s steps(1, end) infinite; }
.vhs-title--js .vhs-title__title::before { animation: vhs-title-jitter 3.7s steps(1, end) infinite; }
.vhs-title--js .vhs-title__title::after { animation: vhs-title-jitter 4.3s steps(1, end) -1.4s infinite; }

/* Hover or focus the CTA: one burst of torn slices and a TRACKING flash (only while the tape plays) */
.vhs-title--js:not([data-paused], [data-offscreen]):has(.vhs-title__cta:is(:hover, :focus-visible)) .vhs-title__title { animation: vhs-title-shake 0.5s steps(1, end); }
.vhs-title--js:not([data-paused], [data-offscreen]):has(.vhs-title__cta:is(:hover, :focus-visible)) .vhs-title__title::before { animation: vhs-title-slice-a 0.5s steps(1, end); }
.vhs-title--js:not([data-paused], [data-offscreen]):has(.vhs-title__cta:is(:hover, :focus-visible)) .vhs-title__title::after { animation: vhs-title-slice-b 0.5s steps(1, end); }
.vhs-title--js:not([data-paused], [data-offscreen]):has(.vhs-title__cta:is(:hover, :focus-visible)) .vhs-title__tracking { visibility: visible; animation: vhs-title-flash 1.2s steps(1, end) both; }

/* STOP (or off screen): freeze everything; STOP also clears the tracking bands */
.vhs-title[data-paused] *, .vhs-title[data-paused] *::before, .vhs-title[data-paused] *::after,
.vhs-title[data-offscreen] *, .vhs-title[data-offscreen] *::before, .vhs-title[data-offscreen] *::after { animation-play-state: paused !important; }
.vhs-title[data-paused] .vhs-title__band { opacity: 0; }

@media (prefers-reduced-motion: reduce) {
  .vhs-title *, .vhs-title *::before, .vhs-title *::after { animation: none !important; }
}

@keyframes vhs-title-roll { from { transform: translateY(-110%); } to { transform: translateY(var(--vhs-title-travel)); } }
@keyframes vhs-title-grain {
  0%, 100% { transform: translate(0, 0); }
  20% { transform: translate(-6%, 4%); }
  40% { transform: translate(5%, -7%); }
  60% { transform: translate(-3%, 8%); }
  80% { transform: translate(7%, 2%); }
}
@keyframes vhs-title-switch { 0%, 100% { translate: 0 0; } 50% { translate: 1.5% 0; } }
@keyframes vhs-title-wobble {
  0%, 93%, 100% { transform: none; }
  94% { transform: skewX(-7deg) translateX(0.03em); }
  96% { transform: skewX(4deg) translateX(-0.02em); }
}
@keyframes vhs-title-jitter {
  0%, 88%, 100% { translate: 0 0; }
  89% { translate: -0.05em 0.02em; }
  91% { translate: 0.07em -0.01em; }
  93% { translate: -0.03em 0; }
}
@keyframes vhs-title-shake {
  0%, 100% { transform: none; }
  20% { transform: translateX(-0.04em) skewX(-6deg); }
  50% { transform: translateX(0.05em); }
  70% { transform: translateX(-0.02em) skewX(4deg); }
}
@keyframes vhs-title-slice-a {
  0% { z-index: 1; background-color: var(--vhs-title-tape); clip-path: inset(12% 0 68% 0); translate: -0.14em 0; }
  20% { z-index: 1; background-color: var(--vhs-title-tape); clip-path: inset(52% 0 30% 0); translate: 0.1em 0; }
  40% { z-index: 1; background-color: var(--vhs-title-tape); clip-path: inset(28% 0 56% 0); translate: -0.08em 0; }
  60% { z-index: 1; background-color: var(--vhs-title-tape); clip-path: inset(78% 0 6% 0); translate: 0.16em 0; }
  80%, 100% { z-index: 1; background-color: var(--vhs-title-tape); clip-path: inset(2% 0 88% 0); translate: -0.05em 0; }
}
@keyframes vhs-title-slice-b {
  0% { z-index: 1; background-color: var(--vhs-title-tape); clip-path: inset(64% 0 18% 0); translate: 0.12em 0; }
  25% { z-index: 1; background-color: var(--vhs-title-tape); clip-path: inset(8% 0 80% 0); translate: -0.1em 0; }
  50% { z-index: 1; background-color: var(--vhs-title-tape); clip-path: inset(40% 0 46% 0); translate: 0.18em 0; }
  75%, 100% { z-index: 1; background-color: var(--vhs-title-tape); clip-path: inset(86% 0 2% 0); translate: -0.07em 0; }
}
@keyframes vhs-title-flash { 0% { opacity: 1; } 85%, 100% { opacity: 0; } }
```

## JS

```js
document.querySelectorAll('[data-vhs-title]').forEach((card) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const title = card.querySelector('.vhs-title__title');
  const time = card.querySelector('.vhs-title__time');
  const deck = card.querySelector('.vhs-title__deck');
  const keys = [...deck.querySelectorAll('[data-vhs-title-key]')];
  let [h, m, s] = time.textContent.split(':').map(Number);
  let offscreen = false;

  // Keep the aberration copies in sync with the heading text
  title.dataset.text = title.textContent.trim();
  card.classList.add('vhs-title--js');
  deck.hidden = false;

  // PLAY and STOP are a pair of VCR keys: each is a toggle (aria-pressed) and exactly one is down.
  // STOP is the pause control: it freezes every loop and the counter.
  const stop = (stopped) => {
    card.toggleAttribute('data-paused', stopped);
    keys.forEach((key) => key.setAttribute('aria-pressed', String((key.dataset.vhsTitleKey === 'stop') === stopped)));
  };
  keys.forEach((key) => key.addEventListener('click', () => stop(key.dataset.vhsTitleKey === 'stop')));

  // Freeze while off screen, without touching the keys
  new IntersectionObserver(([entry]) => {
    offscreen = !entry.isIntersecting;
    card.toggleAttribute('data-offscreen', offscreen);
  }).observe(card);

  // The SP counter runs only while the tape plays (and never under reduced motion)
  setInterval(() => {
    if (reduce.matches || offscreen || card.hasAttribute('data-paused')) return;
    s += 1;
    if (s === 60) { s = 0; m += 1; }
    if (m === 60) { m = 0; h += 1; }
    time.textContent = [h, m, s].map((n) => String(n).padStart(2, '0')).join(':');
  }, 1000);
});
```

## Notes

- One `<h2>` (this is a section, not the page hero). The red/cyan copies are pseudo-elements with empty alternative text (`content: attr(data-text) / ""`), so the heading is read once. The whole picture layer and the OSD are `aria-hidden`; the counter and mode readout are decoration, not status.
- The pause control is a VCR transport: PLAY and STOP are two `aria-pressed` toggles in a labelled group, with exactly one pressed. Pressing STOP sets `data-paused`, which freezes every loop and the counter, clears the tracking bands and switches the OSD to "STOP ■". An IntersectionObserver also freezes the tape off screen. I used two keys rather than one button whose label flips between STOP and PLAY: APG asks for constant labels on `aria-pressed` buttons, and real VCRs had both keys anyway.
- Loops only start once JS has wired the transport, so without JS the card is static: aberration in place, no bands, the transport hidden, every link working. Under reduced motion only the static aberration remains: no rolling, grain, jitter, wobble or burst, and the counter doesn't tick.
- Contrast: headline paper is 17.6:1 on tape (9.9:1 even under a passing tracking band), the lead is 10:1 (5.7:1 under a band), the OSD is 18.3:1 and the CTA label 17.6:1. Red appears only in decoration (aberration, REC dot, STOP LED).
- The tracking bands use `backdrop-filter`, so they genuinely warp what passes beneath them. Without support you still get the moving light band. The burst needs `:has()` and is skipped while stopped, so it can never freeze mid-tear. Grain and head-switching noise are an `feTurbulence` data-URI mask, so they're coloured by a palette variable and carry no colour literals.
