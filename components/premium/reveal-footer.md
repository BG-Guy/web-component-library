# Sticky Reveal Footer

The page lifts away like a sheet to uncover a deep footer waiting underneath. The main content keeps its own background, rounded bottom corners and a lit edge while it scrolls up, and the footer sits beneath it with `position: sticky; bottom: 0`, so no footer height is hard-coded. As the footer is uncovered, its content parallaxes up and scales from 0.95 to 1, a dim overlay lifts, and a giant outlined wordmark fills with light. Wherever the footer is taller than the screen (most phones), it falls back to normal flow with the same layered look. Depends on `tokens/variables.css`.

**Motion:** one scroll-progress variable (linear scrub) drives content parallax + scale 0.95→1, the dim overlay fade and the wordmark's outline→gradient fill · card, link and button hovers (`--dur-2`/`--dur-3`, `--ease-spring`) · scroll-hint nudge (three runs, then still).

## HTML

```html
<div class="reveal-footer" data-reveal-footer>
  <!-- The sheet: in a real page this is your <main> (plus anything else that should lift away) -->
  <div class="reveal-footer__sheet">
    <section class="reveal-footer-demo" aria-labelledby="reveal-footer-demo-title">
      <div class="reveal-footer-demo__inner">
        <p class="reveal-footer-demo__eyebrow">Brand Home Services · Springfield</p>
        <h2 id="reveal-footer-demo-title" class="reveal-footer-demo__title">Good work should feel this easy.</h2>
        <p class="reveal-footer-demo__lead">Upfront prices, two-hour arrival windows and a crew that cleans up before it leaves. Keep scrolling: this page lifts away to show what's underneath.</p>
        <ul class="reveal-footer-demo__stats" role="list">
          <li><strong>4.9/5</strong><span>from 1,200+ reviews</span></li>
          <li><strong>2 hr</strong><span>arrival windows</span></li>
          <li><strong>12k</strong><span>jobs since 2009</span></li>
        </ul>
        <p class="reveal-footer-demo__hint" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
          Scroll
        </p>
      </div>
    </section>
  </div>

  <footer class="reveal-footer__footer">
    <div class="reveal-footer__stage">
      <div class="reveal-footer__inner">
        <div class="reveal-footer__top">
          <div class="reveal-footer__cta">
            <p class="reveal-footer__pill"><span class="reveal-footer__dot" aria-hidden="true"></span>Open now · Mon–Sat, 7am–8pm</p>
            <h2 class="reveal-footer__title">Let's fix it <span class="reveal-footer__glow">today.</span></h2>
            <a class="reveal-footer__btn" href="#book">
              Book a visit
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </div>

          <ul class="reveal-footer__contact" role="list">
            <li>
              <a class="reveal-footer__card" href="tel:+15555550123">
                <span class="reveal-footer__icon" aria-hidden="true">
                  <svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
                </span>
                <span class="reveal-footer__card-text"><small>Call or text, 24/7</small>(555) 555-0123</span>
                <svg class="reveal-footer__card-arrow" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg>
              </a>
            </li>
            <li>
              <a class="reveal-footer__card" href="mailto:hello@example.com">
                <span class="reveal-footer__icon" aria-hidden="true">
                  <svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z" /><path d="m3.5 6.5 8.5 6.5 8.5-6.5" /></svg>
                </span>
                <span class="reveal-footer__card-text"><small>Quotes within 2 hours</small>hello@example.com</span>
                <svg class="reveal-footer__card-arrow" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg>
              </a>
            </li>
          </ul>
        </div>

        <div class="reveal-footer__mid">
          <nav class="reveal-footer__nav" aria-label="Footer">
            <div>
              <h3 class="reveal-footer__heading">Services</h3>
              <ul class="reveal-footer__links" role="list">
                <li><a href="#plumbing">Plumbing</a></li>
                <li><a href="#electrical">Electrical</a></li>
                <li><a href="#heating">Heating</a></li>
                <li><a href="#roofing">Roofing</a></li>
              </ul>
            </div>
            <div>
              <h3 class="reveal-footer__heading">Company</h3>
              <ul class="reveal-footer__links" role="list">
                <li><a href="#about">About</a></li>
                <li><a href="#reviews">Reviews</a></li>
                <li><a href="#careers">Careers</a></li>
                <li><a href="#journal">Journal</a></li>
              </ul>
            </div>
            <div>
              <h3 class="reveal-footer__heading">Areas</h3>
              <ul class="reveal-footer__links" role="list">
                <li><a href="#springfield">Springfield</a></li>
                <li><a href="#westlake">Westlake</a></li>
                <li><a href="#northside">Northside</a></li>
                <li><a href="#riverside">Riverside</a></li>
              </ul>
            </div>
          </nav>

          <form class="reveal-footer__news" action="#">
            <h3 class="reveal-footer__heading">Newsletter</h3>
            <p class="reveal-footer__note">Seasonal maintenance tips, four times a year. No spam.</p>
            <div class="reveal-footer__field">
              <label class="reveal-footer__label">
                <span class="reveal-footer__sr">Email address</span>
                <input class="reveal-footer__input" type="email" name="email" placeholder="you@example.com" autocomplete="email" required>
              </label>
              <button class="reveal-footer__submit" type="submit">Subscribe</button>
            </div>
            <p class="reveal-footer__status" role="status"></p>
          </form>
        </div>

        <div class="reveal-footer__legal">
          <p>© 2026 Brand Home Services · Licensed &amp; insured · Lic. #CSL-104233</p>
          <ul role="list">
            <li><a href="#privacy">Privacy</a></li>
            <li><a href="#terms">Terms</a></li>
            <li><a href="#accessibility">Accessibility</a></li>
          </ul>
        </div>
      </div>

      <div class="reveal-footer__wordmark" data-text="Brand" aria-hidden="true">Brand</div>
    </div>
    <span class="reveal-footer__dim" aria-hidden="true"></span>
  </footer>
</div>
```

