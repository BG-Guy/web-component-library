# Shape Morph

One large, soft glass shape (about 60vmin) floats behind a light page and turns into whatever the reader is on. Sections declare a shape with `data-amb-morph-shape` (`house`, `drop`, `bolt`, `flame` or `leaf`). When one crosses the middle of the viewport, the shape morphs into it over about 700ms with a spring overshoot while its gradient recolours, and scrolling nudges its rotation and scale. It sits to the right of the copy on desktop, and near the top of the screen on phones, where it stays visible above the card being read. Depends on `tokens/variables.css`.

**Motion:** path morph on a JS spring (stiffness 170, damping 16, about 700ms with a slight overshoot) · gradient recolour through registered colours (`calc(var(--dur-4) * 1.25)`, `--ease-out`) · scroll turn and speed tilt/swell (lerped, settles in about 1s) · cards lift with `--ease-spring`.

## HTML

```html
<div class="amb-morph-demo">
  <div class="amb-morph" data-amb-morph-current="house" aria-hidden="true">
    <div class="amb-morph__frame">
      <div class="amb-morph__float">
        <span class="amb-morph__glow"></span>
        <svg class="amb-morph__svg" viewBox="0 0 200 200" focusable="false">
          <defs>
            <linearGradient id="amb-morph-fill" x1="0.15" y1="0" x2="0.85" y2="1">
              <stop class="amb-morph__stop-a" offset="0" /><stop class="amb-morph__stop-b" offset="1" />
            </linearGradient>
            <linearGradient id="amb-morph-rim" x1="0" y1="0" x2="1" y2="1">
              <stop class="amb-morph__rim-a" offset="0" /><stop class="amb-morph__rim-b" offset="0.5" /><stop class="amb-morph__rim-c" offset="1" />
            </linearGradient>
            <radialGradient id="amb-morph-shine" cx="0.34" cy="0.24" r="0.48">
              <stop class="amb-morph__rim-a" offset="0" /><stop class="amb-morph__rim-b" offset="1" />
            </radialGradient>
            <clipPath id="amb-morph-clip">
              <path class="amb-morph__path" d="M100 22C103.6 22 124 43.7 136 55C148 66.3 170.5 84.2 172 90C173.5 95.8 169.6 167.8 166 172C162.4 176.2 122 174 100 174C78 174 37.6 176.2 34 172C30.4 167.8 26.5 95.8 28 90C29.5 84.2 52 66.3 64 55C76 43.7 96.4 22 100 22Z" />
            </clipPath>
            <!-- The five shapes: identical command structure (M + 8 C), 50 numbers each -->
            <path data-amb-morph-def="house" d="M100 22C103.6 22 124 43.7 136 55C148 66.3 170.5 84.2 172 90C173.5 95.8 169.6 167.8 166 172C162.4 176.2 122 174 100 174C78 174 37.6 176.2 34 172C30.4 167.8 26.5 95.8 28 90C29.5 84.2 52 66.3 64 55C76 43.7 96.4 22 100 22Z" />
            <path data-amb-morph-def="drop" d="M100 16C100 16 121.7 44.7 131 60C140.3 75.3 153.8 92 156 108C158.2 124 153.3 144 144 156C134.7 168 114.7 180 100 180C85.3 180 65.3 168 56 156C46.7 144 41.8 124 44 108C46.2 92 59.7 75.3 69 60C78.3 44.7 100 16 100 16Z" />
            <path data-amb-morph-def="bolt" d="M132 12C132.4 11.8 124.7 36 121 48C117.3 60 109.5 83.4 110 84C110.5 84.6 150.6 82.2 150 84C149.4 85.8 74.8 189.6 74 190C73.2 190.4 100.2 111.3 100 110C99.8 108.7 60.1 110.8 60 110C59.9 109.2 84 77.3 96 61C108 44.7 131.6 12.2 132 12Z" />
            <path data-amb-morph-def="flame" d="M118 8C118 8 129.3 34 136 50C142.7 66 156 86 158 104C160 122 157.7 144.3 148 158C138.3 171.7 115.7 185.3 100 186C84.3 186.7 63.7 174.3 54 162C44.3 149.7 40.7 129.3 42 112C43.3 94.7 62 58 62 58C76 84 104 52 118 8Z" />
            <path data-amb-morph-def="leaf" d="M164.2 28.7C164.2 28.7 171.7 54.2 166.5 71C161.2 87.8 145.9 115.3 132.7 129.4C119.5 143.6 103.3 149.6 87.4 155.9C71.4 162.2 37 167 37 167C37 167 36.1 133.6 42.8 115.7C49.4 97.9 63.7 74.1 76.7 60.2C89.6 46.3 105.9 37.6 120.5 32.4C135.1 27.1 164.2 28.7 164.2 28.7Z" />
          </defs>
          <path class="amb-morph__path amb-morph__body" fill="url(#amb-morph-fill)" d="M100 22C103.6 22 124 43.7 136 55C148 66.3 170.5 84.2 172 90C173.5 95.8 169.6 167.8 166 172C162.4 176.2 122 174 100 174C78 174 37.6 176.2 34 172C30.4 167.8 26.5 95.8 28 90C29.5 84.2 52 66.3 64 55C76 43.7 96.4 22 100 22Z" />
          <rect class="amb-morph__shine" width="200" height="200" fill="url(#amb-morph-shine)" clip-path="url(#amb-morph-clip)" />
          <path class="amb-morph__path amb-morph__rim" stroke="url(#amb-morph-rim)" d="M100 22C103.6 22 124 43.7 136 55C148 66.3 170.5 84.2 172 90C173.5 95.8 169.6 167.8 166 172C162.4 176.2 122 174 100 174C78 174 37.6 176.2 34 172C30.4 167.8 26.5 95.8 28 90C29.5 84.2 52 66.3 64 55C76 43.7 96.4 22 100 22Z" />
        </svg>
      </div>
    </div>
  </div>

  <section class="amb-morph-demo__hero" aria-labelledby="amb-morph-title" data-amb-morph-shape="house">
    <div class="amb-morph-demo__inner">
      <p class="amb-morph-demo__eyebrow">Brand Home Services · Springfield</p>
      <h2 id="amb-morph-title" class="amb-morph-demo__display">One call for <span>the whole house.</span></h2>
      <p class="amb-morph-demo__lead">Plumbers, electricians, heating engineers and gardeners on one team, with one booking and one bill.</p>
      <div class="amb-morph-demo__actions">
        <a class="amb-morph-demo__btn amb-morph-demo__btn--primary" href="#amb-morph-book">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-morph-demo__btn amb-morph-demo__btn--ghost" href="tel:+15555550123">(555) 555-0123</a>
      </div>
      <p class="amb-morph-demo__hint">Scroll: the shape follows the trade</p>
    </div>
  </section>

  <section class="amb-morph-demo__section" aria-labelledby="amb-morph-services">
    <div class="amb-morph-demo__inner">
      <header class="amb-morph-demo__head">
        <p class="amb-morph-demo__eyebrow">Four trades, one crew</p>
        <h2 id="amb-morph-services" class="amb-morph-demo__title">Whatever broke, someone on the team fixes it.</h2>
      </header>
      <ol class="amb-morph-demo__trades" role="list">
        <li class="amb-morph-demo__trade" data-amb-morph-shape="drop">
          <span class="amb-morph-demo__num">01</span>
          <h3><a href="#amb-morph-book">Plumbing</a></h3>
          <p>Leaks, blocked drains and water heaters, fixed at a flat price agreed before we start.</p>
          <p class="amb-morph-demo__price">from <b>$149</b></p>
        </li>
        <li class="amb-morph-demo__trade" data-amb-morph-shape="bolt">
          <span class="amb-morph-demo__num">02</span>
          <h3><a href="#amb-morph-book">Electrical</a></h3>
          <p>Panel upgrades, EV chargers and safety checks by licensed electricians.</p>
          <p class="amb-morph-demo__price">from <b>$129</b></p>
        </li>
        <li class="amb-morph-demo__trade" data-amb-morph-shape="flame">
          <span class="amb-morph-demo__num">03</span>
          <h3><a href="#amb-morph-book">Heating &amp; cooling</a></h3>
          <p>Furnace tune-ups, heat pumps and same-day no-heat callouts all winter.</p>
          <p class="amb-morph-demo__price">from <b>$89</b></p>
        </li>
        <li class="amb-morph-demo__trade" data-amb-morph-shape="leaf">
          <span class="amb-morph-demo__num">04</span>
          <h3><a href="#amb-morph-book">Gardens &amp; gutters</a></h3>
          <p>Gutter clearing, hedge trimming and seasonal yard clean-ups.</p>
          <p class="amb-morph-demo__price">from <b>$119</b></p>
        </li>
      </ol>
    </div>
  </section>

  <section class="amb-morph-demo__section" aria-labelledby="amb-morph-proof" data-amb-morph-shape="house">
    <div class="amb-morph-demo__inner">
      <div class="amb-morph-demo__head">
        <p class="amb-morph-demo__eyebrow">Why one team</p>
        <h2 id="amb-morph-proof" class="amb-morph-demo__title">No more juggling four contractors.</h2>
      </div>
      <dl class="amb-morph-demo__stats">
        <div><dt>average rating, 2,100+ reviews</dt><dd>4.9</dd></div>
        <div><dt>jobs finished on the first visit</dt><dd>92%</dd></div>
        <div><dt>invoice for every trade</dt><dd>1</dd></div>
      </dl>
      <figure class="amb-morph-demo__quote">
        <blockquote><p>"The electrician spotted a slow leak behind the panel and had the plumber there the same afternoon. That's the whole point."</p></blockquote>
        <figcaption><strong>Priya S.</strong> · Westlake</figcaption>
      </figure>
    </div>
  </section>

  <section class="amb-morph-demo__section amb-morph-demo__cta" id="amb-morph-book" aria-labelledby="amb-morph-cta">
    <div class="amb-morph-demo__inner">
      <h2 id="amb-morph-cta" class="amb-morph-demo__display amb-morph-demo__display--sm">Tell us what's wrong. <span>We'll send the right trade.</span></h2>
      <div class="amb-morph-demo__actions">
        <a class="amb-morph-demo__btn amb-morph-demo__btn--primary" href="mailto:hello@example.com">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-morph-demo__btn amb-morph-demo__btn--ghost" href="tel:+15555550123">Call (555) 555-0123</a>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* Registered colours, so the gradient and glow recolour smoothly between shapes */
@property --amb-morph-a { syntax: "<color>"; inherits: true; initial-value: transparent; }
@property --amb-morph-b { syntax: "<color>"; inherits: true; initial-value: transparent; }

/* Layer: behind its section by default, behind the whole page with --page */
.amb-morph {
  --amb-morph-a: var(--primary);
  --amb-morph-b: var(--primary-2);
  position: absolute; inset: 0; z-index: -1; overflow: clip; pointer-events: none;
  transition: --amb-morph-a calc(var(--dur-4) * 1.25) var(--ease-out), --amb-morph-b calc(var(--dur-4) * 1.25) var(--ease-out);
}
.amb-morph[data-amb-morph-current="drop"] { --amb-morph-a: color-mix(in srgb, var(--primary-2) 60%, var(--primary)); --amb-morph-b: var(--primary); }
.amb-morph[data-amb-morph-current="bolt"] { --amb-morph-a: var(--accent); --amb-morph-b: color-mix(in srgb, var(--accent) 55%, var(--danger)); }
.amb-morph[data-amb-morph-current="flame"] { --amb-morph-a: color-mix(in srgb, var(--accent) 70%, var(--danger)); --amb-morph-b: var(--danger); }
.amb-morph[data-amb-morph-current="leaf"] { --amb-morph-a: color-mix(in srgb, var(--success) 55%, var(--primary-2)); --amb-morph-b: var(--success); }
.amb-morph--page { position: fixed; }

/* A viewport-tall frame that sticks while its section scrolls past */
.amb-morph__frame { position: sticky; top: 0; height: 100vh; height: 100svh; max-height: 100%; overflow: hidden; }
.amb-morph__frame::after { /* contrast guard: a veil of the page colour, 0–1 */
  content: ""; position: absolute; inset: 0;
  background: var(--surface-light); opacity: var(--amb-morph-scrim, 0);
}

/* The glass shape: tinted body, clipped specular shine, light-to-tint rim, soft coloured glow */
.amb-morph__float { position: absolute; left: 50%; top: 22%; width: 60vmin; aspect-ratio: 1; margin: -30vmin 0 0 -30vmin; }
.amb-morph.is-moving .amb-morph__float { will-change: transform; }
.amb-morph__glow {
  position: absolute; inset: 10% -8% -16%;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--amb-morph-b) 24%, transparent), transparent);
}
.amb-morph__svg { position: absolute; inset: 0; width: 100%; height: 100%; overflow: visible; }
.amb-morph__body { fill-opacity: 0.4; }
.amb-morph__rim { fill: none; stroke-width: 1.5; stroke-linejoin: round; vector-effect: non-scaling-stroke; }
.amb-morph__stop-a { stop-color: var(--amb-morph-a); }
.amb-morph__stop-b { stop-color: var(--amb-morph-b); }
.amb-morph__rim-a { stop-color: var(--surface-light); stop-opacity: 0.95; }
.amb-morph__rim-b { stop-color: var(--surface-light); stop-opacity: 0; }
.amb-morph__rim-c { stop-color: var(--amb-morph-b); stop-opacity: 0.55; }
.amb-morph__shine { opacity: 0.8; }

@media (min-width: 768px) {
  .amb-morph__float { left: 70%; top: 50%; }
}

/* Demo page: a multi-trade landing page with the glass shape behind it */
.amb-morph-demo {
  position: relative; isolation: isolate; color: var(--text-main); font-family: var(--font-sans);
  background: linear-gradient(var(--surface-muted), var(--surface-light) 44rem);
}
.amb-morph-demo__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.amb-morph-demo__hero { display: grid; align-items: end; min-height: 92vh; min-height: 92svh; padding-block: 4rem; }
.amb-morph-demo__section { padding-block: clamp(4rem, 9vw, 6.5rem); }
.amb-morph-demo__eyebrow {
  display: flex; align-items: center; gap: 0.625rem; margin: 0;
  font: 600 0.75rem/1.3 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.amb-morph-demo__eyebrow::before { content: ""; flex: none; width: 0.625rem; height: 0.625rem; border-radius: 50%; background: var(--gradient-brand); }
.amb-morph-demo__display {
  max-width: 13ch; margin: 1.25rem 0 0; font: 600 clamp(2.5rem, 1.3rem + 5vw, 5rem)/0.98 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-morph-demo__display span { color: color-mix(in srgb, var(--text-main) 78%, var(--primary)); }
.amb-morph-demo__display--sm { max-width: 18ch; font-size: clamp(2.25rem, 1.4rem + 3.6vw, 3.75rem); }
.amb-morph-demo__lead { max-width: 32rem; margin: 1.5rem 0 0; font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; }
.amb-morph-demo__title {
  margin: 0.875rem 0 0; font: 600 clamp(1.875rem, 1.2rem + 2.6vw, 3rem)/1.05 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-morph-demo__head { max-width: 34rem; }
.amb-morph-demo__hint { margin: 2.5rem 0 0; font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.amb-morph-demo a:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Buttons */
.amb-morph-demo__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
.amb-morph-demo__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem;
  border-radius: var(--radius-full); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-morph-demo__btn svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-morph-demo__btn:hover { transform: translateY(-2px); }
.amb-morph-demo__btn:active { transform: scale(0.97); }
.amb-morph-demo__btn--primary { background: var(--text-main); color: var(--surface-light); box-shadow: var(--highlight-inverse), var(--shadow-lg); }
.amb-morph-demo__btn--ghost { background: var(--surface-light); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm); }

/* Trades: each card is a trigger, tall enough for its shape to settle */
.amb-morph-demo__trades { display: grid; gap: 1.25rem; max-width: 34rem; margin: 2.5rem 0 0; padding: 0; list-style: none; }
.amb-morph-demo__trade {
  position: relative; display: grid; align-content: center; gap: 0.5rem; min-height: 36vh; min-height: 36svh; padding: 1.75rem;
  border-radius: var(--radius-2xl); background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-lg);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-morph-demo__trade:hover { transform: translateY(-4px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl); }
.amb-morph-demo__num { color: var(--text-muted); font: 600 0.8125rem var(--font-mono); }
.amb-morph-demo__trade h3 { margin: 0; font: 600 clamp(1.5rem, 1.2rem + 1.2vw, 2rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-morph-demo__trade h3 a { color: inherit; text-decoration: none; }
.amb-morph-demo__trade h3 a::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-2xl); }
.amb-morph-demo__trade h3 a:focus-visible { outline: none; }
.amb-morph-demo__trade h3 a:focus-visible::after { outline: 2px solid var(--primary); outline-offset: 3px; }
.amb-morph-demo__trade p { margin: 0; color: var(--text-muted); line-height: 1.6; }
.amb-morph-demo__trade .amb-morph-demo__price { margin-top: 0.5rem; color: var(--text-main); font: 500 0.8125rem var(--font-mono); }
.amb-morph-demo__price b { font-size: 1.125rem; font-weight: 600; }

/* Proof */
.amb-morph-demo__stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; max-width: 34rem; margin: 2rem 0 0; }
.amb-morph-demo__stats div { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.375rem; padding-top: 1rem; border-top: 1px solid color-mix(in srgb, var(--text-main) 16%, transparent); }
.amb-morph-demo__stats dt { font-size: 0.8125rem; line-height: 1.4; }
.amb-morph-demo__stats dd { margin: 0; font: 600 clamp(1.5rem, 1.2rem + 1.4vw, 2.25rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-morph-demo__quote {
  max-width: 34rem; margin: 2.5rem 0 0; padding: 1.75rem; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.amb-morph-demo__quote blockquote { margin: 0; }
.amb-morph-demo__quote blockquote p { margin: 0; font: 500 clamp(1.125rem, 1rem + 0.6vw, 1.375rem)/1.45 var(--font-display); letter-spacing: -0.01em; }
.amb-morph-demo__quote figcaption { margin-top: 1.25rem; color: var(--text-muted); font-size: 0.875rem; }
.amb-morph-demo__quote strong { color: var(--text-main); }
.amb-morph-demo__cta { padding-bottom: clamp(6rem, 18vh, 10rem); }

@media (min-width: 768px) {
  .amb-morph-demo__hero { align-items: center; }
  .amb-morph-demo__trade { min-height: 42vh; min-height: 42svh; padding: 2.25rem; }
}
```

