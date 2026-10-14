# Groovy 70s Section

A 70s heritage section, "Fixing Springfield since 1974": a Shrikhand headline with a stacked mustard-orange-brown shadow, an arched window where a conic-gradient sunburst turns slowly behind a slatted sunset and a little house on the hill, a circular "Family owned" badge with its text set on a path, and a clip-out coupon with a dashed cut line and scissors. Four wavy stripe bands flow across the foot of the section; hovering them sends a ripple down the stack, each stripe sliding exactly one wavelength so it settles seamlessly. On phones everything stacks (copy, window, coupon), tablets pair the window with the coupon, and desktop sets the window beside the copy. Depends on `tokens/variables.css`.

**Motion:** sunburst rotation (80s linear loop, pausable, frozen off-screen) · stripe ripple on hover (1.4s, `--ease-in-out`, 110ms stagger per band) · badge swing (`--dur-4`, `--ease-spring`) · scissors snip along the cut line (`--dur-5`, `--ease-out`) · button lift and press (`--dur-2`, `--ease-spring`).
**Fonts:** Shrikhand (display), https://fonts.googleapis.com/css2?family=Shrikhand&display=swap

## HTML

```html
<section class="groovy" aria-labelledby="groovy-title" data-groovy>
  <div class="groovy__inner">
    <div class="groovy__copy">
      <p class="groovy__eyebrow">Brand Home Services · Est. 1974</p>
      <h2 id="groovy-title" class="groovy__title">
        <span class="groovy__title-main">Fixing Springfield</span>
        <span class="groovy__title-since">since 1974</span>
      </h2>
      <p class="groovy__lead">Three generations of the Brand family have kept Springfield's pipes flowing and furnaces glowing. Same phone number, same handshake promise, same pride in a job done right.</p>
      <div class="groovy__actions">
        <a class="groovy__btn groovy__btn--solid" href="#book">
          Book a visit
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="groovy__btn groovy__btn--ghost" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          (555) 555-0123
        </a>
      </div>
      <ul class="groovy__facts" role="list">
        <li><strong>3</strong> generations</li>
        <li><strong>52</strong> years on call</li>
        <li><strong>40k+</strong> homes fixed</li>
      </ul>
    </div>

    <div class="groovy__scene">
      <div class="groovy__window" aria-hidden="true">
        <span class="groovy__rays"></span>
        <span class="groovy__sun"></span>
        <svg class="groovy__hills" viewBox="0 0 300 120" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
          <path class="groovy__hill-back" d="M0 70Q80 30 160 60T300 50V120H0z" />
          <path class="groovy__house-wall" d="M94 51V38h20v13z" />
          <path class="groovy__house-roof" d="M90 39 104 27l14 12z" />
          <path class="groovy__house-door" d="M100 51v-7h5v7z" />
          <path class="groovy__house-glow" d="M108 41h4v4h-4z" />
          <path class="groovy__hill-front" d="M0 95Q90 60 190 88T300 80V120H0z" />
        </svg>
      </div>
      <svg class="groovy__badge" viewBox="0 0 120 120" width="120" height="120" role="img" aria-label="Family owned since 1974">
        <circle class="groovy__badge-disc" cx="60" cy="60" r="57" />
        <circle class="groovy__badge-ring" cx="60" cy="60" r="34" />
        <path class="groovy__badge-path" id="groovy-badge-path" d="M60 60m-45 0a45 45 0 1 1 90 0a45 45 0 1 1-90 0" />
        <text class="groovy__badge-text"><textPath href="#groovy-badge-path" textLength="280" lengthAdjust="spacing">Family owned • Springfield • Since 1974 •</textPath></text>
        <text class="groovy__badge-est" x="60" y="54" text-anchor="middle">Est.</text>
        <text class="groovy__badge-year" x="60" y="76" text-anchor="middle">1974</text>
      </svg>
      <button class="groovy__pause" type="button" aria-label="Pause sunburst animation" aria-pressed="false" hidden>
        <svg class="groovy__icon-pause" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
        <svg class="groovy__icon-play" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
      </button>
    </div>

    <div class="groovy__coupon">
      <svg class="groovy__scissors" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><circle cx="6" cy="6" r="3" /><circle cx="6" cy="18" r="3" /><path d="M20 4 8.12 15.88M14.47 14.48 20 20M8.12 8.12 12 12" /></svg>
      <div class="groovy__coupon-card">
        <p class="groovy__coupon-kicker">Clip &amp; save</p>
        <h3 class="groovy__coupon-deal"><span class="groovy__coupon-amount">$50 off</span> your first service</h3>
        <p class="groovy__coupon-code">Use code <strong class="groovy__code">GROOVY50</strong> <button class="groovy__copy" type="button" hidden>Copy code</button></p>
        <p class="groovy__coupon-fine">New customers in Westlake, Northside and Riverside. One per household. Expires Dec 31.</p>
        <a class="groovy__coupon-link" href="#book">
          Book with this coupon
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <p class="groovy__copied" role="status"></p>
      </div>
    </div>
  </div>

  <div class="groovy__waves" aria-hidden="true">
    <svg viewBox="0 0 2400 150" width="2400" height="150" aria-hidden="true" focusable="false">
      <path class="groovy__wave groovy__wave--mustard" style="--groovy-i: 0" d="M-200 30q50 -30 100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0V150H-200z" />
      <path class="groovy__wave groovy__wave--orange" style="--groovy-i: 1" d="M-200 54q50 -30 100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0V150H-200z" />
      <path class="groovy__wave groovy__wave--rust" style="--groovy-i: 2" d="M-200 78q50 -30 100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0V150H-200z" />
      <path class="groovy__wave groovy__wave--brown" style="--groovy-i: 3" d="M-200 102q50 -30 100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0t100 0V150H-200z" />
    </svg>
  </div>
</section>
```