## CSS

```css
/* Wrapper: the deep surface the sheet lifts off. isolation keeps the z-indexes local. */
.reveal-footer {
  --reveal-footer-radius: clamp(var(--radius-2xl), 4vw, 3rem);
  position: relative; isolation: isolate;
  background: var(--surface-deep); font-family: var(--font-sans);
}
.reveal-footer svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* The sheet: your page, with its own background, rounded bottom corners and a lit edge */
.reveal-footer__sheet {
  position: relative; z-index: 1; overflow: clip;
  border-radius: 0 0 var(--reveal-footer-radius) var(--reveal-footer-radius);
  background: var(--surface-light); color: var(--text-main);
  box-shadow:
    0 2px 0 color-mix(in srgb, var(--primary-2) 45%, transparent),
    0 40px 80px -24px color-mix(in srgb, var(--surface-deep) 90%, transparent);
}

/* The footer waits underneath, stuck to the bottom of the viewport */
.reveal-footer__footer {
  position: relative; z-index: 0; overflow: clip; container-type: inline-size;
  color: var(--text-inverse);
  background:
    radial-gradient(55% 45% at 10% 0%, color-mix(in srgb, var(--primary) 28%, transparent), transparent 70%),
    radial-gradient(45% 55% at 95% 25%, color-mix(in srgb, var(--primary-2) 18%, transparent), transparent 70%),
    var(--surface-deep);
}
/* Without JS the reveal only switches on where this footer is sure to fit; with JS it is measured */
@media (min-width: 48rem) and (min-height: 44rem) {
  .reveal-footer__footer { position: sticky; bottom: 0; }
}
.reveal-footer--js .reveal-footer__footer { position: sticky; bottom: 0; }
.reveal-footer--js.reveal-footer--flow .reveal-footer__footer { position: relative; }
/* Focus is never hidden under the sheet: the footer comes forward while it holds focus */
.reveal-footer:not(.reveal-footer--flow) .reveal-footer__footer:focus-within { z-index: 2; }

/* Scrubbed by --reveal-footer-p (0 covered → 1 revealed; 1 without JS) */
.reveal-footer__stage {
  position: relative; transform-origin: 50% 0;
  transform: translateY(calc((1 - var(--reveal-footer-p, 1)) * 16vh)) scale(calc(0.95 + var(--reveal-footer-p, 1) * 0.05));
}
.reveal-footer__stage::before { /* light pooling behind the wordmark */
  content: ""; position: absolute; left: 50%; bottom: -35%; width: min(72rem, 120%); aspect-ratio: 2.2; translate: -50% 0;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--primary-2) 32%, transparent), color-mix(in srgb, var(--primary) 14%, transparent) 55%, transparent);
  opacity: var(--reveal-footer-p, 1); pointer-events: none;
}
.reveal-footer__dim { /* shade under the sheet, deepest at its edge */
  position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(to bottom, var(--surface-deep), color-mix(in srgb, var(--surface-deep) 62%, transparent) 40%, color-mix(in srgb, var(--surface-deep) 45%, transparent));
  opacity: calc(1 - var(--reveal-footer-p, 1));
}

/* Layout */
.reveal-footer__inner {
  position: relative; display: grid; gap: clamp(1.5rem, 4vh, 3rem);
  max-width: var(--container-max); margin-inline: auto;
  padding: clamp(2.25rem, 6vh, 4.5rem) var(--gutter) 0;
}
.reveal-footer__top { display: grid; gap: 2rem; }
.reveal-footer__cta { display: grid; justify-items: start; gap: 1.25rem; }
.reveal-footer__pill {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.3125rem 0.75rem 0.3125rem 0.625rem;
  border-radius: var(--radius-full); background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  color: var(--text-inverse-muted); font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.02em;
}
.reveal-footer__dot { width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 30%, transparent), 0 0 12px var(--success); }
.reveal-footer__title { margin: 0; font: 600 clamp(2.75rem, 1.5rem + 4.6vw, 5.25rem)/0.94 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.reveal-footer__glow {
  background: linear-gradient(100deg, var(--text-inverse) 0%, color-mix(in srgb, var(--primary) 40%, var(--text-inverse)) 45%, color-mix(in srgb, var(--primary-2) 75%, var(--text-inverse)) 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}

/* Primary CTA: bright pill with a coloured glow */
.reveal-footer__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: var(--highlight), 0 12px 40px -12px color-mix(in srgb, var(--primary) 90%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.reveal-footer__btn:hover { transform: translateY(-2px); box-shadow: var(--highlight), 0 18px 48px -12px color-mix(in srgb, var(--primary-2) 90%, transparent); }
.reveal-footer__btn:active { transform: scale(0.97); }
.reveal-footer__btn svg { transition: transform var(--dur-3) var(--ease-spring); }
.reveal-footer__btn:hover svg { transform: translateX(3px); }

/* Big contact links as glass cards */
.reveal-footer__contact { display: grid; gap: 0.75rem; align-content: end; margin: 0; padding: 0; list-style: none; }
.reveal-footer__card {
  box-sizing: border-box; display: flex; align-items: center; gap: 0.75rem; min-height: 4.25rem; padding: 0.625rem 1rem 0.625rem 0.625rem;
  border-radius: var(--radius-2xl); background: var(--glass-inverse); color: var(--text-inverse); text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: background-color var(--dur-2), box-shadow var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.reveal-footer__card:hover { background: color-mix(in srgb, var(--text-inverse) 8%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-inverse) 18%, transparent), var(--highlight-inverse); }
.reveal-footer__card:active { transform: scale(0.98); }
.reveal-footer__icon {
  flex: none; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: var(--radius-xl);
  background: var(--gradient-brand); box-shadow: var(--highlight-inverse), 0 8px 20px -8px color-mix(in srgb, var(--primary) 80%, transparent);
}
.reveal-footer__card-text {
  flex: 1; min-width: 0; overflow-wrap: anywhere;
  font: 600 clamp(1.125rem, 0.8rem + 1.5vw, 1.75rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight);
}
.reveal-footer__card-text small { display: block; margin-bottom: 0.3125rem; color: var(--text-inverse-muted); font: 500 0.75rem/1.2 var(--font-mono); letter-spacing: 0.02em; }
.reveal-footer__card-arrow { color: var(--text-inverse-muted); transition: transform var(--dur-3) var(--ease-spring), color var(--dur-2); }
.reveal-footer__card:hover .reveal-footer__card-arrow { color: var(--text-inverse); transform: translate(2px, -2px); }

/* Link columns and newsletter */
.reveal-footer__mid { display: grid; gap: 2rem; padding-top: clamp(1.5rem, 4vh, 2.75rem); border-top: 1px solid var(--border-inverse); }
.reveal-footer__nav { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.5rem 1rem; }
.reveal-footer__heading { margin: 0 0 0.625rem; color: var(--text-inverse-muted); font: 500 0.6875rem/1.4 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.reveal-footer__links { display: grid; margin: 0; padding: 0; list-style: none; }
.reveal-footer__links a {
  display: inline-flex; align-items: center; min-height: 1.75rem; color: var(--text-inverse); font-size: 0.875rem; text-decoration: none;
  transition: color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.reveal-footer__links a:hover { color: color-mix(in srgb, var(--primary-2) 40%, var(--text-inverse)); transform: translateX(3px); }
.reveal-footer__news { min-width: 0; }
.reveal-footer__note { margin: 0 0 0.875rem; color: var(--text-inverse-muted); font-size: 0.875rem; line-height: 1.5; }
.reveal-footer__field {
  display: flex; align-items: center; gap: 0.375rem; max-width: 26rem; padding: 0.3125rem; border-radius: var(--radius-full);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: box-shadow var(--dur-2);
}
.reveal-footer__field:focus-within { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 60%, var(--text-inverse)), 0 0 0 4px color-mix(in srgb, var(--primary-2) 22%, transparent); }
.reveal-footer__label { flex: 1; min-width: 0; display: flex; }
.reveal-footer__input {
  flex: 1; min-width: 0; height: 2.75rem; padding: 0 0.875rem; border: 0; border-radius: var(--radius-full);
  background: transparent; color: var(--text-inverse); font: inherit; font-size: 0.9375rem;
}
.reveal-footer__input::placeholder { color: var(--text-inverse-muted); opacity: 1; }
.reveal-footer__submit {
  flex: none; height: 2.75rem; padding: 0 1.125rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--surface-light); color: var(--text-main); font: 600 0.875rem var(--font-sans);
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2);
}
.reveal-footer__submit:hover { background: color-mix(in srgb, var(--surface-light) 86%, var(--primary-2)); }
.reveal-footer__submit:active { transform: scale(0.95); }
.reveal-footer__status { min-height: 1.25rem; margin: 0.625rem 0 0; color: color-mix(in srgb, var(--primary-2) 40%, var(--text-inverse)); font-size: 0.8125rem; }
.reveal-footer__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* Legal row */
.reveal-footer__legal {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.5rem 1.5rem;
  padding-top: 1.25rem; border-top: 1px solid var(--border-inverse); color: var(--text-inverse-muted); font: 0.75rem/1.5 var(--font-mono);
}
.reveal-footer__legal p { margin: 0; }
.reveal-footer__legal ul { display: flex; flex-wrap: wrap; gap: 0 1.25rem; margin: 0; padding: 0; list-style: none; }
.reveal-footer__legal a { display: inline-flex; align-items: center; min-height: 1.5rem; color: var(--text-inverse-muted); text-decoration: none; transition: color var(--dur-2); }
.reveal-footer__legal a:hover { color: var(--text-inverse); }

/* Giant wordmark: a faint outline that fills with light as the footer is revealed; bleeds off the bottom */
.reveal-footer__wordmark {
  position: relative; margin: clamp(1.25rem, 3vh, 2rem) 0 -0.26em;
  font: 700 clamp(5rem, 26cqi, 16rem)/0.74 var(--font-display); letter-spacing: -0.065em; text-align: center; white-space: nowrap;
  color: transparent; -webkit-text-stroke: 1px color-mix(in srgb, var(--text-inverse) 22%, transparent);
  user-select: none; pointer-events: none;
}
.reveal-footer__wordmark::after {
  content: attr(data-text); position: absolute; inset: 0; -webkit-text-stroke: 0;
  background: linear-gradient(180deg, var(--text-inverse) 15%, color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse)) 50%, color-mix(in srgb, var(--primary) 70%, transparent) 88%);
  -webkit-background-clip: text; background-clip: text;
  opacity: var(--reveal-footer-p, 1);
}

/* Focus on the dark surface */
.reveal-footer__footer :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.reveal-footer__input:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }

/* Demo page section on the sheet */
.reveal-footer-demo {
  position: relative; display: grid; align-items: center; min-height: 90vh; min-height: 90svh;
  background: radial-gradient(80% 60% at 85% 0%, color-mix(in srgb, var(--primary) 8%, transparent), transparent 70%), var(--surface-light);
}
.reveal-footer-demo::before {
  content: ""; position: absolute; inset: 0; pointer-events: none;
  background-image: radial-gradient(circle, color-mix(in srgb, var(--text-main) 14%, transparent) 1px, transparent 1.5px);
  background-size: 22px 22px;
  -webkit-mask-image: radial-gradient(ellipse 70% 70% at 75% 25%, black, transparent 75%);
  mask-image: radial-gradient(ellipse 70% 70% at 75% 25%, black, transparent 75%);
}
.reveal-footer-demo__inner { position: relative; width: 100%; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 12vh, 7rem) var(--gutter); }
.reveal-footer-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.8125rem/1.4 var(--font-mono); letter-spacing: 0.04em; }
.reveal-footer-demo__title { max-width: 14ch; margin: 1rem 0 0; font: 600 clamp(2.5rem, 1.4rem + 4.5vw, 5rem)/1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.reveal-footer-demo__lead { max-width: 36rem; margin: 1.5rem 0 0; color: var(--text-muted); font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem); line-height: 1.6; }
.reveal-footer-demo__stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.75rem; max-width: 36rem; margin: 2.5rem 0 0; padding: 0; list-style: none; }
.reveal-footer-demo__stats li { display: grid; align-content: start; gap: 0.375rem; padding: 1rem; border-radius: var(--radius-xl); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md); }
.reveal-footer-demo__stats strong { font: 600 clamp(1.25rem, 1rem + 1vw, 1.75rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.reveal-footer-demo__stats span { color: var(--text-muted); font-size: 0.8125rem; line-height: 1.35; }
.reveal-footer-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 2.5rem 0 0; color: var(--text-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.reveal-footer-demo__hint svg { animation: reveal-footer-nudge 1.4s var(--ease-in-out) 0.8s 3; }

@media (min-width: 48rem) {
  .reveal-footer__mid { grid-template-columns: minmax(0, 1.6fr) minmax(15rem, 1fr); gap: 2.5rem; }
  .reveal-footer__nav { gap: 1.5rem; }
  .reveal-footer__links a { font-size: 0.9375rem; }
}
@media (min-width: 64rem) {
  .reveal-footer__top { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); align-items: end; gap: 3rem; }
}

/* Reduced motion: the reveal and the light stay, the parallax and scale go */
@media (prefers-reduced-motion: reduce) {
  .reveal-footer__stage { transform: none; }
  .reveal-footer *, .reveal-footer *::before, .reveal-footer *::after { animation: none !important; }
}
@keyframes reveal-footer-nudge { 50% { transform: translateY(4px); } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('[data-reveal-footer]').forEach((root) => {
  const sheet = root.querySelector('.reveal-footer__sheet');
  const footer = root.querySelector('.reveal-footer__footer');
  let frame = 0;
  let near = false;
  root.classList.add('reveal-footer--js');

  // 0 while the sheet still covers the footer, 1 once it has lifted clear (always 1 in flow mode)
  const update = () => {
    frame = 0;
    const flow = root.classList.contains('reveal-footer--flow');
    const lifted = innerHeight - sheet.getBoundingClientRect().bottom;
    const p = flow ? 1 : Math.min(1, Math.max(0, lifted / footer.offsetHeight));
    root.style.setProperty('--reveal-footer-p', p.toFixed(4));
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(update); };

  // A footer taller than the viewport could never show its top: fall back to normal flow
  const fit = () => {
    root.classList.toggle('reveal-footer--flow', footer.offsetHeight > innerHeight);
    queue();
  };

  new IntersectionObserver(([entry]) => {
    near = entry.isIntersecting;
    queue();
  }, { rootMargin: '50% 0px' }).observe(root);
  new ResizeObserver(fit).observe(footer);
  addEventListener('resize', fit, { passive: true });
  addEventListener('scroll', queue, { passive: true });

  // Tabbing into a footer that is still under the sheet: lift the sheet clear so focus is never hidden
  footer.addEventListener('focusin', () => {
    if (root.classList.contains('reveal-footer--flow') || root.getBoundingClientRect().bottom <= innerHeight + 1) return;
    root.scrollIntoView({ block: 'end', behavior: reduce.matches ? 'auto' : 'smooth' });
  });

  // Newsletter: the browser validates the address, then we confirm in place
  root.querySelectorAll('.reveal-footer__news').forEach((form) => form.addEventListener('submit', (e) => {
    e.preventDefault();
    form.querySelector('.reveal-footer__status').textContent = 'Thanks! Check your inbox to confirm.';
    form.reset();
  }));
});
```

