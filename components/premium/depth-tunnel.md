# Depth Tunnel

A pinned, deep-surface stage with real perspective: seven company milestones hang along the Z axis at increasing depth, staggered left, right, up and down around a glowing vanishing point. The signature: scrolling flies the camera forward, so each card swims out of the blur, sharpens as it reaches the focal plane, then rushes past, swelling, softening and fading. A perspective grid floor streams beneath, the light at the end of the tunnel brightens, and a year readout and progress bar track the trip. On phones the offsets tighten and the cards shrink; without JS, or with reduced motion, the same cards form a clean vertical timeline. Depends on `tokens/variables.css`.

**Motion:** camera depth, card opacity/blur and floor scroll are all derived in CSS from one scroll-progress variable (linear scrub, rAF) · current-card glow (`--dur-4`, `--ease-out`) · link arrow nudge (`--ease-spring`) · smooth fly-to on keyboard focus · intro hint bobs three times.

## HTML

```html
<div class="depth-tunnel-demo">
  <p class="depth-tunnel-demo__copy">Twenty-six years in seven stops.</p>
  <p class="depth-tunnel-demo__hint">Scroll to fly through
    <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
  </p>
</div>

<section class="depth-tunnel" aria-labelledby="depth-tunnel-title" data-depth-tunnel>
  <div class="depth-tunnel__stage">
    <header class="depth-tunnel__head">
      <p class="depth-tunnel__eyebrow"><span class="depth-tunnel__dot" aria-hidden="true"></span>Our story · 1998–2024</p>
      <h2 id="depth-tunnel-title" class="depth-tunnel__title">From one van to forty.</h2>
    </header>

    <div class="depth-tunnel__scene">
      <span class="depth-tunnel__glow" aria-hidden="true"></span>
      <span class="depth-tunnel__floor" aria-hidden="true"></span>
      <ol class="depth-tunnel__list" role="list">
        <li class="depth-tunnel__card" data-year="1998">
          <p class="depth-tunnel__top"><span class="depth-tunnel__year">1998</span><span class="depth-tunnel__index" aria-hidden="true">01 / 07</span></p>
          <h3 class="depth-tunnel__name"><a href="#story-1998">First van on the road<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a></h3>
          <p class="depth-tunnel__text">One licensed plumber, a second-hand van and a pager. Dan took every call himself.</p>
        </li>
        <li class="depth-tunnel__card" data-year="2003">
          <p class="depth-tunnel__top"><span class="depth-tunnel__year">2003</span><span class="depth-tunnel__index" aria-hidden="true">02 / 07</span></p>
          <h3 class="depth-tunnel__name"><a href="#story-2003">Our first apprentice<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a></h3>
          <p class="depth-tunnel__text">Maria joined to learn the trade. Today she runs dispatch for all three areas.</p>
        </li>
        <li class="depth-tunnel__card" data-year="2008">
          <p class="depth-tunnel__top"><span class="depth-tunnel__year">2008</span><span class="depth-tunnel__index" aria-hidden="true">03 / 07</span></p>
          <h3 class="depth-tunnel__name"><a href="#story-2008">10,000th repair<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a></h3>
          <p class="depth-tunnel__text">A burst pipe on a freezing Northside night became job number ten thousand.</p>
        </li>
        <li class="depth-tunnel__card" data-year="2012">
          <p class="depth-tunnel__top"><span class="depth-tunnel__year">2012</span><span class="depth-tunnel__index" aria-hidden="true">04 / 07</span></p>
          <h3 class="depth-tunnel__name"><a href="#story-2012">Electricians in-house<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a></h3>
          <p class="depth-tunnel__text">Licensed electricians joined the team, bringing panel upgrades and rewires under one roof.</p>
        </li>
        <li class="depth-tunnel__card" data-year="2016">
          <p class="depth-tunnel__top"><span class="depth-tunnel__year">2016</span><span class="depth-tunnel__index" aria-hidden="true">05 / 07</span></p>
          <h3 class="depth-tunnel__name"><a href="#story-2016">Solar division<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a></h3>
          <p class="depth-tunnel__text">Our first rooftop array went live in Riverside: 6.2 kW on a 1920s bungalow.</p>
        </li>
        <li class="depth-tunnel__card" data-year="2020">
          <p class="depth-tunnel__top"><span class="depth-tunnel__year">2020</span><span class="depth-tunnel__index" aria-hidden="true">06 / 07</span></p>
          <h3 class="depth-tunnel__name"><a href="#story-2020">Same-day guarantee<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a></h3>
          <p class="depth-tunnel__text">Book by noon and we're at your door today, or the visit is free.</p>
        </li>
        <li class="depth-tunnel__card" data-year="2024">
          <p class="depth-tunnel__top"><span class="depth-tunnel__year">2024</span><span class="depth-tunnel__index" aria-hidden="true">07 / 07</span></p>
          <h3 class="depth-tunnel__name"><a href="#story-2024">Forty vans, one team<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a></h3>
          <p class="depth-tunnel__text">Forty vans across Westlake, Northside and Riverside. Still family-run, still answering at 3 a.m.</p>
        </li>
      </ol>
    </div>

    <p class="depth-tunnel__hint" aria-hidden="true">Scroll to fly</p>
    <div class="depth-tunnel__hud" aria-hidden="true">
      <span class="depth-tunnel__now">1998</span>
      <span class="depth-tunnel__bar"><span class="depth-tunnel__fill"></span></span>
      <span class="depth-tunnel__end">2024</span>
    </div>
  </div>
</section>

<div class="depth-tunnel-demo">
  <p class="depth-tunnel-demo__copy">Next stop: your place.</p>
  <p class="depth-tunnel-demo__hint">Scroll back up to fly in reverse</p>
</div>
```

