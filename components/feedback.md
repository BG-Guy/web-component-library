# Feedback & Status

Inline alerts, toasts, announcement and cookie bars, tooltips, chips, progress indicators and empty states. Depends on `tokens/variables.css`.

| #  | Pattern                                                                                   | JS        |
| -- | ----------------------------------------------------------------------------------------- | --------- |
| 1  | **Alert banners**: info/success/warning/error messages with icon, title, optional dismiss | ~9 lines  |
| 2  | **Toast notifications**: polite live region fed by `showToast()`, auto-dismiss after 5s  | ~24 lines |
| 3  | **Announcement bar**: dismissible promo strip above the header, remembered with no flash  | ~11 lines |
| 4  | **Cookie consent banner**: non-blocking bottom bar with equal Accept and Reject           | ~16 lines |
| 5  | **Tooltip**: short hint on hover and focus, Escape to dismiss, kept inside the viewport    | ~18 lines |
| 6  | **Chips & tags**: tags, status pills and removable filter chips                           | ~12 lines |
| 7  | **Progress**: styled native `<progress>` bar and an SVG progress ring                     | ~8 lines (optional) |
| 8  | **Empty state**: icon, heading, helper text and one primary action                        | none      |

## 1. Alert banners

Inline messages in four tones. Each tone has its own icon shape and a hidden tone word ("Error:") in the title, so color is never the only cue. Text stays `--text-main` on the tint; the tone color only draws the icon and edge. Place inside your page container.

### HTML

```html
<!-- Static alert, rendered with the page: no role -->
<div class="alert alert--info">
  <svg class="alert__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>
  <div class="alert__body">
    <p class="alert__title"><span class="alert__sr">Info: </span>Holiday hours</p>
    <p class="alert__text">We're closed Nov 27–28. Emergency repairs are still available at <a href="tel:+15555550123">(555) 555-0123</a>.</p>
  </div>
  <!-- Optional dismiss: hidden until the script can make it work -->
  <button class="alert__close" type="button" aria-label="Dismiss message" hidden>
    <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg>
  </button>
</div>

<div class="alert alert--success">
  <svg class="alert__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/></svg>
  <div class="alert__body">
    <p class="alert__title"><span class="alert__sr">Success: </span>Request received</p>
    <p class="alert__text">We'll call you within one business day to confirm a time.</p>
  </div>
</div>

<div class="alert alert--warning">
  <svg class="alert__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 3 2 20h20Z"/><path d="M12 10v4M12 17h.01"/></svg>
  <div class="alert__body">
    <p class="alert__title"><span class="alert__sr">Warning: </span>Storm delays possible</p>
    <p class="alert__text">Outdoor jobs this week may move by a day. We'll text you if yours does.</p>
  </div>
</div>

<!-- Urgent error your script inserts after a failed submit: role="alert" -->
<div class="alert alert--danger" role="alert">
  <svg class="alert__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="m9 9 6 6m0-6-6 6"/></svg>
  <div class="alert__body">
    <p class="alert__title"><span class="alert__sr">Error: </span>We couldn't send your request</p>
    <p class="alert__text">Check your connection and try again, or call <a href="tel:+15555550123">(555) 555-0123</a>.</p>
  </div>
</div>
```

### CSS

```css
/* Base: tinted surface with a tone edge; --alert-tone drives every variant */
.alert {
  --alert-tone: var(--primary);
  display: flex; align-items: flex-start; gap: var(--space-sm);
  padding: var(--space-md);
  border: 1px solid color-mix(in srgb, var(--alert-tone) 30%, var(--surface-light));
  border-inline-start: 4px solid var(--alert-tone);
  border-radius: var(--radius-md);
  background: color-mix(in srgb, var(--alert-tone) 8%, var(--surface-light));
  color: var(--text-main); font-family: var(--font-sans); line-height: 1.5;
}
.alert--success { --alert-tone: var(--success); }
.alert--warning { --alert-tone: var(--warning); }
.alert--danger { --alert-tone: var(--danger); }

/* Icon carries the tone (3:1+ on the tint); all text stays --text-main (12.5:1+) */
.alert__icon {
  flex: none; width: 1.5rem; height: 1.5rem; color: var(--alert-tone);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.alert__body { flex: 1; min-width: 0; overflow-wrap: anywhere; }
.alert__title { margin: 0; font-weight: 600; }
.alert__text { margin: var(--space-xs) 0 0; font-size: 0.9375rem; }
.alert__text a { color: inherit; text-decoration: underline; }

/* Dismiss: 32px target. No display set, so the hidden attribute keeps working */
.alert__close {
  flex: none; width: 2rem; height: 2rem; margin: calc(-1 * var(--space-xs));
  padding: 0; border: 0; border-radius: var(--radius-sm);
  background: transparent; color: var(--text-main); cursor: pointer;
  transition: background-color var(--transition-fast);
}
.alert__close svg {
  display: block; width: 1.25rem; height: 1.25rem; margin: auto;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round;
}
.alert__close:hover { background: color-mix(in srgb, var(--alert-tone) 15%, var(--surface-light)); }
.alert__close:focus-visible,
.alert a:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Visually hidden tone word */
.alert__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}
```

