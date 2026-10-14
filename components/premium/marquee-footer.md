# Marquee CTA Footer

A deep footer that opens with an enormous edge-to-edge marquee: two rows of "Let's get your home sorted —" running in opposite directions, alternating solid and outlined type. Hover the band (or tab into it) and both rows ease to a stop and drift backwards, through an eased WAAPI `playbackRate`. A white "Start a project" circle floats over the middle and leans towards the pointer on a damped spring. Below it are contact details, three link columns, office hours with a live "Open now" line, and a back-to-top button whose ring fills as the page scrolls. On phones the type scales down to 3.5rem, the columns fold into a two-up grid and the hours stack under the contact block. Depends on `tokens/variables.css`.

**Motion:** marquee loops (WAAPI, linear, steady px/s, opposed rows) · hover/focus slow-and-reverse (`playbackRate` eased over `--dur-5`) · magnetic CTA (rAF damped spring) with label parallax · CTA hover scale and arrow turn (`--ease-spring`) · "Open now" ping (three beats) · back-to-top ring tied to page scroll. A pause button stops the marquee, and everything freezes off-screen.

## HTML

```html
<section class="marquee-footer-demo" id="marquee-footer-top" aria-labelledby="marquee-footer-demo-title">
  <div class="marquee-footer-demo__inner">
    <p class="marquee-footer-demo__eyebrow">Why Brand</p>
    <h2 id="marquee-footer-demo-title" class="marquee-footer-demo__title">Fixed right the first time, or we come back free.</h2>
    <p class="marquee-footer-demo__text">Licensed plumbers, electricians and HVAC pros across Westlake, Northside and Riverside. Upfront prices, tidy work and a two-year guarantee on every job.</p>
  </div>
</section>

<footer class="marquee-footer" aria-labelledby="marquee-footer-title" data-marquee-footer>
  <h2 id="marquee-footer-title" class="marquee-footer__sr">Let's get your home sorted</h2>

  <div class="marquee-footer__band">
    <div class="marquee-footer__rows" aria-hidden="true">
      <div class="marquee-footer__row">
        <div class="marquee-footer__track">
          <span class="marquee-footer__phrase">Let’s get your home sorted</span><span class="marquee-footer__dash">—</span>
          <span class="marquee-footer__phrase marquee-footer__phrase--outline">Let’s get your home sorted</span><span class="marquee-footer__dash">—</span>
          <span class="marquee-footer__phrase">Let’s get your home sorted</span><span class="marquee-footer__dash">—</span>
          <span class="marquee-footer__phrase marquee-footer__phrase--outline">Let’s get your home sorted</span><span class="marquee-footer__dash">—</span>
        </div>
      </div>
      <div class="marquee-footer__row marquee-footer__row--reverse">
        <div class="marquee-footer__track">
          <span class="marquee-footer__phrase marquee-footer__phrase--outline">Let’s get your home sorted</span><span class="marquee-footer__dash">—</span>
          <span class="marquee-footer__phrase">Let’s get your home sorted</span><span class="marquee-footer__dash">—</span>
          <span class="marquee-footer__phrase marquee-footer__phrase--outline">Let’s get your home sorted</span><span class="marquee-footer__dash">—</span>
          <span class="marquee-footer__phrase">Let’s get your home sorted</span><span class="marquee-footer__dash">—</span>
        </div>
      </div>
    </div>
    <a class="marquee-footer__cta" href="#contact">
      <span class="marquee-footer__cta-label">
        Start a project
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </span>
    </a>
    <button class="marquee-footer__pause" type="button" aria-pressed="false" aria-label="Pause marquee" hidden>
      <svg class="marquee-footer__icon-pause" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
      <svg class="marquee-footer__icon-play" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
    </button>
  </div>

  <div class="marquee-footer__inner">
    <div class="marquee-footer__grid">
      <div class="marquee-footer__brand">
        <a class="marquee-footer__logo" href="/">
          <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M3 11 12 4l9 7M5.5 9.5V20h13V9.5M10 20v-5h4v5" /></svg>
          Brand
        </a>
        <p class="marquee-footer__tagline">Plumbing, electrical and heating for Springfield homes since 2009.</p>
        <address class="marquee-footer__contact">
          <a class="marquee-footer__phone" href="tel:+15555550123">(555) 555-0123</a>
          <a href="mailto:hello@example.com">hello@example.com</a>
          <span>12 Westlake Ave, Springfield</span>
        </address>
      </div>

      <nav class="marquee-footer__nav" aria-label="Footer">
        <div>
          <h3 class="marquee-footer__heading">Services</h3>
          <ul class="marquee-footer__links" role="list">
            <li><a href="#plumbing">Plumbing</a></li>
            <li><a href="#electrical">Electrical</a></li>
            <li><a href="#heating">Heating &amp; cooling</a></li>
            <li><a href="#inspections">Inspections</a></li>
          </ul>
        </div>
        <div>
          <h3 class="marquee-footer__heading">Company</h3>
          <ul class="marquee-footer__links" role="list">
            <li><a href="#about">About us</a></li>
            <li><a href="#reviews">Reviews</a></li>
            <li><a href="#careers">Careers</a></li>
            <li><a href="#guides">Home guides</a></li>
          </ul>
        </div>
        <div>
          <h3 class="marquee-footer__heading">Areas</h3>
          <ul class="marquee-footer__links" role="list">
            <li><a href="#westlake">Westlake</a></li>
            <li><a href="#northside">Northside</a></li>
            <li><a href="#riverside">Riverside</a></li>
            <li><a href="#springfield">Springfield</a></li>
          </ul>
        </div>
      </nav>

      <div class="marquee-footer__office">
        <h3 class="marquee-footer__heading">Office hours</h3>
        <p class="marquee-footer__status" hidden><span class="marquee-footer__dot"></span><span></span></p>
        <ul class="marquee-footer__hours" role="list">
          <li class="marquee-footer__day" data-days="1 2 3 4 5" data-open="7:00" data-close="19:00"><span>Mon–Fri</span><span>7:00–19:00</span></li>
          <li class="marquee-footer__day" data-days="6" data-open="8:00" data-close="16:00"><span>Saturday</span><span>8:00–16:00</span></li>
          <li class="marquee-footer__day" data-days="0"><span>Sunday</span><span>Emergencies only</span></li>
        </ul>
        <p class="marquee-footer__note">24/7 emergency line <a href="tel:+15555550199">(555) 555-0199</a></p>
      </div>
    </div>

    <div class="marquee-footer__bar">
      <p class="marquee-footer__legal">© 2026 Brand Home Services · Licensed &amp; insured</p>
      <ul class="marquee-footer__legal-links" role="list">
        <li><a href="#privacy">Privacy</a></li>
        <li><a href="#terms">Terms</a></li>
        <li><a href="#accessibility">Accessibility</a></li>
      </ul>
      <a class="marquee-footer__top" href="#marquee-footer-top">
        <svg class="marquee-footer__ring" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><circle class="marquee-footer__ring-track" cx="24" cy="24" r="22" /><path class="marquee-footer__ring-bar" d="M24 2a22 22 0 1 1 0 44a22 22 0 1 1 0-44" pathLength="1" /></svg>
        <svg class="marquee-footer__up" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 19V5M6 11l6-6 6 6" /></svg>
        <span class="marquee-footer__sr">Back to top</span>
      </a>
    </div>
  </div>
</footer>
```

