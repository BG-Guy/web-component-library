# Premium Buttons

A button set where every interaction gets a response. Combine the base `.pro-btn` with one surface (`--primary`, `--ink`, `--glow`, `--glass`) and any behaviours:

- `--roll`: the label rolls on hover.
- `--arrow`: the arrow badge swaps.
- `--magnetic`: the button drifts towards the cursor.
- `--morph`: loading, then success.
- `--like`: a toggle with a particle burst.

Depends on `tokens/variables.css`.

**Motion:** spring press (scale 0.96) · shine sweep · label roll · arrow swap · magnetic drift · width morph to a spinner, then a drawn check · heart pop with ring + particles · conic border spins while hovered.

## HTML

```html
<div class="pro-btn-demo">
  <div class="pro-btn-demo__row">
    <a class="pro-btn pro-btn--primary" href="#quote">Get a free quote</a>

    <a class="pro-btn pro-btn--ink pro-btn--roll" href="#book">
      <span class="pro-btn__roll"><span class="pro-btn__roll-inner" data-text="Book a visit">Book a visit</span></span>
    </a>

    <a class="pro-btn pro-btn--primary pro-btn--arrow" href="#work">
      See our work
      <span class="pro-btn__badge" aria-hidden="true">
        <svg class="pro-btn__a1" viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        <svg class="pro-btn__a2" viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </span>
    </a>

    <a class="pro-btn pro-btn--ink pro-btn--magnetic" href="tel:+15555550123"><span class="pro-btn__label">Call (555) 555-0123</span></a>

    <span class="pro-btn-demo__group">
      <button class="pro-btn pro-btn--primary pro-btn--morph" type="button" data-pro-btn-morph>
        <span class="pro-btn__label">Confirm booking</span>
        <span class="pro-btn__spinner" aria-hidden="true"></span>
        <span class="pro-btn__done" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg>
          Booked
        </span>
      </button>
      <span class="pro-btn__status" role="status"></span>
    </span>

    <button class="pro-btn pro-btn--like" type="button" aria-pressed="false" data-pro-btn-like>
      <span class="pro-btn__heart" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M12 20.5s-7.5-4.6-9.3-9.2C1.4 7.9 3.6 4.5 7 4.5c2 0 3.6 1.1 5 3 1.4-1.9 3-3 5-3 3.4 0 5.6 3.4 4.3 6.8-1.8 4.6-9.3 9.2-9.3 9.2z" /></svg></span>
      Save
    </button>
  </div>

  <div class="pro-btn-demo__row pro-btn-demo__row--dark">
    <a class="pro-btn pro-btn--glow" href="#emergency">Emergency callout</a>
    <a class="pro-btn pro-btn--glass" href="#pricing">View pricing</a>
    <a class="pro-btn pro-btn--light pro-btn--arrow" href="#quote">
      Start your project
      <span class="pro-btn__badge" aria-hidden="true">
        <svg class="pro-btn__a1" viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        <svg class="pro-btn__a2" viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </span>
    </a>
  </div>
</div>
```

## CSS

