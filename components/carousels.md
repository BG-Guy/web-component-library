# Carousels

Seven sliders and rotators, from a swipeable card row to a zero-JS native carousel, all following the WAI-ARIA APG carousel model. Depends on `tokens/variables.css`.

| #  | Pattern                                                                                          | JS        |
| -- | ------------------------------------------------------------------------------------------------ | --------- |
| 1  | **Scroll-snap card carousel**: swipeable card row; prev/next scroll one card, disabled at the ends | ~17 lines |
| 2  | **Testimonial slider**: one quote at a time, swipe or prev/next/dots, announced on navigation      | ~24 lines |
| 3  | **Logo marquee**: endless logo strip with a pause button; static wrapped row under reduced motion   | ~12 lines |
| 4  | **Hero slideshow**: full-width crossfading slides, 6s auto-advance, play/pause plus prev/next       | ~24 lines |
| 5  | **Thumbnail gallery**: main photo swapped by a row of thumbnail buttons                             | ~12 lines |
| 6  | **Announcement ticker**: one-line rotating messages with a pause button, never announced            | ~21 lines |
| 7  | **Native CSS carousel**: `::scroll-button()` and `::scroll-marker` controls in Chrome 135+, swipe row elsewhere | none |

## 1. Scroll-snap card carousel

Cards on a native scroll-snap row (about 1.2 on phones, 3 from 768px). Prev/next scroll one card and set `aria-disabled` at the ends. Without JS the buttons are hidden and the row still swipes. Place inside your page container.

### HTML

```html
<section class="carousel-snap" aria-roledescription="carousel" aria-label="Our services">
  <div class="carousel-snap__head">
    <h2 class="carousel-snap__title">Our services</h2>
    <div class="carousel-snap__nav">
      <button class="carousel-snap__btn" type="button" data-dir="-1" aria-label="Previous services">
        <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m15 18-6-6 6-6" /></svg>
      </button>
      <button class="carousel-snap__btn" type="button" data-dir="1" aria-label="Next services">
        <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m9 18 6-6-6-6" /></svg>
      </button>
    </div>
  </div>
  <div class="carousel-snap__track">
    <div class="carousel-snap__slide" role="group" aria-roledescription="slide" aria-label="1 of 6">
      <img class="carousel-snap__img" src="roof-repair.jpg" alt="" width="640" height="400" loading="lazy">
      <div class="carousel-snap__body">
        <h3 class="carousel-snap__name">Roof repair</h3>
        <p class="carousel-snap__text">Leaks, missing shingles and storm damage, fixed within the week.</p>
        <a class="carousel-snap__link" href="https://example.com/roof-repair">Roof repair details</a>
      </div>
    </div>
    <div class="carousel-snap__slide" role="group" aria-roledescription="slide" aria-label="2 of 6">
      <img class="carousel-snap__img" src="gutters.jpg" alt="" width="640" height="400" loading="lazy">
      <div class="carousel-snap__body">
        <h3 class="carousel-snap__name">Gutter cleaning</h3>
        <p class="carousel-snap__text">Cleared, flushed and checked for leaks, twice a year.</p>
        <a class="carousel-snap__link" href="https://example.com/gutters">Gutter cleaning details</a>
      </div>
    </div>
    <!-- repeat per service; keep each aria-label "N of 6" -->
  </div>
</section>
```

### CSS

```css
/* Heading row: title left, prev/next right (buttons only once JS runs) */
.carousel-snap__head {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between;
  gap: var(--space-md); margin-block-end: var(--space-lg);
}
.carousel-snap__title { margin: 0; font-size: 1.5rem; line-height: 1.2; color: var(--text-main); }
.carousel-snap__nav { display: flex; gap: var(--space-sm); }
.carousel-snap:not(.carousel-snap--js) .carousel-snap__nav { display: none; }

/* Round icon buttons, dimmed at the ends */
.carousel-snap__btn {
  display: grid; place-items: center; inline-size: 2.75rem; block-size: 2.75rem; padding: 0;
  border: 1px solid var(--text-muted); border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); cursor: pointer;
  transition: background-color var(--transition-fast), opacity var(--transition-fast);
}
.carousel-snap__btn:hover { background: var(--surface-muted); }
.carousel-snap__btn:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.carousel-snap__btn[aria-disabled="true"] { opacity: 0.4; cursor: default; }
.carousel-snap__btn svg {
  inline-size: 1.25rem; block-size: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}

/* Track: native horizontal scroll with mandatory snap */
.carousel-snap__track {
  display: flex; gap: var(--space-md); padding-block-end: var(--space-sm);
  overflow-x: auto; overscroll-behavior-x: contain; scroll-snap-type: x mandatory; scrollbar-width: thin;
}
.carousel-snap__slide {
  flex: 0 0 85%; scroll-snap-align: start; display: flex; flex-direction: column; overflow: hidden;
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); background: var(--surface-light);
}
@media (min-width: 768px) {
  .carousel-snap__track { gap: var(--space-lg); }
  .carousel-snap__slide { flex-basis: calc((100% - 2 * var(--space-lg)) / 3); }
}

/* Card content; the link sits at the bottom so cards line up */
.carousel-snap__img { display: block; inline-size: 100%; block-size: auto; aspect-ratio: 16 / 10; object-fit: cover; }
.carousel-snap__body { display: flex; flex: 1; flex-direction: column; gap: var(--space-sm); padding: var(--space-md); }
.carousel-snap__name { margin: 0; font-size: 1.125rem; color: var(--text-main); }
.carousel-snap__text { margin: 0; font-size: 0.9375rem; line-height: 1.5; color: var(--text-muted); }
.carousel-snap__link {
  align-self: flex-start; margin-block-start: auto; border-radius: var(--radius-sm);
  color: var(--primary); font-weight: 600;
}
.carousel-snap__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
```

