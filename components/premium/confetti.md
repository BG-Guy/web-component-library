# Confetti Burst

A dependency-free `window.confetti(options)` API that bursts brand-coloured confetti from any element or point on one shared, self-cleaning canvas. Rectangles, dots and twisting ribbons fly with gravity, drag, wobble and a 3D tilt that flips each piece as it falls, in three presets: `burst`, `cannons` and `rain`. In the demo, confirming a booking draws a check and fires confetti from the button itself. On phones the card fills the width and the cannons fire to fit the screen height. Depends on `tokens/variables.css`.

**Motion:** canvas particles on one rAF loop (gravity, drag, wobble, tilt; frame-rate independent) · calendar-to-check swap with ring and tick draw (`--dur-5`/`--dur-4`, `--ease-out`) and badge pop (`--ease-spring`) · button press and lift (`--ease-spring`).

## HTML

```html
<div class="confetti-fx-demo">
  <div class="confetti-fx-demo__inner">
    <article class="confetti-fx-demo__card" aria-labelledby="confetti-fx-title">
      <div class="confetti-fx-demo__badge" aria-hidden="true">
        <svg class="confetti-fx-demo__cal" viewBox="0 0 24 24" width="28" height="28" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zM8 14h3" /></svg>
        <svg class="confetti-fx-demo__tick" viewBox="0 0 64 64" width="72" height="72" focusable="false"><circle cx="32" cy="32" r="28" pathLength="1" /><path d="m21 33 8 8 15-17" pathLength="1" /></svg>
      </div>
      <p class="confetti-fx-demo__ref">Booking BR-1042</p>
      <h2 class="confetti-fx-demo__title" id="confetti-fx-title">Confirm your visit</h2>
      <p class="confetti-fx-demo__lead">Check the details, then lock in your slot. Rescheduling is free up to 2 hours before.</p>
      <dl class="confetti-fx-demo__details">
        <div><dt>Service</dt><dd>Leak repair</dd></div>
        <div><dt>When</dt><dd>Wed 15 Oct · 10–12</dd></div>
        <div><dt>Engineer</dt><dd>Maria R.</dd></div>
        <div><dt>Address</dt><dd>14 Elm Street, Westlake</dd></div>
        <div class="confetti-fx-demo__total"><dt>Estimate</dt><dd>$149</dd></div>
      </dl>
      <form class="confetti-fx-demo__form" action="/book/confirm" method="post">
        <button class="confetti-fx-demo__confirm" type="submit">
          <span class="confetti-fx-demo__label">Confirm booking</span>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </button>
      </form>
      <p class="confetti-fx-demo__sr" role="status"></p>
    </article>

    <div class="confetti-fx-demo__try" role="group" aria-labelledby="confetti-fx-try">
      <span class="confetti-fx-demo__try-label" id="confetti-fx-try">Try a preset</span>
      <button type="button" data-confetti="burst">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.2 2.2M16.2 16.2l2.2 2.2M5.6 18.4l2.2-2.2M16.2 7.8l2.2-2.2" /></svg>
        Burst
      </button>
      <button type="button" data-confetti="cannons">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m3 21 5.5-13.5 8 8zM13 3l.8 2.2M18.5 4.5 17 6M21 9.5l-2.2.6M15.5 8.5 18 6" /></svg>
        Cannons
      </button>
      <button type="button" data-confetti="rain">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M6 3v3M12 2v4M18 3v3M9 9v3M15 9v3M6 15v2M12 14v4M18 15v2M9 20v1M15 20v1" /></svg>
        Rain
      </button>
    </div>
    <p class="confetti-fx-demo__rm">Confetti is switched off because your device asks for reduced motion.</p>
  </div>
</div>
```

## CSS

