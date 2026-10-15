# Wireframe House

A deep, blueprint-toned layer for a builder's page: a 3D wireframe house on a turntable (walls, gable roof, chimney, door and windows), projected onto a canvas in true perspective, with far edges fading by depth and a stroke gradient read from the tokens at runtime. On first view the model draws itself in from the footprint up. Scrolling then turns it through one and a half rotations while it leans gently toward the cursor. It sits on the right on desktop, and moves top-right, smaller and fainter, on phones. Depends on `tokens/variables.css`.

**Motion:** one-shot draw-in with plotter tips (1.2s, cubic ease-out) · rotation scrubbed by scroll (1.5 turns, lerped) · cursor lean (lerped, mouse only) · the loop stops once settled · buttons and cards respond with `--ease-spring` over `--dur-3`.

## HTML

```html
<div class="amb-wire-demo">
  <div class="amb-wire" aria-hidden="true">
    <div class="amb-wire__frame">
      <div class="amb-wire__grid"></div>
      <div class="amb-wire__stage">
        <span class="amb-wire__glow"></span>
        <svg class="amb-wire__still" viewBox="0 0 400 400" focusable="false">
          <path class="amb-wire__edges amb-wire__edges--far" d="M155 230L341 287M59 289L155 230L153 128L103 75M194 205L258 224L259 179L194 161L194 205M225 214L226 170M194 183L259 201M46 282L51 273L59 264L69 256L80 248L93 241L107 235L123 230L139 226L157 223L174 222L192 221L211 221L229 222L246 224L263 227L280 231L295 236L309 242L322 249L333 257L342 265L350 274L354 284M80 248L66 243M139 226L136 223M211 221L211 217M280 231L289 225M333 257L341 255" />
          <path class="amb-wire__edges amb-wire__edges--mid" d="M341 287L255 360L59 289M153 128L347 176M53 178L153 128M341 287L347 176M59 289L53 178M103 75L309 122M53 178L103 75M347 176L309 122M274 143L297 149L283 130L259 124L274 143M276 69L300 74L284 82M260 77L276 69M274 143L276 69M297 149L300 74M283 130L284 82M259 124L260 77M177 331L176 254M79 257L122 272L120 223L77 210L79 257M100 264L98 217M78 234L121 248M317 269L286 293M288 244L319 221L317 269M302 281L304 232M318 245L287 269M114 129L96 137L95 116L113 108L114 129M338 334L326 343L312 352M85 350L71 342L60 333L52 323L46 313L43 302L44 292L46 282M354 284L357 294L356 304L353 314L347 324L338 334L357 340M52 323L42 325M46 282L37 282M357 294L366 294" />
          <path class="amb-wire__edges amb-wire__edges--near" d="M347 176L258 239L53 178M255 360L258 239L309 122M284 82L260 77M176 254L213 266L213 344M286 293L288 244M312 352L295 359L276 365L255 370L233 373L210 375L186 374L164 373L141 369L121 364L102 358L85 350M276 365L281 370M186 374L186 380M102 358L88 368" />
        </svg>
        <canvas class="amb-wire__canvas" width="400" height="400"></canvas>
      </div>
    </div>
  </div>

  <section class="amb-wire-demo__hero" aria-labelledby="amb-wire-title">
    <div class="amb-wire-demo__inner">
      <div class="amb-wire-demo__col">
        <p class="amb-wire-demo__eyebrow">Brand Builders · Springfield</p>
        <h2 id="amb-wire-title" class="amb-wire-demo__display">Built right, <span>from the frame up.</span></h2>
        <p class="amb-wire-demo__lead">Kitchens, additions and whole-home remodels, modelled in 3D and signed off by you before anyone lifts a hammer.</p>
        <div class="amb-wire-demo__actions">
          <a class="amb-wire-demo__btn amb-wire-demo__btn--primary" href="#amb-wire-visit">
            Book a design visit
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </a>
          <a class="amb-wire-demo__btn amb-wire-demo__btn--ghost" href="tel:+15555550123">
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
            (555) 555-0123
          </a>
        </div>
        <p class="amb-wire-demo__hint">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M21 12a9 9 0 1 1-2.6-6.4" /><path d="M21 3.5v5h-5" /></svg>
          Scroll to turn the model
        </p>
      </div>
    </div>
  </section>

  <section class="amb-wire-demo__section" aria-labelledby="amb-wire-services">
    <div class="amb-wire-demo__inner">
      <header class="amb-wire-demo__col">
        <p class="amb-wire-demo__eyebrow">What we build</p>
        <h2 id="amb-wire-services" class="amb-wire-demo__title">One crew, from footings to finish.</h2>
      </header>
      <ul class="amb-wire-demo__cards" role="list">
        <li class="amb-wire-demo__card">
          <span class="amb-wire-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><rect x="3" y="4" width="18" height="16" rx="2" /><path d="M3 10h18M7.5 7h.01M11 7h.01M14.5 15h3M7 13v4" /></svg></span>
          <h3><a href="#amb-wire-visit">Kitchen remodels</a></h3>
          <p>Layouts modelled in 3D, cabinets fitted to the millimetre.</p>
          <p class="amb-wire-demo__price">from <b>$18,500</b></p>
        </li>
        <li class="amb-wire-demo__card">
          <span class="amb-wire-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M3 11.5 12 4l9 7.5" /><path d="M5 10v10h14V10" /><path d="M12 11.5v5M9.5 14h5" /></svg></span>
          <h3><a href="#amb-wire-visit">Home additions</a></h3>
          <p>Bedrooms and sunrooms that match the house, with permits handled.</p>
          <p class="amb-wire-demo__price">from <b>$65,000</b></p>
        </li>
        <li class="amb-wire-demo__card">
          <span class="amb-wire-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M2 13 12 5l10 8" /><path d="M5 11v8h14v-8" /><path d="M16 7.4V4h2.5v5.4" /></svg></span>
          <h3><a href="#amb-wire-visit">Roof replacement</a></h3>
          <p>Tear-off to ridge cap in two days, with a 25-year warranty.</p>
          <p class="amb-wire-demo__price">from <b>$9,800</b></p>
        </li>
        <li class="amb-wire-demo__card">
          <span class="amb-wire-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M3 20h4.5v-4h4v-4h4V8H21" /><path d="M3 4h18" /></svg></span>
          <h3><a href="#amb-wire-visit">Basement finishing</a></h3>
          <p>Dry, warm living space with egress windows built to code.</p>
          <p class="amb-wire-demo__price">from <b>$24,000</b></p>
        </li>
      </ul>
    </div>
  </section>

  <section class="amb-wire-demo__section" aria-labelledby="amb-wire-process">
    <div class="amb-wire-demo__inner">
      <div class="amb-wire-demo__col">
        <p class="amb-wire-demo__eyebrow">How it works</p>
        <h2 id="amb-wire-process" class="amb-wire-demo__title">Modelled first. Built once.</h2>
        <ol class="amb-wire-demo__steps" role="list">
          <li><span class="amb-wire-demo__num">01</span><h3>Measure</h3><p>We laser-scan every room in about an hour, so the model matches the house you live in.</p></li>
          <li><span class="amb-wire-demo__num">02</span><h3>Model</h3><p>You walk through the plan in 3D and sign off on every wall, window and finish.</p></li>
          <li><span class="amb-wire-demo__num">03</span><h3>Build</h3><p>One crew from start to finish, with a photo update at the end of every day.</p></li>
        </ol>
        <dl class="amb-wire-demo__stats">
          <div><dt>homes built since 2004</dt><dd>1,400+</dd></div>
          <div><dt>average rating</dt><dd>4.9</dd></div>
          <div><dt>workmanship warranty</dt><dd>10 yr</dd></div>
        </dl>
      </div>
    </div>
  </section>

  <section class="amb-wire-demo__section amb-wire-demo__cta" id="amb-wire-visit" aria-labelledby="amb-wire-cta">
    <div class="amb-wire-demo__inner">
      <div class="amb-wire-demo__col">
        <p class="amb-wire-demo__eyebrow">Free design visit</p>
        <h2 id="amb-wire-cta" class="amb-wire-demo__display amb-wire-demo__display--sm">Let's draw up <span>your home.</span></h2>
        <p class="amb-wire-demo__lead">An hour with a designer in Westlake, Northside, Riverside or anywhere in Springfield. You keep the 3D model either way.</p>
        <div class="amb-wire-demo__actions">
          <a class="amb-wire-demo__btn amb-wire-demo__btn--primary" href="mailto:hello@example.com">
            Book a visit
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </a>
          <a class="amb-wire-demo__btn amb-wire-demo__btn--ghost" href="tel:+15555550123">Call (555) 555-0123</a>
        </div>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* Layer: behind its section by default, behind the whole page with --page */
.amb-wire {
  --amb-wire-ink-1: color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse)); /* stroke gradient start */
  --amb-wire-ink-2: color-mix(in srgb, var(--primary) 55%, var(--text-inverse));   /* stroke gradient end */
  --amb-wire-tip: var(--text-inverse);                                              /* plotter tips while drawing */
  position: absolute; inset: 0; z-index: -1; overflow: clip; pointer-events: none;
}
.amb-wire--page { position: fixed; }

/* A viewport-tall frame that sticks while its section scrolls past */
.amb-wire__frame { position: sticky; top: 0; height: 100vh; height: 100svh; max-height: 100%; overflow: hidden; }
.amb-wire__frame::after { /* contrast guard: a veil of the page colour, 0–1 */
  content: ""; position: absolute; inset: 0;
  background: var(--surface-deep); opacity: var(--amb-wire-scrim, 0);
}
.amb-wire__grid { /* faint blueprint grid around the model */
  position: absolute; inset: 0;
  background-image: linear-gradient(var(--border-inverse) 1px, transparent 1px), linear-gradient(90deg, var(--border-inverse) 1px, transparent 1px);
  background-size: 3rem 3rem;
  -webkit-mask-image: radial-gradient(ellipse 55% 45% at 85% 12%, black, transparent 75%);
  mask-image: radial-gradient(ellipse 55% 45% at 85% 12%, black, transparent 75%);
}

/* Phones: top-right, smaller and fainter. Desktop: the right-hand side, full strength. */
.amb-wire__stage { position: absolute; top: 0.5rem; right: -3.5rem; width: min(72vw, 20rem); aspect-ratio: 1; opacity: 0.6; }
.amb-wire__glow {
  position: absolute; inset: -14%;
  background:
    radial-gradient(closest-side at 50% 60%, color-mix(in srgb, var(--primary) 20%, transparent), transparent),
    radial-gradient(closest-side at 62% 34%, color-mix(in srgb, var(--primary-2) 12%, transparent), transparent);
}
/* Lines never exceed 50% opacity: the canvas draws near edges solid, and this caps them */
.amb-wire__still, .amb-wire__canvas { position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0.5; }
.amb-wire__edges { fill: none; stroke-width: 1.25; stroke-linecap: round; stroke-linejoin: round; vector-effect: non-scaling-stroke; }
.amb-wire__edges--near { stroke: var(--amb-wire-ink-1); }
.amb-wire__edges--mid { stroke: color-mix(in srgb, var(--amb-wire-ink-1) 50%, var(--amb-wire-ink-2)); opacity: 0.72; }
.amb-wire__edges--far { stroke: var(--amb-wire-ink-2); opacity: 0.4; }

/* The still shows without JS and under reduced motion; the live canvas replaces it */
.amb-wire:not(.is-live) .amb-wire__canvas, .amb-wire.is-live .amb-wire__still { display: none; }
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  /* JS will draw the model in, so hold the still back (it fades in after 2s if JS never runs) */
  .amb-wire:not(.is-live) .amb-wire__still { opacity: 0; animation: amb-wire-failsafe 0.4s 2s forwards; }
}
@keyframes amb-wire-failsafe { to { opacity: 0.5; } }

@media (min-width: 768px) {
  .amb-wire__stage {
    top: 50%; right: max(0rem, (100% - var(--container-max)) / 2); width: min(48vw, 38rem);
    translate: 0 -50%; opacity: 1;
  }
  .amb-wire__grid {
    -webkit-mask-image: radial-gradient(ellipse 40% 60% at 74% 50%, black, transparent 75%);
    mask-image: radial-gradient(ellipse 40% 60% at 74% 50%, black, transparent 75%);
  }
}

/* Demo page: a builder's landing page with the model behind it */
.amb-wire-demo {
  position: relative; isolation: isolate; color: var(--text-inverse); font-family: var(--font-sans);
  background:
    radial-gradient(50rem 36rem at 0% 0%, color-mix(in srgb, var(--primary) 16%, transparent), transparent 70%),
    var(--surface-deep);
}
.amb-wire-demo__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.amb-wire-demo__col { max-width: 36rem; }
.amb-wire-demo__hero { display: grid; align-items: end; min-height: 90vh; min-height: 90svh; padding-block: 12rem 4rem; }
.amb-wire-demo__section { padding-block: clamp(4rem, 9vw, 6.5rem); }
.amb-wire-demo__eyebrow {
  display: flex; align-items: center; gap: 0.625rem; margin: 0;
  font: 600 0.75rem/1.3 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.amb-wire-demo__eyebrow::before {
  content: ""; flex: none; width: 0.5rem; height: 0.5rem; border-radius: 2px; transform: rotate(45deg);
  background: var(--primary-2); box-shadow: 0 0 12px color-mix(in srgb, var(--primary-2) 70%, transparent);
}
.amb-wire-demo__display {
  margin: 1.25rem 0 0; font: 600 clamp(2.5rem, 1.3rem + 5vw, 5rem)/0.98 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-wire-demo__display span {
  background: linear-gradient(100deg, var(--text-inverse) 10%, color-mix(in srgb, var(--primary-2) 45%, var(--text-inverse)) 90%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.amb-wire-demo__display--sm { font-size: clamp(2.25rem, 1.4rem + 3.6vw, 3.75rem); }
.amb-wire-demo__lead { margin: 1.5rem 0 0; font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; }
.amb-wire-demo__title {
  margin: 0.875rem 0 0; font: 600 clamp(1.875rem, 1.2rem + 2.6vw, 3rem)/1.05 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}

/* Buttons */
.amb-wire-demo__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
.amb-wire-demo__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem;
  border-radius: var(--radius-full); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out), background-color var(--dur-2);
}
.amb-wire-demo__btn svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-wire-demo__btn:hover { transform: translateY(-2px); }
.amb-wire-demo__btn:active { transform: scale(0.97); }
.amb-wire-demo__btn--primary {
  background: var(--surface-light); color: var(--text-main);
  box-shadow: 0 12px 40px -12px color-mix(in srgb, var(--primary-2) 80%, transparent);
}
.amb-wire-demo__btn--ghost {
  background: color-mix(in srgb, var(--surface-deep) 70%, transparent); color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.amb-wire-demo__btn--ghost:hover { background: color-mix(in srgb, var(--text-inverse) 10%, var(--surface-deep)); }
.amb-wire-demo a:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.amb-wire-demo__hint {
  display: flex; align-items: center; gap: 0.5rem; margin: 3rem 0 0;
  font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.amb-wire-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* Service cards: near-opaque panels, so muted copy keeps 7:1 over the lines */
.amb-wire-demo__cards {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr)); gap: 1rem;
  max-width: 48rem; margin: 2.5rem 0 0; padding: 0; list-style: none;
}
.amb-wire-demo__card {
  position: relative; display: grid; align-content: start; gap: 0.5rem; padding: 1.5rem; border-radius: var(--radius-2xl);
  background: linear-gradient(var(--glass-inverse), var(--glass-inverse)), color-mix(in srgb, var(--surface-deep) 92%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 24px 48px -24px var(--surface-deep);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-wire-demo__card:hover {
  transform: translateY(-4px);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 45%, transparent), var(--highlight-inverse), 0 28px 56px -24px color-mix(in srgb, var(--primary-2) 35%, transparent);
}
.amb-wire-demo__card h3 { margin: 0.75rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-wire-demo__card h3 a { color: inherit; text-decoration: none; }
.amb-wire-demo__card h3 a::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-2xl); }
.amb-wire-demo__card h3 a:focus-visible { outline: none; }
.amb-wire-demo__card h3 a:focus-visible::after { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.amb-wire-demo__card p { margin: 0; color: var(--text-inverse-muted); line-height: 1.55; }
.amb-wire-demo__card .amb-wire-demo__price { margin-top: 0.75rem; color: var(--text-inverse); font: 500 0.8125rem var(--font-mono); }
.amb-wire-demo__price b { font-size: 1.125rem; font-weight: 600; }
.amb-wire-demo__icon {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: var(--radius-lg);
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 30%, transparent), color-mix(in srgb, var(--primary-2) 24%, transparent));
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.amb-wire-demo__icon svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }

/* Process steps and stats */
.amb-wire-demo__steps { display: grid; gap: 1.75rem; margin: 2.5rem 0 0; padding: 0; list-style: none; }
.amb-wire-demo__steps li { display: grid; grid-template-columns: 3rem 1fr; column-gap: 1rem; }
.amb-wire-demo__num {
  grid-row: span 2; display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: var(--radius-lg);
  box-shadow: inset 0 0 0 1px var(--border-inverse); font: 600 0.875rem var(--font-mono);
}
.amb-wire-demo__steps h3 { margin: 0.25rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-wire-demo__steps p { margin: 0.375rem 0 0; line-height: 1.6; }
.amb-wire-demo__stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; margin: 2.75rem 0 0; }
.amb-wire-demo__stats div { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.375rem; padding-top: 1rem; border-top: 1px solid var(--border-inverse); }
.amb-wire-demo__stats dt { font-size: 0.8125rem; line-height: 1.4; }
.amb-wire-demo__stats dd { margin: 0; font: 600 clamp(1.5rem, 1.2rem + 1.4vw, 2.25rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }

.amb-wire-demo__cta { padding-bottom: clamp(6rem, 16vh, 10rem); }

@media (min-width: 768px) {
  .amb-wire-demo__hero { align-items: center; padding-block: 5rem; }
  .amb-wire-demo__col { max-width: 34rem; }
}
```

