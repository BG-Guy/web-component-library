# Aurora Hero

Dark, cinematic hero. Slow-drifting aurora light and a fading grid sit behind a headline that rises word by word out of a blur. An announcement pill has a light tracing its border, and a glass dashboard card floats on the right, tilting towards the cursor while a notification slides in. Depends on `tokens/variables.css`.

**Motion:** aurora drift (18–26s loops) · cursor spotlight · word-by-word blur rise (`--dur-5`, staggered) · conic border sweep · card float + pointer tilt · chart bars grow · toast springs in. A pause button stops all looping motion.

## HTML

```html
<section class="aurora-hero" aria-labelledby="aurora-title" data-aurora-hero>
  <div class="aurora-hero__sky" aria-hidden="true">
    <span class="aurora-hero__blob aurora-hero__blob--1"></span>
    <span class="aurora-hero__blob aurora-hero__blob--2"></span>
    <span class="aurora-hero__blob aurora-hero__blob--3"></span>
    <span class="aurora-hero__grid"></span>
  </div>

  <div class="aurora-hero__inner">
    <div class="aurora-hero__copy">
      <a class="aurora-hero__pill" href="#emergency" style="--i: 0">
        <span class="aurora-hero__pill-tag">New</span>
        24/7 emergency callouts in Springfield
        <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </a>
      <h1 id="aurora-title" class="aurora-hero__title">
        <span class="aurora-hero__line"><span class="aurora-hero__word" style="--i: 1">Home</span> <span class="aurora-hero__word" style="--i: 2">repairs,</span></span>
        <span class="aurora-hero__line"><span class="aurora-hero__word aurora-hero__word--glow" style="--i: 3">done</span> <span class="aurora-hero__word aurora-hero__word--glow" style="--i: 4">right.</span></span>
      </h1>
      <p class="aurora-hero__lead" style="--i: 5">Licensed pros, upfront flat-rate pricing and live arrival tracking. Book a visit in under a minute.</p>
      <div class="aurora-hero__actions" style="--i: 6">
        <a class="aurora-hero__btn aurora-hero__btn--primary" href="#quote">
          Get a free quote
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="aurora-hero__btn aurora-hero__btn--ghost" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          (555) 555-0123
        </a>
      </div>
      <div class="aurora-hero__proof" style="--i: 7">
        <span class="aurora-hero__faces" aria-hidden="true"><span>JM</span><span>AK</span><span>RS</span><span>+</span></span>
        <p><strong>4.9/5</strong> from 1,200+ Springfield homeowners</p>
      </div>
    </div>

    <div class="aurora-hero__stage" aria-hidden="true">
      <div class="aurora-hero__card">
        <div class="aurora-hero__card-head">
          <span>Today</span>
          <span class="aurora-hero__live"><span class="aurora-hero__live-dot"></span>Live</span>
        </div>
        <p class="aurora-hero__metric">$2,480 <small>booked today · +18%</small></p>
        <div class="aurora-hero__chart">
          <span style="--h: 34%; --i: 0"></span><span style="--h: 52%; --i: 1"></span><span style="--h: 41%; --i: 2"></span>
          <span style="--h: 66%; --i: 3"></span><span style="--h: 58%; --i: 4"></span><span style="--h: 80%; --i: 5"></span>
          <span style="--h: 72%; --i: 6"></span><span style="--h: 96%; --i: 7"></span>
        </div>
        <ul class="aurora-hero__jobs">
          <li><span class="aurora-hero__avatar">MR</span><span class="aurora-hero__job"><strong>Water heater install</strong><small>09:00 · Maria R.</small></span><span class="aurora-hero__status aurora-hero__status--done">Done</span></li>
          <li><span class="aurora-hero__avatar">SK</span><span class="aurora-hero__job"><strong>Leak repair</strong><small>11:30 · Sam K.</small></span><span class="aurora-hero__status aurora-hero__status--live">En route</span></li>
          <li><span class="aurora-hero__avatar">JP</span><span class="aurora-hero__job"><strong>Annual inspection</strong><small>14:00 · Jo P.</small></span><span class="aurora-hero__status">Booked</span></li>
        </ul>
      </div>
      <div class="aurora-hero__toast">
        <span class="aurora-hero__toast-icon"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m5 12 5 5L20 7" /></svg></span>
        <span><strong>Technician arriving</strong><small>Sam · 12 min away</small></span>
      </div>
    </div>
  </div>

  <button class="aurora-hero__pause" type="button" aria-pressed="false" hidden>
    <span class="aurora-hero__sr">Pause background animation</span>
    <svg class="aurora-hero__icon-pause" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
    <svg class="aurora-hero__icon-play" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
  </button>
</section>
```