## JS

```js
document.querySelectorAll('.amb-morph').forEach((layer, index) => {
  const page = layer.classList.contains('amb-morph--page'), host = page ? document.documentElement : layer.parentElement;
  const scope = page ? document : host; // sections that declare shapes
  const float = layer.querySelector('.amb-morph__float'), paths = [...layer.querySelectorAll('.amb-morph__path')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)'), NUM = /-?\d*\.?\d+/g;

  // A second instance on the page gets its own gradient and clip ids
  if (index) layer.querySelectorAll('[id]').forEach((el) => {
    const was = `url(#${el.id})`;
    el.id += `-${index}`;
    layer.querySelectorAll('[fill], [stroke], [clip-path]').forEach((n) => ['fill', 'stroke', 'clip-path'].forEach((a) => {
      if (n.getAttribute(a) === was) n.setAttribute(a, `url(#${el.id})`);
    }));
  });

  // Shapes share one command skeleton, so a morph is plain number interpolation (works in every browser)
  const defs = {}, skeleton = layer.querySelector('[data-amb-morph-def]').getAttribute('d').split(NUM);
  layer.querySelectorAll('[data-amb-morph-def]').forEach((p) => {
    const v = p.getAttribute('d').match(NUM).map(Number);
    if (v.length === skeleton.length - 1) defs[p.dataset.ambMorphDef] = v; // skip shapes with a different point count
  });
  const render = (v) => {
    let d = skeleton[0];
    v.forEach((n, i) => { d += Math.round(n * 10) / 10 + skeleton[i + 1]; });
    paths.forEach((p) => p.setAttribute('d', d));
  };

  let cur = defs[layer.dataset.ambMorphCurrent] || Object.values(defs)[0], from = cur, to = cur, x = 1, xv = 0;
  let raf = 0, last = 0, scrolled = 0, pos = null, vel = 0, rot = 0, sc = 1, VH = innerHeight, visible = page, ready = false;

  const morphTo = (name) => {
    const v = defs[name];
    if (!v || v === to) return;
    layer.dataset.ambMorphCurrent = name; // CSS recolours the gradient through registered colours
    to = v;
    if (!ready || reduce.matches) { cur = from = v; x = 1; render(v); return; } // first paint, reduced motion: instant swap
    from = cur; x = 0; xv = 0;
    wake();
  };

  const tick = (now) => {
    raf = 0;
    const dt = last ? Math.min(0.05, (now - last) / 1000) : 1 / 60, r = host.getBoundingClientRect(), y = -r.top; // one layout read
    last = now;
    if (pos === null) pos = y;
    vel += ((y - pos) / Math.max(dt, 0.004) - vel) * 0.25; pos = y; // smoothed scroll speed, px/s
    if (x !== 1) { // morph spring: about 700ms with a slight overshoot
      xv += (170 * (1 - x) - 16 * xv) * dt; x += xv * dt;
      if (Math.abs(1 - x) < 0.001 && Math.abs(xv) < 0.01) x = 1;
      cur = from.map((n, i) => n + (to[i] - n) * x);
      render(cur);
    }
    // Scroll nudges: a slow turn with position, plus a tilt and a slight swell with speed
    const p = Math.min(1, Math.max(0, y / Math.max(1, r.height - VH))), k = 1 - Math.exp(-dt * 5);
    const tr = p * 20 + Math.max(-8, Math.min(8, vel / 160)), ts = 1 + Math.min(0.06, Math.abs(vel) / 30000);
    rot += (tr - rot) * k; sc += (ts - sc) * k;
    float.style.transform = `rotate(${rot.toFixed(2)}deg) scale(${sc.toFixed(4)})`;
    const moving = x !== 1 || now - scrolled < 150 || Math.abs(vel) > 3 || Math.abs(tr - rot) > 0.02 || Math.abs(ts - sc) > 0.0005;
    if (moving && visible && document.visibilityState === 'visible') raf = requestAnimationFrame(tick);
    else { vel = 0; layer.classList.remove('is-moving'); }
  };
  const wake = () => {
    if (raf || !visible || reduce.matches || document.visibilityState !== 'visible') return;
    layer.classList.add('is-moving'); last = 0; raf = requestAnimationFrame(tick);
  };

  // A section takes over when it crosses the middle of the viewport (a 2% band, no per-frame measuring)
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) morphTo(e.target.dataset.ambMorphShape); });
    ready = true;
  }, { rootMargin: '-49% 0px -49% 0px' });
  scope.querySelectorAll('[data-amb-morph-shape]').forEach((m) => io.observe(m));

  render(cur);
  addEventListener('scroll', () => { scrolled = performance.now(); wake(); }, { passive: true });
  addEventListener('resize', () => { VH = innerHeight; }, { passive: true });
  document.addEventListener('visibilitychange', wake);
  if (!page) new IntersectionObserver(([e]) => { visible = e.isIntersecting; pos = null; wake(); }).observe(host);
});
```

## Notes

- **Placement.** The layer is decorative (`aria-hidden`, `pointer-events: none`). By default it's the first child of a `position: relative; isolation: isolate` section, with a sticky, viewport-tall frame holding the shape. Add `.amb-morph--page` to fix it behind the whole page instead: shapes can then be declared by any element in the document, and every section needs a transparent background. Use one ambient background per page. A section takes over when it crosses a thin band at the middle of the viewport (an IntersectionObserver, not per-frame measuring), and a section without `data-amb-morph-shape` keeps the last shape.
- **Authoring shapes.** Every `data-amb-morph-def` path must use the same skeleton: `M x y` followed by exactly eight `C` segments (50 numbers), drawn clockwise from the top of the shape with numbers separated by spaces. Put anchors in matching places (anchor 0 at the top, about 2 on the right, 4 at the bottom, 6 on the left) so points travel short distances. For a sharp corner, put both handles on the anchor; for a smooth curve, set each handle a third of the way along the line between the neighbouring anchors. Use extra anchors on straight edges to make up the count of eight. Keep shapes inside the 200×200 box with about 8% margin for the spring overshoot. Then add a colour rule: `.amb-morph[data-amb-morph-current="name"] { --amb-morph-a: …; --amb-morph-b: …; }`. Paths whose number count doesn't match are ignored.
- **Contrast.** The glass is a 40% tint over the page, with a lighter specular shine and rim. Worst case in the demo: `--text-main` over the flame's red end and its glow is 5.75:1. `--text-muted` drops to 1.9:1 over the shape, so it's used only on the opaque cards (4.76:1), and the eyebrows use `--text-main`. Set `--amb-morph-scrim` (0–1) to lay a `--surface-light` veil over the shape.
- **Performance.** There's no canvas and no blur: the glow is a pre-blurred radial gradient. The loop runs only while the section is on screen, the tab is visible and something is moving. Each frame takes one `getBoundingClientRect`, rewrites three paths (body, clip and rim, 50 numbers) only during a morph, and sets one transform. It stops once the spring and the scroll nudges settle (about 1s after scrolling stops). `will-change` is applied only while the shape moves.
- **Reduced motion and no JS.** Shapes swap instantly with no spring, rotation or swell, and the recolour collapses with the motion tokens. Without JS, the shape in the markup (the house) shows as a still. The JS morph works in every browser; a CSS `d: path()` transition is an optional, Chromium-only alternative. Registered colours (`@property`) make the recolour smooth, and without them it swaps instantly.