```css
@property --pro-btn-angle { syntax: "<angle>"; inherits: false; initial-value: 0deg; }

/* Base: pill, spring press, outline focus that never fights the shadows */
.pro-btn {
  position: relative; isolation: isolate;
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
  height: 2.875rem; padding: 0 1.375rem; border: 0; border-radius: 999px;
  font: 600 0.9375rem/1 var(--font-sans); letter-spacing: -0.005em; white-space: nowrap; text-decoration: none;
  cursor: pointer; -webkit-tap-highlight-color: transparent;
  transition: transform var(--dur-3) var(--ease-spring), translate var(--dur-4) var(--ease-spring),
              box-shadow var(--dur-3) var(--ease-out), background-color var(--dur-2), color var(--dur-2), width var(--dur-4) var(--ease-spring);
}
.pro-btn:hover { transform: translateY(-1px); }
.pro-btn:active { transform: scale(0.96); transition-duration: var(--dur-1); }
.pro-btn:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.pro-btn svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* Primary: lit from above, coloured shadow, shine sweep on hover */
.pro-btn--primary {
  overflow: hidden; color: var(--text-inverse);
  background: linear-gradient(180deg, var(--primary), var(--primary-hover));
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 28%, transparent),
              0 1px 2px color-mix(in srgb, var(--primary-hover) 40%, transparent),
              0 8px 24px -8px color-mix(in srgb, var(--primary) 75%, transparent);
}
.pro-btn--primary:hover { box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 28%, transparent), 0 14px 32px -10px color-mix(in srgb, var(--primary) 90%, transparent); }
.pro-btn--primary::after {
  content: ""; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(110deg, transparent 30%, color-mix(in srgb, var(--surface-light) 30%, transparent) 50%, transparent 70%);
  transform: translateX(-110%); transition: transform var(--dur-5) var(--ease-out);
}
.pro-btn--primary:hover::after { transform: translateX(110%); }

/* Ink and light */
.pro-btn--ink { background: var(--text-main); color: var(--surface-light); box-shadow: var(--highlight-inverse), 0 8px 20px -10px color-mix(in srgb, var(--text-main) 70%, transparent); }
.pro-btn--ink:hover { background: color-mix(in srgb, var(--text-main) 88%, var(--primary)); }
.pro-btn--light { background: var(--surface-light); color: var(--text-main); box-shadow: 0 10px 30px -10px color-mix(in srgb, var(--primary) 80%, transparent); }

/* Glow: conic border that spins only while hovered or focused, with a soft halo */
.pro-btn--glow {
  border: 1.5px solid transparent; color: var(--text-inverse);
  background:
    linear-gradient(var(--surface-deep), var(--surface-deep)) padding-box,
    conic-gradient(from var(--pro-btn-angle), var(--border-inverse) 0 40%, var(--primary-2) 60%, var(--primary) 75%, var(--border-inverse) 90%) border-box;
  animation: pro-btn-spin 3s linear infinite paused;
}
.pro-btn--glow::before {
  content: ""; position: absolute; inset: -3px; z-index: -1; border-radius: inherit; opacity: 0;
  background: conic-gradient(from var(--pro-btn-angle), var(--primary-2), var(--primary), var(--primary-2));
  filter: blur(14px); transition: opacity var(--dur-4) var(--ease-out);
  animation: pro-btn-spin 3s linear infinite paused;
}
.pro-btn--glow:is(:hover, :focus-visible), .pro-btn--glow:is(:hover, :focus-visible)::before { animation-play-state: running; }
.pro-btn--glow:is(:hover, :focus-visible)::before { opacity: 0.5; }

/* Glass, for photos and dark sections */
.pro-btn--glass { color: var(--text-inverse); background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
@supports (backdrop-filter: blur(1px)) { .pro-btn--glass { backdrop-filter: blur(12px) saturate(1.4); } }
.pro-btn--glass:hover { background: color-mix(in srgb, var(--text-inverse) 12%, transparent); }
:is(.pro-btn--glow, .pro-btn--glass):focus-visible { outline-color: var(--text-inverse); }

/* Roll: the label slides up and a copy rolls in from below */
.pro-btn__roll { display: block; height: 1.25em; overflow: hidden; line-height: 1.25; }
.pro-btn__roll-inner { display: flex; flex-direction: column; transition: transform var(--dur-4) var(--ease-out); }
.pro-btn__roll-inner::after { content: attr(data-text); content: attr(data-text) / ""; }
.pro-btn--roll:hover .pro-btn__roll-inner, .pro-btn--roll:focus-visible .pro-btn__roll-inner { transform: translateY(-50%); }

/* Arrow badge: one arrow flies out, the next flies in */
.pro-btn--arrow { padding-right: 0.4375rem; gap: 0.75rem; }
.pro-btn__badge { position: relative; display: grid; place-items: center; width: 2rem; height: 2rem; overflow: hidden; border-radius: 50%; background: color-mix(in srgb, currentColor 18%, transparent); }
.pro-btn__badge svg { grid-area: 1 / 1; transition: transform var(--dur-4) var(--ease-out); }
.pro-btn__a2 { transform: translateX(-160%); }
.pro-btn--arrow:is(:hover, :focus-visible) .pro-btn__a1 { transform: translateX(160%); }
.pro-btn--arrow:is(:hover, :focus-visible) .pro-btn__a2 { transform: none; }

/* Magnetic: JS feeds the offset, the spring brings it home */
.pro-btn--magnetic { translate: var(--pro-btn-mx, 0px) var(--pro-btn-my, 0px); }
.pro-btn--magnetic:hover { transition-duration: var(--dur-3), var(--dur-2); }
.pro-btn--magnetic .pro-btn__label { display: block; translate: calc(var(--pro-btn-mx, 0px) * 0.35) calc(var(--pro-btn-my, 0px) * 0.35); transition: translate var(--dur-4) var(--ease-spring); }

/* Morph: label → spinner circle → success with a drawn check */
.pro-btn--morph { display: inline-grid; place-items: center; overflow: hidden; }
.pro-btn--morph > * { grid-area: 1 / 1; transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-out), filter var(--dur-3); }
.pro-btn--morph::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--success); opacity: 0; transition: opacity var(--dur-3); }
.pro-btn__spinner { width: 1.125rem; height: 1.125rem; border-radius: 50%; border: 2px solid color-mix(in srgb, currentColor 30%, transparent); border-top-color: currentColor; opacity: 0; transform: scale(0.5); animation: pro-btn-turn 0.7s linear infinite; }
.pro-btn__done { display: inline-flex; align-items: center; gap: 0.375rem; opacity: 0; transform: translateY(8px); }
.pro-btn__done path { stroke-width: 2.5; stroke-dasharray: 1; stroke-dashoffset: 1; transition: stroke-dashoffset var(--dur-4) var(--ease-out) var(--dur-2); }
.pro-btn--morph[data-state] .pro-btn__label { opacity: 0; transform: translateY(-8px); filter: blur(4px); }
.pro-btn--morph[data-state="loading"] { padding: 0; }
.pro-btn--morph[data-state="loading"] .pro-btn__spinner { opacity: 1; transform: none; }
.pro-btn--morph[data-state="success"]::before { opacity: 1; }
.pro-btn--morph[data-state="success"] .pro-btn__done { opacity: 1; transform: none; }
.pro-btn--morph[data-state="success"] .pro-btn__done path { stroke-dashoffset: 0; }
.pro-btn--morph[aria-disabled="true"] { cursor: progress; }
.pro-btn__status { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Like: heart pops, ring bursts, particles scatter */
.pro-btn--like { gap: 0.5rem; padding-left: 1rem; background: var(--surface-light); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm); }
.pro-btn--like:hover { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--danger) 30%, var(--border-subtle)), var(--shadow-md); }
.pro-btn__heart { position: relative; display: grid; place-items: center; color: var(--text-muted); transition: color var(--dur-2); }
.pro-btn__heart svg { transition: fill var(--dur-2); }
.pro-btn--like[aria-pressed="true"] .pro-btn__heart { color: var(--danger); }
.pro-btn--like[aria-pressed="true"] .pro-btn__heart svg { fill: currentColor; }
.pro-btn__heart::before, .pro-btn__heart::after { content: ""; position: absolute; left: 50%; top: 50%; border-radius: 50%; pointer-events: none; opacity: 0; }
.pro-btn__heart::before { width: 2.25rem; height: 2.25rem; margin: -1.125rem 0 0 -1.125rem; border: 2px solid var(--danger); }
.pro-btn__heart::after {
  width: 0.3125rem; height: 0.3125rem; margin: -0.15625rem 0 0 -0.15625rem; background: transparent;
  box-shadow: 0 -1.4rem var(--danger), 1.2rem -0.7rem var(--primary-2), 1.2rem 0.7rem var(--accent),
              0 1.4rem var(--danger), -1.2rem 0.7rem var(--primary), -1.2rem -0.7rem var(--accent);
}
.pro-btn--burst .pro-btn__heart svg { animation: pro-btn-pop var(--dur-4) var(--ease-spring); }
.pro-btn--burst .pro-btn__heart::before { animation: pro-btn-ring var(--dur-4) var(--ease-out); }
.pro-btn--burst .pro-btn__heart::after { animation: pro-btn-sparks var(--dur-5) var(--ease-out); }

/* Demo layout only */
.pro-btn-demo { display: grid; gap: 1rem; padding: 2rem var(--gutter); font-family: var(--font-sans); }
.pro-btn-demo__row { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; padding: 2rem; border-radius: var(--radius-2xl); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.pro-btn-demo__row--dark { background: radial-gradient(80% 120% at 0% 0%, color-mix(in srgb, var(--primary) 30%, transparent), transparent 60%), var(--surface-deep); box-shadow: none; }
.pro-btn-demo__group { display: inline-flex; }

@media (prefers-reduced-motion: reduce) {
  .pro-btn, .pro-btn::before, .pro-btn::after, .pro-btn *, .pro-btn *::before, .pro-btn *::after { animation: none !important; }
}

@keyframes pro-btn-spin { to { --pro-btn-angle: 360deg; } }
@keyframes pro-btn-turn { to { rotate: 360deg; } }
@keyframes pro-btn-pop { 0% { transform: scale(1); } 30% { transform: scale(0.7); } 65% { transform: scale(1.3); } 100% { transform: scale(1); } }
@keyframes pro-btn-ring { 0% { opacity: 0.8; transform: scale(0.2); } 100% { opacity: 0; transform: scale(1.4); border-width: 0; } }
@keyframes pro-btn-sparks { 0% { opacity: 1; transform: scale(0.3); } 60% { opacity: 1; } 100% { opacity: 0; transform: scale(1.3); } }
```