## CSS

```css
/* Demo scroll room above and below */
.depth-tunnel-demo {
  display: grid; place-content: center; justify-items: center; gap: 0.875rem; min-height: 70vh; padding: 3rem var(--gutter);
  background: var(--surface-deep); color: var(--text-inverse-muted); font-family: var(--font-sans); text-align: center;
}
.depth-tunnel-demo__copy { margin: 0; color: var(--text-inverse); font: 600 clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.depth-tunnel-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.depth-tunnel-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: depth-tunnel-bob 1.4s var(--ease-in-out) 600ms 3; }

/* Section. Scene geometry (phone values first); camera position in card gaps derives from --depth-tunnel-p */
.depth-tunnel {
  --depth-tunnel-card: 15rem; --depth-tunnel-ox: 10vw; --depth-tunnel-oy: 9vh; --depth-tunnel-gap: 24rem; --depth-tunnel-persp: 45rem;
  --depth-tunnel-t: calc(var(--depth-tunnel-p, 0) * (var(--depth-tunnel-count, 7) - 0.6) - 0.4);
  position: relative; isolation: isolate; background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}
.depth-tunnel__stage { position: relative; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.depth-tunnel__eyebrow { display: flex; align-items: center; gap: 0.625rem; margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.depth-tunnel__dot { flex: none; width: 0.5rem; height: 0.5rem; border-radius: var(--radius-full); background: var(--gradient-brand); box-shadow: 0 0 0.75rem color-mix(in srgb, var(--primary-2) 80%, transparent); }
.depth-tunnel__title { margin: 0.875rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.8vw, 3.25rem)/1.04 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.depth-tunnel__glow, .depth-tunnel__floor, .depth-tunnel__hint, .depth-tunnel__hud { display: none; }

/* Default (no JS, reduced motion): a vertical timeline with a gradient spine */
.depth-tunnel__list { position: relative; display: grid; gap: 1rem; max-width: 40rem; margin: 2.5rem 0 0; padding: 0 0 0 2.25rem; list-style: none; }
.depth-tunnel__list::before { content: ""; position: absolute; left: 0.5rem; top: 1.5rem; bottom: 1.5rem; width: 2px; border-radius: var(--radius-full); background: linear-gradient(var(--primary), var(--primary-2) 70%, transparent); }
.depth-tunnel__card {
  position: relative; display: grid; gap: 0.5rem; padding: 1.25rem 1.25rem 1.5rem; border-radius: var(--radius-2xl);
  background: linear-gradient(160deg, color-mix(in srgb, var(--primary) 18%, var(--surface-deep)), color-mix(in srgb, var(--primary-2) 8%, var(--surface-deep)) 75%);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 30px 60px -30px color-mix(in srgb, var(--surface-deep) 95%, transparent);
  transition: box-shadow var(--dur-4) var(--ease-out), translate var(--dur-3) var(--ease-spring);
}
.depth-tunnel__card::before {
  content: ""; position: absolute; top: 1.75rem; left: calc(-1.75rem + 1px); width: 0.875rem; height: 0.875rem; translate: -50% 0; border-radius: var(--radius-full);
  background: var(--surface-deep); box-shadow: 0 0 0 2px var(--primary-2), 0 0 0 6px color-mix(in srgb, var(--primary-2) 22%, transparent);
}
.depth-tunnel:not(.depth-tunnel--3d) .depth-tunnel__card:hover { translate: 0 -2px; }
.depth-tunnel__top { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; margin: 0; }
.depth-tunnel__year {
  font: 600 clamp(2rem, 1.6rem + 1.2vw, 2.5rem)/1 var(--font-display); letter-spacing: var(--tracking-display); font-variant-numeric: tabular-nums;
  background: linear-gradient(100deg, var(--text-inverse), color-mix(in srgb, var(--primary-2) 70%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.depth-tunnel__index { color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; }
.depth-tunnel__name { margin: 0.25rem 0 0; font: 600 1.1875rem/1.25 var(--font-display); letter-spacing: var(--tracking-tight); }
.depth-tunnel__name a { color: inherit; text-decoration: none; }
.depth-tunnel__name a::after { content: ""; position: absolute; inset: 0; }
.depth-tunnel__name svg { margin-left: 0.375rem; vertical-align: -0.125em; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.depth-tunnel__card:hover .depth-tunnel__name svg { transform: translateX(3px); }
.depth-tunnel__text { margin: 0; color: var(--text-inverse-muted); font-size: 0.9375rem; line-height: 1.55; }
.depth-tunnel a:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; border-radius: var(--radius-sm); }
@supports selector(:has(*)) {
  .depth-tunnel__name a:focus-visible { outline: none; }
  .depth-tunnel__card:has(a:focus-visible) { outline: 2px solid var(--text-inverse); outline-offset: 4px; }
}

/* Card offsets around the flight path; the last card waits dead centre */
.depth-tunnel__card:nth-child(6n+1) { --depth-tunnel-x: -1; --depth-tunnel-y: 0.15; }
.depth-tunnel__card:nth-child(6n+2) { --depth-tunnel-x: 1; --depth-tunnel-y: -0.15; }
.depth-tunnel__card:nth-child(6n+3) { --depth-tunnel-x: -0.15; --depth-tunnel-y: -1; }
.depth-tunnel__card:nth-child(6n+4) { --depth-tunnel-x: 0.2; --depth-tunnel-y: 1; }
.depth-tunnel__card:nth-child(6n+5) { --depth-tunnel-x: -0.8; --depth-tunnel-y: -0.6; }
.depth-tunnel__card:nth-child(6n) { --depth-tunnel-x: 0.8; --depth-tunnel-y: 0.6; }
.depth-tunnel__card:last-child { --depth-tunnel-x: 0; --depth-tunnel-y: 0; }

/* 3D (JS, motion allowed): tall track, pinned stage, perspective scene */
.depth-tunnel--3d { height: calc(100vh + var(--depth-tunnel-count, 7) * 55vh); height: calc(100svh + var(--depth-tunnel-count, 7) * 55svh); }
.depth-tunnel--3d .depth-tunnel__stage { position: sticky; top: 0; height: 100vh; height: 100svh; max-width: none; padding: 0; overflow: hidden; }
.depth-tunnel--3d .depth-tunnel__stage::before, .depth-tunnel--3d .depth-tunnel__stage::after { content: ""; position: absolute; inset-inline: 0; z-index: 1; pointer-events: none; }
.depth-tunnel--3d .depth-tunnel__stage::before { top: 0; height: 10rem; background: linear-gradient(var(--surface-deep) 30%, transparent); }
.depth-tunnel--3d .depth-tunnel__stage::after { bottom: 0; height: 8rem; background: linear-gradient(transparent, var(--surface-deep) 75%); }
.depth-tunnel--3d .depth-tunnel__head { position: absolute; inset: clamp(1.25rem, 5vh, 2.75rem) 0 auto; z-index: 2; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.depth-tunnel--3d .depth-tunnel__title { font-size: clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem); }
.depth-tunnel--3d .depth-tunnel__scene { position: absolute; inset: 0; perspective: var(--depth-tunnel-persp); perspective-origin: 50% 45%; }
.depth-tunnel--3d .depth-tunnel__glow {
  display: block; position: absolute; left: 50%; top: 45%; width: min(80vmin, 44rem); aspect-ratio: 1; translate: -50% -50%; border-radius: var(--radius-full);
  background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 42%, transparent), color-mix(in srgb, var(--primary-2) 14%, transparent) 55%, transparent);
  opacity: calc(0.45 + var(--depth-tunnel-p, 0) * 0.55);
}
/* Floor: a grid laid flat along the stage's bottom edge, streaming toward the viewer with the camera */
.depth-tunnel--3d .depth-tunnel__floor {
  display: block; position: absolute; inset: auto -60% 0; height: 260%; transform-origin: 50% 100%; transform: rotateX(88deg);
  background:
    linear-gradient(color-mix(in srgb, var(--primary-2) 40%, transparent) 2px, transparent 2px) 50% calc(var(--depth-tunnel-t) * 8rem) / 4rem 4rem,
    linear-gradient(90deg, color-mix(in srgb, var(--primary-2) 24%, transparent) 1px, transparent 1px) 50% 0 / 4rem 4rem;
  -webkit-mask-image: linear-gradient(to top, black, transparent 70%);
  mask-image: linear-gradient(to top, black, transparent 70%);
}
.depth-tunnel--3d .depth-tunnel__list { position: absolute; inset: 0; display: grid; place-items: center; max-width: none; margin: 0; padding: 0; transform-style: preserve-3d; }
.depth-tunnel--3d .depth-tunnel__list::before, .depth-tunnel--3d .depth-tunnel__card::before { display: none; }
/* d = camera position minus card index: < 0 still ahead (small, blurred), 0 at the focal plane, > 0 rushing past */
.depth-tunnel--3d .depth-tunnel__card {
  --depth-tunnel-d: calc(var(--depth-tunnel-t) - var(--depth-tunnel-i, 0));
  grid-area: 1 / 1; width: var(--depth-tunnel-card);
  transform:
    translate3d(calc(var(--depth-tunnel-x) * var(--depth-tunnel-ox)), calc(var(--depth-tunnel-y) * var(--depth-tunnel-oy)), calc(var(--depth-tunnel-d) * var(--depth-tunnel-gap)))
    rotateY(calc(var(--depth-tunnel-x) * -12deg));
  opacity: min(clamp(0, calc(1.6 + var(--depth-tunnel-d) * 0.35), 1), clamp(0, calc(1 - (var(--depth-tunnel-d) - 0.15) * 2.4), 1));
  filter: blur(max(calc(var(--depth-tunnel-d) * -2.4px), calc((var(--depth-tunnel-d) - 0.1) * 16px), 0px));
  will-change: transform, opacity, filter;
}
.depth-tunnel--3d .depth-tunnel__card.is-current { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 45%, transparent), var(--highlight-inverse), 0 0 70px -24px color-mix(in srgb, var(--primary) 80%, transparent); }
.depth-tunnel--3d .depth-tunnel__card.is-away { pointer-events: none; }

/* HUD: hint, year readout and progress */
.depth-tunnel--3d .depth-tunnel__hint {
  display: block; position: absolute; z-index: 2; left: 50%; bottom: calc(max(1.25rem, 3.5vh) + 3rem); translate: -50% 0; margin: 0;
  color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; white-space: nowrap;
  opacity: clamp(0, calc(1 - var(--depth-tunnel-p, 0) * 14), 1);
}
.depth-tunnel--3d .depth-tunnel__hud {
  position: absolute; z-index: 2; inset: auto var(--gutter) max(1.25rem, 3.5vh); display: flex; align-items: center; gap: 1rem; max-width: 36rem; margin-inline: auto;
  color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em;
}
.depth-tunnel__now { min-width: 4ch; color: var(--text-inverse); font: 600 1.5rem/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }
.depth-tunnel__bar { position: relative; flex: 1; height: 2px; overflow: hidden; border-radius: var(--radius-full); background: var(--border-inverse); }
.depth-tunnel__fill { position: absolute; inset: 0; background: var(--gradient-brand); transform: scaleX(var(--depth-tunnel-p, 0)); transform-origin: left; }

@media (min-width: 768px) {
  .depth-tunnel { --depth-tunnel-card: 20rem; --depth-tunnel-ox: min(26vw, 20rem); --depth-tunnel-oy: 11vh; --depth-tunnel-gap: 34rem; --depth-tunnel-persp: 62.5rem; }
  .depth-tunnel__card { padding: 1.5rem 1.75rem 1.75rem; }
}
@media (prefers-reduced-motion: reduce) {
  .depth-tunnel-demo *, .depth-tunnel-demo *::before, .depth-tunnel-demo *::after { animation: none !important; }
}
@keyframes depth-tunnel-bob { 50% { transform: translateY(4px); } }
```

