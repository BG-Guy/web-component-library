# Footer Variants

Six alternatives to the standard footer in `components/footer.md`, from a one-column minimal footer to a mega footer. Depends on `tokens/variables.css`.

| #  | Pattern                                                                                      | JS        |
| -- | -------------------------------------------------------------------------------------------- | --------- |
| 1  | **Minimal centered footer**: light; logo, inline links, social icons and copyright, centered | none      |
| 2  | **Newsletter footer**: dark; email signup with inline validation, 3 link columns, legal bar  | ~25 lines |
| 3  | **Mega footer**: dark; brand column plus 5 link columns (1 → 2 → 3 → 6 columns), legal bar | none      |
| 4  | **CTA-topped footer**: quote panel straddling the top edge of a dark footer, then columns    | none      |
| 5  | **Accordion footer**: link groups as `<details>`, collapsed on phones, open from 768px       | ~12 lines |
| 6  | **Brand wordmark footer**: dark; oversized decorative wordmark, contact and social rows      | none      |

## 1. Minimal centered footer

Light footer with everything centered in one column: logo, a wrapping row of links, social icon links and a copyright line.
Rows wrap instead of changing layout, so it needs no breakpoints.

### HTML

```html
<footer class="footer-minimal">
  <div class="footer-minimal__inner">
    <a class="footer-minimal__logo" href="/">Brand</a>

    <nav aria-label="Footer">
      <ul class="footer-minimal__nav" role="list">
        <li><a class="footer-minimal__link" href="/services">Services</a></li>
        <li><a class="footer-minimal__link" href="/about">About</a></li>
        <li><a class="footer-minimal__link" href="/reviews">Reviews</a></li>
        <li><a class="footer-minimal__link" href="/contact">Contact</a></li>
        <li><a class="footer-minimal__link" href="/privacy">Privacy</a></li>
      </ul>
    </nav>

    <ul class="footer-minimal__social" role="list" aria-label="Social media">
      <li>
        <a class="footer-minimal__icon" href="https://social.example.com/brand" aria-label="Brand photos">
          <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M4 7h3l2-3h6l2 3h3v12H4z" /><circle cx="12" cy="13" r="3.5" /></svg>
        </a>
      </li>
      <li>
        <a class="footer-minimal__icon" href="https://video.example.com/brand" aria-label="Brand videos">
          <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9" /><path d="m10 8.5 5 3.5-5 3.5z" /></svg>
        </a>
      </li>
      <li>
        <a class="footer-minimal__icon" href="https://community.example.com/brand" aria-label="Brand community">
          <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22z" /></svg>
        </a>
      </li>
    </ul>

    <p class="footer-minimal__copy">© 2026 Brand · Springfield</p>
  </div>
</footer>
```

### CSS

```css
/* Light full-bleed band; one centered column */
.footer-minimal {
  border-top: 1px solid var(--border-subtle);
  background: var(--surface-muted); color: var(--text-muted);
  font-size: 0.9375rem; line-height: 1.6;
}
.footer-minimal__inner {
  display: flex; flex-direction: column; align-items: center; gap: var(--space-lg);
  max-width: var(--container-max); margin-inline: auto; padding: var(--space-2xl) var(--gutter);
  text-align: center;
}
.footer-minimal__logo {
  font-size: 1.25rem; font-weight: 700; color: var(--text-main);
  text-decoration: none; border-radius: var(--radius-sm);
}

/* Link row and icon row wrap onto extra lines on narrow screens */
.footer-minimal__nav,
.footer-minimal__social { display: flex; flex-wrap: wrap; justify-content: center; margin: 0; padding: 0; list-style: none; }
.footer-minimal__nav { gap: 0 var(--space-lg); }
.footer-minimal__link {
  display: inline-block; padding-block: var(--space-xs); border-radius: var(--radius-sm);
  color: var(--text-main); text-decoration: none; transition: color var(--transition-fast);
}
.footer-minimal__link:hover { color: var(--primary); text-decoration: underline; }

/* 44px round icon links */
.footer-minimal__social { gap: var(--space-sm); }
.footer-minimal__icon {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem;
  border: 1px solid var(--border-subtle); border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main);
  transition: color var(--transition-fast), border-color var(--transition-fast);
}
.footer-minimal__icon:hover { border-color: var(--primary); color: var(--primary); }
.footer-minimal__icon svg {
  width: 1.25rem; height: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}

/* Light-surface focus ring */
.footer-minimal__logo:focus-visible,
.footer-minimal__link:focus-visible,
.footer-minimal__icon:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

.footer-minimal__copy { margin: 0; font-size: 0.875rem; }
```

### Notes

- Social icons and labels are generic placeholders. Swap in each network's own mark (keep `aria-hidden` on the SVG) and name the network in `aria-label`, e.g. "Brand on <Network>". The label is the link's only name.
- The icon list's `aria-label="Social media"` tells screen-reader users what the three links are before they reach them.
- Text links get `--space-xs` vertical padding, so each target is at least 24px tall. Icon links are 44px.
- `--text-muted` on `--surface-muted` stays above 4.5:1. Don't go lighter for the copyright line.

## 2. Newsletter footer

