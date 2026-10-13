# Drag Carousel

Full-bleed project carousel that aligns with your page container but runs edge to edge. Swipe on touch, or drag and fling with a mouse: momentum carries it and it settles on the nearest card. Cards towards the edges scale down and fade, driven by their scroll position, while a progress thumb, a counter and prev/next buttons stay in sync. Depends on `tokens/variables.css`.

**Motion:** native scroll-snap · mouse drag with fling momentum · scroll-driven edge scale/fade · image zoom + arrow rotate on hover · progress thumb glide.

## HTML

```html
<section class="drag-carousel" aria-labelledby="drag-carousel-title" aria-roledescription="carousel" data-drag-carousel>
  <div class="drag-carousel__head">
    <div>
      <p class="drag-carousel__eyebrow">Recent projects</p>
      <h2 id="drag-carousel-title" class="drag-carousel__title">Work we're proud to sign.</h2>
    </div>
    <div class="drag-carousel__controls">
      <p class="drag-carousel__count" aria-hidden="true"><span class="drag-carousel__current">01</span> / 06</p>
      <button class="drag-carousel__btn" type="button" data-dir="-1" aria-label="Previous project">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M19 12H5M11 18l-6-6 6-6" /></svg>
      </button>
      <button class="drag-carousel__btn" type="button" data-dir="1" aria-label="Next project">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </button>
    </div>
  </div>

  <ul class="drag-carousel__track" role="list">
    <li class="drag-carousel__slide" role="group" aria-roledescription="slide" aria-label="1 of 6">
      <a class="drag-carousel__card" href="#kitchen-remodel">
        <img class="drag-carousel__img" src="project-kitchen.jpg" alt="" width="720" height="900" loading="lazy" draggable="false">
        <span class="drag-carousel__meta"><span class="drag-carousel__tag">Kitchen</span><strong>Open-plan kitchen remodel</strong><small>Westlake · 3 weeks</small></span>
        <span class="drag-carousel__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
      </a>
    </li>
    <li class="drag-carousel__slide" role="group" aria-roledescription="slide" aria-label="2 of 6">
      <a class="drag-carousel__card" href="#bathroom">
        <img class="drag-carousel__img" src="project-bathroom.jpg" alt="" width="720" height="900" loading="lazy" draggable="false">
        <span class="drag-carousel__meta"><span class="drag-carousel__tag">Bathroom</span><strong>Walk-in shower conversion</strong><small>Riverside · 9 days</small></span>
        <span class="drag-carousel__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
      </a>
    </li>
    <li class="drag-carousel__slide" role="group" aria-roledescription="slide" aria-label="3 of 6">
      <a class="drag-carousel__card" href="#boiler">
        <img class="drag-carousel__img" src="project-boiler.jpg" alt="" width="720" height="900" loading="lazy" draggable="false">
        <span class="drag-carousel__meta"><span class="drag-carousel__tag">Heating</span><strong>High-efficiency boiler install</strong><small>Northside · 1 day</small></span>
        <span class="drag-carousel__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
      </a>
    </li>
    <li class="drag-carousel__slide" role="group" aria-roledescription="slide" aria-label="4 of 6">
      <a class="drag-carousel__card" href="#deck">
        <img class="drag-carousel__img" src="project-deck.jpg" alt="" width="720" height="900" loading="lazy" draggable="false">
        <span class="drag-carousel__meta"><span class="drag-carousel__tag">Outdoor</span><strong>Cedar deck with built-in seating</strong><small>Westlake · 2 weeks</small></span>
        <span class="drag-carousel__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
      </a>
    </li>
    <li class="drag-carousel__slide" role="group" aria-roledescription="slide" aria-label="5 of 6">
      <a class="drag-carousel__card" href="#rewire">
        <img class="drag-carousel__img" src="project-rewire.jpg" alt="" width="720" height="900" loading="lazy" draggable="false">
        <span class="drag-carousel__meta"><span class="drag-carousel__tag">Electrical</span><strong>Whole-home rewire and panel</strong><small>Downtown · 4 days</small></span>
        <span class="drag-carousel__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
      </a>
    </li>
    <li class="drag-carousel__slide" role="group" aria-roledescription="slide" aria-label="6 of 6">
      <a class="drag-carousel__card" href="#laundry">
        <img class="drag-carousel__img" src="project-laundry.jpg" alt="" width="720" height="900" loading="lazy" draggable="false">
        <span class="drag-carousel__meta"><span class="drag-carousel__tag">Plumbing</span><strong>Laundry room relocation</strong><small>Riverside · 5 days</small></span>
        <span class="drag-carousel__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
      </a>
    </li>
  </ul>

  <div class="drag-carousel__progress" aria-hidden="true"><span></span></div>
</section>
```

## CSS

