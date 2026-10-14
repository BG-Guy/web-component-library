# CLAUDE.md

## Role and purpose

You are a frontend architect with direct access to this curated component library. Its modules are your primary blueprint and source of truth when designing pages. Start from the matching pattern and adapt it. Don't invent a new pattern when one already exists here.

**Premium first.** `components/premium/` holds 100 flagship components: modern design, rich motion, one component per file, grouped in the table below. When a premium component fits the section, use it. Fall back to the base library only for what premium doesn't cover. Most premium components share one visual language (deep surfaces, gradient light, `--font-display`, spring motion), so mixing them keeps a page coherent. The **Retro styles** group is deliberately different: each brings its own era, palette and sometimes font, so use one as a statement section rather than mixing several on a page.

## Progressive disclosure

Never load or scan all component files upfront. Read only what the current task needs.

### Premium components (`components/premium/`, one component per file)

| Section or need                                  | Read                                      |
| ------------------------------------------------ | ----------------------------------------- |
| **Navigation and menus**                         |                                           |
| Header: floating glass bar, mobile circle-reveal menu | `components/premium/floating-navbar.md` |
| Dropdown / mega menu that morphs between menus   | `components/premium/morphing-dropdown.md` |
| Full-screen menu: numbered links + preview pane  | `components/premium/split-menu.md`        |
| Full-screen menu built from falling curtain strips | `components/premium/curtain-menu.md`    |
| Menu revealed by pushing the page back in 3D     | `components/premium/perspective-menu.md`  |
| Floating action button with gooey quick actions (call, text, quote) | `components/premium/gooey-menu.md` |
| Radial fan of quick actions, press-and-drag      | `components/premium/radial-menu.md`       |
| Bottom nav: magnifying dock                      | `components/premium/dock-nav.md`          |
| Bottom nav: tab bar with a liquid notch          | `components/premium/notch-tabbar.md`      |
| Dynamic Island pill that expands into a menu     | `components/premium/island-nav.md`        |
| Side drawer that follows swipe gestures          | `components/premium/swipe-drawer.md`      |
| Multi-level drill-down menu (mobile)             | `components/premium/drilldown-menu.md`    |
| Site search / command palette (⌘K)               | `components/premium/command-palette.md`   |
| **Heroes**                                       |                                           |
| Dark hero: aurora light, dashboard mock          | `components/premium/aurora-hero.md`       |
| Dark technical hero: grid with travelling light beams | `components/premium/beam-grid-hero.md` |
| Search-first hero ("What needs fixing?") with suggestions | `components/premium/search-hero.md` |
| Hero over a tilted, scrolling wall of project photos | `components/premium/tilted-wall-hero.md` |
| Split hero with services orbiting the brand      | `components/premium/orbit-hero.md`        |
| Full-bleed photo slideshow hero, story-style progress | `components/premium/reel-hero.md`    |
| Hero with an x-ray lens that sees inside the walls | `components/premium/xray-hero.md`        |
| **Headlines and type**                           |                                           |
| Animated headings: word rise, highlighter, underline draw, scroll-lit paragraph | `components/premium/kinetic-headline.md` |
| Text that decodes from random glyphs             | `components/premium/scramble-text.md`     |
| Headline whose weight swells under the cursor    | `components/premium/weight-wave.md`       |
| Outlined statement that fills with colour on scroll | `components/premium/fill-text.md`      |
| Text flowing along a curved path on scroll       | `components/premium/path-text.md`         |
| Circular text badges (CTA, seal, scroll cue)     | `components/premium/circle-text.md`       |
| **Scroll stories**                               |                                           |
| How it works / process (scroll-linked line)      | `components/premium/scroll-timeline.md`   |
| Scrollytelling with a pinned device              | `components/premium/sticky-showcase.md`   |
| Projects in a pinned horizontal scroll           | `components/premium/horizontal-scroll.md` |
| Photo that opens to full screen as you scroll into it | `components/premium/zoom-through.md` |
| Sticky cards that stack into a deck ("why choose us") | `components/premium/stacking-cards.md` |
| Fly through a giant word into the scene behind   | `components/premium/text-mask-zoom.md`    |
| Pinned gallery with clip-path wipes              | `components/premium/wipe-gallery.md`      |
| Huge type marquee that reacts to scroll speed    | `components/premium/velocity-marquee.md`  |
| Photo columns moving at different speeds         | `components/premium/column-parallax.md`   |
| Service list that lights the item in focus       | `components/premium/focus-list.md`        |
| Company milestones flying past in 3D             | `components/premium/depth-tunnel.md`      |
| Before/after scrubbed by scroll                  | `components/premium/scroll-compare.md`    |
| Blueprint that draws itself on scroll            | `components/premium/blueprint-draw.md`    |
| Illustrated neighbourhood with layered parallax  | `components/premium/parallax-scene.md`    |
| **Blending sections**                            |                                           |
| Page colours that morph between sections         | `components/premium/chameleon-sections.md` |
| Sticky type that inverts over every section      | `components/premium/blend-text.md`        |
| Full sections that stack like a deck             | `components/premium/section-stack.md`     |
| Sections that melt into each other (soft seams, grain) | `components/premium/seam-melt.md`   |
| Wave divider that ripples with scroll            | `components/premium/liquid-divider.md`    |
| Cover that slides open like doors                | `components/premium/curtain-split.md`     |
| Glass panels straddling two sections             | `components/premium/overlap-glass.md`     |
| Card that morphs into a detail view              | `components/premium/card-morph.md`        |
| **Content sections**                             |                                           |
| Features / benefits section                      | `components/premium/bento-grid.md`        |
| Product tour / feature tabs                      | `components/premium/feature-tabs.md`      |
| Headline numbers / stats                         | `components/premium/stat-counters.md`     |
| Pricing with monthly/yearly                      | `components/premium/pricing-plans.md`     |
| FAQ                                              | `components/premium/smooth-accordion.md`  |
| Partner / client logos                           | `components/premium/logo-marquee.md`      |
| Reviews / testimonials wall                      | `components/premium/testimonial-wall.md`  |
| **Cards and galleries**                          |                                           |
| Project / portfolio carousel                     | `components/premium/drag-carousel.md`     |
| Photo gallery with full-screen viewer            | `components/premium/lightbox-gallery.md`  |
| Membership card with holographic foil            | `components/premium/holo-card.md`         |
| Swipeable review cards                           | `components/premium/swipe-deck.md`        |
| Expanding image panels (service categories)      | `components/premium/expand-panels.md`     |
| Project list with cursor-following previews      | `components/premium/hover-preview-list.md` |
| 3D coverflow carousel                            | `components/premium/coverflow.md`         |
| Booking confirmation as a wallet pass            | `components/premium/wallet-pass.md`       |
| Interactive house cutaway with hotspots          | `components/premium/hotspot-explorer.md`  |
| Team / crew cards                                | `components/premium/crew-cards.md`        |
| Draggable, endless gallery canvas                | `components/premium/infinite-canvas.md`   |
| Case studies as tabbed folders                   | `components/premium/folder-stack.md`      |
| **Forms and booking**                            |                                           |
| Contact / lead form                              | `components/premium/floating-label-form.md` |
| Multi-step quote form                            | `components/premium/quote-wizard.md`      |
| Appointment picker: calendar and time slots      | `components/premium/booking-calendar.md`  |
| Price estimate calculator                        | `components/premium/estimate-calculator.md` |
| Service-area / ZIP checker with map              | `components/premium/coverage-checker.md`  |
| Live technician / job tracker                    | `components/premium/job-tracker.md`       |
| Verification code input                          | `components/premium/otp-input.md`         |
| Photo / file upload                              | `components/premium/file-drop.md`         |
| Star rating and feedback                         | `components/premium/star-rating.md`       |
| **Feedback and utilities**                       |                                           |
| Buttons with micro-interactions                  | `components/premium/premium-buttons.md`   |
| Booking or any modal dialog / bottom sheet       | `components/premium/spring-modal.md`      |
| Notifications / toasts                           | `components/premium/toast-stack.md`       |
| Support chat widget                              | `components/premium/chat-widget.md`       |
| Confetti celebration (`window.confetti`)         | `components/premium/confetti.md`          |
| Dark mode switch with circular reveal            | `components/premium/theme-switch.md`      |
| Custom cursor                                    | `components/premium/custom-cursor.md`     |
| **Retro styles**                                 |                                           |
| CRT terminal with working commands               | `components/premium/crt-terminal.md`      |
| 8-bit arcade UI                                  | `components/premium/pixel-arcade.md`      |
| Windows 95 desktop with working windows          | `components/premium/win95-window.md`      |
| Synthwave / outrun hero                          | `components/premium/synthwave-hero.md`    |
| VHS title card with glitch                       | `components/premium/vhs-glitch.md`        |
| Neo-brutalist section                            | `components/premium/neo-brutalist.md`     |
| Swiss / editorial poster section                 | `components/premium/swiss-poster.md`      |
| 70s groovy heritage section                      | `components/premium/groovy-70s.md`        |
| Skeuomorphic thermostat dial                     | `components/premium/skeuo-thermostat.md`  |
| Split-flap departures board                      | `components/premium/split-flap.md`        |
| **Footers**                                      |                                           |
| Closing CTA + footer                             | `components/premium/cta-footer.md`        |
| Footer revealed as the page lifts away           | `components/premium/reveal-footer.md`     |
| Footer revealed by a growing circle              | `components/premium/circle-footer.md`     |
| Footer with a giant interactive wordmark         | `components/premium/type-footer.md`       |
| Footer that unfolds like paper                   | `components/premium/unfold-footer.md`     |
| Footer under a curved edge that flattens         | `components/premium/curve-footer.md`      |
| Footer opening with a huge marquee CTA           | `components/premium/marquee-footer.md`    |

### Base library

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
- Single-pattern files (including every premium file): go straight to `## HTML`, `## CSS`, `## JS`, `## Notes` or `## Adapting`.
- Premium components need the premium tokens in `tokens/variables.css` and look as intended with Geist + Geist Mono loaded (Google Fonts). Without them they fall back to the system font. A few files name an extra Google Font on their **Fonts:** line; load it when you use that component.
- Page-level premium components (menus, reveal footers, theme switch, cursor, chat, confetti) explain how to wire them into a page in their Notes. Follow that wiring, and keep at most one attention effect per section.
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
