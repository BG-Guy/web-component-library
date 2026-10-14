# Velocity Marquee

Three oversized rows of trade names drift in alternating directions across a deep surface: one outlined, one in brand-gradient type, one strung with rounded photo pills, with inline SVG sparkles between the words. The signature: scroll and the rows pick up speed with your velocity, lean into it with a skew that eases back to rest, and swing round whenever you change scroll direction (the reversal eases through zero rather than snapping). On phones the type steps down and the edge fade narrows so more of each word shows; the loop runs only while the section is on screen and has a pause button. Depends on `tokens/variables.css`.

**Motion:** one rAF loop: base drift plus a smoothed scroll-velocity boost, heading eased through zero on reversal, per-row `skewX` proportional to velocity that decays to rest, sparkles turning with distance travelled · boost meter and heading arrow scrub with the loop (linear) · `--ease-spring` press on buttons · intro hint bobs three times (`--ease-in-out`, under 5s). Pause button + off-screen freeze.

## HTML

```html
<div class="velo-marquee-demo">
  <p class="velo-marquee-demo__copy">Five trades, one Springfield team.</p>
  <p class="velo-marquee-demo__hint">Scroll, then flick
    <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
  </p>
</div>

<section class="velo-marquee" aria-labelledby="velo-marquee-title" data-velo-marquee>
  <div class="velo-marquee__inner velo-marquee__head">
    <div>
      <p class="velo-marquee__eyebrow"><span class="velo-marquee__dot" aria-hidden="true"></span>Licensed in five trades</p>
      <h2 id="velo-marquee-title" class="velo-marquee__title">One call. <span class="velo-marquee__glow">Every trade.</span></h2>
    </div>
    <div class="velo-marquee__aside">
      <p class="velo-marquee__lead">From a dripping tap to a rooftop array, our own specialists cover it, dispatched from one Springfield team since 1998.</p>
      <a class="velo-marquee__link" href="#services">
        Explore services
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </a>
    </div>
  </div>

  <!-- The rows below repeat these five trades three times, so assistive tech gets them once, here -->
  <ul class="velo-marquee__sr" role="list" aria-label="Our trades">
    <li>Plumbing</li><li>Electrical</li><li>HVAC</li><li>Roofing</li><li>Solar</li>
  </ul>

  <div class="velo-marquee__rows" aria-hidden="true">
    <div class="velo-marquee__row velo-marquee__row--outline" data-speed="0.8">
      <div class="velo-marquee__track">
        <span class="velo-marquee__group">Plumbing<svg class="velo-marquee__spark" viewBox="0 0 24 24" focusable="false"><path d="M12 2c.7 5.3 4.7 9.3 10 10-5.3.7-9.3 4.7-10 10-.7-5.3-4.7-9.3-10-10 5.3-.7 9.3-4.7 10-10z" /></svg>Electrical<svg class="velo-marquee__spark" viewBox="0 0 24 24" focusable="false"><path d="M12 2c.7 5.3 4.7 9.3 10 10-5.3.7-9.3 4.7-10 10-.7-5.3-4.7-9.3-10-10 5.3-.7 9.3-4.7 10-10z" /></svg>HVAC<svg class="velo-marquee__spark" viewBox="0 0 24 24" focusable="false"><path d="M12 2c.7 5.3 4.7 9.3 10 10-5.3.7-9.3 4.7-10 10-.7-5.3-4.7-9.3-10-10 5.3-.7 9.3-4.7 10-10z" /></svg>Roofing<svg class="velo-marquee__spark" viewBox="0 0 24 24" focusable="false"><path d="M12 2c.7 5.3 4.7 9.3 10 10-5.3.7-9.3 4.7-10 10-.7-5.3-4.7-9.3-10-10 5.3-.7 9.3-4.7 10-10z" /></svg>Solar<svg class="velo-marquee__spark" viewBox="0 0 24 24" focusable="false"><path d="M12 2c.7 5.3 4.7 9.3 10 10-5.3.7-9.3 4.7-10 10-.7-5.3-4.7-9.3-10-10 5.3-.7 9.3-4.7 10-10z" /></svg></span>
      </div>
    </div>
    <div class="velo-marquee__row velo-marquee__row--gradient" data-speed="1.15">
      <div class="velo-marquee__track">
        <span class="velo-marquee__group">Roofing<svg class="velo-marquee__spark" viewBox="0 0 24 24" focusable="false"><path d="M12 2c.7 5.3 4.7 9.3 10 10-5.3.7-9.3 4.7-10 10-.7-5.3-4.7-9.3-10-10 5.3-.7 9.3-4.7 10-10z" /></svg>Solar<svg class="velo-marquee__spark" viewBox="0 0 24 24" focusable="false"><path d="M12 2c.7 5.3 4.7 9.3 10 10-5.3.7-9.3 4.7-10 10-.7-5.3-4.7-9.3-10-10 5.3-.7 9.3-4.7 10-10z" /></svg>Plumbing<svg class="velo-marquee__spark" viewBox="0 0 24 24" focusable="false"><path d="M12 2c.7 5.3 4.7 9.3 10 10-5.3.7-9.3 4.7-10 10-.7-5.3-4.7-9.3-10-10 5.3-.7 9.3-4.7 10-10z" /></svg>Electrical<svg class="velo-marquee__spark" viewBox="0 0 24 24" focusable="false"><path d="M12 2c.7 5.3 4.7 9.3 10 10-5.3.7-9.3 4.7-10 10-.7-5.3-4.7-9.3-10-10 5.3-.7 9.3-4.7 10-10z" /></svg>HVAC<svg class="velo-marquee__spark" viewBox="0 0 24 24" focusable="false"><path d="M12 2c.7 5.3 4.7 9.3 10 10-5.3.7-9.3 4.7-10 10-.7-5.3-4.7-9.3-10-10 5.3-.7 9.3-4.7 10-10z" /></svg></span>
      </div>
    </div>
    <div class="velo-marquee__row velo-marquee__row--pills" data-speed="0.95">
      <div class="velo-marquee__track">
        <span class="velo-marquee__group">HVAC<span class="velo-marquee__pill"><img src="hvac.jpg" width="176" height="72" alt="" loading="lazy" decoding="async"></span>Roofing<span class="velo-marquee__pill"><img src="roofing.jpg" width="176" height="72" alt="" loading="lazy" decoding="async"></span>Solar<span class="velo-marquee__pill"><img src="solar.jpg" width="176" height="72" alt="" loading="lazy" decoding="async"></span>Plumbing<span class="velo-marquee__pill"><img src="plumbing.jpg" width="176" height="72" alt="" loading="lazy" decoding="async"></span>Electrical<span class="velo-marquee__pill"><img src="electrical.jpg" width="176" height="72" alt="" loading="lazy" decoding="async"></span></span>
      </div>
    </div>
  </div>

  <div class="velo-marquee__inner velo-marquee__foot">
    <div class="velo-marquee__meter" aria-hidden="true" hidden>
      <svg class="velo-marquee__heading" viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      <span class="velo-marquee__bars">
        <span style="--velo-marquee-i: 0"></span><span style="--velo-marquee-i: 1"></span><span style="--velo-marquee-i: 2"></span><span style="--velo-marquee-i: 3"></span><span style="--velo-marquee-i: 4"></span><span style="--velo-marquee-i: 5"></span><span style="--velo-marquee-i: 6"></span>
      </span>
      <span>Scroll to boost</span>
    </div>
    <button class="velo-marquee__pause" type="button" aria-pressed="false" hidden>
      <span class="velo-marquee__sr">Pause animation</span>
      <svg class="velo-marquee__icon-pause" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><rect x="6" y="5" width="4" height="14" rx="1" /><rect x="14" y="5" width="4" height="14" rx="1" /></svg>
      <svg class="velo-marquee__icon-play" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M8 5.5v13a1 1 0 0 0 1.5.9l10-6.5a1 1 0 0 0 0-1.7l-10-6.5A1 1 0 0 0 8 5.5z" /></svg>
    </button>
  </div>
</section>

<div class="velo-marquee-demo">
  <p class="velo-marquee-demo__copy">Now scroll back up.</p>
  <p class="velo-marquee-demo__hint">The rows turn round with you</p>
</div>
```