```css
/* Section: header in the container, track full-bleed but aligned to it */
.drag-carousel {
  --drag-carousel-pad: max(var(--gutter), calc((100% - var(--container-max)) / 2 + var(--gutter)));
  overflow: hidden; padding-block: clamp(4rem, 9vw, 7rem); background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
}
.drag-carousel__head {
  display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 1.5rem;
  max-width: var(--container-max); margin: 0 auto 2rem; padding-inline: var(--gutter);
}
.drag-carousel__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.drag-carousel__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }

/* Controls */
.drag-carousel__controls { display: flex; align-items: center; gap: 0.5rem; }
.drag-carousel__count { margin: 0 0.75rem 0 0; color: var(--text-muted); font: 500 0.875rem var(--font-mono); font-variant-numeric: tabular-nums; }
.drag-carousel__current { color: var(--text-main); }
.drag-carousel__btn {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-light); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2), color var(--dur-2), opacity var(--dur-2);
}
.drag-carousel__btn svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.drag-carousel__btn:hover { background: var(--text-main); color: var(--surface-light); }
.drag-carousel__btn:active { transform: scale(0.92); }
.drag-carousel__btn:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.drag-carousel__btn[aria-disabled="true"] { opacity: 0.35; pointer-events: none; }
.drag-carousel:not(.drag-carousel--js) .drag-carousel__controls { display: none; }

/* Track: native scroll-snap; mouse dragging switches snapping off until release */
.drag-carousel__track {
  position: relative; display: flex; gap: 1.25rem; margin: 0; padding: 0.5rem var(--drag-carousel-pad) 1.5rem; list-style: none;
  overflow-x: auto; overscroll-behavior-x: contain; scroll-snap-type: x mandatory; scroll-padding-inline: var(--drag-carousel-pad);
  scrollbar-width: none; cursor: grab;
}
.drag-carousel__track::-webkit-scrollbar { display: none; }
.drag-carousel__track.is-dragging { scroll-snap-type: none; cursor: grabbing; user-select: none; }
.drag-carousel__track.is-dragging .drag-carousel__card { pointer-events: none; }
.drag-carousel__slide { flex: 0 0 clamp(15rem, 72vw, 22rem); scroll-snap-align: start; }

/* Card: photo, scrim, meta, arrow badge */
.drag-carousel__card {
  position: relative; isolation: isolate; display: block; aspect-ratio: 4 / 5; overflow: hidden; border-radius: var(--radius-2xl);
  background: var(--surface-deep); color: var(--text-inverse); text-decoration: none;
  box-shadow: 0 24px 48px -28px color-mix(in srgb, var(--surface-deep) 70%, transparent);
  transition: transform var(--dur-4) var(--ease-out), box-shadow var(--dur-4) var(--ease-out);
}
.drag-carousel__img { position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%; object-fit: cover; transition: transform var(--dur-5) var(--ease-out); }
.drag-carousel__card::before { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(180deg, transparent 40%, color-mix(in srgb, var(--surface-deep) 88%, transparent) 100%); }
.drag-carousel__meta { position: absolute; left: 1.25rem; right: 1.25rem; bottom: 1.25rem; display: grid; gap: 0.375rem; }
.drag-carousel__meta strong { font: 600 1.25rem/1.2 var(--font-display); letter-spacing: -0.015em; text-wrap: balance; }
.drag-carousel__meta small { color: var(--text-inverse-muted); font-size: 0.8125rem; }
.drag-carousel__tag { justify-self: start; padding: 0.25rem 0.625rem; border-radius: 999px; background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); font-size: 0.75rem; font-weight: 600; }
@supports (backdrop-filter: blur(1px)) { .drag-carousel__tag, .drag-carousel__arrow { backdrop-filter: blur(10px); } }
.drag-carousel__arrow {
  position: absolute; top: 1rem; right: 1rem; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: 50%;
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse);
  transition: transform var(--dur-4) var(--ease-spring), background-color var(--dur-3), color var(--dur-3);
}
.drag-carousel__arrow svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
@media (hover: hover) {
  .drag-carousel__card:hover { transform: translateY(-4px); box-shadow: 0 32px 60px -28px color-mix(in srgb, var(--surface-deep) 85%, transparent); }
  .drag-carousel__card:hover .drag-carousel__img { transform: scale(1.06); }
  .drag-carousel__card:hover .drag-carousel__arrow { transform: rotate(45deg); background: var(--surface-light); color: var(--text-main); }
}
.drag-carousel__card:focus-visible { outline: 2px solid var(--primary); outline-offset: 4px; }

/* Edge cards scale down and fade, driven by their own scroll position */
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .drag-carousel__slide { animation: drag-carousel-focus linear both; animation-timeline: view(inline); animation-range: cover 0% cover 100%; }
  }
}
@keyframes drag-carousel-focus {
  0% { opacity: 0.4; scale: 0.9; }
  20%, 80% { opacity: 1; scale: 1; }
  100% { opacity: 0.4; scale: 0.9; }
}

/* Progress thumb: as wide as the visible share, travels with scroll */
.drag-carousel__progress { position: relative; max-width: var(--container-max); height: 2px; margin: 1rem auto 0; overflow: hidden; border-radius: 2px; background: var(--border-subtle); }
.drag-carousel__progress { width: calc(100% - 2 * var(--gutter)); }
.drag-carousel__progress span {
  position: absolute; inset: 0 auto 0 0; width: calc(var(--ratio, 0.3) * 100%); border-radius: inherit; background: var(--text-main);
  transform: translateX(calc(var(--p, 0) * (1 / var(--ratio, 0.3) - 1) * 100%));
}
.drag-carousel:not(.drag-carousel--js) .drag-carousel__progress { display: none; }
```