### JS

```js
// Prev/next scroll by one card (width + gap); aria-disabled marks the ends
document.querySelectorAll('.carousel-snap').forEach((root) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const track = root.querySelector('.carousel-snap__track');
  const buttons = root.querySelectorAll('.carousel-snap__btn');
  const [prev, next] = buttons;
  const update = () => {
    prev.setAttribute('aria-disabled', track.scrollLeft < 2);
    next.setAttribute('aria-disabled', track.scrollLeft > track.scrollWidth - track.clientWidth - 2);
  };
  buttons.forEach((btn) => btn.addEventListener('click', () => {
    const step = track.firstElementChild.offsetWidth + (parseFloat(getComputedStyle(track).columnGap) || 0);
    track.scrollBy({ left: step * btn.dataset.dir, behavior: reduce.matches ? 'auto' : 'smooth' });
  }));
  // Re-check when a scroll settles (scrollend, or scroll where unsupported) and on resize
  track.addEventListener('onscrollend' in window ? 'scrollend' : 'scroll', update, { passive: true });
  new ResizeObserver(update).observe(track);
  root.classList.add('carousel-snap--js');
});
```

### Notes

- The end buttons use `aria-disabled` rather than `disabled`, so keyboard focus isn't dropped when "Next" reaches the end. Clicks there are no-ops anyway.
- Mandatory snap absorbs sub-pixel rounding in the step, so every click lands cleanly on a card edge.
- Keep one link per card. Focusing it scrolls the card into view, which is how keyboard users move through the row without JS.
- `scrollend` is used where supported; elsewhere it falls back to `scroll`. The check is just two reads, so that's cheap.

## 2. Testimonial slider

One quote at a time on a full-width snap track, so it swipes natively and works without JS. Prev/next and dots scroll it. Off-screen slides are `inert`, and a polite live region speaks only after the user navigates. Place inside your page container.

### HTML

```html
<section class="carousel-quotes" aria-roledescription="carousel" aria-label="Customer testimonials">
  <div class="carousel-quotes__track">
    <div class="carousel-quotes__slide" role="group" aria-roledescription="slide" aria-label="1 of 3">
      <figure class="carousel-quotes__figure">
        <blockquote class="carousel-quotes__quote">
          <p>“They replaced our water heater the same afternoon and left the basement cleaner than they found it.”</p>
        </blockquote>
        <figcaption class="carousel-quotes__cite">Dana R. · Springfield</figcaption>
      </figure>
    </div>
    <div class="carousel-quotes__slide" role="group" aria-roledescription="slide" aria-label="2 of 3">
      <figure class="carousel-quotes__figure">
        <blockquote class="carousel-quotes__quote">
          <p>“Clear quote, no surprises, and the crew showed up exactly when they said they would.”</p>
        </blockquote>
        <figcaption class="carousel-quotes__cite">Sam K. · Northside</figcaption>
      </figure>
    </div>
    <!-- slide 3 of 3: same markup -->
  </div>
  <div class="carousel-quotes__controls">
    <button class="carousel-quotes__btn" type="button" data-step="-1" aria-label="Previous testimonial">
      <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m15 18-6-6 6-6" /></svg>
    </button>
    <div class="carousel-quotes__dots">
      <button class="carousel-quotes__dot" type="button" aria-label="Show testimonial 1" aria-current="true"></button>
      <button class="carousel-quotes__dot" type="button" aria-label="Show testimonial 2"></button>
      <button class="carousel-quotes__dot" type="button" aria-label="Show testimonial 3"></button>
    </div>
    <button class="carousel-quotes__btn" type="button" data-step="1" aria-label="Next testimonial">
      <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m9 18 6-6-6-6" /></svg>
    </button>
  </div>
  <div class="carousel-quotes__live carousel-quotes__sr" aria-live="polite" aria-atomic="true"></div>
</section>
```

### CSS

```css
/* Full-width slides on a mandatory snap row; swipeable with or without JS */
.carousel-quotes { max-inline-size: 48rem; margin-inline: auto; text-align: center; }
.carousel-quotes__track {
  display: flex; overflow-x: auto; overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory; scrollbar-width: thin;
}
.carousel-quotes__slide { flex: 0 0 100%; scroll-snap-align: start; scroll-snap-stop: always; }
.carousel-quotes__figure { margin: 0; padding: var(--space-lg) var(--space-md); }
.carousel-quotes__quote { margin: 0; font-size: 1.25rem; line-height: 1.5; color: var(--text-main); }
.carousel-quotes__quote p { margin: 0; }
.carousel-quotes__cite { margin-block-start: var(--space-md); font-size: 0.9375rem; color: var(--text-muted); }
@media (min-width: 768px) {
  .carousel-quotes__quote { font-size: 1.5rem; }
}

/* Controls exist only with JS; the scrollbar is then redundant */
.carousel-quotes__controls { display: none; }
.carousel-quotes--js .carousel-quotes__controls {
  display: flex; align-items: center; justify-content: center; gap: var(--space-sm); margin-block-start: var(--space-md);
}
.carousel-quotes--js .carousel-quotes__track { scrollbar-width: none; }

/* Prev/next */
.carousel-quotes__btn {
  display: grid; place-items: center; inline-size: 2.75rem; block-size: 2.75rem; padding: 0;
  border: 1px solid var(--text-muted); border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); cursor: pointer;
  transition: background-color var(--transition-fast);
}
.carousel-quotes__btn:hover { background: var(--surface-muted); }
.carousel-quotes__btn svg {
  inline-size: 1.25rem; block-size: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}

/* Dots: 24px target, hollow vs filled so state isn't color alone */
.carousel-quotes__dots { display: flex; }
.carousel-quotes__dot {
  display: grid; place-items: center; inline-size: 1.5rem; block-size: 1.5rem; padding: 0;
  border: 0; border-radius: var(--radius-full); background: none; cursor: pointer;
}
.carousel-quotes__dot::before {
  content: ""; inline-size: 0.625rem; block-size: 0.625rem;
  border: 2px solid var(--text-muted); border-radius: var(--radius-full);
  transition: background-color var(--transition-fast), border-color var(--transition-fast);
}
.carousel-quotes__dot[aria-current="true"]::before { border-color: var(--primary); background: var(--primary); }
.carousel-quotes__btn:focus-visible,
.carousel-quotes__dot:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Live region: read by screen readers, not shown */
.carousel-quotes__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}
```

