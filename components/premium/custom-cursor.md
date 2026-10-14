# Custom Cursor

A two-part cursor for mouse users: a dot that tracks the pointer exactly and a ring that trails it on a spring, stretching along its path as it moves. Over links and buttons the ring swells into a difference-blend disc that inverts what's beneath it. Over projects it becomes a brand pill that says "View" or "Play", and magnetic calls to action pull the ring in while they lean toward the pointer. On touch screens, pens and keyboards nothing changes, and the demo reflows into a single column. Depends on `tokens/variables.css`.

**Motion:** dot follows every frame · ring trails on a rAF spring with velocity stretch · disc and label grow with `--ease-spring` (`--dur-4`) · press shrink · magnetic pull on a spring · project hover zoom (`--dur-5`, `--ease-out`).

## HTML

```html
<div class="cursor-fx-demo">
  <div class="cursor-fx-demo__inner">
    <div class="cursor-fx-demo__head">
      <div>
        <p class="cursor-fx-demo__eyebrow">Recent work</p>
        <h2 class="cursor-fx-demo__title">Projects around Springfield</h2>
      </div>
      <a class="cursor-fx-demo__all" href="#projects">
        All projects
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </a>
    </div>
    <p class="cursor-fx-demo__note">With a mouse, links invert the cursor, projects say hello and the call button pulls it in. Touch screens keep their native behaviour.</p>

    <div class="cursor-fx-demo__grid">
      <a class="cursor-fx-demo__project cursor-fx-demo__project--wide" href="#westlake-kitchen" data-cursor="View">
        <span class="cursor-fx-demo__media"><img src="westlake-kitchen.jpg" width="960" height="640" alt="" loading="lazy"></span>
        <span class="cursor-fx-demo__caption"><strong>Westlake kitchen re-pipe</strong><small>Plumbing · 2025</small></span>
      </a>
      <a class="cursor-fx-demo__project" href="#riverside-bathroom" data-cursor="View">
        <span class="cursor-fx-demo__media cursor-fx-demo__media--alt"><img src="riverside-bathroom.jpg" width="640" height="640" alt="" loading="lazy"></span>
        <span class="cursor-fx-demo__caption"><strong>Riverside bathroom</strong><small>Refit · 2025</small></span>
      </a>

      <article class="cursor-fx-demo__dark" aria-labelledby="cursor-fx-dark-title">
        <p class="cursor-fx-demo__tag"><span class="cursor-fx-demo__live" aria-hidden="true"></span>On call now</p>
        <h3 id="cursor-fx-dark-title">Burst pipe at 2am? We pick up.</h3>
        <p>A licensed engineer reaches you within the hour across Westlake, Northside and Riverside.</p>
        <div class="cursor-fx-demo__row">
          <a class="cursor-fx-demo__call" href="tel:+15555550123" data-cursor-magnet>
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
            (555) 555-0123
          </a>
          <a class="cursor-fx-demo__play" href="#burst-pipe-video" data-cursor="Play">
            <span class="cursor-fx-demo__thumb" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M8 5.5v13l10-6.5z" /></svg></span>
            <span>How we fix a burst pipe <small>Video · 1:12</small></span>
          </a>
        </div>
      </article>

      <form class="cursor-fx-demo__form" action="/contact" method="post">
        <h3>Get a quote by email</h3>
        <label for="cursor-fx-email">Email</label>
        <div class="cursor-fx-demo__field">
          <input id="cursor-fx-email" name="email" type="email" autocomplete="email" placeholder="you@example.com" required>
          <button type="submit" data-cursor-magnet>Send</button>
        </div>
        <p>Text fields keep the normal text cursor.</p>
      </form>
    </div>
  </div>
</div>

<!-- Once per page, last in <body>: decorative, and only switched on for fine pointers -->
<div class="cursor-fx" aria-hidden="true" hidden>
  <div class="cursor-fx__ring"><span class="cursor-fx__label"></span></div>
  <div class="cursor-fx__dot"></div>
</div>
```

## CSS