## JS

```js
document.querySelectorAll('.amb-wire').forEach((layer) => {
  const page = layer.classList.contains('amb-wire--page'), host = page ? document.documentElement : layer.parentElement;
  const canvas = layer.querySelector('.amb-wire__canvas'), ctx = canvas.getContext('2d');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)'), coarse = matchMedia('(pointer: coarse)');
  if (!ctx || reduce.matches) return; // the SVG still stays: one static frame at the same angle

  // Model: a gable house on a turntable, as 3D edges [[x, y, z], [x, y, z]] (y up, front door at +z)
  const E = [];
  const poly = (pts, closed = true) => pts.forEach((p, i) => (closed || i < pts.length - 1) && E.push([p, pts[(i + 1) % pts.length]]));
  const win = (side, at, a0, a1, y0, y1, cross) => {
    const P = (a, y) => (side ? [at, y, a] : [a, y, at]);
    poly([P(a0, y0), P(a1, y0), P(a1, y1), P(a0, y1)]);
    if (cross) E.push([P((a0 + a1) / 2, y0), P((a0 + a1) / 2, y1)], [P(a0, (y0 + y1) / 2), P(a1, (y0 + y1) / 2)]);
  };
  const G = -0.8, T = 0.25, R = 0.95, box = [[-1, -0.7], [1, -0.7], [1, 0.7], [-1, 0.7]];
  const ch = [[0.44, -0.45], [0.66, -0.45], [0.66, -0.2], [0.44, -0.2]], arc = (a, r) => [r * Math.cos(a), G, r * Math.sin(a)];
  for (let i = 0; i < 48; i++) E.push([arc((i / 24) * Math.PI, 1.35), arc(((i + 1) / 24) * Math.PI, 1.35)]); // turntable
  for (let i = 0; i < 12; i++) E.push([arc((i / 6) * Math.PI, 1.35), arc((i / 6) * Math.PI, i % 3 ? 1.43 : 1.52)]);
  const base = E.length;
  poly(box.map(([x, z]) => [x, G, z])); poly(box.map(([x, z]) => [x, T, z])); // footprint, wall plate
  box.forEach(([x, z]) => E.push([[x, G, z], [x, T, z]]));
  E.push([[-1, R, 0], [1, R, 0]]); // ridge and gables
  [-1, 1].forEach((x) => E.push([[x, T, -0.7], [x, R, 0]], [[x, T, 0.7], [x, R, 0]]));
  poly(ch.map(([x, z]) => [x, R + z, z])); poly(ch.map(([x, z]) => [x, 1.15, z])); // chimney on the back slope
  ch.forEach(([x, z]) => E.push([[x, R + z, z], [x, 1.15, z]]));
  poly([[0.25, G, 0.7], [0.25, -0.1, 0.7], [0.6, -0.1, 0.7], [0.6, G, 0.7]], false); // door
  win(0, 0.7, -0.75, -0.3, -0.42, 0.02, true); win(1, 1, -0.25, 0.25, -0.42, 0.02, true);
  win(0, -0.7, -0.55, 0.15, -0.42, 0.02, true); win(1, -1, -0.12, 0.12, 0.42, 0.62, false);
  // Draw-in order: the turntable sweeps round, then the house rises from the footprint up
  const order = E.map(([a, b], i) => (i < base ? (i / base) * 0.3 : 0.3 + (0.7 * (Math.min(a[1], b[1]) - G)) / 1.95));

  // Camera 9.5 units away, over 3x the model's 3-unit span: near/far scale stays within 1.4x
  const D = 9.5, Y0 = -0.6, P0 = 0.42; // Y0/P0: the flattering three-quarter view the still uses
  let S = 0, f = 0, lw = 1, VH = 0, raf = 0, last = 0, t0 = 0, visible = page;
  let yaw = Y0, rev = 0, lx = 0, ly = 0, px = 0, py = 0;

  const draw = () => {
    const c = Math.cos(yaw + lx * 0.5), s = Math.sin(yaw + lx * 0.5), cp = Math.cos(P0 + ly * 0.16), sp = Math.sin(P0 + ly * 0.16);
    const pr = ([x, y, z]) => {
      const x1 = x * c + z * s, z1 = z * c - x * s, y1 = y - 0.15, d = D - z1 * cp - y1 * sp;
      return [S / 2 + (x1 * f) / d, S * 0.47 - ((y1 * cp - z1 * sp) * f) / d, d];
    };
    const bands = [[], [], [], []], tips = [], drawn = 1 - (1 - rev) ** 3;
    ctx.clearRect(0, 0, S, S);
    E.forEach(([a, b], i) => {
      const t = Math.min(1, Math.max(0, (drawn - order[i] * 0.75) / 0.25));
      if (!t) return;
      const A = pr(a), B = pr(b), end = [A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t];
      if (t < 1) tips.push(end);
      // Depth cueing: four bands from near (solid) to far (dim)
      bands[Math.min(3, Math.max(0, Math.floor(((A[2] + B[2]) / 2 - D + 1.55) / 0.78)))].push(A, end);
    });
    bands.forEach((seg, k) => {
      ctx.globalAlpha = 1 - k * 0.24;
      ctx.beginPath();
      for (let j = 0; j < seg.length; j += 2) { ctx.moveTo(seg[j][0], seg[j][1]); ctx.lineTo(seg[j + 1][0], seg[j + 1][1]); }
      ctx.stroke();
    });
    ctx.globalAlpha = 1;
    ctx.beginPath();
    tips.forEach(([x, y]) => { ctx.moveTo(x + lw * 1.6, y); ctx.arc(x, y, lw * 1.6, 0, 2 * Math.PI); });
    ctx.fill();
  };

  const tick = (now) => {
    raf = 0;
    const dt = Math.min(0.05, Math.max(0.001, (now - last) / 1000)), k = 1 - Math.exp(-dt * 6);
    const r = host.getBoundingClientRect(); // the one layout read per frame
    const target = Y0 + Math.min(1, Math.max(0, -r.top / Math.max(1, r.height - VH))) * 3 * Math.PI; // 1.5 turns
    last = now;
    if (!t0) { t0 = now; yaw = target; } // first view: start the draw-in at the current angle
    yaw += (target - yaw) * k; lx += (px - lx) * k; ly += (py - ly) * k;
    rev = Math.min(1, (now - t0) / 1200);
    draw();
    const moving = rev < 1 || Math.abs(target - yaw) > 1e-4 || Math.abs(px - lx) + Math.abs(py - ly) > 1e-3;
    if (moving && visible && document.visibilityState === 'visible') raf = requestAnimationFrame(tick);
  };
  const wake = () => {
    if (raf || !visible || document.visibilityState !== 'visible') return;
    last = performance.now();
    raf = requestAnimationFrame(tick);
  };

  // Size the backing store (DPR capped) and read the stroke colours from the tokens
  new ResizeObserver(() => {
    const dpr = Math.min(devicePixelRatio || 1, coarse.matches ? 1.5 : 2);
    const ink = (name) => { canvas.style.color = `var(${name})`; return getComputedStyle(canvas).color; };
    S = canvas.width = canvas.height = Math.round(canvas.clientWidth * dpr);
    f = 2.85 * S; lw = (coarse.matches ? 1 : 1.25) * dpr; VH = innerHeight;
    const g = ctx.createLinearGradient(0, 0, S, S);
    g.addColorStop(0, ink('--amb-wire-ink-1'));
    g.addColorStop(1, ink('--amb-wire-ink-2'));
    Object.assign(ctx, { strokeStyle: g, fillStyle: ink('--amb-wire-tip'), lineWidth: lw, lineCap: 'round' });
    draw();
  }).observe(canvas);

  addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    px = e.clientX / innerWidth - 0.5; py = e.clientY / innerHeight - 0.5; // lean toward the cursor
    wake();
  }, { passive: true });
  addEventListener('scroll', wake, { passive: true });
  document.addEventListener('visibilitychange', wake);
  layer.classList.add('is-live');
  if (page) wake();
  else new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; wake(); }).observe(host);
});
```

