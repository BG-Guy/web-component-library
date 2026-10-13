# Service Landing Page

One-page site for a local service business, assembled from the component modules. This file holds only the section order, page skeleton, page-level CSS and assembly rules. Open each component file only when you reach its section.

## Section order

| #  | Section                         | Module                                            | id         |
| -- | ------------------------------- | ------------------------------------------------- | ---------- |
| 1  | Header + mobile drawer          | `components/navigation.md`                        |            |
| 2  | Hero (holds the page `<h1>`)    | `components/heroes.md` → A. Split                 |            |
| 3  | Stats + badges                  | `components/trust-and-stats.md` → A, then B       |            |
| 4  | Services                        | `components/cards-and-grids.md` → Feature cards   | `services` |
| 5  | How it works                    | `components/process-steps.md`                     | `process`  |
| 6  | Recent work                     | `components/gallery.md` → B, then A               | `work`     |
| 7  | Reviews                         | `components/cards-and-grids.md` → Review card     | `reviews`  |
| 8  | Pricing (optional)              | `components/cards-and-grids.md` → Pricing cards   | `pricing`  |
| 9  | FAQ                             | `components/faq.md`                               | `faq`      |
| 10 | Quote form                      | `components/forms.md`                             | `quote`    |
| 11 | Closing CTA                     | `components/cta-sections.md` → A. CTA band        |            |
| 12 | Footer                          | `components/footer.md`                            |            |
| 13 | Mobile action bar               | `components/cta-sections.md` → B                  |            |

Point the header links and every "Get a quote" button at these ids (`#services`, `#quote`, …).

## HTML

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Brand | Home repairs and installs in Springfield</title>
  <meta name="description" content="Licensed, insured home services in Springfield. Upfront flat-rate pricing and same-day appointments.">
  <link rel="canonical" href="https://example.com/">
  <link rel="stylesheet" href="tokens/variables.css">
  <style>
    /* Page CSS (below), then each module's CSS in section order */
  </style>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Brand",
    "url": "https://example.com/",
    "telephone": "+1-555-555-0123",
    "email": "hello@example.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "123 Main St",
      "addressLocality": "Springfield",
      "addressRegion": "IL",
      "postalCode": "62701",
      "addressCountry": "US"
    },
    "areaServed": ["Downtown", "Northside", "Westlake", "Riverside"],
    "openingHours": "Mo-Sa 07:00-19:00"
  }
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  <!-- 1. navigation.md → HTML (header, backdrop, drawer) -->

  <main id="main">
    <!-- 2. heroes.md → A. Split -->

    <section class="section section--tight" aria-label="Why customers choose us">
      <div class="container">
        <!-- 3. trust-and-stats.md → A. Stats row, then B. Badge strip -->
      </div>
    </section>

    <section id="services" class="section section--alt" aria-labelledby="services-title">
      <div class="container">
        <header class="section-header">
          <p class="section-header__eyebrow">Services</p>
          <h2 id="services-title">Everything your home needs</h2>
          <p class="section-header__intro">Repairs, installs and maintenance from one licensed team.</p>
        </header>
        <!-- 4. cards-and-grids.md → Feature cards -->
      </div>
    </section>

    <section id="process" class="section" aria-labelledby="process-title">
      <div class="container">
        <header class="section-header">
          <p class="section-header__eyebrow">How it works</p>
          <h2 id="process-title">Booked in three simple steps</h2>
        </header>
        <!-- 5. process-steps.md -->
      </div>
    </section>

    <section id="work" class="section section--alt" aria-labelledby="work-title">
      <div class="container">
        <header class="section-header">
          <p class="section-header__eyebrow">Recent work</p>
          <h2 id="work-title">See the difference</h2>
        </header>
        <!-- 6. gallery.md → B. Before/after, then A. Project grid -->
      </div>
    </section>

    <section id="reviews" class="section" aria-labelledby="reviews-title">
      <div class="container">
        <header class="section-header">
          <p class="section-header__eyebrow">Reviews</p>
          <h2 id="reviews-title">What our customers say</h2>
        </header>
        <!-- 7. cards-and-grids.md → Review cards -->
      </div>
    </section>

    <!-- Optional -->
    <section id="pricing" class="section section--alt" aria-labelledby="pricing-title">
      <div class="container">
        <header class="section-header">
          <p class="section-header__eyebrow">Pricing</p>
          <h2 id="pricing-title">Simple, upfront pricing</h2>
        </header>
        <!-- 8. cards-and-grids.md → Pricing cards -->
      </div>
    </section>

    <!-- div, not section: the FAQ module brings its own <section> and <h2> -->
    <div id="faq" class="section">
      <div class="container">
        <!-- 9. faq.md -->
      </div>
    </div>

    <!-- div, not section: the form is already labelled by its own <h2> -->
    <div id="quote" class="section section--alt">
      <div class="container">
        <!-- 10. forms.md -->
      </div>
    </div>

    <!-- 11. cta-sections.md → A. CTA band -->
  </main>

  <!-- 12. footer.md -->
  <!-- 13. cta-sections.md → B. Mobile action bar -->

  <!-- One module script per component with JS. Module scope prevents name clashes, and modules run deferred. -->
  <script type="module">/* navigation.md → JS */</script>
  <script type="module">/* gallery.md → JS */</script>
  <script type="module">/* forms.md → JS */</script>
