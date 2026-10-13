# Web Component Library

A collection of modular, battle-tested UI patterns for marketing and local-service sites, built on a shared set of design tokens.

- **`components/premium/`**: 20 flagship components with modern design and rich motion: floating glass navbar, morphing mega menu, aurora hero, bento grid, odometer stats, scroll-linked timeline, sticky scrollytelling, shared-element lightbox, spring modal, stacked toasts and more. Start here.
- **The base library**: 117 simpler patterns covering everything else: navigation (desktop and mobile), sections, cards, carousels, forms and controls, feedback, buttons, backgrounds, animations and transitions, plus full-page scaffolds.

Every module is self-contained. It depends only on `tokens/variables.css`, so you can lift a single pattern into a project without pulling in the rest of the library.

## Directory map

The number in brackets is how many patterns each file holds.

```
web-component-library/
├── CLAUDE.md                    Instructions for Claude sessions that use this repo
├── README.md                    You are here: index and usage rules
├── tokens/
│   └── variables.css            Design variables: color, type, spacing, layout, motion, radius, elevation
├── components/
│   ├── premium/                 20 flagship components, one per file (start here)
│   │   ├── aurora-hero.md            Dark hero: drifting aurora, word-by-word rise, tilting dashboard card
│   │   ├── bento-grid.md             Feature bento with cursor spotlight and one-shot animated stories
│   │   ├── cta-footer.md             Closing CTA, sliding-underline columns, newsletter, rising wordmark
│   │   ├── drag-carousel.md          Full-bleed project carousel: drag + fling, scroll-driven edge fade
│   │   ├── feature-tabs.md           Product tour tabs: spring indicator, assembling mocks, autoplay
│   │   ├── floating-label-form.md    Lead form: floating labels, valid ticks, error slide + shake, morphing submit
│   │   ├── floating-navbar.md        Glass navbar that tightens on scroll, hover pill, circle-reveal menu
│   │   ├── kinetic-headline.md       Word rise, highlighter sweep, underline draw, scroll-lit paragraph
│   │   ├── lightbox-gallery.md       Mosaic gallery; thumbnails morph into a viewer (View Transitions)
│   │   ├── logo-marquee.md           Two-way logo marquee with eased hover slow-down
│   │   ├── morphing-dropdown.md      Stripe-style dropdowns: one background morphs between menus
│   │   ├── premium-buttons.md        Shine, roll, arrow swap, magnetic, loading→success, like burst, glow
│   │   ├── pricing-plans.md          Billing switch, rolling prices, featured plan with tracing border
│   │   ├── scroll-timeline.md        How-it-works timeline whose line fills as you scroll
│   │   ├── smooth-accordion.md       FAQ with interruptible height animation and plus→minus spring
│   │   ├── spring-modal.md           Dialog that springs from its trigger; bottom sheet with drag-to-dismiss
│   │   ├── stat-counters.md          Odometer digits, gradient rules, sparkline, ring and live pulse
│   │   ├── sticky-showcase.md        Apple-style scrollytelling with a pinned, cross-fading device frame
│   │   ├── testimonial-wall.md       Review columns drifting in opposite directions
│   │   └── toast-stack.md            Sonner-style stacked toasts: fan-out, swipe, promise morph
│   ├── animations.md            Scroll reveals, progress bar, parallax, rotating words, skeletons, loaders [9]
│   ├── backgrounds.md           Gradient mesh, patterns, grain, aurora, image scrim, dividers, video [9]
│   ├── buttons.md               Base button system, icon, loading, toggle, segmented, split, FAB, copy [10]
│   ├── card-variants.md         Article, product, horizontal media, image overlay, glass, profile cards [6]
│   ├── cards-and-grids.md       Feature, review and pricing cards on a responsive grid [3]
│   ├── carousels.md             Scroll-snap, testimonials, logo marquee, hero slideshow, thumbnails, ticker [7]
│   ├── content-blocks.md        Feature rows, team, timeline, comparison table, pricing toggle, contact, quote [7]
│   ├── cta-sections.md          CTA band and sticky mobile call/quote bar [2]
│   ├── faq.md                   Accordion on native <details>, zero JS [1]
│   ├── feedback.md              Alerts, toasts, announcement bar, cookie banner, tooltip, chips, progress [8]
│   ├── footer.md                Multi-column footer with legal bar [1]
│   ├── footer-variants.md       Minimal, newsletter, mega, CTA-topped, mobile accordion, wordmark [6]
│   ├── forms.md                 Lead/contact form with inline validation [1]
│   ├── form-controls.md         Switch, checkbox/radio, option cards, input addons, search, password, upload [8]
│   ├── gallery.md               Project photo grid and before/after slider [2]
│   ├── heroes.md                Split-column and centered heroes [2]
│   ├── mobile-navigation.md     Full-screen overlay, tab bar, accordion drawer, bottom sheet, burgers [8]
│   ├── modals.md                Native <dialog> modal with backdrop and animation [1]
│   ├── navbar-variants.md       Transparent, auto-hide, split, dropdown, mega menu, utility, pill [8]
│   ├── navigation.md            Sticky header, hamburger toggle, mobile drawer [1]
│   ├── process-steps.md         Numbered "how it works" steps [1]
│   ├── tabs-and-wayfinding.md   Tabs, breadcrumbs, pagination, stepper, table of contents, back-to-top [7]
│   ├── transitions.md           Page transitions, underline, zoom, flip card, crossfade, ripple, tilt [7]
│   └── trust-and-stats.md       Stats row and certification badge strip [2]
└── templates/
    └── service-landing.md       One-page local service site assembled from the components
```

