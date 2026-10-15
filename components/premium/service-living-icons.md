# Living Icon Service Cards

A light services grid where every icon tells a tiny story: a faucet drips and ripples, a bolt flickers and throws sparks, fan blades spin up and settle, roof courses stack row by row, a key turns as the shackle clicks, and rain runs along a gutter and drips. Each story plays once, staggered, as its card first scrolls into view, then replays on hover or keyboard focus while the card lifts on a spring and light glints along its gradient hairline. One column on phones, two from 600px, three from 1024px. Depends on `tokens/variables.css`.

**Motion:** icon micro-stories (1–1.6s keyframes on `--ease-in-out` / `--ease-spring`, never looping, 140ms stagger on first view) · card lift (`--dur-4`, `--ease-spring`) · hairline glint and face sheen (`--dur-5`, `--ease-out`) · "Today" dot pings three times, then rests.

## HTML

```html
<section class="svc-living" aria-labelledby="svc-living-title" data-svc-living>
  <div class="svc-living__inner">
    <header class="svc-living__head">
      <p class="svc-living__eyebrow">Services</p>
      <h2 id="svc-living-title" class="svc-living__title">One call fixes <span class="svc-living__glow">almost anything.</span></h2>
      <p class="svc-living__intro">Licensed, background-checked pros for every corner of your home. Upfront prices, same-day slots across Springfield and a 12-month guarantee on every job.</p>
    </header>

    <ul class="svc-living__grid" role="list">
      <li class="svc-living__card" style="--svc-living-hue: var(--primary)">
        <div class="svc-living__top">
          <span class="svc-living__tile" aria-hidden="true">
            <svg class="svc-living__icon" viewBox="0 0 24 24" width="28" height="28" focusable="false">
              <path d="M3.5 6.5v6.5" />
              <path d="M3.5 8H13a4 4 0 0 1 4 4v1h-3.5v-.5a1 1 0 0 0-1-1H3.5" />
              <path d="M9 8V5.5M6.5 5.5h5" />
              <path class="svc-living__drop" d="M15.25 14.6c.7.9 1.15 1.6 1.15 2.2a1.15 1.15 0 0 1-2.3 0c0-.6.45-1.3 1.15-2.2z" />
              <ellipse class="svc-living__ring" cx="15.25" cy="21" rx="2" ry=".55" />
              <ellipse class="svc-living__ring svc-living__ring--outer" cx="15.25" cy="21" rx="3.6" ry="1" />
            </svg>
          </span>
          <p class="svc-living__eta"><span class="svc-living__dot" aria-hidden="true"></span><span class="svc-living__sr">Available </span>Today</p>
        </div>
        <h3 class="svc-living__name">Plumbing</h3>
        <p class="svc-living__benefit">Leaks, clogs and water heaters, fixed on the first visit.</p>
        <div class="svc-living__meta">
          <p class="svc-living__price"><small>from</small> $89</p>
          <p class="svc-living__rating"><svg class="svc-living__star" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>4.9<span class="svc-living__sr"> out of 5,</span> <span class="svc-living__count">(2,140<span class="svc-living__sr"> reviews</span>)</span></p>
        </div>
        <a class="svc-living__link" href="#book-plumbing">Book plumbing <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </li>

      <li class="svc-living__card" style="--svc-living-hue: var(--accent)">
        <div class="svc-living__top">
          <span class="svc-living__tile" aria-hidden="true">
            <svg class="svc-living__icon" viewBox="0 0 24 24" width="28" height="28" focusable="false">
              <path class="svc-living__bolt" d="M13 2.5 5.5 13.5H11l-1 8 7.5-11H12l1-8z" />
              <path class="svc-living__spark" d="M18.6 5.2l1.9-1.4M19.4 8.1l2.1.3" />
              <path class="svc-living__spark svc-living__spark--low" d="M5.2 18.6l-1.8 1.5M4.5 15.8l-2.1-.2" />
            </svg>
          </span>
          <p class="svc-living__eta"><span class="svc-living__dot" aria-hidden="true"></span><span class="svc-living__sr">Available </span>Today</p>
        </div>
        <h3 class="svc-living__name">Electrical</h3>
        <p class="svc-living__benefit">Outlets, panels and lighting, by licensed electricians.</p>
        <div class="svc-living__meta">
          <p class="svc-living__price"><small>from</small> $99</p>
          <p class="svc-living__rating"><svg class="svc-living__star" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>4.9<span class="svc-living__sr"> out of 5,</span> <span class="svc-living__count">(1,380<span class="svc-living__sr"> reviews</span>)</span></p>
        </div>
        <a class="svc-living__link" href="#book-electrical">Book electrical <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </li>

      <li class="svc-living__card" style="--svc-living-hue: var(--primary-2)">
        <div class="svc-living__top">
          <span class="svc-living__tile" aria-hidden="true">
            <svg class="svc-living__icon" viewBox="0 0 24 24" width="28" height="28" focusable="false">
              <circle cx="12" cy="12" r="9.5" />
              <g class="svc-living__blades">
                <path d="M11.4 10.6C9.6 9.4 9.4 5.6 12.3 4.6c2.3-.7 3.5 1.9 2.4 3.9-.6 1.1-1.5 1.8-2.4 2.3" />
                <path d="M11.4 10.6C9.6 9.4 9.4 5.6 12.3 4.6c2.3-.7 3.5 1.9 2.4 3.9-.6 1.1-1.5 1.8-2.4 2.3" transform="rotate(120 12 12)" />
                <path d="M11.4 10.6C9.6 9.4 9.4 5.6 12.3 4.6c2.3-.7 3.5 1.9 2.4 3.9-.6 1.1-1.5 1.8-2.4 2.3" transform="rotate(240 12 12)" />
              </g>
              <circle cx="12" cy="12" r="1.5" />
            </svg>
          </span>
          <p class="svc-living__eta"><span class="svc-living__dot" aria-hidden="true"></span><span class="svc-living__sr">Available </span>Today</p>
        </div>
        <h3 class="svc-living__name">Heating &amp; cooling</h3>
        <p class="svc-living__benefit">Furnace and AC tune-ups, repairs and new installs.</p>
        <div class="svc-living__meta">
          <p class="svc-living__price"><small>from</small> $129</p>
          <p class="svc-living__rating"><svg class="svc-living__star" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>4.9<span class="svc-living__sr"> out of 5,</span> <span class="svc-living__count">(960<span class="svc-living__sr"> reviews</span>)</span></p>
        </div>
        <a class="svc-living__link" href="#book-hvac">Book heating &amp; cooling <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </li>

      <li class="svc-living__card" style="--svc-living-hue: color-mix(in srgb, var(--danger) 75%, var(--accent))">
        <div class="svc-living__top">
          <span class="svc-living__tile" aria-hidden="true">
            <svg class="svc-living__icon" viewBox="0 0 24 24" width="28" height="28" focusable="false">
              <path d="M5.5 14v6.5h13V14" />
              <path d="M10.5 20.5V17h3v3.5" />
              <path class="svc-living__course" d="M2.5 14 6 10.5h12l3.5 3.5z" />
              <path class="svc-living__course svc-living__course--2" d="M6 10.5 9 7.5h6l3 3" />
              <path class="svc-living__course svc-living__course--3" d="M9 7.5 11 5.5h2l2 2" />
            </svg>
          </span>
          <p class="svc-living__eta"><span class="svc-living__dot" aria-hidden="true"></span><span class="svc-living__sr">Available </span>Today</p>
        </div>
        <h3 class="svc-living__name">Roofing</h3>
        <p class="svc-living__benefit">Leak patches, storm damage and full re-roofs.</p>
        <div class="svc-living__meta">
          <p class="svc-living__price"><small>from</small> $249</p>
          <p class="svc-living__rating"><svg class="svc-living__star" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>4.8<span class="svc-living__sr"> out of 5,</span> <span class="svc-living__count">(610<span class="svc-living__sr"> reviews</span>)</span></p>
        </div>
        <a class="svc-living__link" href="#book-roofing">Book roofing <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </li>

      <li class="svc-living__card" style="--svc-living-hue: color-mix(in srgb, var(--primary) 55%, var(--text-main))">
        <div class="svc-living__top">
          <span class="svc-living__tile" aria-hidden="true">
            <svg class="svc-living__icon" viewBox="0 0 24 24" width="28" height="28" focusable="false">
              <path class="svc-living__shackle" d="M8 11V8a4 4 0 0 1 8 0v3" />
              <rect x="5" y="11" width="14" height="10" rx="2.5" />
              <g class="svc-living__keyhole"><circle cx="12" cy="15.2" r="1.3" /><path d="M12 16.5v1.8" /></g>
              <rect class="svc-living__key" x="10.7" y="12.8" width="2.6" height="6.4" rx="1.3" />
            </svg>
          </span>
          <p class="svc-living__eta"><span class="svc-living__dot" aria-hidden="true"></span><span class="svc-living__sr">Available </span>Today</p>
        </div>
        <h3 class="svc-living__name">Locks &amp; security</h3>
        <p class="svc-living__benefit">Lockouts, rekeys and smart locks, fitted within the hour.</p>
        <div class="svc-living__meta">
          <p class="svc-living__price"><small>from</small> $79</p>
          <p class="svc-living__rating"><svg class="svc-living__star" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>4.9<span class="svc-living__sr"> out of 5,</span> <span class="svc-living__count">(1,020<span class="svc-living__sr"> reviews</span>)</span></p>
        </div>
        <a class="svc-living__link" href="#book-locks">Book locks &amp; security <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </li>

      <li class="svc-living__card" style="--svc-living-hue: color-mix(in srgb, var(--primary-2) 60%, var(--primary))">
        <div class="svc-living__top">
          <span class="svc-living__tile" aria-hidden="true">
            <svg class="svc-living__icon" viewBox="0 0 24 24" width="28" height="28" focusable="false">
              <path class="svc-living__rain" d="M8.5 .9v1.6M15 .9v1.6" />
              <path d="M4 8.5 7 4h10l3 4.5" />
              <path d="M2.5 8.5h19v.8a2.2 2.2 0 0 1-2.2 2.2H4.7a2.2 2.2 0 0 1-2.2-2.2z" />
              <path d="M5 11.5v9h9.5v-9M8 15h3.5v2.5H8z" />
              <path d="M18 11.5v7a2 2 0 0 0 2 2h1.5" />
              <path class="svc-living__flow" d="M4.6 10h3.2" />
              <path class="svc-living__drip" d="M21.6 21.3c.45.55.75 1 .75 1.4a.75.75 0 0 1-1.5 0c0-.4.3-.85.75-1.4z" />
            </svg>
          </span>
          <p class="svc-living__eta"><span class="svc-living__dot" aria-hidden="true"></span><span class="svc-living__sr">Available </span>Today</p>
        </div>
        <h3 class="svc-living__name">Gutters</h3>
        <p class="svc-living__benefit">Cleaning, guards and repairs, with every scrap hauled away.</p>
        <div class="svc-living__meta">
          <p class="svc-living__price"><small>from</small> $119</p>
          <p class="svc-living__rating"><svg class="svc-living__star" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>4.9<span class="svc-living__sr"> out of 5,</span> <span class="svc-living__count">(740<span class="svc-living__sr"> reviews</span>)</span></p>
        </div>
        <a class="svc-living__link" href="#book-gutters">Book gutters <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </li>
    </ul>

    <div class="svc-living__foot">
      <p>Not sure who you need? Call <a href="tel:+15555550123">(555) 555-0123</a> and we'll send the right pro.</p>
      <a class="svc-living__cta" href="#quote">Describe the problem <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section: muted light surface with two soft pools of brand light */
.svc-living {
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(60rem 26rem at 8% -12%, color-mix(in srgb, var(--primary) 9%, transparent), transparent 70%),
    radial-gradient(48rem 24rem at 96% -6%, color-mix(in srgb, var(--primary-2) 9%, transparent), transparent 70%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
.svc-living__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }

/* Heading */
.svc-living__head { max-width: 40rem; margin: 0 auto clamp(2.5rem, 5vw, 3.5rem); text-align: center; }
.svc-living__eyebrow { display: inline-flex; align-items: center; gap: 0.625rem; margin: 0; color: var(--primary); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.svc-living__eyebrow::before, .svc-living__eyebrow::after { content: ""; width: 1.25rem; height: 1px; background: currentColor; opacity: 0.45; }
.svc-living__title { margin: 0.875rem 0 0; font: 600 clamp(2rem, 1.25rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.svc-living__glow { background: linear-gradient(100deg, var(--primary), var(--primary-2)); -webkit-background-clip: text; background-clip: text; color: transparent; }
.svc-living__intro { max-width: 34rem; margin: 1rem auto 0; color: var(--text-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }

/* Grid: 1 → 2 → 3 columns */
.svc-living__grid { display: grid; gap: var(--space-md); margin: 0; padding: 0; list-style: none; }
@media (min-width: 600px) { .svc-living__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-lg); } }
@media (min-width: 1024px) { .svc-living__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); } }

/* Card: gradient hairline (border-box layers) under a white face (padding-box layers).
   Layer 1 is a faint sheen across the face, layer 3 the glint on the hairline; both sweep on hover. */
.svc-living__card {
  --svc-living-ink: color-mix(in srgb, var(--svc-living-hue) 62%, var(--text-main));
  position: relative; display: flex; flex-direction: column; gap: 0.5rem;
  padding: var(--space-lg); border: 1px solid transparent; border-radius: var(--radius-2xl);
  background:
    linear-gradient(115deg, transparent 40%, color-mix(in srgb, var(--svc-living-hue) 7%, transparent) 50%, transparent 60%) padding-box,
    linear-gradient(180deg, var(--surface-light), color-mix(in srgb, var(--surface-muted) 55%, var(--surface-light))) padding-box,
    linear-gradient(115deg, transparent 40%, color-mix(in srgb, var(--svc-living-hue) 85%, var(--surface-light)) 47%, var(--primary-2) 53%, transparent 60%) border-box,
    linear-gradient(160deg, color-mix(in srgb, var(--svc-living-hue) 32%, var(--border-subtle)), var(--border-subtle) 42%, var(--border-subtle) 70%, color-mix(in srgb, var(--svc-living-hue) 16%, var(--border-subtle))) border-box;
  background-size: 300% 100%, 100% 100%, 300% 100%, 100% 100%;
  background-position: 100% 0, 0 0, 100% 0, 0 0;
  background-repeat: no-repeat;
  box-shadow: var(--shadow-sm), 0 18px 36px -28px color-mix(in srgb, var(--svc-living-hue) 55%, transparent);
  transition: transform var(--dur-4) var(--ease-spring);
}
/* Raised shadow lives on a pseudo-element so hover only fades its opacity */
.svc-living__card::before {
  content: ""; position: absolute; inset: -1px; z-index: -1; border-radius: inherit; pointer-events: none; opacity: 0;
  box-shadow: 0 2px 6px color-mix(in srgb, var(--text-main) 5%, transparent), 0 30px 56px -26px color-mix(in srgb, var(--svc-living-hue) 50%, transparent);
  transition: opacity var(--dur-3) var(--ease-out);
}
.svc-living__card:focus-within { transform: translateY(-4px); }
@media (hover: hover) {
  .svc-living__card:hover { transform: translateY(-6px); }
  .svc-living__card:hover::before { opacity: 1; }
}
/* The glint: only entering hover/focus transitions the position; leaving snaps back off-card unseen */
.svc-living__card:is(:hover, :focus-within) {
  background-position: 0% 0, 0 0, 0% 0, 0 0;
  transition: transform var(--dur-4) var(--ease-spring), background-position var(--dur-5) var(--ease-out);
}

/* Top row: icon tile and "Today" chip */
.svc-living__top { display: flex; align-items: flex-start; justify-content: space-between; gap: var(--space-md); margin-bottom: 0.75rem; }
.svc-living__tile {
  flex: none; display: grid; place-items: center; width: 3.5rem; height: 3.5rem; border-radius: var(--radius-xl);
  color: var(--svc-living-ink);
  background: linear-gradient(145deg, color-mix(in srgb, var(--svc-living-hue) 16%, var(--surface-light)), color-mix(in srgb, var(--svc-living-hue) 5%, var(--surface-light)));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--svc-living-hue) 20%, transparent), var(--highlight), 0 10px 20px -14px color-mix(in srgb, var(--svc-living-hue) 80%, transparent);
}
.svc-living__icon { display: block; overflow: visible; fill: none; stroke: currentColor; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
.svc-living__eta {
  display: inline-flex; align-items: center; gap: 0.4375rem; margin: 0; padding: 0.375rem 0.625rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--success) 8%, var(--surface-light)); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--success) 18%, transparent);
  color: color-mix(in srgb, var(--success) 80%, var(--text-main)); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.02em;
}
.svc-living__dot { position: relative; width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 16%, transparent); }
.svc-living__dot::after { content: ""; position: absolute; inset: 0; border-radius: inherit; background: var(--success); opacity: 0; }
.svc-living__card.is-seen .svc-living__dot::after { animation: svc-living-ping 1.4s var(--ease-out) 0.6s 3; }

/* Copy, price and rating */
.svc-living__name { margin: 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.svc-living__benefit { margin: 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.55; }
.svc-living__meta { display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; margin-top: auto; padding-top: var(--space-md); }
.svc-living__price { margin: 0; font: 600 1.375rem/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }
.svc-living__price small { margin-right: 0.125rem; color: var(--text-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0; }
.svc-living__rating { display: inline-flex; align-items: center; gap: 0.3125rem; margin: 0; font-size: 0.875rem; font-weight: 600; font-variant-numeric: tabular-nums; }
.svc-living__count { color: var(--text-muted); font-weight: 500; }
.svc-living__star { flex: none; fill: color-mix(in srgb, var(--accent) 85%, var(--warning)); stroke: color-mix(in srgb, var(--accent) 55%, var(--warning)); stroke-width: 1.5; stroke-linejoin: round; }

/* Stretched link: its ::after covers the card, so the whole card is one target */
.svc-living__link {
  display: flex; align-items: center; justify-content: space-between; gap: 0.75rem;
  margin-top: 0.75rem; padding-top: var(--space-md); border-top: 1px solid var(--border-subtle);
  color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
}
.svc-living__link::after { content: ""; position: absolute; inset: -1px; border-radius: var(--radius-2xl); }
.svc-living__link svg {
  flex: none; box-sizing: border-box; width: 2rem; height: 2rem; padding: 0.5rem; border-radius: 50%;
  background: color-mix(in srgb, var(--svc-living-hue) 12%, var(--surface-light)); color: var(--svc-living-ink);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2) var(--ease-out), color var(--dur-2) var(--ease-out);
}
.svc-living__card:is(:hover, :focus-within) .svc-living__link svg { transform: translateX(3px); background: var(--svc-living-ink); color: var(--surface-light); }
.svc-living__link:focus-visible { outline: 2px solid transparent; }
.svc-living__link:focus-visible::after { box-shadow: var(--focus-ring); }

/* Living icons. The resting style of every part IS the story's last frame, so a finished,
   interrupted or reduced-motion icon always looks complete. */
.svc-living__drop, .svc-living__drip { fill: color-mix(in srgb, var(--svc-living-hue) 30%, transparent); }
.svc-living__drop, .svc-living__ring, .svc-living__bolt, .svc-living__spark, .svc-living__course,
.svc-living__shackle, .svc-living__key, .svc-living__keyhole, .svc-living__rain, .svc-living__flow, .svc-living__drip { transform-box: fill-box; transform-origin: center; }
.svc-living__drop, .svc-living__drip { transform-origin: 50% 0; }
.svc-living__blades { transform-box: view-box; transform-origin: 50% 50%; }
.svc-living__bolt { fill: var(--svc-living-hue); fill-opacity: 0; }
.svc-living__ring, .svc-living__spark, .svc-living__key, .svc-living__rain, .svc-living__flow, .svc-living__drip { opacity: 0; visibility: hidden; }
.svc-living__ring--outer { --svc-living-d: 140ms; }
.svc-living__spark { --svc-living-sx: 1.6px; --svc-living-sy: -1.6px; }
.svc-living__spark--low { --svc-living-sx: -1.6px; --svc-living-sy: 1.6px; --svc-living-d: 60ms; }
.svc-living__course--2 { --svc-living-d: 220ms; }
.svc-living__course--3 { --svc-living-d: 440ms; }

/* Each part names its own story; one trigger rule plays them all */
.svc-living__drop { --svc-living-story: svc-living-drop 1.4s var(--ease-in-out) both; }
.svc-living__ring { --svc-living-story: svc-living-ring 1.4s var(--ease-out) var(--svc-living-d, 0ms) both; }
.svc-living__bolt { --svc-living-story: svc-living-flicker 1.2s var(--ease-in-out) both; }
.svc-living__spark { --svc-living-story: svc-living-spark 1.2s var(--ease-out) var(--svc-living-d, 0ms) both; }
.svc-living__blades { --svc-living-story: svc-living-spin 1.6s var(--ease-in-out) both; }
.svc-living__course { --svc-living-story: svc-living-course 0.6s var(--ease-spring) var(--svc-living-d, 0ms) both; }
.svc-living__shackle { --svc-living-story: svc-living-shackle 1.5s var(--ease-in-out) both; }
.svc-living__key { --svc-living-story: svc-living-key 1.5s var(--ease-out) both; }
.svc-living__keyhole { --svc-living-story: svc-living-keyhole 1.5s var(--ease-in-out) both; }
.svc-living__rain { --svc-living-story: svc-living-rain 1.6s var(--ease-in-out) both; }
.svc-living__flow { --svc-living-story: svc-living-flow 1.6s var(--ease-in-out) both; }
.svc-living__drip { --svc-living-story: svc-living-drip 1.6s var(--ease-in-out) both; }
/* Hover and focus restart the story every time; .is-playing is the one-off entrance from JS */
.svc-living__card:is(:hover, :focus-within, .is-playing) :is(.svc-living__drop, .svc-living__ring, .svc-living__bolt, .svc-living__spark, .svc-living__blades,
  .svc-living__course, .svc-living__shackle, .svc-living__key, .svc-living__keyhole, .svc-living__rain, .svc-living__flow, .svc-living__drip) {
  animation: var(--svc-living-story);
}

/* Footer CTA */
.svc-living__foot { display: flex; flex-direction: column; align-items: center; gap: var(--space-md); margin-top: clamp(2.5rem, 5vw, 3.5rem); text-align: center; }
.svc-living__foot p { margin: 0; color: var(--text-muted); }
.svc-living__foot p a { color: var(--text-main); font-weight: 600; text-decoration-color: color-mix(in srgb, var(--primary) 45%, transparent); text-underline-offset: 3px; }
.svc-living__cta {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: var(--text-main); color: var(--surface-light); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: var(--highlight-inverse), 0 12px 28px -12px color-mix(in srgb, var(--text-main) 70%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.svc-living__cta svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.svc-living__cta:hover svg { transform: translateX(3px); }
.svc-living__cta:active { transform: scale(0.97); }
.svc-living__foot a:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
@media (min-width: 768px) { .svc-living__foot { flex-direction: row; justify-content: center; gap: var(--space-lg); } }

.svc-living__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

@media (prefers-reduced-motion: reduce) {
  .svc-living *, .svc-living *::before, .svc-living *::after { animation: none !important; }
}

/* Faucet: the hanging drop stretches, falls, splashes into two rings, and a new drop forms */
@keyframes svc-living-drop {
  0% { transform: none; }
  14% { transform: scaleY(1.22); }
  24% { transform: translateY(0.8px) scaleY(1.15); }
  34% { transform: translateY(3.4px) scaleY(1.1); opacity: 1; }
  38%, 72% { transform: translateY(3.8px) scale(0.3); opacity: 0; }
  74% { transform: scale(0); opacity: 0; }
  76% { transform: scale(0); opacity: 1; }
  100% { transform: none; opacity: 1; }
}
@keyframes svc-living-ring {
  0%, 33% { opacity: 0; transform: scale(0.2); visibility: visible; }
  40% { opacity: 1; }
  100% { opacity: 0; transform: scale(1.15); visibility: hidden; }
}
/* Bolt: two flickers, a charged flash, two sparks thrown outwards */
@keyframes svc-living-flicker {
  0% { opacity: 1; }
  6% { opacity: 0.2; }
  12% { opacity: 1; }
  18% { opacity: 0.35; }
  26% { opacity: 1; fill-opacity: 0; transform: none; }
  34% { fill-opacity: 0.4; transform: scale(1.08); }
  70%, 100% { opacity: 1; fill-opacity: 0; transform: none; }
}
@keyframes svc-living-spark {
  0%, 28% { opacity: 0; transform: scale(0.4); visibility: visible; }
  36% { opacity: 1; }
  80%, 100% { opacity: 0; transform: translate(var(--svc-living-sx), var(--svc-living-sy)) scale(1.15); visibility: hidden; }
}
/* Fan: two turns that spin up and ease to rest (720deg looks identical to 0deg) */
@keyframes svc-living-spin { to { transform: rotate(720deg); } }
/* Roof: courses drop in from the eaves up and land on a spring */
@keyframes svc-living-course { from { opacity: 0; transform: translateY(-4px); } }
/* Lock: shackle lifts, the key flies into the keyhole and turns, the shackle clicks shut, the key comes out */
@keyframes svc-living-shackle {
  0% { transform: none; }
  16%, 46% { transform: translateY(-2.6px); }
  54% { transform: translateY(0.5px); }
  62% { transform: translateY(-0.3px); }
  70%, 100% { transform: none; }
}
@keyframes svc-living-key {
  0% { opacity: 0; transform: translate(4px, 4px) scale(1.6); visibility: visible; }
  26% { opacity: 1; transform: none; }
  46%, 72% { opacity: 1; transform: rotate(90deg); }
  100% { opacity: 0; transform: rotate(90deg) scale(1.35); visibility: hidden; }
}
@keyframes svc-living-keyhole {
  0%, 14% { opacity: 1; }
  24%, 80% { opacity: 0; }
  100% { opacity: 1; }
}
/* Gutter: rain hits the roof, runs along the trough, drips from the downspout */
@keyframes svc-living-rain {
  0% { opacity: 0; transform: translateY(-1px); visibility: visible; }
  8% { opacity: 1; }
  26%, 100% { opacity: 0; transform: translateY(2.2px); visibility: hidden; }
}
@keyframes svc-living-flow {
  0%, 22% { opacity: 0; transform: none; visibility: visible; }
  30%, 60% { opacity: 1; }
  68%, 100% { opacity: 0; transform: translateX(10.5px); visibility: hidden; }
}
@keyframes svc-living-drip {
  0%, 62% { opacity: 0; transform: scale(0); visibility: visible; }
  64% { opacity: 1; }
  78% { opacity: 1; transform: none; }
  96%, 100% { opacity: 0; transform: translateY(1.8px); visibility: hidden; }
}
@keyframes svc-living-ping { from { opacity: 0.6; transform: none; } to { opacity: 0; transform: scale(2.8); } }
```

