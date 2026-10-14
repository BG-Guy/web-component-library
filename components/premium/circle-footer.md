# Circle Reveal Footer

A round "Get a quote" button sits at the bottom of the last section, and as you scroll to the end of the page a circle of deep gradient grows out of it until the footer surface floods the viewport. The circle is a scroll-scrubbed `clip-path` whose origin is measured from the button, so the button stays at the centre the whole way, surrounded by hairline ripple rings. Once the flood is mostly done, the footer's headline, contact details, link columns and hours rise into place one after another. Phones get the same flood with a smaller seed and a stacked layout. Depends on `tokens/variables.css`.

**Motion:** scroll-scrubbed `clip-path: circle()` (linear scrub) from the seed's radius to the farthest viewport corner · staggered rise of the footer content (`--dur-4`/`--dur-5`, `--ease-out`, `--stagger`) · ripple rings settle outwards (`--dur-5`) · seed hover/focus swell of the surface (`--ease-spring` on an `@property` length) · arrow turn, link underline draw · scroll-hint nudge (three runs).

## HTML

```html
<div class="circle-footer" data-circle-footer>
  <!-- The last section: in a real page this is usually your <main> -->
  <section class="circle-footer__last circle-footer-demo" aria-labelledby="circle-footer-demo-title">
    <div class="circle-footer-demo__inner">
      <p class="circle-footer-demo__eyebrow">Kitchens · Bathrooms · Repairs</p>
      <h2 id="circle-footer-demo-title" class="circle-footer-demo__title">One crew, from first call to final coat.</h2>
      <p class="circle-footer-demo__lead">No subcontractor roulette. The team that measures your kitchen is the team that fits it, and you get one fixed price before we start.</p>
      <ul class="circle-footer-demo__chips" role="list">
        <li>Licensed &amp; insured</li>
        <li>Fixed-price quotes</li>
        <li>2-year workmanship guarantee</li>
      </ul>
      <p class="circle-footer-demo__hint" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
        Scroll
      </p>
    </div>
  </section>

  <footer class="circle-footer__footer">
    <div class="circle-footer__lead">
      <span class="circle-footer__rings" aria-hidden="true"></span>
      <div class="circle-footer__hello">
        <p class="circle-footer__eyebrow circle-footer__item" style="--circle-footer-i: 0">Free written estimates · Reply within 2 hours</p>
        <h2 class="circle-footer__title circle-footer__item" style="--circle-footer-i: 1">Let's price your <span class="circle-footer__glow">project.</span></h2>
      </div>
      <a class="circle-footer__seed" href="#quote">
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg>
        Get a quote
      </a>
    </div>

    <div class="circle-footer__inner">
      <div class="circle-footer__grid">
        <div class="circle-footer__contact circle-footer__item" style="--circle-footer-i: 2">
          <h3 class="circle-footer__heading">Talk to a person</h3>
          <a class="circle-footer__phone" href="tel:+15555550123">(555) 555-0123</a>
          <ul class="circle-footer__lines" role="list">
            <li>
              <a href="mailto:hello@example.com">
                <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z" /><path d="m3.5 6.5 8.5 6.5 8.5-6.5" /></svg>
                hello@example.com
              </a>
            </li>
            <li>
              <a href="#directions">
                <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12zM12 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z" /></svg>
                48 Elm Street, Springfield
              </a>
            </li>
          </ul>
        </div>

        <nav class="circle-footer__nav circle-footer__item" style="--circle-footer-i: 3" aria-label="Footer">
          <div>
            <h3 class="circle-footer__heading">Services</h3>
            <ul class="circle-footer__links" role="list">
              <li><a href="#kitchens">Kitchens</a></li>
              <li><a href="#bathrooms">Bathrooms</a></li>
              <li><a href="#plumbing">Plumbing</a></li>
              <li><a href="#electrical">Electrical</a></li>
              <li><a href="#repairs">Repairs</a></li>
            </ul>
          </div>
          <div>
            <h3 class="circle-footer__heading">Company</h3>
            <ul class="circle-footer__links" role="list">
              <li><a href="#about">About us</a></li>
              <li><a href="#work">Our work</a></li>
              <li><a href="#reviews">Reviews</a></li>
              <li><a href="#financing">Financing</a></li>
              <li><a href="#careers">Careers</a></li>
            </ul>
          </div>
        </nav>

        <div class="circle-footer__open circle-footer__item" style="--circle-footer-i: 4">
          <h3 class="circle-footer__heading">Hours</h3>
          <ul class="circle-footer__hours" role="list">
            <li data-days="1 2 3 4 5"><span>Mon – Fri</span><span>7am – 7pm</span></li>
            <li data-days="6"><span>Saturday</span><span>8am – 4pm</span></li>
            <li data-days="0"><span>Sunday</span><span>Emergencies</span></li>
          </ul>
          <p class="circle-footer__note">Serving Springfield, Westlake, Northside and Riverside. Emergency line open 24/7.</p>
        </div>
      </div>

      <div class="circle-footer__legal circle-footer__item" style="--circle-footer-i: 5">
        <p>© 2026 Brand Home Services · Lic. #CSL-104233</p>
        <ul class="circle-footer__legal-links" role="list">
          <li><a href="#privacy">Privacy</a></li>
          <li><a href="#terms">Terms</a></li>
          <li><a href="#accessibility">Accessibility</a></li>
        </ul>
        <ul class="circle-footer__social" role="list">
          <li>
            <a href="#instagram" aria-label="Brand on Instagram">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><rect x="3" y="3" width="18" height="18" rx="5" /><circle cx="12" cy="12" r="4" /><path d="M17.5 6.5h.01" /></svg>
            </a>
          </li>
          <li>
            <a href="#facebook" aria-label="Brand on Facebook">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M15 3h-2.5A3.5 3.5 0 0 0 9 6.5V10H6v4h3v7h4v-7h3l1-4h-4V7a1 1 0 0 1 1-1h3z" /></svg>
            </a>
          </li>
          <li>
            <a href="#youtube" aria-label="Brand on YouTube">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><rect x="2" y="5" width="20" height="14" rx="4" /><path d="m10 9 5 3-5 3z" /></svg>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </footer>
</div>
```

