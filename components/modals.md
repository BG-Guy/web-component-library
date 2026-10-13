# Modals

Modal dialog built on native `<dialog>` + `showModal()`. Depends on `tokens/variables.css`.

- The browser provides the focus trap, Escape to close, an inert page behind the dialog, and focus return to the opener.
- The close button works without JS (`<form method="dialog">`). The 5-line script opens dialogs and closes them on a backdrop click.
- Fades and rises in where `@starting-style` is supported; elsewhere it opens instantly.

## HTML

Any element with `data-modal-open="{dialog id}"` opens the dialog. Style the trigger with your own button classes.

```html
<button type="button" data-modal-open="quote-modal" aria-haspopup="dialog">Get a quote</button>

<dialog id="quote-modal" class="modal" aria-labelledby="quote-modal-title">
  <div class="modal__panel">
    <div class="modal__header">
      <h2 id="quote-modal-title" class="modal__title">Get a free quote</h2>
      <form method="dialog">
        <button class="modal__close" aria-label="Close">
          <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
            <path d="M6 6l12 12M18 6 6 18" />
          </svg>
        </button>
      </form>
    </div>
    <div class="modal__body">
      <p>Dialog content. For a quote popup, paste the form from <code>components/forms.md</code> here.</p>
    </div>
  </div>
</dialog>
```

## CSS

```css
/* Dialog box: zero padding, so a click that targets the <dialog> itself came from the backdrop */
.modal {
  width: min(32rem, 100% - 2 * var(--gutter)); max-height: 85dvh;
  padding: 0; border: 0; border-radius: var(--radius-lg);
  background: var(--surface-light); color: var(--text-main);
  box-shadow: var(--shadow-lg);
}
.modal::backdrop { background: color-mix(in srgb, var(--surface-dark) 60%, transparent); }

/* Panel: header stays put, body scrolls */
.modal__panel { display: flex; flex-direction: column; max-height: inherit; }
.modal__header {
  display: flex; align-items: center; justify-content: space-between; gap: var(--space-md);
  padding: var(--space-sm) var(--space-sm) var(--space-sm) var(--space-lg);
  border-bottom: 1px solid var(--border-subtle);
}
.modal__title { margin: 0; font-size: 1.25rem; line-height: 1.3; }
.modal__body { overflow-y: auto; padding: var(--space-lg); }
.modal__body > :first-child { margin-top: 0; }
.modal__body > :last-child { margin-bottom: 0; }

/* Close button: 44px target */
.modal__close {
  display: grid; place-items: center; flex: none;
  width: 2.75rem; height: 2.75rem; padding: 0;
  border: 0; border-radius: var(--radius-md);
  background: transparent; color: var(--text-muted); cursor: pointer;
  transition: background-color var(--transition-fast), color var(--transition-fast);
}
.modal__close:hover { background: var(--border-subtle); color: var(--text-main); }
.modal__close:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.modal__close svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; }

/* Lock page scroll while a modal is open */
html:has(.modal:modal) { overflow: hidden; }

/* Enter/exit animation. allow-discrete keeps the dialog in the top layer until the fade ends. */
.modal, .modal::backdrop {
  transition: opacity var(--transition-smooth), translate var(--transition-smooth),
              overlay var(--transition-smooth) allow-discrete, display var(--transition-smooth) allow-discrete;
}
.modal:not([open]), .modal:not([open])::backdrop { opacity: 0; }
.modal:not([open]) { translate: 0 var(--space-md); }
@starting-style {
  .modal[open], .modal[open]::backdrop { opacity: 0; }
  .modal[open] { translate: 0 var(--space-md); }
}
```

## JS

```js
document.addEventListener('click', (e) => {
  const opener = e.target.closest('[data-modal-open]');
  if (opener) document.getElementById(opener.dataset.modalOpen).showModal();
  else if (e.target.matches('dialog.modal[open]')) e.target.close(); // backdrop click
});
```

## Notes

- `showModal()` focuses the first focusable element, which here is the close button. If the dialog holds a form, add `autofocus` to its first field instead.
- Never toggle the `open` attribute directly. That opens a non-modal dialog with no focus trap or backdrop.
- Keep the content `<form>` a sibling of the `<form method="dialog">`, never nested inside it. After a successful fetch submit, call `dialog.close()`.
- Chrome 134+ also supports `closedby="any"` on `<dialog>`, which handles backdrop clicks natively. Keep the script for other browsers.
- For short confirm dialogs, add `aria-describedby` pointing at the message.
- **React:** keep `<dialog>` mounted, open it with `ref.current.showModal()`, and listen for its `close` event to sync state.
- **Tailwind (v4):** the `backdrop:` variant styles `::backdrop`, `open:` targets `[open]`, and `starting:` maps to `@starting-style`.
