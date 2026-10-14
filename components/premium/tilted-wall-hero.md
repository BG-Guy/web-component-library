# Tilted Project Wall Hero

A deep hero set in front of a 3D-tilted wall of finished projects. Five columns of photo tiles drift endlessly in alternating directions and fade into the dark at every edge, and the whole wall leans gently towards the pointer. A frosted glass card in front carries the headline, subcopy, CTAs and a rating row. On phones the wall drops to three columns at a steeper tilt and the card runs full width. Depends on `tokens/variables.css`.

**Motion:** wall fades and settles in (`--dur-5` × 2, `--ease-out`) while columns slide in from their travel direction (`--stagger`) · card materialises out of a blur, then its lines rise in sequence (`--dur-5`, `--stagger`) · columns scroll in alternating directions (linear loops, 52–70s) · pointer tilt eases with `--dur-5` `--ease-out` · buttons respond with `--ease-spring`. A pause button stops the wall; it also freezes off-screen.

## HTML

```html
<section class="wall-hero" aria-labelledby="wall-hero-title" data-wall-hero>
  <div class="wall-hero__scene" aria-hidden="true">
    <div class="wall-hero__tilt">
      <div class="wall-hero__plane">
        <div class="wall-hero__col" style="--wall-hero-c: 0; --wall-hero-speed: 64s">
          <div class="wall-hero__track">
            <figure class="wall-hero__tile"><img src="kitchen-remodel.jpg" alt="" width="480" height="600" decoding="async"><figcaption>Kitchen remodel<span>Westlake</span></figcaption></figure>
            <figure class="wall-hero__tile wall-hero__tile--square"><img src="heat-pump-install.jpg" alt="" width="480" height="480" decoding="async"><figcaption>Heat pump install<span>Riverside</span></figcaption></figure>
            <figure class="wall-hero__tile wall-hero__tile--tall"><img src="deck-build.jpg" alt="" width="480" height="640" loading="lazy" decoding="async"><figcaption>Cedar deck<span>Northside</span></figcaption></figure>
            <figure class="wall-hero__tile"><img src="attic-insulation.jpg" alt="" width="480" height="600" loading="lazy" decoding="async"><figcaption>Attic insulation<span>Springfield</span></figcaption></figure>
          </div>
        </div>
        <div class="wall-hero__col" style="--wall-hero-c: 1; --wall-hero-speed: 52s">
          <div class="wall-hero__track">
            <figure class="wall-hero__tile wall-hero__tile--tall"><img src="roof-replacement.jpg" alt="" width="480" height="640" decoding="async"><figcaption>Roof replacement<span>Northside</span></figcaption></figure>
            <figure class="wall-hero__tile"><img src="bathroom-refit.jpg" alt="" width="480" height="600" decoding="async"><figcaption>Bathroom refit<span>Westlake</span></figcaption></figure>
            <figure class="wall-hero__tile wall-hero__tile--square"><img src="panel-upgrade.jpg" alt="" width="480" height="480" loading="lazy" decoding="async"><figcaption>Panel upgrade<span>Riverside</span></figcaption></figure>
            <figure class="wall-hero__tile"><img src="porch-rebuild.jpg" alt="" width="480" height="600" loading="lazy" decoding="async"><figcaption>Porch rebuild<span>Springfield</span></figcaption></figure>
          </div>
        </div>
        <div class="wall-hero__col" style="--wall-hero-c: 2; --wall-hero-speed: 70s">
          <div class="wall-hero__track">
            <figure class="wall-hero__tile wall-hero__tile--square"><img src="solar-array.jpg" alt="" width="480" height="480" decoding="async"><figcaption>Solar array<span>Riverside</span></figcaption></figure>
            <figure class="wall-hero__tile"><img src="basement-finish.jpg" alt="" width="480" height="600" decoding="async"><figcaption>Basement finish<span>Northside</span></figcaption></figure>
            <figure class="wall-hero__tile wall-hero__tile--tall"><img src="window-install.jpg" alt="" width="480" height="640" loading="lazy" decoding="async"><figcaption>Window install<span>Westlake</span></figcaption></figure>
            <figure class="wall-hero__tile"><img src="laundry-room.jpg" alt="" width="480" height="600" loading="lazy" decoding="async"><figcaption>Laundry room<span>Springfield</span></figcaption></figure>
          </div>
        </div>
        <div class="wall-hero__col" style="--wall-hero-c: 3; --wall-hero-speed: 58s">
          <div class="wall-hero__track">
            <figure class="wall-hero__tile"><img src="patio-pavers.jpg" alt="" width="480" height="600" decoding="async"><figcaption>Patio pavers<span>Westlake</span></figcaption></figure>
            <figure class="wall-hero__tile wall-hero__tile--tall"><img src="siding-repair.jpg" alt="" width="480" height="640" decoding="async"><figcaption>Siding repair<span>Riverside</span></figcaption></figure>
            <figure class="wall-hero__tile wall-hero__tile--square"><img src="fireplace.jpg" alt="" width="480" height="480" loading="lazy" decoding="async"><figcaption>Gas fireplace<span>Northside</span></figcaption></figure>
            <figure class="wall-hero__tile"><img src="mudroom.jpg" alt="" width="480" height="600" loading="lazy" decoding="async"><figcaption>Mudroom built-ins<span>Springfield</span></figcaption></figure>
          </div>
        </div>
        <div class="wall-hero__col" style="--wall-hero-c: 4; --wall-hero-speed: 66s">
          <div class="wall-hero__track">
            <figure class="wall-hero__tile wall-hero__tile--square"><img src="garage-door.jpg" alt="" width="480" height="480" decoding="async"><figcaption>Garage door<span>Northside</span></figcaption></figure>
            <figure class="wall-hero__tile"><img src="fence-install.jpg" alt="" width="480" height="600" decoding="async"><figcaption>Fence install<span>Westlake</span></figcaption></figure>
            <figure class="wall-hero__tile wall-hero__tile--tall"><img src="gutter-guards.jpg" alt="" width="480" height="640" loading="lazy" decoding="async"><figcaption>Gutter guards<span>Riverside</span></figcaption></figure>
            <figure class="wall-hero__tile"><img src="driveway.jpg" alt="" width="480" height="600" loading="lazy" decoding="async"><figcaption>Driveway reseal<span>Springfield</span></figcaption></figure>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="wall-hero__scrim" aria-hidden="true"></div>

  <div class="wall-hero__inner">
    <div class="wall-hero__card">
      <p class="wall-hero__eyebrow" style="--wall-hero-i: 0">
        <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M3 11 12 4l9 7M5 10v10h14V10M10 20v-6h4v6" /></svg>
        Design-build &amp; repair · Springfield
      </p>
      <h1 id="wall-hero-title" class="wall-hero__title">
        <span class="wall-hero__line" style="--wall-hero-i: 1">1,400 homes.</span>
        <span class="wall-hero__line wall-hero__grad" style="--wall-hero-i: 2">Zero shortcuts.</span>
      </h1>
      <p class="wall-hero__lead" style="--wall-hero-i: 3">Kitchens, roofs, baths and heat pumps, built by licensed Brand crews and quoted upfront within 24 hours.</p>
      <div class="wall-hero__actions" style="--wall-hero-i: 4">
        <a class="wall-hero__btn wall-hero__btn--primary" href="#quote">
          Start your project
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="wall-hero__btn wall-hero__btn--glass" href="#projects">See recent work</a>
      </div>
      <div class="wall-hero__rating" style="--wall-hero-i: 5">
        <span class="wall-hero__stars" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
        </span>
        <p><strong>4.9/5</strong> from 312 verified reviews</p>
        <span class="wall-hero__badge">Licensed &amp; insured</span>
      </div>
    </div>
  </div>

  <button class="wall-hero__pause" type="button" aria-pressed="false" aria-label="Pause animation" hidden>
    <svg class="wall-hero__icon-pause" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
    <svg class="wall-hero__icon-play" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
  </button>
</section>
```

