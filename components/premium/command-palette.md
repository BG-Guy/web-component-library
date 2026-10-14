# Command Palette

A ⌘K / Ctrl+K command palette: the shortcut or a search pill in the header springs open a frosted glass dialog with results grouped into Pages, Services and Actions. Fuzzy matching lights up the matched letters, one highlight glides between rows as you arrow through them, and actions such as "Copy email" confirm inside the palette before it closes. On phones it fills the width at the top of the screen, clear of the on-screen keyboard, with a tappable `esc` key. Depends on `tokens/variables.css`.

**Motion:** dialog spring scale-in (`--dur-4`, `--ease-spring`) with backdrop fade · highlight glide between rows (`--dur-3`, `--ease-spring`) · focus line draws under the field (`--ease-out`) · confirmation ring and tick draw (`--dur-5`/`--dur-4`, `--ease-out`).

## HTML

```html
<div class="cmdk-demo">
  <div class="cmdk-demo__bar">
    <div class="cmdk-demo__inner cmdk-demo__bar-inner">
      <a class="cmdk-demo__logo" href="#">
        <span class="cmdk-demo__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M12 2.7s6 6.4 6 11.3a6 6 0 0 1-12 0c0-4.9 6-11.3 6-11.3z" /></svg></span>
        Brand
      </a>
      <nav class="cmdk-demo__nav" aria-label="Main">
        <a href="#">Services</a><a href="#">Pricing</a><a href="#">Areas</a>
      </nav>
      <a class="cmdk__trigger" href="/search" data-cmdk-open="cmdk-palette" aria-haspopup="dialog" aria-keyshortcuts="Meta+K Control+K">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7" /><path d="m20 20-3.5-3.5" /></svg>
        <span>Search</span>
        <kbd class="cmdk__kbd" aria-hidden="true"><span class="cmdk__mod">⌘</span>K</kbd>
      </a>
    </div>
  </div>

  <div class="cmdk-demo__inner cmdk-demo__main">
    <p class="cmdk-demo__eyebrow">Plumbing &amp; heating · Springfield</p>
    <h2 class="cmdk-demo__title">Find any fix in two keystrokes.</h2>
    <p class="cmdk-demo__lead">Jump to a page, a service or an action without leaving the keyboard. Try typing “leak”, “wtr” or “book”.</p>
    <p class="cmdk-demo__hint" aria-hidden="true"><kbd class="cmdk__kbd"><span class="cmdk__mod">⌘</span>K</kbd> opens search from anywhere</p>
    <ul class="cmdk-demo__cards" role="list">
      <li class="cmdk-demo__card">
        <span class="cmdk-demo__card-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M12 2.7s6 6.4 6 11.3a6 6 0 0 1-12 0c0-4.9 6-11.3 6-11.3z" /></svg></span>
        <h3>Leak repair</h3><p>Found, fixed and dried out in one visit.</p><span class="cmdk-demo__price">from $149</span>
      </li>
      <li class="cmdk-demo__card">
        <span class="cmdk-demo__card-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4.1 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3a2.5 2.5 0 0 0 2.5 2.5z" /></svg></span>
        <h3>Water heaters</h3><p>Same-day installs across Westlake and Northside.</p><span class="cmdk-demo__price">from $890</span>
      </li>
      <li class="cmdk-demo__card">
        <span class="cmdk-demo__card-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z" /></svg></span>
        <h3>24/7 emergencies</h3><p>A real person answers, day or night.</p><span class="cmdk-demo__price">(555) 555-0123</span>
      </li>
    </ul>
  </div>
</div>

<dialog class="cmdk" id="cmdk-palette" aria-label="Search Brand" data-cmdk-seed="water heater,emergency">
  <div class="cmdk__panel">
    <div class="cmdk__field">
      <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7" /><path d="m20 20-3.5-3.5" /></svg>
      <label class="cmdk__sr" for="cmdk-input">Search pages, services and actions</label>
      <input class="cmdk__input" id="cmdk-input" type="text" autofocus role="combobox" aria-expanded="false" aria-controls="cmdk-list" aria-autocomplete="list" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Search pages, services, actions…">
      <button class="cmdk__esc" type="button">esc<span class="cmdk__sr"> (close search)</span></button>
    </div>

    <div class="cmdk__body">
      <div class="cmdk__list" id="cmdk-list" role="listbox" aria-label="Results">
        <div class="cmdk__highlight" aria-hidden="true">
          <span class="cmdk__enter"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M9 10 4 15l5 5M20 4v7a4 4 0 0 1-4 4H4" /></svg></span>
        </div>

        <div class="cmdk__group cmdk__group--recent" role="group" aria-labelledby="cmdk-g-recent" hidden>
          <div class="cmdk__group-label" id="cmdk-g-recent" role="presentation">Recent searches</div>
        </div>

        <div class="cmdk__group" role="group" aria-labelledby="cmdk-g-pages">
          <div class="cmdk__group-label" id="cmdk-g-pages" role="presentation">Pages</div>
          <div class="cmdk__option" role="option" data-href="#"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z" /></svg></span><span class="cmdk__label">Home</span><span class="cmdk__meta" aria-hidden="true">/</span></div>
          <div class="cmdk__option" role="option" data-href="#services"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z" /></svg></span><span class="cmdk__label">Services</span><span class="cmdk__meta" aria-hidden="true">/services</span></div>
          <div class="cmdk__option" role="option" data-href="#pricing" data-keywords="cost price quote rates"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8zM7 7h.01" /></svg></span><span class="cmdk__label">Pricing</span><span class="cmdk__meta" aria-hidden="true">/pricing</span></div>
          <div class="cmdk__option" role="option" data-href="#areas" data-keywords="westlake northside riverside map"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12zM12 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z" /></svg></span><span class="cmdk__label">Service areas</span><span class="cmdk__meta" aria-hidden="true">/areas</span></div>
          <div class="cmdk__option" role="option" data-href="#reviews" data-keywords="testimonials rating stars"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg></span><span class="cmdk__label">Reviews</span><span class="cmdk__meta" aria-hidden="true">/reviews</span></div>
          <div class="cmdk__option" role="option" data-href="#contact"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" /></svg></span><span class="cmdk__label">Contact</span><span class="cmdk__meta" aria-hidden="true">/contact</span></div>
        </div>

        <div class="cmdk__group" role="group" aria-labelledby="cmdk-g-services">
          <div class="cmdk__group-label" id="cmdk-g-services" role="presentation">Services</div>
          <div class="cmdk__option" role="option" data-href="#leak-repair" data-keywords="pipe drip burst"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M12 2.7s6 6.4 6 11.3a6 6 0 0 1-12 0c0-4.9 6-11.3 6-11.3z" /></svg></span><span class="cmdk__label">Leak repair</span><span class="cmdk__meta">from $149</span></div>
          <div class="cmdk__option" role="option" data-href="#water-heaters" data-keywords="boiler hot water tank"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4.1 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3a2.5 2.5 0 0 0 2.5 2.5z" /></svg></span><span class="cmdk__label">Water heater install</span><span class="cmdk__meta">from $890</span></div>
          <div class="cmdk__option" role="option" data-href="#drains" data-keywords="clog blocked sink"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M2 7c1.7 1.3 3.3 1.3 5 0s3.3-1.3 5 0 3.3 1.3 5 0 3.3-1.3 5 0M2 12c1.7 1.3 3.3 1.3 5 0s3.3-1.3 5 0 3.3 1.3 5 0 3.3-1.3 5 0M2 17c1.7 1.3 3.3 1.3 5 0s3.3-1.3 5 0 3.3 1.3 5 0 3.3-1.3 5 0" /></svg></span><span class="cmdk__label">Drain cleaning</span><span class="cmdk__meta">from $129</span></div>
          <div class="cmdk__option" role="option" data-href="#emergency" data-keywords="urgent burst flood night"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z" /></svg></span><span class="cmdk__label">Emergency callout</span><span class="cmdk__meta">24/7</span></div>
          <div class="cmdk__option" role="option" data-href="#inspection" data-keywords="check service maintenance"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M9 2h6v4H9zM16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2M9 14l2 2 4-4" /></svg></span><span class="cmdk__label">Annual inspection</span><span class="cmdk__meta">$89</span></div>
        </div>

        <div class="cmdk__group" role="group" aria-labelledby="cmdk-g-actions">
          <div class="cmdk__group-label" id="cmdk-g-actions" role="presentation">Actions</div>
          <div class="cmdk__option cmdk__option--action" role="option" data-href="tel:+15555550123" data-keywords="phone ring talk" data-done="Calling (555) 555-0123" data-detail="Handing over to your phone app…"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg></span><span class="cmdk__label">Call (555) 555-0123</span><span class="cmdk__meta">24/7</span></div>
          <div class="cmdk__option cmdk__option--action" role="option" data-href="#book" data-keywords="schedule appointment visit" data-done="Booking form ready" data-detail="Pick a day and a two-hour window."><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" /></svg></span><span class="cmdk__label">Book a visit</span><span class="cmdk__meta">Same day</span></div>
          <div class="cmdk__option cmdk__option--action" role="option" data-copy="hello@example.com" data-keywords="mail address" data-done="Email copied" data-detail="hello@example.com is on your clipboard."><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M9 9h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H11a2 2 0 0 1-2-2zM5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" /></svg></span><span class="cmdk__label">Copy email</span><span class="cmdk__meta">hello@example.com</span></div>
        </div>
      </div>

      <div class="cmdk__empty" hidden>
        <span class="cmdk__empty-art" aria-hidden="true"><svg viewBox="0 0 24 24" width="24" height="24" focusable="false"><circle cx="11" cy="11" r="7" /><path d="m20 20-3.5-3.5M9 9l4 4M13 9l-4 4" /></svg></span>
        <p class="cmdk__empty-title">No results for “<span class="cmdk__empty-q"></span>”</p>
        <p class="cmdk__empty-hint">Try “leak”, “pricing” or “book”. In a hurry? Call <a href="tel:+15555550123">(555) 555-0123</a>.</p>
      </div>

      <div class="cmdk__done" hidden>
        <svg class="cmdk__tick" viewBox="0 0 24 24" width="48" height="48" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="10" pathLength="1" /><path d="m7.5 12.5 3 3 6-6.5" pathLength="1" /></svg>
        <p class="cmdk__done-title"></p>
        <p class="cmdk__done-detail"></p>
      </div>
    </div>

    <div class="cmdk__foot" aria-hidden="true">
      <span class="cmdk__hint"><kbd class="cmdk__key">↑</kbd><kbd class="cmdk__key">↓</kbd>navigate</span>
      <span class="cmdk__hint"><kbd class="cmdk__key">↵</kbd>open</span>
      <span class="cmdk__hint"><kbd class="cmdk__key">esc</kbd>close</span>
      <span class="cmdk__brand">Brand search</span>
    </div>
    <p class="cmdk__sr cmdk__status" role="status"></p>

    <template class="cmdk__recent-tpl">
      <div class="cmdk__option" role="option"><span class="cmdk__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M3 12a9 9 0 1 0 3-6.7L3 8M3 3v5h5M12 7v5l3 2" /></svg></span><span class="cmdk__label"></span><span class="cmdk__meta" aria-hidden="true">Search again</span></div>
    </template>
  </div>
</dialog>
```