### JS

```js
// Buttons and dots scroll the snap track; the slide that settles in view becomes current
document.querySelectorAll('.carousel-quotes').forEach((root) => {
  const track = root.querySelector('.carousel-quotes__track');
  const slides = [...track.children];
  const dots = [...root.querySelectorAll('.carousel-quotes__dot')];
  const live = root.querySelector('.carousel-quotes__live');
  let current = -1, timer;
  // Off-screen slides go inert (hidden from AT); announce only after the first render
  const setCurrent = (i) => {
    if (i === current) return;
    slides.forEach((slide, n) => (slide.inert = n !== i));
    dots.forEach((dot, n) => dot.setAttribute('aria-current', n === i));
    if (current > -1) live.textContent = `${slides[i].getAttribute('aria-label')}: ${slides[i].textContent.replace(/\s+/g, ' ').trim()}`;
    current = i;
  };
  const go = (i) => {
    i = (i + slides.length) % slides.length;
    track.scrollTo({ left: i * track.clientWidth, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    setCurrent(i);
  };
  root.querySelectorAll('.carousel-quotes__controls button').forEach((btn) => btn.addEventListener('click', () => go(btn.dataset.step ? current + Number(btn.dataset.step) : dots.indexOf(btn))));
  // Swipes: sync once scrolling settles (debounced, so it works without scrollend too)
  const settle = () => setCurrent(Math.round(track.scrollLeft / track.clientWidth));
  track.addEventListener('scroll', () => { clearTimeout(timer); timer = setTimeout(settle, 100); }, { passive: true });
  root.classList.add('carousel-quotes--js');
  setCurrent(0);
});
```

### Notes

- Off-screen slides get `inert`, which hides them from assistive tech and the tab order. The track itself isn't inert, so swiping still works.
- The live region is written only after a button, dot or swipe, never on load. It reads the slide label plus the quote, e.g. "2 of 3: “Clear quote…” Sam K. · Northside".
- JS maps scroll position to an index with `scrollLeft / clientWidth`, so slides must stay exactly 100% wide with no gap. As written it's LTR only.
- `scroll-snap-stop: always` keeps a fast flick from skipping quotes.

## 3. Logo marquee

An endless logo strip. JS clones the list once (hidden from assistive tech) and shows a pause button; hover and focus also pause it. Without JS or under reduced motion it's a static wrapped row. Place inside your page container.

### HTML

```html
<section class="carousel-marquee" aria-roledescription="carousel" aria-label="Trusted partners">
  <div class="carousel-marquee__head">
    <h2 class="carousel-marquee__title">Trusted by Springfield builders and suppliers</h2>
    <button class="carousel-marquee__toggle" type="button">
      <svg class="carousel-marquee__icon carousel-marquee__icon--pause" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
      <svg class="carousel-marquee__icon carousel-marquee__icon--play" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M7 5v14l12-7z" /></svg>
      <span class="carousel-marquee__label">Pause</span>
    </button>
  </div>
  <div class="carousel-marquee__viewport">
    <div class="carousel-marquee__track">
      <ul class="carousel-marquee__list" role="list">
        <li><img class="carousel-marquee__logo" src="partner-1.svg" alt="Springfield Builders Guild" width="160" height="48" loading="lazy"></li>
        <li><img class="carousel-marquee__logo" src="partner-2.svg" alt="Riverside Lumber Supply" width="160" height="48" loading="lazy"></li>
        <li><img class="carousel-marquee__logo" src="partner-3.svg" alt="County Licensed Contractor" width="160" height="48" loading="lazy"></li>
        <!-- 6–10 logos; JS appends an aria-hidden copy of this list -->
      </ul>
    </div>
  </div>
</section>
```

### CSS

