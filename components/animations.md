# Animations

Scroll reveals, scroll-linked effects, rotating and shimmering headlines, loading states and attention pulses, all readable without JS and motionless under reduced motion. Depends on `tokens/variables.css`.

| #  | Pattern                                                                         | JS        |
| -- | ------------------------------------------------------------------------------- | --------- |
| 1  | **Reveal on scroll**: blocks fade and rise into place once as they enter view   | ~13 lines |
| 2  | **Staggered reveal**: children of a list or grid cascade in one after another   | ~15 lines |
| 3  | **Scroll progress bar**: reading-progress bar fixed to the top, pure CSS        | none      |
| 4  | **Parallax layers**: decorative shapes drifting at three speeds behind a band   | none      |
| 5  | **Rotating words headline**: one highlighted word cycles, with a pause control  | ~12 lines |
| 6  | **Skeleton loader**: card-shaped placeholders with a shimmer sweep              | none      |
| 7  | **Loaders**: spinner, bouncing dots and indeterminate bar as status regions     | none      |
| 8  | **Attention pulse**: expanding ring on a CTA and on a notification dot, 3 times | none      |
| 9  | **Shimmer headline**: a colored glint sweeps across the headline's letters      | none      |

## 1. Reveal on scroll

Fades and slides a block up the first time it scrolls into view. Nothing is hidden until the script gates `<html>` with `anim-reveal-ready`; under reduced motion content is simply shown, with no movement. Place inside your page container.

### HTML

```html
<div class="anim-reveal">
  <h2>Licensed, insured and on time</h2>
  <p>Every Brand crew is background-checked and arrives inside a two-hour window.</p>
</div>

<!-- Optional per-element delay to offset neighbors -->
<div class="anim-reveal" style="--anim-reveal-delay: 150ms">
  <p>Call (555) 555-0123 for a free estimate anywhere in Springfield.</p>
</div>
```

### CSS

```css
/* Start pose exists only once JS has gated <html>, and never in print or under reduced motion */
@media screen and (prefers-reduced-motion: no-preference) {
  .anim-reveal-ready .anim-reveal:not(.anim-reveal--in) {
    opacity: 0;
    transform: translateY(var(--space-lg));
  }
  .anim-reveal-ready .anim-reveal--in {
    animation: anim-reveal-in 0.6s cubic-bezier(0.2, 0.7, 0.2, 1) var(--anim-reveal-delay, 0s) both;
  }
}

/* Animates from the start pose to the element's own resting styles */
@keyframes anim-reveal-in {
  from { opacity: 0; transform: translateY(var(--space-lg)); }
}
```

### JS

```js
// Reveal on scroll: gate <html> only when the effect can run, then reveal each element once
const revealItems = document.querySelectorAll('.anim-reveal');
const revealReduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

if (revealItems.length && 'IntersectionObserver' in window && !revealReduced) {
  document.documentElement.classList.add('anim-reveal-ready');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('anim-reveal--in');
      revealObserver.unobserve(entry.target); // once per element
    });
  });
  revealItems.forEach((el) => {
    // Already on screen at load: leave it visible instead of hiding and fading it back in
    if (el.getBoundingClientRect().top < innerHeight) el.classList.remove('anim-reveal');
    else revealObserver.observe(el);
  });
}
```

### Notes

- The gate is added only when IntersectionObserver exists and motion is allowed, so no-JS, old browsers and reduced-motion users always see content. If the setting changes mid-visit, the CSS media query un-hides everything.
- The start pose is opacity-only on purpose: content stays in the accessibility tree, and focus, find-in-page and anchor jumps scroll it into view, which reveals it.
- Elements already on screen when the script runs are left visible (the class is removed), so there's no flash. Still, don't use it on the hero or LCP element.
- Don't put `.anim-reveal` on an element with its own transform or animation (e.g. a hover lift); wrap it instead.

## 2. Staggered reveal

Children of any list or grid cascade in. Children that enter the viewport together get an increasing `--anim-stagger-i`, so a single-column list on phones reveals row by row rather than all at once off-screen. Same gate approach as 1, with its own class `anim-stagger-ready`. Place inside your page container.

### HTML

