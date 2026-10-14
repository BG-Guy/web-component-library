# 8-Bit Arcade UI

A playful two-level section in an NES palette. Above ground there's a HUD, a pixel-art house built from crisp SVG rects, a "PRESS START" blink, stepped-corner pixel buttons that press into their own shadow, and a Satisfaction HP bar that fills one segment at a time. Below the bricks, the underground holds an RPG battle box ("A wild LEAK appeared!") with typewriter text, a blinking advance arrow and a CALL BRAND / RUN menu, plus a high-score table of top-rated techs. Every button press banks a coin: the ? block bumps, a coin spins out and the HUD counter hops. On phones the two levels stack, the HUD shrinks to 8px pixel type and the high-score table drops to four tight columns. Depends on `tokens/variables.css`.

**Motion:** PRESS START blink (4 × 1s) · HP fill in 20 discrete steps (`steps()`, `--dur-5`) · LEAK drop-in · typewriter (JS) and advance-arrow blink (5 × 1s) · button press and release (`--dur-1` / `--ease-spring`) · ? block bump, coin pop and spin, counter hop (`steps()` for an 8-bit frame rate). Nothing loops.
**Fonts:** Press Start 2P: https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap

## HTML

```html
<section class="pixel-kit" aria-labelledby="pixel-kit-title" data-pixel-kit>
  <div class="pixel-kit__hud">
    <div class="pixel-kit__hud-inner">
      <p class="pixel-kit__stat" aria-hidden="true">Brand<span class="pixel-kit__score">004800</span></p>
      <p class="pixel-kit__stat pixel-kit__coins" aria-live="polite" aria-atomic="true">Coins<span><span class="pixel-kit__coin" aria-hidden="true"></span><span aria-hidden="true">×</span><span class="pixel-kit__count">07</span></span></p>
      <p class="pixel-kit__stat" aria-hidden="true">World<span>1-1</span></p>
      <p class="pixel-kit__stat" aria-hidden="true">Time<span>24/7</span></p>
    </div>
  </div>

  <div class="pixel-kit__world">
    <svg class="pixel-kit__cloud pixel-kit__cloud--a" viewBox="0 0 12 6" width="96" height="48" shape-rendering="crispEdges" aria-hidden="true" focusable="false">
      <g class="pixel-kit__fill-white"><rect x="4" y="0" width="4" height="1" /><rect x="2" y="1" width="8" height="1" /><rect x="1" y="2" width="10" height="1" /><rect x="0" y="3" width="12" height="1" /></g>
      <g class="pixel-kit__fill-mist"><rect x="0" y="4" width="12" height="1" /><rect x="1" y="5" width="10" height="1" /></g>
    </svg>
    <svg class="pixel-kit__cloud pixel-kit__cloud--b" viewBox="0 0 12 6" width="72" height="36" shape-rendering="crispEdges" aria-hidden="true" focusable="false">
      <g class="pixel-kit__fill-white"><rect x="4" y="0" width="4" height="1" /><rect x="2" y="1" width="8" height="1" /><rect x="1" y="2" width="10" height="1" /><rect x="0" y="3" width="12" height="1" /></g>
      <g class="pixel-kit__fill-mist"><rect x="0" y="4" width="12" height="1" /><rect x="1" y="5" width="10" height="1" /></g>
    </svg>

    <div class="pixel-kit__world-inner">
      <div class="pixel-kit__copy">
        <p class="pixel-kit__start" aria-hidden="true">Press start</p>
        <h2 id="pixel-kit-title" class="pixel-kit__title">Level up your home</h2>
        <p class="pixel-kit__lead">Licensed techs, flat-rate quotes and same-day slots across Springfield. Open 24/7, and no extra lives needed: every job is guaranteed.</p>
        <div class="pixel-kit__actions">
          <a class="pixel-kit__btn pixel-kit__btn--coin" href="#book"><span class="pixel-kit__face">Book a pro</span></a>
          <a class="pixel-kit__btn" href="tel:+15555550123"><span class="pixel-kit__face">Call (555) 555-0123</span></a>
        </div>
        <div class="pixel-kit__hp">
          <p class="pixel-kit__hp-label"><span class="pixel-kit__hp-tag" aria-hidden="true">HP</span>Satisfaction <span class="pixel-kit__hp-value">98/100</span></p>
          <span class="pixel-kit__hp-bar" aria-hidden="true"><span class="pixel-kit__hp-fill"></span></span>
        </div>
      </div>

      <div class="pixel-kit__stage">
        <button class="pixel-kit__block" type="button" aria-label="Hit the question block for a coin" data-pixel-kit-js hidden>
          <span class="pixel-kit__block-face" aria-hidden="true">?</span>
          <span class="pixel-kit__pop" aria-hidden="true"></span>
        </button>
        <svg class="pixel-kit__house" viewBox="0 0 32 28" width="320" height="280" shape-rendering="crispEdges" aria-hidden="true" focusable="false">
          <g class="pixel-kit__fill-white"><rect x="23" y="1" width="2" height="1" /><rect x="25" y="0" width="2" height="1" /></g>
          <g class="pixel-kit__fill-ink"><rect x="21" y="3" width="5" height="9" /></g>
          <g class="pixel-kit__fill-brick"><rect x="22" y="4" width="3" height="8" /></g>
          <g class="pixel-kit__fill-ink">
            <rect x="15" y="4" width="2" height="1" /><rect x="14" y="5" width="4" height="1" /><rect x="13" y="6" width="6" height="1" />
            <rect x="12" y="7" width="8" height="1" /><rect x="11" y="8" width="10" height="1" /><rect x="10" y="9" width="12" height="1" />
            <rect x="9" y="10" width="14" height="1" /><rect x="8" y="11" width="16" height="1" /><rect x="7" y="12" width="18" height="1" />
            <rect x="6" y="13" width="20" height="1" /><rect x="5" y="14" width="22" height="1" /><rect x="3" y="15" width="26" height="1" />
            <rect x="6" y="15" width="20" height="12" />
          </g>
          <g class="pixel-kit__fill-brick">
            <rect x="15" y="5" width="2" height="1" /><rect x="14" y="6" width="4" height="1" /><rect x="13" y="7" width="6" height="1" />
            <rect x="12" y="8" width="8" height="1" /><rect x="11" y="9" width="10" height="1" /><rect x="10" y="10" width="12" height="1" />
            <rect x="9" y="11" width="14" height="1" /><rect x="8" y="12" width="16" height="1" /><rect x="7" y="13" width="18" height="1" />
            <rect x="6" y="14" width="20" height="1" />
          </g>
          <g class="pixel-kit__fill-brick-lo"><rect x="12" y="8" width="8" height="1" /><rect x="9" y="11" width="14" height="1" /><rect x="6" y="14" width="20" height="1" /></g>
          <g class="pixel-kit__fill-ink"><rect x="14" y="9" width="4" height="3" /></g>
          <g class="pixel-kit__fill-coin"><rect x="15" y="10" width="2" height="1" /></g>
          <g class="pixel-kit__fill-cream"><rect x="7" y="16" width="18" height="10" /><rect x="14" y="27" width="4" height="1" /></g>
          <g class="pixel-kit__fill-ink"><rect x="8" y="17" width="5" height="5" /><rect x="19" y="17" width="5" height="5" /><rect x="13" y="19" width="6" height="8" /></g>
          <g class="pixel-kit__fill-water"><rect x="9" y="18" width="3" height="3" /><rect x="20" y="18" width="3" height="3" /></g>
          <g class="pixel-kit__fill-ink"><rect x="10" y="18" width="1" height="3" /><rect x="9" y="19" width="3" height="1" /><rect x="21" y="18" width="1" height="3" /><rect x="20" y="19" width="3" height="1" /></g>
          <g class="pixel-kit__fill-white"><rect x="9" y="18" width="1" height="1" /><rect x="20" y="18" width="1" height="1" /></g>
          <g class="pixel-kit__fill-brick-lo"><rect x="14" y="20" width="4" height="7" /></g>
          <g class="pixel-kit__fill-coin"><rect x="16" y="23" width="1" height="1" /></g>
          <g class="pixel-kit__fill-leaf"><rect x="8" y="22" width="5" height="1" /><rect x="19" y="22" width="5" height="1" /><rect x="2" y="24" width="1" height="1" /><rect x="29" y="24" width="1" height="1" /></g>
          <g class="pixel-kit__fill-grass">
            <rect x="1" y="24" width="1" height="1" /><rect x="3" y="24" width="1" height="1" /><rect x="0" y="25" width="5" height="2" />
            <rect x="28" y="24" width="1" height="1" /><rect x="30" y="24" width="1" height="1" /><rect x="27" y="25" width="5" height="2" />
            <rect x="0" y="27" width="14" height="1" /><rect x="18" y="27" width="14" height="1" />
          </g>
        </svg>
      </div>
    </div>
  </div>

  <div class="pixel-kit__ground" aria-hidden="true"></div>

  <div class="pixel-kit__under">
    <div class="pixel-kit__under-inner">
      <div class="pixel-kit__window pixel-kit__battle">
        <div class="pixel-kit__arena" aria-hidden="true">
          <svg class="pixel-kit__pipe" viewBox="0 0 20 18" width="80" height="72" shape-rendering="crispEdges" focusable="false">
            <g class="pixel-kit__fill-ink"><rect x="0" y="0" width="16" height="6" /><rect x="1" y="6" width="14" height="12" /></g>
            <g class="pixel-kit__fill-grass"><rect x="1" y="1" width="14" height="4" /><rect x="2" y="6" width="12" height="12" /></g>
            <g class="pixel-kit__fill-leaf"><rect x="2" y="1" width="2" height="4" /><rect x="5" y="1" width="1" height="4" /><rect x="3" y="6" width="2" height="12" /><rect x="6" y="6" width="1" height="12" /></g>
            <g class="pixel-kit__fill-pine"><rect x="12" y="1" width="2" height="4" /><rect x="11" y="6" width="2" height="12" /></g>
            <g class="pixel-kit__fill-ink"><rect x="12" y="9" width="2" height="1" /></g>
            <g class="pixel-kit__fill-water"><rect x="15" y="9" width="2" height="1" /><rect x="17" y="11" width="1" height="2" /><rect x="16" y="15" width="1" height="1" /></g>
          </svg>
          <svg class="pixel-kit__leak" viewBox="0 0 10 11" width="40" height="44" shape-rendering="crispEdges" focusable="false">
            <g class="pixel-kit__fill-ink"><rect x="4" y="0" width="2" height="1" /><rect x="3" y="1" width="4" height="1" /><rect x="2" y="2" width="6" height="2" /><rect x="1" y="4" width="8" height="1" /><rect x="0" y="5" width="10" height="4" /><rect x="1" y="9" width="8" height="1" /><rect x="2" y="10" width="6" height="1" /></g>
            <g class="pixel-kit__fill-water"><rect x="4" y="1" width="2" height="1" /><rect x="3" y="2" width="4" height="2" /><rect x="2" y="4" width="6" height="1" /><rect x="1" y="5" width="8" height="4" /><rect x="2" y="9" width="6" height="1" /></g>
            <g class="pixel-kit__fill-white"><rect x="2" y="5" width="1" height="2" /></g>
            <g class="pixel-kit__fill-ink"><rect x="4" y="6" width="1" height="2" /><rect x="6" y="6" width="1" height="2" /><rect x="4" y="8" width="3" height="1" /></g>
          </svg>
        </div>
        <div class="pixel-kit__dialog">
          <p class="pixel-kit__msg" aria-hidden="true"><span class="pixel-kit__typed">A wild LEAK appeared!</span><span class="pixel-kit__rest"></span></p>
          <p class="pixel-kit__sr pixel-kit__said" aria-live="polite">A wild LEAK appeared!</p>
          <button class="pixel-kit__next" type="button" aria-label="Next message" data-pixel-kit-js hidden></button>
        </div>
        <ul class="pixel-kit__menu" role="list">
          <li><a class="pixel-kit__choice" href="tel:+15555550123">Call BRAND</a></li>
          <li data-pixel-kit-js hidden><button class="pixel-kit__choice pixel-kit__run" type="button">Run</button></li>
        </ul>
      </div>

      <div class="pixel-kit__window pixel-kit__board">
        <table class="pixel-kit__scores">
          <caption>High scores<span>Top-rated Brand techs this month</span></caption>
          <thead>
            <tr><th scope="col">Rank</th><th scope="col">Tech</th><th scope="col">Jobs</th><th scope="col">Rating</th></tr>
          </thead>
          <tbody>
            <tr><td class="pixel-kit__rank">1st</td><th scope="row">Sam K.<span>Plumbing</span></th><td>1,284</td><td>4.98</td></tr>
            <tr><td class="pixel-kit__rank">2nd</td><th scope="row">Maria R.<span>Electrical</span></th><td>1,102</td><td>4.97</td></tr>
            <tr><td class="pixel-kit__rank">3rd</td><th scope="row">Jo P.<span>Heating</span></th><td>986</td><td>4.96</td></tr>
            <tr><td class="pixel-kit__rank">4th</td><th scope="row">Alex T.<span>Roofing</span></th><td>874</td><td>4.95</td></tr>
            <tr><td class="pixel-kit__rank">5th</td><th scope="row">Dev N.<span>Handyman</span></th><td>812</td><td>4.94</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>
```

