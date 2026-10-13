# Process Steps

"How it works" sequence of 3–4 numbered steps. Depends on `tokens/variables.css`. Place inside your page container.

- **<768px:** vertical timeline, with number circles on the left joined by a line.
- **≥768px:** one row, with numbers centered above each step and connectors between them.
- Numbers come from a CSS counter, so adding or reordering steps needs no edits.

## HTML

```html
<ol class="steps" role="list">
  <li class="steps__item">
    <h3 class="steps__title">Request a quote</h3>
    <p class="steps__text">Tell us what you need online or by phone. It takes two minutes.</p>
  </li>
  <li class="steps__item">
    <h3 class="steps__title">Get a fixed price</h3>
    <p class="steps__text">We confirm the details and send a written, flat-rate quote.</p>
  </li>
  <li class="steps__item">
    <h3 class="steps__title">We do the work</h3>
    <p class="steps__text">A licensed pro arrives on time and leaves the space clean.</p>
  </li>
</ol>
```

## CSS

```css
/* List reset + step counter */
.steps { counter-reset: step; display: grid; gap: var(--space-xl); margin: 0; padding: 0; list-style: none; }
.steps__item {
  --dot: 2.5rem; /* number circle size */
  counter-increment: step; position: relative;
  padding-left: calc(var(--dot) + var(--space-md));
}

/* Numbered circle */
.steps__item::before {
  content: counter(step);
  position: absolute; top: 0; left: 0;
  display: grid; place-items: center; width: var(--dot); height: var(--dot);
  border-radius: var(--radius-full); background: var(--primary); color: var(--text-inverse);
  font-weight: 700;
}

/* Vertical connector from this circle down to the next one */
.steps__item:not(:last-child)::after {
  content: ""; position: absolute;
  top: calc(var(--dot) + var(--space-xs)); bottom: calc(var(--space-xs) - var(--space-xl));
  left: calc(var(--dot) / 2 - 1px); width: 2px;
  background: var(--border-subtle);
}

/* Text: title padding centers its first line on the circle */
.steps__title { margin: 0; padding-top: var(--space-sm); font-size: 1.125rem; line-height: 1.3; }
.steps__text { margin: var(--space-xs) 0 0; line-height: 1.6; color: var(--text-muted); }

/* Desktop: one row, circles on top, horizontal connectors across the gaps */
@media (min-width: 768px) {
  .steps { grid-auto-flow: column; grid-auto-columns: minmax(0, 1fr); gap: var(--space-lg); }
  .steps__item { padding: calc(var(--dot) + var(--space-md)) 0 0; text-align: center; }
  .steps__item::before { left: 50%; translate: -50% 0; }
  .steps__item:not(:last-child)::after {
    top: calc(var(--dot) / 2 - 1px); bottom: auto; width: auto; height: 2px;
    left: calc(50% + var(--dot) / 2 + var(--space-sm));
    right: calc(var(--dot) / 2 + var(--space-sm) - 50% - var(--space-lg));
  }
  .steps__title { padding-top: 0; }
}
```

## Notes

- `role="list"` keeps list semantics in Safari after `list-style: none`. Most screen readers read the counter as generated text, so a step is announced as "1 Request a quote".
- Step titles are `<h3>` and assume a section `<h2>` above.
- Three or four steps fit one row at 768px. For five or more, raise the breakpoint so the vertical layout holds longer.
- **React:** map over an array of steps; `class` → `className`.
- **Tailwind:** counters and pseudo-element connectors are awkward as utilities. Keep this CSS as a small component stylesheet next to Tailwind.