## CSS

```css
@property --aurora-hero-angle { syntax: "<angle>"; inherits: false; initial-value: 0deg; }

/* Section and sky */
.aurora-hero {
  position: relative; isolation: isolate; overflow: clip;
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}
.aurora-hero__sky { position: absolute; inset: 0; z-index: -1; pointer-events: none; }
.aurora-hero__blob {
  position: absolute; width: 70vmax; aspect-ratio: 1; border-radius: 50%; opacity: 0.6;
  animation: aurora-drift 18s var(--ease-in-out) infinite alternate;
}
.aurora-hero__blob--1 { top: -45vmax; left: -20vmax; background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 85%, transparent), transparent); }
.aurora-hero__blob--2 { top: -40vmax; right: -30vmax; background: radial-gradient(closest-side, color-mix(in srgb, var(--primary-2) 75%, transparent), transparent); animation-duration: 22s; animation-delay: -7s; }
.aurora-hero__blob--3 { bottom: -50vmax; left: 15%; opacity: 0.35; background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 60%, var(--primary-2)), transparent); animation-duration: 26s; animation-delay: -13s; }
.aurora-hero__grid {
  position: absolute; inset: 0;
  background-image: linear-gradient(var(--border-inverse) 1px, transparent 1px), linear-gradient(90deg, var(--border-inverse) 1px, transparent 1px);
  background-size: 56px 56px;
  -webkit-mask-image: radial-gradient(ellipse 70% 60% at 50% 20%, black, transparent 75%);
  mask-image: radial-gradient(ellipse 70% 60% at 50% 20%, black, transparent 75%);
}
/* Cursor spotlight */
.aurora-hero__sky::after {
  content: ""; position: absolute; inset: 0; opacity: var(--aurora-spot, 0); transition: opacity var(--dur-5);
  background: radial-gradient(32rem circle at var(--aurora-mx, 50%) var(--aurora-my, 20%), color-mix(in srgb, var(--primary-2) 16%, transparent), transparent 65%);
}

/* Layout */
.aurora-hero__inner {
  display: grid; gap: 3.5rem; align-items: center;
  max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4.5rem, 10vw, 8rem) var(--gutter) clamp(4.5rem, 9vw, 7rem);
}

/* Entrance: everything in the copy column rises out of a blur, in order */
.aurora-hero__pill, .aurora-hero__word, .aurora-hero__lead, .aurora-hero__actions, .aurora-hero__proof {
  animation: aurora-rise var(--dur-5) var(--ease-out) calc(var(--i, 0) * 90ms + 100ms) both;
}

/* Announcement pill with a light travelling round its border */
.aurora-hero__pill {
  display: inline-flex; align-items: center; gap: 0.625rem; max-width: 100%;
  padding: 0.3125rem 0.875rem 0.3125rem 0.3125rem; border: 1px solid transparent; border-radius: 999px;
  background:
    linear-gradient(color-mix(in srgb, var(--surface-deep) 85%, transparent), color-mix(in srgb, var(--surface-deep) 85%, transparent)) padding-box,
    conic-gradient(from var(--aurora-hero-angle), var(--border-inverse) 0 55%, var(--primary-2) 72%, var(--primary) 82%, var(--border-inverse) 95%) border-box;
  color: var(--text-inverse-muted); font-size: 0.875rem; text-decoration: none;
  animation: aurora-rise var(--dur-5) var(--ease-out) 100ms both, aurora-spin 5s linear infinite;
  transition: color var(--dur-2);
}
.aurora-hero__pill:hover { color: var(--text-inverse); }
.aurora-hero__pill svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.aurora-hero__pill:hover svg { transform: translateX(3px); }
.aurora-hero__pill-tag { flex: none; padding: 0.125rem 0.5rem; border-radius: 999px; background: var(--gradient-brand); color: var(--text-inverse); font-size: 0.75rem; font-weight: 600; }

/* Headline */
.aurora-hero__title {
  margin: 1.5rem 0 0; font: 600 clamp(2.75rem, 1.4rem + 5.6vw, 5.75rem)/0.98 var(--font-display);
  letter-spacing: var(--tracking-display);
}
.aurora-hero__line { display: block; }
.aurora-hero__word { display: inline-block; }
.aurora-hero__word--glow {
  padding-bottom: 0.08em;
  background: linear-gradient(100deg, var(--text-inverse) 5%, color-mix(in srgb, var(--primary) 45%, var(--text-inverse)) 45%, color-mix(in srgb, var(--primary-2) 80%, var(--text-inverse)) 95%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.aurora-hero__lead {
  max-width: 34rem; margin: 1.5rem 0 0; color: var(--text-inverse-muted);
  font-size: clamp(1.0625rem, 1rem + 0.4vw, 1.25rem); line-height: 1.6;
}

/* Buttons */
.aurora-hero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2.25rem; }
.aurora-hero__btn {
  position: relative; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
  height: 3rem; padding: 0 1.375rem; border-radius: 999px; overflow: hidden;
  font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-2) var(--ease-out), box-shadow var(--dur-3), background-color var(--dur-2);
}
.aurora-hero__btn svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.aurora-hero__btn:hover { transform: translateY(-1px); }
.aurora-hero__btn:active { transform: scale(0.97); }
.aurora-hero__btn--primary {
  background: var(--surface-light); color: var(--text-main);
  box-shadow: 0 12px 40px -12px color-mix(in srgb, var(--primary) 90%, transparent);
}
.aurora-hero__btn--primary:hover { box-shadow: 0 16px 48px -10px color-mix(in srgb, var(--primary-2) 90%, transparent); }
.aurora-hero__btn--primary:hover svg { transform: translateX(3px); }
.aurora-hero__btn--primary::after { /* shine sweep */
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(110deg, transparent 35%, color-mix(in srgb, var(--primary) 16%, transparent) 50%, transparent 65%);
  transform: translateX(-110%); transition: transform var(--dur-5) var(--ease-out);
}
.aurora-hero__btn--primary:hover::after { transform: translateX(110%); }
.aurora-hero__btn--ghost { background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.aurora-hero__btn--ghost:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.aurora-hero :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Social proof */
.aurora-hero__proof { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem; margin-top: 2rem; color: var(--text-inverse-muted); font-size: 0.875rem; }
.aurora-hero__proof p { margin: 0; }
.aurora-hero__proof strong { color: var(--text-inverse); }
.aurora-hero__faces { display: flex; }
.aurora-hero__faces span {
  display: grid; place-items: center; width: 2rem; height: 2rem; margin-left: -0.5rem; border-radius: 50%;
  border: 2px solid var(--surface-deep); background: var(--gradient-brand); color: var(--text-inverse);
  font-size: 0.6875rem; font-weight: 700;
}
.aurora-hero__faces span:first-child { margin-left: 0; }
.aurora-hero__faces span:nth-child(2) { background: linear-gradient(135deg, var(--primary-2), color-mix(in srgb, var(--primary-2) 50%, var(--surface-deep))); }
.aurora-hero__faces span:nth-child(3) { background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 40%, var(--primary))); color: var(--text-main); }
.aurora-hero__faces span:last-child { background: var(--glass-inverse); color: var(--text-inverse-muted); }

/* Dashboard card: floats, tilts towards the pointer */
.aurora-hero__stage { position: relative; perspective: 1200px; max-width: 28rem; width: 100%; margin-inline: auto; }
.aurora-hero__card {
  padding: 1.25rem; border-radius: var(--radius-2xl);
  background: color-mix(in srgb, var(--surface-deep) 55%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 40px 80px -24px color-mix(in srgb, var(--surface-deep) 95%, transparent);
  transform: rotateX(var(--aurora-rx, 0deg)) rotateY(var(--aurora-ry, 0deg));
  transition: transform var(--dur-4) var(--ease-out);
  animation: aurora-card-in var(--dur-5) var(--ease-out) 450ms both, aurora-float 7s var(--ease-in-out) 1.4s infinite alternate;
}
@supports (backdrop-filter: blur(1px)) {
  .aurora-hero__card { background: var(--glass-inverse); backdrop-filter: blur(var(--blur-md)) saturate(1.4); }
}
.aurora-hero__card-head { display: flex; justify-content: space-between; align-items: center; color: var(--text-inverse-muted); font-size: 0.8125rem; font-weight: 500; }
.aurora-hero__live { display: inline-flex; align-items: center; gap: 0.375rem; padding: 0.1875rem 0.5rem; border-radius: 999px; background: color-mix(in srgb, var(--success) 22%, transparent); color: var(--text-inverse); font-size: 0.75rem; }
.aurora-hero__live-dot { position: relative; width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--success); }
.aurora-hero__live-dot::after { content: ""; position: absolute; inset: 0; border-radius: 50%; background: var(--success); animation: aurora-ping 1.6s var(--ease-out) infinite; }
.aurora-hero__metric { margin: 0.75rem 0 0; font: 600 2rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.aurora-hero__metric small { display: block; margin-top: 0.375rem; color: var(--text-inverse-muted); font: 500 0.8125rem var(--font-sans); letter-spacing: 0; }

/* Mini chart: bars grow in, the last one glows */
.aurora-hero__chart { display: flex; align-items: flex-end; gap: 0.375rem; height: 5.5rem; margin-top: 1.25rem; }
.aurora-hero__chart span {
  flex: 1; height: var(--h); border-radius: 0.375rem 0.375rem 0.125rem 0.125rem; transform-origin: bottom;
  background: linear-gradient(to top, color-mix(in srgb, var(--primary) 35%, transparent), color-mix(in srgb, var(--primary-2) 70%, transparent));
  animation: aurora-bar var(--dur-5) var(--ease-out) calc(var(--i) * 70ms + 700ms) both;
}
.aurora-hero__chart span:last-child { background: var(--gradient-brand); box-shadow: 0 0 24px -4px color-mix(in srgb, var(--primary-2) 80%, transparent); }

/* Jobs list */
.aurora-hero__jobs { display: grid; gap: 0.5rem; margin: 1.25rem 0 0; padding: 0; list-style: none; }
.aurora-hero__jobs li { display: flex; align-items: center; gap: 0.75rem; padding: 0.625rem; border-radius: 0.875rem; background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); }
.aurora-hero__avatar { flex: none; display: grid; place-items: center; width: 2rem; height: 2rem; border-radius: 0.625rem; background: var(--gradient-brand); font-size: 0.6875rem; font-weight: 700; }
.aurora-hero__jobs li:nth-child(2) .aurora-hero__avatar { background: linear-gradient(135deg, var(--primary-2), var(--primary)); }
.aurora-hero__jobs li:nth-child(3) .aurora-hero__avatar { background: linear-gradient(135deg, var(--accent), var(--primary-2)); color: var(--text-main); }
.aurora-hero__job { flex: 1; min-width: 0; }
.aurora-hero__job strong { display: block; overflow: hidden; font-size: 0.875rem; font-weight: 600; white-space: nowrap; text-overflow: ellipsis; }
.aurora-hero__job small { color: var(--text-inverse-muted); font-size: 0.75rem; }
.aurora-hero__status { flex: none; padding: 0.1875rem 0.5rem; border-radius: 999px; background: var(--glass-inverse); color: var(--text-inverse-muted); font-size: 0.6875rem; font-weight: 600; }
.aurora-hero__status--done { background: color-mix(in srgb, var(--success) 25%, transparent); color: var(--text-inverse); }
.aurora-hero__status--live { background: color-mix(in srgb, var(--primary) 35%, transparent); color: var(--text-inverse); }

/* Notification that springs in over the card */
.aurora-hero__toast {
  position: absolute; left: -0.5rem; bottom: -1.5rem; display: flex; align-items: center; gap: 0.75rem;
  padding: 0.75rem 1rem 0.75rem 0.75rem; border-radius: 1rem;
  background: var(--surface-light); color: var(--text-main); box-shadow: var(--shadow-xl);
  animation: aurora-toast-in var(--dur-4) var(--ease-spring) 1.6s both;
}
.aurora-hero__toast strong { display: block; font-size: 0.875rem; }
.aurora-hero__toast small { color: var(--text-muted); font-size: 0.75rem; }
.aurora-hero__toast-icon { display: grid; place-items: center; width: 2rem; height: 2rem; border-radius: 50%; background: var(--success); color: var(--surface-light); }
.aurora-hero__toast-icon svg { fill: none; stroke: currentColor; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }

/* Pause control */
.aurora-hero__pause {
  position: absolute; right: var(--gutter); bottom: 1rem; display: grid; place-items: center;
  width: 2.25rem; height: 2.25rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse-muted); box-shadow: inset 0 0 0 1px var(--border-inverse);
  transition: color var(--dur-2), background-color var(--dur-2);
}
.aurora-hero__pause:hover { color: var(--text-inverse); background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.aurora-hero__pause[hidden] { display: none; }
.aurora-hero__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.aurora-hero__icon-play, .aurora-hero__pause[aria-pressed="true"] .aurora-hero__icon-pause { display: none; }
.aurora-hero__pause[aria-pressed="true"] .aurora-hero__icon-play { display: block; }
.aurora-hero__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Paused or off-screen: freeze every loop */
.aurora-hero[data-paused] *, .aurora-hero[data-paused] *::before, .aurora-hero[data-paused] *::after,
.aurora-hero[data-offscreen] *, .aurora-hero[data-offscreen] *::before, .aurora-hero[data-offscreen] *::after { animation-play-state: paused !important; }

@media (min-width: 1024px) {
  .aurora-hero__inner { grid-template-columns: 1.15fr 0.85fr; gap: 4rem; }
  .aurora-hero__toast { left: -2.5rem; }
}
@media (prefers-reduced-motion: reduce) {
  .aurora-hero *, .aurora-hero *::before, .aurora-hero *::after { animation: none !important; }
}

@keyframes aurora-drift {
  0% { transform: translate3d(0, 0, 0) scale(1); }
  50% { transform: translate3d(8%, 6%, 0) scale(1.12); }
  100% { transform: translate3d(-6%, 10%, 0) scale(0.94); }
}
@keyframes aurora-spin { to { --aurora-hero-angle: 360deg; } }
@keyframes aurora-rise { from { opacity: 0; transform: translateY(0.45em); filter: blur(10px); } }
@keyframes aurora-card-in { from { opacity: 0; scale: 0.94; filter: blur(8px); } }
@keyframes aurora-float { to { translate: 0 -10px; } }
@keyframes aurora-bar { from { transform: scaleY(0.06); } }
@keyframes aurora-toast-in { from { opacity: 0; transform: translate(-12px, 16px) scale(0.9); } }
@keyframes aurora-ping { to { transform: scale(2.6); opacity: 0; } }
```