### JS

```js
// Reveal dismiss buttons now that they work
document.querySelectorAll('.alert__close').forEach((btn) => { btn.hidden = false; });

// Remove the alert, then park focus on its container so it doesn't fall back to <body>
document.addEventListener('click', (e) => {
  const alert = e.target.closest('.alert__close')?.closest('.alert');
  if (!alert) return;
  const parent = alert.parentElement;
  alert.remove();
  if (!parent.hasAttribute('tabindex')) parent.tabIndex = -1;
  parent.focus({ preventScroll: true });
});
```

### Notes

- **Which role:** no role for alerts rendered with the page; they're read in normal order. Use `role="alert"` only for urgent messages your script inserts after an action, like a failed submit. It interrupts the screen reader, so never put it on page-load content or on several alerts at once. Use `role="status"` for non-urgent updates ("Saved"). Its container must already be in the DOM before the text changes.
- Tone is conveyed by icon shape, the hidden tone word and the wording. Tone colors on the tint are only ~4.3:1, so they're limited to the icon and edge (3:1 needed for graphics).
- Don't let people dismiss an error that still applies. For field errors, also link the message to the input with `aria-describedby` (`components/forms.md`).
- `color-mix()` tints need Chrome 111, Safari 16.2 or Firefox 113. Older browsers drop the tint but keep the tone edge and icon.

## 2. Toast notifications

Short, non-blocking confirmations. One live region (`role="status"`, polite) is in the HTML from page load, and `showToast()` appends messages to it. Bottom-center on phones, bottom-right from 768px, clear of the home indicator. Each toast auto-dismisses after 5s, paused while hovered or focused.

### HTML

```html
<!-- Once, just before </body>. It must exist (empty) at page load so screen readers track it -->
<div class="toast" role="status" aria-live="polite" aria-atomic="false"></div>
```

### CSS

```css
/* Region: bottom-center on phones, above the home indicator; empty space never blocks clicks */
.toast {
  position: fixed; z-index: 60;
  left: calc(var(--space-md) + env(safe-area-inset-left, 0px));
  right: calc(var(--space-md) + env(safe-area-inset-right, 0px));
  bottom: calc(var(--space-md) + env(safe-area-inset-bottom, 0px));
  display: flex; flex-direction: column; align-items: center; gap: var(--space-sm);
  pointer-events: none;
}
/* Bottom-right from 768px */
@media (min-width: 768px) {
  .toast {
    left: auto; width: 24rem;
    right: calc(var(--space-lg) + env(safe-area-inset-right, 0px));
    bottom: calc(var(--space-lg) + env(safe-area-inset-bottom, 0px));
  }
}

/* Toast card: tint, tone edge and tone icon (a CSS mask), text stays --text-main */
.toast__item {
  --toast-tone: var(--primary);
  --toast-icon: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='9'/%3E%3Cpath d='M12 11v5M12 8h.01'/%3E%3C/svg%3E");
  box-sizing: border-box; width: 100%; max-width: 24rem;
  display: flex; align-items: center; gap: var(--space-sm);
  padding: var(--space-sm) var(--space-sm) var(--space-sm) var(--space-md);
  border: 1px solid color-mix(in srgb, var(--toast-tone) 30%, var(--surface-light));
  border-inline-start: 4px solid var(--toast-tone);
  border-radius: var(--radius-md);
  background: color-mix(in srgb, var(--toast-tone) 8%, var(--surface-light));
  color: var(--text-main); box-shadow: var(--shadow-lg);
  font-family: var(--font-sans); font-size: 0.9375rem; line-height: 1.4;
  pointer-events: auto;
  transition: opacity var(--transition-smooth), translate var(--transition-smooth);
}
.toast__item::before {
  content: ""; flex: none; width: 1.25rem; height: 1.25rem; background: var(--toast-tone);
  -webkit-mask: var(--toast-icon) center / contain no-repeat;
  mask: var(--toast-icon) center / contain no-repeat;
}
.toast__item--success {
  --toast-tone: var(--success);
  --toast-icon: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='9'/%3E%3Cpath d='m8 12 3 3 5-6'/%3E%3C/svg%3E");
}
.toast__item--warning {
  --toast-tone: var(--warning);
  --toast-icon: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 3 2 20h20ZM12 10v4M12 17h.01'/%3E%3C/svg%3E");
}
.toast__item--danger {
  --toast-tone: var(--danger);
  --toast-icon: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='9'/%3E%3Cpath d='m9 9 6 6m0-6-6 6'/%3E%3C/svg%3E");
}

/* Enter from below; the script adds --out to exit. Both become instant under reduced motion */
@starting-style {
  .toast__item { opacity: 0; translate: 0 var(--space-sm); }
}
.toast__item--out { opacity: 0; translate: 0 var(--space-sm); }

.toast__msg { flex: 1; min-width: 0; margin: 0; overflow-wrap: anywhere; }
.toast__close {
  flex: none; width: 2rem; height: 2rem; padding: 0; border: 0; border-radius: var(--radius-sm);
  background: transparent; color: var(--text-main); cursor: pointer;
  transition: background-color var(--transition-fast);
}
.toast__close svg {
  display: block; width: 1.25rem; height: 1.25rem; margin: auto;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round;
}
.toast__close:hover { background: color-mix(in srgb, var(--toast-tone) 15%, var(--surface-light)); }
.toast__close:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
```

