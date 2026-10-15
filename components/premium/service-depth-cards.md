# Layered Depth Service Cards

Four tall, Apple TV–style poster cards on a deep surface. Each is built from separate planes: a token-gradient backdrop, an illustrated mid-ground (pipes, power lines, sun and snowflake, a roof ridge under a dusk sky), a large foreground icon and a text plate. Under a mouse the card tilts up to 10° towards the pointer, the planes slide by different pixel amounts and a soft glare follows the cursor. On touch screens the planes drift apart and back together as each card travels through the viewport; the grid runs one column on phones (capped at 22rem), two from 600px and four from 1024px. Depends on `tokens/variables.css`.

**Motion:** pointer tilt and layer parallax eased in one rAF loop (stops when settled) · glare fade (`--dur-3`) · lift on hover or focus via `translate`/`scale` (`--dur-4`, `--ease-spring`) · scroll-linked layer separation on touch.

## HTML

```html
<section class="svc-depth" aria-labelledby="svc-depth-title" data-svc-depth>
  <div class="svc-depth__inner">
    <header class="svc-depth__head">
      <div>
        <p class="svc-depth__eyebrow">Our trades</p>
        <h2 id="svc-depth-title" class="svc-depth__title">Four trades. <span class="svc-depth__glow">One crew you can trust.</span></h2>
        <p class="svc-depth__intro">Every job goes to a licensed specialist, never a generalist, with upfront prices and a 12-month guarantee.</p>
      </div>
      <a class="svc-depth__all" href="#services">All 14 services <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
    </header>

    <ul class="svc-depth__grid" role="list">
      <li class="svc-depth__item">
        <div class="svc-depth__card" style="--svc-depth-a: var(--primary); --svc-depth-b: var(--primary-2)">
          <div class="svc-depth__layer svc-depth__back" aria-hidden="true"></div>
          <div class="svc-depth__layer svc-depth__mid" aria-hidden="true">
            <svg viewBox="0 0 240 336" preserveAspectRatio="xMidYMid slice" focusable="false">
              <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                <path d="M-20 34H164a34 34 0 0 1 34 34v290" stroke-width="22" opacity=".16" />
                <path d="M-20 30H164a38 38 0 0 1 38 38v290" stroke-width="2.5" opacity=".45" />
                <path d="M30 360V206a30 30 0 0 1 30-30h14" stroke-width="18" opacity=".14" />
                <path d="M26 360V206a34 34 0 0 1 34-34h14" stroke-width="2.5" opacity=".4" />
                <path d="M46 20v28M66 20v28M186 96h24M186 118h24M18 226h24" stroke-width="4" opacity=".45" />
                <circle cx="84" cy="176" r="12" stroke-width="3" opacity=".45" />
                <path d="M84 164v24M72 176h24" stroke-width="3" opacity=".45" />
                <path d="M198 196c3 4 5 7 5 9.5a5 5 0 0 1-10 0c0-2.5 2-5.5 5-9.5z" stroke-width="2.5" opacity=".5" />
              </g>
            </svg>
          </div>
          <div class="svc-depth__layer svc-depth__fore" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="88" height="88" focusable="false"><path d="M3.5 6.5v6.5M3.5 8H13a4 4 0 0 1 4 4v1h-3.5v-.5a1 1 0 0 0-1-1H3.5M9 8V5.5M6.5 5.5h5" /><path d="M15.25 14.6c.7.9 1.15 1.6 1.15 2.2a1.15 1.15 0 0 1-2.3 0c0-.6.45-1.3 1.15-2.2z" /></svg>
          </div>
          <div class="svc-depth__layer svc-depth__plate">
            <h3 class="svc-depth__name">Plumbing</h3>
            <p class="svc-depth__benefit">Leaks, clogs and heaters, fixed on the first visit.</p>
            <div class="svc-depth__row">
              <p class="svc-depth__price"><small>from</small> $89</p>
              <span class="svc-depth__cta" aria-hidden="true">Book plumbing <svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
            </div>
          </div>
          <span class="svc-depth__glare" aria-hidden="true"></span>
          <a class="svc-depth__link" href="#book-plumbing"><span class="svc-depth__sr">Book plumbing</span></a>
        </div>
      </li>

      <li class="svc-depth__item">
        <div class="svc-depth__card" style="--svc-depth-a: var(--accent); --svc-depth-b: var(--warning)">
          <div class="svc-depth__layer svc-depth__back" aria-hidden="true"></div>
          <div class="svc-depth__layer svc-depth__mid" aria-hidden="true">
            <svg viewBox="0 0 240 336" preserveAspectRatio="xMidYMid slice" focusable="false">
              <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                <path d="M40 34v320M200 18v320" stroke-width="7" opacity=".28" />
                <path d="M14 54h52M174 38h52M20 74h40M180 58h40" stroke-width="5" opacity=".32" />
                <path d="M-20 70Q-4 62 14 54M14 54Q94 112 174 38M66 54Q146 112 226 38M226 38Q244 32 262 42M20 74Q100 128 180 58" stroke-width="2.25" opacity=".55" />
                <circle cx="14" cy="54" r="4" opacity=".6" />
                <circle cx="66" cy="54" r="4" opacity=".6" />
                <circle cx="174" cy="38" r="4" opacity=".6" />
                <circle cx="226" cy="38" r="4" opacity=".6" />
                <rect x="190" y="96" width="20" height="26" rx="4" stroke-width="3" opacity=".4" />
              </g>
            </svg>
          </div>
          <div class="svc-depth__layer svc-depth__fore" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="88" height="88" focusable="false"><path d="M13 2.5 5.5 13.5H11l-1 8 7.5-11H12l1-8z" /></svg>
          </div>
          <div class="svc-depth__layer svc-depth__plate">
            <h3 class="svc-depth__name">Electrical</h3>
            <p class="svc-depth__benefit">Outlets, panels and EV chargers, to code.</p>
            <div class="svc-depth__row">
              <p class="svc-depth__price"><small>from</small> $99</p>
              <span class="svc-depth__cta" aria-hidden="true">Book electrical <svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
            </div>
          </div>
          <span class="svc-depth__glare" aria-hidden="true"></span>
          <a class="svc-depth__link" href="#book-electrical"><span class="svc-depth__sr">Book electrical</span></a>
        </div>
      </li>

      <li class="svc-depth__item">
        <div class="svc-depth__card svc-depth__card--split" style="--svc-depth-a: var(--danger); --svc-depth-b: var(--primary)">
          <div class="svc-depth__layer svc-depth__back" aria-hidden="true"></div>
          <div class="svc-depth__layer svc-depth__mid" aria-hidden="true">
            <svg viewBox="0 0 240 336" preserveAspectRatio="xMidYMid slice" focusable="false">
              <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" opacity=".6">
                <circle cx="48" cy="50" r="18" />
                <path d="M48 20v-8M48 80v8M18 50h-8M78 50h8M27 29l-6-6M69 71l6 6M69 29l6-6M27 71l-6 6" />
                <path d="M196 126v60M170 141l52 30M170 171l52-30M190 134l6 6 6-6M190 178l6-6 6 6M174 150l8-2-2-8M218 162l-8 2 2 8M218 150l-8-2 2-8M174 162l8 2-2 8" />
              </g>
            </svg>
          </div>
          <div class="svc-depth__layer svc-depth__fore" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="88" height="88" focusable="false"><circle cx="12" cy="12" r="9.5" /><path d="M11.4 10.6C9.6 9.4 9.4 5.6 12.3 4.6c2.3-.7 3.5 1.9 2.4 3.9-.6 1.1-1.5 1.8-2.4 2.3" /><path d="M11.4 10.6C9.6 9.4 9.4 5.6 12.3 4.6c2.3-.7 3.5 1.9 2.4 3.9-.6 1.1-1.5 1.8-2.4 2.3" transform="rotate(120 12 12)" /><path d="M11.4 10.6C9.6 9.4 9.4 5.6 12.3 4.6c2.3-.7 3.5 1.9 2.4 3.9-.6 1.1-1.5 1.8-2.4 2.3" transform="rotate(240 12 12)" /><circle cx="12" cy="12" r="1.5" /></svg>
          </div>
          <div class="svc-depth__layer svc-depth__plate">
            <h3 class="svc-depth__name">Heating &amp; cooling</h3>
            <p class="svc-depth__benefit">Tune-ups and installs for every season.</p>
            <div class="svc-depth__row">
              <p class="svc-depth__price"><small>from</small> $129</p>
              <span class="svc-depth__cta" aria-hidden="true">Book HVAC <svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
            </div>
          </div>
          <span class="svc-depth__glare" aria-hidden="true"></span>
          <a class="svc-depth__link" href="#book-hvac"><span class="svc-depth__sr">Book HVAC: heating and cooling</span></a>
        </div>
      </li>

      <li class="svc-depth__item">
        <div class="svc-depth__card" style="--svc-depth-a: color-mix(in srgb, var(--primary) 50%, var(--danger)); --svc-depth-b: color-mix(in srgb, var(--primary) 35%, var(--surface-deep))">
          <div class="svc-depth__layer svc-depth__back" aria-hidden="true"></div>
          <div class="svc-depth__layer svc-depth__mid" aria-hidden="true">
            <svg viewBox="0 0 240 336" preserveAspectRatio="xMidYMid slice" focusable="false">
              <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                <path d="M198 30a20 20 0 1 0 13 35 15.5 15.5 0 1 1-13-35z" stroke-width="3" opacity=".65" />
                <path d="M30 38h.01M66 20h.01M150 22h.01M24 104h.01M222 120h.01M118 14h.01" stroke-width="5" opacity=".7" />
                <path d="M-12 226 120 150l132 76" stroke-width="9" opacity=".4" />
                <path d="M60 196h120M28 214h184" stroke-width="3" opacity=".28" />
                <path d="M168 164v-34h20v45" stroke-width="5" opacity=".4" />
              </g>
            </svg>
          </div>
          <div class="svc-depth__layer svc-depth__fore" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="88" height="88" focusable="false"><path d="M5.5 14v6.5h13V14M10.5 20.5V17h3v3.5" /><path d="M2.5 14 6 10.5h12l3.5 3.5zM6 10.5 9 7.5h6l3 3M9 7.5 11 5.5h2l2 2" /></svg>
          </div>
          <div class="svc-depth__layer svc-depth__plate">
            <h3 class="svc-depth__name">Roofing</h3>
            <p class="svc-depth__benefit">Storm repairs with a 10-year warranty.</p>
            <div class="svc-depth__row">
              <p class="svc-depth__price"><small>from</small> $249</p>
              <span class="svc-depth__cta" aria-hidden="true">Book roofing <svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
            </div>
          </div>
          <span class="svc-depth__glare" aria-hidden="true"></span>
          <a class="svc-depth__link" href="#book-roofing"><span class="svc-depth__sr">Book roofing</span></a>
        </div>
      </li>
    </ul>
  </div>
</section>
```