## CSS

```css
/* Palette, display face and a warm, grainy cream sheet */
.groovy {
  --groovy-cream: #fbefd5;
  --groovy-mustard: #e8a93b;
  --groovy-orange: #e0662a;
  --groovy-rust: #b0401c;
  --groovy-brown: #4a2511;
  --groovy-font: "Shrikhand", var(--font-display);
  --groovy-ray-soft: color-mix(in srgb, var(--groovy-mustard) 42%, var(--groovy-cream));
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(60% 45% at 88% 8%, color-mix(in srgb, var(--groovy-mustard) 30%, transparent), transparent 70%),
    var(--groovy-cream);
  color: var(--groovy-brown); font-family: var(--font-sans);
}
.groovy::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none; opacity: 0.55; mix-blend-mode: multiply;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .25 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E");
}
.groovy__inner {
  position: relative; z-index: 1; display: grid; gap: 3rem;
  max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter) 1rem;
}

/* Copy: eyebrow, headline with a stacked offset shadow, lead, actions, facts */
.groovy__eyebrow {
  display: inline-flex; margin: 0; padding: 0.4375rem 1rem; border-radius: var(--radius-full);
  background: var(--groovy-rust); color: var(--groovy-cream);
  font: 700 0.8125rem/1 var(--font-sans); letter-spacing: 0.1em; text-transform: uppercase;
}
.groovy__title { margin: 1.5rem 0 0; font: 400 clamp(2.25rem, 0.9rem + 5vw, 4.75rem)/1.05 var(--groovy-font); letter-spacing: -0.01em; }
.groovy__title-main {
  display: block; color: var(--groovy-rust);
  text-shadow: 0.035em 0.035em 0 var(--groovy-mustard), 0.07em 0.07em 0 var(--groovy-orange), 0.105em 0.105em 0 var(--groovy-brown);
}
.groovy__title-since {
  display: inline-block; margin-top: 0.35em; color: var(--groovy-brown); font-size: 0.52em; rotate: -4deg;
  text-decoration: underline wavy var(--groovy-orange); text-decoration-thickness: 0.07em; text-underline-offset: 0.2em;
}
.groovy__lead {
  max-width: 34rem; margin: 1.75rem 0 0; color: color-mix(in srgb, var(--groovy-brown) 88%, var(--groovy-cream));
  font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem); line-height: 1.6;
}
.groovy__actions { display: flex; flex-wrap: wrap; gap: 0.875rem; margin-top: 2rem; }
.groovy__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.5rem;
  border-radius: var(--radius-full); font: 700 1rem var(--font-sans); text-decoration: none;
  transition: translate var(--dur-2) var(--ease-spring), scale var(--dur-1) var(--ease-out);
}
.groovy__btn svg, .groovy__coupon-link svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.groovy__btn--solid { background: var(--groovy-brown); color: var(--groovy-cream); box-shadow: 0.25rem 0.25rem 0 var(--groovy-orange); }
.groovy__btn--ghost { color: var(--groovy-brown); box-shadow: inset 0 0 0 2px var(--groovy-brown); }
.groovy__btn:hover { translate: 0 -2px; }
.groovy__btn:active { scale: 0.97; }
.groovy__facts { display: flex; flex-wrap: wrap; gap: 0.75rem 1.75rem; margin: 2.25rem 0 0; padding: 0; list-style: none; font-size: 0.9375rem; font-weight: 600; }
.groovy__facts li { display: flex; align-items: baseline; gap: 0.375rem; }
.groovy__facts strong { color: var(--groovy-rust); font: 400 1.75rem/1 var(--groovy-font); }

/* Arched window: rays turn behind a slatted sunset and a house on the hill */
.groovy__scene { position: relative; width: min(100%, 21rem); margin-inline: auto; }
.groovy__window {
  position: relative; isolation: isolate; overflow: hidden; aspect-ratio: 3 / 4;
  border: 0.75rem solid var(--groovy-brown); border-radius: var(--radius-full) var(--radius-full) var(--radius-xl) var(--radius-xl);
  background: var(--groovy-cream);
  box-shadow: 0 2rem 3rem -1.5rem color-mix(in srgb, var(--groovy-brown) 55%, transparent);
}
.groovy__window::after {
  content: ""; position: absolute; inset: 0; pointer-events: none; border-radius: var(--radius-full) var(--radius-full) 0.25rem 0.25rem;
  box-shadow: inset 0 0 0 0.375rem var(--groovy-mustard), inset 0 0 0 0.5rem var(--groovy-brown);
}
.groovy__rays {
  position: absolute; left: 50%; top: 62%; width: 280%; aspect-ratio: 1; translate: -50% -50%;
  background:
    radial-gradient(closest-side, var(--groovy-cream) 14%, transparent 42%),
    repeating-conic-gradient(var(--groovy-mustard) 0deg 7deg, var(--groovy-ray-soft) 7.5deg 14.5deg, var(--groovy-mustard) 15deg);
}
.groovy--js .groovy__rays { animation: groovy-spin 80s linear infinite; }
.groovy__sun {
  position: absolute; left: 50%; top: 62%; width: 46%; aspect-ratio: 1; translate: -50% -50%; border-radius: 50%;
  background: linear-gradient(var(--groovy-mustard), var(--groovy-orange) 48%, var(--groovy-rust));
  -webkit-mask: linear-gradient(black 0 54%, transparent 0 59%, black 0 67%, transparent 0 72%, black 0 79%, transparent 0 84%, black 0);
  mask: linear-gradient(black 0 54%, transparent 0 59%, black 0 67%, transparent 0 72%, black 0 79%, transparent 0 84%, black 0);
}
.groovy__hills { position: absolute; inset: auto 0 0; width: 100%; height: 40%; }
.groovy__hill-back { fill: var(--groovy-rust); }
.groovy__hill-front, .groovy__house-roof, .groovy__house-door { fill: var(--groovy-brown); }
.groovy__house-wall { fill: var(--groovy-cream); }
.groovy__house-glow { fill: var(--groovy-mustard); }

/* Badge: text set on a circular path */
.groovy__badge {
  position: absolute; left: -0.5rem; bottom: 10%; z-index: 2; width: 6.25rem; height: 6.25rem; rotate: -12deg;
  filter: drop-shadow(0 0.5rem 0.75rem color-mix(in srgb, var(--groovy-brown) 35%, transparent));
  transition: rotate var(--dur-4) var(--ease-spring);
}
.groovy__badge:hover { rotate: 14deg; }
.groovy__badge-disc { fill: var(--groovy-rust); stroke: var(--groovy-cream); stroke-width: 2; }
.groovy__badge-ring { fill: none; stroke: var(--groovy-cream); stroke-width: 1.5; stroke-dasharray: 2 3; }
.groovy__badge-path { fill: none; }
.groovy__badge-text { fill: var(--groovy-cream); font: 700 10px var(--font-sans); letter-spacing: 0.06em; text-transform: uppercase; }
.groovy__badge-est { fill: var(--groovy-cream); font: 700 8px var(--font-sans); letter-spacing: 0.2em; text-transform: uppercase; }
.groovy__badge-year { fill: var(--groovy-cream); font: 21px var(--groovy-font); }

/* Pause control for the sunburst */
.groovy__pause {
  position: absolute; top: 0; right: -0.25rem; z-index: 2; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0;
  border: 2px solid var(--groovy-brown); border-radius: 50%; background: var(--groovy-cream); color: var(--groovy-brown); cursor: pointer;
  box-shadow: 0.1875rem 0.1875rem 0 var(--groovy-orange); transition: translate var(--dur-2) var(--ease-spring);
}
.groovy__pause:hover { translate: 0 -2px; }
.groovy__pause[hidden] { display: none; }
.groovy__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.groovy__icon-play, .groovy__pause[aria-pressed="true"] .groovy__icon-pause { display: none; }
.groovy__pause[aria-pressed="true"] .groovy__icon-play { display: block; }

/* Coupon: dashed cut line, scissors that snip along it on hover */
.groovy__coupon { position: relative; align-self: end; padding: 0.625rem; border: 2px dashed var(--groovy-brown); border-radius: var(--radius-2xl); background: var(--groovy-cream); }
.groovy__scissors {
  position: absolute; top: -0.8125rem; left: 1.5rem; padding-inline: 0.25rem; background: var(--groovy-cream); color: var(--groovy-brown);
  fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round;
  transition: translate var(--dur-5) var(--ease-out);
}
.groovy__coupon:is(:hover, :focus-within) .groovy__scissors { translate: 3.5rem 0; }
.groovy__coupon-card {
  display: grid; justify-items: start; gap: 0.625rem; padding: 1.5rem 1.5rem 1.25rem; border-radius: var(--radius-xl);
  background: var(--groovy-mustard); color: var(--groovy-brown);
  box-shadow: inset 0 0 0 2px var(--groovy-brown), inset 0 0 0 6px var(--groovy-mustard), inset 0 0 0 7px var(--groovy-brown);
}
.groovy__coupon-kicker { margin: 0; font: 700 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.groovy__coupon-deal { margin: 0; font: 700 1.125rem/1.25 var(--font-sans); }
.groovy__coupon-amount { display: block; font: 400 clamp(2.5rem, 2rem + 2vw, 3.25rem)/1.05 var(--groovy-font); text-shadow: 0.05em 0.05em 0 var(--groovy-cream); }
.groovy__coupon-code { display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem; margin: 0.25rem 0 0; font-weight: 600; }
.groovy__code { padding: 0.25rem 0.625rem; border: 2px dashed var(--groovy-brown); border-radius: var(--radius-sm); background: var(--groovy-cream); font: 700 1rem var(--font-mono); letter-spacing: 0.12em; }
.groovy__copy {
  min-height: 2rem; padding: 0 0.875rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--groovy-brown); color: var(--groovy-cream); font: 700 0.8125rem var(--font-sans); transition: scale var(--dur-2) var(--ease-spring);
}
.groovy__copy:active { scale: 0.94; }
.groovy__copy[hidden] { display: none; }
.groovy__coupon-fine { max-width: 26rem; margin: 0; font-size: 0.8125rem; line-height: 1.45; }
.groovy__coupon-link { display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.75rem; color: var(--groovy-brown); font-weight: 800; text-underline-offset: 4px; }
.groovy__coupon-link svg { transition: translate var(--dur-3) var(--ease-spring); }
.groovy__coupon-link:hover svg { translate: 3px 0; }
.groovy__copied { margin: 0; font-size: 0.875rem; font-weight: 700; }

/* Stripes: four bands, each a quadratic sine; a hover ripples them one wavelength, staggered */
.groovy__waves { position: relative; height: 9.375rem; margin-top: -3.5rem; overflow: hidden; }
.groovy__waves svg { position: absolute; left: 50%; bottom: 0; width: 2400px; max-width: none; height: 150px; translate: -50% 0; }
.groovy__wave--mustard { fill: var(--groovy-mustard); }
.groovy__wave--orange { fill: var(--groovy-orange); }
.groovy__wave--rust { fill: var(--groovy-rust); }
.groovy__wave--brown { fill: var(--groovy-brown); }
.groovy__waves:hover .groovy__wave { animation: groovy-ripple 1.4s var(--ease-in-out) calc(var(--groovy-i) * 110ms) both; }

/* Focus on the cream sheet */
.groovy :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Paused or off-screen: freeze the sunburst */
.groovy[data-paused] .groovy__rays, .groovy[data-offscreen] .groovy__rays { animation-play-state: paused; }

@media (min-width: 768px) {
  .groovy__inner { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 3.5rem 2.5rem; align-items: end; }
  .groovy__copy { grid-column: 1 / -1; }
  .groovy__scene { width: min(100%, 20rem); }
  .groovy__badge { left: -1.5rem; width: 7rem; height: 7rem; }
}
@media (min-width: 1024px) {
  .groovy__inner { grid-template-columns: 1.1fr 0.9fr; column-gap: 4rem; }
  .groovy__copy { grid-column: 1; grid-row: 1; align-self: start; }
  .groovy__coupon { grid-column: 1; grid-row: 2; max-width: 30rem; }
  .groovy__scene { grid-column: 2; grid-row: 1 / span 2; width: min(100%, 24rem); }
}
@media (prefers-reduced-motion: reduce) {
  .groovy *, .groovy *::before, .groovy *::after { animation: none !important; }
}
@keyframes groovy-spin { to { rotate: 360deg; } }
@keyframes groovy-ripple { to { transform: translateX(200px); } }
```

