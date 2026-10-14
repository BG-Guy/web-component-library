# Curved Lift Footer

The light last section ends in a deep convex curve that bulges down into a deep footer, with a soft glow leaking from beneath its edge. As you scroll toward the end, the curve flattens as if the page were a sheet being pulled taut and lifted away. A round back-to-top button sits on the curve's apex and rides it up as it flattens, the footer rises underneath with parallax, and its big "Say hello." scales up from 0.9. On phones the curve is shallower, the button smaller, and the contact links stack into full-width rows. Depends on `tokens/variables.css`.

**Motion:** one scroll-progress variable (linear scrub) drives the curve's `scaleY` flatten, the apex button's ride, the footer's parallax rise and the headline's scale 0.9→1 · button, chip and link hovers (`--dur-2`/`--dur-3`, `--ease-spring`) · smooth back-to-top scroll (instant under reduced motion) · scroll-hint nudge (three runs).

## HTML

```html
<div class="curve-footer" data-curve-footer>
  <!-- The sheet: in a real page this is your <main>; the curve hangs from its bottom edge -->
  <div class="curve-footer__sheet">
    <section class="curve-footer-demo" aria-labelledby="curve-footer-demo-title">
      <div class="curve-footer-demo__inner">
        <p class="curve-footer-demo__eyebrow">Our promise</p>
        <h2 id="curve-footer-demo-title" class="curve-footer-demo__title">If it isn't right, we come back. Free.</h2>
        <p class="curve-footer-demo__lead">Every repair carries a two-year workmanship guarantee. If something we fixed acts up, call us and we'll be back the same week, no questions and no call-out fee.</p>
        <ul class="curve-footer-demo__points" role="list">
          <li><strong>2 years</strong><span>workmanship guarantee</span></li>
          <li><strong>Same day</strong><span>callbacks on warranty jobs</span></li>
          <li><strong>$0</strong><span>call-out fee to put it right</span></li>
        </ul>
        <p class="curve-footer-demo__hint" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
          Scroll
        </p>
      </div>
    </section>
    <span class="curve-footer__curve" aria-hidden="true">
      <svg class="curve-footer__bulge" viewBox="0 0 100 100" preserveAspectRatio="none" focusable="false">
        <path class="curve-footer__fill" d="M0 0Q50 200 100 0Z" />
        <path class="curve-footer__rim" d="M0 0Q50 200 100 0" />
      </svg>
    </span>
  </div>

  <footer class="curve-footer__footer">
    <a class="curve-footer__top" href="#top" aria-label="Back to top">
      <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 19V5M6 11l6-6 6 6" /></svg>
    </a>

    <div class="curve-footer__body">
      <div class="curve-footer__inner">
        <div class="curve-footer__intro">
          <h2 class="curve-footer__hello">Say <span class="curve-footer__glow">hello.</span></h2>
          <p class="curve-footer__lead">Questions, quotes or a quick fix: a real person answers, seven days a week.</p>
        </div>

        <ul class="curve-footer__reach" role="list">
          <li>
            <a class="curve-footer__chip" href="tel:+15555550123">
              <span class="curve-footer__icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
              </span>
              <span class="curve-footer__chip-text"><small>Call or text</small>(555) 555-0123</span>
            </a>
          </li>
          <li>
            <a class="curve-footer__chip" href="mailto:hello@example.com">
              <span class="curve-footer__icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z" /><path d="m3.5 6.5 8.5 6.5 8.5-6.5" /></svg>
              </span>
              <span class="curve-footer__chip-text"><small>Email</small>hello@example.com</span>
            </a>
          </li>
          <li>
            <a class="curve-footer__btn" href="#book">
              Book a visit
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </li>
        </ul>

        <div class="curve-footer__grid">
          <nav class="curve-footer__nav" aria-label="Footer">
            <div>
              <h3 class="curve-footer__heading">Services</h3>
              <ul class="curve-footer__links" role="list">
                <li><a href="#plumbing">Plumbing</a></li>
                <li><a href="#electrical">Electrical</a></li>
                <li><a href="#heating">Heating</a></li>
                <li><a href="#roofing">Roofing</a></li>
              </ul>
            </div>
            <div>
              <h3 class="curve-footer__heading">Company</h3>
              <ul class="curve-footer__links" role="list">
                <li><a href="#about">About</a></li>
                <li><a href="#guarantee">Guarantee</a></li>
                <li><a href="#reviews">Reviews</a></li>
                <li><a href="#careers">Careers</a></li>
              </ul>
            </div>
            <div>
              <h3 class="curve-footer__heading">Areas</h3>
              <ul class="curve-footer__links" role="list">
                <li><a href="#springfield">Springfield</a></li>
                <li><a href="#westlake">Westlake</a></li>
                <li><a href="#northside">Northside</a></li>
                <li><a href="#riverside">Riverside</a></li>
              </ul>
            </div>
          </nav>
          <div class="curve-footer__open">
            <h3 class="curve-footer__heading">Hours</h3>
            <dl class="curve-footer__hours">
              <div><dt>Mon – Fri</dt><dd>7am – 7pm</dd></div>
              <div><dt>Saturday</dt><dd>8am – 4pm</dd></div>
              <div><dt>Sunday</dt><dd>Emergencies only</dd></div>
            </dl>
          </div>
        </div>

        <div class="curve-footer__legal">
          <p>© 2026 Brand Home Services · Lic. #CSL-104233</p>
          <ul class="curve-footer__legal-links" role="list">
            <li><a href="#privacy">Privacy</a></li>
            <li><a href="#terms">Terms</a></li>
            <li><a href="#accessibility">Accessibility</a></li>
          </ul>
          <ul class="curve-footer__social" role="list">
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
    </div>
  </footer>
</div>
```