### JS

```js
// Toasts: append to the live region, auto-dismiss after 5s, pause while hovered or focused
const region = document.querySelector('.toast');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

function dismiss(item) {
  clearTimeout(item.timer);
  if (reduce.matches) return item.remove();
  item.classList.add('toast__item--out');
  // Remove once the exit transition finishes (right away if there is none)
  Promise.allSettled(item.getAnimations().map((a) => a.finished)).then(() => item.remove());
}

export function showToast(message, tone = 'info') {
  const item = document.createElement('div');
  item.className = `toast__item toast__item--${tone}`;
  item.innerHTML = '<p class="toast__msg"></p><button class="toast__close" type="button" aria-label="Dismiss"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg></button>';
  item.firstChild.textContent = message; // textContent: message is never parsed as HTML
  item.lastChild.addEventListener('click', () => dismiss(item));
  // When the timer fires while the pointer or focus is still on the toast, re-arm instead
  const arm = () => {
    clearTimeout(item.timer);
    item.timer = setTimeout(() => (item.matches(':hover, :focus-within') ? arm() : dismiss(item)), 5000);
  };
  ['mouseenter', 'focusin'].forEach((type) => item.addEventListener(type, () => clearTimeout(item.timer)));
  ['mouseleave', 'focusout'].forEach((type) => item.addEventListener(type, arm));
  region.append(item);
  arm();
  return item;
}

// Usage: showToast("Thanks! We'll call you within one business day.", 'success');
```

### Notes

- Keep the region in the HTML from page load: live regions created along with their content are often not announced. `role="status"` is polite and waits for the screen reader to finish. `aria-atomic="false"` reads only the new toast, not every toast still on screen.
- Toasts time out and never take focus, so use them only for confirmations. Errors that need action, links and "Undo" belong in an alert (pattern 1) near the cause (WCAG 2.2.1). Write each message so it makes sense without its tone.
- Put the script in its own module (e.g. `toast.js`) and `import { showToast } from './toast.js'` where needed. Unknown tones fall back to info styling.
- `@starting-style` (Chrome 117, Safari 17.5, Firefox 129) animates the entrance; older browsers show toasts instantly. If the page has the sticky mobile call bar (`components/cta-sections.md`), raise `.toast`'s `bottom` by its height on phones.
- **React:** mount the region once at the app root and render toasts from state inside it. Never mount the region conditionally.

## 3. Announcement bar

A slim promo strip above the site header. The close button hides it and stores the dismissed promo's ID in `localStorage`. A tiny inline script in `<head>` hides it before first paint on later visits, so there's no flash or layout shift. Full-bleed, with its own inner wrapper.

### HTML

```html
<!-- Near the top of <head>: a classic (not module) inline script, so it runs before first paint.
     Keep the ID in sync with data-announce-id below. -->
<script>
  try { if (localStorage.getItem('announce-dismissed') === 'spring-2026') document.documentElement.classList.add('announce--dismissed'); } catch (e) {}
</script>

<!-- After the skip link, before the site header -->
<aside class="announce" aria-label="Announcement" data-announce-id="spring-2026">
  <div class="announce__inner">
    <p class="announce__text">Spring tune-up: 15% off AC service through May 31. <a class="announce__link" href="https://example.com/offers">See the offer</a></p>
    <!-- Hidden until the script can make it work -->
    <button class="announce__close" type="button" aria-label="Dismiss announcement" hidden>
      <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg>
    </button>
  </div>
</aside>
```

### CSS

