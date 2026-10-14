# Circular Text Badges

Three circular text badges set with SVG `textPath`, each ring sized with `textLength` so the words meet themselves exactly. The signature is the deep "Book a visit" badge: it turns as the page scrolls, winds up to a faster spin while hovered and coasts to a stop, and its arrow slides through the core. A gradient seal and a small scroll badge complete the set, framed in a light same-day-service section. On phones the art card runs full width with the badge hanging off its lower edge, and the scroll badge centres at the end. Depends on `tokens/variables.css`.

**Motion:** scroll-linked ring rotation (CSS `animation-timeline: scroll()`, rAF fallback, linear scrub) · hover spin-up and coast (rAF, exponential ease) · arrow slide-through (`--dur-4`, `--ease-out`) · core and seal spring (`--ease-spring`) · star pop (`--dur-4`, `--stagger`). No autonomous loops.

## HTML

```html
<div class="circle-text-demo">
  <div class="circle-text-demo__intro">
    <p>Words set on a circle, turning as you scroll.</p>
    <span class="circle-text-demo__hint">Scroll</span>
  </div>

  <section class="circle-text" aria-labelledby="circle-text-title" data-circle-text>
    <div class="circle-text__inner">
      <div class="circle-text__copy">
        <p class="circle-text__eyebrow">Same-day service</p>
        <h2 id="circle-text-title" class="circle-text__title">
          <span class="circle-text__line">Booked by noon.</span>
          <span class="circle-text__line circle-text__line--accent">Fixed by dinner.</span>
        </h2>
        <p class="circle-text__lead">Licensed plumbers and electricians across Westlake, Northside and Riverside. Book before noon and we're at your door the same afternoon.</p>

        <div class="circle-text__proof">
          <a class="circle-text__seal" href="#reviews">
            <span class="circle-text__sr">Rated 4.9 out of 5. Licensed, insured and guaranteed. Read our reviews</span>
            <svg class="circle-text__seal-art" viewBox="0 0 200 200" aria-hidden="true" focusable="false">
              <defs>
                <linearGradient id="circle-text-seal-grad" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0" class="circle-text__stop-a" />
                  <stop offset="1" class="circle-text__stop-b" />
                </linearGradient>
                <path id="circle-text-seal-path" d="M37.79 100a62.21 62.21 0 1 1 124.41 0a62.21 62.21 0 1 1 -124.41 0" />
              </defs>
              <path class="circle-text__rosette" fill="url(#circle-text-seal-grad)" d="M100 9A11 11 0 0 1 120.25 11.28A11 11 0 0 1 139.48 18.01A11 11 0 0 1 156.74 28.85A11 11 0 0 1 171.15 43.26A11 11 0 0 1 181.99 60.52A11 11 0 0 1 188.72 79.75A11 11 0 0 1 191 100A11 11 0 0 1 188.72 120.25A11 11 0 0 1 181.99 139.48A11 11 0 0 1 171.15 156.74A11 11 0 0 1 156.74 171.15A11 11 0 0 1 139.48 181.99A11 11 0 0 1 120.25 188.72A11 11 0 0 1 100 191A11 11 0 0 1 79.75 188.72A11 11 0 0 1 60.52 181.99A11 11 0 0 1 43.26 171.15A11 11 0 0 1 28.85 156.74A11 11 0 0 1 18.01 139.48A11 11 0 0 1 11.28 120.25A11 11 0 0 1 9 100A11 11 0 0 1 11.28 79.75A11 11 0 0 1 18.01 60.52A11 11 0 0 1 28.85 43.26A11 11 0 0 1 43.26 28.85A11 11 0 0 1 60.52 18.01A11 11 0 0 1 79.75 11.28A11 11 0 0 1 100 9Z" />
              <circle class="circle-text__disc" cx="100" cy="100" r="84" />
              <circle class="circle-text__hairline" cx="100" cy="100" r="80" />
              <g class="circle-text__seal-ring">
                <text class="circle-text__label"><textPath href="#circle-text-seal-path" textLength="390.9" lengthAdjust="spacing">LICENSED <tspan class="circle-text__sep">•</tspan> INSURED <tspan class="circle-text__sep">•</tspan> GUARANTEED <tspan class="circle-text__sep">•</tspan>&#160;</textPath></text>
              </g>
              <circle class="circle-text__hairline" cx="100" cy="100" r="55" />
              <path class="circle-text__star" style="--circle-text-i: 0" d="M72 69.8L73.59 73.82L77.9 74.08L74.57 76.83L75.64 81.02L72 78.7L68.36 81.02L69.43 76.83L66.1 74.08L70.41 73.82Z" />
              <path class="circle-text__star" style="--circle-text-i: 1" d="M86 69.8L87.59 73.82L91.9 74.08L88.57 76.83L89.64 81.02L86 78.7L82.36 81.02L83.43 76.83L80.1 74.08L84.41 73.82Z" />
              <path class="circle-text__star" style="--circle-text-i: 2" d="M100 69.8L101.59 73.82L105.9 74.08L102.57 76.83L103.64 81.02L100 78.7L96.36 81.02L97.43 76.83L94.1 74.08L98.41 73.82Z" />
              <path class="circle-text__star" style="--circle-text-i: 3" d="M114 69.8L115.59 73.82L119.9 74.08L116.57 76.83L117.64 81.02L114 78.7L110.36 81.02L111.43 76.83L108.1 74.08L112.41 73.82Z" />
              <path class="circle-text__star" style="--circle-text-i: 4" d="M128 69.8L129.59 73.82L133.9 74.08L130.57 76.83L131.64 81.02L128 78.7L124.36 81.02L125.43 76.83L122.1 74.08L126.41 73.82Z" />
              <text class="circle-text__score" x="100" y="126">4.9</text>
            </svg>
          </a>
          <ul class="circle-text__facts" role="list">
            <li class="circle-text__fact"><strong>4.9 out of 5</strong> from 1,200+ Springfield homeowners</li>
            <li class="circle-text__fact">Licensed, insured and guaranteed</li>
          </ul>
        </div>
      </div>

      <div class="circle-text__visual">
        <div class="circle-text__art" aria-hidden="true">
          <div class="circle-text__slots">
            <p class="circle-text__slots-head"><strong>Today</strong><span>Westlake</span></p>
            <ul class="circle-text__slot-list" role="list">
              <li class="circle-text__slot is-gone"><span>8–10 am</span><em>Booked</em></li>
              <li class="circle-text__slot"><span>12–2 pm</span><em>Open</em></li>
              <li class="circle-text__slot is-pick"><span>2–4 pm</span><em>2 left</em></li>
            </ul>
          </div>
        </div>

        <a class="circle-text__cta" href="#book">
          <span class="circle-text__sr">Book a visit, same-day service</span>
          <span class="circle-text__turn" aria-hidden="true">
            <span class="circle-text__spin">
              <svg class="circle-text__ring" viewBox="0 0 200 200" focusable="false">
                <path id="circle-text-cta-path" class="circle-text__path" d="M25.52 100a74.48 74.48 0 1 1 148.97 0a74.48 74.48 0 1 1 -148.97 0" />
                <text class="circle-text__label"><textPath href="#circle-text-cta-path" textLength="468" lengthAdjust="spacing">BOOK A VISIT <tspan class="circle-text__sep">•</tspan> SAME-DAY SERVICE <tspan class="circle-text__sep">•</tspan>&#160;</textPath></text>
              </svg>
            </span>
          </span>
          <span class="circle-text__core" aria-hidden="true">
            <svg class="circle-text__arrow circle-text__arrow--out" viewBox="0 0 24 24" width="24" height="24" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg>
            <svg class="circle-text__arrow circle-text__arrow--in" viewBox="0 0 24 24" width="24" height="24" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg>
          </span>
        </a>
      </div>

      <a class="circle-text__scroll" href="#circle-text-next">
        <span class="circle-text__sr">Scroll to how it works</span>
        <span class="circle-text__turn" aria-hidden="true">
          <svg class="circle-text__ring" viewBox="0 0 200 200" focusable="false">
            <path id="circle-text-scroll-path" class="circle-text__path" d="M30.75 100a69.25 69.25 0 1 1 138.49 0a69.25 69.25 0 1 1 -138.49 0" />
            <text class="circle-text__label"><textPath href="#circle-text-scroll-path" textLength="435.1" lengthAdjust="spacing">SCROLL <tspan class="circle-text__sep">•</tspan> HOW IT WORKS <tspan class="circle-text__sep">•</tspan>&#160;</textPath></text>
          </svg>
        </span>
        <span class="circle-text__hub" aria-hidden="true">
          <svg class="circle-text__down" viewBox="0 0 24 24" width="24" height="24" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
        </span>
      </a>
    </div>
  </section>

  <div class="circle-text-demo__outro" id="circle-text-next">
    <p>How it works: book, track, done.</p>
    <span class="circle-text-demo__hint">Scroll back up</span>
  </div>
</div>
```