```css
/* Heading row with the pause button */
.carousel-marquee__head {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between;
  gap: var(--space-sm) var(--space-md); margin-block-end: var(--space-lg);
}
.carousel-marquee__title { margin: 0; font-size: 1rem; font-weight: 600; color: var(--text-muted); }

/* Default (no JS or reduced motion): static wrapped row; copy and button hidden */
.carousel-marquee__list {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: center;
  gap: var(--space-lg) var(--space-2xl); margin: 0; padding: 0; list-style: none;
}
.carousel-marquee__list[aria-hidden="true"],
.carousel-marquee__toggle { display: none; }
.carousel-marquee__logo { display: block; inline-size: auto; block-size: 2.5rem; }

/* Pause/play pill */
.carousel-marquee__toggle {
  align-items: center; gap: var(--space-xs); min-block-size: 2.75rem; padding-inline: var(--space-md);
  border: 1px solid var(--text-muted); border-radius: var(--radius-full); background: var(--surface-light);
  color: var(--text-main); font: inherit; font-size: 0.875rem; font-weight: 600; cursor: pointer;
}
.carousel-marquee__toggle:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.carousel-marquee__icon {
  inline-size: 1.125rem; block-size: 1.125rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.carousel-marquee__icon--play,
.carousel-marquee--paused .carousel-marquee__icon--pause { display: none; }
.carousel-marquee--paused .carousel-marquee__icon--play { display: block; }

/* Moving strip: JS + motion allowed only. Two equal lists + translateX(-50%) = seamless loop */
@media (prefers-reduced-motion: no-preference) {
  .carousel-marquee--js .carousel-marquee__toggle { display: inline-flex; }
  .carousel-marquee--js .carousel-marquee__viewport {
    overflow: hidden;
    mask-image: linear-gradient(90deg, transparent, var(--text-main) 10%, var(--text-main) 90%, transparent);
  }
  .carousel-marquee--js .carousel-marquee__track {
    display: flex; inline-size: max-content; animation: carousel-marquee-scroll 40s linear infinite;
  }
  .carousel-marquee--js .carousel-marquee__list,
  .carousel-marquee--js .carousel-marquee__list[aria-hidden="true"] {
    display: flex; flex-wrap: nowrap; padding-inline-end: var(--space-2xl); /* trailing gap = inner gap */
  }
  .carousel-marquee--paused .carousel-marquee__track,
  .carousel-marquee:hover .carousel-marquee__track,
  .carousel-marquee:focus-within .carousel-marquee__track { animation-play-state: paused; }
}
@keyframes carousel-marquee-scroll {
  to { transform: translateX(-50%); }
}
```

### JS

```js
// Clone the list once for a seamless loop, then wire the pause button
document.querySelectorAll('.carousel-marquee').forEach((root) => {
  const list = root.querySelector('.carousel-marquee__list');
  const copy = list.cloneNode(true);
  copy.setAttribute('aria-hidden', 'true');
  copy.inert = true; // also keeps any logo links out of the tab order
  list.after(copy);
  const label = root.querySelector('.carousel-marquee__label');
  root.querySelector('.carousel-marquee__toggle').addEventListener('click', () => {
    label.textContent = root.classList.toggle('carousel-marquee--paused') ? 'Play' : 'Pause';
  });
  root.classList.add('carousel-marquee--js');
});
```

### Notes

- Reduced motion is pure CSS: the strip, the copy and the button exist only inside `prefers-reduced-motion: no-preference`, so the JS needs no `matchMedia`.
- One list must be at least as wide as the widest viewport, or a gap shows before the loop restarts. Add logos if it isn't. Scale the duration at about 5–7s per logo.
- Logos sit in a plain list, not slide groups. They're all equivalent, and "slide 4 of 8" would only add noise.
- Alt text is the organization's name. Logotypes are exempt from contrast rules, but keep them legible at 2.5rem tall.

## 4. Hero slideshow

Full-bleed crossfading slides (photo, heading, CTA) that advance every 6s. Play/pause comes first in the tab order, then prev/next. Rotation holds on hover or keyboard focus and never starts under reduced motion. Only the active slide is exposed to assistive tech; without JS the slides form a swipe row.

### HTML

```html
<section class="carousel-hero" aria-roledescription="carousel" aria-label="Featured services">
  <div class="carousel-hero__controls">
    <button class="carousel-hero__btn carousel-hero__toggle" type="button" aria-label="Pause slideshow">
      <svg class="carousel-hero__icon carousel-hero__icon--pause" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
      <svg class="carousel-hero__icon carousel-hero__icon--play" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M7 5v14l12-7z" /></svg>
    </button>
    <button class="carousel-hero__btn" type="button" data-step="-1" aria-label="Previous slide">
      <svg class="carousel-hero__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m15 18-6-6 6-6" /></svg>
    </button>
    <button class="carousel-hero__btn" type="button" data-step="1" aria-label="Next slide">
      <svg class="carousel-hero__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m9 18 6-6-6-6" /></svg>
    </button>
  </div>
  <div class="carousel-hero__slides" aria-live="off">
    <div class="carousel-hero__slide carousel-hero__slide--active" role="group" aria-roledescription="slide" aria-label="1 of 3">
      <img class="carousel-hero__img" src="hero-roofing.jpg" alt="" width="1600" height="900" fetchpriority="high">
      <div class="carousel-hero__content">
        <h2 class="carousel-hero__title">Storm-proof roofing for Springfield homes</h2>
        <p class="carousel-hero__text">Free inspections and written quotes within 48 hours.</p>
        <a class="carousel-hero__cta" href="https://example.com/roofing">Book an inspection</a>
      </div>
    </div>
    <div class="carousel-hero__slide" role="group" aria-roledescription="slide" aria-label="2 of 3">
      <img class="carousel-hero__img" src="hero-kitchen.jpg" alt="" width="1600" height="900" loading="lazy">
      <div class="carousel-hero__content">
        <h2 class="carousel-hero__title">Kitchens rebuilt in weeks, not months</h2>
        <p class="carousel-hero__text">One crew from demolition to the final coat of paint.</p>
        <a class="carousel-hero__cta" href="https://example.com/kitchens">See kitchen projects</a>
      </div>
    </div>
    <!-- slide 3 of 3: same markup, loading="lazy" -->
  </div>
</section>
```