```html
<ul class="anim-stagger anim-stagger--grid" role="list">
  <li class="anim-stagger__card">
    <h3>Free estimates</h3>
    <p>Written quotes within 24 hours, no obligation.</p>
  </li>
  <li class="anim-stagger__card">
    <h3>Upfront pricing</h3>
    <p>The price we quote is the price you pay.</p>
  </li>
  <li class="anim-stagger__card">
    <h3>2-year warranty</h3>
    <p>On every repair, parts and labor included.</p>
  </li>
</ul>
```

### CSS

```css
/* Delay = batch index × step. The script caps the index so big batches don't drag. */
.anim-stagger { --anim-stagger-step: 90ms; }

/* Start pose only behind the JS gate; direct children animate, whatever they are */
@media screen and (prefers-reduced-motion: no-preference) {
  .anim-stagger-ready .anim-stagger > :not(.anim-stagger__item--in, .anim-stagger__item--static) {
    opacity: 0;
    transform: translateY(var(--space-md));
  }
  .anim-stagger-ready .anim-stagger > .anim-stagger__item--in {
    animation: anim-stagger-in 0.5s cubic-bezier(0.2, 0.7, 0.2, 1) both;
    animation-delay: calc(var(--anim-stagger-i, 0) * var(--anim-stagger-step));
  }
}
@keyframes anim-stagger-in {
  from { opacity: 0; transform: translateY(var(--space-md)); }
}

/* Demo layout only: .anim-stagger works on any existing list or grid */
.anim-stagger--grid {
  display: grid; gap: var(--space-md);
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 15rem), 1fr));
  margin: 0; padding: 0; list-style: none;
}
.anim-stagger__card {
  padding: var(--space-lg); border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg); background: var(--surface-light);
  color: var(--text-main); box-shadow: var(--shadow-sm);
}
```

### JS

```js
// Staggered reveal: children entering the viewport together cascade by --anim-stagger-i
const staggerItems = document.querySelectorAll('.anim-stagger > *');
const staggerReduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

if (staggerItems.length && 'IntersectionObserver' in window && !staggerReduced) {
  document.documentElement.classList.add('anim-stagger-ready');
  const staggerObserver = new IntersectionObserver((entries) => {
    let i = 0; // position within this batch of newly visible children
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.style.setProperty('--anim-stagger-i', Math.min(i++, 8));
      entry.target.classList.add('anim-stagger__item--in');
      staggerObserver.unobserve(entry.target);
    });
  });
  staggerItems.forEach((el) => {
    // Already on screen at load: keep it visible instead of hiding and fading it back in
    if (el.getBoundingClientRect().top < innerHeight) el.classList.add('anim-stagger__item--static');
    else staggerObserver.observe(el);
  });
}
```

### Notes

- Add `anim-stagger` to an existing list or `.card-grid` and drop the demo `--grid`/`__card` classes. Only direct children animate.
- The index is capped at 8 (about 0.7s), so a wide screen showing many items at once still finishes quickly.
- CSS-only alternative: set `--anim-stagger-i` per `:nth-child`, or use `sibling-index()` where supported. Both count from the first child instead of per batch.
- No-JS, reduced-motion and print behavior match pattern 1: children are always visible.

## 3. Scroll progress bar

A thin `--primary` bar fixed to the top that fills as the page scrolls, with no JS. Not rendered where scroll-driven animations are unsupported or under reduced motion; decorative and `aria-hidden`, since the scrollbar already shows position. Place once per page, right after the site header.

### HTML

```html
<div class="anim-progress" aria-hidden="true"></div>
```

### CSS

```css
/* Not rendered unless the browser can drive it from the scroll position */
.anim-progress { display: none; }

@supports (animation-timeline: scroll()) {
  @media (prefers-reduced-motion: no-preference) {
    .anim-progress {
      display: block;
      position: fixed; inset: 0 0 auto; z-index: 30;
      height: 0.25rem;
      background: var(--primary);
      transform: scaleX(0); /* stays empty when the page can't scroll */
      transform-origin: 0 50%;
      animation: anim-progress-grow auto linear both;
      animation-timeline: scroll(root block); /* after the shorthand, which resets it */
    }
  }
  @keyframes anim-progress-grow {
    from { transform: scaleX(0); }
    to { transform: scaleX(1); }
  }
}
```

### Notes

- Scroll-driven animations: Chromium 115+ and Safari 26+. Other browsers don't show the bar.
- It shares z-index 30 with a sticky header. Put it after the header in the DOM so it paints on top.
- `scaleX()` keeps it on the compositor, with no layout work while scrolling. For RTL pages set `transform-origin: 100% 50%`.

