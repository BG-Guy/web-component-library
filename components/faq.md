# FAQ

Accordion of questions built on native `<details>`/`<summary>`. Zero JS. Depends on `tokens/variables.css`. Place inside your page container.

- Keyboard support, expanded/collapsed state and find-in-page come from the browser.
- `name="faq"` makes the group exclusive: opening one closes the others. Remove it to allow several open at once.
- Open/close animates where `::details-content` is supported and snaps open elsewhere.

## HTML

```html
<section class="faq" aria-labelledby="faq-title">
  <h2 id="faq-title" class="faq__title">Frequently asked questions</h2>
  <div class="faq__list">
    <details class="faq__item" name="faq" open>
      <summary class="faq__question">Do you charge for estimates?</summary>
      <div class="faq__answer">
        <p>No. Estimates are free, and you get a written flat-rate price before any work starts.</p>
      </div>
    </details>
    <details class="faq__item" name="faq">
      <summary class="faq__question">Are you licensed and insured?</summary>
      <div class="faq__answer">
        <p>Yes. Every technician is licensed, background-checked and covered by our liability insurance.</p>
      </div>
    </details>
    <details class="faq__item" name="faq">
      <summary class="faq__question">How soon can you come out?</summary>
      <div class="faq__answer">
        <p>Most requests get a same-day or next-day slot. Emergency calls are answered 24/7.</p>
      </div>
    </details>
  </div>
</section>
```

## CSS

```css
/* Section and list frame */
.faq { max-width: 48rem; margin-inline: auto; }
.faq__title {
  margin: 0 0 var(--space-lg); text-align: center;
  font-size: clamp(1.5rem, 1rem + 2vw, 2.25rem); line-height: 1.2;
}
.faq__list { border-top: 1px solid var(--border-subtle); }
.faq__item { border-bottom: 1px solid var(--border-subtle); }

/* Question row: full-width click target with a chevron that flips when open */
.faq__question {
  display: flex; align-items: center; justify-content: space-between; gap: var(--space-md);
  min-height: 2.75rem; padding-block: var(--space-md);
  font-size: 1.0625rem; font-weight: 600; color: var(--text-main);
  cursor: pointer; list-style: none;
  transition: color var(--transition-fast);
}
.faq__question::-webkit-details-marker { display: none; } /* Safari's default triangle */
.faq__question::after {
  content: ""; flex: none; width: 0.5rem; height: 0.5rem;
  border: solid var(--text-muted); border-width: 0 2px 2px 0;
  transform: translateY(-25%) rotate(45deg);
  transition: transform var(--transition-smooth);
}
.faq__item[open] > .faq__question::after { transform: translateY(25%) rotate(-135deg); }
.faq__question:hover { color: var(--primary); }
.faq__question:focus-visible {
  outline: 2px solid transparent; box-shadow: var(--focus-ring); border-radius: var(--radius-sm);
}

/* Answer body */
.faq__answer { padding-bottom: var(--space-md); line-height: 1.6; }
.faq__answer > :first-child { margin-top: 0; }
.faq__answer > :last-child { margin-bottom: 0; }

/* Smooth height animation where supported; other browsers open instantly */
@supports selector(::details-content) {
  .faq__item { interpolate-size: allow-keywords; }
  .faq__item::details-content {
    block-size: 0; overflow: clip;
    transition: block-size var(--transition-smooth), content-visibility var(--transition-smooth) allow-discrete;
  }
  .faq__item[open]::details-content { block-size: auto; }
}
```

## Notes

- Each `<summary>` acts as a button, and screen readers announce it as expanded or collapsed. Keep it to plain text: headings inside `<summary>` lose their semantics in some screen readers.
- Exclusive groups (`name`) need Chrome 120+, Safari 17.2+ or Firefox 130+. Older browsers let several stay open, which is harmless.
- Closed answers stay in the page, so Ctrl+F still finds them, and Chromium opens the matching item.
- Write answers that make sense on their own; search results often quote them out of context.
- `FAQPage` JSON-LD is optional. Since 2023, Google shows FAQ rich results only for well-known government and health sites.
- **React:** works as-is (`class` → `className`). Use `open` only for the initial state, and `onToggle` if you need to track it.
- **Tailwind (v4):** `list-none [&::-webkit-details-marker]:hidden` on `<summary>`. Put `group` on `<details>` and `group-open:rotate-180` on an icon.