## CSS

```css
/* Wrapper: light sheet over a deep footer. --curve-footer-s is the curve's depth factor:
   1 = full bulge, 0 = flat; 0.45 (a gentle static curve) without JS or with reduced motion. */
.curve-footer {
  --curve-footer-sheet: var(--surface-light);
  --curve-footer-depth: clamp(3.5rem, 12vw, 10rem);
  --curve-footer-btn: 3.5rem;
  position: relative; isolation: isolate;
  background: var(--surface-deep); font-family: var(--font-sans);
}
.curve-footer svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* The sheet and its curved bottom edge (a parabola, the shape of a sagging sheet) */
.curve-footer__sheet { position: relative; z-index: 1; background: var(--curve-footer-sheet); color: var(--text-main); }
.curve-footer__curve { position: absolute; top: calc(100% - 1px); left: 0; right: 0; height: var(--curve-footer-depth); pointer-events: none; }
.curve-footer__bulge {
  display: block; width: 100%; height: 100%; overflow: visible;
  transform-origin: 50% 0; transform: scaleY(var(--curve-footer-s, 0.45));
  filter: drop-shadow(0 1.25rem 1.75rem color-mix(in srgb, var(--primary) 34%, transparent));
}
.curve-footer__fill { fill: var(--curve-footer-sheet); stroke: none; }
.curve-footer__rim { stroke: color-mix(in srgb, var(--primary-2) 60%, transparent); stroke-width: 1.5; vector-effect: non-scaling-stroke; }

/* The footer beneath, lit from under the curve */
.curve-footer__footer {
  position: relative; color: var(--text-inverse);
  background:
    radial-gradient(45% 55% at 50% 0%, color-mix(in srgb, var(--primary) 32%, transparent), transparent 70%),
    radial-gradient(40% 50% at 100% 100%, color-mix(in srgb, var(--primary-2) 16%, transparent), transparent 70%),
    var(--surface-deep);
}
.curve-footer__body { overflow: clip; } /* clips the parallax offset; the apex button sits outside it */
.curve-footer__inner {
  display: grid; gap: clamp(2.5rem, 6vw, 4rem);
  max-width: var(--container-max); margin-inline: auto;
  padding: calc(var(--curve-footer-depth) * 0.45 + var(--curve-footer-btn) / 2 + 2.5rem) var(--gutter) 1.5rem;
}
/* JS: the content clears the apex with a transform instead, and rises faster than the page (parallax) */
.curve-footer--js .curve-footer__inner {
  padding-top: calc(var(--curve-footer-btn) / 2 + 2.5rem);
  transform: translateY(calc(var(--curve-footer-depth) * var(--curve-footer-s, 0) * 1.2));
}

/* Back to top: rides the apex of the curve */
.curve-footer__top {
  position: absolute; z-index: 2; top: 0; left: 50%;
  translate: -50% calc(var(--curve-footer-depth) * var(--curve-footer-s, 0.45) - 50%);
  display: grid; place-items: center; width: var(--curve-footer-btn); height: var(--curve-footer-btn); border-radius: 50%;
  background: var(--gradient-brand); color: var(--text-inverse);
  box-shadow: 0 0 0 0.3125rem var(--curve-footer-sheet), var(--highlight-inverse), 0 14px 30px -10px color-mix(in srgb, var(--primary) 75%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.curve-footer__top svg { transition: transform var(--dur-3) var(--ease-spring); }
.curve-footer__top:hover { transform: scale(1.06); }
.curve-footer__top:hover svg { transform: translateY(-3px); }
.curve-footer__top:active { transform: scale(0.94); }
.curve-footer__top:focus-visible { outline: 2px solid var(--primary); outline-offset: 0.5rem; }

/* Say hello */
.curve-footer__hello {
  margin: 0; transform-origin: 0 100%;
  font: 600 clamp(3.5rem, 1rem + 11vw, 10rem)/0.9 var(--font-display); letter-spacing: var(--tracking-display);
}
.curve-footer--js .curve-footer__hello { transform: scale(calc(1 - var(--curve-footer-s, 0) * 0.1)); }
.curve-footer__glow {
  background: linear-gradient(100deg, var(--text-inverse) 0%, color-mix(in srgb, var(--primary) 40%, var(--text-inverse)) 45%, color-mix(in srgb, var(--primary-2) 75%, var(--text-inverse)) 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.curve-footer__lead { max-width: 30rem; margin: 1.25rem 0 0; color: var(--text-inverse-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }

/* Contact chips and CTA */
.curve-footer__reach { display: grid; gap: 0.75rem; margin: 0; padding: 0; list-style: none; }
.curve-footer__chip {
  box-sizing: border-box; display: flex; align-items: center; gap: 0.875rem; min-height: 4rem; padding: 0.5rem 1.25rem 0.5rem 0.5rem;
  border-radius: var(--radius-full); background: var(--glass-inverse); color: var(--text-inverse); text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: background-color var(--dur-2), box-shadow var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.curve-footer__chip:hover { background: color-mix(in srgb, var(--text-inverse) 9%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-inverse) 18%, transparent), var(--highlight-inverse); }
.curve-footer__chip:active { transform: scale(0.98); }
.curve-footer__icon { display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: 50%; background: var(--gradient-brand); box-shadow: var(--highlight-inverse), 0 8px 20px -8px color-mix(in srgb, var(--primary) 80%, transparent); }
.curve-footer__chip-text { min-width: 0; overflow-wrap: anywhere; font: 600 clamp(1.0625rem, 0.9rem + 0.8vw, 1.375rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.curve-footer__chip-text small { display: block; margin-bottom: 0.1875rem; color: var(--text-inverse-muted); font: 500 0.6875rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.curve-footer__btn {
  box-sizing: border-box; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; width: 100%; min-height: 3.5rem; padding: 0 1.5rem;
  border-radius: var(--radius-full); background: var(--surface-light); color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: var(--highlight), 0 12px 40px -12px color-mix(in srgb, var(--primary) 90%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.curve-footer__btn:hover { transform: translateY(-2px); box-shadow: var(--highlight), 0 18px 48px -12px color-mix(in srgb, var(--primary-2) 90%, transparent); }
.curve-footer__btn:active { transform: scale(0.97); }
.curve-footer__btn svg { transition: transform var(--dur-3) var(--ease-spring); }
.curve-footer__btn:hover svg { transform: translateX(3px); }

/* Link columns and hours */
.curve-footer__grid { display: grid; gap: 2.5rem; padding-top: clamp(2rem, 5vw, 3rem); border-top: 1px solid var(--border-inverse); }
.curve-footer__nav { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.5rem 1rem; }
.curve-footer__heading { margin: 0 0 0.75rem; color: var(--text-inverse-muted); font: 500 0.6875rem/1.4 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.curve-footer__links { display: grid; margin: 0; padding: 0; list-style: none; }
.curve-footer__links a {
  display: inline-flex; align-items: center; min-height: 2rem; color: var(--text-inverse); font-size: 0.875rem; text-decoration: none;
  transition: color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.curve-footer__links a:hover { color: color-mix(in srgb, var(--primary-2) 40%, var(--text-inverse)); transform: translateX(3px); }
.curve-footer__hours { display: grid; gap: 0.5rem; margin: 0; font-size: 0.875rem; }
.curve-footer__hours div { display: flex; justify-content: space-between; gap: 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--border-inverse); }
.curve-footer__hours dt { color: var(--text-inverse-muted); }
.curve-footer__hours dd { margin: 0; font: 500 0.8125rem/1.5 var(--font-mono); text-align: right; }

/* Legal row */
.curve-footer__legal {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.5rem;
  padding-top: 1.25rem; border-top: 1px solid var(--border-inverse); color: var(--text-inverse-muted); font: 0.75rem/1.5 var(--font-mono);
}
.curve-footer__legal p { margin: 0 auto 0 0; }
.curve-footer__legal-links { display: flex; flex-wrap: wrap; gap: 0 1.25rem; margin: 0; padding: 0; list-style: none; }
.curve-footer__legal-links a { display: inline-flex; align-items: center; min-height: 1.5rem; color: var(--text-inverse-muted); text-decoration: none; transition: color var(--dur-2); }
.curve-footer__legal-links a:hover { color: var(--text-inverse); }
.curve-footer__social { display: flex; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.curve-footer__social a {
  display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%;
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); color: var(--text-inverse-muted);
  transition: color var(--dur-2), background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.curve-footer__social a:hover { color: var(--text-inverse); background: color-mix(in srgb, var(--text-inverse) 10%, transparent); transform: translateY(-2px); }
.curve-footer__body :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Demo: the light last section (decoration kept to the top so the curve meets plain sheet colour) */
.curve-footer-demo {
  position: relative; display: grid; align-items: center; min-height: 100vh; min-height: 100svh;
  background: radial-gradient(50% 45% at 90% 0%, color-mix(in srgb, var(--primary) 9%, transparent), transparent 70%), var(--curve-footer-sheet);
}
.curve-footer-demo__inner { width: 100%; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 12vh, 7rem) var(--gutter); }
.curve-footer-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.8125rem/1.4 var(--font-mono); letter-spacing: 0.04em; }
.curve-footer-demo__title { max-width: 15ch; margin: 1rem 0 0; font: 600 clamp(2.5rem, 1.4rem + 4.5vw, 5rem)/1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.curve-footer-demo__lead { max-width: 36rem; margin: 1.5rem 0 0; color: var(--text-muted); font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem); line-height: 1.6; }
.curve-footer-demo__points { display: grid; gap: 0.625rem; max-width: 38rem; margin: 2.5rem 0 0; padding: 0; list-style: none; }
.curve-footer-demo__points li {
  display: grid; grid-template-columns: 6.5rem minmax(0, 1fr); align-items: baseline; gap: 0.75rem; padding: 0.875rem 1rem;
  border-radius: var(--radius-xl); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md);
}
.curve-footer-demo__points strong { font: 600 clamp(1.125rem, 0.95rem + 0.8vw, 1.5rem)/1.05 var(--font-display); letter-spacing: var(--tracking-tight); }
.curve-footer-demo__points span { color: var(--text-muted); font-size: 0.8125rem; line-height: 1.35; }
.curve-footer-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 2.5rem 0 0; color: var(--text-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.curve-footer-demo__hint svg { animation: curve-footer-nudge 1.4s var(--ease-in-out) 0.8s 3; }

@media (min-width: 48rem) {
  .curve-footer { --curve-footer-btn: 4rem; }
  .curve-footer__grid { grid-template-columns: minmax(0, 2fr) minmax(14rem, 1fr); gap: 3rem; }
  .curve-footer__links a { font-size: 0.9375rem; }
  .curve-footer-demo__points { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.75rem; }
  .curve-footer-demo__points li { grid-template-columns: none; align-content: start; gap: 0.375rem; padding: 1rem; }
}
@media (min-width: 64rem) {
  .curve-footer__reach { grid-template-columns: repeat(2, minmax(0, 1fr)) auto; align-items: center; }
  .curve-footer__btn { width: auto; }
}
@media (prefers-reduced-motion: reduce) {
  .curve-footer *, .curve-footer *::before, .curve-footer *::after { animation: none !important; }
}
@keyframes curve-footer-nudge { 50% { transform: translateY(4px); } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

document.querySelectorAll('[data-curve-footer]').forEach((root) => {
  const footer = root.querySelector('.curve-footer__footer');
  const curve = root.querySelector('.curve-footer__curve');
  const toTop = root.querySelector('.curve-footer__top');

  // Back to top: a smooth glide (instant under reduced motion); focus follows to #top if the page has one
  toTop.addEventListener('click', (e) => {
    e.preventDefault();
    scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
    document.getElementById(toTop.hash.slice(1))?.focus({ preventScroll: true });
  });

  // Reduced motion, or a footer already on screen at load (short page): keep the gentle static curve
  if (reduce || footer.getBoundingClientRect().top < innerHeight) return;
  let frame = 0;
  let near = false;
  root.classList.add('curve-footer--js');

  // 0 once the whole bulge is in view, 1 when the footer is fully up (or its top reaches the viewport top)
  const update = () => {
    frame = 0;
    const r = footer.getBoundingClientRect();
    const depth = curve.offsetHeight;
    const span = Math.max(1, Math.min(r.height, innerHeight) - depth);
    const p = Math.min(1, Math.max(0, (innerHeight - depth - r.top) / span));
    root.style.setProperty('--curve-footer-s', (1 - p).toFixed(4));
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(update); };

  new IntersectionObserver(([entry]) => {
    near = entry.isIntersecting;
    queue();
  }, { rootMargin: '25% 0px' }).observe(footer);
  addEventListener('scroll', queue, { passive: true });
  addEventListener('resize', queue, { passive: true });
  update();
});
```