### CSS

```css
/* Full-bleed frame. Without JS the slides form a swipeable snap row */
.carousel-hero { position: relative; background: var(--surface-dark); color: var(--text-inverse); }
.carousel-hero__slides { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; }
.carousel-hero__slide {
  position: relative; flex: 0 0 100%; display: flex; align-items: flex-end;
  min-block-size: min(85svh, 34rem); scroll-snap-align: start;
}
@media (min-width: 768px) {
  .carousel-hero__slide { min-block-size: min(80svh, 40rem); }
}

/* With JS: slides stack in one grid cell and crossfade; visibility hides inactive ones from AT */
.carousel-hero--js .carousel-hero__slides { display: grid; overflow: hidden; }
.carousel-hero--js .carousel-hero__slide {
  grid-area: 1 / 1;
  transition: opacity var(--transition-smooth), visibility var(--transition-smooth);
}
.carousel-hero--js .carousel-hero__slide:not(.carousel-hero__slide--active) { opacity: 0; visibility: hidden; }

/* Photo plus a bottom-weighted scrim so the text stays above 4.5:1 */
.carousel-hero__img { position: absolute; inset: 0; inline-size: 100%; block-size: 100%; object-fit: cover; }
.carousel-hero__slide::after {
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(to top,
    color-mix(in srgb, var(--surface-dark) 90%, transparent) 35%,
    color-mix(in srgb, var(--surface-dark) 30%, transparent));
}

/* Inner wrapper aligned to the page container; bottom padding clears the controls */
.carousel-hero__content {
  position: relative; z-index: 1; box-sizing: border-box; inline-size: 100%;
  max-inline-size: var(--container-max); margin-inline: auto;
  padding: var(--space-2xl) var(--gutter) calc(2.75rem + var(--space-2xl));
}
.carousel-hero__title { max-inline-size: 20ch; margin: 0 0 var(--space-sm); font-size: 2rem; line-height: 1.15; color: var(--text-inverse); }
.carousel-hero__text { max-inline-size: 40ch; margin: 0 0 var(--space-lg); font-size: 1.125rem; line-height: 1.5; color: var(--text-inverse); }
@media (min-width: 768px) {
  .carousel-hero__title { font-size: 3rem; }
}
.carousel-hero__cta {
  display: inline-flex; align-items: center; min-block-size: 2.75rem; padding-inline: var(--space-lg);
  border-radius: var(--radius-md); background: var(--primary); color: var(--text-inverse);
  font-weight: 600; text-decoration: none; transition: background-color var(--transition-fast);
}
.carousel-hero__cta:hover { background: var(--primary-hover); }

/* Controls: first in the DOM (play/pause leads the tab order), shown bottom-right */
.carousel-hero__controls {
  position: absolute; z-index: 2; inset-inline: 0; inset-block-end: var(--space-lg);
  display: flex; justify-content: flex-end; gap: var(--space-sm);
  box-sizing: border-box; max-inline-size: var(--container-max); margin-inline: auto; padding-inline: var(--gutter);
  pointer-events: none;
}
.carousel-hero:not(.carousel-hero--js) .carousel-hero__controls { display: none; }
.carousel-hero__btn {
  display: grid; place-items: center; inline-size: 2.75rem; block-size: 2.75rem; padding: 0;
  border: 1px solid var(--text-inverse-muted); border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-dark) 75%, transparent); color: var(--text-inverse);
  cursor: pointer; pointer-events: auto; transition: background-color var(--transition-fast);
}
.carousel-hero__btn:hover { background: var(--surface-dark); }
.carousel-hero__btn:focus-visible,
.carousel-hero__cta:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }
.carousel-hero__icon {
  inline-size: 1.25rem; block-size: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.carousel-hero__icon--play,
.carousel-hero--stopped .carousel-hero__icon--pause { display: none; }
.carousel-hero--stopped .carousel-hero__icon--play { display: block; }
```

### JS

```js
// Auto-advance every 6s. Hover or keyboard focus holds it, the button stops it, reduced motion never starts it
document.querySelectorAll('.carousel-hero').forEach((root) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const slides = [...root.querySelectorAll('.carousel-hero__slide')];
  const toggle = root.querySelector('.carousel-hero__toggle');
  let index = 0, timer, stopped = reduce.matches;
  const show = (i) => {
    index = (i + slides.length) % slides.length;
    slides.forEach((slide, n) => slide.classList.toggle('carousel-hero__slide--active', n === index));
  };
  // Announce slide changes (aria-live polite) only while not rotating
  const sync = () => {
    const rotating = !stopped && !root.matches(':hover') && !root.querySelector(':focus-visible');
    clearInterval(timer);
    if (rotating) timer = setInterval(() => show(index + 1), 6000);
    root.querySelector('.carousel-hero__slides').setAttribute('aria-live', rotating ? 'off' : 'polite');
    toggle.setAttribute('aria-label', stopped ? 'Play slideshow' : 'Pause slideshow');
    root.classList.toggle('carousel-hero--stopped', stopped);
  };
  toggle.addEventListener('click', () => { stopped = !stopped; sync(); });
  root.querySelectorAll('[data-step]').forEach((btn) => btn.addEventListener('click', () => show(index + Number(btn.dataset.step))));
  ['mouseenter', 'mouseleave', 'focusin', 'focusout'].forEach((type) => root.addEventListener(type, () => setTimeout(sync)));
  reduce.addEventListener('change', () => { stopped ||= reduce.matches; sync(); });
  root.classList.add('carousel-hero--js');
  sync();
});
```