## CSS

```css
/* Section: deep, full height; the wall sits behind everything */
.wall-hero {
  --wall-hero-rx: 40deg;  /* steeper tilt on phones */
  --wall-hero-rz: -18deg;
  --wall-hero-gap: 0.75rem;
  --wall-hero-soft: color-mix(in srgb, var(--text-inverse-muted) 60%, var(--text-inverse));
  position: relative; isolation: isolate; overflow: clip;
  display: grid; align-items: center;
  min-height: 100vh; min-height: 100svh;
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}

/* Scene (perspective + edge fade) > tilt (pointer) > plane (fixed lean) > columns > tracks */
.wall-hero__scene {
  position: absolute; inset: 0; z-index: -2; perspective: 1200px; pointer-events: none;
  -webkit-mask-image: radial-gradient(ellipse 85% 80% at 50% 50%, black 35%, transparent 95%);
  mask-image: radial-gradient(ellipse 85% 80% at 50% 50%, black 35%, transparent 95%);
  animation: wall-hero-scene calc(var(--dur-5) * 2) var(--ease-out) backwards;
}
.wall-hero__tilt { position: absolute; inset: 0; transform-style: preserve-3d; transition: transform var(--dur-5) var(--ease-out); }
.wall-hero__plane {
  position: absolute; left: 50%; top: 50%; width: max(150%, 60rem); height: max(160%, 56rem);
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); align-items: start; gap: var(--wall-hero-gap);
  transform: translate(-50%, -50%) rotateX(var(--wall-hero-rx)) rotateZ(var(--wall-hero-rz));
}
.wall-hero__col { min-width: 0; animation: wall-hero-col calc(var(--dur-5) * 1.6) var(--ease-out) calc(var(--wall-hero-c) * var(--stagger) * 2) backwards; }
.wall-hero__col:nth-child(even) { --wall-hero-from: -14%; } /* columns slide in from the way they travel */
.wall-hero__col:nth-child(n + 4) { display: none; }
.wall-hero__track { display: grid; gap: var(--wall-hero-gap); padding-bottom: var(--wall-hero-gap); }

/* The loop starts only once JS has repeated the tiles (no gap, no jump); even columns run the other way */
.wall-hero--live .wall-hero__track { animation: wall-hero-scroll var(--wall-hero-speed, 60s) linear infinite; }
.wall-hero--live .wall-hero__col:nth-child(even) .wall-hero__track { animation-direction: reverse; }
.wall-hero:is([data-paused], [data-offscreen]) .wall-hero__track { animation-play-state: paused; }

/* Project tiles: photo, brand-tinted placeholder underneath, caption on a soft scrim */
.wall-hero__tile {
  position: relative; margin: 0; overflow: hidden; border-radius: var(--radius-xl);
  background: linear-gradient(150deg, color-mix(in srgb, var(--primary) 45%, var(--surface-deep)), color-mix(in srgb, var(--primary-2) 30%, var(--surface-deep)));
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 30px 60px -30px color-mix(in srgb, var(--surface-deep) 90%, transparent);
}
.wall-hero__tile:nth-child(3n + 2) { background: linear-gradient(150deg, color-mix(in srgb, var(--accent) 40%, var(--surface-deep)), color-mix(in srgb, var(--primary) 30%, var(--surface-deep))); }
.wall-hero__tile:nth-child(3n) { background: linear-gradient(150deg, color-mix(in srgb, var(--primary-2) 45%, var(--surface-deep)), color-mix(in srgb, var(--primary) 25%, var(--surface-deep))); }
.wall-hero__tile img { display: block; width: 100%; height: auto; aspect-ratio: 4 / 5; object-fit: cover; }
.wall-hero__tile--square img { aspect-ratio: 1; }
.wall-hero__tile--tall img { aspect-ratio: 3 / 4; }
.wall-hero__tile figcaption {
  position: absolute; inset: auto 0 0; display: grid; gap: 0.125rem; padding: 2.5rem 0.875rem 0.75rem;
  background: linear-gradient(transparent, color-mix(in srgb, var(--surface-deep) 85%, transparent));
  font-size: 0.8125rem; font-weight: 600;
}
.wall-hero__tile figcaption span { color: var(--text-inverse-muted); font: 500 0.625rem/1.3 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }

/* Scrim: darkens the middle for the card, adds a little brand light, fades the bottom into the page */
.wall-hero__scrim {
  position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background:
    radial-gradient(ellipse 50% 40% at 50% 45%, color-mix(in srgb, var(--primary) 18%, transparent), transparent 70%),
    radial-gradient(ellipse 60% 50% at 50% 50%, color-mix(in srgb, var(--surface-deep) 80%, transparent), color-mix(in srgb, var(--surface-deep) 35%, transparent) 80%, transparent),
    linear-gradient(color-mix(in srgb, var(--surface-deep) 50%, transparent), transparent 25%, transparent 70%, var(--surface-deep));
}

/* Foreground: one glass card, centred */
.wall-hero__inner {
  display: grid; justify-items: center; width: 100%; max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4.5rem, 12vw, 7rem) var(--gutter);
}
.wall-hero__card {
  position: relative; width: 100%; max-width: 40rem; padding: clamp(1.5rem, 5vw, 3rem); border-radius: var(--radius-2xl); text-align: center;
  background: color-mix(in srgb, var(--surface-deep) 86%, transparent);
  box-shadow: var(--highlight-inverse), 0 40px 100px -30px color-mix(in srgb, var(--surface-deep) 95%, transparent), 0 0 80px -30px color-mix(in srgb, var(--primary) 45%, transparent);
  animation: wall-hero-card var(--dur-5) var(--ease-out) 250ms backwards;
}
@supports (backdrop-filter: blur(1px)) {
  .wall-hero__card {
    background: color-mix(in srgb, var(--surface-deep) 70%, transparent);
    -webkit-backdrop-filter: blur(var(--blur-md)) saturate(1.4); backdrop-filter: blur(var(--blur-md)) saturate(1.4);
  }
}
.wall-hero__card::before { /* gradient hairline: bright at the top-left, teal at the bottom-right */
  content: ""; position: absolute; inset: 0; padding: 1px; border-radius: inherit; pointer-events: none;
  background: linear-gradient(160deg, color-mix(in srgb, var(--text-inverse) 30%, transparent), var(--border-inverse) 35%, transparent 60%, color-mix(in srgb, var(--primary-2) 50%, transparent));
  -webkit-mask: linear-gradient(black 0 0) content-box, linear-gradient(black 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(black 0 0) content-box, linear-gradient(black 0 0);
  mask-composite: exclude;
}

/* Copy rises line by line once the card has materialised */
.wall-hero__eyebrow, .wall-hero__line, .wall-hero__lead, .wall-hero__actions, .wall-hero__rating {
  animation: wall-hero-rise var(--dur-5) var(--ease-out) calc(450ms + var(--wall-hero-i) * var(--stagger) * 2) backwards;
}
.wall-hero__eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.375rem 0.75rem; border-radius: var(--radius-full);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse);
  color: var(--wall-hero-soft); font: 500 0.6875rem/1.2 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.wall-hero__eyebrow svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.wall-hero__title { margin: 1.25rem 0 0; font: 600 clamp(2.25rem, 1.1rem + 5.2vw, 4.75rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.wall-hero__line { display: block; }
.wall-hero__grad {
  padding-bottom: 0.06em;
  background: linear-gradient(95deg, var(--text-inverse) 5%, color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse)) 55%, color-mix(in srgb, var(--primary) 45%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.wall-hero__lead { max-width: 30rem; margin: 1.25rem auto 0; color: var(--wall-hero-soft); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.1875rem); line-height: 1.6; text-wrap: pretty; }

/* CTAs: solid light primary, glass secondary; stacked on phones */
.wall-hero__actions { display: grid; gap: 0.75rem; margin-top: 2rem; }
.wall-hero__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.5rem;
  border-radius: var(--radius-full); font: 600 0.9375rem/1 var(--font-sans); text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out), background-color var(--dur-2);
}
.wall-hero__btn svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.wall-hero__btn:hover { transform: translateY(-2px); }
.wall-hero__btn:active { transform: scale(0.97); }
.wall-hero__btn--primary { background: var(--surface-light); color: var(--text-main); box-shadow: var(--highlight), 0 14px 40px -14px color-mix(in srgb, var(--primary-2) 85%, transparent); }
.wall-hero__btn--primary:hover { box-shadow: var(--highlight), 0 18px 48px -12px color-mix(in srgb, var(--primary) 90%, transparent); }
.wall-hero__btn--primary:hover svg { transform: translateX(3px); }
.wall-hero__btn--glass { background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.wall-hero__btn--glass:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.wall-hero :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Rating row: the stars fill in left to right */
.wall-hero__rating {
  display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 0.5rem 0.875rem;
  margin-top: 1.75rem; padding-top: 1.5rem; border-top: 1px solid var(--border-inverse);
  color: var(--wall-hero-soft); font-size: 0.875rem;
}
.wall-hero__rating p { margin: 0; }
.wall-hero__rating strong { color: var(--text-inverse); }
.wall-hero__stars { display: inline-flex; gap: 0.125rem; color: var(--accent); animation: wall-hero-stars var(--dur-5) var(--ease-out) 1.1s backwards; }
.wall-hero__stars svg { fill: currentColor; stroke: currentColor; stroke-width: 1.5; stroke-linejoin: round; }
.wall-hero__badge {
  padding: 0.25rem 0.625rem; border-radius: var(--radius-full); color: var(--text-inverse); font-size: 0.75rem; font-weight: 500;
  background: color-mix(in srgb, var(--success) 22%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--success) 45%, transparent);
}

/* Pause control */
.wall-hero__pause {
  position: absolute; right: var(--gutter); bottom: 1rem; display: grid; place-items: center;
  width: 2.5rem; height: 2.5rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse-muted); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
  transition: color var(--dur-2), background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.wall-hero__pause:hover { color: var(--text-inverse); background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.wall-hero__pause:active { transform: scale(0.92); }
.wall-hero__pause[hidden] { display: none; }
.wall-hero__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.wall-hero__icon-play, .wall-hero__pause[aria-pressed="true"] .wall-hero__icon-pause { display: none; }
.wall-hero__pause[aria-pressed="true"] .wall-hero__icon-play { display: block; }

@media (min-width: 768px) {
  .wall-hero { --wall-hero-rx: 30deg; --wall-hero-rz: -12deg; --wall-hero-gap: 1rem; }
  .wall-hero__plane { width: max(140%, 72rem); grid-template-columns: repeat(5, minmax(0, 1fr)); }
  .wall-hero__col:nth-child(n + 4) { display: block; }
  .wall-hero__actions { display: flex; flex-wrap: wrap; justify-content: center; }
}
@media (prefers-reduced-motion: reduce) {
  .wall-hero *, .wall-hero *::before, .wall-hero *::after { animation: none !important; }
}

@keyframes wall-hero-scene { from { opacity: 0; transform: scale(1.12); } }
@keyframes wall-hero-col { from { opacity: 0; translate: 0 var(--wall-hero-from, 14%); } }
@keyframes wall-hero-scroll { to { transform: translateY(calc(-100% / var(--wall-hero-sets, 2))); } }
@keyframes wall-hero-card { from { opacity: 0; transform: translateY(24px) scale(0.96); filter: blur(12px); } }
@keyframes wall-hero-rise { from { opacity: 0; transform: translateY(14px); filter: blur(6px); } }
@keyframes wall-hero-stars { from { clip-path: inset(0 100% 0 0); } }
```

