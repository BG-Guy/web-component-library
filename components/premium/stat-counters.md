# Stat Counters

Headline numbers that roll in like an odometer when the section scrolls into view. Each digit wheel spins through a full turn and settles on its value, one column after another. A gradient rule draws across each stat, and a small visual finishes beneath: a sparkline, stars, a progress ring, a live pulse. The real numbers are in the HTML, so there's no "0" without JS. Depends on `tokens/variables.css`.

**Motion:** per-digit odometer wheels (staggered, ease-out) · gradient rule draw · sparkline stroke draw · star fill · ring close · live pulse (3×).

## HTML

```html
<section class="counter-stats" aria-labelledby="counter-stats-title" data-counter-stats>
  <div class="counter-stats__inner">
    <h2 id="counter-stats-title" class="counter-stats__title">Fifteen years of showing up on time.</h2>
    <ul class="counter-stats__list" role="list">
      <li class="counter-stats__item">
        <p class="counter-stats__value"><span class="counter-stats__num" data-counter>12,480</span><span class="counter-stats__unit">+</span></p>
        <p class="counter-stats__label">Jobs completed since 2009</p>
        <svg class="counter-stats__spark" viewBox="0 0 120 32" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M1 29 20 25l20 2 20-10 20 2 20-10 18-6" pathLength="1" /></svg>
      </li>
      <li class="counter-stats__item">
        <p class="counter-stats__value"><span class="counter-stats__num" data-counter>4.9</span><span class="counter-stats__unit">/5</span></p>
        <p class="counter-stats__label">Average rating, 1,248 reviews</p>
        <span class="counter-stats__stars" aria-hidden="true"><span>★★★★★</span>★★★★★</span>
      </li>
      <li class="counter-stats__item">
        <p class="counter-stats__value"><span class="counter-stats__num" data-counter>98</span><span class="counter-stats__unit">%</span></p>
        <p class="counter-stats__label">Arrivals inside the booked window</p>
        <svg class="counter-stats__ring" viewBox="0 0 36 36" aria-hidden="true" focusable="false">
          <circle class="counter-stats__ring-track" cx="18" cy="18" r="15" />
          <circle class="counter-stats__ring-fill" cx="18" cy="18" r="15" pathLength="100" style="--pct: 98" />
        </svg>
      </li>
      <li class="counter-stats__item">
        <p class="counter-stats__value"><span class="counter-stats__num" data-counter>38</span><span class="counter-stats__unit">sec</span></p>
        <p class="counter-stats__label">Average time to answer, 24/7</p>
        <span class="counter-stats__pulse" aria-hidden="true">Live</span>
      </li>
    </ul>
  </div>
</section>
```

## CSS