```css
/* The shared canvas the API creates on first use and removes when the last piece lands */
.confetti-fx { position: fixed; inset: 0; z-index: var(--z-toast); width: 100%; height: 100%; pointer-events: none; }

/* Demo: a booking confirmation on a softly lit light page */
.confetti-fx-demo {
  --confetti-fx-muted: color-mix(in srgb, var(--text-muted) 75%, var(--text-main));
  --confetti-fx-accent: color-mix(in srgb, var(--primary) 80%, var(--text-main));
  display: grid; align-items: center; min-height: 40rem; padding-block: clamp(3rem, 8vw, 5rem);
  background:
    radial-gradient(50% 40% at 50% 0%, color-mix(in srgb, var(--primary) 12%, transparent), transparent 70%),
    radial-gradient(40% 40% at 0% 100%, color-mix(in srgb, var(--accent) 12%, transparent), transparent 70%),
    radial-gradient(40% 40% at 100% 90%, color-mix(in srgb, var(--primary-2) 12%, transparent), transparent 70%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
.confetti-fx-demo__inner { display: grid; justify-items: center; gap: 1.75rem; width: 100%; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); box-sizing: border-box; }
.confetti-fx-demo svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.confetti-fx-demo button:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.confetti-fx-demo__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }

/* Card */
.confetti-fx-demo__card {
  position: relative; width: min(100%, 27rem); padding: clamp(1.5rem, 5vw, 2.25rem); border-radius: var(--radius-2xl); text-align: center; box-sizing: border-box;
  background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl), 0 40px 80px -40px color-mix(in srgb, var(--primary) 45%, transparent);
}
.confetti-fx-demo__card::before { content: ""; position: absolute; top: 0; left: 2.5rem; right: 2.5rem; height: 2px; border-radius: 2px; background: var(--gradient-brand); }
.confetti-fx-demo__badge {
  display: grid; place-items: center; width: 4.5rem; height: 4.5rem; margin: 0 auto 1.25rem; border-radius: 50%; color: var(--primary);
  background: radial-gradient(circle at 30% 25%, color-mix(in srgb, var(--primary) 14%, var(--surface-light)), var(--surface-light) 70%);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md);
}
.confetti-fx-demo__badge svg { grid-area: 1 / 1; }
.confetti-fx-demo__cal { transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring); }
.confetti-fx-demo__tick { opacity: 0; }
.confetti-fx-demo__tick circle, .confetti-fx-demo__tick path { stroke-dasharray: 1; }
.confetti-fx-demo__tick circle { stroke: color-mix(in srgb, var(--success) 30%, transparent); stroke-width: 3; }
.confetti-fx-demo__tick path { stroke: var(--success); stroke-width: 4.5; }
.confetti-fx-demo__ref { margin: 0; color: var(--confetti-fx-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.confetti-fx-demo__title { margin: 0.5rem 0 0; font: 600 clamp(1.75rem, 1.4rem + 1.6vw, 2.25rem)/1.1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.confetti-fx-demo__lead { max-width: 22rem; margin: 0.75rem auto 0; color: var(--confetti-fx-muted); line-height: 1.55; }
.confetti-fx-demo__details {
  display: grid; gap: 0.625rem; margin: 1.5rem 0 0; padding: 1rem 1.125rem; border-radius: var(--radius-xl); text-align: left;
  background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle);
}
.confetti-fx-demo__details div { display: flex; justify-content: space-between; gap: 1rem; font-size: 0.875rem; }
.confetti-fx-demo__details dt { flex: none; color: var(--confetti-fx-muted); }
.confetti-fx-demo__details dd { margin: 0; font-weight: 600; text-align: right; }
.confetti-fx-demo__details .confetti-fx-demo__total { padding-top: 0.625rem; border-top: 1px dashed var(--border-subtle); }
.confetti-fx-demo__total dd { font: 600 1rem var(--font-mono); }
.confetti-fx-demo__form { margin: 1.5rem 0 0; }
.confetti-fx-demo__confirm {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; width: 100%; height: 3.25rem; border: 0; border-radius: 999px; cursor: pointer;
  background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font: 600 1rem var(--font-sans);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 25%, transparent), var(--shadow-glow);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.confetti-fx-demo__confirm svg { transition: transform var(--dur-3) var(--ease-spring); }
.confetti-fx-demo__confirm:hover { transform: translateY(-1px); }
.confetti-fx-demo__confirm:hover svg { transform: translateX(3px); }
.confetti-fx-demo__confirm:active { transform: scale(0.97); }

/* Confirmed: calendar spins away, the ring and tick draw, the button turns green */
.confetti-fx-demo__card.is-confirmed .confetti-fx-demo__badge { background: radial-gradient(circle at 30% 25%, color-mix(in srgb, var(--success) 16%, var(--surface-light)), var(--surface-light) 70%); }
.confetti-fx-demo__card.is-confirmed .confetti-fx-demo__cal { opacity: 0; transform: scale(0.4) rotate(-20deg); }
.confetti-fx-demo__card.is-confirmed .confetti-fx-demo__tick { opacity: 1; animation: confetti-fx-pop var(--dur-5) var(--ease-spring) both; }
.confetti-fx-demo__card.is-confirmed .confetti-fx-demo__tick circle { animation: confetti-fx-draw var(--dur-5) var(--ease-out) both; }
.confetti-fx-demo__card.is-confirmed .confetti-fx-demo__tick path { animation: confetti-fx-draw var(--dur-4) var(--ease-out) 300ms both; }
.confetti-fx-demo__card.is-confirmed .confetti-fx-demo__confirm {
  background: linear-gradient(180deg, var(--success), color-mix(in srgb, var(--success) 82%, var(--surface-deep)));
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 25%, transparent), 0 10px 40px -10px color-mix(in srgb, var(--success) 60%, transparent);
}

/* Preset buttons */
.confetti-fx-demo__try { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; }
.confetti-fx-demo__try-label { width: 100%; margin-bottom: 0.25rem; color: var(--confetti-fx-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-align: center; text-transform: uppercase; }
.confetti-fx-demo__try button {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 2.75rem; padding: 0 1.125rem; border: 0; border-radius: 999px; cursor: pointer;
  background: var(--surface-light); color: var(--text-main); font: 600 0.875rem var(--font-sans);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.confetti-fx-demo__try button:hover { transform: translateY(-2px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md); }
.confetti-fx-demo__try button:active { transform: scale(0.95); }
.confetti-fx-demo__try svg { color: var(--confetti-fx-accent); }
.confetti-fx-demo__rm { display: none; max-width: 24rem; margin: 0; color: var(--confetti-fx-muted); font-size: 0.875rem; text-align: center; }

/* No JS: nothing to try. Reduced motion: say why nothing flies, and draw the check instantly */
@media (scripting: none) { .confetti-fx-demo__try { display: none; } }
@media (prefers-reduced-motion: reduce) {
  .confetti-fx-demo__rm { display: block; }
  .confetti-fx-demo *, .confetti-fx-demo *::before, .confetti-fx-demo *::after { animation: none !important; }
}
@keyframes confetti-fx-draw { from { stroke-dashoffset: 1; } }
@keyframes confetti-fx-pop { from { opacity: 0; transform: scale(0.6); } }
```