Dark footer led by an email signup (visible label, inline success/error message in a polite live region), plus 3 link columns and a legal bar.
The signup sits above the links until 1024px, then beside them. The script validates in the browser only; it doesn't send anything.

### HTML

```html
<footer class="footer-newsletter">
  <div class="footer-newsletter__inner footer-newsletter__main">
    <div class="footer-newsletter__signup">
      <h2 class="footer-newsletter__title" id="footer-newsletter-title">Seasonal home tips</h2>
      <p class="footer-newsletter__lead">One short email a month: maintenance reminders and member offers. Unsubscribe anytime.</p>
      <form class="footer-newsletter__form" action="/subscribe" method="post" aria-labelledby="footer-newsletter-title">
        <label class="footer-newsletter__label" for="footer-newsletter-email">Email address</label>
        <div class="footer-newsletter__row">
          <input class="footer-newsletter__input" id="footer-newsletter-email" name="email" type="email"
                 autocomplete="email" required aria-describedby="footer-newsletter-msg">
          <button class="footer-newsletter__btn" type="submit">Subscribe</button>
        </div>
        <p class="footer-newsletter__msg" id="footer-newsletter-msg" role="status" aria-live="polite"></p>
      </form>
    </div>

    <nav class="footer-newsletter__cols" aria-label="Footer">
      <div>
        <h2 class="footer-newsletter__heading">Services</h2>
        <ul class="footer-newsletter__list" role="list">
          <li><a href="/plumbing">Plumbing</a></li>
          <li><a href="/electrical">Electrical</a></li>
          <li><a href="/hvac">Heating &amp; cooling</a></li>
          <li><a href="/roofing">Roofing</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-newsletter__heading">Company</h2>
        <ul class="footer-newsletter__list" role="list">
          <li><a href="/about">About us</a></li>
          <li><a href="/reviews">Reviews</a></li>
          <li><a href="/careers">Careers</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-newsletter__heading">Help</h2>
        <ul class="footer-newsletter__list" role="list">
          <li><a href="/faq">FAQ</a></li>
          <li><a href="/financing">Financing</a></li>
          <li><a href="/warranty">Warranty</a></li>
          <li><a href="/areas">Service areas</a></li>
        </ul>
      </div>
    </nav>
  </div>

  <div class="footer-newsletter__bottom">
    <div class="footer-newsletter__inner footer-newsletter__bar">
      <p class="footer-newsletter__copy">© 2026 Brand. All rights reserved.</p>
      <ul class="footer-newsletter__legal" role="list">
        <li><a href="/privacy">Privacy</a></li>
        <li><a href="/terms">Terms</a></li>
      </ul>
    </div>
  </div>
</footer>
```

### CSS

```css
/* Dark full-bleed footer with its own container */
.footer-newsletter {
  background: var(--surface-dark); color: var(--text-inverse-muted);
  font-size: 0.9375rem; line-height: 1.6;
}
.footer-newsletter__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.footer-newsletter__main { display: grid; gap: var(--space-2xl); padding-block: var(--space-2xl); }

/* Signup: input and button share a row; the button drops below, full width, when there's no room */
.footer-newsletter__signup { max-width: 32rem; }
.footer-newsletter__title { margin: 0; font-size: 1.25rem; line-height: 1.3; color: var(--text-inverse); }
.footer-newsletter__lead { margin: var(--space-xs) 0 var(--space-md); }
.footer-newsletter__label { display: block; margin-bottom: var(--space-xs); font-weight: 600; color: var(--text-inverse); }
.footer-newsletter__row { display: flex; flex-wrap: wrap; gap: var(--space-sm); }
.footer-newsletter__input {
  flex: 999 1 12rem; min-width: 0; min-height: 2.75rem; padding: 0 var(--space-md);
  border: 1px solid var(--text-muted); border-radius: var(--radius-md);
  background: var(--surface-light); color: var(--text-main); font: inherit; font-size: 1rem;
}
.footer-newsletter__input[aria-invalid="true"] { border-color: var(--danger); }
.footer-newsletter__btn {
  flex: 1 0 auto; min-height: 2.75rem; padding: 0 var(--space-lg);
  border: 0; border-radius: var(--radius-md); background: var(--primary); color: var(--text-inverse);
  font: inherit; font-weight: 600; cursor: pointer; transition: background-color var(--transition-fast);
}
.footer-newsletter__btn:hover { background: var(--primary-hover); }

/* Status text stays --text-inverse for contrast; a colored bar marks the state */
.footer-newsletter__msg { margin: var(--space-sm) 0 0; font-size: 0.875rem; color: var(--text-inverse); }
.footer-newsletter__msg--error,
.footer-newsletter__msg--success { padding-left: var(--space-sm); border-left: 3px solid var(--danger); }
.footer-newsletter__msg--success { border-left-color: var(--success); }

/* Link columns: 2 per row on phones, 3 once they fit */
.footer-newsletter__cols {
  display: grid; gap: var(--space-xl) var(--space-lg);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 8rem), 1fr));
}
.footer-newsletter__heading {
  margin: 0 0 var(--space-sm);
  font-size: 0.875rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; color: var(--text-inverse);
}
.footer-newsletter__list,
.footer-newsletter__legal { margin: 0; padding: 0; list-style: none; }
.footer-newsletter__list { display: grid; gap: var(--space-sm); }

/* Links muted until hovered; light outline for focus on the dark surface */
.footer-newsletter a {
  color: inherit; text-decoration: none; border-radius: var(--radius-sm);
  transition: color var(--transition-fast);
}
.footer-newsletter a:hover { color: var(--text-inverse); text-decoration: underline; }
.footer-newsletter a:focus-visible,
.footer-newsletter__input:focus-visible,
.footer-newsletter__btn:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }

/* Legal bar: stacked, then split left/right from 768px */
.footer-newsletter__bottom { border-top: 1px solid color-mix(in srgb, var(--text-inverse) 15%, transparent); }
.footer-newsletter__bar {
  display: flex; flex-direction: column; gap: var(--space-sm);
  padding-block: var(--space-lg); font-size: 0.875rem;
}
.footer-newsletter__copy { margin: 0; }
.footer-newsletter__legal { display: flex; flex-wrap: wrap; column-gap: var(--space-lg); }
.footer-newsletter__legal a { display: inline-block; padding-block: var(--space-xs); }

@media (min-width: 768px) {
  .footer-newsletter__bar { flex-direction: row; align-items: center; justify-content: space-between; }
}
@media (min-width: 1024px) {
  .footer-newsletter__main { grid-template-columns: minmax(0, 2fr) minmax(0, 3fr); }
}
```