```css
.counter-stats { background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); }
.counter-stats__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 8vw, 6rem) var(--gutter); }
.counter-stats__title { max-width: 28rem; margin: 0 0 3rem; font: 600 clamp(1.75rem, 1.2rem + 2vw, 2.5rem)/1.1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.counter-stats__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Grid: 2×2, then one row with hairline separators */
.counter-stats__list { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2.5rem 1.5rem; margin: 0; padding: 0; list-style: none; }
@media (min-width: 1024px) { .counter-stats__list { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 2rem; } }
.counter-stats__item { position: relative; display: grid; align-content: start; gap: 0.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border-subtle); }
.counter-stats__item::before { /* gradient rule that draws across */
  content: ""; position: absolute; top: -1px; left: 0; right: 0; height: 2px; border-radius: 2px;
  background: var(--gradient-brand); transform-origin: left;
  transition: transform calc(var(--dur-5) * 1.6) var(--ease-out);
}
.counter-stats__item:nth-child(2)::before { transition-delay: 120ms; }
.counter-stats__item:nth-child(3)::before { transition-delay: 240ms; }
.counter-stats__item:nth-child(4)::before { transition-delay: 360ms; }

/* Number: odometer wheels, each digit a 1em window over a 0–9 ×2 strip */
.counter-stats__value { display: flex; align-items: baseline; gap: 0.25rem; margin: 0; }
.counter-stats__num { font: 600 clamp(2.75rem, 1.9rem + 3.4vw, 4.25rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }
.counter-stats__digits { display: inline-flex; }
.counter-stats__wheel { display: inline-block; height: 1em; overflow: hidden; }
.counter-stats__strip { display: flex; flex-direction: column; transition: transform calc(var(--dur-5) * 2.2) var(--ease-out); transition-delay: calc(var(--c) * 90ms + 100ms); }
.counter-stats__strip > span { display: block; height: 1em; }
.counter-stats__unit { color: var(--primary); font: 600 clamp(1.25rem, 1rem + 1vw, 1.75rem)/1 var(--font-display); }
.counter-stats__label { margin: 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.45; }

/* Small visuals under each label */
.counter-stats__spark { width: 7.5rem; height: 2rem; margin-top: 0.5rem; overflow: visible; }
.counter-stats__spark path { fill: none; stroke: var(--primary); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 1; stroke-dashoffset: 0; transition: stroke-dashoffset calc(var(--dur-5) * 1.8) var(--ease-out) 300ms; }
.counter-stats__stars { position: relative; justify-self: start; margin-top: 0.5rem; color: var(--border-subtle); font-size: 1.125rem; letter-spacing: 0.12em; }
.counter-stats__stars span { position: absolute; inset: 0 auto 0 0; width: 98%; overflow: hidden; color: var(--accent); white-space: nowrap; transition: width calc(var(--dur-5) * 1.6) var(--ease-out) 300ms; }
.counter-stats__ring { width: 2.75rem; height: 2.75rem; margin-top: 0.25rem; rotate: -90deg; }
.counter-stats__ring circle { fill: none; stroke-width: 3.5; }
.counter-stats__ring-track { stroke: var(--border-subtle); }
.counter-stats__ring-fill { stroke: var(--primary-2); stroke-linecap: round; stroke-dasharray: 100px; stroke-dashoffset: calc((100 - var(--pct)) * 1px); transition: stroke-dashoffset calc(var(--dur-5) * 1.8) var(--ease-out) 300ms; }
.counter-stats__pulse { position: relative; justify-self: start; display: inline-flex; align-items: center; gap: 0.5rem; margin-top: 0.5rem; padding: 0.25rem 0.625rem 0.25rem 1.5rem; border-radius: 999px; background: color-mix(in srgb, var(--success) 12%, transparent); color: var(--success); font-size: 0.75rem; font-weight: 600; }
.counter-stats__pulse::before, .counter-stats__pulse::after { content: ""; position: absolute; left: 0.625rem; top: 50%; width: 0.5rem; height: 0.5rem; margin-top: -0.25rem; border-radius: 50%; background: var(--success); }

/* Start state (JS on, not yet seen) and the "in" state */
.counter-stats--js:not(.counter-stats--in) .counter-stats__item::before { transform: scaleX(0); }
.counter-stats--js:not(.counter-stats--in) .counter-stats__spark path { stroke-dashoffset: 1; }
.counter-stats--js:not(.counter-stats--in) .counter-stats__stars span { width: 0%; }
.counter-stats--js:not(.counter-stats--in) .counter-stats__ring-fill { stroke-dashoffset: 100px; }
.counter-stats--in .counter-stats__strip { transform: translateY(calc(var(--d) * -1em)); }
@media (prefers-reduced-motion: no-preference) {
  .counter-stats--in .counter-stats__pulse::after { animation: counter-stats-ping 1.4s var(--ease-out) 1s 3 backwards; }
}
@keyframes counter-stats-ping { from { transform: scale(1); opacity: 0.8; } to { transform: scale(3); opacity: 0; } }
```

## JS

```js
document.querySelectorAll('[data-counter-stats]').forEach((root) => {
  // Reduced motion: leave the plain numbers; visuals render finished
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  root.classList.add('counter-stats--js');

  // Turn "12,480" into digit wheels; the original text stays for screen readers
  root.querySelectorAll('[data-counter]').forEach((num) => {
    const text = num.textContent.trim();
    const sr = document.createElement('span');
    sr.className = 'counter-stats__sr';
    sr.textContent = text;
    const digits = document.createElement('span');
    digits.className = 'counter-stats__digits';
    digits.setAttribute('aria-hidden', 'true');
    let column = 0;
    [...text].forEach((ch) => {
      if (!/\d/.test(ch)) { digits.append(ch); return; }
      const wheel = document.createElement('span');
      wheel.className = 'counter-stats__wheel';
      const strip = document.createElement('span');
      strip.className = 'counter-stats__strip';
      strip.style.setProperty('--d', 10 + Number(ch)); // land on the digit after one full turn
      strip.style.setProperty('--c', column++);
      for (let i = 0; i < 20; i++) strip.append(Object.assign(document.createElement('span'), { textContent: i % 10 }));
      wheel.append(strip);
      digits.append(wheel);
    });
    num.replaceChildren(sr, digits);
  });

  // Roll everything once, when 40% of the section is visible
  const io = new IntersectionObserver(([entry]) => {
    if (!entry.isIntersecting) return;
    root.classList.add('counter-stats--in');
    io.disconnect();
  }, { threshold: 0.4 });
  io.observe(root);
});
```

## Notes

- The final numbers are real text in the HTML. JS only adds the wheels; screen readers get the original value from a visually hidden copy, and the wheels are `aria-hidden`.
- Under reduced motion nothing is replaced and every visual is shown finished. That's why the visuals only start "empty" under `.counter-stats--js`.
- Any characters work: commas, decimals and units stay static, while digits roll. Keep numbers honest and current.
- On a dark band, set `.counter-stats { background: var(--surface-deep); color: var(--text-inverse) }`, swap the label colour to `--text-inverse-muted` and the hairline to `--border-inverse`.