```css
/* Full-bleed dark strip; the inner wrapper keeps content on the page grid */
.announce { background: var(--surface-dark); color: var(--text-inverse); font-family: var(--font-sans); }
.announce__inner {
  display: flex; align-items: center; gap: var(--space-sm);
  max-width: var(--container-max); margin-inline: auto;
  padding: var(--space-xs) var(--gutter);
}
.announce__text { flex: 1; min-width: 0; margin: 0; padding-block: var(--space-xs); font-size: 0.875rem; line-height: 1.5; }
.announce__link { color: var(--text-inverse); font-weight: 600; text-decoration: underline; }

/* Close: 40px target. No display set, so the hidden attribute keeps working */
.announce__close {
  flex: none; width: 2.5rem; height: 2.5rem; padding: 0; border: 0; border-radius: var(--radius-md);
  background: transparent; color: var(--text-inverse); cursor: pointer;
  transition: background-color var(--transition-fast);
}
.announce__close svg {
  display: block; width: 1.25rem; height: 1.25rem; margin: auto;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round;
}
.announce__close:hover { background: color-mix(in srgb, var(--text-inverse) 12%, var(--surface-dark)); }

/* Focus on a dark surface */
.announce__link:focus-visible,
.announce__close:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }

/* Centered from 768px; the start padding balances the close button */
@media (min-width: 768px) {
  .announce__text { text-align: center; padding-inline-start: 2.5rem; }
}

/* Optional: pin it. Then set the sticky header's top to the bar's height */
.announce--sticky { position: sticky; top: 0; z-index: 50; }

/* Set on <html> by the head snippet: hidden before first paint */
.announce--dismissed .announce { display: none; }
```

### JS

```js
// Reveal the close button; on click hide the bar and remember this promo. Storage may be blocked
const KEY = 'announce-dismissed';
document.querySelectorAll('.announce').forEach((bar) => {
  const id = bar.dataset.announceId;
  try { if (localStorage.getItem(KEY) === id) bar.hidden = true; } catch {} // fallback if the head snippet is missing
  const close = bar.querySelector('.announce__close');
  close.hidden = false;
  close.addEventListener('click', () => {
    bar.hidden = true;
    try { localStorage.setItem(KEY, id); } catch {}
  });
});
```

### Notes

- The head snippet is the one deliberate classic inline script. Module scripts run after parsing, too late to stop the flash. Under a strict CSP, allow it with a nonce or hash.
- Change the ID in both places for each new promo, so people who closed the old one still see the new one.
- `<aside aria-label>` makes it a named landmark; keep the skip link first in the DOM. Dismissal uses `hidden`, which also removes it from the tab order and accessibility tree.
- Text on `--surface-dark` is `--text-inverse` (17:1), and the link is underlined, not marked by color alone.

## 4. Cookie consent banner

A non-modal bar fixed to the bottom. Reject and Accept share one button style, so neither is pushed. It doesn't trap focus or block the page, and while it's open the page gets bottom padding so it never covers focused content (WCAG 2.4.11). It starts `hidden`; the script shows it only when no choice is stored.

### HTML

```html
<!-- Right after the skip link, so keyboard and screen-reader users reach it first. Visually fixed to the bottom -->
<section class="cookie-banner" aria-label="Cookie consent" hidden>
  <div class="cookie-banner__inner">
    <p class="cookie-banner__text">
      We use optional cookies to measure traffic and improve our service. Essential cookies are always on.
      <a class="cookie-banner__link" href="https://example.com/cookie-settings">Manage preferences</a>
    </p>
    <div class="cookie-banner__actions">
      <button class="cookie-banner__btn" type="button" data-consent="rejected">Reject all</button>
      <button class="cookie-banner__btn" type="button" data-consent="accepted">Accept all</button>
    </div>
  </div>
</section>
```

### CSS

```css
/* Non-modal bar fixed to the bottom, clear of the home indicator */
.cookie-banner {
  position: fixed; z-index: 50; left: 0; right: 0; bottom: 0;
  padding-bottom: env(safe-area-inset-bottom, 0px);
  border-top: 1px solid var(--border-subtle);
  background: var(--surface-light); color: var(--text-main);
  box-shadow: var(--shadow-lg); font-family: var(--font-sans);
}
.cookie-banner__inner {
  display: flex; flex-direction: column; gap: var(--space-md);
  max-width: var(--container-max); margin-inline: auto;
  padding: var(--space-md) var(--gutter);
}
.cookie-banner__text { margin: 0; font-size: 0.9375rem; line-height: 1.5; }
.cookie-banner__link { color: var(--primary); font-weight: 600; text-decoration: underline; }

/* Equal weight: one style and one size for both choices */
.cookie-banner__actions { display: flex; gap: var(--space-sm); }
.cookie-banner__btn {
  flex: 1; min-height: 2.75rem; padding: 0 var(--space-lg);
  border: 0; border-radius: var(--radius-md);
  background: var(--primary); color: var(--text-inverse);
  font: inherit; font-weight: 600; white-space: nowrap; cursor: pointer;
  transition: background-color var(--transition-fast);
}
.cookie-banner__btn:hover { background: var(--primary-hover); }
.cookie-banner__link:focus-visible,
.cookie-banner__btn:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Text and buttons side by side from 768px */
@media (min-width: 768px) {
  .cookie-banner__inner { flex-direction: row; align-items: center; justify-content: space-between; gap: var(--space-xl); }
  .cookie-banner__btn { flex: none; min-width: 9rem; }
}

/* While open, pad the page by the banner's height so it can't hide content or focus */
html:has(.cookie-banner:not([hidden])) { scroll-padding-bottom: var(--cookie-banner-h, 0px); }
body:has(.cookie-banner:not([hidden])) { padding-bottom: var(--cookie-banner-h, 0px); }
```