## 4. Parallax layers

A full-bleed dark band whose three decorative layers drift at different speeds via `animation-timeline: view()`, static where unsupported and under reduced motion. Text is `--text-inverse`, at least 7:1 over every layer. Place between sections, not inside the page container.

### HTML

```html
<section class="anim-parallax" aria-labelledby="anim-parallax-title">
  <div class="anim-parallax__layers" aria-hidden="true">
    <span class="anim-parallax__layer anim-parallax__layer--back"></span>
    <span class="anim-parallax__layer anim-parallax__layer--mid"></span>
    <span class="anim-parallax__layer anim-parallax__layer--front"></span>
  </div>
  <div class="anim-parallax__inner">
    <h2 class="anim-parallax__title" id="anim-parallax-title">Built for Springfield weather</h2>
    <p class="anim-parallax__text">Roofs, siding and decks installed to handle summer storms and winter ice.</p>
  </div>
</section>
```

### CSS

```css
/* Dark band; overflow clips the drifting layers so nothing scrolls sideways */
.anim-parallax {
  position: relative; isolation: isolate; overflow: hidden;
  padding-block: var(--space-2xl);
  background: var(--surface-dark); color: var(--text-inverse);
}
.anim-parallax__inner {
  position: relative; z-index: 1;
  max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter);
}
.anim-parallax__title { margin: 0 0 var(--space-sm); font-size: clamp(1.5rem, 1.1rem + 2vw, 2.25rem); line-height: 1.2; }
.anim-parallax__text { margin: 0; max-width: 40rem; }

/* Every layer covers the band, so its view() timeline matches the section's.
   --anim-parallax-shift: positive = faster than the page (near), negative = slower (far). */
.anim-parallax__layers,
.anim-parallax__layer { position: absolute; inset: 0; }
.anim-parallax__layer::before { content: ""; position: absolute; border-radius: var(--radius-full); }

.anim-parallax__layer--back { --anim-parallax-shift: -2rem; }
.anim-parallax__layer--back::before {
  top: -6rem; right: -5rem; width: 18rem; height: 18rem;
  background: color-mix(in srgb, var(--primary) 35%, var(--surface-dark));
}
.anim-parallax__layer--mid { --anim-parallax-shift: 2.5rem; }
.anim-parallax__layer--mid::before {
  bottom: -3rem; left: 8%; width: 9rem; height: 9rem;
  border: 0.75rem solid color-mix(in srgb, var(--accent) 30%, var(--surface-dark));
}
.anim-parallax__layer--front { --anim-parallax-shift: 5rem; }
.anim-parallax__layer--front::before {
  top: 20%; right: 8%; width: 7rem; height: 7rem;
  background: radial-gradient(circle, color-mix(in srgb, var(--text-inverse-muted) 30%, transparent) 0.125rem, transparent 0.15rem) 0 0 / 1rem 1rem;
}

/* Scroll-linked drift, only where view() timelines exist and motion is welcome */
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .anim-parallax__layer {
      animation: anim-parallax-drift auto linear both;
      animation-timeline: view();
    }
  }
  @keyframes anim-parallax-drift {
    from { transform: translateY(var(--anim-parallax-shift)); }
    to { transform: translateY(calc(var(--anim-parallax-shift) * -1)); }
  }
}
```

### Notes

- Layers are `aria-hidden` and purely decorative. Never put content or meaningful images in them.
- Layer colors are `color-mix()` blends with `--surface-dark`, so `--text-inverse` stays at least 7:1 wherever a shape drifts behind the text. Don't switch body text to `--text-inverse-muted` here: over the dot layer it drops below 4.5:1.
- Keep shifts under about 5rem; large parallax distances can trigger motion discomfort even with reduced motion off.
- Support: Chromium 115+ and Safari 26+. Elsewhere the layers sit still and the band looks the same, minus the drift.
- Give each instance its own heading `id`.

## 5. Rotating words headline

A headline whose last word cycles through four options, with a pause control the script reveals before the loop starts. Screen readers get one static sentence; the animated copy is `aria-hidden`, and its slot is as wide as the longest word, so nothing reflows. Place inside your page container.

### HTML

