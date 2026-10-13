# CLAUDE.md

## Role and purpose

You are a frontend architect with direct access to this curated component library. Its modules are your primary blueprint and source of truth when designing pages. Start from the matching pattern and adapt it. Don't invent a new pattern when one already exists here.

## Progressive disclosure

Never load or scan all component files upfront. Read only what the current task needs:

| Task                                                             | Read                                   |
| ---------------------------------------------------------------- | -------------------------------------- |
| Any output                                                       | `tokens/variables.css`                 |
| **Navigation**                                                   |                                        |
| Standard sticky header with slide-out mobile drawer              | `components/navigation.md`             |
| Header variants: transparent-over-hero, auto-hide, split logo, dropdowns, mega menu, utility bar, floating pill | `components/navbar-variants.md` |
| Mobile menus: full-screen overlay, bottom tab bar, accordion drawer, bottom sheet, slide-down panel, hamburger animations, link strip, compact top bar | `components/mobile-navigation.md` |
| Tabs, breadcrumbs, pagination, form stepper, table of contents, back-to-top | `components/tabs-and-wayfinding.md` |
| **Page sections**                                                |                                        |
| Hero / above-the-fold section                                    | `components/heroes.md`                 |
| Stats, trust badges, certifications                              | `components/trust-and-stats.md`        |
| Feature, review or pricing cards                                 | `components/cards-and-grids.md`        |
| Article, product, horizontal, image-overlay, glass or profile cards | `components/card-variants.md`       |
| Feature rows, team, timeline, comparison table, pricing toggle, contact + map, pull quote | `components/content-blocks.md` |
| "How it works" / process steps                                   | `components/process-steps.md`          |
| Project photos, before/after slider                              | `components/gallery.md`                |
| Carousels: card scroller, testimonials, logo marquee, hero slideshow, thumbnails, ticker | `components/carousels.md` |
| FAQ / accordion                                                  | `components/faq.md`                    |
| CTA band, sticky mobile call bar                                 | `components/cta-sections.md`           |
| Standard multi-column footer                                     | `components/footer.md`                 |
| Footer variants: minimal, newsletter, mega, CTA-topped, mobile accordion, wordmark | `components/footer-variants.md` |
| **Controls and feedback**                                        |                                        |
| Buttons: base system, icon, loading, toggle, segmented, group, split, FAB, copy | `components/buttons.md` |
| Contact or lead form                                             | `components/forms.md`                  |
| Switch, custom checkbox/radio, option cards, input addons, search, password, file upload, quantity | `components/form-controls.md` |
| Alerts, toasts, announcement bar, cookie banner, tooltip, chips, progress, empty state | `components/feedback.md` |
| Modal / popup dialog                                             | `components/modals.md`                 |
| **Visual effects**                                               |                                        |
| Section backgrounds: gradients, patterns, grain, aurora, image scrim, dividers, video | `components/backgrounds.md` |
| Scroll reveals, progress bar, parallax, rotating words, skeletons, loaders, pulse, shimmer | `components/animations.md` |
| Page transitions, link underline, image zoom, flip card, crossfade, ripple, tilt | `components/transitions.md` |
| **Full pages**                                                   |                                        |
| Landing page for a service business                              | `templates/service-landing.md`, then only the components it lists |

- For a full page, start from the closest template's section order, then work section by section. Open each component file only when you reach that section.
- Don't glob, grep or list the repo for context. This table is the index. Open `README.md` only if the table doesn't cover the request.
- Single-pattern files: go straight to `## HTML`, `## CSS`, `## JS`, `## Notes` or `## Adapting`.
- Multi-pattern files open with a numbered pattern table. Read the table, then only the `## N. <Pattern>` section you need; each section is self-contained. In `buttons.md` and `navbar-variants.md`, pattern 1 is a base the others build on, so read it too.

## Execution constraints

- Do NOT run automated test suites, headless browser verification or package audits unless explicitly asked.
- Deliver in a single pass. Output self-contained HTML/CSS/JS (one file, with tokens inlined or linked), or a framework-specific component (React/JSX, Vue, Svelte, Tailwind) when one is requested.
- Keep the design tokens from `tokens/variables.css`. Style with `var(--token)`. Don't hard-code colors, spacing, radii, shadows or durations; if a value is missing, add a token.
- When adapting a module, keep its accessibility wiring intact: labels, `aria-*` attributes, focus handling and keyboard support.

## Quality bar

- **Fast loads:** HTML and CSS first. No frameworks or libraries unless asked. Give every image `width`/`height`, lazy-load below the fold, and never lazy-load the hero image.
- **No JavaScript bloat:** use vanilla JS only for behavior CSS can't handle. No jQuery, animation libraries or icon fonts; use inline SVG.
- **Clean breakpoints:** mobile-first `min-width` queries, with 768px as the main breakpoint. No horizontal scroll at 320px wide.
- **Accessibility (WCAG 2.2 AA):** semantic landmarks, one `<h1>` per page, labelled controls, visible focus (`--focus-ring`), 4.5:1 text contrast, 24px minimum target size, and `prefers-reduced-motion` respected. The motion tokens handle transitions; keyframe animations need their own reduced-motion fallback, and anything moving longer than 5s needs a pause control.
- **Effects in moderation:** use at most one or two attention effects per page (animations, backgrounds, transitions). They support the content; they don't replace it.