### JS

```js
// Show the banner only when no choice is stored; on click save, hide and notify the page
const KEY = 'cookie-consent';
const root = document.documentElement;
document.querySelectorAll('.cookie-banner').forEach((banner) => {
  let saved = null;
  try { saved = localStorage.getItem(KEY); } catch {}
  if (saved) return;
  banner.hidden = false;
  // Feed the banner's live height to the page padding above
  new ResizeObserver(() => root.style.setProperty('--cookie-banner-h', `${banner.offsetHeight}px`)).observe(banner);
  banner.addEventListener('click', (e) => {
    const choice = e.target.closest('[data-consent]')?.dataset.consent;
    if (!choice) return;
    try { localStorage.setItem(KEY, choice); } catch {}
    banner.hidden = true;
    document.dispatchEvent(new CustomEvent('cookie-consent', { detail: choice }));
  });
});
```

### Notes

- Legal requirements vary by region (GDPR/ePrivacy, US state privacy laws), so have the wording and behavior reviewed. This banner only records a choice: it doesn't load, block or delete any scripts or cookies. Load analytics only after `accepted`: listen for the `cookie-consent` event, or read the key on later page loads.
- Keep both buttons on the same class. Making Accept bolder, or turning Reject into a link, is a dark pattern that regulators flag.
- "Manage preferences" points to a settings page; you can open it in a `components/modals.md` dialog instead. Add a footer link that clears the key, so people can change their choice later.
- It's not a dialog: no backdrop, no focus trap, and the page stays usable. The `:has()` padding needs Chrome 105, Safari 15.4 or Firefox 121; older browsers let the banner overlap the page bottom. Without JS it stays hidden.

## 5. Tooltip

A short, non-interactive hint for a button or link, wired with `aria-describedby`. It opens on hover and keyboard focus, stays open while the pointer moves onto it, and Escape hides it without moving focus or the pointer (WCAG 1.4.13). It sits above the trigger, and the script nudges it back inside the viewport. Place inside your page container.

### HTML

```html
<!-- Icon button: aria-label names it, the tooltip describes it -->
<p>
  Service call: $89
  <span class="tooltip">
    <button class="tooltip__trigger" type="button" aria-label="About the service call fee" aria-describedby="tip-fee">
      <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>
    </button>
    <span class="tooltip__bubble" id="tip-fee" role="tooltip">Waived when you book the repair.</span>
  </span>
</p>

<!-- Text link trigger; add tooltip--below for triggers near the top of the viewport -->
<span class="tooltip">
  <a class="tooltip__link" href="https://example.com/warranty" aria-describedby="tip-warranty">2-year warranty</a>
  <span class="tooltip__bubble" id="tip-warranty" role="tooltip">Parts and labor on every install.</span>
</span>
```

### CSS

```css
/* Wrapper anchors the bubble */
.tooltip { position: relative; display: inline-block; }

/* Bubble: above the trigger, short and narrow enough for 320px. --tooltip-shift comes from JS */
.tooltip__bubble {
  position: absolute; z-index: 70; bottom: calc(100% + var(--space-sm)); left: 50%;
  translate: calc(-50% + var(--tooltip-shift, 0px)) 0;
  display: none;
  width: max-content; max-width: min(15rem, calc(100vw - var(--space-xl)));
  padding: var(--space-xs) var(--space-sm); border-radius: var(--radius-sm);
  background: var(--surface-dark); color: var(--text-inverse); box-shadow: var(--shadow-md);
  font-family: var(--font-sans); font-size: 0.875rem; font-weight: 400; line-height: 1.4;
  text-align: center; white-space: normal;
}
/* Invisible bridge over the gap, so the pointer can move onto the bubble */
.tooltip__bubble::after { content: ""; position: absolute; left: 0; right: 0; top: 100%; height: var(--space-sm); }

/* Show on hover and focus; Escape adds --dismissed until the next hover or focus */
.tooltip:hover .tooltip__bubble,
.tooltip:focus-within .tooltip__bubble { display: block; }
.tooltip.tooltip--dismissed .tooltip__bubble { display: none; }

/* Optional: open below the trigger */
.tooltip--below .tooltip__bubble { bottom: auto; top: calc(100% + var(--space-sm)); }
.tooltip--below .tooltip__bubble::after { top: auto; bottom: 100%; }

/* Triggers: 24px icon button, or a plain link */
.tooltip__trigger {
  width: 1.5rem; height: 1.5rem; padding: 0; border: 0; border-radius: var(--radius-full);
  background: transparent; color: var(--text-muted); cursor: help; vertical-align: middle;
  transition: color var(--transition-fast);
}
.tooltip__trigger svg {
  display: block; width: 1.25rem; height: 1.25rem; margin: auto;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round;
}
.tooltip__trigger:hover { color: var(--text-main); }
.tooltip__link { color: var(--primary); text-decoration: underline; }
.tooltip__trigger:focus-visible,
.tooltip__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
```