## CSS

```css
/* Demo scroll room above and below */
.velo-marquee-demo {
  display: grid; place-content: center; justify-items: center; gap: 0.875rem; min-height: 70vh; padding: 3rem var(--gutter);
  background: var(--surface-deep); color: var(--text-inverse-muted); font-family: var(--font-sans); text-align: center;
}
.velo-marquee-demo__copy { margin: 0; color: var(--text-inverse); font: 600 clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.velo-marquee-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.velo-marquee-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: velo-marquee-bob 1.4s var(--ease-in-out) 600ms 3; }

/* Section: deep surface, two pools of brand light behind the rows */
.velo-marquee {
  --velo-marquee-fade: 7%;
  position: relative; isolation: isolate; overflow: clip;
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}
.velo-marquee::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background:
    radial-gradient(55% 40% at 28% 62%, color-mix(in srgb, var(--primary) 24%, transparent), transparent 70%),
    radial-gradient(45% 36% at 80% 72%, color-mix(in srgb, var(--primary-2) 18%, transparent), transparent 70%);
}
.velo-marquee__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }

/* Heading block */
.velo-marquee__head { display: grid; gap: 1.5rem; padding-top: clamp(3.5rem, 8vw, 6rem); }
.velo-marquee__eyebrow { display: flex; align-items: center; gap: 0.625rem; margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.velo-marquee__dot { flex: none; width: 0.5rem; height: 0.5rem; border-radius: var(--radius-full); background: var(--gradient-brand); box-shadow: 0 0 0.75rem color-mix(in srgb, var(--primary-2) 80%, transparent); }
.velo-marquee__title { margin: 0.875rem 0 0; font: 600 clamp(2.125rem, 1.4rem + 2.8vw, 3.5rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.velo-marquee__glow {
  background: linear-gradient(100deg, color-mix(in srgb, var(--primary) 55%, var(--text-inverse)), color-mix(in srgb, var(--primary-2) 70%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.velo-marquee__aside { display: grid; justify-items: start; gap: 1.25rem; }
.velo-marquee__lead { max-width: 30rem; margin: 0; color: var(--text-inverse-muted); font-size: 1.0625rem; line-height: 1.6; }
.velo-marquee__link {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.125rem; border-radius: var(--radius-full);
  background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: background-color var(--dur-2) var(--ease-out), transform var(--dur-3) var(--ease-spring);
}
.velo-marquee__link:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.velo-marquee__link:active { transform: scale(0.97); }
.velo-marquee__link svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.velo-marquee__link:hover svg { transform: translateX(3px); }
.velo-marquee :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Rows: full-bleed, ruled like a type specimen, faded at both edges */
.velo-marquee__rows {
  display: grid; margin-block: clamp(2.5rem, 6vw, 4.5rem) clamp(1.5rem, 3vw, 2.5rem); overflow: clip;
  font-family: var(--font-display); font-weight: 600; line-height: 1; letter-spacing: var(--tracking-display);
  -webkit-mask-image: linear-gradient(90deg, transparent, black var(--velo-marquee-fade), black calc(100% - var(--velo-marquee-fade)), transparent);
  mask-image: linear-gradient(90deg, transparent, black var(--velo-marquee-fade), black calc(100% - var(--velo-marquee-fade)), transparent);
}
.velo-marquee__row {
  display: flex; padding-block: 0.1em 0.14em; border-top: 1px solid var(--border-inverse); white-space: nowrap;
  transform: skewX(var(--velo-marquee-skew, 0deg));
}
.velo-marquee__row:last-child { border-bottom: 1px solid var(--border-inverse); }
.velo-marquee__track { display: flex; flex: none; will-change: transform; }
.velo-marquee__group { display: flex; flex: none; align-items: center; gap: 0.3em; padding-right: 0.3em; }
.velo-marquee__spark { flex: none; width: 0.4em; height: 0.4em; rotate: var(--velo-marquee-spin, 0deg); }

/* Row 1: outlined type with outlined teal sparkles */
.velo-marquee__row--outline { font-size: clamp(2.75rem, 1.2rem + 7vw, 7.5rem); color: color-mix(in srgb, var(--text-inverse) 55%, transparent); }
.velo-marquee__row--outline .velo-marquee__spark { fill: none; stroke: color-mix(in srgb, var(--primary-2) 75%, var(--text-inverse)); stroke-width: 1.25; stroke-linejoin: round; }
@supports (-webkit-text-stroke: 1px) {
  .velo-marquee__row--outline { color: transparent; -webkit-text-stroke: 1.5px color-mix(in srgb, var(--text-inverse) 62%, transparent); }
}

/* Row 2: brand-gradient type; each copy carries the full gradient, so the wrap is seamless */
.velo-marquee__row--gradient { font-size: clamp(3.25rem, 1.3rem + 8.5vw, 9rem); }
.velo-marquee__row--gradient .velo-marquee__group {
  background: linear-gradient(90deg, color-mix(in srgb, var(--primary) 55%, var(--text-inverse)), color-mix(in srgb, var(--primary-2) 70%, var(--text-inverse)) 50%, color-mix(in srgb, var(--primary) 55%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.velo-marquee__row--gradient .velo-marquee__spark { fill: color-mix(in srgb, var(--accent) 85%, var(--text-inverse)); }

/* Row 3: solid type strung with rounded photo pills (gradient chips until the photos load) */
.velo-marquee__row--pills { font-size: clamp(2.5rem, 1.1rem + 6vw, 6.75rem); color: var(--text-inverse); }
.velo-marquee__pill {
  flex: none; width: 1.9em; height: 0.78em; border-radius: var(--radius-full); overflow: hidden;
  background: var(--gradient-brand); outline: 1px solid var(--border-inverse); outline-offset: -1px;
  box-shadow: 0 0.15em 0.45em -0.2em color-mix(in srgb, var(--primary) 70%, transparent);
}
.velo-marquee__pill:nth-child(3n+2) { background: linear-gradient(135deg, var(--primary-2), color-mix(in srgb, var(--accent) 55%, var(--primary-2))); }
.velo-marquee__pill:nth-child(3n) { background: linear-gradient(135deg, color-mix(in srgb, var(--accent) 80%, var(--primary)), var(--primary)); }
.velo-marquee__pill img { display: block; width: 100%; height: 100%; object-fit: cover; }

/* Footer: boost meter (heading arrow + bars) and the pause control */
.velo-marquee__foot { display: flex; align-items: center; gap: 1rem; min-height: 2.75rem; padding-bottom: clamp(2.5rem, 6vw, 4rem); }
.velo-marquee__meter { display: inline-flex; align-items: center; gap: 0.75rem; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; transition: opacity var(--dur-3) var(--ease-out); }
.velo-marquee__meter[hidden] { display: none; }
.velo-marquee__heading { flex: none; fill: none; stroke: var(--text-inverse); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; rotate: calc((1 - var(--velo-marquee-heading, 1)) * 90deg); }
.velo-marquee__bars { display: inline-flex; align-items: flex-end; gap: 0.1875rem; height: 1.125rem; }
.velo-marquee__bars span {
  width: 0.1875rem; height: calc(0.375rem + var(--velo-marquee-i) * 0.125rem); border-radius: var(--radius-full);
  background: linear-gradient(to top, var(--primary), color-mix(in srgb, var(--primary-2) 70%, var(--text-inverse)));
  opacity: clamp(0.2, calc(var(--velo-marquee-v, 0) * 6 - var(--velo-marquee-i) + 1), 1);
}
.velo-marquee__pause {
  flex: none; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; margin-left: auto; padding: 0; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse-muted); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: color var(--dur-2) var(--ease-out), background-color var(--dur-2) var(--ease-out), transform var(--dur-3) var(--ease-spring);
}
.velo-marquee__pause:hover { color: var(--text-inverse); background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.velo-marquee__pause:active { transform: scale(0.92); }
.velo-marquee__pause[hidden] { display: none; }
.velo-marquee__pause svg { fill: currentColor; }
.velo-marquee__icon-play, .velo-marquee__pause[aria-pressed="true"] .velo-marquee__icon-pause { display: none; }
.velo-marquee__pause[aria-pressed="true"] .velo-marquee__icon-play { display: block; }
.velo-marquee__sr { position: absolute; width: 1px; height: 1px; margin: 0; padding: 0; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }

/* Paused: the meter dims; any CSS animation added inside freezes too */
.velo-marquee[data-paused] .velo-marquee__meter { opacity: 0.45; }
.velo-marquee[data-paused] *, .velo-marquee[data-paused] *::before, .velo-marquee[data-paused] *::after { animation-play-state: paused !important; }

@media (min-width: 768px) {
  .velo-marquee { --velo-marquee-fade: 14%; }
  .velo-marquee__head { grid-template-columns: 1.1fr 0.9fr; align-items: end; gap: 3rem; }
}
@media (prefers-reduced-motion: reduce) {
  .velo-marquee__row { transform: none; }
  .velo-marquee__spark { rotate: none; }
  .velo-marquee-demo *, .velo-marquee-demo *::before, .velo-marquee-demo *::after { animation: none !important; }
}
@keyframes velo-marquee-bob { 50% { transform: translateY(4px); } }
```