### Notes

- Rotation runs only when the slideshow isn't stopped, hovered or holding keyboard focus (APG). `aria-live` stays `off` while it rotates and switches to `polite` otherwise, so manual prev/next is announced but auto-advance never is.
- Under reduced motion it starts stopped, with the button labelled "Play slideshow". Users can still start it, and the crossfade is instant because the transition tokens collapse.
- Slide headings are `h2` because inactive slides are hidden. Keep the page `<h1>` outside the slideshow.
- The first image is eager with `fetchpriority="high"`, the rest lazy. With JS all slides share one frame, so the later images load right after the first and a crossfade never shows a blank.
- Photos are `alt=""` because they're a backdrop for the heading. Give real alt text if the photo carries information the text doesn't.

## 5. Thumbnail gallery

A main photo plus thumbnail buttons that swap its `src`/`alt` and move `aria-current`. The strip swipes horizontally on phones and wraps into a grid from 768px. Place inside your page container.

### HTML

```html
<section class="carousel-thumbs" aria-roledescription="carousel" aria-label="Deck build photos">
  <div class="carousel-thumbs__stage" role="group" aria-roledescription="slide" aria-label="1 of 4">
    <img class="carousel-thumbs__main" src="deck-1.jpg" alt="Finished cedar deck with built-in benches" width="1200" height="800" loading="lazy">
  </div>
  <ul class="carousel-thumbs__list" role="list">
    <li class="carousel-thumbs__item">
      <button class="carousel-thumbs__thumb" type="button" data-src="deck-1.jpg" aria-current="true"
              aria-label="Finished cedar deck with built-in benches">
        <img src="deck-1-thumb.jpg" alt="" width="160" height="120" loading="lazy">
      </button>
    </li>
    <li class="carousel-thumbs__item">
      <button class="carousel-thumbs__thumb" type="button" data-src="deck-2.jpg"
              aria-label="Deck stairs with recessed step lights">
        <img src="deck-2-thumb.jpg" alt="" width="160" height="120" loading="lazy">
      </button>
    </li>
    <!-- repeat per photo -->
  </ul>
</section>
```

### CSS

```css
/* Main photo: fixed 3:2 frame, so swapping images never shifts the layout */
.carousel-thumbs__stage { overflow: hidden; border-radius: var(--radius-lg); background: var(--border-subtle); }
.carousel-thumbs__main { display: block; inline-size: 100%; block-size: auto; aspect-ratio: 3 / 2; object-fit: cover; }

/* Thumbnails: one swipeable row on phones (padding keeps focus rings unclipped) */
.carousel-thumbs__list {
  display: grid; grid-auto-flow: column; grid-auto-columns: 5rem; gap: var(--space-sm);
  margin: var(--space-sm) 0 0; padding: var(--space-xs); list-style: none;
  overflow-x: auto; overscroll-behavior-x: contain; scroll-snap-type: x proximity; scrollbar-width: thin;
}
.carousel-thumbs__item { scroll-snap-align: start; }
@media (min-width: 768px) {
  .carousel-thumbs__list { grid-auto-flow: row; grid-template-columns: repeat(auto-fill, minmax(6rem, 1fr)); overflow: visible; }
}

/* Thumbnail button: dimmed until hovered or current; current also gets a primary border */
.carousel-thumbs__thumb {
  display: block; inline-size: 100%; padding: 0; overflow: hidden; cursor: pointer;
  border: 2px solid transparent; border-radius: var(--radius-md); background: var(--border-subtle);
  transition: border-color var(--transition-fast);
}
.carousel-thumbs__thumb img {
  display: block; inline-size: 100%; block-size: auto; aspect-ratio: 4 / 3; object-fit: cover;
  opacity: 0.7; transition: opacity var(--transition-fast);
}
.carousel-thumbs__thumb:hover img,
.carousel-thumbs__thumb[aria-current="true"] img { opacity: 1; }
.carousel-thumbs__thumb[aria-current="true"] { border-color: var(--primary); }
.carousel-thumbs__thumb:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
```

### JS

```js
// Thumbnail click: swap the main image, move aria-current, update the slide label
document.querySelectorAll('.carousel-thumbs').forEach((root) => {
  const main = root.querySelector('.carousel-thumbs__main');
  const stage = root.querySelector('.carousel-thumbs__stage');
  const thumbs = [...root.querySelectorAll('.carousel-thumbs__thumb')];
  thumbs.forEach((thumb, i) => thumb.addEventListener('click', () => {
    thumbs.forEach((t) => t.removeAttribute('aria-current'));
    thumb.setAttribute('aria-current', 'true');
    main.src = thumb.dataset.src;
    main.alt = thumb.getAttribute('aria-label');
    stage.setAttribute('aria-label', `${i + 1} of ${thumbs.length}`);
  }));
});
```

### Notes

- Each button's `aria-label` describes its photo and doubles as the main image's new `alt`, so the thumbnail `<img>` stays `alt=""`. That keeps one source of truth.
- Without JS every photo is still visible as a thumbnail. To make full-size photos reachable without JS too, use links (`href` = full image) and call `preventDefault()` in the handler.
- The main image is lazy because galleries usually sit below the fold. Drop `loading="lazy"` if it's the first thing on the page. If you use `srcset`, swap a `data-srcset` alongside `data-src`.

## 6. Announcement ticker