```css
/* Page level: hide the system cursor only while the custom one is running.
   Text fields keep their I-beam, and dialogs/popovers (top layer, above the cursor) keep the native cursor. */
html:has(.cursor-fx.is-on), html:has(.cursor-fx.is-on) :not(dialog[open], dialog[open] *, [popover], [popover] *) { cursor: none; }
html:has(.cursor-fx.is-on) :is(dialog[open], [popover]) { cursor: auto; }
html:has(.cursor-fx.is-on) :is(input:not([type="checkbox"], [type="radio"], [type="range"], [type="button"], [type="submit"], [type="reset"], [type="color"], [type="file"], [type="image"]), textarea, [contenteditable]:not([contenteditable="false"])) { cursor: auto; }

/* Cursor parts sit straight on the page (no wrapper stacking context), so difference blending reaches the content */
.cursor-fx { --cursor-fx-size: 2.25rem; --cursor-fx-press: 1; }
.cursor-fx__ring, .cursor-fx__dot {
  position: fixed; top: 0; left: 0; z-index: var(--z-popover); pointer-events: none; will-change: transform;
  transition: opacity var(--dur-2) var(--ease-out);
}
.cursor-fx__ring { width: 0; height: 0; mix-blend-mode: difference; }
.cursor-fx__ring::before {
  content: ""; position: absolute; top: 0; left: 0; translate: -50% -50%; border-radius: 50%;
  width: calc(var(--cursor-fx-size) * var(--cursor-fx-press)); height: calc(var(--cursor-fx-size) * var(--cursor-fx-press));
  border: 1.5px solid var(--text-inverse); background-color: transparent;
  transform: rotate(var(--cursor-fx-a, 0rad)) scale(var(--cursor-fx-sx, 1), var(--cursor-fx-sy, 1));
  transition: width var(--dur-4) var(--ease-spring), height var(--dur-4) var(--ease-spring), background-color var(--dur-3) var(--ease-out), border-color var(--dur-3);
}
.cursor-fx__dot { width: 0.375rem; height: 0.375rem; margin: -0.1875rem 0 0 -0.1875rem; border-radius: 50%; background: var(--text-inverse); mix-blend-mode: difference; }
.cursor-fx__label {
  position: absolute; top: 0; left: 0; translate: -50% -50%; opacity: 0; scale: 0.6;
  color: var(--text-inverse); font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; white-space: nowrap;
  transition: opacity var(--dur-2) var(--ease-out), scale var(--dur-4) var(--ease-spring);
}

/* States set by JS on the wrapper */
.cursor-fx.is-link { --cursor-fx-size: 4rem; }
.cursor-fx.is-link .cursor-fx__ring::before { border-color: transparent; background-color: var(--text-inverse); }
.cursor-fx.is-label { --cursor-fx-size: 5.25rem; }
.cursor-fx.is-label .cursor-fx__ring { mix-blend-mode: normal; }
.cursor-fx.is-label .cursor-fx__ring::before {
  border-color: transparent;
  background-image: linear-gradient(135deg, var(--primary), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
  box-shadow: var(--highlight-inverse), var(--shadow-glow);
}
.cursor-fx.is-label .cursor-fx__label { opacity: 1; scale: 1; transition-delay: var(--stagger); }
.cursor-fx.is-down { --cursor-fx-press: 0.78; }
.cursor-fx.is-label .cursor-fx__dot,
.cursor-fx.is-hidden .cursor-fx__ring, .cursor-fx.is-hidden .cursor-fx__dot,
.cursor-fx.is-native .cursor-fx__ring, .cursor-fx.is-native .cursor-fx__dot { opacity: 0; }

/* Demo: a light projects page with one dark card */
.cursor-fx-demo {
  --cursor-fx-muted: color-mix(in srgb, var(--text-muted) 75%, var(--text-main));
  background: radial-gradient(60% 40% at 100% 0%, color-mix(in srgb, var(--primary) 8%, transparent), transparent 70%), var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
.cursor-fx-demo svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.cursor-fx-demo__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(3.5rem, 8vw, 6rem) var(--gutter); }
.cursor-fx-demo__head { display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 1rem 2rem; }
.cursor-fx-demo__eyebrow { margin: 0; color: color-mix(in srgb, var(--primary) 80%, var(--text-main)); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.cursor-fx-demo__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.3rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.cursor-fx-demo__all { display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.75rem; border-radius: var(--radius-sm); color: var(--text-main); font-weight: 600; text-decoration: none; }
.cursor-fx-demo__all svg { transition: transform var(--dur-3) var(--ease-spring); }
.cursor-fx-demo__all:hover svg { transform: translateX(4px); }
.cursor-fx-demo__note { max-width: 40rem; margin: 1rem 0 0; color: var(--cursor-fx-muted); line-height: 1.6; }
.cursor-fx-demo a:focus-visible, .cursor-fx-demo button:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.cursor-fx-demo__grid { display: grid; gap: 1rem; margin-top: 2.5rem; }

/* Project cards */
.cursor-fx-demo__project {
  display: grid; gap: 0.875rem; padding: 0.5rem 0.5rem 1rem; border-radius: var(--radius-2xl); color: var(--text-main); text-decoration: none;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm);
  transition: box-shadow var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-out);
}
.cursor-fx-demo__project:hover { transform: translateY(-2px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl); }
.cursor-fx-demo__media {
  display: block; overflow: hidden; aspect-ratio: 3 / 2; border-radius: var(--radius-xl);
  background:
    radial-gradient(60% 80% at 20% 15%, color-mix(in srgb, var(--accent) 45%, transparent), transparent 70%),
    linear-gradient(135deg, color-mix(in srgb, var(--primary) 70%, var(--surface-deep)), var(--primary-2));
}
.cursor-fx-demo__media--alt {
  background:
    radial-gradient(70% 70% at 80% 20%, color-mix(in srgb, var(--primary-2) 55%, transparent), transparent 70%),
    linear-gradient(160deg, color-mix(in srgb, var(--accent) 35%, var(--surface-light)), color-mix(in srgb, var(--primary) 55%, var(--surface-deep)));
}
.cursor-fx-demo__media img { display: block; width: 100%; height: 100%; object-fit: cover; transition: scale var(--dur-5) var(--ease-out); }
.cursor-fx-demo__project:hover img { scale: 1.04; }
.cursor-fx-demo__caption { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: 0.25rem 1rem; padding-inline: 0.5rem; }
.cursor-fx-demo__caption strong { font: 600 1rem var(--font-display); letter-spacing: var(--tracking-tight); }
.cursor-fx-demo__caption small { color: var(--cursor-fx-muted); font: 0.75rem var(--font-mono); white-space: nowrap; }

/* Dark card */
.cursor-fx-demo__dark {
  display: grid; align-content: start; gap: 0.875rem; padding: clamp(1.5rem, 4vw, 2.25rem); border-radius: var(--radius-2xl); overflow: hidden;
  background:
    radial-gradient(80% 70% at 100% 0%, color-mix(in srgb, var(--primary) 40%, transparent), transparent 70%),
    radial-gradient(70% 60% at 0% 100%, color-mix(in srgb, var(--primary-2) 30%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); box-shadow: var(--highlight-inverse), var(--shadow-xl);
}
.cursor-fx-demo__dark h3 { max-width: 18ch; margin: 0; font: 600 clamp(1.5rem, 1.2rem + 1.3vw, 2.125rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.cursor-fx-demo__dark p { max-width: 34rem; margin: 0; color: var(--text-inverse-muted); line-height: 1.6; }
.cursor-fx-demo__dark a:focus-visible { outline-color: var(--text-inverse); }
.cursor-fx-demo .cursor-fx-demo__tag {
  display: inline-flex; align-items: center; gap: 0.5rem; justify-self: start; padding: 0.3125rem 0.75rem; border-radius: 999px;
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); color: var(--text-inverse); font: 500 0.75rem var(--font-mono);
}
.cursor-fx-demo__live { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 30%, transparent); }
.cursor-fx-demo__row { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem 1.5rem; margin-top: 0.5rem; }
.cursor-fx-demo__call {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; padding: 0 1.375rem; border-radius: 999px;
  background: var(--text-inverse); color: var(--surface-deep); font-weight: 600; text-decoration: none;
  box-shadow: 0 12px 32px -12px color-mix(in srgb, var(--primary) 80%, transparent);
}
.cursor-fx-demo__play { display: inline-flex; align-items: center; gap: 0.75rem; min-height: 3rem; border-radius: var(--radius-lg); color: var(--text-inverse); font-weight: 600; text-decoration: none; }
.cursor-fx-demo__play small { display: block; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); }
.cursor-fx-demo__thumb {
  display: grid; place-items: center; width: 4.5rem; height: 3rem; border-radius: 0.75rem;
  background: radial-gradient(80% 90% at 30% 20%, color-mix(in srgb, var(--accent) 40%, transparent), transparent 70%), linear-gradient(135deg, var(--primary), var(--primary-2));
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.cursor-fx-demo__thumb svg { fill: currentColor; }

/* Quote form: the text field keeps the system cursor */
.cursor-fx-demo__form {
  display: grid; align-content: start; gap: 0.625rem; padding: clamp(1.5rem, 4vw, 2rem); border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm);
}
.cursor-fx-demo__form h3 { margin: 0 0 0.375rem; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.cursor-fx-demo__form label { font-size: 0.875rem; font-weight: 600; }
.cursor-fx-demo__form p { margin: 0; color: var(--cursor-fx-muted); font-size: 0.8125rem; }
.cursor-fx-demo__field { display: flex; gap: 0.5rem; }
.cursor-fx-demo__field input {
  flex: 1; min-width: 0; height: 3rem; padding: 0 1rem; border: 0; border-radius: 999px;
  background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); color: var(--text-main); font: 1rem var(--font-sans);
  transition: box-shadow var(--dur-2);
}
.cursor-fx-demo__field input::placeholder { color: var(--cursor-fx-muted); opacity: 1; }
.cursor-fx-demo__field input:focus { outline: 2px solid transparent; box-shadow: inset 0 0 0 1px var(--primary), var(--focus-ring); }
.cursor-fx-demo__field button {
  flex: none; height: 3rem; padding: 0 1.25rem; border: 0; border-radius: 999px; cursor: pointer;
  background: var(--primary); color: var(--text-inverse); font: 600 0.9375rem var(--font-sans); box-shadow: var(--shadow-glow);
}

@media (min-width: 768px) {
  .cursor-fx-demo__grid { grid-template-columns: repeat(6, minmax(0, 1fr)); }
  .cursor-fx-demo__project { grid-column: span 2; }
  .cursor-fx-demo__project--wide { grid-column: span 4; }
  .cursor-fx-demo__media { aspect-ratio: auto; height: clamp(14rem, 24vw, 19rem); }
  .cursor-fx-demo__dark, .cursor-fx-demo__form { grid-column: span 3; }
}
@media (min-width: 1024px) {
  .cursor-fx-demo__dark { grid-column: span 4; }
  .cursor-fx-demo__form { grid-column: span 2; }
}
```