## CSS

```css
/* Local NES palette. Pixel unit = --space-xs (4px); corner shapes are stepped polygons */
.pixel-kit {
  --pixel-kit-sky: #5c94fc;
  --pixel-kit-mist: #a4e4fc;
  --pixel-kit-white: #fcfcfc;
  --pixel-kit-grass: #00a800;
  --pixel-kit-leaf: #80d010;
  --pixel-kit-pine: #005800;
  --pixel-kit-brick: #c84c0c;
  --pixel-kit-brick-hi: #fc9838;
  --pixel-kit-brick-lo: #881400;
  --pixel-kit-coin: #f8b800;
  --pixel-kit-coin-lo: #ac7c00;
  --pixel-kit-cream: #fce0a8;
  --pixel-kit-water: #3cbcfc;
  --pixel-kit-cave: #0058f8;
  --pixel-kit-ink: #000000;
  --pixel-kit-font: "Press Start 2P", var(--font-mono);
  --pixel-kit-u: var(--space-xs);
  --pixel-kit-notch: polygon(0.25rem 0, calc(100% - 0.25rem) 0, calc(100% - 0.25rem) 0.25rem, 100% 0.25rem, 100% calc(100% - 0.25rem), calc(100% - 0.25rem) calc(100% - 0.25rem), calc(100% - 0.25rem) 100%, 0.25rem 100%, 0.25rem calc(100% - 0.25rem), 0 calc(100% - 0.25rem), 0 0.25rem, 0.25rem 0.25rem);
  --pixel-kit-notch-2: polygon(0.5rem 0, calc(100% - 0.5rem) 0, calc(100% - 0.5rem) 0.25rem, calc(100% - 0.25rem) 0.25rem, calc(100% - 0.25rem) 0.5rem, 100% 0.5rem, 100% calc(100% - 0.5rem), calc(100% - 0.25rem) calc(100% - 0.5rem), calc(100% - 0.25rem) calc(100% - 0.25rem), calc(100% - 0.5rem) calc(100% - 0.25rem), calc(100% - 0.5rem) 100%, 0.5rem 100%, 0.5rem calc(100% - 0.25rem), 0.25rem calc(100% - 0.25rem), 0.25rem calc(100% - 0.5rem), 0 calc(100% - 0.5rem), 0 0.5rem, 0.25rem 0.5rem, 0.25rem 0.25rem, 0.5rem 0.25rem);
  overflow: clip; color: var(--pixel-kit-ink); font-family: var(--font-mono);
}
.pixel-kit__start, .pixel-kit__title, .pixel-kit__stat, .pixel-kit__face, .pixel-kit__block-face, .pixel-kit__hp-label,
.pixel-kit__msg, .pixel-kit__choice, .pixel-kit__scores caption, .pixel-kit__scores thead th, .pixel-kit__rank {
  font-family: var(--pixel-kit-font); font-weight: 400; text-transform: uppercase; -webkit-font-smoothing: none;
}
.pixel-kit__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Sprite fills */
.pixel-kit__fill-ink { fill: var(--pixel-kit-ink); }
.pixel-kit__fill-white { fill: var(--pixel-kit-white); }
.pixel-kit__fill-mist { fill: var(--pixel-kit-mist); }
.pixel-kit__fill-brick { fill: var(--pixel-kit-brick); }
.pixel-kit__fill-brick-lo { fill: var(--pixel-kit-brick-lo); }
.pixel-kit__fill-coin { fill: var(--pixel-kit-coin); }
.pixel-kit__fill-cream { fill: var(--pixel-kit-cream); }
.pixel-kit__fill-water { fill: var(--pixel-kit-water); }
.pixel-kit__fill-grass { fill: var(--pixel-kit-grass); }
.pixel-kit__fill-leaf { fill: var(--pixel-kit-leaf); }
.pixel-kit__fill-pine { fill: var(--pixel-kit-pine); }

/* HUD */
.pixel-kit__hud { background: var(--pixel-kit-ink); color: var(--pixel-kit-white); }
.pixel-kit__hud-inner {
  display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: var(--space-sm);
  max-width: var(--container-max); margin-inline: auto; padding: 0.875rem var(--gutter);
}
.pixel-kit__stat { display: grid; gap: var(--space-sm); justify-items: start; margin: 0; font-size: 0.5rem; line-height: 1; }
.pixel-kit__stat > span { display: inline-flex; align-items: center; gap: 0.25em; }
.pixel-kit__count { display: inline-block; }
.pixel-kit__coin, .pixel-kit__pop {
  display: inline-block; background: linear-gradient(90deg, var(--pixel-kit-coin) 0 37.5%, var(--pixel-kit-cream) 37.5% 62.5%, var(--pixel-kit-coin) 62.5%);
  clip-path: polygon(25% 0, 75% 0, 75% 12.5%, 100% 12.5%, 100% 87.5%, 75% 87.5%, 75% 100%, 25% 100%, 25% 87.5%, 0 87.5%, 0 12.5%, 25% 12.5%);
}
.pixel-kit__coin { width: 0.75em; height: 1em; }
.pixel-kit__coins.is-hop .pixel-kit__count { animation: pixel-kit-hop var(--dur-3) steps(3, end); }
.pixel-kit__coins.is-hop .pixel-kit__coin { animation: pixel-kit-spin var(--dur-4) steps(4, end); }
@media (min-width: 768px) { .pixel-kit__stat { font-size: 0.75rem; } }

/* Overworld */
.pixel-kit__world { position: relative; isolation: isolate; background: var(--pixel-kit-sky); }
.pixel-kit__cloud { position: absolute; z-index: -1; height: auto; }
.pixel-kit__cloud--a { top: 1.75rem; right: 6%; width: 6rem; }
.pixel-kit__cloud--b { display: none; top: 40%; left: 50%; width: 4.5rem; }
@media (min-width: 768px) { .pixel-kit__cloud--b { display: block; } }
.pixel-kit__world-inner {
  display: grid; gap: 1rem;
  max-width: var(--container-max); margin-inline: auto; padding: clamp(3rem, 7vw, 5rem) var(--gutter) 0;
}
@media (min-width: 768px) { .pixel-kit__world-inner { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); align-items: end; gap: 2rem; } }
.pixel-kit__copy { align-self: center; padding-bottom: 1rem; }
@media (min-width: 768px) { .pixel-kit__copy { padding-bottom: 3.5rem; } }
.pixel-kit__start { margin: 0; font-size: 0.625rem; letter-spacing: 0.1em; }
.pixel-kit__world.is-live .pixel-kit__start { animation: pixel-kit-blink 1s steps(1, end) 4; }
.pixel-kit__title {
  margin: 1rem 0 0; font-size: clamp(1rem, 0.55rem + 2.25vw, 2rem); line-height: 1.45; text-wrap: balance;
  text-shadow: 0.125em 0.125em 0 var(--pixel-kit-cream);
}
.pixel-kit__lead { max-width: 30rem; margin: 1.25rem 0 0; font-size: 0.9375rem; font-weight: 500; line-height: 1.65; }

/* Pixel buttons: ink silhouette + cast shadow (pseudos), clipped face; the face presses into the shadow */
.pixel-kit__actions { display: flex; flex-wrap: wrap; gap: 1rem 0.75rem; margin-top: 2rem; }
.pixel-kit__btn { position: relative; isolation: isolate; display: inline-flex; padding: 0.25rem 0.25rem 0.5rem; color: var(--pixel-kit-ink); text-decoration: none; cursor: pointer; }
.pixel-kit__btn::before, .pixel-kit__btn::after { content: ""; position: absolute; left: 0; right: 0; clip-path: var(--pixel-kit-notch-2); }
.pixel-kit__btn::before { top: 0; bottom: 0.25rem; z-index: -1; background: var(--pixel-kit-ink); transition: transform var(--dur-3) var(--ease-spring); }
.pixel-kit__btn::after { top: 0.25rem; bottom: 0; z-index: -2; background: color-mix(in srgb, var(--pixel-kit-ink) 45%, var(--pixel-kit-sky)); }
.pixel-kit__face {
  display: flex; align-items: center; min-height: 2.25rem; padding: 0 1rem; clip-path: var(--pixel-kit-notch);
  background: var(--pixel-kit-white); box-shadow: inset 0 calc(var(--pixel-kit-u) * -1) 0 var(--pixel-kit-mist);
  font-size: 0.625rem; line-height: 1.3;
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2);
}
.pixel-kit__btn--coin .pixel-kit__face { background: var(--pixel-kit-coin); box-shadow: inset 0 var(--pixel-kit-u) 0 var(--pixel-kit-cream), inset 0 calc(var(--pixel-kit-u) * -1) 0 var(--pixel-kit-coin-lo); }
.pixel-kit__btn:hover .pixel-kit__face { background: var(--pixel-kit-cream); }
.pixel-kit__btn--coin:hover .pixel-kit__face { background: color-mix(in srgb, var(--pixel-kit-coin) 70%, var(--pixel-kit-cream)); }
.pixel-kit__btn:is(:active, .is-down)::before, .pixel-kit__btn:is(:active, .is-down) .pixel-kit__face { transform: translateY(var(--pixel-kit-u)); transition-duration: var(--dur-1); }
.pixel-kit__btn:focus-visible, .pixel-kit__block:focus-visible { outline: 2px solid var(--pixel-kit-ink); outline-offset: 3px; }
@media (min-width: 768px) { .pixel-kit__face { font-size: 0.75rem; padding: 0 1.25rem; } }

/* Satisfaction HP bar: segmented by a mask, revealed one segment per step */
.pixel-kit__hp { max-width: 24rem; margin-top: 2rem; }
.pixel-kit__hp-label { display: flex; align-items: center; gap: 0.625rem; margin: 0 0 0.625rem; font-size: 0.625rem; line-height: 1; }
.pixel-kit__hp-tag { padding: 0.25rem 0.375rem; background: var(--pixel-kit-ink); color: var(--pixel-kit-coin); }
.pixel-kit__hp-value { margin-left: auto; }
.pixel-kit__hp-bar { display: block; height: 1.25rem; padding: var(--pixel-kit-u); background: var(--pixel-kit-ink); clip-path: var(--pixel-kit-notch); }
.pixel-kit__hp-fill {
  display: block; height: 100%; clip-path: inset(0 2% 0 0);
  background: linear-gradient(var(--pixel-kit-leaf) 0 35%, var(--pixel-kit-grass) 35%);
  -webkit-mask: repeating-linear-gradient(90deg, black 0 calc(5% - 2px), transparent calc(5% - 2px) 5%);
  mask: repeating-linear-gradient(90deg, black 0 calc(5% - 2px), transparent calc(5% - 2px) 5%);
}
.pixel-kit__world.is-live .pixel-kit__hp-fill { animation: pixel-kit-fill calc(var(--dur-5) * 1.8) steps(20, end) both; }

/* Stage: ? block above the house */
.pixel-kit__stage { display: grid; gap: 1.5rem; justify-items: center; padding-top: 4.5rem; }
.pixel-kit__stage:has(.pixel-kit__block[hidden]) { padding-top: 1.5rem; }
.pixel-kit__block { position: relative; justify-self: start; width: 3.5rem; height: 3.5rem; margin-left: 14%; padding: 0; border: 0; background: none; cursor: pointer; }
.pixel-kit__block[hidden] { display: none; }
.pixel-kit__block-face {
  display: grid; place-items: center; width: 100%; height: 100%; clip-path: var(--pixel-kit-notch);
  background:
    linear-gradient(var(--pixel-kit-ink) 0 0) 0.5rem 0.5rem / 0.25rem 0.25rem no-repeat,
    linear-gradient(var(--pixel-kit-ink) 0 0) calc(100% - 0.5rem) 0.5rem / 0.25rem 0.25rem no-repeat,
    linear-gradient(var(--pixel-kit-ink) 0 0) 0.5rem calc(100% - 0.5rem) / 0.25rem 0.25rem no-repeat,
    linear-gradient(var(--pixel-kit-ink) 0 0) calc(100% - 0.5rem) calc(100% - 0.5rem) / 0.25rem 0.25rem no-repeat,
    var(--pixel-kit-coin);
  box-shadow: inset 0 0 0 0.25rem var(--pixel-kit-ink), inset 0.5rem 0.5rem 0 var(--pixel-kit-cream), inset -0.5rem -0.5rem 0 var(--pixel-kit-coin-lo);
  color: var(--pixel-kit-brick-lo); font-size: 1.25rem; line-height: 1; text-shadow: 0.125rem 0.125rem 0 var(--pixel-kit-cream);
}
.pixel-kit__pop { position: absolute; left: 50%; top: 0; width: 1rem; height: 1.5rem; margin-left: -0.5rem; opacity: 0; pointer-events: none; }
.pixel-kit__block.is-bump .pixel-kit__block-face { animation: pixel-kit-bump var(--dur-3) steps(4, end); }
.pixel-kit__block.is-bump .pixel-kit__pop { animation: pixel-kit-pop calc(var(--dur-5) * 0.8) steps(10, end); }
.pixel-kit__house { width: min(100%, 18rem); height: auto; }
@media (min-width: 768px) { .pixel-kit__house { width: min(100%, 22rem); } }

/* Ground: grass lip plus two courses of offset bricks */
.pixel-kit__ground {
  position: relative; height: 2.5rem;
  background: linear-gradient(90deg, var(--pixel-kit-leaf) 50%, var(--pixel-kit-grass) 50%) 0 0 / 1rem var(--pixel-kit-u) repeat-x, var(--pixel-kit-grass);
}
.pixel-kit__ground::before, .pixel-kit__ground::after {
  content: ""; position: absolute; left: 0; right: 0; height: 1rem;
  background:
    linear-gradient(90deg, var(--pixel-kit-ink) 0 var(--pixel-kit-u), transparent 0) 0 0 / 2rem 100%,
    linear-gradient(var(--pixel-kit-brick-hi) 0 var(--pixel-kit-u), var(--pixel-kit-brick) 0 calc(100% - var(--pixel-kit-u)), var(--pixel-kit-ink) 0);
}
.pixel-kit__ground::before { top: 0.5rem; }
.pixel-kit__ground::after { top: 1.5rem; background-position: 1rem 0, 0 0; }

/* Underground: two windows with a light ring and pixel-rounded corners */
.pixel-kit__under { background: var(--pixel-kit-ink); color: var(--pixel-kit-white); }
.pixel-kit__under-inner {
  display: grid; gap: 1.5rem;
  max-width: var(--container-max); margin-inline: auto; padding: clamp(2.5rem, 6vw, 4rem) var(--gutter) clamp(3rem, 7vw, 5rem);
}
@media (min-width: 768px) { .pixel-kit__under-inner { grid-template-columns: repeat(2, minmax(0, 1fr)); align-items: start; } }
.pixel-kit__window {
  position: relative; padding: 1.5rem 1.25rem 1.25rem; clip-path: var(--pixel-kit-notch);
  background: var(--pixel-kit-ink);
  box-shadow: inset 0 0 0 0.25rem var(--pixel-kit-white), inset 0 0 0 0.5rem var(--pixel-kit-ink), inset 0 0 0 0.625rem color-mix(in srgb, var(--pixel-kit-white) 28%, var(--pixel-kit-ink));
}
@media (min-width: 768px) { .pixel-kit__window { padding: 1.75rem; } }

/* Battle: arena, typed message, menu */
.pixel-kit__arena {
  display: flex; align-items: flex-end; justify-content: center; gap: 1.5rem; height: 7.5rem; margin-bottom: 1.25rem; padding-bottom: 0.5rem;
  background:
    linear-gradient(transparent calc(100% - 0.5rem), var(--pixel-kit-cave) 0),
    radial-gradient(ellipse 60% 80% at 50% 100%, color-mix(in srgb, var(--pixel-kit-water) 22%, transparent), transparent 70%);
}
.pixel-kit__pipe { width: 5rem; height: auto; }
.pixel-kit__leak { width: 2.5rem; height: auto; margin-bottom: 1rem; }
.pixel-kit__battle.is-live .pixel-kit__leak { animation: pixel-kit-appear var(--dur-5) steps(6, end) both; }
.pixel-kit__dialog { position: relative; padding-right: 2.25rem; }
.pixel-kit__msg { min-height: calc(1.9em * 3); margin: 0; font-size: 0.6875rem; line-height: 1.9; }
.pixel-kit__rest { visibility: hidden; }
.pixel-kit__next { position: absolute; right: 0; bottom: 0; display: grid; place-items: center; width: 2rem; height: 2rem; padding: 0; border: 0; background: none; color: var(--pixel-kit-white); cursor: pointer; }
.pixel-kit__next[hidden] { display: none; }
.pixel-kit__next::before {
  content: ""; width: 0.75rem; height: 0.375rem; background: currentColor;
  clip-path: polygon(0 0, 100% 0, 100% 33.33%, 83.33% 33.33%, 83.33% 66.66%, 66.66% 66.66%, 66.66% 100%, 33.33% 100%, 33.33% 66.66%, 16.66% 66.66%, 16.66% 33.33%, 0 33.33%);
}
.pixel-kit__next.is-blink::before { animation: pixel-kit-blink 1s steps(1, end) 5; }
.pixel-kit__menu { display: flex; flex-wrap: wrap; gap: 0.25rem 1.5rem; margin: 1rem 0 0; padding: 1rem 0 0; border-top: 2px dashed color-mix(in srgb, var(--pixel-kit-white) 30%, transparent); list-style: none; }
.pixel-kit__menu li[hidden] { display: none; }
.pixel-kit__choice {
  position: relative; display: inline-flex; align-items: center; min-height: 2.75rem; padding: 0 0.75rem 0 1.75rem;
  border: 0; background: none; color: var(--pixel-kit-white); font-size: 0.6875rem; line-height: 1; text-decoration: none; cursor: pointer;
}
.pixel-kit__choice::before {
  content: ""; position: absolute; left: 0.5rem; top: 50%; width: 0.375rem; height: 0.75rem; translate: 0 -50%; visibility: hidden;
  background: var(--pixel-kit-coin);
  clip-path: polygon(0 0, 33.33% 0, 33.33% 16.66%, 66.66% 16.66%, 66.66% 33.33%, 100% 33.33%, 100% 66.66%, 66.66% 66.66%, 66.66% 83.33%, 33.33% 83.33%, 33.33% 100%, 0 100%);
}
.pixel-kit__choice:is(:hover, :focus-visible)::before { visibility: visible; }
.pixel-kit__menu:not(:has(:hover, :focus-visible)) li:first-child .pixel-kit__choice::before { visibility: visible; }
.pixel-kit__choice:focus-visible, .pixel-kit__next:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* High scores */
.pixel-kit__scores { width: 100%; border-collapse: collapse; font-size: 0.8125rem; line-height: 1.35; font-variant-numeric: tabular-nums; }
.pixel-kit__scores caption { margin-bottom: 1rem; color: var(--pixel-kit-coin); font-size: 0.75rem; line-height: 1.4; text-align: left; }
.pixel-kit__scores caption span { display: block; margin-top: 0.625rem; color: var(--pixel-kit-mist); font: 500 0.75rem/1.4 var(--font-mono); text-transform: none; -webkit-font-smoothing: auto; }
.pixel-kit__scores th, .pixel-kit__scores td { padding: 0.625rem 0.25rem; text-align: left; vertical-align: top; }
.pixel-kit__scores thead th { padding-bottom: 0.75rem; border-bottom: 0.25rem solid color-mix(in srgb, var(--pixel-kit-white) 25%, transparent); color: var(--pixel-kit-mist); font-size: 0.5rem; line-height: 1; }
.pixel-kit__scores tbody tr + tr > * { border-top: 2px dashed color-mix(in srgb, var(--pixel-kit-white) 18%, transparent); }
.pixel-kit__scores tbody th { font-weight: 600; }
.pixel-kit__scores tbody th span { display: block; color: var(--pixel-kit-mist); font-size: 0.6875rem; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; }
.pixel-kit__scores :is(th, td):last-child { text-align: right; color: var(--pixel-kit-coin); }
.pixel-kit__scores thead th:last-child { color: var(--pixel-kit-mist); }
.pixel-kit__rank { font-size: 0.625rem; line-height: 1.6; }
.pixel-kit__scores tbody tr:nth-child(1) .pixel-kit__rank { color: var(--pixel-kit-coin); }
.pixel-kit__scores tbody tr:nth-child(3) .pixel-kit__rank { color: var(--pixel-kit-brick-hi); }
.pixel-kit__scores tbody tr:nth-child(n + 4) .pixel-kit__rank { color: var(--pixel-kit-mist); }
@media (min-width: 768px) { .pixel-kit__scores th, .pixel-kit__scores td { padding-inline: 0.5rem; } }

/* Start states for in-view reveals, with a failsafe if the script never arrives */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .pixel-kit__world:not(.is-live) .pixel-kit__hp-fill { clip-path: inset(0 100% 0 0); animation: pixel-kit-failsafe-fill 0s 3s forwards; }
  .pixel-kit__battle:not(.is-live) .pixel-kit__msg, .pixel-kit__battle:not(.is-live) .pixel-kit__leak { visibility: hidden; animation: pixel-kit-failsafe-show 0s 3s forwards; }
  .pixel-kit--js .pixel-kit__world:not(.is-live) .pixel-kit__hp-fill,
  .pixel-kit--js .pixel-kit__battle:not(.is-live) .pixel-kit__msg,
  .pixel-kit--js .pixel-kit__battle:not(.is-live) .pixel-kit__leak { animation: none; }
}

@media (prefers-reduced-motion: reduce) {
  .pixel-kit *, .pixel-kit *::before, .pixel-kit *::after { animation: none !important; }
}

@keyframes pixel-kit-blink { 50% { opacity: 0; } }
@keyframes pixel-kit-fill { from { clip-path: inset(0 100% 0 0); } }
@keyframes pixel-kit-appear { from { opacity: 0; transform: translateY(-1.5rem); } }
@keyframes pixel-kit-bump { 50% { transform: translateY(calc(var(--pixel-kit-u) * -2)); } }
@keyframes pixel-kit-hop { 50% { transform: translateY(-0.375rem); } }
@keyframes pixel-kit-spin { 25%, 75% { transform: scaleX(0.3); } 50% { transform: scaleX(-1); } }
@keyframes pixel-kit-pop {
  0% { opacity: 1; transform: translateY(0) scaleX(1); }
  25% { transform: translateY(-3.5rem) scaleX(0.3); }
  50% { transform: translateY(-5rem) scaleX(1); }
  75% { opacity: 1; transform: translateY(-4.25rem) scaleX(0.3); }
  100% { opacity: 0; transform: translateY(-3rem) scaleX(1); }
}
@keyframes pixel-kit-failsafe-fill { to { clip-path: inset(0 2% 0 0); } }
@keyframes pixel-kit-failsafe-show { to { visibility: visible; } }
```