## CSS

```css
/* Section: light, with soft brand light in two corners */
.circle-text {
  --circle-text-turns: 1.25;  /* full turns across the whole page scroll */
  --circle-text-cta: clamp(8rem, 6.4rem + 5vw, 11rem);
  position: relative; overflow: clip;
  background:
    radial-gradient(60% 55% at 100% 0%, color-mix(in srgb, var(--primary-2) 9%, transparent), transparent 70%),
    radial-gradient(55% 50% at 0% 100%, color-mix(in srgb, var(--primary) 7%, transparent), transparent 70%),
    var(--surface-light);
  color: var(--text-main); font-family: var(--font-sans);
}
.circle-text__inner {
  display: grid; grid-template-areas: "copy" "visual" "scroll"; gap: 3rem;
  max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter);
}
.circle-text a:focus-visible { outline: 2px solid var(--primary); outline-offset: 4px; }
.circle-text__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* Copy */
.circle-text__copy { grid-area: copy; }
.circle-text__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; color: var(--primary); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.circle-text__eyebrow::before { content: ""; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--gradient-brand); box-shadow: 0 0 0 3px color-mix(in srgb, var(--primary) 14%, transparent); }
.circle-text__title { margin: 1rem 0 0; font: 600 clamp(2.25rem, 1.3rem + 3.8vw, 4.25rem)/1 var(--font-display); letter-spacing: var(--tracking-display); }
.circle-text__line { display: block; }
.circle-text__line--accent { width: fit-content; padding-bottom: 0.08em; background: var(--gradient-brand); -webkit-background-clip: text; background-clip: text; color: transparent; }
.circle-text__lead { max-width: 32rem; margin: 1.25rem 0 0; color: var(--text-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }
.circle-text__proof { display: flex; align-items: center; gap: 1.25rem; margin-top: 2rem; }
.circle-text__facts { display: grid; gap: 0.625rem; margin: 0; padding: 0; list-style: none; }
.circle-text__fact { position: relative; padding-left: 1.75rem; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.45; }
.circle-text__fact strong { color: var(--text-main); }
.circle-text__fact::before { content: ""; position: absolute; left: 0; top: 0.125rem; width: 1.125rem; height: 1.125rem; border-radius: 50%; background: color-mix(in srgb, var(--primary) 12%, transparent); }
.circle-text__fact::after { content: ""; position: absolute; left: 0.4375rem; top: 0.3125rem; width: 0.25rem; height: 0.5rem; border: solid var(--primary); border-width: 0 2px 2px 0; rotate: 45deg; }

/* Shared ring parts: text on a circle, turned by page scroll */
.circle-text__ring { display: block; width: 100%; height: 100%; overflow: visible; }
.circle-text__path { fill: none; }
.circle-text__label { font-family: var(--font-mono); font-size: var(--circle-text-fs); font-weight: 500; letter-spacing: 0; font-variant-ligatures: none; fill: currentColor; }
.circle-text__sep { fill: var(--circle-text-sep, currentColor); }
.circle-text__turn { position: absolute; inset: 0; rotate: calc(var(--circle-text-p, 0) * var(--circle-text-turns) * var(--circle-text-dir, 1) * 1turn); }
.circle-text__spin { position: absolute; inset: 0; rotate: var(--circle-text-spin, 0deg); }
@supports (animation-timeline: scroll()) {
  @media (prefers-reduced-motion: no-preference) {
    .circle-text__turn { animation: circle-text-turn linear both; animation-timeline: scroll(); }
  }
}

/* 1. CTA: the deep badge, hanging off the art card */
.circle-text__visual {
  --circle-text-cx: calc(1rem + var(--circle-text-cta) / 2);  /* badge centre, from the card's bottom-left */
  --circle-text-cy: calc(var(--circle-text-cta) * 0.1);
  grid-area: visual; position: relative; margin-bottom: calc(var(--circle-text-cta) * 0.4);
}
.circle-text__cta {
  --circle-text-fs: 22.94px;
  --circle-text-sep: color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse));
  position: absolute; z-index: 1; display: block;
  left: calc(var(--circle-text-cx) - var(--circle-text-cta) / 2); bottom: calc(var(--circle-text-cy) - var(--circle-text-cta) / 2);
  width: var(--circle-text-cta); aspect-ratio: 1; border-radius: 50%; color: var(--text-inverse); text-decoration: none;
  background: radial-gradient(circle at 30% 22%, color-mix(in srgb, var(--primary) 30%, var(--surface-deep)), var(--surface-deep) 72%);
  box-shadow:
    inset 0 0 0 1px var(--border-inverse), inset 0 0 0 7px var(--surface-deep), inset 0 0 0 8px var(--border-inverse), var(--highlight-inverse),
    0 28px 56px -18px color-mix(in srgb, var(--surface-deep) 65%, transparent);
}
.circle-text__core {
  position: absolute; inset: 22%; display: grid; place-items: center; overflow: hidden; border-radius: 50%;
  background: var(--gradient-brand); color: var(--text-inverse);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 35%, transparent), 0 10px 24px -8px color-mix(in srgb, var(--primary) 80%, transparent);
  transition: scale var(--dur-4) var(--ease-spring);
}
.circle-text__arrow { grid-area: 1 / 1; width: 40%; height: auto; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-4) var(--ease-out); }
.circle-text__arrow--in { translate: -170% 170%; }
.circle-text__cta:is(:hover, :focus-visible) .circle-text__core { scale: 1.06; }
.circle-text__cta:is(:hover, :focus-visible) .circle-text__arrow--out { translate: 170% -170%; }
.circle-text__cta:is(:hover, :focus-visible) .circle-text__arrow--in { translate: 0 0; transition-delay: 50ms; }

/* Art card: ripples radiate from the badge, a slot picker floats top right */
.circle-text__art {
  position: relative; aspect-ratio: 4 / 3; border-radius: var(--radius-2xl); overflow: hidden;
  background:
    radial-gradient(90% 80% at 100% 0%, color-mix(in srgb, var(--primary-2) 24%, transparent), transparent 65%),
    radial-gradient(80% 90% at 0% 100%, color-mix(in srgb, var(--primary) 22%, transparent), transparent 65%),
    var(--surface-muted);
  box-shadow: var(--shadow-xl), inset 0 0 0 1px var(--border-subtle);
}
.circle-text__art::before {
  content: ""; position: absolute; inset: 0;
  background: repeating-radial-gradient(circle at var(--circle-text-cx) calc(100% - var(--circle-text-cy)), transparent 0 calc(2.25rem - 1px), color-mix(in srgb, var(--primary) 22%, transparent) calc(2.25rem - 1px) 2.25rem);
  -webkit-mask-image: radial-gradient(circle at var(--circle-text-cx) calc(100% - var(--circle-text-cy)), black 15%, transparent 72%);
  mask-image: radial-gradient(circle at var(--circle-text-cx) calc(100% - var(--circle-text-cy)), black 15%, transparent 72%);
}
.circle-text__slots {
  position: absolute; top: 1rem; right: 1rem; width: min(14.5rem, 62%); padding: 0.875rem; border-radius: var(--radius-xl);
  background: var(--surface-light); box-shadow: var(--shadow-lg), inset 0 0 0 1px var(--border-subtle), var(--highlight);
}
.circle-text__slots-head { display: flex; justify-content: space-between; align-items: baseline; gap: 0.5rem; margin: 0 0 0.625rem; }
.circle-text__slots-head strong { font: 600 0.9375rem var(--font-display); letter-spacing: var(--tracking-tight); }
.circle-text__slots-head span { color: var(--text-muted); font: 500 0.6875rem var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.circle-text__slot-list { display: grid; gap: 0.375rem; margin: 0; padding: 0; list-style: none; }
.circle-text__slot { display: flex; justify-content: space-between; align-items: center; gap: 0.5rem; padding: 0.5rem 0.625rem; border-radius: 0.625rem; background: var(--surface-muted); font-size: 0.8125rem; font-weight: 600; }
.circle-text__slot em { color: var(--success); font: 500 0.6875rem var(--font-mono); letter-spacing: 0.04em; text-transform: uppercase; }
.circle-text__slot.is-gone { color: var(--text-muted); }
.circle-text__slot.is-gone span { text-decoration: line-through; }
.circle-text__slot.is-gone em { color: var(--text-muted); }
.circle-text__slot.is-pick { background: var(--text-main); color: var(--surface-light); box-shadow: 0 8px 18px -8px color-mix(in srgb, var(--text-main) 80%, transparent); }
.circle-text__slot.is-pick em { color: color-mix(in srgb, var(--surface-light) 78%, transparent); }

/* 2. Seal: gradient rosette, stars and a ring of credentials */
.circle-text__seal {
  --circle-text-fs: 19.16px;
  --circle-text-sep: var(--primary);
  flex: none; display: block; width: clamp(6.5rem, 5.5rem + 2vw, 7.75rem); aspect-ratio: 1; border-radius: 50%; color: var(--text-main);
  transition: translate var(--dur-3) var(--ease-spring);
}
.circle-text__seal:hover { translate: 0 -2px; }
.circle-text__seal-art { display: block; width: 100%; height: 100%; overflow: visible; filter: drop-shadow(0 12px 16px color-mix(in srgb, var(--primary) 24%, transparent)); }
.circle-text__stop-a { stop-color: var(--primary); }
.circle-text__stop-b { stop-color: var(--primary-2); }
.circle-text__disc { fill: var(--surface-light); }
.circle-text__hairline { fill: none; stroke: color-mix(in srgb, var(--primary) 32%, transparent); stroke-width: 1.25; stroke-dasharray: 2 3; }
.circle-text__rosette, .circle-text__seal-ring { transform-origin: 100px 100px; transition: transform var(--dur-5) var(--ease-spring); }
.circle-text__star { fill: var(--accent); transform-box: fill-box; transform-origin: center; }
.circle-text__score { font: 600 46px var(--font-display); letter-spacing: -0.04em; text-anchor: middle; fill: var(--text-main); }
.circle-text__seal:is(:hover, :focus-visible) .circle-text__rosette { transform: rotate(24deg); }
.circle-text__seal:is(:hover, :focus-visible) .circle-text__seal-ring { transform: rotate(-16deg); }
.circle-text__seal:is(:hover, :focus-visible) .circle-text__star { animation: circle-text-pop var(--dur-4) var(--ease-spring) calc(var(--circle-text-i) * var(--stagger)) both; }

/* 3. Scroll badge: small, counter-rotating */
.circle-text__scroll {
  --circle-text-fs: 30.21px;
  --circle-text-dir: -1;
  --circle-text-sep: var(--primary);
  grid-area: scroll; justify-self: center; position: relative; display: grid; place-items: center;
  width: 5.75rem; aspect-ratio: 1; border-radius: 50%; color: var(--text-main); text-decoration: none;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-md);
}
.circle-text__hub {
  position: relative; display: grid; place-items: center; width: 38%; aspect-ratio: 1; border-radius: 50%;
  background: color-mix(in srgb, var(--primary) 9%, var(--surface-light)); color: var(--primary);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 22%, transparent);
}
.circle-text__down { width: 58%; height: auto; fill: none; stroke: currentColor; stroke-width: 2.25; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.circle-text__scroll:is(:hover, :focus-visible) .circle-text__down { translate: 0 18%; }

/* Demo scroll room */
.circle-text-demo__intro, .circle-text-demo__outro {
  display: grid; place-content: center; justify-items: center; gap: 0.75rem; min-height: 70vh; min-height: 70svh;
  padding: 3rem var(--gutter); background: var(--surface-muted); color: var(--text-muted); font-family: var(--font-sans); text-align: center;
}
.circle-text-demo__intro p, .circle-text-demo__outro p { max-width: 24rem; margin: 0; color: var(--text-main); font: 600 clamp(1.25rem, 1rem + 1vw, 1.75rem)/1.2 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.circle-text-demo__hint { font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }

@media (min-width: 768px) {
  .circle-text__art { aspect-ratio: 16 / 9; }
  .circle-text__slots { top: 1.5rem; right: 1.5rem; padding: 1rem; }
}
@media (min-width: 1024px) {
  .circle-text__inner {
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); grid-template-areas: "copy visual" "scroll visual";
    column-gap: clamp(3rem, 6vw, 6rem); row-gap: 2rem; align-items: start;
  }
  .circle-text__visual { --circle-text-cx: calc(var(--circle-text-cta) * 0.28); --circle-text-cy: calc(var(--circle-text-cta) * 0.28); margin-bottom: 0; }
  .circle-text__art { aspect-ratio: 1; }
  .circle-text__scroll { justify-self: start; align-self: end; }
}

@media (prefers-reduced-motion: reduce) {
  .circle-text *, .circle-text *::before, .circle-text *::after { animation: none !important; }
  .circle-text__seal:is(:hover, :focus-visible) :is(.circle-text__rosette, .circle-text__seal-ring) { transform: none; }
}

@keyframes circle-text-turn { to { rotate: calc(var(--circle-text-turns) * var(--circle-text-dir, 1) * 1turn); } }
@keyframes circle-text-pop { 40% { transform: scale(1.35); } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const native = CSS.supports('animation-timeline: scroll()');

document.querySelectorAll('[data-circle-text]').forEach((root) => {
  if (reduce.matches) return; // badges stay still

  // No scroll timelines (e.g. Firefox): mirror page scroll progress into --circle-text-p while near the viewport
  if (!native) {
    let frame = 0;
    let near = false;
    const write = () => {
      frame = 0;
      const max = document.documentElement.scrollHeight - innerHeight;
      root.style.setProperty('--circle-text-p', max > 0 ? (scrollY / max).toFixed(4) : '0');
    };
    const queue = () => { if (near && !frame) frame = requestAnimationFrame(write); };
    new IntersectionObserver(([entry]) => { near = entry.isIntersecting; if (near) write(); }, { rootMargin: '25% 0px' }).observe(root);
    addEventListener('scroll', queue, { passive: true });
    addEventListener('resize', queue, { passive: true });
  }

  // Hover: the CTA ring winds up to a fast spin, then coasts to a stop on leave (mouse only)
  root.querySelectorAll('.circle-text__cta').forEach((cta) => {
    const spin = cta.querySelector('.circle-text__spin');
    let angle = 0;
    let speed = 0;
    let target = 0;
    let frame = 0;
    let last = 0;
    const step = (now) => {
      const dt = Math.min(48, now - (last || now));
      last = now;
      speed += (target - speed) * (1 - Math.exp(-dt / 280));
      angle = (angle + speed * dt) % 360;
      spin.style.setProperty('--circle-text-spin', `${angle.toFixed(2)}deg`);
      if (target || speed > 0.001) frame = requestAnimationFrame(step);
      else frame = last = 0;
    };
    const boost = (on) => {
      target = on ? 0.14 : 0; // degrees per millisecond
      if (!frame) frame = requestAnimationFrame(step);
    };
    cta.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse') boost(true); });
    cta.addEventListener('pointerleave', () => boost(false));
  });
});
```