## JS

```js
// Play each icon's story once, staggered, the first time its card scrolls into view.
// Hover and focus replays are pure CSS, so this file only handles the entrance.
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('[data-svc-living]').forEach((root) => {
  if (!('IntersectionObserver' in window)) return;
  const cards = [...root.querySelectorAll('.svc-living__card')];

  // is-playing is short-lived: if it stayed on, hover could never restart the same animation
  const play = (card, delay) => {
    setTimeout(() => {
      card.classList.add('is-playing');
      setTimeout(() => card.classList.remove('is-playing'), 1800);
    }, delay);
  };

  const io = new IntersectionObserver((entries) => {
    entries.filter((entry) => entry.isIntersecting).forEach((entry, n) => {
      io.unobserve(entry.target);
      entry.target.classList.add('is-seen');
      if (!reduce.matches) play(entry.target, n * 140);
    });
  }, { threshold: 0.6 });

  cards.forEach((card) => io.observe(card));
});
```

## Notes

- Each card is one stretched link ("Book plumbing"): its `::after` covers the card and carries the focus ring, so the whole card is a single tab stop. Icons are `aria-hidden`; the chip reads "Available Today" and ratings read "4.9 out of 5, (2,140 reviews)".
- Every animated part's resting style is its story's last frame, so an icon always rests complete. Hover and `:focus-within` restart the CSS story each time. JS adds `is-seen` once per card, which also pings the "Today" dot three times (4.8s, then still), plus a short-lived `is-playing` class for the staggered entrance. A class that stayed on would block hover replays, because re-applying the same animation name doesn't restart it.
- Without JS everything renders and the hover and focus stories still play; only the entrance and the ping are skipped. Under reduced motion all keyframes are off and icons show their final frame; the lift and glint become instant through the motion tokens.
- Contrast: chip text (`--success` mixed with `--text-main` on an 8% tint) is about 5.4:1, muted copy on the card face at least 4.6:1, and the gradient headline words are display size (at least 3.6:1). Icon ink mixes the card hue 62/38 with `--text-main`, staying above 3:1 on its tile even for amber.
- Retheme each card with `--svc-living-hue` (any token or `color-mix()`); the tile, ink, hairline, glint and shadows all derive from it. To add a service, draw a 24×24 stroke icon, give its moving parts a class that sets `--svc-living-story`, and add that class to the trigger's `:is()` list.
