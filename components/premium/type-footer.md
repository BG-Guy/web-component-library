# Living Wordmark Footer

A deep footer that ends in an enormous "BRAND" wordmark, sized with container-query units to run edge to edge and bleed off the bottom. The letters are alive: as the cursor nears, each one swells from weight 400 to 800, lifts and tints toward the brand gradient, with a smooth falloff across its neighbours. On touch screens a single weight wave rolls across when the footer comes into view, and tapping a letter bounces it. Every letter's width is fixed at its weight-800 width, so neighbours never shift. Depends on `tokens/variables.css`.

**Motion:** pointer-proximity weight 400→800 + lift + gradient tint, eased per frame toward its target (rAF, ~90ms time constant, stops when settled) · light pool following the strongest letter · touch entry wave (1.5s, once) · tap bounce (760ms keyframes on `translate`) · button and link hovers (`--dur-2`/`--dur-3`, `--ease-spring`).

## HTML

```html
<section class="type-footer-demo" aria-labelledby="type-footer-demo-title">
  <div class="type-footer-demo__inner">
    <p class="type-footer-demo__eyebrow">Since 2009 · Springfield</p>
    <h2 id="type-footer-demo-title" class="type-footer-demo__title">Fixed properly, the first time.</h2>
    <p class="type-footer-demo__lead">Every visit starts with a written, fixed price and ends with a tidy floor. Scroll to the bottom and run your cursor along our name, or tap a letter.</p>
    <ul class="type-footer-demo__tags" role="list">
      <li>Plumbing</li>
      <li>Electrical</li>
      <li>Carpentry</li>
      <li>Painting</li>
    </ul>
    <p class="type-footer-demo__hint" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
      Scroll
    </p>
  </div>
</section>

<footer class="type-footer" data-type-footer>
  <div class="type-footer__inner">
    <div class="type-footer__top">
      <div>
        <p class="type-footer__eyebrow">Free estimates across Springfield</p>
        <h2 class="type-footer__title">Got a job that needs doing?</h2>
      </div>
      <div class="type-footer__actions">
        <a class="type-footer__btn type-footer__btn--primary" href="#estimate">
          Book a free estimate
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="type-footer__btn type-footer__btn--ghost" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          (555) 555-0123
        </a>
      </div>
    </div>

    <div class="type-footer__grid">
      <div class="type-footer__about">
        <p class="type-footer__brand">
          <span class="type-footer__logo" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M3 11.5 12 4l9 7.5" /><path d="M5.5 10v9.5h13V10" /><path d="M10 19.5v-5h4v5" /></svg>
          </span>
          Brand Home Services
        </p>
        <p class="type-footer__blurb">Licensed plumbers, electricians and carpenters on one schedule. Upfront prices, tidy work and a two-year guarantee.</p>
        <ul class="type-footer__contact" role="list">
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

      <nav class="type-footer__nav" aria-label="Footer">
        <div>
          <h3 class="type-footer__heading">Services</h3>
          <ul class="type-footer__links" role="list">
            <li><a href="#plumbing">Plumbing</a></li>
            <li><a href="#electrical">Electrical</a></li>
            <li><a href="#carpentry">Carpentry</a></li>
            <li><a href="#painting">Painting</a></li>
          </ul>
        </div>
        <div>
          <h3 class="type-footer__heading">Company</h3>
          <ul class="type-footer__links" role="list">
            <li><a href="#about">About</a></li>
            <li><a href="#reviews">Reviews</a></li>
            <li><a href="#careers">Careers</a></li>
            <li><a href="#journal">Journal</a></li>
          </ul>
        </div>
        <div>
          <h3 class="type-footer__heading">Areas</h3>
          <ul class="type-footer__links" role="list">
            <li><a href="#springfield">Springfield</a></li>
            <li><a href="#westlake">Westlake</a></li>
            <li><a href="#northside">Northside</a></li>
            <li><a href="#riverside">Riverside</a></li>
          </ul>
        </div>
      </nav>

      <form class="type-footer__news" action="#">
        <h3 class="type-footer__heading">The Brand letter</h3>
        <p class="type-footer__note">One email a season: what to check before winter, summer storms and the holidays.</p>
        <div class="type-footer__field">
          <label class="type-footer__label">
            <span class="type-footer__sr">Email address</span>
            <input class="type-footer__input" type="email" name="email" placeholder="you@example.com" autocomplete="email" required>
          </label>
          <button class="type-footer__submit" type="submit" aria-label="Subscribe">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </button>
        </div>
        <p class="type-footer__status" role="status"></p>
      </form>
    </div>

    <div class="type-footer__legal">
      <p>© 2026 Brand Home Services · Lic. #CSL-104233</p>
      <ul class="type-footer__legal-links" role="list">
        <li><a href="#privacy">Privacy</a></li>
        <li><a href="#terms">Terms</a></li>
        <li><a href="#accessibility">Accessibility</a></li>
        <li><a href="#sitemap">Sitemap</a></li>
      </ul>
      <ul class="type-footer__social" role="list">
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

  <!-- The living wordmark: one accessible name, decorative letters -->
  <div class="type-footer__mark" role="img" aria-label="Brand">
    <span class="type-footer__letter" data-letter="B" aria-hidden="true">B</span>
    <span class="type-footer__letter" data-letter="R" aria-hidden="true">R</span>
    <span class="type-footer__letter" data-letter="A" aria-hidden="true">A</span>
    <span class="type-footer__letter" data-letter="N" aria-hidden="true">N</span>
    <span class="type-footer__letter" data-letter="D" aria-hidden="true">D</span>
  </div>
</footer>
```

