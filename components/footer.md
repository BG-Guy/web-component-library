# Footer

Dark multi-column site footer with a legal bar. Depends on `tokens/variables.css`.

- **Columns:** company summary + logo · quick links · service areas · contact (clickable phone and email).
- **Layout:** stacked below 768px · 2×2 from 768px · 4 columns from 1024px. Legal bar stacks on mobile and splits left/right from 768px.

## HTML

```html
<footer class="site-footer">
  <div class="site-footer__container site-footer__grid">
    <div class="site-footer__brand">
      <a class="site-footer__logo" href="/">Brand</a>
      <p>Licensed, insured and locally owned. Honest quotes and work we guarantee.</p>
    </div>

    <nav class="site-footer__col" aria-labelledby="footer-links">
      <h2 id="footer-links" class="site-footer__heading">Quick links</h2>
      <ul role="list">
        <li><a href="/about">About us</a></li>
        <li><a href="/services">Services</a></li>
        <li><a href="/reviews">Reviews</a></li>
        <li><a href="/faq">FAQ</a></li>
      </ul>
    </nav>

    <div class="site-footer__col">
      <h2 class="site-footer__heading">Service areas</h2>
      <ul role="list">
        <li><a href="/areas/downtown">Downtown</a></li>
        <li><a href="/areas/northside">Northside</a></li>
        <li><a href="/areas/westlake">Westlake</a></li>
        <li><a href="/areas/riverside">Riverside</a></li>
      </ul>
    </div>

    <div class="site-footer__col">
      <h2 class="site-footer__heading">Contact</h2>
      <address>
        <ul role="list">
          <li><a href="tel:+15555550123">(555) 555-0123</a></li>
          <li><a href="mailto:hello@example.com">hello@example.com</a></li>
          <li>123 Main St, Springfield</li>
        </ul>
      </address>
      <p class="site-footer__hours">Mon–Sat, 7am–7pm</p>
    </div>
  </div>

  <div class="site-footer__bottom">
    <div class="site-footer__container site-footer__bar">
      <p>© 2026 Brand. All rights reserved.</p>
      <ul class="site-footer__legal" role="list">
        <li><a href="/privacy">Privacy</a></li>
        <li><a href="/terms">Terms</a></li>
        <li><a href="/accessibility">Accessibility</a></li>
      </ul>
    </div>
  </div>
</footer>
```

## CSS

```css
.site-footer {
  background: var(--surface-dark); color: var(--text-inverse-muted);
  font-size: 0.9375rem; line-height: 1.6;
}
.site-footer__container { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.site-footer__grid { display: grid; gap: var(--space-xl); padding-block: var(--space-2xl); }

.site-footer__logo { font-size: 1.25rem; font-weight: 700; color: var(--text-inverse); text-decoration: none; }
.site-footer__brand p { max-width: 22rem; margin: var(--space-sm) 0 0; }
.site-footer__heading {
  margin: 0 0 var(--space-sm);
  font-size: 0.875rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;
  color: var(--text-inverse);
}
.site-footer ul { margin: 0; padding: 0; list-style: none; }
.site-footer__col ul { display: grid; gap: var(--space-sm); }
.site-footer address { font-style: normal; }
.site-footer__hours { margin: var(--space-sm) 0 0; }

.site-footer a {
  color: inherit; text-decoration: none; overflow-wrap: anywhere;
  transition: color var(--transition-fast);
}
.site-footer a:hover { color: var(--text-inverse); text-decoration: underline; }
.site-footer a:focus-visible { /* light ring: --focus-ring is too faint on dark surfaces */
  outline: 2px solid var(--text-inverse); outline-offset: 2px; border-radius: var(--radius-sm);
}

/* Bottom bar */
.site-footer__bottom { border-top: 1px solid color-mix(in srgb, var(--text-inverse) 15%, transparent); }
.site-footer__bar {
  display: flex; flex-direction: column; gap: var(--space-sm);
  padding-block: var(--space-lg); font-size: 0.875rem;
}
.site-footer__bar p { margin: 0; }
.site-footer__legal { display: flex; flex-wrap: wrap; gap: var(--space-xs) var(--space-lg); }

@media (min-width: 768px) {
  .site-footer__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .site-footer__bar { flex-direction: row; align-items: center; justify-content: space-between; }
}

@media (min-width: 1024px) {
  .site-footer__grid { grid-template-columns: 1.5fr 1fr 1fr 1.25fr; }
}
```

## Notes

- `tel:` links use E.164 (`+15555550123`) so they dial from anywhere. The visible number can use local formatting.
- `<address>` holds contact details only. Headings aren't allowed inside it, so the column heading sits above it.
- Text contrast on `--surface-dark` is about 7:1 for muted and 17:1 for headings.
- Render the copyright year on the server or at build time; no JS needed.
- Local SEO: repeat the same name, address and phone in `LocalBusiness` JSON-LD.
- **React:** static markup; `class` → `className`.
- **Tailwind (v4):** grid `grid gap-8 md:grid-cols-2 lg:grid-cols-[1.5fr_1fr_1fr_1.25fr]`. Bar `flex flex-col gap-2 md:flex-row md:items-center md:justify-between`.