## JS

```js
// Shared recipe: 0 when the track's top reaches the viewport top, 1 when its bottom reaches the viewport bottom
const progress = (el) => { const r = el.getBoundingClientRect(); const range = r.height - innerHeight; return range > 0 ? Math.min(1, Math.max(0, -r.top / range)) : 0; };

document.querySelectorAll('[data-depth-tunnel]').forEach((root) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const cards = [...root.querySelectorAll('.depth-tunnel__card')];
  const now = root.querySelector('.depth-tunnel__now');
  const lead = 0.4;                     // the first card starts this many gaps beyond the focal plane (matches the CSS)
  const span = cards.length - 1 + lead; // total camera travel, in card gaps
  let near = false, frame = 0, current = -1;
  root.style.setProperty('--depth-tunnel-count', cards.length);
  cards.forEach((card, i) => card.style.setProperty('--depth-tunnel-i', i));

  // One progress write per frame: CSS derives depth, blur, opacity and the floor from it.
  // Cards rushing past (or still far off) stop catching the pointer; the nearest one is "current".
  const update = () => {
    frame = 0;
    const p = progress(root);
    const t = p * span - lead;
    root.style.setProperty('--depth-tunnel-p', p.toFixed(4));
    cards.forEach((card, n) => card.classList.toggle('is-away', t - n > 0.3 || t - n < -3.5));
    const index = Math.min(cards.length - 1, Math.max(0, Math.round(t)));
    if (index === current) return;
    current = index;
    cards.forEach((card, n) => card.classList.toggle('is-current', n === index));
    now.textContent = cards[index].dataset.year;
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(update); };
  const mode = () => { root.classList.toggle('depth-tunnel--3d', !reduce.matches); update(); };

  // Keyboard focus flies the camera to that card's depth, so the focused link is always the sharp one
  root.addEventListener('focusin', (e) => {
    const n = cards.indexOf(e.target.closest('.depth-tunnel__card'));
    if (n < 0 || reduce.matches || !e.target.matches(':focus-visible')) return;
    const r = root.getBoundingClientRect();
    scrollTo({ top: scrollY + r.top + ((n + lead) / span) * (r.height - innerHeight), behavior: 'smooth' });
  });

  new IntersectionObserver(([entry]) => { near = entry.isIntersecting; queue(); }).observe(root);
  addEventListener('scroll', queue, { passive: true });
  addEventListener('resize', queue);
  reduce.addEventListener('change', mode);
  mode();
});
```