## CSS

```css
/* Footer: deep surface lit from below; the container the wordmark sizes against */
.type-footer {
  position: relative; overflow: clip; container-type: inline-size;
  color: var(--text-inverse); font-family: var(--font-sans);
  background:
    radial-gradient(60% 45% at 50% 100%, color-mix(in srgb, var(--primary) 24%, transparent), transparent 70%),
    radial-gradient(40% 35% at 0% 0%, color-mix(in srgb, var(--primary-2) 14%, transparent), transparent 70%),
    var(--surface-deep);
}
.type-footer svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.type-footer__inner {
  position: relative; display: grid; gap: clamp(2.5rem, 6vw, 4rem);
  max-width: var(--container-max); margin-inline: auto; padding: clamp(3.5rem, 9vw, 6.5rem) var(--gutter) 0;
}

/* CTA row */
.type-footer__top { display: grid; gap: 1.75rem; padding-bottom: clamp(2.5rem, 6vw, 4rem); border-bottom: 1px solid var(--border-inverse); }
.type-footer__eyebrow { margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1.5 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.type-footer__title { max-width: 16ch; margin: 0.75rem 0 0; font: 600 clamp(2.25rem, 1.3rem + 3.8vw, 4.25rem)/1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.type-footer__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; }
.type-footer__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out), background-color var(--dur-2);
}
.type-footer__btn:hover { transform: translateY(-2px); }
.type-footer__btn:active { transform: scale(0.97); }
.type-footer__btn svg { transition: transform var(--dur-3) var(--ease-spring); }
.type-footer__btn--primary { background: var(--surface-light); color: var(--text-main); box-shadow: var(--highlight), 0 12px 40px -12px color-mix(in srgb, var(--primary) 90%, transparent); }
.type-footer__btn--primary:hover { box-shadow: var(--highlight), 0 18px 48px -12px color-mix(in srgb, var(--primary-2) 90%, transparent); }
.type-footer__btn--primary:hover svg { transform: translateX(3px); }
.type-footer__btn--ghost { background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.type-footer__btn--ghost:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }

/* About, link columns, newsletter */
.type-footer__grid { display: grid; gap: 2.5rem; grid-template-areas: "about" "nav" "news"; }
.type-footer__about { grid-area: about; min-width: 0; }
.type-footer__nav { grid-area: nav; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.5rem 1rem; }
.type-footer__news { grid-area: news; min-width: 0; }
.type-footer__brand { display: flex; align-items: center; gap: 0.75rem; margin: 0; font: 600 1.0625rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.type-footer__logo { display: grid; place-items: center; width: 2.25rem; height: 2.25rem; border-radius: 0.625rem; background: var(--gradient-brand); box-shadow: var(--highlight-inverse), 0 8px 20px -8px color-mix(in srgb, var(--primary) 80%, transparent); }
.type-footer__blurb { max-width: 22rem; margin: 1rem 0 0; color: var(--text-inverse-muted); font-size: 0.9375rem; line-height: 1.6; }
.type-footer__contact { display: grid; gap: 0.125rem; margin: 1.25rem 0 0; padding: 0; list-style: none; }
.type-footer__contact a {
  display: inline-flex; align-items: center; gap: 0.625rem; min-height: 2.25rem; color: var(--text-inverse); font-size: 0.9375rem; text-decoration: none;
  overflow-wrap: anywhere; transition: color var(--dur-2);
}
.type-footer__contact svg { color: var(--text-inverse-muted); }
.type-footer__contact a:hover { color: color-mix(in srgb, var(--primary-2) 40%, var(--text-inverse)); }
.type-footer__heading { margin: 0 0 0.75rem; color: var(--text-inverse-muted); font: 500 0.6875rem/1.4 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.type-footer__links { display: grid; margin: 0; padding: 0; list-style: none; }
.type-footer__links a {
  display: inline-flex; align-items: center; min-height: 2rem; color: var(--text-inverse); font-size: 0.875rem; text-decoration: none;
  transition: color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.type-footer__links a:hover { color: color-mix(in srgb, var(--primary-2) 40%, var(--text-inverse)); transform: translateX(3px); }
.type-footer__note { max-width: 24rem; margin: 0 0 1rem; color: var(--text-inverse-muted); font-size: 0.875rem; line-height: 1.55; }
.type-footer__field {
  display: flex; align-items: center; gap: 0.375rem; max-width: 24rem; padding: 0.3125rem; border-radius: var(--radius-full);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); transition: box-shadow var(--dur-2);
}
.type-footer__field:focus-within { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 60%, var(--text-inverse)), 0 0 0 4px color-mix(in srgb, var(--primary-2) 22%, transparent); }
.type-footer__label { flex: 1; min-width: 0; display: flex; }
.type-footer__input { flex: 1; min-width: 0; height: 2.75rem; padding: 0 0.875rem; border: 0; border-radius: var(--radius-full); background: transparent; color: var(--text-inverse); font: inherit; font-size: 0.9375rem; }
.type-footer__input::placeholder { color: var(--text-inverse-muted); opacity: 1; }
.type-footer__submit {
  flex: none; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--gradient-brand); color: var(--text-inverse); box-shadow: var(--highlight-inverse);
  transition: transform var(--dur-3) var(--ease-spring);
}
.type-footer__submit:hover { transform: rotate(-8deg) scale(1.06); }
.type-footer__submit:active { transform: scale(0.92); }
.type-footer__status { min-height: 1.25rem; margin: 0.625rem 0 0; color: color-mix(in srgb, var(--primary-2) 40%, var(--text-inverse)); font-size: 0.8125rem; }
.type-footer__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* Legal row */
.type-footer__legal {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.5rem;
  padding-top: 1.25rem; border-top: 1px solid var(--border-inverse); color: var(--text-inverse-muted); font: 0.75rem/1.5 var(--font-mono);
}
.type-footer__legal p { margin: 0 auto 0 0; }
.type-footer__legal-links { display: flex; flex-wrap: wrap; gap: 0 1.25rem; margin: 0; padding: 0; list-style: none; }
.type-footer__legal-links a { display: inline-flex; align-items: center; min-height: 1.5rem; color: var(--text-inverse-muted); text-decoration: none; transition: color var(--dur-2); }
.type-footer__legal-links a:hover { color: var(--text-inverse); }
.type-footer__social { display: flex; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.type-footer__social a {
  display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%;
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); color: var(--text-inverse-muted);
  transition: color var(--dur-2), background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.type-footer__social a:hover { color: var(--text-inverse); background: color-mix(in srgb, var(--text-inverse) 10%, transparent); transform: translateY(-2px); }
.type-footer :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.type-footer__input:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }

/* The wordmark: edge to edge (100cqi split across the measured letter widths), bleeding off the bottom */
.type-footer__mark {
  position: relative; display: flex; justify-content: center; margin: clamp(1.5rem, 4vw, 3rem) 0 -0.26em;
  font-family: var(--font-display); font-weight: 400; line-height: 0.74; white-space: nowrap;
  font-size: calc(100vw / var(--type-footer-sum, 3.9));
  font-size: calc(100cqi / var(--type-footer-sum, 3.9));
  color: color-mix(in srgb, var(--text-inverse) 16%, var(--surface-deep));
  cursor: default; user-select: none; -webkit-user-select: none; -webkit-tap-highlight-color: transparent;
  -webkit-mask-image: linear-gradient(to bottom, black 30%, transparent);
  mask-image: linear-gradient(to bottom, black 30%, transparent);
}
.type-footer__mark::before { /* light pooling under the most excited letter */
  content: ""; position: absolute; left: 0; top: -0.35em; width: 1.7em; height: 1.5em; pointer-events: none;
  translate: calc(var(--type-footer-gx, 0) * 1em - 50%) 0;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--primary-2) 30%, transparent), transparent);
  opacity: var(--type-footer-glow, 0);
}
.type-footer__letter { position: relative; flex: none; text-align: center; }
/* JS: fixed widths; one variable per letter (--type-footer-f, 0–1) drives weight, lift and tint */
.type-footer--js .type-footer__letter {
  width: calc(var(--type-footer-w, 0.7) * 1em);
  font-weight: calc(400 + var(--type-footer-f, 0) * 400);
  transform: translateY(calc(var(--type-footer-f, 0) * -0.09em));
}
.type-footer--js .type-footer__letter::after { /* the gradient runs across the whole word; each letter shows its slice */
  content: attr(data-letter); position: absolute; inset: 0;
  background: linear-gradient(90deg, color-mix(in srgb, var(--primary) 60%, var(--text-inverse)), color-mix(in srgb, var(--primary-2) 70%, var(--text-inverse)));
  background-size: calc(var(--type-footer-sum, 3.9) * 1em) 100%;
  background-position: calc(var(--type-footer-x, 0) * -1em) 0;
  -webkit-background-clip: text; background-clip: text; color: transparent;
  opacity: var(--type-footer-f, 0);
}
.type-footer__mark.is-measuring .type-footer__letter { width: auto; font-weight: 800; transform: none; }
.type-footer__letter.is-bounce { animation: type-footer-bounce 760ms var(--ease-out); }

/* Demo page section above the footer */
.type-footer-demo {
  position: relative; display: grid; align-items: center; min-height: 85vh; min-height: 85svh;
  background:
    radial-gradient(50% 60% at 100% 100%, color-mix(in srgb, var(--primary-2) 10%, transparent), transparent 70%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
.type-footer-demo__inner { width: 100%; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 12vh, 7rem) var(--gutter); }
.type-footer-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.8125rem/1.4 var(--font-mono); letter-spacing: 0.04em; }
.type-footer-demo__title { max-width: 15ch; margin: 1rem 0 0; font: 600 clamp(2.5rem, 1.4rem + 4.5vw, 5rem)/1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.type-footer-demo__lead { max-width: 34rem; margin: 1.5rem 0 0; color: var(--text-muted); font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem); line-height: 1.6; }
.type-footer-demo__tags { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 2rem 0 0; padding: 0; list-style: none; }
.type-footer-demo__tags li { padding: 0.5rem 0.875rem; border-radius: var(--radius-full); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm); font-size: 0.8125rem; font-weight: 500; }
.type-footer-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 2.5rem 0 0; color: var(--text-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.type-footer-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: type-footer-nudge 1.4s var(--ease-in-out) 0.8s 3; }

@media (min-width: 48rem) {
  .type-footer__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); grid-template-areas: "about news" "nav nav"; gap: 2.5rem 3rem; }
  .type-footer__links a { font-size: 0.9375rem; }
}
@media (min-width: 64rem) {
  .type-footer__top { grid-template-columns: minmax(0, 1fr) auto; align-items: end; }
  .type-footer__grid { grid-template-columns: minmax(0, 1.25fr) minmax(0, 2.2fr) minmax(0, 1.35fr); grid-template-areas: "about nav news"; }
}
@media (prefers-reduced-motion: reduce) {
  .type-footer *, .type-footer *::before, .type-footer *::after { animation: none !important; }
  .type-footer-demo__hint svg { animation: none; }
}

@keyframes type-footer-bounce {
  0% { translate: 0 0; }
  22% { translate: 0 -0.14em; }
  50% { translate: 0 0.02em; }
  72% { translate: 0 -0.035em; }
  100% { translate: 0 0; }
}
@keyframes type-footer-nudge { 50% { transform: translateY(4px); } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const touch = matchMedia('(hover: none)').matches;

document.querySelectorAll('[data-type-footer]').forEach((footer) => {
  // Newsletter: the browser validates the address, then we confirm in place
  footer.querySelectorAll('.type-footer__news').forEach((form) => form.addEventListener('submit', (e) => {
    e.preventDefault();
    form.querySelector('.type-footer__status').textContent = 'Thanks! Check your inbox to confirm.';
    form.reset();
  }));

  const mark = footer.querySelector('.type-footer__mark');
  const letters = [...mark.querySelectorAll('.type-footer__letter')];
  if (reduce || !letters.length) return; // reduced motion: the wordmark stays static

  const cur = letters.map(() => 0);
  const target = letters.map(() => 0);
  const kick = letters.map(() => 0);
  let centers = [];
  let sum = 3.9;
  let pointer = null;
  let wave = 0;
  let raf = 0;
  let last = 0;

  // Fix every letter at its weight-800 width (in em), so swelling never pushes a neighbour
  const measure = () => {
    mark.classList.add('is-measuring');
    const size = parseFloat(getComputedStyle(mark).fontSize);
    const widths = letters.map((l) => l.getBoundingClientRect().width / size - 0.01);
    mark.classList.remove('is-measuring');
    sum = 0;
    centers = widths.map((w, i) => {
      letters[i].style.setProperty('--type-footer-w', w.toFixed(4));
      letters[i].style.setProperty('--type-footer-x', sum.toFixed(4));
      sum += w;
      return sum - w / 2;
    });
    mark.style.setProperty('--type-footer-sum', sum.toFixed(4));
    footer.classList.add('type-footer--js');
  };

  // Pull of a point on each letter: smoothstep falloff over roughly a letter and a half
  const aim = (px, py) => {
    const r = mark.getBoundingClientRect();
    const em = r.width / sum;
    const line = r.top + em * 0.28; // middle of the visible caps
    const reach = Math.max(140, r.width * 0.2);
    letters.forEach((_, i) => {
      const t = Math.max(0, 1 - Math.hypot(px - r.left - centers[i] * em, (py ?? line) - line) / reach);
      target[i] = t * t * (3 - 2 * t);
    });
  };

  // One frame: follow the pointer (or the touch wave), ease each letter toward its goal, stop once settled
  const tick = (now) => {
    const dt = last ? Math.min(64, now - last) : 16;
    last = now;
    if (wave) {
      const t = Math.max(0, Math.min(1, (now - wave) / 1500));
      const r = mark.getBoundingClientRect();
      const s = t < 0.5 ? 2 * t * t : 1 - (2 - 2 * t) ** 2 / 2;
      aim(r.left - r.width * 0.15 + r.width * 1.3 * s, null);
      if (t === 1) { wave = 0; target.fill(0); }
    } else if (pointer) aim(pointer.x, pointer.y);

    const follow = 1 - Math.exp(-dt / 90);
    let busy = wave > 0;
    let glow = 0;
    let gx = 0;
    let total = 0;
    letters.forEach((l, i) => {
      kick[i] *= Math.exp(-dt / 380);
      const goal = Math.max(target[i], kick[i]);
      cur[i] += (goal - cur[i]) * follow;
      if (Math.abs(goal - cur[i]) > 0.002 || kick[i] > 0.01) busy = true;
      l.style.setProperty('--type-footer-f', cur[i].toFixed(3));
      glow = Math.max(glow, cur[i]);
      gx += cur[i] * centers[i];
      total += cur[i];
    });
    mark.style.setProperty('--type-footer-glow', glow.toFixed(3));
    if (total > 0.001) mark.style.setProperty('--type-footer-gx', (gx / total).toFixed(3));
    raf = busy ? requestAnimationFrame(tick) : 0;
    if (!busy) last = 0;
  };
  const wake = () => { if (!raf) raf = requestAnimationFrame(tick); };

  // Mouse: proximity (also re-aimed when the page scrolls under a still cursor)
  footer.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    pointer = { x: e.clientX, y: e.clientY };
    wake();
  }, { passive: true });
  footer.addEventListener('pointerleave', () => { pointer = null; target.fill(0); wake(); });
  addEventListener('scroll', () => { if (pointer) wake(); }, { passive: true });

  // Tap (or click) a letter: it swells and bounces
  mark.addEventListener('pointerdown', (e) => {
    const letter = e.target.closest('.type-footer__letter');
    if (!letter) return;
    kick[letters.indexOf(letter)] = 1;
    letter.classList.remove('is-bounce');
    void letter.offsetWidth; // restart the keyframes
    letter.classList.add('is-bounce');
    wake();
  });
  mark.addEventListener('animationend', (e) => e.target.classList.remove('is-bounce'));

  // Touch screens can't hover: one weight wave rolls across the first time the wordmark shows
  if (touch) {
    const seen = new IntersectionObserver(([entry]) => {
      if (!entry.isIntersecting) return;
      seen.disconnect();
      wave = performance.now();
      wake();
    }, { threshold: 0.35 });
    seen.observe(mark);
  }

  measure();
  document.fonts?.ready.then(measure);
  document.fonts?.addEventListener('loadingdone', measure);
});
```

