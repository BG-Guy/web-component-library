# Sticky Showcase

Apple-style scrollytelling. Steps of copy scroll past a pinned device frame; as each step reaches the middle of the screen, the frame cross-fades to that step's scene, which assembles itself piece by piece. The active step brightens, its accent bar draws in, and the progress dots follow. On phones the frame pins at the top and the copy scrolls beneath it. Depends on `tokens/variables.css`.

**Motion:** scene cross-fade (opacity + scale + blur) · staggered scene assembly · checklist ticks · shield draw · step accent bar · progress dot stretch.

## HTML

```html
<section class="sticky-showcase" aria-labelledby="sticky-showcase-title" data-sticky-showcase>
  <div class="sticky-showcase__inner">
    <header class="sticky-showcase__head">
      <p class="sticky-showcase__eyebrow">One visit, start to finish</p>
      <h2 id="sticky-showcase-title" class="sticky-showcase__title">No guesswork. No surprises.</h2>
    </header>

    <div class="sticky-showcase__layout">
      <div class="sticky-showcase__media" aria-hidden="true">
        <div class="sticky-showcase__frame">
          <div class="sticky-showcase__screen is-active">
            <div class="sticky-showcase__ui">
              <p class="sticky-showcase__ui-label" style="--i: 0">Your photos</p>
              <div class="sticky-showcase__thumbs" style="--i: 1"><span></span><span></span><span></span></div>
              <p class="sticky-showcase__bubble" style="--i: 2">Looks like a worn cartridge valve. We'll bring the part.</p>
            </div>
          </div>
          <div class="sticky-showcase__screen">
            <div class="sticky-showcase__ui">
              <p class="sticky-showcase__ui-label" style="--i: 0">Your quote</p>
              <p class="sticky-showcase__price" style="--i: 1">$149 <small>flat · parts included</small></p>
              <div class="sticky-showcase__button" style="--i: 2">Approve quote</div>
            </div>
          </div>
          <div class="sticky-showcase__screen">
            <div class="sticky-showcase__ui">
              <p class="sticky-showcase__ui-label" style="--i: 0">Job checklist · Sam K.</p>
              <ul class="sticky-showcase__checks" style="--i: 1">
                <li style="--c: 0">Water shut off</li><li style="--c: 1">Valve replaced</li><li style="--c: 2">Pressure tested</li><li style="--c: 3">Area cleaned</li>
              </ul>
            </div>
          </div>
          <div class="sticky-showcase__screen">
            <div class="sticky-showcase__ui sticky-showcase__ui--center">
              <svg class="sticky-showcase__shield" style="--i: 0" viewBox="0 0 64 64" width="72" height="72" focusable="false"><path d="M32 6 54 14v16c0 15-10 24-22 28C20 54 10 45 10 30V14z" /><path class="sticky-showcase__tick" d="m22 32 7 7 14-14" pathLength="1" /></svg>
              <p class="sticky-showcase__price" style="--i: 1">Covered <small>until October 2031</small></p>
            </div>
          </div>
          <div class="sticky-showcase__dots"><span class="is-active"></span><span></span><span></span><span></span></div>
        </div>
      </div>

      <ol class="sticky-showcase__steps" role="list">
        <li class="sticky-showcase__step is-active">
          <p class="sticky-showcase__num">01</p>
          <h3>Show us the problem</h3>
          <p>Snap a photo when you book. We diagnose before we arrive, so the right part is already in the van.</p>
        </li>
        <li class="sticky-showcase__step">
          <p class="sticky-showcase__num">02</p>
          <h3>Approve one clear price</h3>
          <p>A written, flat-rate quote within 15 minutes. What you approve is what you pay.</p>
        </li>
        <li class="sticky-showcase__step">
          <p class="sticky-showcase__num">03</p>
          <h3>Watch it get done right</h3>
          <p>Your technician works through a checklist you can follow live, then tests everything with you.</p>
        </li>
        <li class="sticky-showcase__step">
          <p class="sticky-showcase__num">04</p>
          <h3>Stay covered for five years</h3>
          <p>Every job carries our workmanship guarantee. Your receipt doubles as your warranty.</p>
        </li>
      </ol>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section */
.sticky-showcase { background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); }
.sticky-showcase__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.sticky-showcase__head { max-width: 40rem; margin-bottom: 2rem; }
.sticky-showcase__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.sticky-showcase__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }

/* Layout: frame pinned at the top (phones) or beside the steps (desktop) */
.sticky-showcase__layout { display: grid; }
.sticky-showcase__media { position: sticky; top: 0.75rem; z-index: 2; padding-bottom: 1rem; background: var(--surface-light); }
.sticky-showcase__frame {
  position: relative; height: min(42vh, 22rem); overflow: hidden; border-radius: var(--radius-2xl);
  background:
    radial-gradient(70% 60% at 80% 10%, color-mix(in srgb, var(--primary-2) 50%, transparent), transparent 65%),
    radial-gradient(70% 70% at 10% 95%, color-mix(in srgb, var(--primary) 60%, transparent), transparent 65%),
    var(--surface-deep);
  box-shadow: var(--shadow-xl), inset 0 0 0 1px var(--border-inverse);
}
.sticky-showcase__steps { margin: 0; padding: 0; list-style: none; }
.sticky-showcase__step { position: relative; display: flex; flex-direction: column; justify-content: center; min-height: 55vh; padding: 2rem 0 2rem 1.5rem; }

/* Step copy: muted until active; an accent bar draws in on the active step */
.sticky-showcase__step::before {
  content: ""; position: absolute; left: 0; top: 50%; width: 3px; height: 5.5rem; margin-top: -2.75rem; border-radius: 3px;
  background: linear-gradient(var(--primary), var(--primary-2)); transform: scaleY(0); transition: transform var(--dur-4) var(--ease-out);
}
.sticky-showcase__num { margin: 0; color: var(--text-muted); font: 500 0.8125rem/1 var(--font-mono); }
.sticky-showcase__step h3 { margin: 0.75rem 0 0; font: 600 clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); transition: color var(--dur-4); }
.sticky-showcase__step p:last-child { margin: 0.75rem 0 0; max-width: 28rem; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.sticky-showcase--js .sticky-showcase__step h3 { color: var(--text-muted); }
.sticky-showcase--js .sticky-showcase__step.is-active h3 { color: var(--text-main); }
.sticky-showcase__step.is-active::before { transform: scaleY(1); }
.sticky-showcase__step.is-active .sticky-showcase__num { color: var(--primary); }

/* Scenes: stacked in the frame, cross-fading */
.sticky-showcase__screen {
  position: absolute; inset: 0; display: grid; place-items: center; padding: 1.5rem;
  opacity: 0; transform: scale(0.96); filter: blur(8px);
  transition: opacity var(--dur-4) var(--ease-out), transform var(--dur-4) var(--ease-out), filter var(--dur-4) var(--ease-out);
}
.sticky-showcase__screen.is-active { opacity: 1; transform: none; filter: none; }
.sticky-showcase__screen.is-active .sticky-showcase__ui > * { animation: sticky-showcase-in var(--dur-4) var(--ease-out) calc(var(--i, 0) * 90ms + 150ms) both; }
.sticky-showcase__ui {
  display: grid; gap: 0.875rem; width: min(100%, 20rem); padding: 1.25rem; border-radius: 1.25rem;
  background: var(--surface-light); color: var(--text-main);
  box-shadow: 0 30px 60px -20px color-mix(in srgb, var(--surface-deep) 90%, transparent), var(--highlight);
}
.sticky-showcase__ui--center { justify-items: center; text-align: center; }
.sticky-showcase__ui-label { margin: 0; color: var(--text-muted); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; }

/* Scene parts */
.sticky-showcase__thumbs { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.5rem; }
.sticky-showcase__thumbs span { aspect-ratio: 1; border-radius: 0.75rem; background: radial-gradient(80% 80% at 30% 20%, color-mix(in srgb, var(--primary-2) 55%, var(--surface-light)), color-mix(in srgb, var(--primary) 70%, var(--surface-deep))); }
.sticky-showcase__thumbs span:nth-child(2) { background: radial-gradient(80% 80% at 70% 30%, color-mix(in srgb, var(--accent) 60%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep))); }
.sticky-showcase__thumbs span:nth-child(3) { background: radial-gradient(80% 80% at 40% 70%, color-mix(in srgb, var(--primary) 45%, var(--surface-light)), var(--surface-deep)); }
.sticky-showcase__bubble { margin: 0; padding: 0.75rem 0.875rem; border-radius: 1rem 1rem 1rem 0.25rem; background: color-mix(in srgb, var(--primary) 10%, var(--surface-light)); font-size: 0.875rem; line-height: 1.45; }
.sticky-showcase__price { margin: 0; font: 600 2.25rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.sticky-showcase__price small { display: block; margin-top: 0.375rem; color: var(--text-muted); font: 500 0.8125rem var(--font-sans); letter-spacing: 0; }
.sticky-showcase__button { display: grid; place-items: center; height: 2.75rem; border-radius: 0.875rem; background: var(--primary); color: var(--text-inverse); font-size: 0.875rem; font-weight: 600; box-shadow: 0 10px 24px -10px var(--primary); }
.sticky-showcase__checks { display: grid; gap: 0.5rem; margin: 0; padding: 0; list-style: none; font-size: 0.875rem; }
.sticky-showcase__checks li { position: relative; padding-left: 1.75rem; }
.sticky-showcase__checks li::before { content: ""; position: absolute; left: 0; top: 0.0625rem; width: 1.125rem; height: 1.125rem; border-radius: 50%; box-shadow: inset 0 0 0 1.5px var(--border-subtle); }
.sticky-showcase__checks li::after { content: ""; position: absolute; left: 0.4375rem; top: 0.25rem; width: 0.25rem; height: 0.5rem; border: solid var(--surface-light); border-width: 0 2px 2px 0; transform: rotate(45deg) scale(0); }
.sticky-showcase__screen.is-active .sticky-showcase__checks li::before { animation: sticky-showcase-fill var(--dur-3) var(--ease-out) calc(var(--c) * 320ms + 500ms) both; }
.sticky-showcase__screen.is-active .sticky-showcase__checks li::after { animation: sticky-showcase-tick var(--dur-4) var(--ease-spring) calc(var(--c) * 320ms + 560ms) both; }
.sticky-showcase__shield path:first-child { fill: color-mix(in srgb, var(--primary) 14%, transparent); stroke: var(--primary); stroke-width: 2.5; stroke-linejoin: round; }
.sticky-showcase__tick { fill: none; stroke: var(--primary-2); stroke-width: 4; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 1; stroke-dashoffset: 0; }
.sticky-showcase__screen.is-active .sticky-showcase__tick { animation: sticky-showcase-draw var(--dur-5) var(--ease-out) 450ms both; }

/* Progress dots: the active one stretches into a pill */
.sticky-showcase__dots { position: absolute; left: 50%; bottom: 1rem; display: flex; gap: 0.375rem; transform: translateX(-50%); }
.sticky-showcase__dots span { width: 0.375rem; height: 0.375rem; border-radius: 999px; background: color-mix(in srgb, var(--text-inverse) 35%, transparent); transition: width var(--dur-4) var(--ease-spring), background-color var(--dur-3); }
.sticky-showcase__dots .is-active { width: 1.5rem; background: var(--text-inverse); }

/* Desktop: steps left, frame pinned and vertically centred on the right */
@media (min-width: 1024px) {
  .sticky-showcase__layout { grid-template-columns: 1fr 1fr; column-gap: 4rem; }
  .sticky-showcase__steps { grid-column: 1; grid-row: 1; }
  .sticky-showcase__media { grid-column: 2; grid-row: 1; align-self: start; top: calc(50vh - min(17rem, 36vh)); padding: 0; background: none; }
  .sticky-showcase__frame { height: min(34rem, 72vh); }
  .sticky-showcase__step { min-height: 75vh; padding-left: 2rem; }
}

@media (prefers-reduced-motion: reduce) {
  .sticky-showcase__screen *, .sticky-showcase__screen *::before, .sticky-showcase__screen *::after { animation: none !important; }
  .sticky-showcase__checks li::before { background: var(--success); box-shadow: none; }
  .sticky-showcase__checks li::after { transform: rotate(45deg); }
}
@keyframes sticky-showcase-in { from { opacity: 0; transform: translateY(12px); filter: blur(4px); } }
@keyframes sticky-showcase-fill { to { background: var(--success); box-shadow: none; } }
@keyframes sticky-showcase-tick { to { transform: rotate(45deg) scale(1); } }
@keyframes sticky-showcase-draw { from { stroke-dashoffset: 1; } }
```