### JS

```js
// Client-side check only: the success branch is a stub until a backend or email provider is wired in
document.querySelectorAll('.footer-newsletter__form').forEach((form) => {
  const input = form.querySelector('.footer-newsletter__input');
  const msg = form.querySelector('.footer-newsletter__msg');
  form.noValidate = true; // the inline message replaces the browser's validation bubble

  const show = (state, text) => {
    msg.textContent = text;
    msg.classList.toggle('footer-newsletter__msg--error', state === 'error');
    msg.classList.toggle('footer-newsletter__msg--success', state === 'success');
  };

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!input.validity.valid) {
      input.setAttribute('aria-invalid', 'true');
      show('error', input.validity.valueMissing ? 'Enter your email address.'
        : 'Enter a valid email address, like name@example.com.');
      return;
    }
    input.removeAttribute('aria-invalid');
    show('success', 'Thanks! Check your inbox to confirm your subscription.');
    form.reset();
  });

  // Clear the error as soon as the visitor edits the field
  input.addEventListener('input', () => {
    if (input.hasAttribute('aria-invalid')) { input.removeAttribute('aria-invalid'); show('', ''); }
  });
});
```

### Notes

- **Needs a backend.** The script only validates and shows a message; nothing is sent. Post to your email provider or server (e.g. `fetch(form.action, { method: 'POST', body: new FormData(form) })`) and show the success message only after it responds. Without JS the form posts to `action` with native browser validation.
- The status `<p>` is a polite live region, present and empty from page load so screen readers catch updates. Never hide it with `display: none`. `aria-describedby` repeats the error when focus returns to the field.
- `--success` and `--danger` fall below 4.5:1 on `--surface-dark`, so the message text stays `--text-inverse`. The colored bar (3:1+) and the wording carry the state.
- `type="email"` accepts `name@host` without a dot. Add a `pattern` if that matters, and always validate again on the server.
- IDs (`footer-newsletter-*`) must be unique if a page repeats the form.

## 3. Mega footer

Dark footer with a brand column and 5 link columns in one `<nav>`. Links run 1 column on phones, 2 from 480px and 3 from 768px, with the brand above them.
From 1024px the brand joins them as the sixth column.

### HTML

```html
<footer class="footer-mega">
  <div class="footer-mega__inner footer-mega__main">
    <div class="footer-mega__brand">
      <a class="footer-mega__logo" href="/">Brand</a>
      <p class="footer-mega__about">Licensed, insured home services for Springfield and nearby towns since 2005.</p>
      <address class="footer-mega__contact">
        <a href="tel:+15555550123">(555) 555-0123</a>
        <a href="mailto:hello@example.com">hello@example.com</a>
      </address>
    </div>

    <nav class="footer-mega__nav" aria-label="Footer">
      <div>
        <h2 class="footer-mega__heading">Services</h2>
        <ul class="footer-mega__list" role="list">
          <li><a href="/plumbing">Plumbing</a></li>
          <li><a href="/electrical">Electrical</a></li>
          <li><a href="/hvac">Heating &amp; cooling</a></li>
          <li><a href="/roofing">Roofing</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-mega__heading">Service areas</h2>
        <ul class="footer-mega__list" role="list">
          <li><a href="/areas/downtown">Downtown</a></li>
          <li><a href="/areas/northside">Northside</a></li>
          <li><a href="/areas/westlake">Westlake</a></li>
          <li><a href="/areas/riverside">Riverside</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-mega__heading">Company</h2>
        <ul class="footer-mega__list" role="list">
          <li><a href="/about">About us</a></li>
          <li><a href="/reviews">Reviews</a></li>
          <li><a href="/careers">Careers</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-mega__heading">Resources</h2>
        <ul class="footer-mega__list" role="list">
          <li><a href="/blog">Blog</a></li>
          <li><a href="/guides">Home guides</a></li>
          <li><a href="/projects">Our projects</a></li>
          <li><a href="/financing">Financing</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-mega__heading">Support</h2>
        <ul class="footer-mega__list" role="list">
          <li><a href="/book">Book a visit</a></li>
          <li><a href="/emergency">Emergencies</a></li>
          <li><a href="/warranty">Warranty</a></li>
          <li><a href="/faq">FAQ</a></li>
        </ul>
      </div>
    </nav>
  </div>

  <div class="footer-mega__bottom">
    <div class="footer-mega__inner footer-mega__bar">
      <p class="footer-mega__copy">© 2026 Brand · License #000000</p>
      <ul class="footer-mega__legal" role="list">
        <li><a href="/privacy">Privacy</a></li>
        <li><a href="/terms">Terms</a></li>
        <li><a href="/accessibility">Accessibility</a></li>
        <li><a href="/sitemap">Sitemap</a></li>
      </ul>
    </div>
  </div>
</footer>
```

