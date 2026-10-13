# Web Component Library

A collection of modular, battle-tested UI patterns for marketing and local-service sites, built on a shared set of design tokens. There are 117 patterns: navigation (desktop and mobile), heroes, sections, cards, carousels, forms and controls, feedback, buttons, backgrounds, animations and transitions, plus full-page scaffolds.

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

## Adding a module

- One Markdown file per category in `components/`.
  - Single-pattern files use `## HTML`, `## CSS`, `## JS` (if needed) and `## Notes`.
  - Multi-pattern files open with a numbered pattern table, then one self-contained `## N. <Pattern>` section each, with `### HTML/CSS/JS/Notes`.
- Depend only on `tokens/variables.css`. Every class in a pattern starts with that pattern's root class (`.site-header__*`, `.carousel-snap__*`) so modules can be combined without collisions.
- No hard-coded colors, spacing, radii or shadows. If a value is missing, add a token.
- Transitions use the motion tokens. Keyframe animations may use literal durations, but every animation must stop under `prefers-reduced-motion`, and anything that moves for more than 5s needs a pause control.
- Build mobile-first with `min-width` queries. 768px is the main breakpoint; add 1024px only when the layout needs it.
- Stacking order for fixed and overlay elements: content 0–5 · nav backdrop 10 · drawers 20 · sticky header 30 · full-screen menus 40 · banners 50 · toasts 60 · tooltips 70 · skip link 100.
- Templates hold only the section order, page skeleton and page-level CSS. They point to component files instead of copying them.
- Keep commentary short. These files are read by people and by AI tools, so every line should earn its place.
- Add every new module to the directory map above and to the table in `CLAUDE.md`.