## Notes

- The milestones are an ordered list in date order. Each card is titled by an `<h3>` link that stretches over the card, so the DOM reads as a plain timeline whatever the camera is doing. Tabbing into a card smooth-scrolls the camera to that card's depth (only for keyboard focus, and never under reduced motion), so the focused link is always the sharp, front-facing one. The year readout, progress bar, hint, floor and glow are decorative (`aria-hidden`). Cards rushing past or still far away get `pointer-events: none`, so a faded giant can't swallow clicks.
- Without JS, or with `prefers-reduced-motion` (switched live), there's no pin, perspective, blur or fly-through: the same cards form a vertical timeline with a gradient spine. In 3D mode everything is derived in CSS from the single `--depth-tunnel-p` written by the shared rAF + IntersectionObserver recipe; JS touches classes only when a card crosses a threshold.
- Contrast: cards are near-opaque deep gradients, so `--text-inverse` is ≥ 15:1, `--text-inverse-muted` ≥ 6.7:1 and the year gradient ≥ 7.8:1. Blurred and faded states are passing frames; the card at the focal plane is always sharp at full contrast.
- Tuning: `--depth-tunnel-gap` (Z distance between cards), `--depth-tunnel-persp`, `--depth-tunnel-ox`/`-oy` (offset spread) and `--depth-tunnel-card` are set per breakpoint. Each card gets 55vh of scroll, and the `nth-child` rules set the left/right/up/down pattern (the last card always lands centred). `lead` (0.4) appears in both the JS and the `--depth-tunnel-t` formula; change both together.
- Add or remove milestones freely: JS writes `--depth-tunnel-count` and each card's index, and the track height follows. Give each card a `data-year` for the readout.
- Support: plain 3D transforms, `filter` and `min()`/`max()`/`clamp()` inside `opacity`/`blur()` (all current engines); `svh` falls back to `vh`. The floor uses a moving `background-position`, so it costs one repaint of a single layer per frame.
