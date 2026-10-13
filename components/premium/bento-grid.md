# Bento Grid

Feature section in a bento layout. A spotlight and a glowing border follow the cursor across every card at once. Each card plays a small story once, as it scrolls into view: a van drives the route to your door, quotes fan out, stars fill, support rings pulse, price bars rise and a guarantee shield draws its check. Dark by default; add `bento--light` for a light section. Depends on `tokens/variables.css`.

**Motion:** pointer spotlight + border glow · SVG route draw with a van following the path · card fan (spring) · star fill sweep · ring pulses (3×) · staggered bars · shield check draw. Everything is one-shot except the hover effects.

## HTML

```html
<section class="bento" aria-labelledby="bento-title" data-bento>
  <div class="bento__inner">
    <header class="bento__head">
      <p class="bento__eyebrow">Why Brand</p>
      <h2 id="bento-title" class="bento__title">Everything you expect from a pro. <span>Nothing you don't.</span></h2>
    </header>

    <ul class="bento__grid" role="list">
      <li class="bento__card bento__card--wide">
        <div class="bento__visual bento__visual--map" aria-hidden="true">
          <svg class="bento__map" viewBox="0 0 480 200" preserveAspectRatio="xMidYMid slice" focusable="false">
            <defs>
              <linearGradient id="bento-route-grad" x1="0" x2="1">
                <stop class="bento__stop-a" offset="0" /><stop class="bento__stop-b" offset="1" />
              </linearGradient>
            </defs>
            <path class="bento__streets" d="M-10 44H490M-10 132H490M86-10V210M262-10V210M392-10V210" />
            <path id="bento-route" class="bento__route-base" d="M40 160 C 120 160, 130 70, 210 80 S 330 150, 400 60" />
            <path class="bento__route" d="M40 160 C 120 160, 130 70, 210 80 S 330 150, 400 60" pathLength="1" />
            <circle class="bento__pin-pulse" cx="400" cy="60" r="10" />
            <circle class="bento__pin" cx="400" cy="60" r="6" />
            <g class="bento__van">
              <circle class="bento__van-halo" r="10" /><circle class="bento__van-core" r="4.5" />
              <animateMotion dur="2.6s" begin="indefinite" fill="freeze" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines="0.16 1 0.3 1"><mpath href="#bento-route" /></animateMotion>
            </g>
          </svg>
          <span class="bento__chip bento__chip--eta"><span class="bento__live"></span>Sam · ETA 12 min</span>
          <span class="bento__chip bento__chip--arrived">Arrived 2:14 pm</span>
        </div>
        <div class="bento__body">
          <h3 class="bento__card-title">Live arrival tracking</h3>
          <p class="bento__card-text">Follow your technician on the map, minute by minute. No more waiting by the window.</p>
        </div>
      </li>

      <li class="bento__card">
        <div class="bento__visual bento__visual--quotes" aria-hidden="true">
          <div class="bento__quote" style="--bento-n: 0; --bento-d: 2"><span>Water heater</span><strong>$1,180</strong></div>
          <div class="bento__quote" style="--bento-n: 2; --bento-d: 1"><span>Drain clean</span><strong>$95</strong></div>
          <div class="bento__quote" style="--bento-n: 1; --bento-d: 0"><span>Leak repair</span><strong>$149</strong><em>Approved</em></div>
        </div>
        <div class="bento__body">
          <h3 class="bento__card-title">Quotes in minutes</h3>
          <p class="bento__card-text">Written, flat-rate prices before any work starts.</p>
        </div>
      </li>

      <li class="bento__card">
        <div class="bento__visual bento__visual--rating" aria-hidden="true">
          <p class="bento__score">4.9</p>
          <p class="bento__stars"><span class="bento__stars-fill">★★★★★</span>★★★★★</p>
          <span class="bento__faces"><span>JM</span><span>AK</span><span>RS</span><span>LT</span></span>
        </div>
        <div class="bento__body">
          <h3 class="bento__card-title">Rated 4.9 by 1,200+ neighbours</h3>
          <p class="bento__card-text">Verified reviews from real Springfield jobs.</p>
        </div>
      </li>

      <li class="bento__card">
        <div class="bento__visual bento__visual--support" aria-hidden="true">
          <span class="bento__ring"></span><span class="bento__ring" style="--r: 1"></span><span class="bento__ring" style="--r: 2"></span>
          <span class="bento__headset"><svg viewBox="0 0 24 24" width="26" height="26" focusable="false"><path d="M4 14v-2a8 8 0 0 1 16 0v2M4 14a2 2 0 0 1 2-2h1v6H6a2 2 0 0 1-2-2v-2zM20 14a2 2 0 0 0-2-2h-1v6h1a2 2 0 0 0 2-2v-2zM17 18c0 1.7-1.8 3-5 3" /></svg></span>
        </div>
        <div class="bento__body">
          <h3 class="bento__card-title">A human answers, 24/7</h3>
          <p class="bento__card-text">Average answer time: 38 seconds.</p>
        </div>
      </li>

      <li class="bento__card">
        <div class="bento__visual bento__visual--price" aria-hidden="true">
          <div class="bento__bars">
            <span style="--h: 82%; --i: 0"></span><span style="--h: 64%; --i: 1"></span><span style="--h: 90%; --i: 2"></span>
            <span style="--h: 48%; --i: 3"></span><span class="bento__bar-us" style="--h: 36%; --i: 4"></span>
          </div>
          <span class="bento__tag">$149 flat</span>
        </div>
        <div class="bento__body">
          <h3 class="bento__card-title">Fair, upfront pricing</h3>
          <p class="bento__card-text">Up to 40% below typical callout-plus-hourly rates.</p>
        </div>
      </li>

      <li class="bento__card bento__card--full">
        <div class="bento__shield" aria-hidden="true">
          <svg viewBox="0 0 64 64" width="64" height="64" focusable="false">
            <path class="bento__shield-body" d="M32 6 54 14v16c0 15-10 24-22 28C20 54 10 45 10 30V14z" />
            <path class="bento__shield-check" d="m22 32 7 7 14-14" pathLength="1" />
          </svg>
        </div>
        <div class="bento__body">
          <h3 class="bento__card-title">5-year workmanship guarantee</h3>
          <p class="bento__card-text">If anything we fixed fails, we come back and make it right. Free, no questions asked.</p>
        </div>
        <a class="bento__link" href="#guarantee">How it works <span aria-hidden="true">→</span></a>
      </li>
    </ul>
  </div>
</section>
```