## CSS

```css
/* Shared ink: darker muted/accent so small text clears 4.5:1 on tinted light and glass */
.cmdk-demo, .cmdk {
  --cmdk-muted: color-mix(in srgb, var(--text-muted) 75%, var(--text-main));
  --cmdk-accent: color-mix(in srgb, var(--primary) 80%, var(--text-main));
}
.cmdk-demo svg, .cmdk svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }

/* Demo page: light and softly lit, so the glass has colour to frost */
.cmdk-demo {
  min-height: 35rem; overflow: clip; color: var(--text-main); font-family: var(--font-sans);
  background:
    radial-gradient(50% 40% at 8% 0%, color-mix(in srgb, var(--primary) 14%, transparent), transparent 70%),
    radial-gradient(40% 45% at 100% 35%, color-mix(in srgb, var(--primary-2) 14%, transparent), transparent 70%),
    radial-gradient(45% 40% at 40% 110%, color-mix(in srgb, var(--accent) 12%, transparent), transparent 70%),
    var(--surface-muted);
}
.cmdk-demo__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.cmdk-demo__bar { border-bottom: 1px solid color-mix(in srgb, var(--border-subtle) 80%, transparent); background: var(--glass); }
.cmdk-demo__bar-inner { display: flex; align-items: center; gap: 1.75rem; height: 4.25rem; }
.cmdk-demo__logo {
  display: inline-flex; align-items: center; gap: 0.625rem; margin-right: auto; border-radius: var(--radius-md);
  color: var(--text-main); font: 600 1.125rem var(--font-display); letter-spacing: var(--tracking-tight); text-decoration: none;
}
.cmdk-demo__mark { display: grid; place-items: center; width: 2.125rem; height: 2.125rem; border-radius: 0.75rem; background: var(--gradient-brand); color: var(--text-inverse); box-shadow: var(--highlight), var(--shadow-glow); }
.cmdk-demo__nav { display: none; gap: 1.75rem; }
.cmdk-demo__nav a { border-radius: var(--radius-sm); color: var(--cmdk-muted); font-size: 0.9375rem; font-weight: 500; text-decoration: none; transition: color var(--dur-2); }
.cmdk-demo__nav a:hover { color: var(--text-main); }
.cmdk-demo a:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

.cmdk-demo__main { padding-block: clamp(3rem, 8vw, 5.5rem) 3.5rem; }
.cmdk-demo__eyebrow { margin: 0; color: var(--cmdk-accent); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.cmdk-demo__title { max-width: 16ch; margin: 0.875rem 0 0; font: 600 clamp(2.25rem, 1.4rem + 4vw, 4rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.cmdk-demo__lead { max-width: 34rem; margin: 1.25rem 0 0; color: var(--cmdk-muted); font-size: 1.0625rem; line-height: 1.6; }
.cmdk-demo__hint { display: none; align-items: center; gap: 0.625rem; margin: 1.5rem 0 0; color: var(--cmdk-muted); font-size: 0.875rem; }
.cmdk-demo__cards { display: grid; gap: 0.875rem; margin: 2.75rem 0 0; padding: 0; list-style: none; }
.cmdk-demo__card {
  display: grid; grid-template-columns: auto 1fr; column-gap: 0.875rem; padding: 1.125rem; border-radius: var(--radius-xl);
  background: var(--glass); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm);
}
.cmdk-demo__card-icon { grid-row: span 3; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 0.75rem; background: color-mix(in srgb, var(--primary) 10%, var(--surface-light)); color: var(--primary); }
.cmdk-demo__card h3 { margin: 0; font: 600 1rem/1.3 var(--font-display); letter-spacing: var(--tracking-tight); }
.cmdk-demo__card p { margin: 0.25rem 0 0; color: var(--cmdk-muted); font-size: 0.875rem; line-height: 1.5; }
.cmdk-demo__price { margin-top: 0.625rem; font: 500 0.8125rem var(--font-mono); }

/* Trigger: a search pill; the shortcut chip appears where there's a keyboard-sized screen */
.cmdk__trigger {
  display: inline-flex; align-items: center; gap: 0.625rem; height: 2.75rem; padding: 0 1rem 0 0.875rem; border-radius: 999px; cursor: pointer;
  background: var(--surface-light); color: var(--cmdk-muted); font: 500 0.9375rem var(--font-sans); text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm);
  transition: color var(--dur-2), box-shadow var(--dur-3) var(--ease-out), transform var(--dur-3) var(--ease-spring);
}
.cmdk__trigger:hover { color: var(--text-main); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 35%, var(--border-subtle)), var(--highlight), var(--shadow-md); }
.cmdk__trigger:active { transform: scale(0.97); }
.cmdk__trigger:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.cmdk__kbd {
  display: inline-flex; align-items: center; height: 1.5rem; padding: 0 0.4375rem; border-radius: 0.4375rem;
  background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle), inset 0 -1.5px 0 var(--border-subtle);
  color: var(--cmdk-muted); font: 500 0.75rem/1 var(--font-mono);
}
.cmdk__trigger .cmdk__kbd { display: none; }

/* Dialog: frosted glass that springs in near the top */
.cmdk {
  --cmdk-line: color-mix(in srgb, var(--text-main) 9%, transparent);
  width: min(40rem, calc(100% - 1.5rem)); max-width: none; max-height: calc(100vh - 1.5rem); max-height: calc(100dvh - 1.5rem);
  margin: 0.75rem auto auto; padding: 0; border: 0; border-radius: var(--radius-2xl); overflow: hidden;
  background: color-mix(in srgb, var(--surface-light) 88%, transparent); color: var(--text-main); font-family: var(--font-sans);
  box-shadow:
    inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 70%, transparent), var(--highlight), 0 0 0 1px var(--cmdk-line),
    var(--shadow-xl), 0 48px 120px -32px color-mix(in srgb, var(--primary) 40%, transparent);
  opacity: 0; transform: translateY(-0.5rem) scale(0.96); transform-origin: 50% 0;
  transition: opacity var(--dur-2) var(--ease-out), transform var(--dur-4) var(--ease-spring);
}
@supports (backdrop-filter: blur(1px)) { .cmdk { backdrop-filter: blur(var(--blur-lg)) saturate(1.8); } }
.cmdk[data-state="open"] { opacity: 1; transform: none; }
.cmdk::backdrop { background: color-mix(in srgb, var(--surface-deep) 24%, transparent); backdrop-filter: blur(2px); opacity: 0; transition: opacity var(--dur-3) var(--ease-out); }
.cmdk[data-state="open"]::backdrop { opacity: 1; }
html:has(.cmdk[open]) { overflow: hidden; }
.cmdk__panel { display: flex; flex-direction: column; max-height: inherit; background: radial-gradient(90% 60% at 50% -20%, color-mix(in srgb, var(--surface-light) 80%, transparent), transparent 70%); }
.cmdk :is(button, a):focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }

/* Field: a brand line draws under it while the input has focus */
.cmdk__field { position: relative; display: flex; align-items: center; gap: 0.75rem; padding: 0 0.875rem 0 1.125rem; border-bottom: 1px solid var(--cmdk-line); color: var(--cmdk-muted); }
.cmdk__field > svg { flex: none; }
.cmdk__field::after {
  content: ""; position: absolute; left: 0; right: 0; bottom: -1px; height: 2px;
  background: linear-gradient(90deg, var(--primary), var(--primary-2)); transform: scaleX(0); transition: transform var(--dur-5) var(--ease-out);
}
.cmdk__field:focus-within::after { transform: scaleX(1); }
.cmdk__input {
  flex: 1; min-width: 0; height: 3.75rem; padding: 0; border: 0; background: none; outline: 2px solid transparent;
  color: var(--text-main); font: 500 1.0625rem var(--font-sans);
}
.cmdk__input::placeholder { color: var(--cmdk-muted); opacity: 1; }
.cmdk__esc {
  flex: none; height: 1.75rem; padding: 0 0.5rem; border: 0; border-radius: 0.5rem; cursor: pointer;
  background: color-mix(in srgb, var(--text-main) 6%, transparent); box-shadow: inset 0 -1.5px 0 var(--cmdk-line);
  color: var(--cmdk-muted); font: 500 0.75rem/1 var(--font-mono); transition: background-color var(--dur-2), color var(--dur-2);
}
.cmdk__esc:hover { background: color-mix(in srgb, var(--text-main) 10%, transparent); color: var(--text-main); }

/* Results: grouped options over one gliding highlight */
.cmdk__body { display: flex; flex-direction: column; flex: 1; min-height: 0; }
.cmdk__list {
  position: relative; flex: 1; min-height: 0; max-height: min(26rem, 45vh); padding: 0.375rem 0.5rem 0.5rem; /* clears a phone keyboard */
  overflow-y: auto; overscroll-behavior: contain; scroll-padding-block: 2.25rem 0.5rem; scrollbar-width: thin;
}
.cmdk__group-label { padding: 0.875rem 0.75rem 0.375rem; color: var(--cmdk-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.cmdk__option { position: relative; z-index: 1; display: flex; align-items: center; gap: 0.75rem; min-height: 3rem; padding: 0.375rem 0.75rem; border-radius: var(--radius-xl); cursor: pointer; user-select: none; }
.cmdk__option[hidden] { display: none; }
.cmdk__icon {
  flex: none; display: grid; place-items: center; width: 2rem; height: 2rem; border-radius: 0.625rem;
  background: var(--surface-light); color: var(--cmdk-muted); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  transition: color var(--dur-2), background-color var(--dur-2), box-shadow var(--dur-3), transform var(--dur-3) var(--ease-spring);
}
.cmdk__option--action .cmdk__icon { color: var(--primary); }
.cmdk__option[aria-selected="true"] .cmdk__icon { background-color: var(--primary); color: var(--text-inverse); box-shadow: var(--highlight), 0 6px 16px -6px var(--primary); transform: scale(1.06); }
.cmdk__label { flex: 1; min-width: 0; overflow: hidden; font-size: 0.9375rem; font-weight: 500; white-space: nowrap; text-overflow: ellipsis; }
.cmdk__meta { flex: none; max-width: 42%; overflow: hidden; color: var(--cmdk-muted); font: 0.75rem var(--font-mono); white-space: nowrap; text-overflow: ellipsis; }
.cmdk__mark {
  padding: 0; background: none; color: var(--cmdk-accent); font-weight: 650;
  text-decoration-line: underline; text-decoration-thickness: 2px; text-decoration-color: color-mix(in srgb, var(--primary) 35%, transparent); text-underline-offset: 0.2em;
}
.cmdk__highlight {
  position: absolute; z-index: 0; top: 0; left: 0.5rem; right: 0.5rem; height: var(--cmdk-h, 3rem); pointer-events: none;
  border-radius: var(--radius-xl); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md);
  opacity: 0; transform: translateY(var(--cmdk-y, 0));
  transition: transform var(--dur-3) var(--ease-spring), height var(--dur-3) var(--ease-out), opacity var(--dur-2);
}
.cmdk__highlight.is-visible { opacity: 1; }
.cmdk__highlight::before { content: ""; position: absolute; left: 0.3125rem; top: 28%; bottom: 28%; width: 3px; border-radius: 3px; background: linear-gradient(var(--primary), var(--primary-2)); }
.cmdk__enter {
  position: absolute; top: 50%; right: 0.625rem; display: none; place-items: center; width: 1.5rem; height: 1.5rem; margin-top: -0.75rem;
  border-radius: 0.4375rem; background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); color: var(--cmdk-muted);
}

/* Empty state and in-palette confirmation */
.cmdk__empty, .cmdk__done { display: grid; justify-items: center; gap: 0.375rem; padding: 2.75rem 1.5rem 3rem; text-align: center; }
.cmdk__empty[hidden], .cmdk__done[hidden] { display: none; }
.cmdk__empty-art {
  display: grid; place-items: center; width: 3.25rem; height: 3.25rem; margin-bottom: 0.625rem; border-radius: 1rem; rotate: -6deg;
  background: var(--surface-light); color: var(--cmdk-muted); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md);
}
.cmdk__empty-title, .cmdk__done-title { margin: 0; font: 600 1.0625rem/1.3 var(--font-display); letter-spacing: var(--tracking-tight); overflow-wrap: anywhere; }
.cmdk__empty-hint, .cmdk__done-detail { max-width: 22rem; margin: 0; color: var(--cmdk-muted); font-size: 0.875rem; line-height: 1.55; }
.cmdk__empty-hint a { border-radius: var(--radius-sm); color: var(--cmdk-accent); font-weight: 600; text-underline-offset: 0.2em; }
.cmdk__tick { margin-bottom: 0.75rem; overflow: visible; }
.cmdk__tick circle, .cmdk__tick path { stroke-dasharray: 1; }
.cmdk__tick circle { fill: color-mix(in srgb, var(--success) 8%, transparent); stroke: color-mix(in srgb, var(--success) 30%, transparent); stroke-width: 1.5; }
.cmdk__tick path { stroke: var(--success); stroke-width: 2; }
.cmdk__done:not([hidden]) .cmdk__tick { animation: cmdk-pop var(--dur-4) var(--ease-spring) both; }
.cmdk__done:not([hidden]) .cmdk__tick circle { animation: cmdk-draw var(--dur-5) var(--ease-out) both; }
.cmdk__done:not([hidden]) .cmdk__tick path { animation: cmdk-draw var(--dur-4) var(--ease-out) 250ms both; }

/* Footer key hints */
.cmdk__foot {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem 1.125rem; padding: 0.625rem 1rem; border-top: 1px solid var(--cmdk-line);
  background: color-mix(in srgb, var(--surface-muted) 60%, transparent); color: var(--cmdk-muted); font-size: 0.75rem;
}
.cmdk__hint { display: inline-flex; align-items: center; gap: 0.25rem; }
.cmdk__key {
  display: inline-grid; place-items: center; min-width: 1.375rem; height: 1.375rem; margin-right: 0.125rem; padding: 0 0.3125rem; border-radius: 0.375rem;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), inset 0 -1.5px 0 var(--border-subtle); color: var(--text-main); font: 500 0.6875rem/1 var(--font-mono);
}
.cmdk__brand { display: none; margin-left: auto; font-family: var(--font-mono); }
.cmdk__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }

@media (min-width: 768px) {
  .cmdk-demo__nav, .cmdk-demo__hint { display: flex; }
  .cmdk-demo__cards { grid-template-columns: repeat(3, 1fr); }
  .cmdk__trigger { min-width: 15rem; }
  .cmdk__trigger .cmdk__kbd { display: inline-flex; margin-left: auto; }
  .cmdk { margin-top: 12vh; max-height: 76vh; }
  .cmdk__list { max-height: min(26rem, 52vh); }
  .cmdk__option { padding-right: 2.75rem; }
  .cmdk__enter { display: grid; }
  .cmdk__brand { display: inline; }
}
@media (hover: none) and (pointer: coarse) {
  .cmdk__foot { display: none; } /* key hints are noise on touch-only devices */
}
@media (prefers-reduced-motion: reduce) {
  .cmdk { transform: none; }
  .cmdk *, .cmdk *::before, .cmdk *::after { animation: none !important; }
}
@keyframes cmdk-draw { from { stroke-dashoffset: 1; } }
@keyframes cmdk-pop { from { opacity: 0; transform: scale(0.6); } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const mac = /Mac|iPhone|iPad|iPod/.test(navigator.userAgent);
document.querySelectorAll('.cmdk__mod').forEach((k) => { k.textContent = mac ? '⌘' : 'Ctrl '; });

// Subsequence match: consecutive letters and word starts score higher
const fuzzy = (text, q) => {
  const t = text.toLowerCase(), hits = [];
  let score = 0, prev = -2;
  for (const ch of q) {
    const i = t.indexOf(ch, prev + 1);
    if (i < 0) return null;
    score += i === prev + 1 ? 4 : i === 0 || t[i - 1] === ' ' ? 3 : 1;
    hits.push((prev = i));
  }
  return { score: score - t.length / 100, hits };
};

document.querySelectorAll('.cmdk').forEach((dialog, n) => {
  const uid = `cmdk-${n}`;
  const [input, list, hl, empty, done, title, detail, status, recentGroup, tpl] = ['input', 'list', 'highlight', 'empty', 'done',
    'done-title', 'done-detail', 'status', 'group--recent', 'recent-tpl'].map((part) => dialog.querySelector(`.cmdk__${part}`));
  const groups = [...list.querySelectorAll('.cmdk__group:not(.cmdk__group--recent)')], meta = new Map(), key = `cmdk-recent:${dialog.id}`;
  let items = [], active = null, opener = null, pending = '', timer = 0, said = 0, recent = [];

  // Unique ids per instance for the combobox/listbox wiring
  dialog.querySelector('label[for]').htmlFor = input.id = `${uid}-input`;
  input.setAttribute('aria-controls', (list.id = `${uid}-list`));
  list.querySelectorAll('.cmdk__group-label').forEach((l, i) => l.parentElement.setAttribute('aria-labelledby', (l.id = `${uid}-g${i}`)));
  groups.flatMap((g) => [...g.querySelectorAll('[role="option"]')]).forEach((o, i) => {
    o.id = `${uid}-o${i}`;
    meta.set(o, { text: o.querySelector('.cmdk__label').textContent, order: i });
  });
  // Recent searches persist in localStorage; data-cmdk-seed fills the demo on a first visit
  try { recent = JSON.parse(localStorage.getItem(key)) || []; } catch { recent = []; }
  if (!Array.isArray(recent) || !recent.length) recent = (dialog.dataset.cmdkSeed || '').split(',').filter(Boolean);
  const remember = (q) => {
    if ((q = q.trim()).length < 2) return;
    recent = [q, ...recent.filter((r) => r !== q)].slice(0, 3);
    try { localStorage.setItem(key, JSON.stringify(recent)); } catch { /* private mode: keep it in memory */ }
  };
  // Wrap matched characters in <mark>, built as DOM nodes (no innerHTML)
  const paint = (o, hits = []) => {
    const parts = [''];
    meta.get(o).text.split('').forEach((c, i) => {
      if (hits.includes(i)) parts.push(Object.assign(document.createElement('mark'), { className: 'cmdk__mark', textContent: c }), '');
      else parts[parts.length - 1] += c;
    });
    o.querySelector('.cmdk__label').replaceChildren(...parts);
  };
  // One highlight glides to the active row; aria-activedescendant follows it
  const setActive = (i, instant, quiet) => {
    active?.removeAttribute('aria-selected');
    active = items[i] || null;
    hl.classList.toggle('is-visible', !!active);
    if (!active) return input.removeAttribute('aria-activedescendant');
    active.setAttribute('aria-selected', 'true');
    input.setAttribute('aria-activedescendant', active.id);
    if (instant) hl.style.transition = 'none';
    hl.style.setProperty('--cmdk-y', `${active.offsetTop}px`);
    hl.style.setProperty('--cmdk-h', `${active.offsetHeight}px`);
    if (instant) { void hl.offsetWidth; hl.style.transition = ''; }
    if (!quiet) active.scrollIntoView({ block: 'nearest' });
  };
  const filter = (instant) => {
    const q = input.value.toLowerCase().replace(/\s+/g, '');
    if (!done.hidden) { clearTimeout(timer); pending = ''; done.hidden = true; }
    recentGroup.hidden = !!q || !recent.length;
    recentGroup.replaceChildren(recentGroup.firstElementChild, ...recent.map((r, i) => {
      const o = tpl.content.firstElementChild.cloneNode(true);
      o.id = `${uid}-r${i}`;
      o.dataset.recent = o.querySelector('.cmdk__label').textContent = r;
      return o;
    }));
    groups.forEach((g) => {
      const ranked = [...g.querySelectorAll('[role="option"]')].map((o) => {
        const { text, order } = meta.get(o);
        const m = !q ? { score: -order } : fuzzy(text, q) || ((o.dataset.keywords || '').includes(q) ? { score: 0 } : null);
        o.hidden = !m;
        paint(o, m?.hits);
        return [o, m ? m.score : -1e9];
      });
      ranked.sort((a, b) => b[1] - a[1]).forEach(([o]) => g.append(o));
      g.hidden = ranked.every(([o]) => o.hidden);
    });
    items = [...list.querySelectorAll('.cmdk__group:not([hidden]) [role="option"]:not([hidden])')];
    list.hidden = !items.length;
    empty.hidden = !!items.length;
    dialog.querySelector('.cmdk__empty-q').textContent = input.value.trim();
    input.setAttribute('aria-expanded', String(!!items.length));
    setActive(0, instant);
    clearTimeout(said);
    said = setTimeout(() => { status.textContent = q ? `${items.length || 'No'} result${items.length === 1 ? '' : 's'}` : ''; }, 400);
  };

  // Open with a spring (CSS); close plays the exit, then returns focus and follows any chosen link
  const open = (from) => {
    clearTimeout(timer);
    if (!dialog.open) { opener = from || document.activeElement; input.value = ''; dialog.showModal(); filter(true); }
    requestAnimationFrame(() => requestAnimationFrame(() => { dialog.dataset.state = 'open'; }));
  };
  const close = () => {
    if (!dialog.open) return;
    clearTimeout(timer);
    delete dialog.dataset.state;
    timer = setTimeout(() => dialog.close(), reduce.matches ? 0 : 200);
  };
  const dismiss = () => { pending = ''; close(); };
  dialog.addEventListener('close', () => {
    delete dialog.dataset.state;
    opener?.focus?.();
    if (pending) location.href = pending;
    pending = '';
  });

  // Pages navigate once the palette has closed; actions confirm inside it first
  const say = (head, text) => { title.textContent = status.textContent = head; detail.textContent = text; };
  const choose = (o) => {
    if (!o) return;
    if (o.dataset.recent) { input.value = o.dataset.recent; filter(); return; }
    remember(input.value);
    pending = o.dataset.href || '';
    if (!o.dataset.done) return close();
    clearTimeout(said);
    say(o.dataset.done, o.dataset.detail || '');
    const blocked = () => say('Clipboard blocked', `The address is ${o.dataset.copy}.`);
    if (o.dataset.copy) navigator.clipboard ? navigator.clipboard.writeText(o.dataset.copy).catch(blocked) : blocked();
    done.hidden = false;
    list.hidden = empty.hidden = true;
    input.setAttribute('aria-expanded', 'false');
    input.removeAttribute('aria-activedescendant');
    timer = setTimeout(close, 1400);
  };

  input.addEventListener('input', () => filter());
  input.addEventListener('keydown', (e) => {
    if (e.isComposing || !done.hidden) return;
    const i = items.indexOf(active), last = items.length - 1;
    const to = { ArrowDown: i < last ? i + 1 : 0, ArrowUp: i > 0 ? i - 1 : last, Home: 0, End: last }[e.key];
    if (to !== undefined && items.length) { e.preventDefault(); setActive(to); }
    else if (e.key === 'Enter') { e.preventDefault(); choose(active); }
  });
  list.addEventListener('mousedown', (e) => e.preventDefault()); // keep focus in the input
  list.addEventListener('pointermove', (e) => {
    const o = e.target.closest('[role="option"]');
    if (o && o !== active) setActive(items.indexOf(o), false, true);
  });
  list.addEventListener('click', (e) => choose(e.target.closest('[role="option"]')));

  // Openers: links to /search without JS, buttons with it; plus the global shortcut
  document.querySelectorAll(`[data-cmdk-open="${dialog.id}"]`).forEach((t) => {
    t.setAttribute('role', 'button');
    t.addEventListener('click', (e) => { e.preventDefault(); open(t); });
    t.addEventListener('keydown', (e) => { if (e.key === ' ') { e.preventDefault(); open(t); } });
  });
  document.addEventListener('keydown', (e) => {
    if (e.defaultPrevented || !(e.metaKey || e.ctrlKey) || e.key?.toLowerCase() !== 'k') return;
    e.preventDefault();
    if (dialog.dataset.state === 'open') dismiss(); else open();
  });
  dialog.addEventListener('cancel', (e) => { e.preventDefault(); dismiss(); });
  dialog.addEventListener('click', (e) => { if (e.target === dialog || e.target.closest('.cmdk__esc')) dismiss(); });
});
```

