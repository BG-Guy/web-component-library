# Web Component Library

A collection of modular, battle-tested UI patterns for marketing and local-service sites, built on a shared set of design tokens.

- **`components/premium/`**: 100 flagship components with modern design and rich motion, in eleven groups: navigation and menus, heroes, headlines and type, scroll stories, blending sections, content sections, cards and galleries, forms and booking, feedback and utilities, retro styles, and footers. Start here; the [premium index](#premium-index) lists every file.
- **The base library**: 117 simpler patterns covering everything else: navigation (desktop and mobile), sections, cards, carousels, forms and controls, feedback, buttons, backgrounds, animations and transitions, plus full-page scaffolds.

Every module is self-contained. It depends only on `tokens/variables.css`, so you can lift a single pattern into a project without pulling in the rest of the library.

## Live gallery

`docs/index.html` is a single-page gallery with a live preview of every pattern, phone/tablet/full-width toggles and the code for each. It's served by GitHub Pages from the `docs/` folder on `main`. Open it locally in any browser too.

After changing a component, rebuild it from the repo root:

```
python3 tools/gallery/build_gallery.py . tools/gallery/shell.html docs/index.html
```

New premium components also need an entry in `PREMIUM_GROUPS` (and `PREMIUM_FRAME` if they need a fixed-height or phone-width preview) in `tools/gallery/build_gallery.py`.

## Directory map

The number in brackets is how many patterns each file holds.

```
web-component-library/
├── CLAUDE.md                    Instructions for Claude sessions that use this repo
├── README.md                    You are here: index and usage rules
├── docs/index.html              Live gallery of every pattern (GitHub Pages)
├── tools/gallery/               Gallery builder: build_gallery.py + shell.html
├── tokens/
│   └── variables.css            Design variables: color, type, spacing, layout, motion, radius, elevation
├── components/
│   ├── premium/                 100 flagship components, one per file, in 11 groups (start here; see the premium index)
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

## Premium index

Every premium file is one self-contained component in `components/premium/`. Groups match the gallery and the table in `CLAUDE.md`.

**Navigation and menus**
- `floating-navbar.md`: glass navbar that tightens on scroll, hover pill, circle-reveal mobile menu
- `morphing-dropdown.md`: Stripe-style dropdowns; one background morphs between menus
- `split-menu.md`: full-screen menu, numbered links rising from masks, preview pane wiping between links
- `curtain-menu.md`: menu background built from strips that fall like curtain slats
- `perspective-menu.md`: the page tilts back in 3D to reveal the menu beneath
- `gooey-menu.md`: floating action button that oozes call/text/quote bubbles (SVG goo filter)
- `radial-menu.md`: fan of quick actions on an arc, with press-and-drag selection
- `dock-nav.md`: macOS-style magnifying dock as a bottom nav
- `notch-tabbar.md`: bottom tab bar whose active icon rides a liquid notch
- `island-nav.md`: Dynamic Island pill with live status that morphs into a menu card
- `swipe-drawer.md`: side drawer that follows the finger, with fling and rubber-banding
- `drilldown-menu.md`: iOS-settings-style multi-level menu with parallax slides
- `command-palette.md`: ⌘K palette with fuzzy search, grouped results and actions

**Heroes**
- `aurora-hero.md`: dark hero; drifting aurora, word-by-word rise, tilting dashboard card
- `beam-grid-hero.md`: dark technical grid with travelling light beams and a cursor spotlight
- `search-hero.md`: "What needs fixing?" input with typed suggestions and a combobox of services
- `tilted-wall-hero.md`: glass headline card over a 3D wall of scrolling project tiles
- `orbit-hero.md`: services orbiting the brand mark on tilted rings
- `reel-hero.md`: full-bleed photo slideshow with Ken Burns and story-style progress
- `xray-hero.md`: a lens that follows the cursor and reveals the pipes and wiring behind the walls

**Headlines and type**
- `kinetic-headline.md`: word rise, highlighter sweep, underline draw, scroll-lit paragraph
- `scramble-text.md`: headlines and links that decode from random glyphs
- `weight-wave.md`: letters whose weight swells under the cursor (variable Geist)
- `fill-text.md`: outlined statement that fills with the brand gradient line by line on scroll
- `path-text.md`: text ribbons flowing along curved paths as you scroll
- `circle-text.md`: circular text badges: scroll-rotating CTA, seal, scroll cue

**Scroll stories**
- `scroll-timeline.md`: how-it-works timeline whose line fills as you scroll
- `sticky-showcase.md`: Apple-style scrollytelling with a pinned, cross-fading device frame
- `horizontal-scroll.md`: pinned section; vertical scroll drives a row of project panels
- `zoom-through.md`: inset photo opens to full screen as you scroll into it
- `stacking-cards.md`: sticky cards that stack into a deck as the next one slides over
- `text-mask-zoom.md`: fly through a giant cut-out word into the scene behind it
- `wipe-gallery.md`: pinned frame where each photo wipes in with a different clip shape
- `velocity-marquee.md`: huge type rows that speed up, flip and skew with scroll velocity
- `column-parallax.md`: photo columns moving at different speeds around a sticky panel
- `focus-list.md`: giant service list that lights the item crossing the centre
- `depth-tunnel.md`: company milestones flying toward you in 3D
- `scroll-compare.md`: before/after whose divider sweeps with scroll and stays draggable
- `blueprint-draw.md`: house blueprint that draws itself, with callouts popping in
- `parallax-scene.md`: illustrated neighbourhood that goes from dawn to day as the van parks

**Blending sections**
- `chameleon-sections.md`: page colours morph from section to section
- `blend-text.md`: sticky giant wordmark that inverts over every section (`mix-blend-mode`)
- `section-stack.md`: full sections slide over each other like a deck
- `seam-melt.md`: sections dissolve into each other with soft seams, glow and grain
- `liquid-divider.md`: layered wave divider that ripples with scroll
- `curtain-split.md`: cover that slides apart like doors to reveal the section
- `overlap-glass.md`: glass panels straddling two sections, tinted by both
- `card-morph.md`: case-study card that morphs into a detail view (View Transitions)

**Content sections**
- `bento-grid.md`: feature bento with cursor spotlight and one-shot animated stories
- `feature-tabs.md`: product tour tabs: spring indicator, assembling mocks, autoplay
- `stat-counters.md`: odometer digits, gradient rules, sparkline, ring and live pulse
- `pricing-plans.md`: billing switch, rolling prices, featured plan with tracing border
- `smooth-accordion.md`: FAQ with interruptible height animation and plus→minus spring
- `logo-marquee.md`: two-way logo marquee with eased hover slow-down
- `testimonial-wall.md`: review columns drifting in opposite directions

**Cards and galleries**
- `drag-carousel.md`: full-bleed project carousel: drag + fling, scroll-driven edge fade
- `lightbox-gallery.md`: mosaic gallery; thumbnails morph into a viewer (View Transitions)
- `holo-card.md`: membership card with holographic foil, glare, tilt and flip
- `swipe-deck.md`: swipeable stack of review cards with fling
- `expand-panels.md`: row of image panels; the active one springs open
- `hover-preview-list.md`: editorial project list with a cursor-following image preview
- `coverflow.md`: 3D coverflow with reflections, drag and fling
- `wallet-pass.md`: appointment pass that slides out of a wallet and flips
- `hotspot-explorer.md`: house cutaway with hotspots that open anchored popovers
- `crew-cards.md`: team cards with morphing blob portraits and rolling job counts
- `infinite-canvas.md`: gallery canvas you drag in any direction, wrapping endlessly
- `folder-stack.md`: case studies as tabbed folders that shuffle forward

**Forms and booking**
- `floating-label-form.md`: lead form: floating labels, valid ticks, error slide + shake, morphing submit
- `quote-wizard.md`: multi-step estimate with sliding steps and a live price pill
- `booking-calendar.md`: date grid plus time slots, with a confirm button that morphs to a check
- `estimate-calculator.md`: sliders and options driving a rolling total and breakdown bar
- `coverage-checker.md`: ZIP / neighbourhood checker with a map, pin drop and result card
- `job-tracker.md`: "your technician is on the way" map, ETA and stage stepper
- `otp-input.md`: six-digit code with sliding caret, paste ripple and success morph
- `file-drop.md`: photo upload with fanning cards, thumbnails and progress rings
- `star-rating.md`: star rating with a face that morphs from frown to grin

**Feedback and utilities**
- `premium-buttons.md`: shine, roll, arrow swap, magnetic, loading→success, like burst, glow
- `spring-modal.md`: dialog that springs from its trigger; bottom sheet with drag-to-dismiss
- `toast-stack.md`: Sonner-style stacked toasts: fan-out, swipe, promise morph
- `chat-widget.md`: launcher that morphs into a support chat with typing and quick replies
- `confetti.md`: `window.confetti()` bursts in brand colours
- `theme-switch.md`: sun/moon switch with a circular View Transition reveal
- `custom-cursor.md`: dot-and-ring cursor with labels and magnetic targets

**Retro styles**
- `crt-terminal.md`: CRT monitor that boots up and runs real commands
- `pixel-arcade.md`: 8-bit UI: pixel buttons, HP bar, RPG dialog, high scores
- `win95-window.md`: Windows 95 desktop with draggable windows, taskbar and start menu
- `synthwave-hero.md`: outrun hero: striped sun, neon grid, chrome headline
- `vhs-glitch.md`: VHS title card with OSD, tracking bands and RGB split
- `neo-brutalist.md`: thick borders, hard shadows, stickers and pressable cards
- `swiss-poster.md`: International Typographic Style section with a drawn grid
- `groovy-70s.md`: sunburst, wavy stripes and a coupon card, est. 1974
- `skeuo-thermostat.md`: tactile thermostat dial with detents and mode rockers
- `split-flap.md`: Solari departures board announcing availability

**Footers**
- `cta-footer.md`: closing CTA, sliding-underline columns, newsletter, rising wordmark
- `reveal-footer.md`: the page lifts like a sheet to uncover the footer
- `circle-footer.md`: footer floods in through a circle grown from the CTA
- `type-footer.md`: giant wordmark whose letters swell under the cursor
- `unfold-footer.md`: footer unfolds in three paper panels
- `curve-footer.md`: curved page edge that flattens as the footer rises
- `marquee-footer.md`: huge marquee CTA with a magnetic button, hours and back-to-top ring

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
- Premium components live one per file in `components/premium/`: a title, a short description, a `**Motion:**` line, an optional `**Fonts:**` line (any Google Font beyond Geist, with its URL), then `## HTML`, `## CSS`, `## JS` and `## Notes`. Every class, custom property, keyframe and id starts with the component's root. They use the premium tokens for motion (`--ease-spring`, `--dur-*`), so reduced motion is handled at the token level; loops and keyframes still need their own reduced-motion rule.
- No hard-coded colors, spacing, radii or shadows. If a value is missing, add a token. The one exception is themed premium components (retro styles, holographic foil): they may declare a local palette as `--root-*` custom properties on their root and use only those variables.
- Transitions use the motion tokens. Keyframe animations may use literal durations, but every animation must stop under `prefers-reduced-motion`, and anything that moves for more than 5s needs a pause control.
- Build mobile-first with `min-width` queries. 768px is the main breakpoint; add 1024px only when the layout needs it.
- Stacking order for fixed and overlay elements: content 0–5 · nav backdrop 10 · drawers 20 · sticky header 30 · full-screen menus 40 · banners 50 · toasts 60 · tooltips 70 · skip link 100.
- Templates hold only the section order, page skeleton and page-level CSS. They point to component files instead of copying them.
- Keep commentary short. These files are read by people and by AI tools, so every line should earn its place.
- Add every new module to the directory map above (premium components go in the premium index) and to the table in `CLAUDE.md`.