```html
<div class="anim-words">
  <h2 class="anim-words__title">
    <span class="anim-words__sr">Springfield's go-to crew for repairs, remodels, roofing and gutters.</span>
    <span aria-hidden="true">Springfield's go-to crew for
      <span class="anim-words__window">
        <span class="anim-words__list">
          <span class="anim-words__word">repairs</span>
          <span class="anim-words__word">remodels</span>
          <span class="anim-words__word">roofing</span>
          <span class="anim-words__word">gutters</span>
          <span class="anim-words__word">repairs</span><!-- copy of the first word for a seamless loop -->
        </span>
      </span>
    </span>
  </h2>
  <button class="anim-words__toggle" type="button" hidden>
    <svg class="anim-words__icon anim-words__icon--pause" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M9 5v14M15 5v14" /></svg>
    <svg class="anim-words__icon anim-words__icon--play" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 5v14l12-7z" /></svg>
    <span class="anim-words__label">Pause</span><span class="anim-words__sr"> rotating words</span>
  </button>
</div>
```

### CSS

```css
/* Headline, then the pause control underneath */
.anim-words { display: grid; gap: var(--space-sm); justify-items: start; }
.anim-words__title {
  margin: 0; color: var(--text-main);
  font-size: clamp(1.75rem, 1.2rem + 2.5vw, 2.75rem); line-height: 1.2;
}
.anim-words__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

/* One-line window. A stacked list is as wide as its longest word, which reserves the width. */
.anim-words__window {
  display: inline-block; vertical-align: top;
  height: 1.2em; overflow: hidden; color: var(--primary);
}
.anim-words__list { display: flex; flex-direction: column; }
.anim-words__word { white-space: nowrap; }

/* 4 words + the copy: hold each for 20%, step by one item (100% / 5) */
@media (prefers-reduced-motion: no-preference) {
  .anim-words--running .anim-words__list { animation: anim-words-tick 10s ease-in-out infinite; }
}
.anim-words--paused .anim-words__list { animation-play-state: paused; }
@keyframes anim-words-tick {
  0%, 20% { transform: translateY(0); }
  25%, 45% { transform: translateY(-20%); }
  50%, 70% { transform: translateY(-40%); }
  75%, 95% { transform: translateY(-60%); }
  100% { transform: translateY(-80%); }
}

/* Pause/play toggle. [hidden] needs restating because display is set here. */
.anim-words__toggle {
  display: inline-flex; align-items: center; gap: var(--space-xs);
  min-height: 2rem; padding: var(--space-xs) var(--space-md);
  border: 1px solid var(--text-muted); border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main);
  font: inherit; font-size: 0.875rem; cursor: pointer;
  transition: background-color var(--transition-fast);
}
.anim-words__toggle[hidden] { display: none; }
.anim-words__toggle:hover { background: var(--surface-muted); }
.anim-words__toggle:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.anim-words__icon {
  width: 1rem; height: 1rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.anim-words__icon--play,
.anim-words--paused .anim-words__icon--pause { display: none; }
.anim-words--paused .anim-words__icon--play { display: block; }
@media (prefers-reduced-motion: reduce) {
  .anim-words__toggle { display: none; }
}
```

### JS

```js
// Rotating words: start the loop only where its pause control can be shown (WCAG 2.2.2)
const wordsReduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

document.querySelectorAll('.anim-words').forEach((el) => {
  const toggle = el.querySelector('.anim-words__toggle');
  const label = el.querySelector('.anim-words__label');
  if (wordsReduced || !toggle || !label) return;
  toggle.hidden = false;
  el.classList.add('anim-words--running');
  toggle.addEventListener('click', () => {
    const paused = el.classList.toggle('anim-words--paused');
    label.textContent = paused ? 'Play' : 'Pause';
  });
});
```

### Notes

- **Why a pause control, not a cycle cap:** WCAG 2.2.2 counts total running time. Four words at a readable pace take about 10s, so even one cycle needs a pause. The loop runs only after the button is shown. Without JS, or under reduced motion, the first word shows and stays.
- The heading's accessible name is the hidden sentence. Keep it in sync with the visible words. The button's name toggles between "Pause rotating words" and "Play rotating words".
- To use N words: keep a copy of the first word last, hold each for `100/N`% of the cycle and step by `-100/(N+1)`%.
- Keep the rotating slot at the end of the line, so the reserved width never leaves a gap mid-sentence. In a hero, make the heading the page's single `<h1>`.

## 6. Skeleton loader