## JS

```js
document.querySelectorAll('[data-wall-hero]').forEach((hero) => {
  // Reduced motion: leave the static wall exactly as authored (no loop, no tilt, no pause button)
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const plane = hero.querySelector('.wall-hero__plane');
  const tilt = hero.querySelector('.wall-hero__tilt');
  const pause = hero.querySelector('.wall-hero__pause');
  const tracks = [...hero.querySelectorAll('.wall-hero__track')];

  // Repeat each column's tiles until a one-set shift never shows a gap; CSS scrolls by 100% / sets
  const fill = () => tracks.forEach((track) => {
    if (!track.offsetHeight) return; // column hidden at this width
    const set = [...track.children].filter((tile) => !tile.hasAttribute('data-wall-hero-clone'));
    let sets = track.children.length / set.length;
    const need = Math.max(2, Math.ceil(plane.offsetHeight / (track.offsetHeight / sets)) + 1);
    for (; sets < need; sets += 1) {
      track.append(...set.map((tile) => {
        const copy = tile.cloneNode(true);
        copy.setAttribute('data-wall-hero-clone', '');
        return copy;
      }));
    }
    track.style.setProperty('--wall-hero-sets', sets);
  });
  fill();
  hero.classList.add('wall-hero--live'); // copies match the originals, so reversed columns start without a jump
  new ResizeObserver(fill).observe(hero);

  // Pause button (WCAG 2.2.2) and an off-screen freeze
  pause.hidden = false;
  pause.addEventListener('click', () => {
    pause.setAttribute('aria-pressed', String(hero.toggleAttribute('data-paused')));
  });
  new IntersectionObserver(([entry]) => hero.toggleAttribute('data-offscreen', !entry.isIntersecting)).observe(hero);

  // Pointer tilt (mouse only): one transform write per frame; CSS eases it with --ease-out
  let frame = 0, px = 0, py = 0;
  hero.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    px = e.clientX; py = e.clientY;
    frame ||= requestAnimationFrame(() => {
      frame = 0;
      const r = hero.getBoundingClientRect();
      const x = (px - r.left) / r.width - 0.5;
      const y = (py - r.top) / r.height - 0.5;
      tilt.style.transform = `rotateX(${(-y * 5).toFixed(2)}deg) rotateY(${(x * 7).toFixed(2)}deg)`;
    });
  }, { passive: true });
  hero.addEventListener('pointerleave', () => { tilt.style.transform = ''; });
});
```

