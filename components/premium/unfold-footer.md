# Origami Unfold Footer

A light paper footer that arrives folded and opens like a map as it scrolls into view. It hangs from the deep section above in three horizontal panels: the top one hinges down from that section's edge (rotateX −90° → 0, origin top), then the middle one, then the bottom, each starting as the one above it lies flat. While a panel is angled it carries simulated light: a bright crease and shading that deepens toward its far edge, over a faint paper grain. The content follows the folds (CTA and contact, link columns with a little service-area map, then legal, socials and a debossed wordmark), and on phones each panel stacks its content and unfolds the same way. Depends on `tokens/variables.css`.

**Motion:** per-panel scroll scrub (linear) of `perspective() rotateX()` from −90° to 0, strictly in sequence · shade and crease highlight fade with the angle · button, link and social hovers (`--dur-2`/`--dur-3`, `--ease-spring`) · scroll-hint nudge (three runs).

## HTML

```html
<section class="unfold-footer-demo" aria-labelledby="unfold-footer-demo-title">
  <div class="unfold-footer-demo__inner">
    <p class="unfold-footer-demo__eyebrow">Before you go</p>
    <h2 id="unfold-footer-demo-title" class="unfold-footer-demo__title">Everything you need, folded into one sheet.</h2>
    <p class="unfold-footer-demo__lead">Numbers, hours, the areas we cover and every page on the site. Keep scrolling and the footer opens like a map.</p>
    <p class="unfold-footer-demo__hint" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
      Scroll
    </p>
  </div>
</section>

<footer class="unfold-footer" data-unfold-footer>
  <div class="unfold-footer__sheet">
    <!-- Panel 1: CTA and contact -->
    <div class="unfold-footer__panel unfold-footer__panel--1">
      <span class="unfold-footer__fold" aria-hidden="true">01 / 03</span>
      <div class="unfold-footer__cta">
        <p class="unfold-footer__eyebrow">Brand Home Services · Springfield</p>
        <h2 class="unfold-footer__title">Let's get it <span class="unfold-footer__marker">sorted.</span></h2>
        <a class="unfold-footer__btn" href="#book">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
      </div>
      <div class="unfold-footer__reach">
        <a class="unfold-footer__phone" href="tel:+15555550123">(555) 555-0123</a>
        <a class="unfold-footer__mail" href="mailto:hello@example.com">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z" /><path d="m3.5 6.5 8.5 6.5 8.5-6.5" /></svg>
          hello@example.com
        </a>
        <dl class="unfold-footer__hours">
          <div><dt>Mon – Fri</dt><dd>7am – 7pm</dd></div>
          <div><dt>Saturday</dt><dd>8am – 4pm</dd></div>
          <div><dt>Sunday</dt><dd>Emergencies</dd></div>
        </dl>
      </div>
      <span class="unfold-footer__shade" aria-hidden="true"></span>
    </div>

    <!-- Panel 2: link columns and the service-area map -->
    <div class="unfold-footer__panel unfold-footer__panel--2">
      <span class="unfold-footer__fold" aria-hidden="true">02 / 03</span>
      <nav class="unfold-footer__nav" aria-label="Footer">
        <div>
          <h3 class="unfold-footer__heading">Services</h3>
          <ul class="unfold-footer__links" role="list">
            <li><a href="#plumbing">Plumbing</a></li>
            <li><a href="#electrical">Electrical</a></li>
            <li><a href="#heating">Heating</a></li>
            <li><a href="#roofing">Roofing</a></li>
          </ul>
        </div>
        <div>
          <h3 class="unfold-footer__heading">Company</h3>
          <ul class="unfold-footer__links" role="list">
            <li><a href="#about">About</a></li>
            <li><a href="#reviews">Reviews</a></li>
            <li><a href="#careers">Careers</a></li>
            <li><a href="#journal">Journal</a></li>
          </ul>
        </div>
        <div>
          <h3 class="unfold-footer__heading">Areas</h3>
          <ul class="unfold-footer__links" role="list">
            <li><a href="#springfield">Springfield</a></li>
            <li><a href="#westlake">Westlake</a></li>
            <li><a href="#northside">Northside</a></li>
            <li><a href="#riverside">Riverside</a></li>
          </ul>
        </div>
      </nav>
      <div class="unfold-footer__map" aria-hidden="true">
        <svg viewBox="0 0 280 168" width="280" height="168" focusable="false">
          <ellipse class="unfold-footer__zone" cx="62" cy="58" rx="50" ry="34" />
          <ellipse class="unfold-footer__zone unfold-footer__zone--alt" cx="190" cy="40" rx="58" ry="30" />
          <ellipse class="unfold-footer__zone" cx="214" cy="128" rx="54" ry="30" />
          <path class="unfold-footer__river" d="M-6 142C34 136 60 112 100 118S160 150 198 138 250 98 290 102" />
          <path class="unfold-footer__road" d="M0 84h280M140 0v168" />
          <circle class="unfold-footer__ring" cx="140" cy="84" r="15" />
          <circle class="unfold-footer__pin" cx="140" cy="84" r="5" />
          <text x="62" y="61" text-anchor="middle">WESTLAKE</text>
          <text x="194" y="43" text-anchor="middle">NORTHSIDE</text>
          <text x="216" y="131" text-anchor="middle">RIVERSIDE</text>
          <text x="148" y="104">SPRINGFIELD HQ</text>
        </svg>
        <p class="unfold-footer__map-caption"><span>Service area</span><span>20 mi radius</span></p>
      </div>
      <span class="unfold-footer__shade" aria-hidden="true"></span>
    </div>

    <!-- Panel 3: wordmark, socials and legal -->
    <div class="unfold-footer__panel unfold-footer__panel--3">
      <span class="unfold-footer__fold" aria-hidden="true">03 / 03</span>
      <div class="unfold-footer__base">
        <p class="unfold-footer__wordmark" aria-hidden="true">Brand</p>
        <ul class="unfold-footer__social" role="list">
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
      <div class="unfold-footer__legal">
        <p>© 2026 Brand Home Services · Lic. #CSL-104233</p>
        <ul class="unfold-footer__legal-links" role="list">
          <li><a href="#privacy">Privacy</a></li>
          <li><a href="#terms">Terms</a></li>
          <li><a href="#accessibility">Accessibility</a></li>
        </ul>
      </div>
      <span class="unfold-footer__shade" aria-hidden="true"></span>
    </div>
  </div>
</footer>
```