## JS

```js
document.querySelectorAll('[data-sticky-showcase]').forEach((root) => {
  const steps = [...root.querySelectorAll('.sticky-showcase__step')];
  const screens = [...root.querySelectorAll('.sticky-showcase__screen')];
  const dots = [...root.querySelectorAll('.sticky-showcase__dots span')];
  root.classList.add('sticky-showcase--js');

  // Activate step i everywhere: copy, scene and dot
  const activate = (i) => {
    [steps, screens, dots].forEach((set) => set.forEach((el, n) => el.classList.toggle('is-active', n === i)));
    steps.forEach((step, n) => (n === i ? step.setAttribute('aria-current', 'step') : step.removeAttribute('aria-current')));
  };

  // A step becomes active when it crosses a band just below the middle of the viewport
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => { if (entry.isIntersecting) activate(steps.indexOf(entry.target)); });
  }, { rootMargin: '-50% 0px -40% 0px' });
  steps.forEach((step) => io.observe(step));
});
```

## Notes

- The frame is decorative (`aria-hidden`); all meaning is in the ordered list of steps, so screen-reader and keyboard users get the full story without the visuals. The active step also gets `aria-current`.
- Without JS every step reads at full strength, and the first scene shows.
- Replace the scenes with screenshots or photos: keep one `.sticky-showcase__screen` per step, in the same order.
- The sticky frame needs no `overflow: hidden` on any ancestor between it and the page scroller, or `position: sticky` stops working.
- Under reduced motion, scenes swap with an instant fade and checklists render already ticked.
