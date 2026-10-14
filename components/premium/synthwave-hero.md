# Synthwave Hero

An outrun hero for summer AC deals. A starfield fades into a magenta horizon. On load a huge striped sun rises into place behind wireframe mountains, a hot-pink perspective grid scrolls toward you, and the headline lands: "COOL HOMES." in 80s chrome, then "Hot deals." flickering on in neon script. The mouse drifts the stars, sun and two mountain ranges at different depths. On phones the same scene stacks under the copy: the sun scales to the space left above the horizon, the grid takes the lower third, and the CTAs wrap into a centred pair. Depends on `tokens/variables.css`.

**Motion:** sun rise (2 × `--dur-5`, `--ease-out`) · mountains lift and horizon draw (`--dur-5`, staggered) · chrome headline slam and glint · neon ignition flicker (`steps()`, finite) · copy rise (`--stagger`) · grid scroll (0.7s linear loop) and star twinkle (2.8s loop), both with a pause button and an off-screen freeze · pointer parallax eased with `--dur-5`.
**Fonts:** Mr Dafoe (neon script): https://fonts.googleapis.com/css2?family=Mr+Dafoe&display=swap

## HTML

```html
<section class="synthwave" aria-labelledby="synthwave-title" data-synthwave>
  <span class="synthwave__stars" aria-hidden="true"></span>

  <div class="synthwave__inner">
    <p class="synthwave__eyebrow" style="--synthwave-i: 0"><span>Est. 1986</span> Brand heating &amp; cooling</p>
    <h1 id="synthwave-title" class="synthwave__title">
      <span class="synthwave__chrome">Cool homes.</span>
      <span class="synthwave__neon">Hot deals.</span>
    </h1>
    <p class="synthwave__lead" style="--synthwave-i: 3">Summer AC tune-up, $79 flat. Licensed techs and same-day slots across Springfield, Westlake and Riverside.</p>
    <div class="synthwave__actions" style="--synthwave-i: 4">
      <a class="synthwave__cta" href="#book">
        Book a tune-up
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </a>
      <a class="synthwave__call" href="tel:+15555550123">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
        (555) 555-0123
      </a>
    </div>
  </div>

  <div class="synthwave__scene" aria-hidden="true">
    <div class="synthwave__sunset">
      <span class="synthwave__halo"></span>
      <span class="synthwave__sun"></span>
      <svg class="synthwave__range synthwave__range--far" viewBox="0 0 1440 300" preserveAspectRatio="none" focusable="false">
        <path class="synthwave__ridge" d="M0 300V214L84 176L168 206L262 142L344 192L436 152L522 198L604 166L684 204L760 178L842 208L934 154L1016 196L1104 144L1190 190L1272 162L1356 202L1440 174V300Z" />
        <path class="synthwave__wire" d="M84 176L40 300M84 176L130 300M262 142L210 300M262 142L310 300M436 152L390 300M436 152L480 300M604 166L560 300M604 166L650 300M760 178L720 300M760 178L800 300M934 154L890 300M934 154L980 300M1104 144L1060 300M1104 144L1150 300M1272 162L1230 300M1272 162L1320 300M0 258H1440" />
      </svg>
      <svg class="synthwave__range synthwave__range--near" viewBox="0 0 1440 300" preserveAspectRatio="none" focusable="false">
        <path class="synthwave__ridge" d="M0 300V118L72 78L150 126L232 58L330 148L408 196L478 252L516 300ZM1440 300V118L1368 78L1290 126L1208 58L1110 148L1032 196L962 252L924 300Z" />
        <path class="synthwave__wire" d="M72 78L30 300M72 78L118 300M232 58L182 300M232 58L280 300M150 126L206 300M330 148L372 300M408 196L440 300M1368 78L1410 300M1368 78L1322 300M1208 58L1258 300M1208 58L1160 300M1290 126L1234 300M1110 148L1068 300M1032 196L1000 300" />
      </svg>
    </div>
    <div class="synthwave__floor">
      <div class="synthwave__view">
        <div class="synthwave__plane"><span class="synthwave__grid"></span></div>
      </div>
    </div>
    <span class="synthwave__horizon"></span>
  </div>

  <button class="synthwave__pause" type="button" aria-pressed="false" hidden>
    <span class="synthwave__sr">Pause background animation</span>
    <svg class="synthwave__icon-pause" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
    <svg class="synthwave__icon-play" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
  </button>
</section>
```