Card-shaped placeholders with a light band sweeping each card three times, static under reduced motion. `aria-busy="true"` marks the region and visually hidden "Loading…" text names it. Place inside your page container.

### HTML

```html
<div class="anim-skeleton" aria-busy="true">
  <span class="anim-skeleton__sr">Loading…</span>
  <div class="anim-skeleton__card" aria-hidden="true">
    <div class="anim-skeleton__block anim-skeleton__block--media"></div>
    <div class="anim-skeleton__block anim-skeleton__block--title"></div>
    <div class="anim-skeleton__block"></div>
    <div class="anim-skeleton__block anim-skeleton__block--short"></div>
  </div>
  <!-- repeat the card for as many items as you expect -->
</div>
```

### CSS

```css
/* Same responsive grid the real cards will use */
.anim-skeleton {
  display: grid; gap: var(--space-md);
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 16rem), 1fr));
}
.anim-skeleton__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}
.anim-skeleton__card {
  position: relative; overflow: hidden;
  display: grid; gap: var(--space-sm); padding: var(--space-md);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  background: var(--surface-light);
}

/* Placeholder shapes */
.anim-skeleton__block { height: 0.75rem; border-radius: var(--radius-sm); background: var(--border-subtle); }
.anim-skeleton__block--media { height: auto; aspect-ratio: 16 / 9; margin-bottom: var(--space-xs); border-radius: var(--radius-md); }
.anim-skeleton__block--title { height: 1.25rem; width: 70%; }
.anim-skeleton__block--short { width: 45%; }

/* Shimmer: one light band per card, parked off-card and moved with transform only */
.anim-skeleton__card::after {
  content: ""; position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(90deg, transparent, color-mix(in srgb, var(--surface-light) 70%, transparent), transparent);
  transform: translateX(-100%);
}
@media (prefers-reduced-motion: no-preference) {
  .anim-skeleton__card::after { animation: anim-skeleton-sweep 1.6s ease-in-out 3; }
}
@keyframes anim-skeleton-sweep {
  from { transform: translateX(-100%); }
  to { transform: translateX(100%); }
}
```

### Notes

- When content arrives, replace the cards and set `aria-busy="false"`. The hidden "Loading…" is read on navigation but not announced on its own; for a spoken update, use a `role="status"` region (see 7).
- Three 1.6s sweeps (about 4.8s) keep it under WCAG 2.2.2's 5s limit. After that the grey blocks still read as loading. For an endless shimmer, add a pause control.
- Match block sizes to the real cards so the swap causes no layout shift.

## 7. Loaders

Spinner, three bouncing dots and an indeterminate bar, each a `role="status"` region with a visually hidden label. Under reduced motion the indicator freezes and the label becomes visible text. Place inside your page container.

### HTML

```html
<!-- Spinner -->
<div class="anim-loader" role="status">
  <span class="anim-loader__spinner" aria-hidden="true"></span>
  <span class="anim-loader__label">Loading your quote…</span>
</div>

<!-- Three bouncing dots -->
<div class="anim-loader" role="status">
  <span class="anim-loader__dots" aria-hidden="true">
    <span class="anim-loader__dot"></span><span class="anim-loader__dot"></span><span class="anim-loader__dot"></span>
  </span>
  <span class="anim-loader__label">Checking available times…</span>
</div>

<!-- Indeterminate bar -->
<div class="anim-loader anim-loader--bar" role="status">
  <span class="anim-loader__track" aria-hidden="true"><span class="anim-loader__fill"></span></span>
  <span class="anim-loader__label">Uploading photos…</span>
</div>
```

### CSS