## JS

```js
// Morph: lock width → shrink to a spinner circle → expand to success → reset
document.querySelectorAll('[data-pro-btn-morph]').forEach((btn) => {
  const status = btn.parentElement.querySelector('.pro-btn__status');
  btn.addEventListener('click', () => {
    if (btn.dataset.state) return;
    const width = btn.offsetWidth;
    btn.style.width = `${width}px`;
    btn.setAttribute('aria-disabled', 'true');
    status.textContent = 'Booking…';
    requestAnimationFrame(() => { btn.dataset.state = 'loading'; btn.style.width = `${btn.offsetHeight}px`; });
    // Demo timing: replace with your request's promise
    setTimeout(() => {
      btn.dataset.state = 'success';
      btn.style.width = `${width}px`;
      status.textContent = 'Booked. A confirmation is on its way.';
      setTimeout(() => {
        delete btn.dataset.state;
        btn.removeAttribute('aria-disabled');
        btn.style.width = '';
        status.textContent = '';
      }, 2600);
    }, 1600);
  });
});

// Like: toggle state, restart the burst animation on each "on"
document.querySelectorAll('[data-pro-btn-like]').forEach((btn) => {
  btn.addEventListener('click', () => {
    const on = btn.getAttribute('aria-pressed') !== 'true';
    btn.setAttribute('aria-pressed', String(on));
    btn.classList.remove('pro-btn--burst');
    if (on) { void btn.offsetWidth; btn.classList.add('pro-btn--burst'); }
  });
});

// Magnetic: drift towards the pointer (mouse, motion allowed)
if (matchMedia('(hover: hover) and (prefers-reduced-motion: no-preference)').matches) {
  document.querySelectorAll('.pro-btn--magnetic').forEach((btn) => {
    btn.addEventListener('pointermove', (e) => {
      const r = btn.getBoundingClientRect();
      btn.style.setProperty('--pro-btn-mx', `${(e.clientX - r.left - r.width / 2) * 0.3}px`);
      btn.style.setProperty('--pro-btn-my', `${(e.clientY - r.top - r.height / 2) * 0.45}px`);
    });
    btn.addEventListener('pointerleave', () => {
      btn.style.setProperty('--pro-btn-mx', '0px');
      btn.style.setProperty('--pro-btn-my', '0px');
    });
  });
}
```

## Notes

- Focus uses `outline` (offset 3px), not `box-shadow`, so it never fights the button's own shadows. Glow and glass switch it to `--text-inverse` for dark backgrounds.
- `--morph` keeps one accessible name ("Confirm booking"). Progress and the result are announced through the adjacent `role="status"` element, and the button is `aria-disabled` while busy so it can't be double-submitted.
- `--like` is a real toggle (`aria-pressed`). Colour isn't the only signal, because the heart fills.
- The glow border only spins while hovered or focused, so nothing loops at rest. Reduced motion removes all keyframe effects; presses and colour changes stay (instantly).
- `--roll` hides its duplicate label from screen readers with `content: … / ""`. Older browsers that ignore that syntax still show the effect, but may read the label twice.
- Mix and match sparingly: one `--primary` per view, with `--ink` or `--glass` as the secondary.