## JS

```js
const fx = document.querySelector('.cursor-fx');
const fine = matchMedia('(hover: hover) and (pointer: fine)');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
// Where the system cursor takes over: text fields, and dialogs/popovers that sit above the cursor in the top layer
const NATIVE = 'input:not([type="checkbox"], [type="radio"], [type="range"], [type="button"], [type="submit"], [type="reset"], [type="color"], [type="file"], [type="image"]), textarea, [contenteditable]:not([contenteditable="false"]), dialog[open], [popover]';
const HOT = 'a[href], button, [role="button"], label, summary, select, [data-cursor], [data-cursor-magnet]';

if (fx && fine.matches && !reduce.matches) {
  const ring = fx.querySelector('.cursor-fx__ring');
  const dot = fx.querySelector('.cursor-fx__dot');
  const label = fx.querySelector('.cursor-fx__label');
  const p = { x: 0, y: 0 }; // pointer
  const r = { x: 0, y: 0, vx: 0, vy: 0 }; // ring
  const m = { x: 0, y: 0, vx: 0, vy: 0 }; // magnet's own nudge
  const ac = new AbortController();
  const on = { passive: true, signal: ac.signal };
  let magnet = null, nudged = null, raf = 0, last = 0;

  // Damped spring, normalised to 60fps so it feels the same on 120Hz screens
  const spring = (s, tx, ty, k, damp, t) => {
    s.vx = (s.vx + (tx - s.x) * k * t) * damp ** t;
    s.vy = (s.vy + (ty - s.y) * k * t) * damp ** t;
    s.x += s.vx * t;
    s.y += s.vy * t;
  };

  const frame = (now) => {
    const t = Math.min((now - last) / 16.67, 3);
    last = now;
    let tx = p.x, ty = p.y, mx = 0, my = 0;
    if (magnet) { // pull the ring toward the element's centre and lean the element toward the pointer
      const b = magnet.getBoundingClientRect();
      const cx = b.left + b.width / 2 - m.x, cy = b.top + b.height / 2 - m.y;
      tx = cx + (p.x - cx) * 0.35; ty = cy + (p.y - cy) * 0.35;
      mx = (p.x - cx) * 0.22; my = (p.y - cy) * 0.22;
    }
    spring(r, tx, ty, 0.14, 0.72, t);
    if (nudged) {
      spring(m, mx, my, 0.12, 0.7, t);
      nudged.style.translate = `${m.x.toFixed(2)}px ${m.y.toFixed(2)}px`;
      if (!magnet && Math.abs(m.x) + Math.abs(m.y) + Math.abs(m.vx) + Math.abs(m.vy) < 0.05) { nudged.style.translate = ''; nudged = null; }
    }
    const speed = Math.hypot(r.vx, r.vy), stretch = Math.min(speed / 50, 0.3);
    dot.style.transform = `translate3d(${p.x}px, ${p.y}px, 0)`;
    ring.style.transform = `translate3d(${r.x}px, ${r.y}px, 0)`;
    ring.style.setProperty('--cursor-fx-a', `${Math.atan2(r.vy, r.vx)}rad`);
    ring.style.setProperty('--cursor-fx-sx', 1 + stretch);
    ring.style.setProperty('--cursor-fx-sy', 1 - stretch / 2);
    const settled = speed < 0.02 && Math.abs(tx - r.x) + Math.abs(ty - r.y) < 0.1 && !nudged;
    raf = settled ? 0 : requestAnimationFrame(frame);
  };
  const wake = () => { if (!raf) { last = performance.now(); raf = requestAnimationFrame(frame); } };

  fx.hidden = false;
  fx.classList.add('is-on', 'is-hidden');

  addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    if (fx.classList.contains('is-hidden')) Object.assign(r, { x: e.clientX, y: e.clientY, vx: 0, vy: 0 }); // appear in place
    p.x = e.clientX;
    p.y = e.clientY;
    fx.classList.remove('is-hidden');
    wake();
  }, on);

  // What's under the pointer sets the shape: native zone, link disc, label pill, magnet
  document.addEventListener('pointerover', (e) => {
    if (e.pointerType !== 'mouse') return;
    const native = e.target.closest(NATIVE);
    const hot = !native && e.target.closest(HOT);
    const word = hot && hot.closest('[data-cursor]')?.dataset.cursor;
    fx.classList.toggle('is-native', !!native);
    fx.classList.toggle('is-link', !!hot && !word);
    fx.classList.toggle('is-label', !!word);
    if (word) label.textContent = word;
    const next = (hot && hot.closest('[data-cursor-magnet]')) || null;
    if (next !== magnet) {
      if (nudged && nudged !== next) { nudged.style.translate = ''; Object.assign(m, { x: 0, y: 0, vx: 0, vy: 0 }); }
      magnet = next;
      nudged = next || nudged;
    }
    wake();
  }, on);

  // Leaving the window hides it; pressing shrinks the ring
  document.addEventListener('pointerout', (e) => {
    if (e.relatedTarget || e.pointerType !== 'mouse') return;
    fx.classList.add('is-hidden');
    magnet = null;
    wake();
  }, on);
  addEventListener('pointerdown', (e) => fx.classList.toggle('is-down', e.pointerType === 'mouse'), on);
  addEventListener('pointerup', () => fx.classList.remove('is-down'), on);

  // Hand back to the system cursor if the device or the motion preference changes
  const off = () => {
    if (fine.matches && !reduce.matches) return;
    ac.abort();
    cancelAnimationFrame(raf);
    if (nudged) nudged.style.translate = '';
    fx.classList.remove('is-on');
    fx.hidden = true;
  };
  fine.addEventListener('change', off, { signal: ac.signal });
  reduce.addEventListener('change', off, { signal: ac.signal });
}
```