### CSS

```css
/* Dark full-bleed footer with its own container */
.footer-mega {
  background: var(--surface-dark); color: var(--text-inverse-muted);
  font-size: 0.9375rem; line-height: 1.6;
}
.footer-mega__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }

/* Brand above a nested link grid; the nested grid keeps all 5 columns in one <nav> */
.footer-mega__main { display: grid; gap: var(--space-2xl) var(--space-lg); padding-block: var(--space-2xl); }
.footer-mega__nav { display: grid; gap: var(--space-xl) var(--space-lg); }

/* Brand column */
.footer-mega__about { max-width: 22rem; margin: var(--space-sm) 0 var(--space-md); }
.footer-mega__contact { display: grid; justify-items: start; gap: var(--space-xs); font-style: normal; }

/* Column headings and lists */
.footer-mega__heading {
  margin: 0 0 var(--space-sm);
  font-size: 0.875rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; color: var(--text-inverse);
}
.footer-mega__list,
.footer-mega__legal { margin: 0; padding: 0; list-style: none; }
.footer-mega__list { display: grid; gap: var(--space-sm); }

/* Links muted until hovered; light outline for focus on the dark surface */
.footer-mega a {
  color: inherit; text-decoration: none; border-radius: var(--radius-sm); overflow-wrap: anywhere;
  transition: color var(--transition-fast);
}
.footer-mega a:hover { color: var(--text-inverse); text-decoration: underline; }
.footer-mega a:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }
/* Logo: the doubled class outranks `.footer-mega a` */
.footer-mega .footer-mega__logo { font-size: 1.25rem; font-weight: 700; color: var(--text-inverse); }

/* Legal bar: stacked, then split left/right from 768px */
.footer-mega__bottom { border-top: 1px solid color-mix(in srgb, var(--text-inverse) 15%, transparent); }
.footer-mega__bar {
  display: flex; flex-direction: column; gap: var(--space-sm);
  padding-block: var(--space-lg); font-size: 0.875rem;
}
.footer-mega__copy { margin: 0; }
.footer-mega__legal { display: flex; flex-wrap: wrap; column-gap: var(--space-lg); }
.footer-mega__legal a { display: inline-block; padding-block: var(--space-xs); }

/* Column count: 1 → 2 → 3 → brand + 5 */
@media (min-width: 480px) {
  .footer-mega__nav { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 768px) {
  .footer-mega__nav { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .footer-mega__bar { flex-direction: row; align-items: center; justify-content: space-between; }
}
@media (min-width: 1024px) {
  .footer-mega__main { grid-template-columns: minmax(0, 1.5fr) minmax(0, 5fr); }
  .footer-mega__nav { grid-template-columns: repeat(5, minmax(0, 1fr)); }
}
```

### Notes

- One `<nav aria-label="Footer">` holds all five columns, so screen-reader users get one landmark rather than five. That's why the links are a nested grid instead of sharing a grid with the brand.
- At 1024px each link column is about 125px wide. Keep labels to two or three short words, or start the 6-column layout at 1200px.
- The legal links get vertical padding to reach a 24px target at the smaller font size.
- The hairline uses `color-mix()` (all evergreen browsers since 2023). Older browsers drop the border and nothing else.
- **Tailwind (v4):** nav `grid gap-x-6 gap-y-8 min-[480px]:grid-cols-2 md:grid-cols-3 lg:grid-cols-5`, wrapper `grid gap-12 lg:grid-cols-[1.5fr_5fr]`.

## 4. CTA-topped footer

A `--primary` CTA panel (headline, text, two buttons) straddles the top edge of a dark footer, followed by 3 columns and a legal bar.
The overlap is a fixed length that the footer's top margin reserves, so a taller, wrapped panel at 320px grows into the footer and never covers the section above.

### HTML