## CSS

```css
/* Section palette: dark by default, light with .bento--light */
.bento {
  --bento-bg: var(--surface-deep);
  --bento-card: color-mix(in srgb, var(--surface-light) 3%, var(--surface-deep));
  --bento-float: color-mix(in srgb, var(--surface-deep) 72%, transparent);
  --bento-line: var(--border-inverse);
  --bento-text: var(--text-inverse);
  --bento-muted: var(--text-inverse-muted);
  --bento-fill: var(--glass-inverse);
  background: var(--bento-bg); color: var(--bento-text); font-family: var(--font-sans);
}
.bento--light {
  --bento-bg: var(--surface-muted);
  --bento-card: var(--surface-light);
  --bento-float: var(--surface-light);
  --bento-line: var(--border-subtle);
  --bento-text: var(--text-main);
  --bento-muted: var(--text-muted);
  --bento-fill: color-mix(in srgb, var(--text-main) 4%, transparent);
}
.bento__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }

/* Heading */
.bento__head { max-width: 40rem; margin-bottom: 3rem; }
.bento__eyebrow { margin: 0; color: var(--primary-2); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.bento--light .bento__eyebrow { color: var(--primary); }
.bento__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.bento__title span { color: var(--bento-muted); }

/* Grid */
.bento__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
@media (min-width: 640px) {
  .bento__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .bento__card--wide, .bento__card--full { grid-column: span 2; }
}
@media (min-width: 1024px) {
  .bento__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .bento__card--full { grid-column: 1 / -1; }
}

/* Card with a cursor spotlight and a border glow that follows it */
.bento__card {
  position: relative; isolation: isolate; display: flex; flex-direction: column;
  padding: 1rem 1rem 1.5rem; border-radius: var(--radius-2xl);
  background: var(--bento-card); box-shadow: inset 0 0 0 1px var(--bento-line), var(--highlight-inverse);
  transition: transform var(--dur-4) var(--ease-out);
}
.bento--light .bento__card { box-shadow: inset 0 0 0 1px var(--bento-line), var(--shadow-sm); }
.bento__card::before, .bento__card::after {
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  opacity: 0; transition: opacity var(--dur-4) var(--ease-out);
}
.bento__card::before {
  z-index: -1;
  background: radial-gradient(26rem circle at var(--bento-mx, 50%) var(--bento-my, 50%), color-mix(in srgb, var(--primary) 14%, transparent), transparent 60%);
}
.bento__card::after {
  padding: 1px;
  background: radial-gradient(18rem circle at var(--bento-mx, 50%) var(--bento-my, 50%), color-mix(in srgb, var(--primary-2) 85%, transparent), transparent 60%);
  -webkit-mask: linear-gradient(black 0 0) content-box, linear-gradient(black 0 0);
  -webkit-mask-composite: xor; mask-composite: exclude;
}
.bento__grid--lit .bento__card::before, .bento__grid--lit .bento__card::after { opacity: 1; }
.bento__card:hover { transform: translateY(-2px); }

.bento__body { padding: 0 0.5rem; }
.bento__card-title { margin: 0; font: 600 1.125rem/1.3 var(--font-display); letter-spacing: -0.015em; }
.bento__card-text { margin: 0.375rem 0 0; color: var(--bento-muted); font-size: 0.9375rem; line-height: 1.55; }

/* Visual stage at the top of each card */
.bento__visual {
  position: relative; height: 11rem; margin-bottom: 1.25rem; overflow: hidden; border-radius: calc(var(--radius-2xl) - 0.5rem);
  background: var(--bento-fill); box-shadow: inset 0 0 0 1px var(--bento-line);
}
.bento__chip {
  position: absolute; display: inline-flex; align-items: center; gap: 0.375rem;
  padding: 0.375rem 0.625rem; border-radius: 999px; background: var(--bento-float); color: var(--bento-text);
  box-shadow: inset 0 0 0 1px var(--bento-line), 0 8px 20px -10px color-mix(in srgb, var(--surface-deep) 80%, transparent);
  font-size: 0.75rem; font-weight: 600; white-space: nowrap;
}
@supports (backdrop-filter: blur(1px)) { .bento__chip { backdrop-filter: blur(10px); } }

/* 1. Map: route draws, van drives it, pin pulses, "Arrived" pops */
.bento__visual--map { height: 13rem; background: radial-gradient(80% 100% at 75% 0%, color-mix(in srgb, var(--primary) 20%, transparent), transparent 60%), var(--bento-fill); }
.bento__map { display: block; width: 100%; height: 100%; }
.bento__stop-a { stop-color: var(--primary); }
.bento__stop-b { stop-color: var(--primary-2); }
.bento__streets { fill: none; stroke: var(--bento-line); stroke-width: 12; stroke-linecap: round; }
.bento__route-base { fill: none; stroke: color-mix(in srgb, var(--bento-muted) 40%, transparent); stroke-width: 2.5; stroke-dasharray: 2 8; stroke-linecap: round; }
.bento__route {
  fill: none; stroke: url(#bento-route-grad); stroke-width: 4; stroke-linecap: round;
  stroke-dasharray: 1; stroke-dashoffset: 0;
  filter: drop-shadow(0 0 6px color-mix(in srgb, var(--primary-2) 70%, transparent));
  transition: stroke-dashoffset calc(var(--dur-5) * 2.9) var(--ease-out) 150ms;
}
.bento__pin { fill: var(--primary-2); stroke: var(--surface-light); stroke-width: 3; }
.bento__pin-pulse { fill: color-mix(in srgb, var(--primary-2) 40%, transparent); transform-box: fill-box; transform-origin: center; }
.bento__van { opacity: 0; transition: opacity var(--dur-3); }
.bento__van-halo { fill: color-mix(in srgb, var(--surface-light) 90%, transparent); }
.bento__van-core { fill: var(--primary); }
.bento__chip--eta { top: 0.75rem; left: 0.75rem; }
.bento__chip--arrived {
  right: 0.75rem; bottom: 0.75rem; background: var(--success); color: var(--surface-light); box-shadow: 0 10px 24px -10px var(--success);
  transition: opacity var(--dur-3), transform var(--dur-4) var(--ease-spring); transition-delay: calc(var(--dur-5) * 2.8);
}
.bento__live { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 30%, transparent); }

/* 2. Quotes: a tidy stack that fans out */
.bento__visual--quotes { display: grid; place-items: center; }
.bento__quote {
  grid-area: 1 / 1; display: grid; gap: 0.25rem; width: 9rem; padding: 0.875rem 1rem; border-radius: 1rem;
  background: var(--bento-float); color: var(--bento-text);
  box-shadow: inset 0 0 0 1px var(--bento-line), 0 14px 28px -14px color-mix(in srgb, var(--surface-deep) 90%, transparent);
  --bento-spread: 1;
  transform: translateX(calc((var(--bento-n) - 1) * 58% * var(--bento-spread))) translateY(calc((var(--bento-n) - 1) * (var(--bento-n) - 1) * 10px)) rotate(calc((var(--bento-n) - 1) * 9deg * var(--bento-spread)));
  transition: transform var(--dur-5) var(--ease-spring); transition-delay: calc(var(--bento-d) * 60ms);
}
@supports (backdrop-filter: blur(1px)) { .bento__quote { backdrop-filter: blur(10px); } }
.bento__quote span { color: var(--bento-muted); font-size: 0.75rem; }
.bento__quote strong { font: 600 1.25rem/1 var(--font-display); letter-spacing: -0.02em; }
.bento__quote em { justify-self: start; margin-top: 0.25rem; padding: 0.125rem 0.5rem; border-radius: 999px; background: color-mix(in srgb, var(--success) 22%, transparent); font-size: 0.6875rem; font-style: normal; font-weight: 600; }
.bento__card:hover .bento__quote { --bento-spread: 1.18; }

/* 3. Rating: number, stars fill left to right */
.bento__visual--rating { display: grid; place-content: center; justify-items: center; gap: 0.25rem; }
.bento__score {
  margin: 0; font: 600 3.75rem/1 var(--font-display); letter-spacing: var(--tracking-display);
  background: linear-gradient(180deg, var(--bento-text), color-mix(in srgb, var(--bento-text) 55%, transparent));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.bento__stars { position: relative; margin: 0; color: var(--bento-line); font-size: 1.25rem; letter-spacing: 0.15em; }
.bento__stars-fill { position: absolute; inset: 0 auto 0 0; width: 98%; overflow: hidden; color: var(--accent); white-space: nowrap; transition: width calc(var(--dur-5) * 1.6) var(--ease-out) 200ms; }
.bento__faces { display: flex; margin-top: 0.75rem; }
.bento__faces span { display: grid; place-items: center; width: 1.75rem; height: 1.75rem; margin-left: -0.4rem; border-radius: 50%; border: 2px solid var(--bento-card); background: var(--gradient-brand); color: var(--text-inverse); font-size: 0.5625rem; font-weight: 700; }
.bento__faces span:first-child { margin-left: 0; }
.bento__faces span:nth-child(2) { background: linear-gradient(135deg, var(--primary-2), var(--surface-deep)); }
.bento__faces span:nth-child(3) { background: linear-gradient(135deg, var(--accent), var(--primary-2)); color: var(--text-main); }

/* 4. Support: rings ripple out from the headset */
.bento__visual--support { display: grid; place-items: center; }
.bento__ring { grid-area: 1 / 1; width: 5rem; height: 5rem; border-radius: 50%; box-shadow: inset 0 0 0 1px var(--bento-line); transform: scale(calc(1 + var(--r, 0) * 0.55)); }
.bento__headset {
  grid-area: 1 / 1; display: grid; place-items: center; width: 4rem; height: 4rem; border-radius: 50%;
  background: var(--gradient-brand); color: var(--text-inverse); box-shadow: 0 12px 32px -10px color-mix(in srgb, var(--primary) 90%, transparent);
}
.bento__headset svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }

/* 5. Price: bars rise, ours glows, the tag drops in */
.bento__visual--price { display: flex; align-items: flex-end; padding: 1.25rem 1.25rem 0; }
.bento__bars { display: flex; align-items: flex-end; gap: 0.625rem; width: 100%; height: 100%; }
.bento__bars span {
  flex: 1; height: var(--h); border-radius: 0.5rem 0.5rem 0 0; transform-origin: bottom;
  background: color-mix(in srgb, var(--bento-muted) 22%, transparent);
  transition: transform var(--dur-5) var(--ease-spring); transition-delay: calc(var(--i) * 80ms + 150ms);
}
.bento__bars .bento__bar-us { background: var(--gradient-brand); box-shadow: 0 0 28px -4px color-mix(in srgb, var(--primary-2) 80%, transparent); }
.bento__tag {
  position: absolute; right: 1rem; top: 1rem; padding: 0.375rem 0.75rem; border-radius: 0.625rem;
  background: var(--surface-light); color: var(--text-main); font: 600 0.875rem/1 var(--font-display); box-shadow: var(--shadow-lg);
  transition: opacity var(--dur-3), transform var(--dur-4) var(--ease-spring); transition-delay: 700ms;
}

/* 6. Guarantee banner: shield check draws */
.bento__card--full { flex-direction: row; flex-wrap: wrap; align-items: center; gap: 1.25rem 1.5rem; padding: 1.5rem; }
.bento__card--full .bento__body { flex: 1 1 18rem; padding: 0; }
.bento__shield { display: grid; place-items: center; width: 4.5rem; height: 4.5rem; border-radius: 1.25rem; background: var(--bento-fill); box-shadow: inset 0 0 0 1px var(--bento-line); }
.bento__shield-body { fill: color-mix(in srgb, var(--primary) 22%, transparent); stroke: var(--primary-2); stroke-width: 2.5; stroke-linejoin: round; }
.bento__shield-check { fill: none; stroke: var(--bento-text); stroke-width: 4; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 1; stroke-dashoffset: 0; transition: stroke-dashoffset var(--dur-5) var(--ease-out) 300ms; }
.bento__link {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 2.75rem; padding: 0 1.25rem; border-radius: 999px;
  background: var(--bento-text); color: var(--bento-bg); font-size: 0.875rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring);
}
.bento__link span { transition: transform var(--dur-3) var(--ease-spring); }
.bento__link:hover span { transform: translateX(4px); }
.bento__link:active { transform: scale(0.96); }
.bento__link:focus-visible { outline: 2px solid var(--bento-text); outline-offset: 3px; }

/* Start states: only once JS is running and only until each card has been seen */
.bento--js .bento__card:not(.bento__card--in) .bento__route { stroke-dashoffset: 1; }
.bento--js .bento__card:not(.bento__card--in) .bento__chip--arrived { opacity: 0; transform: scale(0.8) translateY(6px); }
.bento--js .bento__card:not(.bento__card--in) .bento__quote { --bento-spread: 0; transform: translateY(calc(var(--bento-d) * -8px)) scale(calc(1 - var(--bento-d) * 0.06)); }
.bento--js .bento__card:not(.bento__card--in) .bento__stars-fill { width: 0%; }
.bento--js .bento__card:not(.bento__card--in) .bento__bars span { transform: scaleY(0.08); }
.bento--js .bento__card:not(.bento__card--in) .bento__tag { opacity: 0; transform: translateY(-10px); }
.bento--js .bento__card:not(.bento__card--in) .bento__shield-check { stroke-dashoffset: 1; }
@media (prefers-reduced-motion: no-preference) {
  .bento__card--in .bento__pin-pulse { animation: bento-ping 1.4s var(--ease-out) 2.6s 3 backwards; }
  .bento__card--in .bento__ring { animation: bento-ripple 1.8s var(--ease-out) calc(var(--r, 0) * 250ms + 200ms) 3 backwards; }
}
@keyframes bento-ping { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(2.8); opacity: 0; } }
@keyframes bento-ripple { 0% { opacity: 0.9; } 100% { opacity: 0; transform: scale(calc(1.6 + var(--r, 0) * 0.55)); } }
```

