# Web Component Library

A collection of modular, battle-tested UI patterns for marketing and local-service sites, built on a shared set of design tokens. It covers navigation, heroes, trust signals, cards, process steps, galleries, FAQs, forms, CTAs, modals and footers, plus full-page scaffolds.

Every module is self-contained. It depends only on `tokens/variables.css`, so you can lift a single pattern into a project without pulling in the rest of the library.

## Directory map

```
web-component-library/
├── CLAUDE.md                 Instructions for Claude sessions that use this repo
├── README.md                 You are here: index and usage rules
├── tokens/
│   └── variables.css         Design variables: color, type, spacing, layout, motion, radius, elevation
├── components/
│   ├── cards-and-grids.md    Feature, review and pricing cards on a responsive grid
│   ├── cta-sections.md       CTA band and sticky mobile call/quote bar
│   ├── faq.md                Accordion on native <details>, zero JS
│   ├── footer.md             Multi-column footer with legal bar
│   ├── forms.md              Lead/contact form with inline validation
│   ├── gallery.md            Project photo grid and before/after slider
│   ├── heroes.md             Split-column and centered heroes
│   ├── modals.md             Native <dialog> modal with backdrop and animation
│   ├── navigation.md         Sticky header, hamburger toggle, mobile drawer
│   ├── process-steps.md      Numbered "how it works" steps
│   └── trust-and-stats.md    Stats row and certification badge strip
└── templates/
    └── service-landing.md    One-page local service site assembled from the components
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
2. Read that one file and `tokens/variables.css`. Nothing else.
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
| Color      | `--primary` `--primary-hover` `--accent` `--surface-light` `--surface-dark` `--surface-muted` `--text-main` `--text-muted` `--text-inverse` `--text-inverse-muted` `--border-subtle` `--danger` |
| Typography | `--font-sans` (system font stack)                                                                                            |
| Spacing    | `--space-xs` (4px) `--space-sm` (8px) `--space-md` (16px) `--space-lg` (24px) `--space-xl` (32px) `--space-2xl` (48px)       |
| Layout     | `--container-max` (1200px) `--gutter` (16px mobile, 32px from 768px) `--gutter-mobile` `--gutter-desktop`                    |
| Motion     | `--transition-fast` (150ms ease) `--transition-smooth` (250ms ease-in-out); both collapse under `prefers-reduced-motion`     |
| Radius     | `--radius-sm` (4px) `--radius-md` (8px) `--radius-lg` (12px) `--radius-full`                                                 |
| Elevation  | `--shadow-sm` `--shadow-md` `--shadow-lg` `--focus-ring`                                                                     |

## Adding a module

- One Markdown file per category in `components/`, with `## HTML`, `## CSS`, `## JS` (if needed) and `## Notes` sections, so readers can jump straight to the code.
- Depend only on `tokens/variables.css`. Prefix classes by module (`.site-header__*`, `.hero__*`, `.lead-form__*`) so modules can be combined without collisions.
- No hard-coded colors, spacing, radii, shadows or durations. If a value is missing, add a token.
- Build mobile-first with `min-width` queries. 768px is the main breakpoint; add a second only when the layout needs it (the footer uses 1024px).
- Templates hold only the section order, page skeleton and page-level CSS. They point to component files instead of copying them.
- Keep commentary short. These files are read by people and by AI tools, so every line should earn its place.
- Add every new module to the directory map above and to the table in `CLAUDE.md`.