## JS

```js
// window.confetti(options): dependency-free confetti on one shared, self-cleaning canvas
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const TAU = Math.PI * 2;
const MAX = 700; // pieces on screen at once, across all calls
const rand = (a, b) => a + Math.random() * (b - a);
const PRESETS = {
  burst: { count: 130, angle: 90, spread: 110, speed: [9, 21], gravity: 0.35, drag: 0.955, life: [2200, 3200], sway: 0.6 },
  cannons: { count: 90, spread: 50, speed: [26, 38], gravity: 0.35, drag: 0.965, life: [2600, 3600], sway: 0.6 },
  rain: { count: 160, angle: 270, spread: 30, speed: [1, 3], gravity: 0.06, drag: 0.99, life: [4200, 5600], sway: 1.4 },
};
let canvas = null, ctx = null, parts = [], raf = 0, last = 0, w = 0, h = 0;

const fit = () => {
  const dpr = Math.min(devicePixelRatio || 1, 2);
  [w, h] = [innerWidth, innerHeight];
  canvas.width = w * dpr;
  canvas.height = h * dpr;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
};
const mount = () => {
  if (canvas) return;
  canvas = Object.assign(document.createElement('canvas'), { className: 'confetti-fx' });
  canvas.setAttribute('aria-hidden', 'true');
  document.body.append(canvas);
  ctx = canvas.getContext('2d');
  fit();
  addEventListener('resize', fit, { passive: true });
};
const unmount = () => {
  removeEventListener('resize', fit);
  canvas.remove();
  canvas = ctx = null;
};

// Brand colours are read from the tokens at call time, so a retheme or dark mode just works
const tokenColors = () => ['--primary', '--primary-2', '--accent', '--success'].map((token) => {
  canvas.style.color = `var(${token})`;
  return getComputedStyle(canvas).color;
});
const point = (from) => {
  if (!(from instanceof Element)) return { x: (from?.x ?? 0.5) * w, y: (from?.y ?? 0.5) * h }; // viewport fractions
  const r = from.getBoundingClientRect();
  return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
};

const piece = (x, y, angle, o, colors, owner, delay = 0) => {
  const a = ((angle + rand(-o.spread / 2, o.spread / 2)) * Math.PI) / 180;
  const v = rand(o.speed[0], o.speed[1]);
  const kind = Math.random();
  return {
    x, y, vx: Math.cos(a) * v, vy: -Math.sin(a) * v, owner, age: -delay, life: rand(o.life[0], o.life[1]),
    gravity: o.gravity, drag: o.drag, sway: o.sway, size: rand(0.8, 1.25), color: colors[(Math.random() * colors.length) | 0],
    shape: kind < 0.45 ? 'rect' : kind < 0.75 ? 'dot' : 'ribbon',
    rot: rand(0, TAU), spin: rand(-0.18, 0.18), tilt: rand(0, TAU), tiltSpeed: rand(0.05, 0.16), wobble: rand(0, TAU), wobbleSpeed: rand(0.04, 0.1),
  };
};

const draw = (p, alpha) => {
  const flip = Math.cos(p.tilt), s = p.size;
  ctx.save();
  ctx.globalAlpha = alpha * (flip < 0 ? 0.8 : 1); // the back face reads a touch darker
  ctx.fillStyle = p.color;
  ctx.translate(p.x, p.y);
  ctx.rotate(p.rot);
  ctx.beginPath();
  if (p.shape === 'rect') ctx.rect(-5 * s, -3 * s * flip, 10 * s, 6 * s * flip);
  else if (p.shape === 'dot') ctx.ellipse(0, 0, 4 * s, 4 * s * Math.abs(flip) + 0.4, 0, 0, TAU);
  else { // a ribbon: its width follows cos(), so the strip pinches and twists along its length
    for (let i = 0; i <= 13; i++) {
      const top = i < 7, u = top ? i / 6 : (13 - i) / 6;
      ctx.lineTo((u - 0.5) * 22 * s, Math.sin(u * TAU + p.wobble) * 3 * s + (top ? -1 : 1) * Math.cos(p.tilt + u * Math.PI) * 2.6 * s);
    }
  }
  ctx.fill();
  ctx.restore();
};

// One loop for every call; frame-rate independent; stops and removes the canvas when empty
const tick = (now) => {
  const dt = Math.min(now - last, 50), t = dt / 16.67;
  last = now;
  ctx.clearRect(0, 0, w, h);
  parts = parts.filter((p) => {
    if ((p.age += dt) < 0) return true; // rain drops waiting their turn
    p.vx *= p.drag ** t;
    p.vy = p.vy * p.drag ** t + p.gravity * t;
    p.wobble += p.wobbleSpeed * t;
    p.tilt += p.tiltSpeed * t;
    p.rot += p.spin * t;
    p.x += (p.vx + Math.cos(p.wobble) * p.sway) * t;
    p.y += p.vy * t;
    const alpha = Math.min(1, (p.life - p.age) / 500);
    if (alpha > 0 && p.y < h + 40) { draw(p, alpha); return true; }
    if (--p.owner.left === 0) p.owner.done();
    return false;
  });
  if (parts.length) raf = requestAnimationFrame(tick);
  else { raf = 0; unmount(); }
};

window.confetti = (options = {}) => {
  if (reduce.matches) return Promise.resolve(); // reduced motion: no confetti at all
  mount();
  const preset = PRESETS[options.preset] ? options.preset : 'burst';
  const o = { ...PRESETS[preset], ...options };
  const colors = o.colors || tokenColors();
  const owner = { left: 0 };
  const done = new Promise((resolve) => { owner.done = resolve; });
  const room = Math.max(0, MAX - parts.length);
  const batch = [];
  if (preset === 'cannons') { // from both bottom corners, scaled to the viewport height
    const k = Math.min(1.3, Math.max(0.8, Math.sqrt(h / 700)));
    const oc = { ...o, speed: o.speed.map((v) => v * k) };
    for (let i = 0; i < Math.min(o.count, room / 2); i++) {
      batch.push(piece(0, h, 60, oc, colors, owner, rand(0, 150)), piece(w, h, 120, oc, colors, owner, rand(0, 150)));
    }
  } else if (preset === 'rain') { // from just above the top edge, spread over ~2s
    for (let i = 0; i < Math.min(o.count, room); i++) batch.push(piece(rand(0, w), rand(-80, -10), o.angle, o, colors, owner, rand(0, 1800)));
  } else {
    const { x, y } = point(o.origin);
    for (let i = 0; i < Math.min(o.count, room); i++) batch.push(piece(x, y, o.angle, o, colors, owner));
  }
  owner.left = batch.length;
  parts.push(...batch);
  if (!batch.length) owner.done();
  if (!parts.length) unmount();
  else if (!raf) { last = performance.now(); raf = requestAnimationFrame(tick); }
  return done;
};

// Demo: confirming the booking draws the check and celebrates from the button
document.querySelectorAll('.confetti-fx-demo').forEach((demo) => {
  const card = demo.querySelector('.confetti-fx-demo__card');
  const form = demo.querySelector('.confetti-fx-demo__form');
  form.addEventListener('submit', (e) => {
    e.preventDefault(); // demo only: a real page confirms on the server, then celebrates
    if (!card.classList.contains('is-confirmed')) {
      card.classList.add('is-confirmed');
      const copy = { title: 'Booking confirmed', lead: 'We’ll text you when Maria is on her way. See you Wednesday!', label: 'Celebrate again', sr: 'Booking confirmed. We’ll text you when Maria is on her way.' };
      Object.entries(copy).forEach(([part, text]) => { card.querySelector(`.confetti-fx-demo__${part}`).textContent = text; });
    }
    window.confetti({ preset: 'burst', origin: form.querySelector('button') });
  });
  demo.querySelectorAll('[data-confetti]').forEach((b) => b.addEventListener('click', () => window.confetti({ preset: b.dataset.confetti, origin: b })));
});
```