A one-line bar that fades and slides through 3–4 messages every 5s, with a pause button first. Rotation holds on hover or keyboard focus, is never announced, and stays on the first message under reduced motion. Without JS all messages are listed. Full-bleed with its own inner wrapper.

### HTML

```html
<section class="carousel-ticker" aria-roledescription="carousel" aria-label="Announcements">
  <div class="carousel-ticker__inner">
    <button class="carousel-ticker__toggle" type="button" aria-label="Pause announcements">
      <svg class="carousel-ticker__icon carousel-ticker__icon--pause" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
      <svg class="carousel-ticker__icon carousel-ticker__icon--play" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M7 5v14l12-7z" /></svg>
    </button>
    <div class="carousel-ticker__track">
      <div class="carousel-ticker__msg carousel-ticker__msg--active" role="group" aria-roledescription="slide" aria-label="1 of 3">
        Spring special: 15% off gutter cleaning through May. <a class="carousel-ticker__link" href="https://example.com/offers">See offers</a>
      </div>
      <div class="carousel-ticker__msg" role="group" aria-roledescription="slide" aria-label="2 of 3">
        24/7 emergency repairs: <a class="carousel-ticker__link" href="tel:+15555550123">(555) 555-0123</a>
      </div>
      <div class="carousel-ticker__msg" role="group" aria-roledescription="slide" aria-label="3 of 3">
        Licensed and insured in Springfield since 2009
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
/* Full-bleed dark bar with its own inner wrapper */
.carousel-ticker { background: var(--surface-dark); color: var(--text-inverse); font-size: 0.875rem; line-height: 1.4; }
.carousel-ticker__inner {
  display: flex; align-items: center; gap: var(--space-sm);
  max-inline-size: var(--container-max); margin-inline: auto; padding: var(--space-xs) var(--gutter);
}
.carousel-ticker__track { flex: 1; min-inline-size: 0; padding-block: var(--space-sm); text-align: center; }
.carousel-ticker__link { border-radius: var(--radius-sm); color: var(--text-inverse); font-weight: 600; text-underline-offset: 2px; }

/* With JS: messages share one grid cell (height = longest, no jump) and fade/slide in */
.carousel-ticker--js .carousel-ticker__track { display: grid; }
.carousel-ticker--js .carousel-ticker__msg {
  grid-area: 1 / 1;
  transition: opacity var(--transition-smooth), translate var(--transition-smooth), visibility var(--transition-smooth);
}
.carousel-ticker--js .carousel-ticker__msg:not(.carousel-ticker__msg--active) {
  opacity: 0; translate: 0 var(--space-sm); visibility: hidden;
}

/* Pause/play: 32px icon button, hidden without JS */
.carousel-ticker__toggle {
  display: none; flex: none; place-items: center; inline-size: 2rem; block-size: 2rem; padding: 0;
  border: 0; border-radius: var(--radius-full); background: none; color: var(--text-inverse); cursor: pointer;
  transition: background-color var(--transition-fast);
}
.carousel-ticker--js .carousel-ticker__toggle { display: grid; }
.carousel-ticker__toggle:hover { background: color-mix(in srgb, var(--text-inverse) 15%, transparent); }
.carousel-ticker__toggle:focus-visible,
.carousel-ticker__link:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }
.carousel-ticker__icon {
  inline-size: 1rem; block-size: 1rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.carousel-ticker__icon--play,
.carousel-ticker--stopped .carousel-ticker__icon--pause { display: none; }
.carousel-ticker--stopped .carousel-ticker__icon--play { display: block; }
```

### JS

```js
// Rotate every 5s unless stopped, hovered or keyboard-focused. No live region: rotation stays silent
document.querySelectorAll('.carousel-ticker').forEach((root) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const msgs = [...root.querySelectorAll('.carousel-ticker__msg')];
  const toggle = root.querySelector('.carousel-ticker__toggle');
  let index = 0, timer, stopped = reduce.matches;
  const next = () => {
    index = (index + 1) % msgs.length;
    msgs.forEach((msg, n) => msg.classList.toggle('carousel-ticker__msg--active', n === index));
  };
  const sync = () => {
    clearInterval(timer);
    if (!stopped && !root.matches(':hover') && !root.querySelector(':focus-visible')) timer = setInterval(next, 5000);
    toggle.setAttribute('aria-label', stopped ? 'Play announcements' : 'Pause announcements');
    root.classList.toggle('carousel-ticker--stopped', stopped);
  };
  toggle.addEventListener('click', () => { stopped = !stopped; sync(); });
  ['mouseenter', 'mouseleave', 'focusin', 'focusout'].forEach((type) => root.addEventListener(type, () => setTimeout(sync)));
  reduce.addEventListener('change', () => { stopped ||= reduce.matches; sync(); });
  root.classList.add('carousel-ticker--js');
  sync();
});
```

### Notes

- There's deliberately no `aria-live`: announcing every 5s would interrupt screen readers. Inactive messages use `visibility: hidden`, so only the current one is read and links in hidden messages can't take focus.
- All messages share one grid cell, so the bar is as tall as the longest message. It doesn't jump when a message wraps at 320px.
- Under reduced motion it starts stopped on the first message. Play still lets users read the others, with instant swaps.
- Keep messages under about 60 characters. If the bar is sticky, use `z-index: 50` (the banner layer).

## 7. Native CSS carousel

Project cards whose prev/next buttons and dot markers are generated by CSS (`::scroll-button()`, `::scroll-marker`) inside an `@supports` guard. No JS; other browsers get the same swipeable snap row without controls. Place inside your page container.

### HTML