## CSS

```css
/* Demo only: a short page section so the footer reads in context */
.marquee-footer-demo { background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); }
.marquee-footer-demo__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 6.5rem) var(--gutter); }
.marquee-footer-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.marquee-footer-demo__title { max-width: 40rem; margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.6vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.marquee-footer-demo__text { max-width: 36rem; margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }

/* Footer */
.marquee-footer { position: relative; overflow: clip; background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans); }
.marquee-footer__sr { position: absolute; width: 1px; height: 1px; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }
.marquee-footer :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Marquee band: two opposed rows, edge-faded, with a glow behind the CTA */
.marquee-footer__band {
  position: relative; isolation: isolate; border-bottom: 1px solid var(--border-inverse);
  background: radial-gradient(35% 60% at 50% 50%, color-mix(in srgb, var(--primary) 26%, transparent), transparent 70%);
}
.marquee-footer__rows {
  display: grid; padding-block: clamp(2.5rem, 6vw, 4.5rem);
  -webkit-mask-image: linear-gradient(90deg, transparent, black 7%, black 93%, transparent);
  mask-image: linear-gradient(90deg, transparent, black 7%, black 93%, transparent);
}
.marquee-footer__row { overflow: hidden; }
.marquee-footer__track {
  display: flex; width: max-content; white-space: nowrap;
  font: 600 clamp(3.5rem, 1rem + 11vw, 10rem)/1.04 var(--font-display); letter-spacing: var(--tracking-display);
}
.marquee-footer__row--reverse .marquee-footer__track { transform: translateX(-50%); }
/* Trailing margins (not gap) keep both halves of a track exactly equal, so -50% loops seamlessly */
.marquee-footer__phrase, .marquee-footer__dash { flex: none; margin-right: 0.28em; }
.marquee-footer__phrase--outline { color: color-mix(in srgb, var(--text-inverse) 16%, transparent); }
@supports (-webkit-text-stroke: 1px currentColor) {
  .marquee-footer__phrase--outline { color: transparent; -webkit-text-stroke: 1.5px color-mix(in srgb, var(--text-inverse) 55%, transparent); }
}
.marquee-footer__dash { background: var(--gradient-brand); -webkit-background-clip: text; background-clip: text; color: transparent; }

/* Magnetic CTA: JS moves it with --marquee-footer-mx/-my, the label a little further */
.marquee-footer__cta {
  position: absolute; top: 50%; left: 50%; z-index: 2;
  display: grid; place-items: center; width: clamp(7.5rem, 5.5rem + 7vw, 11rem); aspect-ratio: 1; border-radius: 50%;
  background: var(--surface-light); color: var(--text-main); text-align: center; text-decoration: none;
  font: 600 clamp(0.9375rem, 0.85rem + 0.35vw, 1.125rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight);
  box-shadow: 0 0 0 0.625rem color-mix(in srgb, var(--surface-light) 7%, transparent), 0 30px 60px -18px color-mix(in srgb, var(--primary) 75%, transparent);
  translate: calc(-50% + var(--marquee-footer-mx, 0px)) calc(-50% + var(--marquee-footer-my, 0px));
  transition: scale var(--dur-3) var(--ease-spring), background-color var(--dur-3) var(--ease-out), color var(--dur-3) var(--ease-out), box-shadow var(--dur-4) var(--ease-out);
}
.marquee-footer__cta:hover {
  scale: 1.06; background: var(--primary); color: var(--text-inverse);
  box-shadow: 0 0 0 1rem color-mix(in srgb, var(--primary) 18%, transparent), 0 30px 70px -16px color-mix(in srgb, var(--primary) 90%, transparent);
}
.marquee-footer__cta:active { scale: 0.96; }
.marquee-footer__cta-label { display: grid; justify-items: center; gap: 0.5rem; max-width: 72%; translate: var(--marquee-footer-lx, 0px) var(--marquee-footer-ly, 0px); }
.marquee-footer__cta svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: rotate var(--dur-3) var(--ease-spring); }
.marquee-footer__cta:hover svg { rotate: -45deg; }

/* Pause control */
.marquee-footer__pause {
  position: absolute; right: var(--gutter); bottom: 0.875rem; z-index: 2; display: grid; place-items: center;
  width: 2.25rem; height: 2.25rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse-muted); box-shadow: inset 0 0 0 1px var(--border-inverse);
  transition: color var(--dur-2) var(--ease-out), background-color var(--dur-2) var(--ease-out);
}
.marquee-footer__pause:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); color: var(--text-inverse); }
.marquee-footer__pause[hidden] { display: none; }
.marquee-footer__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.marquee-footer__icon-play, .marquee-footer__pause[aria-pressed="true"] .marquee-footer__icon-pause { display: none; }
.marquee-footer__pause[aria-pressed="true"] .marquee-footer__icon-play { display: block; }

/* Body: contact, link columns, office hours */
.marquee-footer__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(3rem, 7vw, 5rem) var(--gutter) 1.75rem; }
.marquee-footer__grid { display: grid; gap: 2.75rem; grid-template-areas: "brand" "nav" "office"; }
.marquee-footer__brand { grid-area: brand; }
.marquee-footer__nav { grid-area: nav; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2rem 1.5rem; }
.marquee-footer__office { grid-area: office; }
.marquee-footer__logo { display: inline-flex; align-items: center; gap: 0.625rem; color: var(--text-inverse); font: 600 1.375rem var(--font-display); letter-spacing: var(--tracking-tight); text-decoration: none; }
.marquee-footer__logo svg { fill: none; stroke: var(--primary-2); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.marquee-footer__tagline { max-width: 22rem; margin: 0.875rem 0 0; color: var(--text-inverse-muted); line-height: 1.6; }
.marquee-footer__contact { display: grid; justify-items: start; gap: 0.5rem; margin-top: 1.5rem; color: var(--text-inverse-muted); font-style: normal; }
.marquee-footer__contact a { color: var(--text-inverse); text-decoration: underline; text-decoration-color: transparent; text-underline-offset: 4px; transition: text-decoration-color var(--dur-2) var(--ease-out); }
.marquee-footer__contact a:hover { text-decoration-color: currentColor; }
.marquee-footer__contact .marquee-footer__phone { font: 600 clamp(1.5rem, 1.2rem + 1vw, 1.875rem)/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.marquee-footer__heading { margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.marquee-footer__links { display: grid; gap: 0.25rem; margin: 0.875rem 0 0; padding: 0; list-style: none; }
.marquee-footer__links a, .marquee-footer__legal-links a {
  display: inline-flex; align-items: center; min-height: 2rem; color: var(--text-inverse); text-decoration: underline; text-decoration-color: transparent; text-underline-offset: 4px;
  transition: text-decoration-color var(--dur-2) var(--ease-out), color var(--dur-2) var(--ease-out);
}
.marquee-footer__links a:hover, .marquee-footer__legal-links a:hover { text-decoration-color: currentColor; }

/* Office hours with a live "Open now" line */
.marquee-footer__status { display: flex; align-items: center; gap: 0.5rem; margin: 0.875rem 0 0; font-weight: 500; }
.marquee-footer__status[hidden] { display: none; }
.marquee-footer__dot { position: relative; flex: none; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--text-inverse-muted); }
.marquee-footer__status.is-open .marquee-footer__dot { background: color-mix(in srgb, var(--success) 65%, var(--text-inverse)); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 30%, transparent); }
.marquee-footer__status.is-open .marquee-footer__dot::after {
  content: ""; position: absolute; inset: 0; border-radius: 50%; background: inherit;
  animation: marquee-footer-ping 1.6s var(--ease-out) 3;
}
.marquee-footer__hours { display: grid; gap: 0.25rem; margin: 0.75rem 0 0; padding: 0; list-style: none; }
.marquee-footer__day { display: flex; justify-content: space-between; gap: 1rem; padding: 0.5rem 0.75rem; border-radius: var(--radius-md); color: var(--text-inverse-muted); }
.marquee-footer__day > :last-child { color: var(--text-inverse); font: 500 0.875rem/1.5 var(--font-mono); text-align: right; }
.marquee-footer__day.is-today { background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); color: var(--text-inverse); }
.marquee-footer__note { margin: 1rem 0 0; color: var(--text-inverse-muted); font-size: 0.875rem; }
.marquee-footer__note a { color: var(--text-inverse); font-weight: 600; text-underline-offset: 3px; }

/* Bottom bar and back-to-top ring */
.marquee-footer__bar {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.5rem; margin-top: clamp(2.5rem, 6vw, 4rem); padding-top: 1.5rem;
  border-top: 1px solid var(--border-inverse); color: var(--text-inverse-muted); font-size: 0.8125rem;
}
.marquee-footer__legal { flex: 1 1 14rem; margin: 0; }
.marquee-footer__legal-links { display: flex; flex-wrap: wrap; gap: 0 1.25rem; margin: 0; padding: 0; list-style: none; }
.marquee-footer__top {
  position: relative; display: grid; place-items: center; flex: none; width: 3rem; height: 3rem; border-radius: 50%;
  background: var(--glass-inverse); color: var(--text-inverse); transition: background-color var(--dur-2) var(--ease-out);
}
.marquee-footer__top:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.marquee-footer__ring { position: absolute; inset: 0; width: 100%; height: 100%; }
.marquee-footer__ring-track, .marquee-footer__ring-bar { fill: none; stroke-width: 2; }
.marquee-footer__ring-track { stroke: var(--border-inverse); }
.marquee-footer__ring-bar {
  stroke: color-mix(in srgb, var(--primary-2) 70%, var(--text-inverse)); stroke-linecap: round;
  stroke-dasharray: 1; stroke-dashoffset: calc(1 - var(--marquee-footer-p, 0));
}
.marquee-footer__up { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.marquee-footer__top:hover .marquee-footer__up { translate: 0 -2px; }

/* Paused or off-screen: freeze CSS loops (the marquee itself is paused in JS) */
.marquee-footer[data-paused] *, .marquee-footer[data-paused] *::before, .marquee-footer[data-paused] *::after,
.marquee-footer[data-offscreen] *, .marquee-footer[data-offscreen] *::before, .marquee-footer[data-offscreen] *::after { animation-play-state: paused !important; }

@media (min-width: 768px) {
  .marquee-footer__grid { grid-template-columns: 1fr 1fr; grid-template-areas: "brand office" "nav nav"; }
  .marquee-footer__nav { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
@media (min-width: 1024px) {
  .marquee-footer__grid { grid-template-columns: 1.15fr 2fr 1fr; grid-template-areas: "brand nav office"; gap: 3rem; }
}
@media (prefers-reduced-motion: reduce) {
  .marquee-footer *, .marquee-footer *::before, .marquee-footer *::after { animation: none !important; }
}
@keyframes marquee-footer-ping { to { transform: scale(2.8); opacity: 0; } }
```