## Notes

- **Wiring:** wrap everything that should lift away plus the footer in `<div class="reveal-footer" data-reveal-footer>`. Put `.reveal-footer__sheet` on your `<main>` (or a wrapper around header + main); it needs an opaque background and clips its children to the rounded corners (`overflow: clip`). The `<footer class="reveal-footer__footer">` must be the wrapper's last child. Sticky breaks if any ancestor has `overflow: hidden | auto | scroll`; `overflow: clip` is fine.
- **Taller than the viewport:** JS compares the footer's height with `innerHeight` on load, resize and content changes, and toggles `.reveal-footer--flow`. That drops `sticky`, shows the end state and keeps the sheet's rounded edge. Phones usually take this path. Without JS, sticky only switches on at ≥ 768px wide and ≥ 704px tall, where this footer (about 640px tall from 1024px wide) fits. Raise those numbers if you add rows.
- **No JS:** the CSS-only reveal still plays inside that media query. Content sits at its end state: no parallax, scale, dim or fill. **Reduced motion:** the dim overlay still fades and the wordmark still fills (opacity only), but the content never translates or scales.
- **Accessibility:** one `contentinfo` landmark, with the link columns in a labelled `<nav>`. The wordmark is `aria-hidden` (the brand name is in the legal row). If focus lands in the footer while the sheet still covers it, the footer is raised above the sheet (pure CSS) and JS scrolls to the end so the focused element is never obscured (WCAG 2.4.11).
- **Contrast on `--surface-deep`:** `--text-inverse` is about 18:1 and `--text-inverse-muted` about 7:1. The "today." gradient bottoms out near 6.8:1 at its teal end, and the white CTA button carries `--text-main` (14.6:1).
- **Retheme:** change `--reveal-footer-radius`, the sheet's background or the footer's two radial lights. The progress variable `--reveal-footer-p` is public, so you can hang more effects on it.