```html
<section class="carousel-native" aria-roledescription="carousel" aria-label="Recent projects">
  <h2 class="carousel-native__title">Recent projects</h2>
  <div class="carousel-native__viewport">
    <div class="carousel-native__track">
      <div class="carousel-native__slide" role="group" aria-roledescription="slide" aria-label="1 of 5">
        <img class="carousel-native__img" src="project-patio.jpg" alt="Stone patio with a built-in fire pit" width="800" height="600" loading="lazy">
        <h3 class="carousel-native__name"><a class="carousel-native__link" href="https://example.com/projects/patio">Backyard patio · Northside</a></h3>
      </div>
      <div class="carousel-native__slide" role="group" aria-roledescription="slide" aria-label="2 of 5">
        <img class="carousel-native__img" src="project-bath.jpg" alt="Walk-in shower with grey slate tile" width="800" height="600" loading="lazy">
        <h3 class="carousel-native__name"><a class="carousel-native__link" href="https://example.com/projects/bath">Bathroom remodel · Westlake</a></h3>
      </div>
      <!-- repeat per project; keep each aria-label "N of 5" -->
    </div>
  </div>
</section>
```

### CSS

```css
/* Baseline (every browser): swipeable snap row, ~1.2 cards on phones, 3 from 768px */
.carousel-native__title { margin: 0 0 var(--space-lg); font-size: 1.5rem; line-height: 1.2; color: var(--text-main); }
.carousel-native__track {
  display: flex; gap: var(--space-md); padding-block-end: var(--space-sm);
  overflow-x: auto; overscroll-behavior-x: contain; scroll-snap-type: x mandatory; scrollbar-width: thin;
}
.carousel-native__slide { flex: 0 0 85%; scroll-snap-align: start; }
@media (min-width: 768px) {
  .carousel-native__track { gap: var(--space-lg); }
  .carousel-native__slide { flex-basis: calc((100% - 2 * var(--space-lg)) / 3); }
}
.carousel-native__img { display: block; inline-size: 100%; block-size: auto; aspect-ratio: 4 / 3; object-fit: cover; border-radius: var(--radius-lg); }
.carousel-native__name { margin: 0; padding: var(--space-sm) var(--space-xs) 0; font-size: 1rem; }
.carousel-native__link { border-radius: var(--radius-sm); color: var(--text-main); text-decoration: none; }
.carousel-native__link:hover { color: var(--primary); text-decoration: underline; }
.carousel-native__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Chrome 135+: generated buttons and markers. The track stays unpositioned, so they're placed
   against __viewport and don't scroll with the cards */
@supports (scroll-marker-group: after) {
  .carousel-native__viewport { position: relative; padding-block-end: calc(2.75rem + var(--space-md)); }
  .carousel-native__track { scroll-marker-group: after; scrollbar-width: none; }
  @media (prefers-reduced-motion: no-preference) {
    .carousel-native__track { scroll-behavior: smooth; }
  }

  /* Prev/next: content alt text is the accessible name; auto-disabled at the ends */
  .carousel-native__track::scroll-button(*) {
    position: absolute; inset-block-end: 0; inline-size: 2.75rem; block-size: 2.75rem;
    border: 1px solid var(--text-muted); border-radius: var(--radius-full);
    background: var(--surface-light); color: var(--text-main); font-size: 1.25rem; cursor: pointer;
    transition: background-color var(--transition-fast), opacity var(--transition-fast);
  }
  .carousel-native__track::scroll-button(inline-start) { content: "\2190" / "Previous projects"; inset-inline-start: 0; }
  .carousel-native__track::scroll-button(inline-end) { content: "\2192" / "Next projects"; inset-inline-end: 0; }
  .carousel-native__track::scroll-button(*):hover { background: var(--surface-muted); }
  .carousel-native__track::scroll-button(*):disabled { opacity: 0.4; cursor: default; }
  .carousel-native__track::scroll-button(*):focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

  /* Dot markers centered between the buttons; the text (slide label) is the name, visually hidden */
  .carousel-native__track::scroll-marker-group {
    position: absolute; inset-block-end: 0; inset-inline: calc(2.75rem + var(--space-sm));
    display: flex; flex-wrap: wrap; align-items: center; justify-content: center; min-block-size: 2.75rem;
  }
  .carousel-native__slide::scroll-marker {
    content: attr(aria-label); box-sizing: border-box; inline-size: 1.5rem; block-size: 1.5rem;
    padding: var(--space-sm); border-radius: var(--radius-full); background: var(--text-muted) content-box;
    overflow: hidden; white-space: nowrap; text-indent: 1.5rem;
    transition: padding var(--transition-fast), background-color var(--transition-fast);
  }
  .carousel-native__slide::scroll-marker:target-current { padding: var(--space-xs); background-color: var(--primary); }
  .carousel-native__slide::scroll-marker:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
}
```

### Notes

- **Support:** `::scroll-button()`, `::scroll-marker`, `scroll-marker-group` and `:target-current` are Chrome/Edge 135+ only for now. Firefox and Safari skip the `@supports` block and get the plain swipe row, where keyboard users Tab through the project links. If you need controls in every browser, use pattern 1.
- Don't give the track `position`, `transform` or `contain`. That would make it the containing block, and the generated controls would scroll away with the cards.
- Chrome exposes the markers as a tablist: Tab into it, then use the arrow keys. Marker names come from each slide's `aria-label` via `attr()` (e.g. "3 of 5"), and the arrows are named by their `content` alt text.
- Scroll buttons move by roughly one visible width (3 cards from 768px) and disable themselves at the ends.