## JS

```js
const ease = (t) => (t < 0.5 ? 2 * t * t : 1 - (-2 * t + 2) ** 2 / 2);
const DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const mins = (hm) => hm.split(':').reduce((sum, part) => sum * 60 + Number(part), 0);

document.querySelectorAll('[data-marquee-footer]').forEach((root) => {
  const $ = (part) => root.querySelector(`.marquee-footer__${part}`);
  const [band, cta, pause, toTop, status] = ['band', 'cta', 'pause', 'top', 'status'].map($);
  const tracks = [...root.querySelectorAll('.marquee-footer__track')];
  const days = [...root.querySelectorAll('.marquee-footer__day')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const token = (name) => parseFloat(getComputedStyle(root).getPropertyValue(name)) || 0;
  let paused = false;
  let onscreen = false;

  // Marquee: one linear WAAPI loop per row (the second runs the other way) at a steady 80px/s
  const anims = tracks.map((track, i) => track.animate(
    { transform: i % 2 ? ['translateX(-50%)', 'translateX(0)'] : ['translateX(0)', 'translateX(-50%)'] },
    { duration: 60000, iterations: Infinity },
  ));
  const fit = () => anims.forEach((anim, i) => {
    const progress = anim.effect.getComputedTiming().progress ?? 0;
    const duration = (tracks[i].scrollWidth / 2 / 80) * 1000;
    anim.effect.updateTiming({ duration });
    anim.currentTime = progress * duration;
  });
  const sync = () => {
    const run = onscreen && !paused && !reduce.matches;
    anims.forEach((anim) => (run ? anim.play() : anim.pause()));
    pause.hidden = reduce.matches;
  };
  sync();
  new ResizeObserver(fit).observe(tracks[0]);
  reduce.addEventListener('change', sync);
  pause.addEventListener('click', () => {
    paused = !paused;
    pause.setAttribute('aria-pressed', String(paused));
    root.toggleAttribute('data-paused', paused);
    sync();
  });

  // Hover or focus in the band eases both rows to a slow reverse; leaving eases them back
  let rate = 1;
  let rampFrame = 0;
  const ramp = (to) => {
    cancelAnimationFrame(rampFrame);
    const from = rate;
    const start = performance.now();
    const duration = token('--dur-5') || 1;
    const step = (now) => {
      const t = Math.min(1, (now - start) / duration);
      rate = from + (to - from) * ease(t);
      anims.forEach((anim) => { anim.playbackRate = rate; });
      if (t < 1) rampFrame = requestAnimationFrame(step);
    };
    rampFrame = requestAnimationFrame(step);
  };

  // Magnetic CTA: a damped spring pulls it towards a nearby mouse pointer, at most 56px off centre
  const s = { x: 0, y: 0, vx: 0, vy: 0 };
  let pointer = null;
  let springFrame = 0;
  let last = 0;
  const spring = (now) => {
    const dt = last ? Math.min(0.032, (now - last) / 1000) : 1 / 60;
    last = now;
    let tx = 0;
    let ty = 0;
    if (pointer) {
      const r = band.getBoundingClientRect();
      const dx = pointer.x - (r.left + r.width / 2);
      const dy = pointer.y - (r.top + r.height / 2);
      const d = Math.hypot(dx, dy);
      const pull = d < cta.offsetWidth * 1.5 ? Math.min(0.4, 56 / d) : 0;
      tx = dx * pull;
      ty = dy * pull;
    }
    s.vx += ((tx - s.x) * 180 - s.vx * 16) * dt;
    s.vy += ((ty - s.y) * 180 - s.vy * 16) * dt;
    s.x += s.vx * dt;
    s.y += s.vy * dt;
    cta.style.setProperty('--marquee-footer-mx', `${s.x.toFixed(2)}px`);
    cta.style.setProperty('--marquee-footer-my', `${s.y.toFixed(2)}px`);
    cta.style.setProperty('--marquee-footer-lx', `${(s.x * 0.35).toFixed(2)}px`);
    cta.style.setProperty('--marquee-footer-ly', `${(s.y * 0.35).toFixed(2)}px`);
    const settled = Math.abs(tx - s.x) + Math.abs(ty - s.y) + Math.abs(s.vx) + Math.abs(s.vy) < 0.3;
    springFrame = settled || !onscreen ? 0 : requestAnimationFrame(spring);
    if (!springFrame) last = 0;
  };
  const wake = () => { if (!springFrame && !reduce.matches) springFrame = requestAnimationFrame(spring); };

  band.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse') ramp(-0.35); });
  band.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    pointer = { x: e.clientX, y: e.clientY };
    wake();
  }, { passive: true });
  band.addEventListener('pointerleave', () => { pointer = null; wake(); ramp(1); });
  band.addEventListener('focusin', () => ramp(-0.35));
  band.addEventListener('focusout', (e) => { if (!band.contains(e.relatedTarget)) ramp(1); });

  // Back to top: the ring fills with page progress (rAF-throttled, passive, only while the footer is visible)
  let scrollFrame = 0;
  const progress = () => {
    scrollFrame = 0;
    const max = document.documentElement.scrollHeight - innerHeight;
    root.style.setProperty('--marquee-footer-p', max > 0 ? Math.min(1, scrollY / max).toFixed(3) : '1');
  };
  const onScroll = () => { if (!scrollFrame) scrollFrame = requestAnimationFrame(progress); };
  toTop.addEventListener('click', (e) => {
    e.preventDefault();
    scrollTo({ top: 0, behavior: reduce.matches ? 'auto' : 'smooth' });
    const target = document.querySelector(toTop.hash);
    if (!target) return;
    if (!target.hasAttribute('tabindex')) target.tabIndex = -1;
    target.focus({ preventScroll: true });
  });
  new IntersectionObserver(([entry]) => {
    onscreen = entry.isIntersecting;
    root.toggleAttribute('data-offscreen', !onscreen);
    sync();
    if (!onscreen) return removeEventListener('scroll', onScroll);
    addEventListener('scroll', onScroll, { passive: true });
    progress();
  }).observe(root);

  // Office hours: "Open now" from the clock (the office's time zone when data-timezone is set)
  const rule = (day) => days.find((li) => li.dataset.days.split(' ').includes(String(day)));
  const clock = () => {
    const zone = root.dataset.timezone;
    const now = zone ? new Date(new Date().toLocaleString('en-US', { timeZone: zone })) : new Date();
    const day = now.getDay();
    const t = now.getHours() * 60 + now.getMinutes();
    const today = rule(day);
    const open = Boolean(today?.dataset.open) && t >= mins(today.dataset.open) && t < mins(today.dataset.close);
    let text = open ? `Open now · until ${today.dataset.close}` : 'Closed';
    for (let i = 0; !open && i < 7; i += 1) {
      const next = rule((day + i) % 7);
      if (next?.dataset.open && (i > 0 || t < mins(next.dataset.open))) {
        text = `Closed · opens ${i === 0 ? 'today' : i === 1 ? 'tomorrow' : DAYS[(day + i) % 7]} ${next.dataset.open}`;
        break;
      }
    }
    days.forEach((li) => li.classList.toggle('is-today', li === today));
    status.classList.toggle('is-open', open);
    status.lastElementChild.textContent = text;
    status.hidden = false;
  };
  clock();
  setInterval(clock, 60000);
});
```