```html
<footer class="footer-cta">
  <div class="footer-cta__inner">
    <div class="footer-cta__panel">
      <div>
        <h2 class="footer-cta__title">Ready for a free, no-pressure quote?</h2>
        <p class="footer-cta__text">Tell us about the job and get a fixed price within one business day.</p>
      </div>
      <div class="footer-cta__actions">
        <a class="footer-cta__btn footer-cta__btn--light" href="/quote">Get a free quote</a>
        <a class="footer-cta__btn footer-cta__btn--outline" href="tel:+15555550123">Call (555) 555-0123</a>
      </div>
    </div>

    <div class="footer-cta__grid">
      <div>
        <a class="footer-cta__logo" href="/">Brand</a>
        <p class="footer-cta__about">Licensed, insured and locally owned. Work we guarantee.</p>
      </div>
      <nav aria-labelledby="footer-cta-links">
        <h2 class="footer-cta__heading" id="footer-cta-links">Quick links</h2>
        <ul class="footer-cta__list" role="list">
          <li><a href="/services">Services</a></li>
          <li><a href="/reviews">Reviews</a></li>
          <li><a href="/about">About us</a></li>
          <li><a href="/faq">FAQ</a></li>
        </ul>
      </nav>
      <div>
        <h2 class="footer-cta__heading">Contact</h2>
        <address class="footer-cta__list">
          <a href="tel:+15555550123">(555) 555-0123</a>
          <a href="mailto:hello@example.com">hello@example.com</a>
          <span>123 Main St, Springfield</span>
        </address>
      </div>
    </div>
  </div>

  <div class="footer-cta__bottom">
    <div class="footer-cta__inner footer-cta__bar">
      <p class="footer-cta__copy">© 2026 Brand. All rights reserved.</p>
      <ul class="footer-cta__legal" role="list">
        <li><a href="/privacy">Privacy</a></li>
        <li><a href="/terms">Terms</a></li>
      </ul>
    </div>
  </div>
</footer>
```

### CSS

```css
/* Dark footer; its top margin reserves room for the part of the panel that sticks up */
.footer-cta {
  --footer-cta-overlap: var(--space-2xl);
  display: flow-root; /* stops the panel's negative margin collapsing into this margin */
  margin-top: var(--footer-cta-overlap);
  background: var(--surface-dark); color: var(--text-inverse-muted);
  font-size: 0.9375rem; line-height: 1.6;
}
.footer-cta__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }

/* CTA panel, pulled up by the overlap so it straddles the footer's top edge */
.footer-cta__panel {
  position: relative; z-index: 1;
  display: grid; gap: var(--space-lg);
  margin-top: calc(var(--footer-cta-overlap) * -1);
  padding: var(--space-xl) var(--space-lg);
  border-radius: var(--radius-lg); background: var(--primary); color: var(--text-inverse);
  box-shadow: var(--shadow-lg);
}
.footer-cta__title { margin: 0; font-size: clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem); line-height: 1.2; text-wrap: balance; }
.footer-cta__text { max-width: 36rem; margin: var(--space-sm) 0 0; font-size: 1.0625rem; }

/* Buttons share a row when they fit and stack full width when they don't */
.footer-cta__actions { display: flex; flex-wrap: wrap; gap: var(--space-sm); }
.footer-cta__btn {
  flex: 1 1 auto; display: inline-flex; align-items: center; justify-content: center;
  min-height: 2.75rem; padding: var(--space-sm) var(--space-lg);
  border: 2px solid var(--text-inverse); border-radius: var(--radius-md);
  font-weight: 600; text-align: center; text-decoration: none;
  transition: background-color var(--transition-fast), border-color var(--transition-fast), color var(--transition-fast);
}
.footer-cta__btn--light { border-color: var(--surface-light); background: var(--surface-light); color: var(--primary); }
.footer-cta__btn--light:hover { border-color: var(--surface-muted); background: var(--surface-muted); color: var(--primary-hover); }
.footer-cta__btn--outline { background: transparent; color: var(--text-inverse); }
.footer-cta__btn--outline:hover { background: var(--primary-hover); }

/* Footer columns: as many 13rem columns as fit (1 on phones, 3 from 768px) */
.footer-cta__grid {
  display: grid; gap: var(--space-xl); padding-block: var(--space-2xl);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 13rem), 1fr));
}
.footer-cta__logo { font-size: 1.25rem; font-weight: 700; color: var(--text-inverse); text-decoration: none; border-radius: var(--radius-sm); }
.footer-cta__about { max-width: 22rem; margin: var(--space-sm) 0 0; }
.footer-cta__heading {
  margin: 0 0 var(--space-sm);
  font-size: 0.875rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; color: var(--text-inverse);
}
.footer-cta__list,
.footer-cta__legal { margin: 0; padding: 0; list-style: none; }
.footer-cta__list { display: grid; justify-items: start; gap: var(--space-sm); font-style: normal; }

/* Text links muted until hovered; one light outline for every focusable on dark or --primary */
.footer-cta__list a,
.footer-cta__legal a {
  color: inherit; text-decoration: none; border-radius: var(--radius-sm); overflow-wrap: anywhere;
  transition: color var(--transition-fast);
}
.footer-cta__list a:hover,
.footer-cta__legal a:hover { color: var(--text-inverse); text-decoration: underline; }
.footer-cta a:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }

/* Legal bar */
.footer-cta__bottom { border-top: 1px solid color-mix(in srgb, var(--text-inverse) 15%, transparent); }
.footer-cta__bar { display: flex; flex-direction: column; gap: var(--space-sm); padding-block: var(--space-lg); font-size: 0.875rem; }
.footer-cta__copy { margin: 0; }
.footer-cta__legal { display: flex; flex-wrap: wrap; column-gap: var(--space-lg); }
.footer-cta__legal a { display: inline-block; padding-block: var(--space-xs); }

/* Wider screens: deeper overlap, copy beside stacked buttons, split legal bar */
@media (min-width: 768px) {
  .footer-cta { --footer-cta-overlap: calc(var(--space-2xl) * 1.5); }
  .footer-cta__panel { grid-template-columns: minmax(0, 1fr) auto; align-items: center; gap: var(--space-xl); padding: var(--space-2xl); }
  .footer-cta__actions { flex-direction: column; }
  .footer-cta__bar { flex-direction: row; align-items: center; justify-content: space-between; }
}
```