## JS

```js
document.querySelectorAll('[data-groovy]').forEach((root, n) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const pause = root.querySelector('.groovy__pause');
  const copy = root.querySelector('.groovy__copy');
  const code = root.querySelector('.groovy__code');
  const status = root.querySelector('.groovy__copied');

  // The badge's text path needs a unique id when the section appears more than once
  const path = root.querySelector('.groovy__badge-path');
  path.id = `groovy-badge-path-${n}`;
  root.querySelector('.groovy__badge textPath').setAttribute('href', `#${path.id}`);

  // The sunburst only turns once a pause button can be offered (WCAG 2.2.2); no button when motion is off
  root.classList.add('groovy--js');
  const syncMotion = () => { pause.hidden = reduce.matches; };
  syncMotion();
  reduce.addEventListener('change', syncMotion);
  pause.addEventListener('click', () => {
    pause.setAttribute('aria-pressed', String(root.toggleAttribute('data-paused')));
  });

  // Freeze the loop while the section is off screen, without touching the button state
  new IntersectionObserver(([entry]) => root.toggleAttribute('data-offscreen', !entry.isIntersecting)).observe(root);

  // Coupon: copy the code where the Clipboard API is available
  if (!navigator.clipboard) return;
  copy.hidden = false;
  copy.addEventListener('click', async () => {
    const text = code.textContent.trim();
    try {
      await navigator.clipboard.writeText(text);
      status.textContent = `Code ${text} copied. Paste it at checkout.`;
    } catch {
      status.textContent = `Couldn't copy. The code is ${text}.`;
    }
  });
});
```

## Notes

- Accessibility: the window and the stripes are decorative (`aria-hidden`); the badge is `role="img"` labelled "Family owned since 1974"; the offer is an `<h3>` with the code as real text, and the copy button reports through a `role="status"` region. JS gives each instance's badge text path a unique id.
- Motion: the sunburst (80s loop) only turns once JS can show the `aria-pressed` pause button, and it freezes off-screen. The stripe ripple runs once per hover; each band moves exactly one 200px wavelength, so it lands where it started. With no JS the sunburst is static and the copy button stays hidden; under reduced motion everything is static and the pause button is hidden.
- Contrast on cream: rust headline 5.1:1 (display), brown body 11.8:1 (the 88% lead 8.4:1), cream on rust (eyebrow, badge) 5.1:1, brown on the mustard coupon 6.5:1. Orange and mustard carry no text on cream (2.8:1 and lower): they're shadow, stripe and sunset colours only.
- Shrikhand loads into `--groovy-font` with a Geist fallback. Retheme through the five palette variables: the rays, sunset, hills, badge and stripes all read from them. The stripes are a fixed 2400px strip centred in the section, so their wavelength stays the same on every screen.