## Notes

- The marquee rows are `aria-hidden`, and a visually hidden `<h2>` ("Let's get your home sorted") names the `<footer>` landmark. The CTA, pause button and back-to-top are real links and buttons with visible focus. Back-to-top is a plain `#marquee-footer-top` link: JS adds a smooth scroll (instant under reduced motion) and moves focus to the target, so keyboard users land at the top as well.
- The marquee meets WCAG 2.2.2. A pause button (`aria-pressed`) stops it, hovering or focusing the band reverses it slowly, and it freezes whenever the footer is off-screen. Under reduced motion the rows stay put, the pause button hides and the CTA isn't magnetic. The "Open now" ping runs three beats and stops.
- Without JS the rows are static, the CTA and links all work, the back-to-top ring stays empty and the hours list shows without a status line.
- Contrast: footer text is `--text-inverse` (about 19:1) and `--text-inverse-muted` (7.7:1) on `--surface-deep`. The CTA label is `--text-main` on white (14.6:1), or `--text-inverse` on `--primary` on hover (5.2:1). The "Open now" state is carried in text too, so it doesn't rely on the green dot.
- To wire it into a real page, put the footer last in `<body>` and point the back-to-top `href` at your skip-link target or `<main>`. Set `data-timezone="America/Chicago"` (any IANA zone) on the footer so "Open now" uses the office's clock rather than the visitor's. Edit hours in the `data-days`/`data-open`/`data-close` attributes (days 0–6, 24-hour times). The marquee speed is the `80` (px/s) in `fit()`.