## Notes

- Each badge is a single link whose name comes from visually hidden text ("Book a visit, same-day service", "Rated 4.9 out of 5…", "Scroll to how it works"). The SVG rings, arrows and art card are `aria-hidden`, and focus shows a circular `--primary` outline that follows the badge.
- Seamless rings: the label is set in Geist Mono, and its font size is chosen so the natural length almost equals the circle's circumference (`2πr`). `textLength` with `lengthAdjust="spacing"` absorbs any font-metric drift, and a trailing no-break space keeps the gap at the seam identical to the others. To change the copy, keep the character count or recompute `font-size ≈ 2πr / (0.6 × characters)`.
- Scroll rotation uses `animation-timeline: scroll()` inside `@supports`. Elsewhere, a passive, rAF-throttled listener, gated by an IntersectionObserver, writes page progress to `--circle-text-p`. Tune the speed with `--circle-text-turns`, and the direction with `--circle-text-dir`.
- Without JS the badges are static links (the scroll rotation still runs where CSS supports it). Under reduced motion all rotation, the hover spin and the seal's wind-up are off, and the arrow swap is instant.
- Contrast: white ring text on `--surface-deep` is 18.8:1, ring text on the seal and scroll badges is 14.6:1, the gradient headline line runs 5.2:1 to 3.7:1 on white (large display text only), and the arrow on the brand gradient is 3.6:1 or better (non-text). On a page with several copies, suffix the three `circle-text-*-path` ids and the gradient id per copy.