## JS

```js
document.querySelectorAll('[data-velo-marquee]').forEach((root) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const pause = root.querySelector('.velo-marquee__pause');
  const meter = root.querySelector('.velo-marquee__meter');
  const rows = [...root.querySelectorAll('.velo-marquee__row')].map((row, i) => ({
    row,
    track: row.querySelector('.velo-marquee__track'),
    group: row.querySelector('.velo-marquee__group'),
    dir: i % 2 ? -1 : 1,
    speed: Number(row.dataset.speed) || 1,
    x: 0, w: 1, spin: 0,
  }));
  let visible = false, frame = 0, lastT = 0, lastY = 0, vel = 0, heading = 1, target = 1;

  // Clone each group (aria-hidden) until its track can wrap seamlessly at any width
  const measure = () => rows.forEach((r) => {
    const w = r.group.offsetWidth;
    if (!w) return; // not rendered yet: keep the last width, clone nothing
    r.w = w;
    while (r.track.children.length < Math.ceil(r.row.offsetWidth / w) + 1) {
      const copy = r.group.cloneNode(true);
      copy.setAttribute('aria-hidden', 'true');
      r.track.append(copy);
    }
  });

  // One frame: smooth the scroll velocity, ease the heading through zero, then move, skew and spin each row
  const tick = (t) => {
    const dt = lastT ? Math.min(t - lastT, 50) : 16;
    const dy = scrollY - lastY;
    lastT = t;
    lastY = scrollY;
    if (dy) target = Math.sign(dy);
    vel += (dy / dt - vel) * (1 - Math.exp(-dt / 110));
    heading += (target - heading) * (1 - Math.exp(-dt / 240));
    const boost = Math.min(Math.abs(vel), 3) / 3;
    rows.forEach((r) => {
      const step = r.dir * heading * r.speed * (0.05 + boost * 0.85) * dt;
      r.x = (r.x + step) % r.w;
      if (r.x > 0) r.x -= r.w;
      r.spin = (r.spin + step * 0.5) % 90;
      r.track.style.transform = `translate3d(${r.x.toFixed(2)}px, 0, 0)`;
      r.row.style.setProperty('--velo-marquee-skew', `${(Math.max(-3, Math.min(3, vel)) * -r.dir * 3.5).toFixed(2)}deg`);
      r.row.style.setProperty('--velo-marquee-spin', `${r.spin.toFixed(1)}deg`);
    });
    meter.style.setProperty('--velo-marquee-v', boost.toFixed(3));
    meter.style.setProperty('--velo-marquee-heading', heading.toFixed(3));
    frame = requestAnimationFrame(tick);
  };

  // The loop runs only while visible, unpaused and with motion allowed
  const run = () => {
    const on = visible && !reduce.matches && !root.hasAttribute('data-paused');
    if (on && !frame) { lastT = 0; lastY = scrollY; vel = 0; frame = requestAnimationFrame(tick); }
    if (!on && frame) {
      cancelAnimationFrame(frame);
      frame = 0;
      rows.forEach((r) => r.row.style.setProperty('--velo-marquee-skew', '0deg'));
    }
    if (reduce.matches) rows.forEach((r) => { r.x = 0; r.track.style.transform = ''; });
  };
  const sync = () => { pause.hidden = meter.hidden = reduce.matches; run(); };

  // Pause control (WCAG 2.2.2); going off screen freezes the loop without touching its state
  pause.addEventListener('click', () => {
    pause.setAttribute('aria-pressed', String(root.toggleAttribute('data-paused')));
    run();
  });
  new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; run(); }).observe(root);
  new ResizeObserver(measure).observe(root);
  document.fonts?.ready.then(measure);
  reduce.addEventListener('change', sync);
  sync();
});
```