## Notes

- **Wiring:** put `<footer class="type-footer" data-type-footer>` at the end of the page; it needs no wrapper. The footer is its own size container (`container-type: inline-size`), so the wordmark always spans the footer's width. To change the word, edit the letter spans (each `data-letter` must match its text) and the `aria-label`. Any length works because JS measures it.
- **Fonts:** the swell runs from weight 400 to 800, so it needs Geist's variable axis across that range. The library's standard link (`family=Geist:wght@400..800`) provides it. With static weights the browser snaps between them. JS measures widths at weight 800 on init, after `document.fonts.ready`, and again whenever more fonts finish loading.
- **Accessibility:** the wordmark is `role="img"` with `aria-label="Brand"`, and its letter spans are `aria-hidden`. The effect is pointer-only decoration with nothing interactive inside it. Logotypes are exempt from contrast (WCAG 1.4.3); every other piece of text is `--text-inverse` (about 18:1) or `--text-inverse-muted` (about 7:1) on `--surface-deep`, and the teal hover colour is about 11:1.
- **No JS or reduced motion:** a static weight-400 wordmark that fades into the bottom edge and fills about 85% of the width via the fallback ratio (override `--type-footer-sum` to tune it). Under reduced motion JS sets up the newsletter, then stops before any motion is wired.
- **Performance:** one rAF loop runs only while letters are settling or the touch wave is playing, and it stops once every letter reaches its target. Only five fixed-width spans change `font-weight`, so the re-layout stays contained.
- **Support:** container-query units fall back to `vw`. `calc()` in `font-weight`, the individual `translate` property and `background-clip: text` work in all current engines.