## CSS

```css
@property --circle-footer-swell { syntax: "<length>"; inherits: true; initial-value: 0px; }

/* Wrapper: the last section plus the footer that floods over it */
.circle-footer {
  --circle-footer-seed: 6.5rem;
  --circle-footer-gap: clamp(2rem, 6vh, 3.5rem);
  --circle-footer-page: var(--surface-light); /* the last section's background */
  position: relative; isolation: isolate; font-family: var(--font-sans);
}
.circle-footer--js { background: var(--circle-footer-page); }
.circle-footer svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.circle-footer--js .circle-footer__last { padding-bottom: calc(var(--circle-footer-seed) + var(--circle-footer-gap) + 2.5rem); }

/* Footer surface: deep gradient. Without JS (or with reduced motion) it is simply a footer. */
.circle-footer__footer {
  position: relative; z-index: 1; overflow: clip; color: var(--text-inverse);
  background:
    radial-gradient(45% 35% at 100% 100%, color-mix(in srgb, var(--primary-2) 20%, transparent), transparent 70%),
    linear-gradient(180deg, color-mix(in srgb, var(--primary) 16%, var(--surface-deep)), var(--surface-deep) 65%);
}
/* JS: the lead fills a screen and is pulled up over the last section, clipped to a circle around the seed */
.circle-footer--js .circle-footer__footer {
  margin-top: -100vh; margin-top: -100svh;
  clip-path: circle(calc(var(--circle-footer-r, calc(var(--circle-footer-seed) / 2)) + var(--circle-footer-swell)) at var(--circle-footer-ox, 50%) var(--circle-footer-oy, 50%));
  transition: --circle-footer-swell var(--dur-4) var(--ease-spring);
}
.circle-footer--js .circle-footer__footer:has(.circle-footer__seed:is(:hover, :focus-visible)) { --circle-footer-swell: 0.75rem; }
.circle-footer.is-flooded .circle-footer__footer,
.circle-footer.is-focus .circle-footer__footer { clip-path: none; }
/* Focus in the last section: shrink back to the seed so nothing focused is covered */
.circle-footer.is-dormant .circle-footer__footer {
  clip-path: circle(calc(var(--circle-footer-seed) / 2 + var(--circle-footer-swell)) at var(--circle-footer-ox, 50%) var(--circle-footer-oy, 50%));
}

/* Lead: headline + seed, with ripple rings and light centred on the seed */
.circle-footer__lead {
  position: relative; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; gap: 2rem;
  padding: clamp(4rem, 10vh, 6.5rem) var(--gutter) var(--circle-footer-gap); text-align: center;
}
.circle-footer--js .circle-footer__lead { min-height: 100vh; min-height: 100svh; }
.circle-footer__rings {
  position: absolute; left: 50%; top: calc(100% - var(--circle-footer-gap) - var(--circle-footer-seed) / 2);
  width: 80vmax; aspect-ratio: 1; translate: -50% -50%; pointer-events: none;
  background:
    repeating-radial-gradient(circle, transparent 0 calc(var(--circle-footer-seed) * 0.6 - 1px), var(--border-inverse) calc(var(--circle-footer-seed) * 0.6 - 1px) calc(var(--circle-footer-seed) * 0.6)),
    radial-gradient(closest-side, color-mix(in srgb, var(--primary) 42%, transparent), color-mix(in srgb, var(--primary-2) 16%, transparent) 45%, transparent 80%);
  -webkit-mask-image: radial-gradient(closest-side, black 15%, transparent);
  mask-image: radial-gradient(closest-side, black 15%, transparent);
}
.circle-footer--js .circle-footer__rings {
  transform: scale(0.6); opacity: 0.5;
  transition: transform calc(var(--dur-5) * 1.8) var(--ease-out), opacity var(--dur-5) var(--ease-out);
}
.circle-footer.is-open .circle-footer__rings,
.circle-footer.is-focus .circle-footer__rings { transform: none; opacity: 1; }

.circle-footer__hello { position: relative; display: grid; justify-items: center; gap: 1rem; max-width: 46rem; }
.circle-footer__eyebrow { margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1.5 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.circle-footer__title { margin: 0; font: 600 clamp(2.5rem, 1.4rem + 4.4vw, 4.75rem)/0.98 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.circle-footer__glow {
  background: linear-gradient(100deg, var(--text-inverse) 0%, color-mix(in srgb, var(--primary) 40%, var(--text-inverse)) 45%, color-mix(in srgb, var(--primary-2) 75%, var(--text-inverse)) 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}

/* The seed: the button the circle grows from */
.circle-footer__seed {
  position: relative; display: grid; place-items: center; align-content: center; gap: 0.375rem;
  box-sizing: border-box; width: var(--circle-footer-seed); aspect-ratio: 1; border: 1.5px solid transparent; border-radius: 50%;
  background:
    radial-gradient(circle at 50% 15%, color-mix(in srgb, var(--primary) 50%, var(--surface-deep)), var(--surface-deep) 70%) padding-box,
    conic-gradient(from 200deg, var(--primary), var(--primary-2), color-mix(in srgb, var(--text-inverse) 35%, transparent), var(--primary)) border-box;
  box-shadow: var(--highlight-inverse), inset 0 -12px 24px -10px color-mix(in srgb, var(--primary-2) 55%, transparent);
  color: var(--text-inverse); font: 600 0.875rem/1.15 var(--font-sans); text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring);
}
.circle-footer__seed svg { transition: transform var(--dur-4) var(--ease-spring); }
.circle-footer__seed:hover svg { transform: rotate(45deg); }
.circle-footer__seed:active { transform: scale(0.95); }

/* Content assembles with staggered rises once the flood is mostly done */
.circle-footer--js .circle-footer__item {
  opacity: 0; transform: translateY(1.5rem); filter: blur(6px);
  transition: opacity var(--dur-4) var(--ease-out), transform var(--dur-5) var(--ease-out), filter var(--dur-4) var(--ease-out);
}
.circle-footer.is-open .circle-footer__item,
.circle-footer.is-focus .circle-footer__item {
  opacity: 1; transform: none; filter: none;
  transition-delay: calc(var(--circle-footer-i, 0) * var(--stagger) * 1.5);
}

/* Footer body */
.circle-footer__inner {
  display: grid; gap: clamp(2.5rem, 6vh, 4rem);
  max-width: var(--container-max); margin-inline: auto; padding: clamp(2.5rem, 6vh, 4rem) var(--gutter) 1.5rem;
}
.circle-footer__grid {
  display: grid; gap: 2.5rem; grid-template-areas: "contact" "nav" "open";
  padding-top: clamp(2rem, 5vh, 3rem); border-top: 1px solid var(--border-inverse);
}
.circle-footer__contact { grid-area: contact; min-width: 0; }
.circle-footer__nav { grid-area: nav; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; }
.circle-footer__open { grid-area: open; min-width: 0; }
.circle-footer__heading { margin: 0 0 0.875rem; color: var(--text-inverse-muted); font: 500 0.6875rem/1.4 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }

.circle-footer__phone {
  position: relative; display: inline-flex; align-items: center; min-height: 2.75rem;
  color: var(--text-inverse); font: 600 clamp(1.75rem, 1.2rem + 2vw, 2.5rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); text-decoration: none;
}
.circle-footer__phone::after {
  content: ""; position: absolute; left: 0; right: 0; bottom: 0.125rem; height: 2px; border-radius: 2px;
  background: var(--gradient-brand); transform: scaleX(0); transform-origin: left; transition: transform var(--dur-4) var(--ease-out);
}
.circle-footer__phone:hover::after { transform: scaleX(1); }
.circle-footer__lines { display: grid; gap: 0.25rem; margin: 0.75rem 0 0; padding: 0; list-style: none; }
.circle-footer__lines a {
  display: inline-flex; align-items: center; gap: 0.625rem; min-height: 2.25rem; color: var(--text-inverse); font-size: 0.9375rem; text-decoration: none;
  overflow-wrap: anywhere; transition: color var(--dur-2);
}
.circle-footer__lines svg { color: var(--text-inverse-muted); }
.circle-footer__lines a:hover { color: color-mix(in srgb, var(--primary-2) 40%, var(--text-inverse)); }

.circle-footer__links { display: grid; margin: 0; padding: 0; list-style: none; }
.circle-footer__links a {
  display: inline-flex; align-items: center; min-height: 2rem; color: var(--text-inverse); font-size: 0.9375rem; text-decoration: none;
  transition: color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.circle-footer__links a:hover { color: color-mix(in srgb, var(--primary-2) 40%, var(--text-inverse)); transform: translateX(3px); }

.circle-footer__hours { display: grid; gap: 0.25rem; margin: 0; padding: 0; list-style: none; font-size: 0.9375rem; }
.circle-footer__hours li { display: flex; justify-content: space-between; gap: 1rem; padding: 0.5rem 0.75rem; border-radius: var(--radius-md); color: var(--text-inverse-muted); }
.circle-footer__hours span:last-child { color: var(--text-inverse); font: 500 0.8125rem/1.6 var(--font-mono); white-space: nowrap; }
.circle-footer__hours li[aria-current="date"] { background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); color: var(--text-inverse); }
.circle-footer__hours li[aria-current="date"] span:first-child::after {
  content: ""; display: inline-block; width: 0.4375rem; height: 0.4375rem; margin-left: 0.5rem; border-radius: 50%; vertical-align: middle;
  background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 30%, transparent);
}
.circle-footer__note { margin: 1rem 0 0; color: var(--text-inverse-muted); font-size: 0.8125rem; line-height: 1.55; }

.circle-footer__legal {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.5rem;
  padding-top: 1.25rem; border-top: 1px solid var(--border-inverse); color: var(--text-inverse-muted); font: 0.75rem/1.5 var(--font-mono);
}
.circle-footer__legal p { margin: 0 auto 0 0; }
.circle-footer__legal-links { display: flex; flex-wrap: wrap; gap: 0 1.25rem; margin: 0; padding: 0; list-style: none; }
.circle-footer__legal-links a { display: inline-flex; align-items: center; min-height: 1.5rem; color: var(--text-inverse-muted); text-decoration: none; transition: color var(--dur-2); }
.circle-footer__legal-links a:hover { color: var(--text-inverse); }
.circle-footer__social { display: flex; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.circle-footer__social a {
  display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%;
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); color: var(--text-inverse-muted);
  transition: color var(--dur-2), background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.circle-footer__social a:hover { color: var(--text-inverse); background: color-mix(in srgb, var(--text-inverse) 10%, transparent); transform: translateY(-2px); }

.circle-footer__footer :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Demo: the light last section */
.circle-footer-demo {
  position: relative; display: grid; align-items: center; min-height: 100vh; min-height: 100svh;
  background: var(--circle-footer-page); color: var(--text-main);
}
.circle-footer-demo::before {
  content: ""; position: absolute; inset: 0; pointer-events: none;
  background:
    radial-gradient(40% 50% at 15% 10%, color-mix(in srgb, var(--primary) 9%, transparent), transparent 70%),
    radial-gradient(40% 45% at 90% 30%, color-mix(in srgb, var(--primary-2) 9%, transparent), transparent 70%);
}
.circle-footer--js .circle-footer-demo::after { /* soft contact shadow under the seed, which sits over this section */
  content: ""; position: absolute; left: 50%; bottom: calc(var(--circle-footer-gap) - 0.75rem); translate: -50% 0;
  width: calc(var(--circle-footer-seed) * 1.3); height: calc(var(--circle-footer-seed) * 0.4); pointer-events: none;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--surface-deep) 28%, transparent), transparent);
}
.circle-footer-demo__inner {
  position: relative; display: grid; justify-items: center; width: 100%; max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4rem, 12vh, 7rem) var(--gutter); text-align: center;
}
.circle-footer-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.8125rem/1.4 var(--font-mono); letter-spacing: 0.04em; }
.circle-footer-demo__title { max-width: 16ch; margin: 1rem 0 0; font: 600 clamp(2.5rem, 1.4rem + 4.5vw, 5rem)/1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.circle-footer-demo__lead { max-width: 34rem; margin: 1.5rem 0 0; color: var(--text-muted); font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem); line-height: 1.6; }
.circle-footer-demo__chips { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; margin: 2rem 0 0; padding: 0; list-style: none; }
.circle-footer-demo__chips li {
  padding: 0.5rem 0.875rem; border-radius: var(--radius-full); background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm); font-size: 0.8125rem; font-weight: 500;
}
.circle-footer-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 2.5rem 0 0; color: var(--text-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.circle-footer-demo__hint svg { animation: circle-footer-nudge 1.4s var(--ease-in-out) 0.8s 3; }

@media (min-width: 48rem) {
  .circle-footer { --circle-footer-seed: 7.5rem; }
  .circle-footer__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); grid-template-areas: "contact open" "nav nav"; gap: 2.5rem 3rem; }
}
@media (min-width: 64rem) {
  .circle-footer__grid { grid-template-columns: minmax(0, 1.2fr) minmax(0, 1.4fr) minmax(0, 1fr); grid-template-areas: "contact nav open"; }
}
@media (prefers-reduced-motion: reduce) {
  .circle-footer *, .circle-footer *::before, .circle-footer *::after { animation: none !important; }
}
@keyframes circle-footer-nudge { 50% { transform: translateY(4px); } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

document.querySelectorAll('[data-circle-footer]').forEach((root) => {
  const footer = root.querySelector('.circle-footer__footer');
  const seed = root.querySelector('.circle-footer__seed');

  // Opening hours: mark today's row
  root.querySelector(`.circle-footer__hours [data-days~="${new Date().getDay()}"]`)?.setAttribute('aria-current', 'date');

  // Reduced motion, or the footer is already on screen (short page): leave it as a normal footer
  if (reduce || footer.getBoundingClientRect().top < innerHeight) return;

  let frame = 0;
  let near = false;
  let ox = 0;
  let oy = 0;
  let r0 = 0;
  root.classList.add('circle-footer--js');

  // Scrub: the circle grows from the seed as the seed rises from the bottom edge to ~40% of the viewport
  const update = () => {
    frame = 0;
    const box = footer.getBoundingClientRect();
    const cx = box.left + ox;
    const cy = box.top + oy;
    const start = innerHeight - r0 * 1.5;
    const end = innerHeight * 0.42;
    const p = Math.min(1, Math.max(0, (start - cy) / Math.max(1, start - end)));
    const corner = Math.hypot(Math.max(cx, innerWidth - cx), Math.max(cy, innerHeight - cy));
    root.style.setProperty('--circle-footer-r', `${(r0 + (corner - r0) * p).toFixed(1)}px`);
    root.classList.toggle('is-flooded', p >= 1);
    if (p > 0.55) root.classList.add('is-open');
    else if (p < 0.3) root.classList.remove('is-open');
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(update); };

  // Origin = the seed's centre in the footer's own box; re-measured whenever layout changes
  const measure = () => {
    const box = footer.getBoundingClientRect();
    const s = seed.getBoundingClientRect();
    ox = s.left - box.left + s.width / 2;
    oy = s.top - box.top + s.height / 2;
    r0 = seed.offsetWidth / 2;
    root.style.setProperty('--circle-footer-ox', `${ox.toFixed(1)}px`);
    root.style.setProperty('--circle-footer-oy', `${oy.toFixed(1)}px`);
    queue();
  };

  new IntersectionObserver(([entry]) => {
    near = entry.isIntersecting;
    queue();
  }, { rootMargin: '25% 0px' }).observe(footer);
  new ResizeObserver(measure).observe(footer);
  addEventListener('resize', measure, { passive: true });
  addEventListener('scroll', queue, { passive: true });
  measure(); // origin is right before the first paint

  // Focus inside the footer floods it at once; focus above it shrinks the circle back to the seed
  root.addEventListener('focusin', (e) => {
    const inside = footer.contains(e.target);
    root.classList.toggle('is-focus', inside && e.target !== seed);
    root.classList.toggle('is-dormant', !inside);
  });
  root.addEventListener('focusout', () => root.classList.remove('is-focus', 'is-dormant'));
});
```