```css
/* Shared: indicator and label in a row; override the color per surface */
.anim-loader {
  --anim-loader-color: var(--primary);
  --anim-loader-track: color-mix(in srgb, var(--anim-loader-color) 20%, transparent);
  position: relative;
  display: inline-flex; align-items: center; gap: var(--space-sm);
  color: var(--text-muted); font-size: 0.875rem;
}
.anim-loader__label {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

/* Spinner: ring with one colored quarter */
.anim-loader__spinner {
  box-sizing: border-box; width: 2rem; height: 2rem;
  border: 0.25rem solid var(--anim-loader-track); border-top-color: var(--anim-loader-color);
  border-radius: var(--radius-full);
  animation: anim-loader-spin 0.8s linear infinite;
}

/* Dots: top padding leaves room for the bounce */
.anim-loader__dots { display: inline-flex; gap: var(--space-xs); padding-top: var(--space-sm); }
.anim-loader__dot {
  width: 0.625rem; height: 0.625rem; border-radius: var(--radius-full);
  background: var(--anim-loader-color);
  animation: anim-loader-bounce 1.2s ease-in-out infinite;
}
.anim-loader__dot:nth-child(2) { animation-delay: 0.15s; }
.anim-loader__dot:nth-child(3) { animation-delay: 0.3s; }

/* Indeterminate bar: a 40% segment crossing the track */
.anim-loader--bar { display: flex; flex-direction: column; align-items: stretch; width: 100%; max-width: 20rem; }
.anim-loader__track { height: 0.25rem; overflow: hidden; border-radius: var(--radius-full); background: var(--anim-loader-track); }
.anim-loader__fill {
  display: block; width: 40%; height: 100%; border-radius: inherit;
  background: var(--anim-loader-color);
  animation: anim-loader-slide 1.4s ease-in-out infinite;
}

@keyframes anim-loader-spin { to { transform: rotate(1turn); } }
@keyframes anim-loader-bounce {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(calc(var(--space-sm) * -1)); }
}
@keyframes anim-loader-slide {
  from { transform: translateX(-100%); }
  to { transform: translateX(250%); }
}

/* Reduced motion: frozen indicator, label shown as visible text */
@media (prefers-reduced-motion: reduce) {
  .anim-loader__spinner, .anim-loader__dot, .anim-loader__fill { animation: none; }
  .anim-loader__fill { transform: translateX(75%); } /* centered segment */
  .anim-loader__label {
    position: static; width: auto; height: auto; margin: 0;
    overflow: visible; clip: auto; white-space: normal;
  }
}
```

### Notes

- `role="status"` announces changes, not content that is already there when the region is inserted. Keep the status element in the page and set its label text when loading starts. Remove the loader, or change the label to "Loaded", when done.
- These loop until removed. WCAG 2.2.2 treats a loading indicator as essential, because a stopped one reads as frozen. Keep waits short, and use determinate progress for long ones.
- The `--primary` arc, dots and fill are 5.2:1 on light surfaces. On `--surface-dark`, set `--anim-loader-color: var(--text-inverse)` and give the label `color: var(--text-inverse-muted)`.
- Set `aria-busy="true"` on the region being updated, and clear it when the loader goes away.

## 8. Attention pulse

Draws the eye with an expanding ring, on a primary CTA and on a small notification dot. It pulses three times (under 5s) and then stays still. There is no pulse under reduced motion. Place inside your page container.

### HTML

```html
<a class="anim-pulse anim-pulse--cta" href="#estimate">
  Book a free estimate
  <svg class="anim-pulse__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
</a>

<a class="anim-pulse anim-pulse--notify" href="#offers">
  Seasonal offers
  <span class="anim-pulse__dot" aria-hidden="true"></span>
  <span class="anim-pulse__sr">(new)</span>
</a>
```

### CSS

```css
/* Shared: ring color and positioning context */
.anim-pulse { --anim-pulse-color: var(--primary); position: relative; }
.anim-pulse:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.anim-pulse__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

/* CTA pill */
.anim-pulse--cta {
  display: inline-flex; align-items: center; gap: var(--space-sm);
  min-height: 2.75rem; padding: var(--space-sm) var(--space-lg);
  border-radius: var(--radius-full);
  background: var(--primary); color: var(--text-inverse);
  font-weight: 600; text-decoration: none;
  transition: background-color var(--transition-fast);
}
.anim-pulse--cta:hover { background: var(--primary-hover); }
.anim-pulse__icon {
  width: 1.25rem; height: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}

/* Text link with a notification dot */
.anim-pulse--notify {
  display: inline-flex; align-items: center; gap: var(--space-sm);
  min-height: 1.5rem; border-radius: var(--radius-sm);
  color: var(--primary); font-weight: 600; text-underline-offset: 0.2em;
  transition: color var(--transition-fast);
}
.anim-pulse--notify:hover { color: var(--primary-hover); }
.anim-pulse__dot {
  --anim-pulse-color: var(--danger);
  position: relative; flex: none; width: 0.625rem; height: 0.625rem;
  border-radius: var(--radius-full); background: var(--anim-pulse-color);
}

/* The ring rests at opacity 0, so it is gone once the iterations finish */
.anim-pulse--cta::after,
.anim-pulse__dot::after {
  content: ""; position: absolute; inset: 0; pointer-events: none;
  border-radius: inherit; opacity: 0;
}
.anim-pulse--cta::after { --anim-pulse-scale: 1.07, 1.35; border: 0.125rem solid var(--anim-pulse-color); }
.anim-pulse__dot::after { --anim-pulse-scale: 2.6; background: var(--anim-pulse-color); }

@media (prefers-reduced-motion: no-preference) {
  .anim-pulse--cta::after,
  .anim-pulse__dot::after { animation: anim-pulse-ring 1.6s ease-out 0.5s 3; }
}
@keyframes anim-pulse-ring {
  from { opacity: 0.6; transform: scale(1); }
  to { opacity: 0; transform: scale(var(--anim-pulse-scale)); }
}
```