## CSS

```css
/* Footer: a deep "table" continuing the section above; the paper hangs from its top edge */
.unfold-footer {
  --unfold-footer-paper: color-mix(in srgb, var(--surface-muted) 90%, var(--accent)); /* warm cream */
  --unfold-footer-ink: var(--text-main);
  --unfold-footer-muted: color-mix(in srgb, var(--text-muted) 75%, var(--text-main));
  --unfold-footer-line: color-mix(in srgb, var(--text-main) 14%, transparent);
  --unfold-footer-grid: color-mix(in srgb, var(--text-main) 6%, transparent);
  padding: 0 var(--gutter) var(--gutter);
  background: var(--surface-deep); color: var(--unfold-footer-ink); font-family: var(--font-sans);
}
.unfold-footer svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.unfold-footer__sheet { max-width: var(--container-max); margin-inline: auto; }

/* Panels: paper with grain, a crease at every fold, and a shade that tracks the angle */
.unfold-footer__panel {
  position: relative; isolation: isolate; backface-visibility: hidden;
  padding: clamp(2rem, 4vw, 3rem) clamp(1.25rem, 4vw, 3rem);
  background: var(--unfold-footer-paper);
}
.unfold-footer__panel::before { /* paper grain: ink through a noise mask */
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; pointer-events: none;
  background: var(--unfold-footer-ink); opacity: 0.07;
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  -webkit-mask-size: 160px; mask-size: 160px;
}
.unfold-footer__panel::after { /* the paper never lies perfectly flat at a fold */
  content: ""; position: absolute; inset: 0 0 auto; height: 2.5rem; z-index: -1; pointer-events: none;
  background: linear-gradient(to bottom, color-mix(in srgb, var(--text-main) 6%, transparent), transparent);
}
.unfold-footer__panel + .unfold-footer__panel {
  box-shadow: inset 0 1px 0 var(--unfold-footer-line), inset 0 2px 0 color-mix(in srgb, var(--surface-light) 70%, transparent);
}
.unfold-footer__panel--2 { background: color-mix(in srgb, var(--unfold-footer-paper) 97%, var(--text-main)); }
.unfold-footer__panel--3 { border-radius: 0 0 var(--radius-lg) var(--radius-lg); }
.unfold-footer__fold {
  position: absolute; top: 0.875rem; right: clamp(1rem, 3vw, 1.5rem);
  color: var(--unfold-footer-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.1em;
}
.unfold-footer__shade { /* bright crease + light falling away toward the far edge */
  position: absolute; inset: 0; z-index: 2; border-radius: inherit; pointer-events: none;
  background:
    linear-gradient(to bottom, color-mix(in srgb, var(--surface-light) 60%, transparent), transparent 16%),
    linear-gradient(to bottom, color-mix(in srgb, var(--surface-deep) 10%, transparent), color-mix(in srgb, var(--surface-deep) 62%, transparent));
  opacity: calc(1 - var(--unfold-footer-q, 1));
}

/* JS: each panel hinges on its top edge; --unfold-footer-q is 0 folded, 1 flat (1 without JS) */
.unfold-footer--js .unfold-footer__panel {
  transform-origin: 50% 0;
  transform: perspective(75rem) rotateX(calc((1 - var(--unfold-footer-q, 1)) * -90deg));
}
/* A panel holding keyboard focus always lies flat */
.unfold-footer--js .unfold-footer__panel:focus-within { transform: none; }
.unfold-footer__panel:focus-within .unfold-footer__shade { opacity: 0; }

/* Panel 1: CTA and contact */
.unfold-footer__panel--1 { display: grid; gap: 2rem; }
.unfold-footer__eyebrow { margin: 0; color: var(--unfold-footer-muted); font: 500 0.75rem/1.5 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.unfold-footer__title { margin: 0.75rem 0 0; font: 600 clamp(2.25rem, 1.4rem + 3.6vw, 4rem)/1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.unfold-footer__marker { /* highlighter stroke, printed on the paper */
  padding-inline: 0.04em;
  background: linear-gradient(transparent 58%, color-mix(in srgb, var(--accent) 45%, transparent) 58% 90%, transparent 90%);
}
.unfold-footer__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; margin-top: 1.5rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: linear-gradient(180deg, color-mix(in srgb, var(--primary) 18%, var(--surface-deep)), var(--surface-deep));
  color: var(--text-inverse); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: var(--highlight-inverse), 0 10px 24px -12px color-mix(in srgb, var(--surface-deep) 80%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.unfold-footer__btn:hover { transform: translateY(-2px); box-shadow: var(--highlight-inverse), 0 16px 32px -14px color-mix(in srgb, var(--surface-deep) 90%, transparent); }
.unfold-footer__btn:active { transform: scale(0.97); }
.unfold-footer__btn svg { transition: transform var(--dur-3) var(--ease-spring); }
.unfold-footer__btn:hover svg { transform: translateX(3px); }
.unfold-footer__reach { display: grid; justify-items: start; gap: 0.25rem; min-width: 0; }
.unfold-footer__phone {
  display: inline-flex; align-items: center; min-height: 2.75rem; color: var(--unfold-footer-ink); text-decoration: none;
  font: 600 clamp(1.75rem, 1.3rem + 1.8vw, 2.5rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); transition: color var(--dur-2);
}
.unfold-footer__mail {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.25rem; color: var(--unfold-footer-ink); font-size: 1rem; overflow-wrap: anywhere;
  text-decoration: underline; text-decoration-color: var(--unfold-footer-line); text-underline-offset: 0.25em; transition: color var(--dur-2), text-decoration-color var(--dur-2);
}
.unfold-footer__phone:hover, .unfold-footer__mail:hover { color: var(--primary-hover); text-decoration-color: currentColor; }
.unfold-footer__hours { display: grid; gap: 0.375rem; width: 100%; max-width: 22rem; margin: 0.75rem 0 0; padding-top: 1rem; border-top: 1px dashed var(--unfold-footer-line); font-size: 0.875rem; }
.unfold-footer__hours div { display: flex; align-items: baseline; gap: 0.5rem; }
.unfold-footer__hours dt { flex: 1; display: flex; align-items: baseline; gap: 0.5rem; color: var(--unfold-footer-muted); }
.unfold-footer__hours dt::after { content: ""; flex: 1; border-bottom: 1px dotted var(--unfold-footer-line); } /* timetable leader */
.unfold-footer__hours dd { margin: 0; font: 500 0.8125rem/1.5 var(--font-mono); }

/* Panel 2: link columns and the map */
.unfold-footer__panel--2 { display: grid; gap: 2rem; }
.unfold-footer__nav { display: grid; grid-template-columns: repeat(auto-fit, minmax(5.5rem, 1fr)); gap: 1.5rem 1rem; }
.unfold-footer__heading { margin: 0 0 0.75rem; color: var(--unfold-footer-muted); font: 500 0.6875rem/1.4 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.unfold-footer__links { display: grid; margin: 0; padding: 0; list-style: none; }
.unfold-footer__links a {
  display: inline-flex; align-items: center; min-height: 2rem; color: var(--unfold-footer-ink); font-size: 0.875rem; text-decoration: none;
  transition: color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.unfold-footer__links a:hover { color: var(--primary-hover); transform: translateX(3px); }
.unfold-footer__map {
  padding: 0.75rem; border-radius: var(--radius-lg);
  background-image: linear-gradient(var(--unfold-footer-grid) 1px, transparent 1px), linear-gradient(90deg, var(--unfold-footer-grid) 1px, transparent 1px);
  background-size: 1.25rem 1.25rem; box-shadow: inset 0 0 0 1px var(--unfold-footer-line);
}
.unfold-footer__map svg { display: block; width: 100%; height: auto; }
.unfold-footer__zone { fill: color-mix(in srgb, var(--primary) 8%, transparent); stroke: color-mix(in srgb, var(--primary) 45%, transparent); stroke-width: 1; stroke-dasharray: 3 3; }
.unfold-footer__zone--alt { fill: color-mix(in srgb, var(--primary-2) 9%, transparent); stroke: color-mix(in srgb, var(--primary-2) 55%, transparent); }
.unfold-footer__river { stroke: color-mix(in srgb, var(--primary) 30%, var(--unfold-footer-paper)); stroke-width: 6; }
.unfold-footer__road { stroke: var(--unfold-footer-line); stroke-width: 1.5; }
.unfold-footer__ring { stroke: color-mix(in srgb, var(--accent) 75%, transparent); stroke-width: 1.5; }
.unfold-footer__pin { fill: var(--surface-deep); stroke: var(--unfold-footer-paper); stroke-width: 2; }
.unfold-footer__map text { fill: var(--unfold-footer-muted); stroke: none; font: 500 8px var(--font-mono); letter-spacing: 0.12em; }
.unfold-footer__map-caption { display: flex; justify-content: space-between; gap: 1rem; margin: 0.5rem 0 0; color: var(--unfold-footer-muted); font: 500 0.6875rem/1.4 var(--font-mono); letter-spacing: 0.06em; }

/* Panel 3: wordmark, socials, legal */
.unfold-footer__panel--3 { display: grid; gap: 1.5rem; }
.unfold-footer__base { display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 1rem; }
.unfold-footer__wordmark { /* debossed into the paper */
  margin: 0; color: var(--unfold-footer-ink); font: 700 clamp(3.5rem, 2rem + 7vw, 7.5rem)/0.8 var(--font-display); letter-spacing: -0.06em;
  text-shadow: 0 1px 0 color-mix(in srgb, var(--surface-light) 85%, transparent), 0 -1px 0 color-mix(in srgb, var(--text-main) 14%, transparent);
}
.unfold-footer__social { display: flex; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.unfold-footer__social a {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: 50%;
  color: var(--unfold-footer-ink); box-shadow: inset 0 0 0 1px var(--unfold-footer-line);
  transition: background-color var(--dur-2), color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.unfold-footer__social a:hover { background: var(--surface-deep); color: var(--text-inverse); transform: translateY(-2px); }
.unfold-footer__legal {
  display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0.5rem 1.5rem;
  padding-top: 1rem; border-top: 1px solid var(--unfold-footer-line); color: var(--unfold-footer-muted); font: 0.75rem/1.5 var(--font-mono);
}
.unfold-footer__legal p { margin: 0; }
.unfold-footer__legal-links { display: flex; flex-wrap: wrap; gap: 0 1.25rem; margin: 0; padding: 0; list-style: none; }
.unfold-footer__legal-links a { display: inline-flex; align-items: center; min-height: 1.5rem; color: var(--unfold-footer-muted); text-decoration: none; transition: color var(--dur-2); }
.unfold-footer__legal-links a:hover { color: var(--unfold-footer-ink); text-decoration: underline; }

/* Focus on paper */
.unfold-footer :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Demo: the deep section the paper hangs from (glows kept away from its bottom edge so the seam is invisible) */
.unfold-footer-demo {
  position: relative; display: grid; align-items: center; min-height: 85vh; min-height: 85svh;
  background:
    radial-gradient(55% 45% at 85% 0%, color-mix(in srgb, var(--primary) 30%, transparent), transparent 70%),
    radial-gradient(40% 35% at 0% 35%, color-mix(in srgb, var(--primary-2) 16%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); font-family: var(--font-sans);
}
.unfold-footer-demo__inner { width: 100%; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 12vh, 7rem) var(--gutter); }
.unfold-footer-demo__eyebrow { margin: 0; color: color-mix(in srgb, var(--primary-2) 40%, var(--text-inverse)); font: 500 0.8125rem/1.4 var(--font-mono); letter-spacing: 0.04em; }
.unfold-footer-demo__title { max-width: 16ch; margin: 1rem 0 0; font: 600 clamp(2.5rem, 1.4rem + 4.5vw, 5rem)/1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.unfold-footer-demo__lead { max-width: 34rem; margin: 1.5rem 0 0; color: var(--text-inverse-muted); font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem); line-height: 1.6; }
.unfold-footer-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 2.5rem 0 0; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.unfold-footer-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: unfold-footer-nudge 1.4s var(--ease-in-out) 0.8s 3; }

@media (min-width: 48rem) {
  .unfold-footer__panel--1 { grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); align-items: end; gap: 3rem; }
  .unfold-footer__links a { font-size: 0.9375rem; }
}
@media (min-width: 64rem) {
  .unfold-footer__panel--2 { grid-template-columns: minmax(0, 1.5fr) minmax(16rem, 1fr); align-items: center; gap: 3rem; }
}
@media (prefers-reduced-motion: reduce) {
  .unfold-footer *, .unfold-footer *::before, .unfold-footer *::after { animation: none !important; }
  .unfold-footer-demo__hint svg { animation: none; }
}
@keyframes unfold-footer-nudge { 50% { transform: translateY(4px); } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

document.querySelectorAll('[data-unfold-footer]').forEach((footer) => {
  if (reduce) return; // reduced motion: the sheet stays flat
  const panels = [...footer.querySelectorAll('.unfold-footer__panel')];
  // Panels already on screen at load stay flat (nothing flashes) until they have left the viewport once
  const settled = panels.map((panel) => panel.getBoundingClientRect().top < innerHeight);
  let frame = 0;
  let near = false;
  footer.classList.add('unfold-footer--js');

  // A panel unfolds while its hinge rises into view and lies flat once 85% of its height is in.
  // Panel n + 1 hinges on panel n's bottom edge, so they always open in order, the last by the page end.
  const update = () => {
    frame = 0;
    panels.forEach((panel, i) => {
      const top = panel.getBoundingClientRect().top; // the hinge line itself never moves
      if (settled[i] && top >= innerHeight) settled[i] = false;
      const q = settled[i] ? 1 : Math.min(1, Math.max(0, (innerHeight - top) / (panel.offsetHeight * 0.85)));
      panel.style.setProperty('--unfold-footer-q', q.toFixed(4));
    });
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(update); };

  new IntersectionObserver(([entry]) => {
    near = entry.isIntersecting;
    queue();
  }, { rootMargin: '20% 0px' }).observe(footer);
  addEventListener('scroll', queue, { passive: true });
  addEventListener('resize', queue, { passive: true });
  update();

  // Keyboard: the focused panel lies flat (CSS), then the focused link is brought fully on screen
  footer.addEventListener('focusin', (e) => requestAnimationFrame(() => e.target.scrollIntoView({ block: 'nearest' })));
});
```