## JS

```js
const LINES = ['A wild LEAK appeared!', 'LEAK used DRIP. Your water bill rose 12%!', "BRAND can be there today. It's super effective!"];
const RUN = "Can't escape! Leaks only get worse.";

document.querySelectorAll('[data-pixel-kit]').forEach((kit) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const [world, battle, typed, rest, said, next, coins, count, score, run] = ['world', 'battle', 'typed', 'rest', 'said', 'next', 'coins', 'count', 'score', 'run']
    .map((part) => kit.querySelector(`.pixel-kit__${part}`));
  let total = Number(count.textContent);
  let points = Number(score.textContent);
  let line = 0;
  let timer = 0;

  kit.classList.add('pixel-kit--js');
  kit.querySelectorAll('[data-pixel-kit-js]').forEach((el) => { el.hidden = false; });

  // Restart a one-shot CSS animation by re-adding its class
  const replay = (el, name) => { el.classList.remove(name); void el.offsetWidth; el.classList.add(name); };

  // Typewriter: the untyped remainder stays in place but invisible, so words never jump lines.
  // Screen readers get the whole message at once from the polite live copy.
  const say = (text) => {
    clearInterval(timer);
    said.textContent = text;
    next.classList.remove('is-blink');
    let i = reduce.matches ? text.length : 0;
    const tick = () => {
      typed.textContent = text.slice(0, i);
      rest.textContent = text.slice(i);
      if (i++ < text.length) return;
      clearInterval(timer);
      replay(next, 'is-blink');
    };
    tick();
    if (i <= text.length) timer = setInterval(tick, 34);
  };

  // Every pixel-button press banks a coin and 200 points; the counter hops
  const bank = () => {
    total = Math.min(99, total + 1);
    points += 200;
    count.textContent = String(total).padStart(2, '0');
    score.textContent = String(points).padStart(6, '0');
    if (!reduce.matches) replay(coins, 'is-hop');
  };
  kit.addEventListener('click', (event) => {
    const button = event.target.closest('.pixel-kit__btn, .pixel-kit__block, .pixel-kit__choice');
    if (!button) return;
    bank();
    // Keyboard presses get the same press-down as :active
    button.classList.add('is-down');
    setTimeout(() => button.classList.remove('is-down'), 140);
    if (button.matches('.pixel-kit__block') && !reduce.matches) replay(button, 'is-bump');
  });
  next.addEventListener('click', () => { line = (line + 1) % LINES.length; say(LINES[line]); });
  run.addEventListener('click', () => say(RUN));

  // Each level wakes up when it scrolls into view
  const io = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    io.unobserve(entry.target);
    entry.target.classList.add('is-live');
    if (entry.target === battle) say(LINES[0]);
  }), { threshold: 0.3 });
  [world, battle].forEach((el) => io.observe(el));
});
```