## Notes

- APG combobox with a grouped listbox: the input keeps focus and points at the active option through `aria-activedescendant`. ↑/↓ wrap, Home/End jump to the first and last result, and Enter runs the result. A polite `role="status"` says "5 results" once typing pauses, and it also reads out each action's confirmation. Focus never leaves the input, so the field draws a 2px brand line under itself as its focus indicator (≥ 3.7:1). Buttons and links get the standard outline.
- It's a real modal `<dialog>`: the page behind is inert, Escape, the `esc` key and backdrop clicks close it, and focus goes back to whatever opened it. Without JS the trigger is a plain link to `/search`. With JS it becomes a button, and ⌘K (Ctrl+K elsewhere) toggles the palette from anywhere.
- To install, put the `<dialog>` once before `</body>` and add `data-cmdk-open="<dialog id>"` to any trigger. Each option takes `data-href` (a page, `tel:` or `#anchor`, followed after the palette closes). Add `data-done` and `data-detail` for an in-palette confirmation, `data-copy` to copy text, and `data-keywords` for extra search terms. Recent searches are kept in `localStorage` (try/catch). `data-cmdk-seed` only fills the demo on a first visit.
- Contrast: the glass is 88% `--surface-light` over a lightly dimmed page, so small grey text uses `--cmdk-muted` (≈ 5.9:1) and highlighted letters use `--cmdk-accent` (≈ 5.2:1). `--text-main` reads at more than 12:1. Over dark pages, raise the glass mix to 94%.
- Reduced motion: no scale, and the open, glide and confirmation draws are instant. Without `backdrop-filter` the panel stays an 88% light surface.