### JS

```js
// Escape hides any open tooltip without moving focus or the pointer (WCAG 1.4.13)
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') document.querySelectorAll('.tooltip').forEach((t) => t.classList.add('tooltip--dismissed'));
});

// On hover/focus: re-enable, then shift the bubble back inside the viewport (8px margin)
document.querySelectorAll('.tooltip').forEach((tip) => {
  const bubble = tip.querySelector('.tooltip__bubble');
  const open = () => {
    tip.classList.remove('tooltip--dismissed');
    requestAnimationFrame(() => {
      bubble.style.setProperty('--tooltip-shift', '0px');
      const { left, right, width } = bubble.getBoundingClientRect();
      if (!width) return; // already closed again
      const edge = 8, max = document.documentElement.clientWidth - edge;
      bubble.style.setProperty('--tooltip-shift', `${Math.max(edge - left, 0) + Math.min(max - right, 0)}px`);
    });
  };
  tip.addEventListener('mouseenter', open);
  tip.addEventListener('focusin', open);
});
```

### Notes

- Keep hints to one short sentence, with nothing interactive inside: keyboard users can't reach content in a tooltip. For links, rich content or must-read info, use a disclosure or a `popover` toggletip instead.
- `aria-describedby` still works while the bubble is `display: none`, so screen readers read the hint on focus. Icon-only triggers still need their own `aria-label`: the tooltip describes the trigger, it doesn't name it.
- On touch, a tap focuses the trigger and shows the bubble. Don't rely on tooltips for anything touch users must see.
- Without JS, hover and focus still work, but Escape and edge correction don't. Keep triggers away from the screen edges or use `tooltip--below`.
- Optional enhancement: CSS anchor positioning (Chromium 125+, Safari 26, not yet everywhere). Inside `@supports (position-anchor: --a)`, anchor the bubble to the trigger and add `position-try-fallbacks: flip-block` to flip it below automatically. Keep this version as the default.

## 6. Chips & tags

Compact labels: neutral tags, status pills in four tones, and removable filter chips. Text stays `--text-main` on the tint. Status pills add a tone dot, but the word carries the meaning. Remove buttons are 24px targets labelled "Remove <name>", and after a removal focus moves to the next chip, else the previous one, else the list. Place inside your page container.

### HTML

```html
<!-- Tags -->
<ul class="chip__group" role="list" aria-label="Services">
  <li class="chip">Plumbing</li>
  <li class="chip">Water heaters</li>
  <li class="chip">24/7 emergency</li>
</ul>

<!-- Status pills: inline, e.g. in a job list or table cell -->
<span class="chip">Draft</span>
<span class="chip chip--info">Scheduled</span>
<span class="chip chip--success">Completed</span>
<span class="chip chip--warning">Awaiting parts</span>
<span class="chip chip--danger">Overdue</span>

<!-- Removable filter chips: remove buttons stay hidden until the script runs -->
<p class="chip__label" id="filters-label">Active filters</p>
<ul class="chip__group" role="list" aria-labelledby="filters-label">
  <li class="chip chip--filter" data-value="water-heaters">
    Water heaters
    <button class="chip__remove" type="button" aria-label="Remove Water heaters" hidden>
      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg>
    </button>
  </li>
  <li class="chip chip--filter" data-value="under-500">
    Under $500
    <button class="chip__remove" type="button" aria-label="Remove Under $500" hidden>
      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg>
    </button>
  </li>
</ul>
```

### CSS

```css
/* Group: wrapping row of chips */
.chip__group { display: flex; flex-wrap: wrap; gap: var(--space-sm); margin: 0; padding: 0; list-style: none; }
.chip__label { margin: 0 0 var(--space-sm); font-size: 0.875rem; font-weight: 600; color: var(--text-main); }

/* Chip: tinted pill. --chip-tone drives the tint, border and dot; text stays --text-main (12.5:1+) */
.chip {
  --chip-tone: var(--text-muted);
  box-sizing: border-box; display: inline-flex; align-items: center; gap: var(--space-xs);
  max-width: 100%; min-height: 1.75rem; padding: 0 var(--space-sm);
  border: 1px solid color-mix(in srgb, var(--chip-tone) 30%, var(--surface-light));
  border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--chip-tone) 10%, var(--surface-light));
  color: var(--text-main); font-family: var(--font-sans);
  font-size: 0.875rem; font-weight: 500; line-height: 1.25; overflow-wrap: anywhere; vertical-align: middle;
}
.chip--info { --chip-tone: var(--primary); }
.chip--success { --chip-tone: var(--success); }
.chip--warning { --chip-tone: var(--warning); }
.chip--danger { --chip-tone: var(--danger); }

/* Status dot: decorative, the word carries the meaning */
.chip:is(.chip--info, .chip--success, .chip--warning, .chip--danger)::before {
  content: ""; flex: none; width: 0.5rem; height: 0.5rem;
  border-radius: var(--radius-full); background: var(--chip-tone);
}

/* Filter chip: 24px remove button. No display set, so the hidden attribute keeps working */
.chip--filter { padding-inline-end: var(--space-xs); }
.chip__remove {
  flex: none; width: 1.5rem; height: 1.5rem; padding: 0; border: 0; border-radius: var(--radius-full);
  background: transparent; color: var(--text-main); cursor: pointer;
  transition: background-color var(--transition-fast);
}
.chip__remove svg {
  display: block; width: 1rem; height: 1rem; margin: auto;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round;
}
.chip__remove:hover { background: color-mix(in srgb, var(--chip-tone) 25%, var(--surface-light)); }
.chip__remove:focus-visible,
.chip__group:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
```