## CSS

```css
/* Section: deep surface, two pools of pre-blurred light and a faint grid that fades out */
.svc-depth {
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(48rem 26rem at 0% 0%, color-mix(in srgb, var(--primary) 22%, transparent), transparent 70%),
    radial-gradient(44rem 26rem at 100% 100%, color-mix(in srgb, var(--primary-2) 16%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); font-family: var(--font-sans);
}
.svc-depth::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none; opacity: 0.6;
  background-image: linear-gradient(var(--border-inverse) 1px, transparent 1px), linear-gradient(90deg, var(--border-inverse) 1px, transparent 1px);
  background-size: 64px 64px;
  -webkit-mask-image: radial-gradient(ellipse 70% 55% at 50% 0%, black, transparent 75%);
  mask-image: radial-gradient(ellipse 70% 55% at 50% 0%, black, transparent 75%);
}
.svc-depth__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }

/* Heading with a secondary link */
.svc-depth__head { display: grid; gap: var(--space-lg); margin-bottom: clamp(2.5rem, 5vw, 3.5rem); }
@media (min-width: 768px) { .svc-depth__head { grid-template-columns: minmax(0, 1fr) auto; align-items: end; } }
.svc-depth__eyebrow { margin: 0; color: color-mix(in srgb, var(--accent) 70%, var(--text-inverse)); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.svc-depth__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.25rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.svc-depth__glow {
  background: linear-gradient(100deg, var(--text-inverse), color-mix(in srgb, var(--accent) 45%, var(--text-inverse)) 50%, color-mix(in srgb, var(--primary-2) 60%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.svc-depth__intro { max-width: 34rem; margin: 1rem 0 0; color: var(--text-inverse-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }
.svc-depth__all {
  justify-self: start; display: inline-flex; align-items: center; gap: var(--space-sm); min-height: 2.75rem; padding: 0 1.125rem; border-radius: var(--radius-full);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  color: var(--text-inverse); font-size: 0.9375rem; font-weight: 600; text-decoration: none; white-space: nowrap;
  transition: background-color var(--dur-2) var(--ease-out);
}
.svc-depth__all svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.svc-depth__all:hover { background: color-mix(in srgb, var(--text-inverse) 12%, transparent); }
.svc-depth__all:hover svg { transform: translateX(3px); }

/* Grid: 1 → 2 → 4 posters. Each item supplies the perspective; its own box never moves */
.svc-depth__grid { display: grid; gap: var(--space-lg); margin: 0; padding: 0; list-style: none; }
@media (min-width: 600px) { .svc-depth__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (min-width: 1024px) { .svc-depth__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1.25rem; } }
.svc-depth__item { width: 100%; max-width: 22rem; margin-inline: auto; perspective: 1000px; }

/* Card: tilts with --svc-depth-x / --svc-depth-y (-1…1); lift uses the separate translate/scale
   properties so it can transition while JS drives the tilt every frame. Max tilt 10°/6° plus a
   1.03 lift keeps the projected scale under 1.1. */
.svc-depth__card {
  --svc-depth-x: 0;
  --svc-depth-y: 0;
  position: relative; isolation: isolate; overflow: hidden; aspect-ratio: 5 / 7.4; border-radius: var(--radius-2xl);
  background: var(--svc-depth-b);
  box-shadow: 0 32px 64px -34px color-mix(in srgb, var(--svc-depth-a) 70%, transparent);
  transform: rotateX(calc(var(--svc-depth-y) * -6deg)) rotateY(calc(var(--svc-depth-x) * 10deg));
  transition: translate var(--dur-4) var(--ease-spring), scale var(--dur-4) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.svc-depth__card.is-live { translate: 0 -6px; scale: 1.03; box-shadow: 0 40px 80px -36px color-mix(in srgb, var(--svc-depth-a) 90%, transparent); }
.svc-depth__card::after { content: ""; position: absolute; inset: 0; z-index: 3; border-radius: inherit; pointer-events: none; box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }

/* Planes: each slides by its own pixel depth (negative = behind the card plane) */
.svc-depth__layer {
  position: absolute; inset: 0;
  transform: translate3d(calc(var(--svc-depth-x) * var(--svc-depth-z) * 1px), calc(var(--svc-depth-y) * var(--svc-depth-z) * 1px), 0);
}
.svc-depth__card.is-moving :is(.svc-depth__layer, .svc-depth__glare) { will-change: transform; }
.svc-depth__back {
  --svc-depth-z: -6; inset: -1rem;
  background:
    linear-gradient(180deg, transparent 45%, color-mix(in srgb, var(--surface-deep) 55%, transparent)),
    radial-gradient(80% 55% at 20% 6%, color-mix(in srgb, var(--text-inverse) 24%, transparent), transparent 70%),
    linear-gradient(165deg, var(--svc-depth-a), color-mix(in srgb, var(--svc-depth-a) 45%, var(--svc-depth-b)) 55%, color-mix(in srgb, var(--svc-depth-b) 70%, var(--surface-deep)));
}
.svc-depth__card--split .svc-depth__back {
  background:
    linear-gradient(180deg, transparent 45%, color-mix(in srgb, var(--surface-deep) 55%, transparent)),
    radial-gradient(80% 55% at 20% 6%, color-mix(in srgb, var(--text-inverse) 20%, transparent), transparent 70%),
    linear-gradient(112deg, var(--svc-depth-a), color-mix(in srgb, var(--svc-depth-a) 75%, var(--surface-deep)) 46%, color-mix(in srgb, var(--svc-depth-b) 75%, var(--surface-deep)) 54%, var(--svc-depth-b));
}
.svc-depth__mid { --svc-depth-z: 7; inset: -1rem; color: color-mix(in srgb, var(--text-inverse) 90%, var(--svc-depth-a)); }
.svc-depth__mid svg { display: block; width: 100%; height: 100%; overflow: visible; }
.svc-depth__fore { --svc-depth-z: 16; bottom: 42%; display: grid; place-items: center; color: var(--text-inverse); }
.svc-depth__fore svg {
  width: 36%; max-width: 6rem; height: auto; fill: none; stroke: currentColor; stroke-width: 1.25; stroke-linecap: round; stroke-linejoin: round;
  filter: drop-shadow(0 10px 8px color-mix(in srgb, var(--surface-deep) 45%, transparent));
}
.svc-depth__glare {
  position: absolute; inset: -50%; z-index: 1; pointer-events: none; opacity: 0;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--text-inverse) 28%, transparent), transparent 72%);
  transform: translate3d(calc(var(--svc-depth-x) * 25%), calc(var(--svc-depth-y) * 25%), 0);
  transition: opacity var(--dur-3) var(--ease-out);
}
.svc-depth__card.is-live .svc-depth__glare { opacity: 1; }

/* Text plate: the nearest solid plane, above the glare so its text never washes out */
.svc-depth__plate {
  --svc-depth-z: 8; z-index: 2; inset: auto 0.75rem 0.75rem; padding: var(--space-md) 1.125rem 1.125rem; border-radius: var(--radius-xl);
  background: color-mix(in srgb, var(--surface-deep) 80%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 18px 36px -18px color-mix(in srgb, var(--surface-deep) 90%, transparent);
}
.svc-depth__name { margin: 0; font: 600 1.375rem/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.svc-depth__benefit { margin: 0.375rem 0 0; color: var(--text-inverse-muted); font-size: 0.875rem; line-height: 1.5; }
.svc-depth__row { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--space-sm) 0.75rem; margin-top: 0.875rem; padding-top: 0.875rem; border-top: 1px solid var(--border-inverse); }
.svc-depth__price { margin: 0; font: 600 1.25rem/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }
.svc-depth__price small { margin-right: 0.125rem; color: var(--text-inverse-muted); font: 500 0.6875rem var(--font-mono); letter-spacing: 0; }
.svc-depth__cta {
  display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.25rem; padding: 0 0.875rem; border-radius: var(--radius-full);
  background: var(--text-inverse); color: var(--surface-deep); font-size: 0.8125rem; font-weight: 600; white-space: nowrap;
}
.svc-depth__cta svg { fill: none; stroke: currentColor; stroke-width: 2.25; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.svc-depth__card:hover .svc-depth__cta svg { transform: translateX(3px); }

/* One invisible link covers the poster; the visible "Book …" pill is its label */
.svc-depth__link { position: absolute; inset: 0; z-index: 4; border-radius: inherit; }
.svc-depth__link:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: -5px; }
@supports selector(:has(*)) {
  .svc-depth__link:focus-visible { outline-color: transparent; }
  .svc-depth__card:has(.svc-depth__link:focus-visible) { outline: 2px solid var(--text-inverse); outline-offset: 3px; translate: 0 -6px; scale: 1.03; }
}
.svc-depth__all:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.svc-depth__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Reduced motion: flat and still (JS also stops driving the tilt) */
@media (prefers-reduced-motion: reduce) {
  .svc-depth__card, .svc-depth__layer, .svc-depth__glare { transform: none; }
}
```

