# Heroes

Two above-the-fold patterns sharing one stylesheet. Depends on `tokens/variables.css`.

- **A. Split:** headline, value points and CTAs on the left; image or video on the right. Stacks text-first below 768px.
- **B. Centered:** pill badge, title, lead and CTAs, centered.

## HTML

### A. Split

```html
<section class="hero hero--split" aria-labelledby="hero-title">
  <div class="hero__inner">
    <div class="hero__content">
      <h1 id="hero-title" class="hero__title">Expert service, done right the first time</h1>
      <p class="hero__lead">Licensed pros, upfront pricing and same-day appointments across the metro area.</p>
      <ul class="hero__points" role="list">
        <li>Flat-rate quotes before work starts</li>
        <li>Same-day and weekend availability</li>
        <li>Workmanship guaranteed for 5 years</li>
      </ul>
      <div class="hero__actions">
        <a class="hero-btn hero-btn--primary" href="#quote">Get a free quote</a>
        <a class="hero-btn hero-btn--secondary" href="tel:+15555550123">Call (555) 555-0123</a>
      </div>
    </div>
    <div class="hero__media">
      <img src="hero.jpg" alt="Technician inspecting a water heater" width="1200" height="900" fetchpriority="high">
      <!-- Video: <video autoplay muted loop playsinline poster="hero.jpg" aria-hidden="true">
                    <source src="hero.mp4" type="video/mp4"></video> -->
    </div>
  </div>
</section>
```

Add `hero--media-first` to the section to show the media above the text on mobile.

### B. Centered

```html
<section class="hero hero--centered" aria-labelledby="hero-centered-title">
  <div class="hero__inner">
    <p class="hero__badge">Now booking spring appointments</p>
    <h1 id="hero-centered-title" class="hero__title">Home services you can actually rely on</h1>
    <p class="hero__lead">One call for repairs, installs and maintenance. Transparent pricing, no surprises.</p>
    <div class="hero__actions">
      <a class="hero-btn hero-btn--primary" href="#quote">Book a visit</a>
      <a class="hero-btn hero-btn--secondary" href="#services">See services</a>
    </div>
  </div>
</section>
```

## CSS

```css
/* Shared */
.hero { padding-block: var(--space-2xl); background: var(--surface-light); color: var(--text-main); }
.hero__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.hero__title {
  margin: 0; font-size: clamp(2rem, 1rem + 3vw, 3.5rem);
  line-height: 1.1; letter-spacing: -0.02em; text-wrap: balance;
}
.hero__lead {
  max-width: 40rem; margin: var(--space-md) 0 0;
  font-size: 1.125rem; line-height: 1.6; color: var(--text-muted);
}
.hero__actions { display: flex; flex-wrap: wrap; gap: var(--space-sm); margin-top: var(--space-xl); }

.hero-btn {
  display: inline-flex; flex: 1 1 auto; align-items: center; justify-content: center; /* full-width on mobile */
  min-height: 2.75rem; padding: var(--space-sm) var(--space-lg);
  border: 1px solid transparent; border-radius: var(--radius-md);
  font-weight: 600; text-decoration: none;
  transition: background-color var(--transition-fast), border-color var(--transition-fast);
}
.hero-btn:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.hero-btn--primary { background: var(--primary); color: var(--text-inverse); }
.hero-btn--primary:hover { background: var(--primary-hover); }
.hero-btn--secondary { border-color: var(--border-subtle); color: var(--text-main); }
.hero-btn--secondary:hover { border-color: var(--text-muted); }

/* A. Split */
.hero--split .hero__inner { display: grid; gap: var(--space-xl); align-items: center; }
.hero__points { display: grid; gap: var(--space-sm); margin: var(--space-lg) 0 0; padding: 0; list-style: none; line-height: 1.5; }
.hero__points li { position: relative; padding-left: var(--space-lg); }
.hero__points li::before { /* CSS checkmark */
  content: ""; position: absolute; left: var(--space-xs); top: 0.35em;
  width: 0.4em; height: 0.8em;
  border: solid var(--primary); border-width: 0 0.15em 0.15em 0;
  transform: rotate(45deg);
}
.hero__media {
  aspect-ratio: 4 / 3; overflow: hidden;
  border-radius: var(--radius-lg); box-shadow: var(--shadow-lg);
  background: var(--border-subtle); /* placeholder while media loads */
}
.hero__media > img, .hero__media > video { display: block; width: 100%; height: 100%; object-fit: cover; }

/* B. Centered */
.hero--centered { text-align: center; }
.hero--centered .hero__inner { max-width: 48rem; }
.hero--centered .hero__lead { margin-inline: auto; }
.hero--centered .hero__actions { justify-content: center; }
.hero__badge {
  display: inline-flex; align-items: center; gap: var(--space-sm);
  margin: 0 0 var(--space-md); padding: var(--space-xs) var(--space-md);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--primary) 8%, var(--surface-light));
  color: var(--primary); font-size: 0.875rem; font-weight: 600;
}
.hero__badge::before {
  content: ""; width: 0.5rem; height: 0.5rem;
  border-radius: var(--radius-full); background: var(--accent);
}

@media (max-width: 767.98px) {
  .hero--media-first .hero__media { order: -1; }
}

@media (min-width: 768px) {
  .hero { padding-block: calc(var(--space-2xl) * 2); }
  .hero--split .hero__inner { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-2xl); }
  .hero-btn { flex: none; }
}
```

## Notes

- Use one `<h1>` per page. Demote to `<h2>` if the hero isn't the page's main heading.
- The hero image is usually the LCP element: keep `fetchpriority="high"`, never add `loading="lazy"`, and keep `width`/`height` to prevent layout shift. Serve AVIF/WebP through `<picture>`.
- Video is decorative (`aria-hidden`, `muted`). A loop longer than 5s needs a pause control (WCAG 2.2.2). For `prefers-reduced-motion` users, show the poster image instead.
- `role="list"` keeps list semantics in Safari after `list-style: none`.
- **React:** `class` → `className`, `fetchpriority` → `fetchPriority`.
- **Tailwind:** split grid `grid items-center gap-8 md:grid-cols-2 md:gap-12`; media-first `max-md:order-first`.