## JS

```js
document.querySelectorAll('[data-aurora-hero]').forEach((hero) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const card = hero.querySelector('.aurora-hero__card');
  const pause = hero.querySelector('.aurora-hero__pause');

  // Pause control for the looping light (WCAG 2.2.2); hidden when motion is already off
  pause.hidden = reduce.matches;
  pause.addEventListener('click', () => {
    pause.setAttribute('aria-pressed', String(hero.toggleAttribute('data-paused')));
  });

  // Save battery: freeze loops while the hero is off screen
  new IntersectionObserver(([entry]) => hero.toggleAttribute('data-offscreen', !entry.isIntersecting)).observe(hero);

  // Cursor spotlight and card tilt (mouse only), throttled to one update per frame
  let frame = 0;
  hero.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse' || reduce.matches || frame) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      const r = hero.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width;
      const y = (e.clientY - r.top) / r.height;
      hero.style.setProperty('--aurora-mx', `${x * 100}%`);
      hero.style.setProperty('--aurora-my', `${y * 100}%`);
      hero.style.setProperty('--aurora-spot', '1');
      card.style.setProperty('--aurora-ry', `${(x - 0.5) * 10}deg`);
      card.style.setProperty('--aurora-rx', `${(0.5 - y) * 8}deg`);
    });
  });
  hero.addEventListener('pointerleave', () => {
    hero.style.setProperty('--aurora-spot', '0');
    card.style.setProperty('--aurora-rx', '0deg');
    card.style.setProperty('--aurora-ry', '0deg');
  });
});
```

## Notes

- Everything animates with CSS on load; JS only adds the spotlight, the tilt and the pause button. Without JS the hero still animates in and reads completely.
- The dashboard is decorative (`aria-hidden`); swap it for a product shot or photo inside `.aurora-hero__stage` and keep the float.
- Text contrast: the headline gradient stays above 4.5:1 on `--surface-deep` at every point, and body copy uses `--text-inverse-muted` (7:1).
- The light behind the grid comes from large radial gradients, not `filter: blur()`, so it stays cheap on the GPU. Loops freeze when the hero scrolls out of view.
- Use one `<h1>` per page. In a sub-page hero, keep the same layout with a shorter title and drop the stage.