## JS

```js
// Layered Depth Service Cards: pointer tilt with parallax planes and a moving glare; on touch, the planes
// separate with each card's scroll progress. One rAF loop that runs only while visible and still moving.
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const fine = matchMedia('(hover: hover) and (pointer: fine)');

document.querySelectorAll('[data-svc-depth]').forEach((root) => {
  const grid = root.querySelector('.svc-depth__grid');
  const cards = [...root.querySelectorAll('.svc-depth__card')].map((el) => ({ el, x: 0, y: 0, tx: 0, ty: 0, top: 0, h: 0, rect: null, out: '' }));
  let raf = 0;
  let visible = false;

  // Card positions come from the untransformed list items and are re-read only on resize
  const measure = () => {
    const g = grid.getBoundingClientRect();
    cards.forEach((c) => {
      const r = c.el.parentElement.getBoundingClientRect();
      c.top = r.top - g.top;
      c.h = r.height;
    });
  };

  const tick = () => {
    raf = 0;
    if (!visible || document.hidden || reduce.matches) return;
    if (!fine.matches) {
      const g = grid.getBoundingClientRect(); // the one layout read per frame
      cards.forEach((c) => {
        const offset = g.top + c.top + c.h / 2 - innerHeight / 2;
        c.ty = 0.7 * Math.max(-1, Math.min(1, offset / (innerHeight / 2 + c.h / 2)));
      });
    }
    let moving = false;
    cards.forEach((c) => {
      c.x += (c.tx - c.x) * 0.12;
      c.y += (c.ty - c.y) * 0.12;
      const settled = Math.abs(c.tx - c.x) < 0.002 && Math.abs(c.ty - c.y) < 0.002;
      if (settled) [c.x, c.y] = [c.tx, c.ty];
      else moving = true;
      c.el.classList.toggle('is-moving', !settled);
      const out = `${c.x.toFixed(3)} ${c.y.toFixed(3)}`;
      if (out === c.out) return;
      c.out = out;
      c.el.style.setProperty('--svc-depth-x', c.x.toFixed(3));
      c.el.style.setProperty('--svc-depth-y', c.y.toFixed(3));
    });
    if (moving) raf = requestAnimationFrame(tick);
  };
  const kick = () => {
    if (!raf && visible && !document.hidden && !reduce.matches) raf = requestAnimationFrame(tick);
  };

  // Mouse and pen: tilt towards the pointer, using the rect cached on entry (no reads while moving)
  cards.forEach((c) => {
    c.el.addEventListener('pointerenter', (e) => {
      if (e.pointerType === 'touch' || !fine.matches || reduce.matches) return;
      c.rect = c.el.getBoundingClientRect();
      c.el.classList.add('is-live');
    });
    c.el.addEventListener('pointermove', (e) => {
      if (!c.rect) return;
      c.tx = Math.max(-1, Math.min(1, ((e.clientX - c.rect.left) / c.rect.width) * 2 - 1));
      c.ty = Math.max(-1, Math.min(1, ((e.clientY - c.rect.top) / c.rect.height) * 2 - 1));
      kick();
    }, { passive: true });
    c.el.addEventListener('pointerleave', () => {
      c.rect = null;
      [c.tx, c.ty] = [0, 0];
      c.el.classList.remove('is-live');
      kick();
    });
  });

  // Snap flat when the input type or the motion preference changes
  const reset = () => cards.forEach((c) => {
    Object.assign(c, { x: 0, y: 0, tx: 0, ty: 0, rect: null, out: '' });
    c.el.classList.remove('is-live', 'is-moving');
    c.el.style.removeProperty('--svc-depth-x');
    c.el.style.removeProperty('--svc-depth-y');
  });
  [fine, reduce].forEach((query) => query.addEventListener('change', () => { reset(); kick(); }));

  addEventListener('scroll', () => { if (!fine.matches) kick(); }, { passive: true });
  document.addEventListener('visibilitychange', kick);
  new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; kick(); }).observe(root);
  new ResizeObserver(() => { measure(); kick(); }).observe(grid);
});
```