## Notes

- The three rows repeat the same five trades, so they are decorative (`aria-hidden`, pill images `alt=""`) and assistive tech reads the visually hidden "Our trades" list once. The copies JS appends for the wrap-around carry `aria-hidden` too, and nothing in the rows is focusable.
- WCAG 2.2.2: the drift runs indefinitely, so a pause button (`aria-pressed`) stops the rAF loop, and an IntersectionObserver also stops it off screen without changing the button. Under `prefers-reduced-motion` there's no loop, no skew and no sparkle spin: the rows sit still and the pause button and meter stay hidden. Without JS you get the same static rows; each starts on a different trade, so they still read as a composed poster.
- Contrast on `--surface-deep`: gradient row ≥ 7.8:1 at every stop, outline stroke about 6.9:1, pill row and heading `--text-inverse` 18:1, lead `--text-inverse-muted` 7:1. The amber sparkles and photo pills are ornament only.
- Tuning: `data-speed` sets each row's relative pace; in `tick`, `0.05` is the base drift (px/ms), `0.85` the extra speed at full boost, `3.5` the degrees of skew per px/ms of scroll, and the two time constants (110 ms, 240 ms) set how fast velocity and heading settle. `--velo-marquee-fade` sets the edge-fade width.
- Swapping content: change the words in each `.velo-marquee__group` (start each row on a different word), keep one sparkle or pill per word, and update the hidden list to match. Pills fall back to brand-gradient chips when an image is missing.
- Support: `-webkit-text-stroke` works in every current engine, with a translucent solid fill as the fallback. Prefixed and unprefixed `mask-image` are both included; the standalone `rotate` property on the sparkles needs Safari 14.1+.