## JS

```js
document.querySelectorAll('[data-drag-carousel]').forEach((root) => {
  const track = root.querySelector('.drag-carousel__track');
  const slides = [...track.children];
  const buttons = [...root.querySelectorAll('.drag-carousel__btn')];
  const counter = root.querySelector('.drag-carousel__current');
  const progress = root.querySelector('.drag-carousel__progress');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.classList.add('drag-carousel--js');

  // Snap positions measured from the first slide; go to the one nearest x
  const positions = () => slides.map((s) => s.offsetLeft - slides[0].offsetLeft);
  const nearest = (x) => positions().reduce((best, p, i, all) => (Math.abs(p - x) < Math.abs(all[best] - x) ? i : best), 0);
  const goTo = (i) => {
    const max = track.scrollWidth - track.clientWidth;
    track.scrollTo({ left: Math.min(positions()[Math.max(0, Math.min(i, slides.length - 1))], max), behavior: reduce ? 'auto' : 'smooth' });
  };
  buttons.forEach((b) => b.addEventListener('click', () => goTo(nearest(track.scrollLeft) + Number(b.dataset.dir))));

  // Keep counter, progress thumb and button states in sync with scroll
  const sync = () => {
    const max = Math.max(track.scrollWidth - track.clientWidth, 1);
    counter.textContent = String(nearest(track.scrollLeft) + 1).padStart(2, '0');
    progress.style.setProperty('--ratio', Math.min(track.clientWidth / track.scrollWidth, 1).toFixed(3));
    progress.style.setProperty('--p', Math.min(track.scrollLeft / max, 1).toFixed(3));
    buttons[0].setAttribute('aria-disabled', String(track.scrollLeft < 4));
    buttons[1].setAttribute('aria-disabled', String(track.scrollLeft > max - 4));
  };
  track.addEventListener('scroll', () => requestAnimationFrame(sync), { passive: true });
  addEventListener('resize', sync);
  sync();

  // Mouse drag with fling; capture only once it's really a drag so plain clicks still open links
  let drag = null;
  let swallowClick = false;
  track.addEventListener('pointerdown', (e) => {
    if (e.pointerType !== 'mouse' || e.button !== 0) return;
    drag = { id: e.pointerId, startX: e.clientX, left: track.scrollLeft, lastX: e.clientX, lastT: performance.now(), v: 0, active: false };
  });
  track.addEventListener('pointermove', (e) => {
    if (!drag) return;
    const dx = e.clientX - drag.startX;
    if (!drag.active && Math.abs(dx) > 6) {
      drag.active = true;
      track.setPointerCapture(drag.id);
      track.classList.add('is-dragging');
    }
    if (!drag.active) return;
    const now = performance.now();
    drag.v = (e.clientX - drag.lastX) / Math.max(now - drag.lastT, 1);
    drag.lastX = e.clientX;
    drag.lastT = now;
    track.scrollLeft = drag.left - dx;
  });
  const release = () => {
    if (drag?.active) {
      track.classList.remove('is-dragging');
      goTo(nearest(track.scrollLeft - drag.v * 280)); // fling: project the release velocity forward
      swallowClick = true;
    }
    drag = null;
  };
  track.addEventListener('pointerup', release);
  track.addEventListener('pointercancel', release);
  track.addEventListener('click', (e) => { if (swallowClick) { e.preventDefault(); swallowClick = false; } }, true);
});
```

## Notes

- Touch uses native scrolling with snap; the drag code only runs for mouse input. Keyboard users tab through the cards, and the browser scrolls each one into view.
- Without JS it's a swipeable, snapping row; the counter, buttons and progress bar hide.
- Prev/next use `aria-disabled` at the ends rather than `disabled`, so keyboard focus is never dropped.
- The edge fade uses scroll-driven animations (`view(inline)`). Without them every card is fully opaque.
- Photos: use a 4:5 crop; text sits on a gradient scrim, so any image keeps `--text-inverse` readable.