### Notes

- `display: flow-root` on the footer is load-bearing: without it, the footer's `margin-top` and the panel's negative margin collapse into zero and the overlap disappears.
- The reserved strip above the footer shows whatever is behind the footer. If the section above has its own background, end it with padding instead and let the page background fill the strip.
- Keep `--footer-cta-overlap` well under the panel's height. Raise it from 768px only, where the panel is shorter.
- Panel text is `--text-inverse` on `--primary` (about 5:1). The light button uses `--primary` text on white, and `--primary-hover` on hover to stay above 4.5:1.
- Don't stack this under `components/cta-sections.md`'s CTA band; use one or the other.

## 5. Accordion footer

Light footer whose link groups are native `<details>`: collapsed disclosure rows on phones, an always-open 3-column grid with plain headings from 768px.
Every group ships `open`, so without JS all links are visible. Phone and email sit outside the accordion so they're never hidden.

### HTML

```html
<footer class="footer-accordion">
  <div class="footer-accordion__inner footer-accordion__main">
    <div>
      <a class="footer-accordion__logo" href="/">Brand</a>
      <p class="footer-accordion__about">Repairs, installs and upgrades across Springfield. Same-week appointments.</p>
      <address class="footer-accordion__contact">
        <a href="tel:+15555550123">(555) 555-0123</a>
        <a href="mailto:hello@example.com">hello@example.com</a>
      </address>
    </div>

    <nav class="footer-accordion__nav" aria-label="Footer">
      <details class="footer-accordion__group" open>
        <summary class="footer-accordion__summary">
          <h2 class="footer-accordion__heading">
            Services
            <svg class="footer-accordion__chevron" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
          </h2>
        </summary>
        <ul class="footer-accordion__list" role="list">
          <li><a href="/plumbing">Plumbing</a></li>
          <li><a href="/electrical">Electrical</a></li>
          <li><a href="/hvac">Heating &amp; cooling</a></li>
        </ul>
      </details>
      <details class="footer-accordion__group" open>
        <summary class="footer-accordion__summary">
          <h2 class="footer-accordion__heading">
            Company
            <svg class="footer-accordion__chevron" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
          </h2>
        </summary>
        <ul class="footer-accordion__list" role="list">
          <li><a href="/about">About us</a></li>
          <li><a href="/reviews">Reviews</a></li>
          <li><a href="/careers">Careers</a></li>
        </ul>
      </details>
      <details class="footer-accordion__group" open>
        <summary class="footer-accordion__summary">
          <h2 class="footer-accordion__heading">
            Help
            <svg class="footer-accordion__chevron" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
          </h2>
        </summary>
        <ul class="footer-accordion__list" role="list">
          <li><a href="/faq">FAQ</a></li>
          <li><a href="/financing">Financing</a></li>
          <li><a href="/warranty">Warranty</a></li>
        </ul>
      </details>
    </nav>
  </div>

  <div class="footer-accordion__bottom">
    <div class="footer-accordion__inner footer-accordion__bar">
      <p class="footer-accordion__copy">© 2026 Brand. All rights reserved.</p>
      <ul class="footer-accordion__legal" role="list">
        <li><a href="/privacy">Privacy</a></li>
        <li><a href="/terms">Terms</a></li>
      </ul>
    </div>
  </div>
</footer>
```

### CSS