## Notes

- **Wiring:** place `<footer class="unfold-footer" data-unfold-footer>` directly after a deep section. Its own background is `--surface-deep`, so the paper hangs from one continuous surface; change both together. The paper is `.unfold-footer__sheet`, and each `.unfold-footer__panel` (with its `.unfold-footer__shade`) is one fold. Two to four panels of any height work. A footer taller than the viewport is fine, because each panel unfolds as its own hinge comes into view.
- **How it works:** JS writes `--unfold-footer-q` per panel (0 folded, 1 flat) from where its hinge sits in the viewport. A panel is flat once 85% of it has scrolled in. Every hinge is the previous panel's bottom edge, so the panels open strictly in order, and the last one is always flat by the end of the page. Panels already on screen at load start flat.
- **No JS or reduced motion:** the flat sheet, still with its creases and grain. Rotating large surfaces is exactly the motion reduced-motion users opt out of, so JS doesn't run at all.
- **Accessibility:** the folds are transforms only, so reading order and the accessibility tree never change, inside one `contentinfo` landmark. A panel that holds focus is forced flat, and the focused link is scrolled fully into view. The map, the fold numbers and the wordmark are `aria-hidden`; the areas exist as real links and the brand name is in the legal row.
- **Contrast on the cream paper** (`--surface-muted` mixed with 10% `--accent`): `--text-main` 12.8:1. The local muted ink is 5.5:1; plain `--text-muted` would only reach 4.2:1, so it's mixed darker. Link hover (`--primary-hover`) is 5.9:1 and the `--primary` focus ring 4.5:1.
- **Retheme:** paper, ink, line and grid colours are local variables on `.unfold-footer`. For the reverse look, set the paper to `--surface-deep`, the ink to `--text-inverse`, and the footer and the section above to a light surface.