### JS

```js
// Reveal remove buttons now that they work
document.querySelectorAll('.chip__remove').forEach((btn) => { btn.hidden = false; });

// Remove the chip, tell the page, then focus the next chip, else the previous, else the list
document.addEventListener('click', (e) => {
  const chip = e.target.closest('.chip__remove')?.closest('.chip');
  if (!chip) return;
  const list = chip.parentElement;
  const near = chip.nextElementSibling || chip.previousElementSibling;
  chip.remove();
  list.dispatchEvent(new CustomEvent('chip-remove', { bubbles: true, detail: chip.dataset.value }));
  const target = near?.querySelector('.chip__remove') || list;
  if (target === list) list.tabIndex = -1;
  target.focus();
});
```

### Notes

- Tone colors on the tint are only ~4.1–4.5:1, so they're used only for the dot and border; the text is always `--text-main`. Every pill needs a word that states its status (WCAG 1.4.1).
- Name the chip in each remove label (`Remove Water heaters`); "Remove" alone is ambiguous in a list. The 1.5rem button meets the 24px target size (WCAG 2.5.8).
- When the last chip goes, focus lands on the list, which is announced by its label ("Active filters"). Listen for `chip-remove` to refresh results, and announce the new count in a `role="status"` region.
- These chips aren't toggles. For selectable filters use checkboxes or `<button aria-pressed>` (`components/form-controls.md`), and never nest the remove button inside another button.

## 7. Progress

A styled native `<progress>` with a visible label and percentage, plus a circular ring for dashboards. Both expose a name and a value to assistive tech: the bar natively, the ring through `role="progressbar"`. Place inside your page container.

### HTML

```html
<!-- Bar: native <progress>, named by <label for> -->
<div class="progress">
  <div class="progress__head">
    <label class="progress__label" for="upload-progress">Uploading photos</label>
    <!-- Visible copy of the value; hidden from AT, which reads it from the bar -->
    <span class="progress__value" aria-hidden="true">60%</span>
  </div>
  <progress class="progress__bar" id="upload-progress" max="100" value="60">60%</progress>
</div>

<!-- Ring: SVG drawing, named and valued through ARIA -->
<div class="progress progress--ring" style="--progress-value: 75">
  <div class="progress__ring" role="progressbar" aria-labelledby="ring-label"
       aria-valuemin="0" aria-valuemax="100" aria-valuenow="75">
    <svg class="progress__svg" viewBox="0 0 36 36" width="96" height="96" aria-hidden="true" focusable="false">
      <!-- r = 100 / 2π, so the circumference is 100 and dash lengths read as percent -->
      <circle class="progress__track" cx="18" cy="18" r="15.9155"/>
      <circle class="progress__fill" cx="18" cy="18" r="15.9155"/>
    </svg>
    <span class="progress__value" aria-hidden="true">75%</span>
  </div>
  <p class="progress__label" id="ring-label">Kitchen remodel</p>
</div>
```

### CSS

```css
/* Bar: label row above a slim track */
.progress { color: var(--text-main); font-family: var(--font-sans); }
.progress__head {
  display: flex; justify-content: space-between; align-items: baseline; gap: var(--space-sm);
  margin-bottom: var(--space-xs);
}
.progress__label { margin: 0; font-size: 0.9375rem; font-weight: 600; }
.progress__value { font-size: 0.875rem; color: var(--text-muted); font-variant-numeric: tabular-nums; }

/* Native <progress>: reset, then style the track (element, WebKit) and the fill (WebKit, Firefox) */
.progress__bar {
  -webkit-appearance: none; appearance: none;
  display: block; width: 100%; height: 0.5rem;
  border: 0; border-radius: var(--radius-full); overflow: hidden;
  background: var(--border-subtle); color: var(--primary);
}
.progress__bar::-webkit-progress-bar { background: var(--border-subtle); }
.progress__bar::-webkit-progress-value {
  background: var(--primary); border-radius: var(--radius-full);
  transition: width var(--transition-smooth);
}
.progress__bar::-moz-progress-bar { background: var(--primary); border-radius: var(--radius-full); }

/* Ring: track and fill stacked; the fill's dash length is --progress-value */
.progress--ring { display: inline-grid; justify-items: center; gap: var(--space-sm); text-align: center; }
.progress__ring { display: grid; place-items: center; width: 6rem; height: 6rem; }
.progress__ring > * { grid-area: 1 / 1; }
.progress__svg { width: 100%; height: 100%; transform: rotate(-90deg); fill: none; stroke-width: 3.5; }
.progress__track { stroke: var(--border-subtle); }
.progress__fill {
  stroke: var(--primary); stroke-linecap: round;
  stroke-dasharray: var(--progress-value, 0) 100;
  transition: stroke-dasharray var(--transition-smooth);
}
.progress__ring .progress__value { font-size: 1.25rem; font-weight: 700; color: var(--text-main); }
```