```css
/* Light full-bleed footer with its own container */
.footer-accordion {
  border-top: 1px solid var(--border-subtle);
  background: var(--surface-muted); color: var(--text-muted);
  font-size: 0.9375rem; line-height: 1.6;
}
.footer-accordion__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.footer-accordion__main { display: grid; gap: var(--space-xl); padding-block: var(--space-2xl); }
.footer-accordion__about { max-width: 22rem; margin: var(--space-sm) 0 var(--space-md); }
.footer-accordion__contact { display: grid; justify-items: start; gap: var(--space-xs); font-style: normal; }

/* Phones: full-width 44px disclosure rows split by hairlines */
.footer-accordion__nav { border-top: 1px solid var(--border-subtle); }
.footer-accordion__group { border-bottom: 1px solid var(--border-subtle); }
.footer-accordion__summary { list-style: none; cursor: pointer; border-radius: var(--radius-sm); color: var(--text-main); }
.footer-accordion__summary::-webkit-details-marker { display: none; }
.footer-accordion__heading {
  display: flex; align-items: center; justify-content: space-between; gap: var(--space-md);
  min-height: 2.75rem; margin: 0;
  font-size: 0.875rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;
}
.footer-accordion__chevron {
  flex: none; width: 1.25rem; height: 1.25rem; transition: rotate var(--transition-smooth);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.footer-accordion__group[open] .footer-accordion__chevron { rotate: 180deg; }
.footer-accordion__list { display: grid; gap: var(--space-sm); margin: 0; padding: 0 0 var(--space-md); list-style: none; }

/* Links and the light-surface focus ring */
.footer-accordion a {
  color: inherit; text-decoration: none; border-radius: var(--radius-sm); overflow-wrap: anywhere;
  transition: color var(--transition-fast);
}
.footer-accordion a:hover { color: var(--primary); text-decoration: underline; }
.footer-accordion a:focus-visible,
.footer-accordion__summary:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
/* Logo: the doubled class outranks `.footer-accordion a` */
.footer-accordion .footer-accordion__logo { font-size: 1.25rem; font-weight: 700; color: var(--text-main); }

/* Legal bar */
.footer-accordion__bottom { border-top: 1px solid var(--border-subtle); }
.footer-accordion__bar { display: flex; flex-direction: column; gap: var(--space-sm); padding-block: var(--space-lg); font-size: 0.875rem; }
.footer-accordion__copy { margin: 0; }
.footer-accordion__legal { display: flex; flex-wrap: wrap; column-gap: var(--space-lg); margin: 0; padding: 0; list-style: none; }
.footer-accordion__legal a { display: inline-block; padding-block: var(--space-xs); }

/* From 768px: a 3-column grid; summaries read as plain headings (the JS keeps groups open and untabbable) */
@media (min-width: 768px) {
  .footer-accordion__main { grid-template-columns: minmax(0, 1fr) minmax(0, 2fr); }
  .footer-accordion__nav { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-lg); border-top: 0; }
  .footer-accordion__group { border-bottom: 0; }
  .footer-accordion__summary { cursor: default; pointer-events: none; }
  .footer-accordion__heading { min-height: 0; margin-bottom: var(--space-sm); }
  .footer-accordion__chevron { display: none; }
  .footer-accordion__list { padding-bottom: 0; }
  .footer-accordion__bar { flex-direction: row; align-items: center; justify-content: space-between; }
}
```

### JS

```js
// Below 768px groups start collapsed; from 768px they stay open and the summary leaves the tab order
const footerWide = matchMedia('(min-width: 768px)');
const footerGroups = document.querySelectorAll('.footer-accordion__group');

const syncFooterGroups = () => footerGroups.forEach((group) => {
  group.open = footerWide.matches;
  group.querySelector('.footer-accordion__summary').tabIndex = footerWide.matches ? -1 : 0;
});

// Re-open a group closed on desktop some other way (e.g. a screen reader's virtual cursor)
footerGroups.forEach((group) => group.addEventListener('toggle', () => {
  if (footerWide.matches && !group.open) group.open = true;
}));

syncFooterGroups();
footerWide.addEventListener('change', syncFooterGroups);
```

### Notes

- `<details>`/`<summary>` give the expand/collapse state and keyboard support (Enter/Space) natively, so no ARIA is needed. Chromium also auto-expands a closed group when find-in-page matches inside it.
- Groups ship `open` and the script closes them on phones after load, so there's a brief reflow. It's usually below the fold; if not, close them in the server-rendered HTML for mobile.
- From 768px the CSS removes the pointer and chevron and the JS sets `tabindex="-1"`, so the summary is a heading in look and behavior. Without JS, a keyboard user can still collapse a group on desktop; that's harmless.
- A heading inside `<summary>` is valid HTML. Some screen readers announce it only as the toggle's name, not as a heading, so don't rely on it for heading navigation.
- Crossing 768px (rotation, resize) resets groups: open on desktop, collapsed on phones.

## 6. Brand wordmark footer

Dark footer that closes on an oversized wordmark sized to its container. Above it sit a contact row (phone, email, address) and social icons; below it, copyright and legal links.
The wordmark is decorative and `aria-hidden`; the brand name stays in the copyright line.

### HTML