## CSS

```css
/* Local neon palette. Chrome stops are tuned so even the dark "horizon" band clears 5:1 on the sky */
.synthwave {
  --synthwave-night: #0d0221;
  --synthwave-purple: #2b0b4f;
  --synthwave-magenta: #ff2a6d;
  --synthwave-pink: #ff7ad9;
  --synthwave-cyan: #2de2f0;
  --synthwave-sun: #ffd319;
  --synthwave-orange: #ff901f;
  --synthwave-haze: #f4ecff;
  --synthwave-haze-dim: #cbb8ec;
  --synthwave-chrome-1: #f7fbff;
  --synthwave-chrome-2: #7cc8ff;
  --synthwave-chrome-3: #9f7ee6;
  --synthwave-chrome-4: #ff9fd8;
  --synthwave-chrome-5: #ffe3a3;
  --synthwave-script: "Mr Dafoe", var(--font-display);
  --synthwave-h: 48%;
  position: relative; isolation: isolate; overflow: clip;
  display: flex; flex-direction: column; min-height: 100vh; min-height: 100svh;
  background: linear-gradient(180deg, var(--synthwave-night) 0%, var(--synthwave-purple) 52%, color-mix(in srgb, var(--synthwave-magenta) 40%, var(--synthwave-purple)) 100%);
  color: var(--synthwave-haze); font-family: var(--font-sans);
}

/* Stars: three co-prime dot tilings read as random; a fourth layer twinkles */
.synthwave__stars {
  position: absolute; inset: 0 0 30%; z-index: -1; pointer-events: none;
  background:
    radial-gradient(circle, var(--synthwave-haze) 0 1px, transparent 1.5px) 0 0 / 97px 89px,
    radial-gradient(circle, color-mix(in srgb, var(--synthwave-haze) 65%, transparent) 0 0.75px, transparent 1.25px) 31px 43px / 61px 53px,
    radial-gradient(circle, color-mix(in srgb, var(--synthwave-cyan) 75%, transparent) 0 1px, transparent 1.5px) 13px 7px / 151px 127px;
  -webkit-mask: linear-gradient(180deg, black 35%, transparent);
  mask: linear-gradient(180deg, black 35%, transparent);
  translate: calc(var(--synthwave-px, 0) * -6px) calc(var(--synthwave-py, 0) * -4px);
  transition: translate var(--dur-5) var(--ease-out);
}
.synthwave__stars::after {
  content: ""; position: absolute; inset: 0;
  background: radial-gradient(circle, var(--synthwave-haze) 0 1.25px, transparent 2px) 47px 23px / 173px 149px;
  animation: synthwave-twinkle 2.8s var(--ease-in-out) infinite alternate;
}

/* Copy */
.synthwave__inner {
  position: relative; z-index: 2; width: 100%; max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4.5rem, 11vh, 8rem) var(--gutter) 1.5rem; text-align: center;
}
.synthwave__eyebrow, .synthwave__lead, .synthwave__actions {
  animation: synthwave-rise-in var(--dur-5) var(--ease-out) calc(var(--synthwave-i, 0) * var(--stagger) * 3 + 200ms) both;
}
.synthwave__eyebrow {
  display: inline-flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 0.5rem 0.75rem; margin: 0;
  color: var(--synthwave-cyan); font: 600 0.75rem/1.3 var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase;
  text-shadow: 0 0 12px color-mix(in srgb, var(--synthwave-cyan) 55%, transparent);
}
.synthwave__eyebrow span { padding: 0.1875rem 0.625rem; border: 1px solid color-mix(in srgb, var(--synthwave-cyan) 55%, transparent); border-radius: var(--radius-full); box-shadow: inset 0 0 8px color-mix(in srgb, var(--synthwave-cyan) 25%, transparent); }
.synthwave__title { margin: 1.25rem 0 0; font-family: var(--font-display); font-weight: 400; line-height: 1; }

/* Chrome: sky above a hard horizon, warm metal below, a light edge and an extruded drop */
.synthwave__chrome {
  position: relative; display: inline-block; padding: 0.04em 0.1em 0.08em;
  font-size: clamp(2.125rem, 0.9rem + 6.4vw, 6.5rem); font-weight: 800; letter-spacing: var(--tracking-tight); text-transform: uppercase;
  background: linear-gradient(180deg, var(--synthwave-chrome-1) 4%, var(--synthwave-chrome-2) 44%, var(--synthwave-chrome-3) 49%, var(--synthwave-chrome-1) 50.5%, var(--synthwave-chrome-3) 53%, var(--synthwave-chrome-4) 74%, var(--synthwave-chrome-5) 96%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  -webkit-text-stroke: 1px color-mix(in srgb, var(--synthwave-chrome-1) 55%, transparent);
  filter: drop-shadow(0 0.045em 0 color-mix(in srgb, var(--synthwave-magenta) 35%, var(--synthwave-night))) drop-shadow(0 0 0.35em color-mix(in srgb, var(--synthwave-magenta) 40%, transparent));
  transform: skewX(-9deg);
  animation: synthwave-slam var(--dur-5) var(--ease-out) 150ms both;
}
.synthwave__chrome::after { /* lens glint on the last letter */
  content: ""; position: absolute; top: -0.06em; right: 0.12em; width: 0.42em; aspect-ratio: 1;
  background: var(--synthwave-chrome-1);
  clip-path: polygon(50% 0, 56% 44%, 100% 50%, 56% 56%, 50% 100%, 44% 56%, 0 50%, 44% 44%);
  transform: scale(0.6) rotate(45deg);
  animation: synthwave-glint var(--dur-5) var(--ease-out) 1.1s both;
}
.synthwave__neon {
  display: block; width: fit-content; margin: -0.38em auto 0; padding-inline: 0.2em;
  color: var(--synthwave-pink); font: 400 clamp(2.75rem, 1.2rem + 7vw, 7rem)/1.05 var(--synthwave-script); letter-spacing: 0.01em;
  text-shadow: 0 0 2px var(--synthwave-haze), 0 0 10px var(--synthwave-pink), 0 0 26px var(--synthwave-magenta), 0 0 52px color-mix(in srgb, var(--synthwave-magenta) 60%, transparent);
  transform: rotate(-7deg) translateX(6%);
  animation: synthwave-ignite 1.3s steps(1, end) 850ms both;
}
.synthwave__lead { max-width: 34rem; margin: 1.75rem auto 0; color: var(--synthwave-haze-dim); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.1875rem); line-height: 1.6; }

/* Neon-tube CTA and a quiet phone link */
.synthwave__actions { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 0.75rem 1.25rem; margin-top: 2rem; }
.synthwave__cta {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; padding: 0 1.5rem;
  border: 2px solid var(--synthwave-cyan); border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--synthwave-cyan) 8%, transparent); color: var(--synthwave-cyan);
  font: 700 0.875rem/1 var(--font-sans); letter-spacing: 0.08em; text-decoration: none; text-transform: uppercase;
  text-shadow: 0 0 10px color-mix(in srgb, var(--synthwave-cyan) 70%, transparent);
  box-shadow: 0 0 14px color-mix(in srgb, var(--synthwave-cyan) 45%, transparent), inset 0 0 14px color-mix(in srgb, var(--synthwave-cyan) 30%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out), background-color var(--dur-3) var(--ease-out), color var(--dur-2);
}
.synthwave__cta svg, .synthwave__call svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.synthwave__cta svg { transition: transform var(--dur-3) var(--ease-spring); }
.synthwave__cta:hover {
  background: color-mix(in srgb, var(--synthwave-cyan) 18%, transparent); color: var(--synthwave-haze);
  box-shadow: 0 0 22px color-mix(in srgb, var(--synthwave-cyan) 70%, transparent), inset 0 0 18px color-mix(in srgb, var(--synthwave-cyan) 45%, transparent);
}
.synthwave__cta:hover svg { transform: translateX(3px); }
.synthwave__cta:active { transform: scale(0.96); }
.synthwave__call {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 3rem; padding: 0 0.5rem;
  color: var(--synthwave-haze); font: 600 0.9375rem var(--font-mono); text-decoration: none; transition: color var(--dur-2), text-shadow var(--dur-2);
}
.synthwave__call:hover { color: var(--synthwave-pink); text-shadow: 0 0 12px color-mix(in srgb, var(--synthwave-magenta) 70%, transparent); }
.synthwave :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Scene: horizon sits at --synthwave-h; everything above it is clipped by the sunset box */
.synthwave__scene { position: relative; flex: 1; min-height: clamp(15rem, 44vh, 28rem); }
.synthwave__sunset { position: absolute; inset: 0 0 calc(100% - var(--synthwave-h)); overflow: hidden; container-type: size; }
.synthwave__halo {
  position: absolute; left: 50%; bottom: 0; width: min(48rem, 140cqw); aspect-ratio: 2 / 1; translate: -50% 0;
  background: radial-gradient(ellipse 50% 100% at 50% 100%, color-mix(in srgb, var(--synthwave-magenta) 55%, transparent), color-mix(in srgb, var(--synthwave-orange) 16%, transparent) 45%, transparent 70%);
}
.synthwave__sun {
  --synthwave-sun-size: min(26rem, 72cqw, 140cqh);
  position: absolute; left: 50%; bottom: calc(var(--synthwave-sun-size) * -0.3);
  width: var(--synthwave-sun-size); aspect-ratio: 1; margin-left: calc(var(--synthwave-sun-size) / -2); border-radius: 50%;
  background: linear-gradient(180deg, var(--synthwave-sun) 8%, var(--synthwave-orange) 42%, var(--synthwave-magenta) 72%);
  -webkit-mask: linear-gradient(180deg, black 0 47%, transparent 0 49%, black 0 54%, transparent 0 57%, black 0 61%, transparent 0 65%, black 0 68%, transparent 0 73%, black 0 75.5%, transparent 0 81%, black 0 83%, transparent 0);
  mask: linear-gradient(180deg, black 0 47%, transparent 0 49%, black 0 54%, transparent 0 57%, black 0 61%, transparent 0 65%, black 0 68%, transparent 0 73%, black 0 75.5%, transparent 0 81%, black 0 83%, transparent 0);
  translate: calc(var(--synthwave-px, 0) * -10px) calc(var(--synthwave-py, 0) * -5px);
  transition: translate var(--dur-5) var(--ease-out);
  animation: synthwave-sunrise calc(var(--dur-5) * 2) var(--ease-out) both;
}
.synthwave__range { position: absolute; bottom: 0; left: -6%; width: 112%; overflow: visible; transition: translate var(--dur-5) var(--ease-out); }
.synthwave__range--far { height: clamp(3.5rem, 10vw, 7rem); translate: calc(var(--synthwave-px, 0) * -18px) 0; animation: synthwave-lift var(--dur-5) var(--ease-out) 350ms both; }
.synthwave__range--near {
  height: clamp(5rem, 14vw, 10rem); translate: calc(var(--synthwave-px, 0) * -34px) calc(var(--synthwave-py, 0) * -4px);
  filter: drop-shadow(0 0 0.5rem color-mix(in srgb, var(--synthwave-cyan) 40%, transparent));
  animation: synthwave-lift var(--dur-5) var(--ease-out) 500ms both;
}
.synthwave__ridge { fill: color-mix(in srgb, var(--synthwave-night) 82%, var(--synthwave-purple)); stroke-width: 1.5; stroke-linejoin: round; vector-effect: non-scaling-stroke; }
.synthwave__wire { fill: none; stroke-width: 1; opacity: 0.45; vector-effect: non-scaling-stroke; }
.synthwave__range--far .synthwave__ridge { stroke: color-mix(in srgb, var(--synthwave-magenta) 75%, transparent); }
.synthwave__range--far .synthwave__wire { stroke: var(--synthwave-magenta); }
.synthwave__range--near .synthwave__ridge { stroke: var(--synthwave-cyan); stroke-width: 2; }
.synthwave__range--near .synthwave__wire { stroke: var(--synthwave-cyan); }
.synthwave__horizon {
  position: absolute; left: 0; right: 0; top: var(--synthwave-h); height: 2px; margin-top: -1px;
  background: linear-gradient(90deg, transparent, var(--synthwave-pink) 15% 85%, transparent);
  box-shadow: 0 0 10px 1px var(--synthwave-magenta), 0 0 36px 6px color-mix(in srgb, var(--synthwave-magenta) 45%, transparent);
  animation: synthwave-draw var(--dur-5) var(--ease-out) 250ms both;
}

/* Floor: a rotateX plane under a perspective sized in floor heights (cqh), so it looks the same at any size */
.synthwave__floor {
  position: absolute; inset: var(--synthwave-h) 0 0; overflow: hidden; container-type: size;
  background: linear-gradient(180deg, color-mix(in srgb, var(--synthwave-magenta) 28%, var(--synthwave-night)), var(--synthwave-night) 55%);
}
.synthwave__view {
  position: absolute; inset: 0; perspective: 160cqh; perspective-origin: 50% 0;
  -webkit-mask: linear-gradient(180deg, transparent, black 32%);
  mask: linear-gradient(180deg, transparent, black 32%);
  animation: synthwave-fade var(--dur-5) var(--ease-out) 450ms both;
}
.synthwave__plane { position: absolute; top: 0; left: -10%; right: -10%; height: 130cqh; transform-origin: 50% 0; transform: rotateX(72deg); }
.synthwave__grid {
  --synthwave-cell: 12cqh;
  position: absolute; inset: calc(var(--synthwave-cell) * -1) 0 0;
  background:
    linear-gradient(90deg, transparent calc(50% - 2px), color-mix(in srgb, var(--synthwave-pink) 40%, transparent) calc(50% - 1px), var(--synthwave-pink) 50%, color-mix(in srgb, var(--synthwave-pink) 40%, transparent) calc(50% + 1px), transparent calc(50% + 2px)),
    linear-gradient(180deg, transparent calc(50% - 2px), color-mix(in srgb, var(--synthwave-magenta) 45%, transparent) calc(50% - 1px), var(--synthwave-magenta) 50%, color-mix(in srgb, var(--synthwave-magenta) 45%, transparent) calc(50% + 1px), transparent calc(50% + 2px));
  background-position: 50% 0;
  background-size: var(--synthwave-cell) var(--synthwave-cell);
  animation: synthwave-run 0.7s linear infinite;
}

/* Pause control */
.synthwave__pause {
  position: absolute; right: var(--gutter); bottom: 1rem; z-index: 3; display: grid; place-items: center;
  width: 2.25rem; height: 2.25rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: color-mix(in srgb, var(--synthwave-night) 55%, transparent); color: var(--synthwave-haze-dim);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--synthwave-cyan) 35%, transparent);
  transition: color var(--dur-2), box-shadow var(--dur-2);
}
.synthwave__pause:hover { color: var(--synthwave-haze); box-shadow: inset 0 0 0 1px var(--synthwave-cyan), 0 0 12px color-mix(in srgb, var(--synthwave-cyan) 45%, transparent); }
.synthwave__pause[hidden] { display: none; }
.synthwave__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.synthwave__icon-play, .synthwave__pause[aria-pressed="true"] .synthwave__icon-pause { display: none; }
.synthwave__pause[aria-pressed="true"] .synthwave__icon-play { display: block; }
.synthwave__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Paused or off-screen: freeze every loop */
.synthwave[data-paused] *, .synthwave[data-paused] *::before, .synthwave[data-paused] *::after,
.synthwave[data-offscreen] *, .synthwave[data-offscreen] *::before, .synthwave[data-offscreen] *::after { animation-play-state: paused !important; }

@media (min-width: 768px) {
  .synthwave { --synthwave-h: 46%; }
  .synthwave__neon { transform: rotate(-7deg) translateX(16%); }
  .synthwave__actions { gap: 1rem 1.5rem; }
}
@media (prefers-reduced-motion: reduce) {
  .synthwave *, .synthwave *::before, .synthwave *::after { animation: none !important; }
}

@keyframes synthwave-run { to { transform: translateY(var(--synthwave-cell)); } }
@keyframes synthwave-twinkle { from { opacity: 0.15; } to { opacity: 1; } }
@keyframes synthwave-sunrise { from { transform: translateY(55%); } }
@keyframes synthwave-lift { from { opacity: 0; transform: translateY(35%); } }
@keyframes synthwave-draw { from { opacity: 0; transform: scaleX(0); } }
@keyframes synthwave-fade { from { opacity: 0; } }
@keyframes synthwave-rise-in { from { opacity: 0; transform: translateY(0.75rem); filter: blur(6px); } }
@keyframes synthwave-slam { from { opacity: 0; transform: skewX(-9deg) translateY(-0.35em) scale(1.12); filter: blur(10px); } }
@keyframes synthwave-glint { from { transform: scale(0) rotate(-90deg); } 60% { transform: scale(1.15) rotate(30deg); } }
@keyframes synthwave-ignite {
  0%, 12%, 20%, 46%, 54% { opacity: 0.08; }
  10%, 16%, 40%, 50%, 100% { opacity: 1; }
}
```

