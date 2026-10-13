# CLAUDE.md

## Role and purpose

You are a frontend architect with direct access to this curated component library. Its modules are your primary blueprint and source of truth when designing pages. Start from the matching pattern and adapt it. Don't invent a new pattern when one already exists here.

## Progressive disclosure

Never load or scan all component files upfront. Read only what the current task needs:

| Task                                   | Read                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| Any output                             | `tokens/variables.css`                                       |
| Header, menu, mobile drawer            | `components/navigation.md`                                   |
| Hero / above-the-fold section          | `components/heroes.md`                                       |
| Stats, trust badges, certifications    | `components/trust-and-stats.md`                              |
| Feature, review or pricing cards       | `components/cards-and-grids.md`                              |
| "How it works" / process steps         | `components/process-steps.md`                                |
| Project photos, before/after slider    | `components/gallery.md`                                      |
| FAQ / accordion                        | `components/faq.md`                                          |
| Contact or lead form                   | `components/forms.md`                                        |
| CTA band, sticky mobile call bar       | `components/cta-sections.md`                                 |
| Modal / popup dialog                   | `components/modals.md`                                       |
| Footer                                 | `components/footer.md`                                       |
| Full landing page for a service business | `templates/service-landing.md`, then only the components it lists |

- For a full page, start from the closest template's section order, then work section by section. Open each component file only when you reach that section.
- Don't glob, grep or list the repo for context. This table is the index. Open `README.md` only if the table doesn't cover the request.
- Inside a component file, go straight to the section you need: `## HTML`, `## CSS`, `## JS`, `## Notes` or `## Adapting`.

## Execution constraints

- Do NOT run automated test suites, headless browser verification or package audits unless explicitly asked.
- Deliver in a single pass. Output self-contained HTML/CSS/JS (one file, with tokens inlined or linked), or a framework-specific component (React/JSX, Vue, Svelte, Tailwind) when one is requested.
- Keep the design tokens from `tokens/variables.css`. Style with `var(--token)`. Don't hard-code colors, spacing, radii, shadows or durations; if a value is missing, add a token.
- When adapting a module, keep its accessibility wiring intact: labels, `aria-*` attributes, focus handling and keyboard support.

## Quality bar

- **Fast loads:** HTML and CSS first. No frameworks or libraries unless asked. Give every image `width`/`height`, lazy-load below the fold, and never lazy-load the hero image.
- **No JavaScript bloat:** use vanilla JS only for behavior CSS can't handle. No jQuery, animation libraries or icon fonts; use inline SVG.
- **Clean breakpoints:** mobile-first `min-width` queries, with 768px as the main breakpoint. No horizontal scroll at 320px wide.
- **Accessibility (WCAG 2.2 AA):** semantic landmarks, one `<h1>` per page, labelled controls, visible focus (`--focus-ring`), 4.5:1 text contrast, 24px minimum target size, and `prefers-reduced-motion` respected (the motion tokens handle this).