```html
<footer class="footer-brand">
  <div class="footer-brand__inner">
    <div class="footer-brand__meta">
      <address class="footer-brand__contact">
        <a class="footer-brand__item" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5l1.5-2.5 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2" /></svg>
          (555) 555-0123
        </a>
        <a class="footer-brand__item" href="mailto:hello@example.com">
          <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="14" rx="2" /><path d="m3 7 9 6 9-6" /></svg>
          hello@example.com
        </a>
        <span class="footer-brand__item">
          <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z" /><circle cx="12" cy="10" r="2.5" /></svg>
          123 Main St, Springfield
        </span>
      </address>

      <ul class="footer-brand__social" role="list" aria-label="Social media">
        <li>
          <a class="footer-brand__icon" href="https://social.example.com/brand" aria-label="Brand photos">
            <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M4 7h3l2-3h6l2 3h3v12H4z" /><circle cx="12" cy="13" r="3.5" /></svg>
          </a>
        </li>
        <li>
          <a class="footer-brand__icon" href="https://video.example.com/brand" aria-label="Brand videos">
            <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9" /><path d="m10 8.5 5 3.5-5 3.5z" /></svg>
          </a>
        </li>
        <li>
          <a class="footer-brand__icon" href="https://community.example.com/brand" aria-label="Brand community">
            <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22z" /></svg>
          </a>
        </li>
      </ul>
    </div>

    <div class="footer-brand__mark">
      <p class="footer-brand__wordmark" aria-hidden="true">Brand</p>
    </div>

    <div class="footer-brand__bar">
      <p class="footer-brand__copy">© 2026 Brand. All rights reserved.</p>
      <ul class="footer-brand__legal" role="list">
        <li><a href="/privacy">Privacy</a></li>
        <li><a href="/terms">Terms</a></li>
      </ul>
    </div>
  </div>
</footer>
```

### CSS

```css
/* Dark full-bleed footer with its own container */
.footer-brand {
  background: var(--surface-dark); color: var(--text-inverse-muted);
  font-size: 0.9375rem; line-height: 1.6;
}
.footer-brand__inner {
  display: grid; gap: var(--space-xl);
  max-width: var(--container-max); margin-inline: auto; padding: var(--space-2xl) var(--gutter) var(--space-lg);
}

/* Contact and social rows: stacked on phones, one line from 768px */
.footer-brand__meta { display: flex; flex-direction: column; gap: var(--space-lg); }
.footer-brand__contact { display: flex; flex-direction: column; align-items: flex-start; gap: var(--space-sm) var(--space-xl); font-style: normal; }
.footer-brand__item { display: inline-flex; align-items: center; gap: var(--space-sm); min-height: 1.5rem; }
.footer-brand__item svg,
.footer-brand__icon svg {
  flex: none; width: 1.25rem; height: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.footer-brand__social { display: flex; flex-wrap: wrap; gap: var(--space-sm); margin: 0; padding: 0; list-style: none; }
.footer-brand__icon {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem;
  border: 1px solid color-mix(in srgb, var(--text-inverse) 30%, transparent); border-radius: var(--radius-full);
  color: var(--text-inverse); transition: background-color var(--transition-fast), color var(--transition-fast);
}
.footer-brand__icon:hover { background: var(--text-inverse); color: var(--surface-dark); }

/* Oversized wordmark: 30cqi tracks the container width (18vw fallback); overflow guards long names */
.footer-brand__mark { container-type: inline-size; overflow: hidden; }
.footer-brand__wordmark {
  margin: 0; white-space: nowrap; color: var(--text-inverse);
  font-size: clamp(3.5rem, 18vw, 14rem);
  font-size: clamp(3.5rem, 30cqi, 22rem);
  font-weight: 800; line-height: 1; letter-spacing: -0.05em;
}

/* Copyright bar */
.footer-brand__bar {
  display: flex; flex-direction: column; gap: var(--space-sm); padding-top: var(--space-lg);
  border-top: 1px solid color-mix(in srgb, var(--text-inverse) 15%, transparent); font-size: 0.875rem;
}
.footer-brand__copy { margin: 0; }
.footer-brand__legal { display: flex; flex-wrap: wrap; column-gap: var(--space-lg); margin: 0; padding: 0; list-style: none; }

/* Text links muted until hovered; light outline for focus on the dark surface */
.footer-brand__contact a,
.footer-brand__legal a {
  color: inherit; text-decoration: none; overflow-wrap: anywhere;
  transition: color var(--transition-fast);
}
.footer-brand__contact a:hover,
.footer-brand__legal a:hover { color: var(--text-inverse); text-decoration: underline; }
.footer-brand__legal a { display: inline-block; padding-block: var(--space-xs); }
.footer-brand a:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }

@media (min-width: 768px) {
  .footer-brand__meta { flex-direction: row; align-items: center; justify-content: space-between; }
  .footer-brand__contact { flex-direction: row; flex-wrap: wrap; align-items: center; }
  .footer-brand__bar { flex-direction: row; align-items: center; justify-content: space-between; }
}
```

### Notes

- The wordmark is decoration (`aria-hidden="true"`, not a link), so screen readers skip it; the copyright line keeps the brand name in the page. Don't put the only copy of the name there.
- Sizing: `30cqi` follows the container (Chrome 105+, Safari 16+, Firefox 110+). Browsers without container units drop that declaration and use the `18vw` one. Tune `30cqi` to your name's length so it spans the row; `overflow: hidden` on the wrapper prevents horizontal scroll if it's too long.
- Social icons and labels are generic placeholders. Swap in each network's mark and name it in `aria-label`, e.g. "Brand on <Network>".
- `tel:` uses E.164 (`+15555550123`) so it dials from anywhere; the visible number can use local formatting.
- To use a logo instead of text, use an inline SVG with `aria-hidden="true"` and `width: 100%`. No container units needed.