## JS

```js
document.querySelectorAll('[data-synthwave]').forEach((hero) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const pause = hero.querySelector('.synthwave__pause');
  let frame = 0;
  let point = null;

  // Pause control for the grid and stars (WCAG 2.2.2); hidden when motion is already off
  pause.hidden = reduce.matches;
  reduce.addEventListener('change', () => { pause.hidden = reduce.matches; });
  pause.addEventListener('click', () => {
    pause.setAttribute('aria-pressed', String(hero.toggleAttribute('data-paused')));
  });

  // Freeze the loops while the hero is off screen
  new IntersectionObserver(([entry]) => hero.toggleAttribute('data-offscreen', !entry.isIntersecting)).observe(hero);

  // Mouse parallax: stars, sun and two mountain ranges drift by depth, one update per frame
  hero.addEventListener('pointermove', (event) => {
    if (event.pointerType !== 'mouse' || reduce.matches) return;
    point = event;
    frame ||= requestAnimationFrame(() => {
      frame = 0;
      const r = hero.getBoundingClientRect();
      hero.style.setProperty('--synthwave-px', (((point.clientX - r.left) / r.width) * 2 - 1).toFixed(3));
      hero.style.setProperty('--synthwave-py', (((point.clientY - r.top) / r.height) * 2 - 1).toFixed(3));
    });
  }, { passive: true });
  hero.addEventListener('pointerleave', () => {
    hero.style.setProperty('--synthwave-px', '0');
    hero.style.setProperty('--synthwave-py', '0');
  });
});
```