### Notes

- Three 1.6s pulses (about 4.8s) stay under WCAG 2.2.2's 5s limit. Use one pulsing element per screen.
- The dot is `aria-hidden`. Its meaning is in the visually hidden "(new)", so the link reads "Seasonal offers (new)". `--danger` keeps the dot above 3:1 against white.
- `--anim-pulse-scale` (1.07 × 1.35) gives an even ring on a pill about 5:1 wide. For a round icon button, use one value, e.g. `1.3`. The ring reaches about 0.5rem beyond the control, which the page gutter covers at 320px.
- To pulse when the CTA scrolls into view rather than on load, put the `animation` rule behind a class that an IntersectionObserver adds, as in pattern 1.

## 9. Shimmer headline

A headline with a colored glint sweeping its letters twice (about 4.8s), using `background-clip: text`. Both gradient stops pass 4.5:1 on their surface, so every frame does; unsupported browsers and reduced motion get the solid base color. Place inside your page container.

### HTML

```html
<h2 class="anim-shimmer">Spring tune-up specials end Friday</h2>

<!-- On a --surface-dark section -->
<h2 class="anim-shimmer anim-shimmer--on-dark">Same-day service across Springfield</h2>
```

### CSS

```css
/* Solid token color first: what unsupported browsers and forced colors show */
.anim-shimmer {
  --anim-shimmer-base: var(--text-main);
  --anim-shimmer-glint: var(--primary);
  width: fit-content; max-width: 100%; margin: 0;
  font-size: clamp(1.75rem, 1.25rem + 2.5vw, 2.75rem); font-weight: 800; line-height: 1.15;
  color: var(--anim-shimmer-base);
}
/* Dark surfaces: every blend of these stays at least 6:1 on --surface-dark */
.anim-shimmer--on-dark {
  --anim-shimmer-base: var(--text-inverse-muted);
  --anim-shimmer-glint: var(--accent);
}

/* Gradient text where clipping works. The glint band starts parked off the left edge. */
@supports (background-clip: text) or (-webkit-background-clip: text) {
  .anim-shimmer {
    background: linear-gradient(100deg, var(--anim-shimmer-base) 40%, var(--anim-shimmer-glint) 50%, var(--anim-shimmer-base) 60%) 100% 0 / 250% 100% no-repeat;
    -webkit-background-clip: text; background-clip: text; /* after the shorthand, which resets it */
    -webkit-text-fill-color: transparent;
  }
  @media (prefers-reduced-motion: no-preference) {
    .anim-shimmer { animation: anim-shimmer-sweep 2.4s ease-in-out 0.3s 2 both; }
  }
}
@keyframes anim-shimmer-sweep {
  from { background-position: 100% 0; }
  to { background-position: 0 0; }
}

/* Forced colors: drop the gradient and use the system text color */
@media (forced-colors: active) {
  .anim-shimmer { background: none; -webkit-text-fill-color: currentColor; }
}
```

### Notes

- Contrast at every frame: the default blends `--text-main` into `--primary`. Every channel of `--text-main` is darker, so no mix is lighter than `--primary` (5.2:1 on white). `--on-dark` blends `--text-inverse-muted` into `--accent` and stays at least 6:1 on `--surface-dark`.
- It animates `background-position`, which repaints, because a text-clipped gradient can't be moved with a transform. It's short, limited to two sweeps and confined to one headline.
- The `-webkit-` declarations cover Safari and older Chromium. `width: fit-content` keeps the sweep on the words instead of empty line space.
- Don't use `--primary` text on the dark variant (3.4:1). Keep both stops to the pairings above.