## Notes

- Each poster is one link. An invisible `<a>` ("Book plumbing") covers the card above every plane, and the visible "Book plumbing" pill is its label (`aria-hidden`, so it isn't read twice). Planes, illustrations and the glare are `aria-hidden`; the name, benefit and price stay in reading order. `:focus-visible` lifts the card and draws a 2px ring outside it through `:has()`; engines without `:has()` get an inset ring on the link.
- Performance budget: under a 1000px perspective the tilt is capped at 10° (Y) and 6° (X), which with the 1.03 lift keeps projected scale at about 1.09 or less. Planes move only by `translate3d` pixel offsets (−6 to +16px), never `translateZ`. One rAF loop per section eases toward its targets and stops once everything settles. It runs only while the section is on screen and the tab is visible, and `will-change` is set only on cards that are moving. With a mouse the loop reads no layout; on touch it reads one grid rect per frame.
- On touch and no-hover devices the planes drift apart as a card moves away from the middle of the viewport and lie flat when it is centred (passive scroll → rAF, gated by IntersectionObserver).
- Without JS, or under reduced motion, the posters are flat and still: the variables stay at 0 and the reduced-motion block also zeroes transforms. Lift on focus remains (instant under reduced motion).
- Contrast: plate text sits on an 80% `--surface-deep` plate. Over the brightest backdrop (amber) that is at least 11:1 for `--text-inverse` and 5.5:1 for `--text-inverse-muted`. The glare sits beneath the plate, so it never lowers text contrast.
- Retheme each card with `--svc-depth-a` / `--svc-depth-b` (tokens or `color-mix()`); `svc-depth__card--split` gives a hard warm/cool split. Swap the mid-ground SVG (240×336 viewBox) and the 24×24 foreground icon per trade.
