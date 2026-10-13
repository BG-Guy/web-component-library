# CTA Footer

A closing act for the page: a big call to action under a soft glow that follows the cursor, then the footer proper. It has columns with underlines that slide in, an inline newsletter form that shakes on error and confirms on success, and social icons that lift. A giant wordmark, cropped by the bottom edge, rises letter by letter as the footer scrolls into view. Depends on `tokens/variables.css`.

**Motion:** cursor-following glow · live dot pulse (3×) · CTA button shine · underline slide · icon lift · newsletter shake / success swap · staggered wordmark rise.

## HTML

```html
<footer class="cta-footer" data-cta-footer>
  <div class="cta-footer__glow" aria-hidden="true"></div>
  <div class="cta-footer__inner">
    <section class="cta-footer__cta" aria-labelledby="cta-footer-title">
      <p class="cta-footer__eyebrow"><span class="cta-footer__live" aria-hidden="true"></span>Booking today in Springfield</p>
      <h2 id="cta-footer-title" class="cta-footer__title">Ready when <span>you are.</span></h2>
      <p class="cta-footer__lead">Same-day appointments, upfront pricing and a 5-year guarantee on every job.</p>
      <div class="cta-footer__actions">
        <a class="cta-footer__btn cta-footer__btn--primary" href="#quote">
          Get a free quote
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="cta-footer__btn cta-footer__btn--ghost" href="tel:+15555550123">Call (555) 555-0123</a>
      </div>
    </section>

    <div class="cta-footer__grid">
      <div class="cta-footer__brand">
        <a class="cta-footer__logo" href="/"><span class="cta-footer__mark" aria-hidden="true"></span>Brand</a>
        <p>Licensed, insured and locally owned since 2009.</p>
        <form class="cta-footer__news" action="/subscribe" method="post" data-cta-footer-news>
          <label class="cta-footer__news-label" for="cta-footer-email">Seasonal maintenance tips, four times a year</label>
          <div class="cta-footer__news-row">
            <input id="cta-footer-email" name="email" type="email" autocomplete="email" placeholder="you@example.com" required aria-describedby="cta-footer-news-status">
            <button type="submit">Subscribe</button>
          </div>
          <p class="cta-footer__news-status" id="cta-footer-news-status" role="status"></p>
        </form>
      </div>

      <nav class="cta-footer__nav" aria-label="Footer">
        <div>
          <h3>Services</h3>
          <ul role="list">
            <li><a class="cta-footer__link" href="#repairs">Repairs</a></li>
            <li><a class="cta-footer__link" href="#installs">Installations</a></li>
            <li><a class="cta-footer__link" href="#plans">Maintenance plans</a></li>
            <li><a class="cta-footer__link" href="#emergency">24/7 emergency</a></li>
          </ul>
        </div>
        <div>
          <h3>Company</h3>
          <ul role="list">
            <li><a class="cta-footer__link" href="#about">About us</a></li>
            <li><a class="cta-footer__link" href="#reviews">Reviews</a></li>
            <li><a class="cta-footer__link" href="#careers">Careers</a></li>
            <li><a class="cta-footer__link" href="#areas">Service areas</a></li>
          </ul>
        </div>
        <div>
          <h3>Contact</h3>
          <ul role="list">
            <li><a class="cta-footer__link" href="tel:+15555550123">(555) 555-0123</a></li>
            <li><a class="cta-footer__link" href="mailto:hello@example.com">hello@example.com</a></li>
            <li>123 Main St, Springfield</li>
            <li>Mon–Sat, 7am–7pm</li>
          </ul>
        </div>
      </nav>
    </div>

    <div class="cta-footer__bottom">
      <p>© 2026 Brand. All rights reserved.</p>
      <ul class="cta-footer__legal" role="list">
        <li><a class="cta-footer__link" href="/privacy">Privacy</a></li>
        <li><a class="cta-footer__link" href="/terms">Terms</a></li>
        <li><a class="cta-footer__link" href="/accessibility">Accessibility</a></li>
      </ul>
      <ul class="cta-footer__social" role="list">
        <li><a href="#" aria-label="Brand on Instagram"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M7 3h10a4 4 0 0 1 4 4v10a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V7a4 4 0 0 1 4-4zM12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM17.5 6.5h.01" /></svg></a></li>
        <li><a href="#" aria-label="Brand on Facebook"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M15 8h-2a2 2 0 0 0-2 2v11M8 13h6" /></svg></a></li>
        <li><a href="#" aria-label="Brand on YouTube"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M3 8a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v8a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3zM10 9l5 3-5 3z" /></svg></a></li>
      </ul>
    </div>
  </div>

  <p class="cta-footer__wordmark" aria-hidden="true"><span style="--i: 0">B</span><span style="--i: 1">r</span><span style="--i: 2">a</span><span style="--i: 3">n</span><span style="--i: 4">d</span></p>
</footer>
```