## Notes

- The wall is decorative: its wrapper is `aria-hidden="true"`, every tile image has `alt=""` and the captions stay out of the accessibility tree. The card holds the content: one `<h1>`, the lead, two CTAs and the rating text ("4.9/5 from 312 verified reviews"; the stars are hidden from assistive tech).
- Without JS the wall is static (one set of tiles per column) and the card is complete. JS repeats the tiles, then adds `.wall-hero--live` to start the loop. Because the copies match the originals, the columns that run in reverse begin one set up without a visible jump. Under reduced motion the script exits early: the wall stays static, with no tilt, no entrance and no pause button.
- The pause button sets `data-paused`, and an `IntersectionObserver` sets `data-offscreen`; either one pauses the column loops. The tilt follows the mouse only, eased by a `--dur-5` transition, and never runs on touch.
- Images: the first two tiles in each column load eagerly (they're on screen at load); the rest are `loading="lazy"`, and clones keep their original's setting (same cached file, so no flash and no extra request). Replace the placeholder names with your own project photos (`object-fit: cover` crops any aspect). Each tile has a brand-tinted gradient underneath while its photo loads.
- Contrast: the card is 70% `--surface-deep` glass over an 80% central scrim, so even a pure-white photo behind it leaves a background around #1d2230. The lead (`--wall-hero-soft`) measures 7.6:1 or better against that worst case, the gradient line 7:1 or better, and the primary CTA label 14:1.
- Tune it with `--wall-hero-rx`/`--wall-hero-rz` (lean; steeper below 768px), `--wall-hero-speed` per column, `--wall-hero-gap`, or more columns (the first three show on phones).