## Notes

- **Wiring:** wrap the block before the footer (usually `<main>`) and the footer in `<div class="circle-footer" data-circle-footer>`. Give that block `.circle-footer__last`; with JS it gets extra bottom padding so its content clears the seed. Set `--circle-footer-page` to its background, because that colour shows below it while the circle grows. Keep that block at `z-index: auto`. The seed (`.circle-footer__seed`) is the footer's first link, and JS measures its centre on load and resize to use as the origin.
- **How it works:** with JS, the footer's lead is one screen tall and pulled up over the last section (`margin-top: -100svh`). `clip-path` makes the overlap invisible and unclickable until the circle reaches it. Once the circle covers the viewport the clip is dropped (`is-flooded`), so a footer taller than the viewport scrolls on normally. The flood needs about 60% of a screen of scroll after the seed appears, so keep at least that much footer below the lead.
- **No JS, reduced motion, or a footer already on screen at load (short pages):** no overlap, clip or entrance. You get a normal footer whose headline sits over the seed as a round CTA, so nothing jumps.
- **Accessibility:** the footer stays in the accessibility tree throughout; the clip and the rise are visual only. Focus anywhere in the footer floods it at once (`is-focus`). Focus in the last section shrinks the circle back to the seed (`is-dormant`), so a focused element is never covered (WCAG 2.4.11). Hours are a list, and today's row gets `aria-current="date"`.
- **Support:** `clip-path: circle()` works everywhere. The hover/focus swell transitions an `@property` length behind `:has()`; older engines just skip the swell.
- **Contrast:** `--text-inverse` is about 18:1 on the deep gradient and `--text-inverse-muted` about 7:1. The "project." gradient stays at 6.8:1 or better, and the seed label is white on the darkest part of its own fill.