## Notes

- One `<h2>`, real links and buttons, and a semantic `<table>` with a caption and column/row headers. The house, clouds, pipe, LEAK, ground and most HUD stats are decorative (`aria-hidden`), but the coin counter is a polite live region ("Coins 08"). The battle text types into an `aria-hidden` paragraph while a visually hidden live copy announces each message once. The ▶ menu cursor follows hover and focus, as it does in a real RPG menu.
- Focus: on the sky, buttons get a 2px ink outline (7.1:1) because `--primary` is only 1.75:1 against NES sky blue. In the underground, controls get the dark-surface `--text-inverse` outline. Each pixel button's clip-path sits on an inner face, so the focus outline is never clipped. Pixel buttons, the ? block and menu choices are 44px or larger; the advance arrow is 32px.
- Contrast: ink text on sky 7.1:1, ink on coin 11.9:1, white on ink 20.5:1, coin on ink 11.9:1, mist on ink 15.1:1, orange rank on ink 9.7:1. White text never sits on the sky (2.9:1), which is why the HUD has its own ink bar.
- Without JS, the battle box shows its message with a working CALL BRAND link, the HP bar is full, and the JS-only controls (? block, RUN, advance arrow) stay `hidden`. If scripting is on but the module fails, a 3s CSS failsafe reveals the hidden start states. Under reduced motion there's no blink, typewriter, drop-in, bump, pop or hop: text appears whole and the coin count still updates.
- Every animation is finite (the longest is the 5s arrow blink), so no pause control is needed. `steps()` easing gives sprites an 8-bit frame rate; releases use `--ease-spring`.
- Retheme by swapping the palette (for example, a Game Boy set of four greens). Sprites are grouped by fill class, so recolouring never touches the SVG. The pixel unit is `--space-xs`, and `--pixel-kit-notch` / `--pixel-kit-notch-2` give 1- and 2-step corners to any element.