## JS

```js
document.querySelectorAll('[data-bento]').forEach((bento) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const grid = bento.querySelector('.bento__grid');
  const cards = [...grid.querySelectorAll('.bento__card')];
  bento.classList.add('bento--js');

  // Spotlight + border glow: every card tracks the same pointer, one update per frame
  let frame = 0;
  grid.addEventListener('pointermove', (e) => {
    if (frame) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      cards.forEach((card) => {
        const r = card.getBoundingClientRect();
        card.style.setProperty('--bento-mx', `${e.clientX - r.left}px`);
        card.style.setProperty('--bento-my', `${e.clientY - r.top}px`);
      });
    });
  });
  grid.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse') grid.classList.add('bento__grid--lit'); });
  grid.addEventListener('pointerleave', () => grid.classList.remove('bento__grid--lit'));

  // Each card's story plays once when it's a third visible; the van follows the SVG route
  const io = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    const card = entry.target;
    card.classList.add('bento__card--in');
    io.unobserve(card);
    const drive = card.querySelector('animateMotion');
    if (drive && !reduce) {
      drive.parentElement.style.opacity = '1';
      drive.beginElement();
    }
  }), { threshold: 0.35 });
  cards.forEach((card) => io.observe(card));
});
```

## Notes

- Visuals are decorative (`aria-hidden`); each card's meaning is in its heading and text. Only the guarantee banner has a link, so the cards don't need stretched links.
- Without JS, every visual shows its finished state. Start states only apply under `.bento--js`, and only until a card has been seen.
- The border glow is a 1px gradient ring cut out with `mask-composite`. If the browser can't composite masks, it's simply not shown.
- The route uses SVG `<animateMotion>`, so the van follows the exact curve at any size. Keep `id="bento-route"` unique if a page has two bentos.
- Swap a card's story without touching the shell: keep `.bento__visual` + `.bento__body` and replace the inner visual.