### JS

```js
// Optional helper: keep the bar or ring, its ARIA value and the visible text in sync
export function setProgress(block, value) {
  const v = Math.round(Math.min(100, Math.max(0, value)));
  const bar = block.querySelector('.progress__bar');
  if (bar) bar.value = v;
  block.querySelector('[role="progressbar"]')?.setAttribute('aria-valuenow', v);
  block.style.setProperty('--progress-value', v);
  block.querySelector('.progress__value').textContent = `${v}%`;
}

// Usage: setProgress(document.querySelector('.progress'), 80);
```

### Notes

- **Why `role="progressbar"` for the ring:** it shows how far a task has got (a project, an upload), which is what progressbar means, and screen readers support it well. Use `<meter>` instead for a measurement in a known range that isn't progress, like "Crew capacity 80%" or a rating. Native `<meter>` can't be drawn as a ring and `role="meter"` support is uneven, so show those as a styled `<meter>` bar.
- Both need a visible name: `<label for>` names the native bar and `aria-labelledby` names the ring. The visible percentage is `aria-hidden` because the value is already exposed. Add `aria-valuetext` (e.g. "75%, tiling stage") when the number alone isn't enough.
- Value changes aren't announced. For long tasks, announce milestones ("Upload complete") in a `role="status"` region, not every percent. For unknown durations use a loader from `components/animations.md`.
- The fill (`--primary`) is 4.2:1 against the track (`--border-subtle`), above the 3:1 needed for graphics.

## 8. Empty state

A centered placeholder for empty search results, lists or dashboards, with a decorative icon, a heading, one line of help and a single primary action. No JS. Place inside your page container.

### HTML

```html
<section class="empty-state" aria-labelledby="empty-title">
  <svg class="empty-state__icon" viewBox="0 0 24 24" width="32" height="32" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4M8 11h6"/></svg>
  <h2 class="empty-state__title" id="empty-title">No services match "gutter repair"</h2>
  <p class="empty-state__text">Try a shorter search or clear your filters. Not sure what you need? Call <a href="tel:+15555550123">(555) 555-0123</a> and we'll point you the right way.</p>
  <a class="empty-state__btn" href="https://example.com/services">Browse all services</a>
</section>
```

### CSS

```css
/* Centered column with a readable measure */
.empty-state {
  display: flex; flex-direction: column; align-items: center; gap: var(--space-sm);
  max-width: 28rem; margin-inline: auto; padding: var(--space-2xl) var(--space-md);
  text-align: center; color: var(--text-main); font-family: var(--font-sans);
}

/* Decorative icon in a soft tinted circle */
.empty-state__icon {
  box-sizing: content-box; width: 2rem; height: 2rem; padding: var(--space-md);
  margin-bottom: var(--space-sm); border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--primary) 10%, var(--surface-light)); color: var(--primary);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.empty-state__title { margin: 0; font-size: 1.25rem; line-height: 1.3; overflow-wrap: anywhere; }
.empty-state__text { margin: 0; color: var(--text-muted); line-height: 1.5; }
.empty-state__text a { color: var(--primary); }

/* One primary action, 44px tall */
.empty-state__btn {
  display: inline-flex; align-items: center; justify-content: center;
  min-height: 2.75rem; margin-top: var(--space-md); padding: 0 var(--space-lg);
  border: 0; border-radius: var(--radius-md);
  background: var(--primary); color: var(--text-inverse);
  font: inherit; font-weight: 600; text-decoration: none; cursor: pointer;
  transition: background-color var(--transition-fast);
}
.empty-state__btn:hover { background: var(--primary-hover); }
.empty-state__btn:focus-visible,
.empty-state__text a:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
```

### Notes

- The icon is decorative (`aria-hidden`). The heading says what's empty and the text says what to do next. Match the heading level to the page outline.
- Offer one primary action: a link when it navigates, a `<button>` when it acts in place ("Clear filters").
- When a live search turns up nothing, announce the result count in a `role="status"` region; don't move focus to the empty state.
- On first-run dashboards, make the action the first real step ("Book your first service") rather than a dead end.