</body>
</html>
```

## CSS

```css
/* Base: reset, type and colors every module inherits */
*, *::before, *::after { box-sizing: border-box; }
body {
  margin: 0; font-family: var(--font-sans); font-size: 1rem; line-height: 1.6;
  color: var(--text-main); background: var(--surface-light);
}
img, video { max-width: 100%; height: auto; }
h1, h2, h3 { line-height: 1.2; text-wrap: balance; }

/* Anchors (and focused form fields) clear the sticky header; smooth scroll only if motion is OK */
[id] { scroll-margin-top: calc(var(--header-h, 4rem) + var(--space-md)); }
@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
}

/* Skip link: off-screen until focused */
.skip-link {
  position: absolute; top: var(--space-sm); left: var(--space-sm); z-index: 100;
  padding: var(--space-sm) var(--space-md); border-radius: var(--radius-md);
  background: var(--surface-dark); color: var(--text-inverse); font-weight: 600;
  translate: 0 -200%;
}
.skip-link:focus { translate: none; }

/* Layout helpers */
.container { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.section { padding-block: var(--space-2xl); }
.section--tight { padding-block: var(--space-xl); }
.section--alt { background: var(--surface-muted); }

/* Section header: eyebrow, h2, intro */
.section-header { max-width: 40rem; margin: 0 auto var(--space-xl); text-align: center; }
.section-header__eyebrow {
  margin: 0 0 var(--space-xs); font-size: 0.875rem; font-weight: 600;
  letter-spacing: 0.05em; text-transform: uppercase; color: var(--primary);
}
.section-header h2 { margin: 0; font-size: clamp(1.75rem, 1.25rem + 2vw, 2.5rem); }
.section-header__intro { margin: var(--space-sm) 0 0; color: var(--text-muted); }

/* Placement of modules on this page */
.badges, .compare + .gallery { margin-top: var(--space-xl); }
#quote .lead-form { margin-inline: auto; }

@media (min-width: 768px) {
  .section { padding-block: calc(var(--space-2xl) * 2); }
  .section--tight { padding-block: var(--space-2xl); }
}
```

## Assembly rules

- Paste the page CSS first, then each module's CSS in section order. Module classes are prefixed, so nothing needs deduplicating.
- Headings: the hero holds the only `<h1>`. Section titles are `<h2>`, and card and step titles are `<h3>`.
- Images: only the hero image loads eagerly, with `fetchpriority="high"`. Every other image gets `loading="lazy"`.
- Keep the business details identical everywhere they appear: hero, footer, action bar, form copy and JSON-LD (name, phone, email, address, service areas).
- Switch `"@type"` to the closest schema.org subtype, e.g. `Plumber`, `Electrician`, `HVACBusiness` or `RoofingContractor`.
- Drop any section the business can't fill with real content (no pricing, no photos). Then remove its nav link and keep the `--alt` backgrounds alternating.
- For production, combine the tokens, page CSS and module CSS into one stylesheet, and the scripts into one deferred file.