## Notes

- **Placement.** The layer is decorative (`aria-hidden`, `pointer-events: none`). By default it's the first child of a `position: relative; isolation: isolate` section, and a sticky, viewport-tall frame keeps the model in view while that section scrolls; the 1.5 turns map to the section's scroll range. Add `.amb-wire--page` to fix it behind the whole page instead, with the turns mapped to the document and every section's background left transparent. Use one ambient background per page. The cursor lean comes from `pointermove` on `window` (mouse only), so the layer never takes a click.
- **Contrast.** The stroke gradient comes from `--amb-wire-ink-1`/`-2` (55% `--primary-2`/`--primary` mixed into `--text-inverse`), resolved through `getComputedStyle` on every resize, so retheming the tokens retints the model. The canvas draws near edges solid, and the element's own `opacity: 0.5` caps every pixel, even where lines cross. Worst case in the demo: body copy in `--text-inverse` over the brightest line inside the glow is 5.26:1; on phones the stage drops to 60%, giving about 7:1. `--text-inverse-muted` would fall to 2.2:1 over a line, so it's used only on the near-opaque cards (7.0:1). Set `--amb-wire-scrim` (0–1) to lay a `--surface-deep` veil over the model.
- **Performance.** There are 114 edges with no particles. The camera sits at 9.5 units against a model span of about 3, so projected scale stays within 1.4× at any angle. The single rAF loop runs only while the section is on screen, the tab is visible, and the draw-in, scroll rotation or cursor lean is still settling (a 6/s lerp, so within about 1.5s); then it stops. Each frame takes one `getBoundingClientRect`, a clear, four depth-band strokes and the plotter tips. The backing store is capped at DPR 2 (1.5 on coarse pointers) and resized by a `ResizeObserver`. There's no blur: the glow is a pre-blurred radial gradient.
- **Reduced motion and no JS.** An inline SVG still of the same model, at the same three-quarter angle and in the same depth bands, shows instead of the canvas, with no draw-in, rotation or loop. With scripting on, the still is held back so it doesn't flash before the draw-in; a 2s CSS failsafe brings it back if JS never runs.
- **Adapting.** The model is a plain list of 3D edges built by `poly()` and `win()`, so a garage, porch or different roof is a few lines. Keep the camera distance at least 3× the model's span. `Y0`/`P0` set the resting angle; if you change them, regenerate the still's paths at the same angle.