## Notes

- **Install:** put the `.cursor-fx` markup once, last in `<body>`, outside any element with `transform`, `filter`, `opacity` or `isolation`, so the difference blend reaches the page. Then load the module. Mark elements with `data-cursor="View"` (any short word, e.g. "Drag" or "Play") for a label, and with `data-cursor-magnet` for magnetic calls to action. Magnets move with the `translate` property, so their own `transform` hovers keep working.
- It only switches on for `(hover: hover) and (pointer: fine)` without reduced motion, and it hands back to the system cursor if either changes. Touch, pen and keyboard users get the native behaviour, and the system cursor is only hidden (through `html:has(.cursor-fx.is-on)`) while the script is running. Without JS nothing changes.
- The cursor is decorative (`aria-hidden`, `pointer-events: none`) and never touches focus styles. It hides when the pointer leaves the window and over text fields, which keep their I-beam. It also hides inside open dialogs and popovers, which sit in the top layer above it, so the native cursor takes over there.
- Contrast: the ring and dot use `mix-blend-mode: difference` with `--text-inverse`, so they invert whatever is beneath (dark on light, light on dark). The label pill puts `--text-inverse` on a primary-to-deep-teal gradient (≥ 5.2:1). The dark card's muted copy is ≥ 5:1 over its glow.
- Motion runs in one rAF loop that sleeps once the ring settles. Tune the feel with the spring numbers in `frame()`: stiffness `0.14` and damping `0.72` for the ring, and the `0.35`/`0.22` pull factors for magnets.