## Notes

- **Wiring:** wrap your main content and the footer in `<div class="curve-footer" data-curve-footer>`. Put `.curve-footer__sheet` on `<main>`; its background is `--curve-footer-sheet`, and its bottom area should stay plain so the curve's fill matches it. The `.curve-footer__curve` span is the sheet's last child. The `<footer class="curve-footer__footer">` holds the apex button and `.curve-footer__body`. The sheet must not clip overflow, because `overflow: hidden` would cut the curve off.
- **Back to top:** `href="#top"` works without JS as a native jump. JS turns it into a smooth glide and moves focus to an element with `id="top"` if the page has one (give it `tabindex="-1"`, e.g. your skip-link target), so keyboard users land at the top as well.
- **No JS, reduced motion, or a footer already on screen at load:** a static, gentle curve (`--curve-footer-s: 0.45`) with the button on its apex and the content laid out below it; nothing moves. Under reduced motion JS only wires the back-to-top link, which jumps instantly.
- **Taller footers:** the flatten completes when the footer's top reaches the top of the viewport, and the footer then scrolls normally. The parallax offset is clipped by `.curve-footer__body`, so it never adds scroll height. The flatten itself is a single `scaleY` on the curve.
- **Accessibility:** the curve SVG is `aria-hidden`. The back-to-top link has an `aria-label` and a 64px target (56px on phones), with a `--primary` focus ring at 0.5rem offset that holds 5.2:1 on the light sheet and 3.8:1 on the deep footer. Footer text is `--text-inverse` (about 18:1) or `--text-inverse-muted` (about 7:1) on `--surface-deep`, and the "hello." gradient stays at 6.8:1 or better.
- **Retheme:** set `--curve-footer-sheet` (the sheet and the curve's fill), `--curve-footer-depth` (how deep the bulge sags) and `--curve-footer-btn`. The rim and glow come from `--primary-2` and `--primary`.