## CSS

```css
/* Shell: deep surface, a static aurora at the top plus a glow that follows the cursor */
.cta-footer { position: relative; isolation: isolate; overflow: hidden; background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans); }
.cta-footer::before {
  content: ""; position: absolute; inset: 0 0 auto; z-index: -1; height: 36rem; pointer-events: none;
  background:
    radial-gradient(50% 60% at 30% 0%, color-mix(in srgb, var(--primary) 35%, transparent), transparent 70%),
    radial-gradient(45% 55% at 75% 0%, color-mix(in srgb, var(--primary-2) 28%, transparent), transparent 70%);
}
.cta-footer__glow {
  position: absolute; inset: 0; z-index: -1; pointer-events: none; opacity: var(--cta-footer-glow, 0); transition: opacity var(--dur-5);
  background: radial-gradient(28rem circle at var(--cta-footer-mx, 50%) var(--cta-footer-my, 20%), color-mix(in srgb, var(--primary-2) 14%, transparent), transparent 65%);
}
.cta-footer__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(5rem, 11vw, 8rem) var(--gutter) 2rem; }
.cta-footer :is(a, button, input):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* CTA */
.cta-footer__cta { max-width: 44rem; margin: 0 auto; text-align: center; }
.cta-footer__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.375rem 0.875rem; border-radius: 999px; background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); color: var(--text-inverse-muted); font-size: 0.8125rem; font-weight: 500; }
.cta-footer__live { position: relative; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); }
.cta-footer__live::after { content: ""; position: absolute; inset: 0; border-radius: 50%; background: var(--success); animation: cta-footer-ping 1.6s var(--ease-out) 3; }
.cta-footer__title { margin: 1.5rem 0 0; font: 600 clamp(2.75rem, 1.4rem + 5.5vw, 5.5rem)/0.98 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.cta-footer__title span {
  background: linear-gradient(100deg, var(--text-inverse), color-mix(in srgb, var(--primary-2) 75%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.cta-footer__lead { max-width: 32rem; margin: 1.25rem auto 0; color: var(--text-inverse-muted); font-size: 1.125rem; line-height: 1.6; }
.cta-footer__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2.25rem; }
.cta-footer__btn {
  position: relative; display: inline-flex; align-items: center; gap: 0.5rem; height: 3.25rem; padding: 0 1.5rem; overflow: hidden;
  border-radius: 999px; font-size: 1rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3), background-color var(--dur-2);
}
.cta-footer__btn svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.cta-footer__btn:hover { transform: translateY(-2px); }
.cta-footer__btn:active { transform: scale(0.97); }
.cta-footer__btn--primary { background: var(--surface-light); color: var(--text-main); box-shadow: 0 16px 48px -14px color-mix(in srgb, var(--primary) 95%, transparent); }
.cta-footer__btn--primary:hover svg { transform: translateX(4px); }
.cta-footer__btn--primary::after {
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(110deg, transparent 35%, color-mix(in srgb, var(--primary) 18%, transparent) 50%, transparent 65%);
  transform: translateX(-110%); transition: transform var(--dur-5) var(--ease-out);
}
.cta-footer__btn--primary:hover::after { transform: translateX(110%); }
.cta-footer__btn--ghost { background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); }
.cta-footer__btn--ghost:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }

/* Footer grid */
.cta-footer__grid { display: grid; gap: 3rem; margin-top: clamp(5rem, 10vw, 7rem); padding-top: 3rem; border-top: 1px solid var(--border-inverse); }
@media (min-width: 900px) { .cta-footer__grid { grid-template-columns: 1fr 1.6fr; gap: 4rem; } }
.cta-footer__logo { display: inline-flex; align-items: center; gap: 0.625rem; color: var(--text-inverse); font: 650 1.25rem/1 var(--font-display); letter-spacing: -0.02em; text-decoration: none; }
.cta-footer__mark { position: relative; width: 1.75rem; height: 1.75rem; border-radius: 0.5rem; background: var(--gradient-brand); box-shadow: var(--highlight-inverse); }
.cta-footer__mark::after { content: ""; position: absolute; inset: 0.4375rem; border-radius: 50%; border: 2px solid var(--text-inverse); border-right-color: transparent; transform: rotate(-45deg); }
.cta-footer__brand > p { max-width: 20rem; margin: 1rem 0 0; color: var(--text-inverse-muted); line-height: 1.6; }

/* Newsletter: pill row; shakes on error, swaps to a success state */
.cta-footer__news { margin-top: 2rem; }
.cta-footer__news-label { display: block; margin-bottom: 0.625rem; font-size: 0.875rem; font-weight: 600; }
.cta-footer__news-row {
  display: flex; gap: 0.375rem; max-width: 24rem; padding: 0.3125rem; border-radius: 999px;
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); transition: box-shadow var(--dur-3);
}
.cta-footer__news-row:focus-within { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 70%, transparent), 0 0 0 4px color-mix(in srgb, var(--primary-2) 18%, transparent); }
.cta-footer__news-row input { flex: 1; min-width: 0; height: 2.5rem; padding: 0 0.875rem; border: 0; background: transparent; color: var(--text-inverse); font: 500 0.9375rem var(--font-sans); }
.cta-footer__news-row input::placeholder { color: var(--text-inverse-muted); }
.cta-footer__news-row input:focus-visible { outline: none; }
.cta-footer__news-row button {
  flex: none; height: 2.5rem; padding: 0 1.125rem; border: 0; border-radius: 999px; cursor: pointer;
  background: var(--surface-light); color: var(--text-main); font: 600 0.875rem var(--font-sans);
  transition: background-color var(--dur-3), color var(--dur-3), transform var(--dur-3) var(--ease-spring);
}
.cta-footer__news-row button:active { transform: scale(0.95); }
.cta-footer__news[data-state="error"] .cta-footer__news-row { box-shadow: inset 0 0 0 1px var(--danger); animation: cta-footer-shake 420ms var(--ease-out); }
.cta-footer__news[data-state="success"] .cta-footer__news-row button { background: var(--success); color: var(--surface-light); }
.cta-footer__news-status { min-height: 1.25rem; margin: 0.5rem 0 0 0.875rem; color: var(--text-inverse-muted); font-size: 0.8125rem; }

/* Link columns with sliding underlines */
.cta-footer__nav { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2rem; }
@media (min-width: 640px) { .cta-footer__nav { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
.cta-footer__nav h3 { margin: 0 0 1rem; color: var(--text-inverse); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; }
.cta-footer__nav ul, .cta-footer__legal, .cta-footer__social { margin: 0; padding: 0; list-style: none; }
.cta-footer__nav ul { display: grid; gap: 0.75rem; color: var(--text-inverse-muted); font-size: 0.9375rem; }
.cta-footer__link {
  color: var(--text-inverse-muted); text-decoration: none; overflow-wrap: anywhere;
  background: linear-gradient(currentColor, currentColor) 0 100% / 0 1px no-repeat;
  transition: color var(--dur-2), background-size var(--dur-3) var(--ease-out);
}
.cta-footer__link:hover, .cta-footer__link:focus-visible { color: var(--text-inverse); background-size: 100% 1px; }

/* Bottom bar */
.cta-footer__bottom { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1rem 2rem; margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--border-inverse); color: var(--text-inverse-muted); font-size: 0.875rem; }
.cta-footer__bottom > p { margin: 0; }
.cta-footer__legal { display: flex; flex-wrap: wrap; gap: 0.5rem 1.5rem; }
.cta-footer__social { display: flex; gap: 0.5rem; }
.cta-footer__social a {
  display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%;
  background: var(--glass-inverse); color: var(--text-inverse-muted); box-shadow: inset 0 0 0 1px var(--border-inverse);
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2), color var(--dur-2);
}
.cta-footer__social svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.cta-footer__social a:hover { transform: translateY(-3px); background: var(--primary); color: var(--text-inverse); }

/* Giant wordmark, cropped by the bottom edge; letters rise in */
.cta-footer__wordmark {
  display: flex; justify-content: center; height: 0.74em; margin: 2rem 0 0; overflow: hidden;
  font: 700 clamp(6rem, 1rem + 22vw, 20rem)/0.8 var(--font-display); letter-spacing: -0.06em; user-select: none;
}
.cta-footer__wordmark span {
  display: inline-block;
  background: linear-gradient(180deg, color-mix(in srgb, var(--text-inverse) 18%, transparent), transparent 85%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  transition: transform calc(var(--dur-5) * 1.4) var(--ease-out); transition-delay: calc(var(--i) * 70ms);
}
.cta-footer--js:not(.cta-footer--in) .cta-footer__wordmark span { transform: translateY(70%); }

@media (prefers-reduced-motion: reduce) {
  .cta-footer__live::after, .cta-footer__news[data-state="error"] .cta-footer__news-row { animation: none; }
}
@keyframes cta-footer-ping { to { transform: scale(2.8); opacity: 0; } }
@keyframes cta-footer-shake { 0%, 100% { transform: none; } 20% { transform: translateX(-6px); } 40% { transform: translateX(6px); } 60% { transform: translateX(-4px); } 80% { transform: translateX(3px); } }
```