## Notes

- **API:** `confetti(options?)` returns a Promise that resolves once that call's pieces have landed. The options are `preset` (`'burst'` by default, `'cannons'` or `'rain'`) and `origin`, which is used by `burst` and takes an Element or `{ x, y }` as 0–1 fractions of the viewport (centre by default). The rest override the preset: `count`, `angle` (degrees, 90 is up), `spread` (degrees), `speed: [min, max]` (px per 60fps frame), `gravity`, `drag`, `life: [min, max]` (ms), `sway` and `colors` (any CSS colours). For example: `confetti({ origin: button })`, `confetti({ preset: 'cannons' })`, `await confetti({ preset: 'rain', count: 80 })`.
- **Canvas:** one shared `.confetti-fx` canvas (`position: fixed`, `pointer-events: none`, `aria-hidden`, `--z-toast`) is created on the first call and removed when the last piece lands. Every call shares one rAF loop, with at most 700 pieces and the pixel ratio capped at 2. Colours come from `--primary`, `--primary-2`, `--accent` and `--success`, resolved at call time.
- **Reduced motion:** the API returns a resolved Promise straight away and draws nothing, and the demo says so in a note. Confetti is decoration only, so put the meaning in text: the demo swaps the heading to "Booking confirmed" and announces it through `role="status"`.
- **Install:** load the script once as a module. `window.confetti` is its only global, so call it from success handlers anywhere. The `.confetti-fx-demo` wiring is demo-only. Without JS the booking form posts normally, and `@media (scripting: none)` hides the preset row.
- **Contrast:** button text is `--text-inverse` on the `--primary` gradient (≥ 5.2:1), and on `--success` once confirmed (5:1). Muted copy uses `--confetti-fx-muted` (≈ 5.9:1).