## Notes

- This is the page hero, so it owns the `<h1>`. The headline reads "Cool homes. Hot deals." as one heading, and the whole scene (stars, sun, mountains, grid, horizon) is `aria-hidden`. The pause button follows the shared recipe (`aria-pressed`, "Pause background animation"): it freezes the grid scroll and star twinkle, which also freeze automatically off screen. Everything else is a finite entrance.
- Contrast: chrome stops are 5.2:1 or better against the purple sky (the lavender horizon band is the lowest), with a light text-stroke defining every glyph. The neon script is 7.2:1, the lead 9.2:1, the eyebrow and CTA text 10.5:1, and the phone link 14.5:1. The copy sits above the horizon, so it never overlaps the sun.
- Under reduced motion, the scene renders its final frame: sun up, grid still, no flicker, glint, twinkle or parallax, and no pause button (nothing moves). Without JS, the CSS entrance and the grid still play; JS only adds the pause button, the off-screen freeze and the parallax.
- The floor's `perspective` and grid cell are in container units (`cqh`), so the vanishing point holds at any hero height. The sun sizes itself to the space above the horizon (`min(26rem, 72cqw, 140cqh)`). Container queries, container units and `mask` are evergreen. If Mr Dafoe doesn't load, the script line falls back to the display font.
- Retune with `--synthwave-h` (horizon height), the sun's stripe stops in its mask, and the palette variables. A teal-and-orange "miami" variant takes about five variable swaps.