## JS

```js
document.querySelectorAll('[data-cta-footer]').forEach((footer) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  footer.classList.add('cta-footer--js');

  // Wordmark letters rise once the bottom of the footer is in view
  const wordmark = footer.querySelector('.cta-footer__wordmark');
  const io = new IntersectionObserver(([entry]) => {
    if (!entry.isIntersecting) return;
    footer.classList.add('cta-footer--in');
    io.disconnect();
  }, { threshold: 0.2 });
  io.observe(wordmark);

  // Glow follows the cursor (mouse, motion allowed)
  let frame = 0;
  footer.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse' || reduce || frame) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      const r = footer.getBoundingClientRect();
      footer.style.setProperty('--cta-footer-mx', `${e.clientX - r.left}px`);
      footer.style.setProperty('--cta-footer-my', `${e.clientY - r.top}px`);
      footer.style.setProperty('--cta-footer-glow', '1');
    });
  });
  footer.addEventListener('pointerleave', () => footer.style.setProperty('--cta-footer-glow', '0'));

  // Newsletter: inline validation with a shake, then a success state
  const form = footer.querySelector('[data-cta-footer-news]');
  const input = form.querySelector('input');
  const button = form.querySelector('button');
  const status = form.querySelector('.cta-footer__news-status');
  form.noValidate = true;
  form.addEventListener('submit', (e) => {
    e.preventDefault(); // demo: post with fetch in production
    if (!input.checkValidity()) {
      delete form.dataset.state;
      void form.offsetWidth; // restart the shake
      form.dataset.state = 'error';
      input.setAttribute('aria-invalid', 'true');
      status.textContent = 'Enter a valid email address, like name@example.com.';
      input.focus();
      return;
    }
    input.removeAttribute('aria-invalid');
    form.dataset.state = 'success';
    button.textContent = 'Subscribed';
    status.textContent = 'You’re subscribed. The first tips arrive next season.';
  });
  input.addEventListener('input', () => {
    if (form.dataset.state !== 'error') return;
    delete form.dataset.state;
    input.removeAttribute('aria-invalid');
    status.textContent = '';
  });
});
```

## Notes

- Text contrast on `--surface-deep`: headings `--text-inverse` (17:1), body and links `--text-inverse-muted` (7:1). The wordmark is decorative (`aria-hidden`) and deliberately low-contrast.
- Without JS the wordmark is simply visible and the newsletter posts to `action` with native validation.
- `tel:` and `mailto:` links are real links; social links name the network and the brand in `aria-label`. The icons are generic; swap in real marks.
- The status line under the newsletter is a polite live region, so errors and success are announced. The input is tied to it with `aria-describedby`.
- Pairs with `aurora-hero.md`: the same deep surface and gradient light bookend the page.