| Path          | Use it when you need…                                                    |
| ------------- | ------------------------------------------------------------------------ |
| `tokens/`     | Colors, fonts, spacing, widths, transitions, radii or shadows. Always included. |
| `components/` | One UI pattern: a navbar, a hero, a form, a card grid, a footer.         |
| `templates/`  | A complete page: section order, page skeleton and the modules to use.    |

## Usage guidelines

### Pull only the module you need

This library is meant to be referenced piecemeal. Whether you're a developer or an AI assistant working from this repo, load only the module for the task at hand, plus the tokens:

1. Find the module in the directory map above.
2. Read that one file and `tokens/variables.css`. Nothing else. In multi-pattern files, read the pattern table at the top, then only the `## N.` section you need.
3. Don't read, scan or index the whole repository. Modules don't depend on each other, so the rest of the codebase adds noise, not context.

**Example:** to build a pricing section, reference `components/cards-and-grids.md` and `tokens/variables.css` only.

To fetch a single file without cloning:

```
https://raw.githubusercontent.com/bg-guy/web-component-library/main/components/forms.md
```

Templates are the one place where modules combine. A template lists its sections and the module for each. Read the template, then pull each component only when you reach its section.

### Load tokens first

```html
<link rel="stylesheet" href="tokens/variables.css">
<!-- then the CSS from the module you're using -->
```

### Customize with tokens, not literals

Components use `var(--token)` for every color, space, radius, shadow and duration. To restyle, override tokens instead of editing component CSS, either globally in `:root` or scoped to a wrapper:

```css
/* Re-theme one section without touching component code */
.promo {
  --primary: #7c3aed;
  --primary-hover: #6d28d9;
}
```

## Token reference

| Group      | Tokens                                                                                                                       |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Color      | `--primary` `--primary-hover` `--accent` `--surface-light` `--surface-dark` `--surface-muted` `--text-main` `--text-muted` `--text-inverse` `--text-inverse-muted` `--border-subtle` |
| Status     | `--success` `--warning` `--danger` (use `--primary` for info)                                                                |
| Typography | `--font-sans` (system font stack)                                                                                            |
| Spacing    | `--space-xs` (4px) `--space-sm` (8px) `--space-md` (16px) `--space-lg` (24px) `--space-xl` (32px) `--space-2xl` (48px)       |
| Layout     | `--container-max` (1200px) `--gutter` (16px mobile, 32px from 768px) `--gutter-mobile` `--gutter-desktop`                    |
| Motion     | `--transition-fast` (150ms ease) `--transition-smooth` (250ms ease-in-out); both collapse under `prefers-reduced-motion`     |
| Radius     | `--radius-sm` (4px) `--radius-md` (8px) `--radius-lg` (12px) `--radius-full`                                                 |
| Elevation  | `--shadow-sm` `--shadow-md` `--shadow-lg` `--focus-ring`                                                                     |
| Premium: colour | `--primary-2` `--gradient-brand` `--surface-deep` `--border-inverse` `--glass` `--glass-inverse` `--highlight` `--highlight-inverse` |
| Premium: type   | `--font-display` (Geist) `--font-mono` (Geist Mono) `--tracking-tight` `--tracking-display`                         |
| Premium: motion | `--ease-out` `--ease-in-out` `--ease-spring` (real spring via `linear()`) `--dur-1`…`--dur-5` `--stagger`; durations collapse under reduced motion |
| Premium: depth  | `--radius-xl` `--radius-2xl` `--shadow-xl` `--shadow-glow` `--blur-md` `--blur-lg` `--z-sticky` `--z-overlay` `--z-banner` `--z-toast` `--z-popover` |

For the intended premium look, load the fonts once per page:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400..800&family=Geist+Mono:wght@400..600&display=swap">
```

## Adding a module

- One Markdown file per category in `components/`.
  - Single-pattern files use `## HTML`, `## CSS`, `## JS` (if needed) and `## Notes`.
  - Multi-pattern files open with a numbered pattern table, then one self-contained `## N. <Pattern>` section each, with `### HTML/CSS/JS/Notes`.
- Depend only on `tokens/variables.css`. Every class in a pattern starts with that pattern's root class (`.site-header__*`, `.carousel-snap__*`) so modules can be combined without collisions. The one exception is state classes (`is-active`, `is-reached`), which are only ever used together with a component class, e.g. `.feature-tabs__panel.is-active`.
- Premium components live one per file in `components/premium/`. They use the premium tokens for motion (`--ease-spring`, `--dur-*`), so reduced motion is handled at the token level; loops and keyframes still need their own reduced-motion rule.
- No hard-coded colors, spacing, radii or shadows. If a value is missing, add a token.
- Transitions use the motion tokens. Keyframe animations may use literal durations, but every animation must stop under `prefers-reduced-motion`, and anything that moves for more than 5s needs a pause control.
- Build mobile-first with `min-width` queries. 768px is the main breakpoint; add 1024px only when the layout needs it.
- Stacking order for fixed and overlay elements: content 0–5 · nav backdrop 10 · drawers 20 · sticky header 30 · full-screen menus 40 · banners 50 · toasts 60 · tooltips 70 · skip link 100.
- Templates hold only the section order, page skeleton and page-level CSS. They point to component files instead of copying them.
- Keep commentary short. These files are read by people and by AI tools, so every line should earn its place.
- Add every new module to the directory map above and to the table in `CLAUDE.md`.
