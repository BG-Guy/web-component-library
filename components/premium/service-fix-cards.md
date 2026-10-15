# Problem → Fixed Service Cards

Photo-led service cards that prove the work. Hover a card, focus its link or tap "See the fix", and a diagonal wipe with a bright squeegee edge sweeps the problem photo away to reveal the finished job, while the status chip morphs from an amber warning ("Leaking water heater") to green ("Fixed in 2 h") as its check draws and the "What we did" list ticks itself off. The first card plays one teaser wipe and return when it first scrolls into view. One column on phones, a 2×2 grid from 600px. Depends on `tokens/variables.css`.

**Motion:** a registered `--svc-fix-p` (0–1) drives the clip-path wipe, edge glint, chip colour sweep, label roll, width morph and check draw together (`--dur-5`, `--ease-in-out`) · one 1.6s teaser on the first card · toggle icon flip (`--ease-spring`) · card lift (`--dur-4`, `--ease-spring`).

## HTML

```html
<section class="svc-fix" aria-labelledby="svc-fix-title" data-svc-fix>
  <div class="svc-fix__inner">
    <header class="svc-fix__head">
      <div>
        <p class="svc-fix__eyebrow">Real jobs · this month</p>
        <h2 id="svc-fix-title" class="svc-fix__title">See the problem. <span class="svc-fix__glow">Then see it fixed.</span></h2>
      </div>
      <p class="svc-fix__intro">Every visit is photographed before and after, so you know exactly what you paid for.<span class="svc-fix__hint"> Hover a photo, or tap “See the fix”.</span></p>
    </header>

    <ul class="svc-fix__grid" role="list">
      <li class="svc-fix__card">
        <div class="svc-fix__media">
          <figure class="svc-fix__shot svc-fix__shot--before">
            <img src="water-heater-before.jpg" alt="Rusty water heater leaking onto a stained concrete floor" width="800" height="600" loading="lazy" decoding="async">
            <figcaption class="svc-fix__tag">Before<span class="svc-fix__tag-note">: leaking water heater</span></figcaption>
          </figure>
          <figure class="svc-fix__shot svc-fix__shot--after">
            <img src="water-heater-after.jpg" alt="The same water heater with a new relief valve and a clean, dry floor" width="800" height="600" loading="lazy" decoding="async">
            <figcaption class="svc-fix__tag">After<span class="svc-fix__tag-note">: fixed in 2 hours</span></figcaption>
          </figure>
          <span class="svc-fix__edge" aria-hidden="true"></span>
          <p class="svc-fix__status" aria-hidden="true">
            <svg class="svc-fix__status-icon" viewBox="0 0 24 24" width="16" height="16" focusable="false"><path class="svc-fix__warn" d="M12 4 3 19.5h18zM12 10v4M12 16.8v.2" /><path class="svc-fix__check" d="m5.5 12.5 4.5 4.5 8.5-9.5" pathLength="1" /></svg>
            <span class="svc-fix__status-text">
              <span class="svc-fix__status-label">Leaking water heater</span>
              <span class="svc-fix__status-label svc-fix__status-label--fixed">Fixed in 2 h</span>
            </span>
          </p>
          <button class="svc-fix__toggle" type="button" aria-pressed="false" hidden>
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 4h14a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zM4.5 19.5l15-15" /></svg>
            See the fix<span class="svc-fix__sr">: water heater</span>
          </button>
        </div>
        <div class="svc-fix__body">
          <div class="svc-fix__name-row">
            <span class="svc-fix__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><rect x="6" y="2.5" width="12" height="18" rx="3" /><path d="M6 7.5h12M12 10.5s-2 2.2-2 3.6a2 2 0 0 0 4 0c0-1.4-2-3.6-2-3.6zM9 20.5v1.5M15 20.5v1.5" /></svg></span>
            <h3 class="svc-fix__name">Water heater repair</h3>
          </div>
          <p class="svc-fix__benefit">Hot water back the same day, with the cause found, not just patched.</p>
          <h4 class="svc-fix__did">What we did</h4>
          <ul class="svc-fix__steps" role="list">
            <li style="--svc-fix-i: 0">Drained and flushed the tank</li>
            <li style="--svc-fix-i: 1">Replaced the pressure relief valve</li>
            <li style="--svc-fix-i: 2">Pressure-tested every joint</li>
          </ul>
          <div class="svc-fix__foot">
            <p class="svc-fix__price"><small>from</small> $189</p>
            <a class="svc-fix__link" href="#book-water-heater">Book this fix<span class="svc-fix__sr">: water heater repair</span> <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </div>
      </li>

      <li class="svc-fix__card">
        <div class="svc-fix__media">
          <figure class="svc-fix__shot svc-fix__shot--before">
            <img src="kitchen-drain-before.jpg" alt="Kitchen sink full of standing grey water" width="800" height="600" loading="lazy" decoding="async">
            <figcaption class="svc-fix__tag">Before<span class="svc-fix__tag-note">: blocked kitchen drain</span></figcaption>
          </figure>
          <figure class="svc-fix__shot svc-fix__shot--after">
            <img src="kitchen-drain-after.jpg" alt="The same sink, empty and draining freely" width="800" height="600" loading="lazy" decoding="async">
            <figcaption class="svc-fix__tag">After<span class="svc-fix__tag-note">: cleared in 45 minutes</span></figcaption>
          </figure>
          <span class="svc-fix__edge" aria-hidden="true"></span>
          <p class="svc-fix__status" aria-hidden="true">
            <svg class="svc-fix__status-icon" viewBox="0 0 24 24" width="16" height="16" focusable="false"><path class="svc-fix__warn" d="M12 4 3 19.5h18zM12 10v4M12 16.8v.2" /><path class="svc-fix__check" d="m5.5 12.5 4.5 4.5 8.5-9.5" pathLength="1" /></svg>
            <span class="svc-fix__status-text">
              <span class="svc-fix__status-label">Blocked kitchen drain</span>
              <span class="svc-fix__status-label svc-fix__status-label--fixed">Cleared in 45 min</span>
            </span>
          </p>
          <button class="svc-fix__toggle" type="button" aria-pressed="false" hidden>
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 4h14a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zM4.5 19.5l15-15" /></svg>
            See the fix<span class="svc-fix__sr">: kitchen drain</span>
          </button>
        </div>
        <div class="svc-fix__body">
          <div class="svc-fix__name-row">
            <span class="svc-fix__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M3 11h18v1.5a6.5 6.5 0 0 1-6.5 6.5h-5A6.5 6.5 0 0 1 3 12.5zM12 19v2.5M9 21.5h6M15.5 11V6a2 2 0 0 0-4 0" /></svg></span>
            <h3 class="svc-fix__name">Drain cleaning</h3>
          </div>
          <p class="svc-fix__benefit">Clogs cleared with a camera check, so they stay cleared.</p>
          <h4 class="svc-fix__did">What we did</h4>
          <ul class="svc-fix__steps" role="list">
            <li style="--svc-fix-i: 0">Camera-inspected the line</li>
            <li style="--svc-fix-i: 1">Hydro-jetted the grease build-up</li>
            <li style="--svc-fix-i: 2">Fitted a new trap seal</li>
          </ul>
          <div class="svc-fix__foot">
            <p class="svc-fix__price"><small>from</small> $129</p>
            <a class="svc-fix__link" href="#book-drain">Book this fix<span class="svc-fix__sr">: drain cleaning</span> <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </div>
      </li>

      <li class="svc-fix__card">
        <div class="svc-fix__media">
          <figure class="svc-fix__shot svc-fix__shot--before">
            <img src="breaker-panel-before.jpg" alt="Open breaker panel with a tripped switch and tangled, unlabelled wires" width="800" height="600" loading="lazy" decoding="async">
            <figcaption class="svc-fix__tag">Before<span class="svc-fix__tag-note">: breaker keeps tripping</span></figcaption>
          </figure>
          <figure class="svc-fix__shot svc-fix__shot--after">
            <img src="breaker-panel-after.jpg" alt="The same panel with neat wiring, a new circuit and every breaker labelled" width="800" height="600" loading="lazy" decoding="async">
            <figcaption class="svc-fix__tag">After<span class="svc-fix__tag-note">: fixed in 3 hours</span></figcaption>
          </figure>
          <span class="svc-fix__edge" aria-hidden="true"></span>
          <p class="svc-fix__status" aria-hidden="true">
            <svg class="svc-fix__status-icon" viewBox="0 0 24 24" width="16" height="16" focusable="false"><path class="svc-fix__warn" d="M12 4 3 19.5h18zM12 10v4M12 16.8v.2" /><path class="svc-fix__check" d="m5.5 12.5 4.5 4.5 8.5-9.5" pathLength="1" /></svg>
            <span class="svc-fix__status-text">
              <span class="svc-fix__status-label">Breaker keeps tripping</span>
              <span class="svc-fix__status-label svc-fix__status-label--fixed">Fixed in 3 h</span>
            </span>
          </p>
          <button class="svc-fix__toggle" type="button" aria-pressed="false" hidden>
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 4h14a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zM4.5 19.5l15-15" /></svg>
            See the fix<span class="svc-fix__sr">: breaker panel</span>
          </button>
        </div>
        <div class="svc-fix__body">
          <div class="svc-fix__name-row">
            <span class="svc-fix__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><rect x="5" y="2.5" width="14" height="19" rx="2" /><path d="M8.5 7h2.5M13 7h2.5M8.5 11h2.5M13 11h2.5M8.5 15h2.5M13 15h2.5" /></svg></span>
            <h3 class="svc-fix__name">Electrical panel repair</h3>
          </div>
          <p class="svc-fix__benefit">Safe, labelled circuits and no more surprise outages.</p>
          <h4 class="svc-fix__did">What we did</h4>
          <ul class="svc-fix__steps" role="list">
            <li style="--svc-fix-i: 0">Traced the overloaded circuit</li>
            <li style="--svc-fix-i: 1">Added a dedicated 20 A line</li>
            <li style="--svc-fix-i: 2">Labelled every breaker</li>
          </ul>
          <div class="svc-fix__foot">
            <p class="svc-fix__price"><small>from</small> $149</p>
            <a class="svc-fix__link" href="#book-panel">Book this fix<span class="svc-fix__sr">: electrical panel repair</span> <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </div>
      </li>

      <li class="svc-fix__card">
        <div class="svc-fix__media">
          <figure class="svc-fix__shot svc-fix__shot--before">
            <img src="roof-before.jpg" alt="Roof with torn and missing shingles after a storm" width="800" height="600" loading="lazy" decoding="async">
            <figcaption class="svc-fix__tag">Before<span class="svc-fix__tag-note">: storm-damaged shingles</span></figcaption>
          </figure>
          <figure class="svc-fix__shot svc-fix__shot--after">
            <img src="roof-after.jpg" alt="The same roof with matched new shingles and resealed flashing" width="800" height="600" loading="lazy" decoding="async">
            <figcaption class="svc-fix__tag">After<span class="svc-fix__tag-note">: fixed in 1 day</span></figcaption>
          </figure>
          <span class="svc-fix__edge" aria-hidden="true"></span>
          <p class="svc-fix__status" aria-hidden="true">
            <svg class="svc-fix__status-icon" viewBox="0 0 24 24" width="16" height="16" focusable="false"><path class="svc-fix__warn" d="M12 4 3 19.5h18zM12 10v4M12 16.8v.2" /><path class="svc-fix__check" d="m5.5 12.5 4.5 4.5 8.5-9.5" pathLength="1" /></svg>
            <span class="svc-fix__status-text">
              <span class="svc-fix__status-label">Storm-damaged shingles</span>
              <span class="svc-fix__status-label svc-fix__status-label--fixed">Fixed in 1 day</span>
            </span>
          </p>
          <button class="svc-fix__toggle" type="button" aria-pressed="false" hidden>
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 4h14a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zM4.5 19.5l15-15" /></svg>
            See the fix<span class="svc-fix__sr">: roof</span>
          </button>
        </div>
        <div class="svc-fix__body">
          <div class="svc-fix__name-row">
            <span class="svc-fix__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M3 11.5 12 4l9 7.5M5.5 9.5v11h13v-11M15 6.5V3.5h2.5V8.6M10 20.5v-5h4v5" /></svg></span>
            <h3 class="svc-fix__name">Roof repair</h3>
          </div>
          <p class="svc-fix__benefit">Leaks sealed before the next storm, with matched shingles.</p>
          <h4 class="svc-fix__did">What we did</h4>
          <ul class="svc-fix__steps" role="list">
            <li style="--svc-fix-i: 0">Replaced 40 torn shingles</li>
            <li style="--svc-fix-i: 1">Resealed the chimney flashing</li>
            <li style="--svc-fix-i: 2">Cleared the valleys and gutters</li>
          </ul>
          <div class="svc-fix__foot">
            <p class="svc-fix__price"><small>from</small> $329</p>
            <a class="svc-fix__link" href="#book-roof">Book this fix<span class="svc-fix__sr">: roof repair</span> <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </div>
      </li>
    </ul>

    <div class="svc-fix__cta">
      <p><strong>Got a problem like these?</strong> Send us a photo and get a fixed-price quote in 15 minutes.</p>
      <a class="svc-fix__cta-btn" href="#photo-quote">Send a photo <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
    </div>
  </div>
</section>
```

## CSS

```css
/* One progress value drives the whole reveal: 0 = problem, 1 = fixed */
@property --svc-fix-p { syntax: "<number>"; inherits: true; initial-value: 0; }

/* Section: warm paper white */
.svc-fix {
  background:
    radial-gradient(56rem 24rem at 100% 0%, color-mix(in srgb, var(--accent) 10%, transparent), transparent 70%),
    color-mix(in srgb, var(--accent) 4%, var(--surface-light));
  color: var(--text-main); font-family: var(--font-sans);
}
.svc-fix__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }

/* Split header */
.svc-fix__head { display: grid; gap: var(--space-md); margin-bottom: clamp(2.25rem, 5vw, 3.5rem); }
@media (min-width: 768px) { .svc-fix__head { grid-template-columns: 1.25fr 1fr; align-items: end; gap: var(--space-2xl); } }
.svc-fix__eyebrow { margin: 0; color: var(--warning); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.svc-fix__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.25rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.svc-fix__glow { background: linear-gradient(100deg, var(--success), var(--primary-2)); -webkit-background-clip: text; background-clip: text; color: transparent; }
.svc-fix__intro { max-width: 30rem; margin: 0; color: var(--text-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }
.svc-fix:not(.svc-fix--js) .svc-fix__hint { display: none; }

/* Grid: 1 column, then 2×2 */
.svc-fix__grid { display: grid; gap: var(--space-lg); margin: 0; padding: 0; list-style: none; }
@media (min-width: 600px) { .svc-fix__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (min-width: 1024px) { .svc-fix__grid { gap: var(--space-xl); } }

/* Card: photo on a white mat (outer radius = inner radius + padding) */
.svc-fix__card {
  display: flex; flex-direction: column; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-lg);
  transition: transform var(--dur-4) var(--ease-spring);
}
@media (hover: hover) { .svc-fix__card:hover { transform: translateY(-4px); } }

/* Photos. Without JS they stack, each labelled Before / After */
.svc-fix__media { position: relative; display: grid; gap: var(--space-sm); padding: var(--space-sm); }
.svc-fix__shot {
  position: relative; margin: 0; overflow: hidden; aspect-ratio: 4 / 3; border-radius: var(--radius-xl);
  background: linear-gradient(135deg, color-mix(in srgb, var(--warning) 28%, var(--surface-muted)), color-mix(in srgb, var(--text-main) 14%, var(--surface-muted)));
}
.svc-fix__shot--after { background: linear-gradient(135deg, color-mix(in srgb, var(--success) 22%, var(--surface-muted)), color-mix(in srgb, var(--primary-2) 16%, var(--surface-muted))); }
.svc-fix__shot img { display: block; width: 100%; height: 100%; object-fit: cover; }
.svc-fix__tag {
  position: absolute; left: 0.75rem; bottom: 0.75rem; max-width: calc(100% - 1.5rem); padding: 0.375rem 0.625rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 72%, transparent); color: var(--text-inverse);
  font: 600 0.6875rem/1.25 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase;
}
.svc-fix__tag-note { font-family: var(--font-sans); letter-spacing: 0; text-transform: none; }

/* With JS: both photos share one frame and the "before" is clipped away along a diagonal */
.svc-fix--js .svc-fix__card { --svc-fix-p: 0; transition: transform var(--dur-4) var(--ease-spring), --svc-fix-p var(--dur-5) var(--ease-in-out); }
@media (hover: hover) {
  .svc-fix--js .svc-fix__card:hover { --svc-fix-p: 1; }
  /* Over the toggle, show the pinned state so a click visibly does something */
  .svc-fix--js .svc-fix__card:has(.svc-fix__toggle:hover):not(.is-fixed) { --svc-fix-p: 0; }
}
.svc-fix--js .svc-fix__card.is-fixed { --svc-fix-p: 1; }
.svc-fix--js .svc-fix__card:has(.svc-fix__link:focus-visible) { --svc-fix-p: 1; }
.svc-fix--js .svc-fix__card.is-teasing { animation: svc-fix-tease 1.6s var(--ease-in-out) both; }

.svc-fix--js .svc-fix__media { gap: 0; }
.svc-fix--js .svc-fix__shot, .svc-fix--js .svc-fix__edge { grid-area: 1 / 1; }
.svc-fix--js .svc-fix__tag-note { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.svc-fix--js .svc-fix__shot--before {
  z-index: 1;
  clip-path: polygon(calc(var(--svc-fix-p) * 130%) 0, 100% 0, 100% 100%, calc(var(--svc-fix-p) * 130% - 30%) 100%);
}
/* Squeegee edge: a soft halo and a bright core riding the wipe line, visible only mid-sweep */
.svc-fix__edge { display: none; }
.svc-fix--js .svc-fix__edge {
  --svc-fix-x: calc(var(--svc-fix-p) * 130%);
  position: relative; z-index: 2; display: block; border-radius: var(--radius-xl); pointer-events: none;
  opacity: min(1, calc(var(--svc-fix-p) * 8), calc((1 - var(--svc-fix-p)) * 8));
}
.svc-fix--js .svc-fix__edge::before, .svc-fix--js .svc-fix__edge::after { content: ""; position: absolute; inset: 0; border-radius: inherit; }
.svc-fix--js .svc-fix__edge::before {
  background: color-mix(in srgb, var(--surface-light) 28%, transparent);
  clip-path: polygon(calc(var(--svc-fix-x) - 4%) 0, calc(var(--svc-fix-x) + 2.5%) 0, calc(var(--svc-fix-x) - 27.5%) 100%, calc(var(--svc-fix-x) - 34%) 100%);
}
.svc-fix--js .svc-fix__edge::after {
  background: color-mix(in srgb, var(--surface-light) 92%, transparent);
  clip-path: polygon(calc(var(--svc-fix-x) - 0.4%) 0, calc(var(--svc-fix-x) + 0.4%) 0, calc(var(--svc-fix-x) - 29.6%) 100%, calc(var(--svc-fix-x) - 30.4%) 100%);
}

/* Status chip: green sweeps in over amber, the label rolls, the slot morphs between the two widths */
.svc-fix__status { display: none; }
.svc-fix--js .svc-fix__status {
  position: absolute; z-index: 3; top: 1.25rem; left: 1.25rem; isolation: isolate; overflow: hidden;
  display: inline-flex; align-items: center; gap: 0.4375rem; margin: 0; padding: 0.4375rem 0.75rem 0.4375rem 0.5625rem;
  border-radius: var(--radius-full); background: var(--warning); color: var(--text-inverse); font: 600 0.8125rem/1.2 var(--font-sans);
  box-shadow: var(--highlight), 0 10px 24px -12px color-mix(in srgb, var(--surface-deep) 70%, transparent);
}
.svc-fix--js .svc-fix__status::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--success); clip-path: inset(0 calc((1 - var(--svc-fix-p)) * 100%) 0 0); }
.svc-fix__status-icon { flex: none; overflow: visible; fill: none; stroke: currentColor; stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; }
.svc-fix__warn { transform-box: fill-box; transform-origin: center; opacity: calc(1 - var(--svc-fix-p) * 2.5); transform: scale(calc(1 - var(--svc-fix-p) * 0.6)); }
.svc-fix__check { stroke-dasharray: 1; stroke-dashoffset: clamp(0, calc((1 - var(--svc-fix-p)) / 0.6), 1); }
.svc-fix__status-text {
  display: grid; justify-items: start; overflow: hidden;
  width: calc(var(--svc-fix-w0) + (var(--svc-fix-w1) - var(--svc-fix-w0)) * var(--svc-fix-p));
}
.svc-fix__status-label { grid-area: 1 / 1; white-space: nowrap; opacity: calc(1 - var(--svc-fix-p) * 1.8); transform: translateY(calc(var(--svc-fix-p) * -130%)); }
.svc-fix__status-label--fixed { opacity: calc(var(--svc-fix-p) * 1.8 - 0.8); transform: translateY(calc((1 - var(--svc-fix-p)) * 130%)); }

/* "See the fix" toggle: small, static glass panel on the photo */
.svc-fix__toggle {
  position: absolute; z-index: 3; right: 1.25rem; bottom: 1.25rem;
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1rem 0 0.875rem;
  border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: color-mix(in srgb, var(--surface-light) 92%, transparent); color: var(--text-main); font: 600 0.875rem/1 var(--font-sans);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-main) 8%, transparent), var(--shadow-lg);
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2) var(--ease-out), color var(--dur-2) var(--ease-out);
}
@supports (backdrop-filter: blur(1px)) {
  .svc-fix__toggle { background: color-mix(in srgb, var(--surface-light) 80%, transparent); backdrop-filter: blur(8px) saturate(1.3); }
}
.svc-fix__toggle[hidden] { display: none; }
.svc-fix__toggle svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-4) var(--ease-spring); }
.svc-fix__toggle[aria-pressed="true"] { background: var(--text-main); color: var(--surface-light); }
.svc-fix__toggle[aria-pressed="true"] svg { transform: rotate(90deg); }
.svc-fix__toggle:active { transform: scale(0.96); }

/* Body */
.svc-fix__body { display: flex; flex: 1; flex-direction: column; gap: 0.75rem; padding: 0.75rem 1.25rem 1.25rem; }
@media (min-width: 1024px) { .svc-fix__body { padding: var(--space-md) 1.75rem 1.75rem; } }
.svc-fix__name-row { display: flex; align-items: center; gap: 0.75rem; }
.svc-fix__icon {
  flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: var(--radius-lg);
  background: color-mix(in srgb, var(--success) 10%, var(--surface-light)); color: var(--success);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--success) 18%, transparent);
}
.svc-fix__icon svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.svc-fix__name { margin: 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.svc-fix__benefit { margin: 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.55; }
.svc-fix__did { margin: 0.375rem 0 0; color: var(--text-muted); font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }

/* "What we did": static ticks without JS; with JS they tick off one by one as the fix is revealed */
.svc-fix__steps { display: grid; gap: var(--space-sm); margin: 0; padding: 0; list-style: none; }
.svc-fix__steps li { --svc-fix-k: 1; position: relative; padding-left: 1.75rem; font-size: 0.9375rem; line-height: 1.4; }
.svc-fix--js .svc-fix__steps li { --svc-fix-k: clamp(0, calc((var(--svc-fix-p) - 0.35 - var(--svc-fix-i) * 0.18) * 5), 1); }
.svc-fix__steps li::before {
  content: ""; position: absolute; left: 0; top: 0.0625rem; width: 1.125rem; height: 1.125rem; border-radius: 50%;
  background: color-mix(in srgb, var(--success) calc(var(--svc-fix-k) * 14%), var(--surface-muted));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--success) calc(var(--svc-fix-k) * 30%), var(--border-subtle));
}
.svc-fix__steps li::after {
  content: ""; position: absolute; left: 0.4375rem; top: 0.25rem; width: 0.25rem; height: 0.5rem;
  border: solid var(--success); border-width: 0 2px 2px 0;
  opacity: calc(0.3 + var(--svc-fix-k) * 0.7); transform: rotate(45deg) scale(calc(0.7 + var(--svc-fix-k) * 0.3));
}

/* Price and booking link */
.svc-fix__foot { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--space-md); margin-top: auto; padding-top: var(--space-md); border-top: 1px dashed var(--border-subtle); }
.svc-fix__price { margin: 0; font: 600 1.5rem/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }
.svc-fix__price small { margin-right: 0.1875rem; color: var(--text-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0; }
.svc-fix__link, .svc-fix__cta-btn {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.125rem; border-radius: var(--radius-full);
  background: var(--text-main); color: var(--surface-light); font-size: 0.875rem; font-weight: 600; text-decoration: none; white-space: nowrap;
  box-shadow: var(--highlight-inverse), 0 10px 22px -12px color-mix(in srgb, var(--text-main) 70%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2) var(--ease-out);
}
.svc-fix__link svg, .svc-fix__cta-btn svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.svc-fix__link:hover { background: color-mix(in srgb, var(--text-main) 85%, var(--primary)); }
.svc-fix__link:hover svg, .svc-fix__cta-btn:hover svg { transform: translateX(3px); }
.svc-fix__link:active, .svc-fix__cta-btn:active { transform: scale(0.97); }
.svc-fix :is(.svc-fix__link, .svc-fix__toggle, .svc-fix__cta-btn):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Footer CTA */
.svc-fix__cta {
  display: flex; flex-direction: column; align-items: flex-start; gap: var(--space-md); margin-top: clamp(2rem, 4vw, 3rem);
  padding: 1.25rem var(--space-lg); border-radius: var(--radius-2xl); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-md);
}
.svc-fix__cta p { margin: 0; color: var(--text-muted); line-height: 1.5; }
.svc-fix__cta strong { color: var(--text-main); }
.svc-fix__cta-btn { background: var(--primary); color: var(--text-inverse); }
.svc-fix__cta-btn:hover { background: var(--primary-hover); }
@media (min-width: 768px) { .svc-fix__cta { flex-direction: row; align-items: center; justify-content: space-between; } }

.svc-fix__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

@media (prefers-reduced-motion: reduce) {
  .svc-fix *, .svc-fix *::before, .svc-fix *::after { animation: none !important; }
}
@keyframes svc-fix-tease {
  0%, 100% { --svc-fix-p: 0; }
  42%, 58% { --svc-fix-p: 1; }
}
```

## JS

```js
// Problem → Fixed cards: the pinned toggle, chip width measuring and a one-off teaser.
// Hover and focus peeks are CSS; everything animates from one registered property, --svc-fix-p.
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('[data-svc-fix]').forEach((root) => {
  const cards = [...root.querySelectorAll('.svc-fix__card')];
  root.classList.add('svc-fix--js');

  cards.forEach((card) => {
    const toggle = card.querySelector('.svc-fix__toggle');
    const before = card.querySelector('.svc-fix__shot--before');
    const after = card.querySelector('.svc-fix__shot--after');
    const slot = card.querySelector('.svc-fix__status-text');
    const [problem, fixed] = slot.children;

    // The toggle pins the fix; assistive tech only gets the photo that is pinned on screen
    const hide = (el, on) => (on ? el.setAttribute('aria-hidden', 'true') : el.removeAttribute('aria-hidden'));
    const pin = (on) => {
      card.classList.toggle('is-fixed', on);
      toggle.setAttribute('aria-pressed', String(on));
      hide(before, on);
      hide(after, !on);
    };
    toggle.hidden = false;
    toggle.addEventListener('click', () => pin(!card.classList.contains('is-fixed')));
    pin(false);

    // The chip's label slot morphs between both label widths; re-measured when fonts load or text zooms
    const ro = new ResizeObserver(() => {
      slot.style.setProperty('--svc-fix-w0', `${problem.offsetWidth}px`);
      slot.style.setProperty('--svc-fix-w1', `${fixed.offsetWidth}px`);
    });
    ro.observe(problem);
    ro.observe(fixed);
  });

  // Teaser: the first card wipes to the fix and back once, the first time it is mostly in view
  const first = cards[0];
  if (!first || reduce.matches || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver(([entry]) => {
    if (!entry.isIntersecting) return;
    io.disconnect();
    if (!first.matches(':hover') && !first.classList.contains('is-fixed')) first.classList.add('is-teasing');
  }, { threshold: 0.6 });
  io.observe(first);
  first.addEventListener('animationend', (e) => {
    if (e.animationName === 'svc-fix-tease') first.classList.remove('is-teasing');
  });
});
```

## Notes

- "See the fix" is a real button with `aria-pressed` and a constant name ("See the fix: water heater"). Pinning decides what assistive tech gets: the hidden photo's `<figure>`, caption included, is `aria-hidden`, so screen-reader users hear the state that's pinned on screen. Hover and focus peeks are visual only, and the morphing chip is `aria-hidden` because the captions carry the same words.
- Peeks: hovering a card (on `(hover: hover)` devices) or focusing its booking link reveals the fix. Hovering the toggle itself shows the pinned state, so a click always visibly changes something.
- Without JS, both photos stack with "Before: …" and "After: …" captions and the lists show static ticks; the chip and toggle stay hidden. Under reduced motion `--dur-5` collapses, so the swap is instant and the teaser never runs.
- One registered number, `--svc-fix-p`, drives the clip-path wipe, edge glint, chip sweep, label roll, check draw and list ticks, so they can never drift apart. Browsers without `@property` get an instant swap. The focus peek and toggle-hover rules use `:has()`. The chip's width morph is a layout animation on one small, absolutely positioned element.
- Contrast: chip text (`--text-inverse`) is about 4.8:1 on both `--warning` and `--success`. Photo captions sit on a 72% `--surface-deep` pill (at least 7.8:1 over the brightest photo), and toggle text on its 80% white glass is at least 8:1 over the darkest photo.
- Use real 4:3 job photos named `<thing>-before.jpg` and `<thing>-after.jpg`. The slant is the `130%` / `30%` pair in the clip-path and edge polygons; change both together.
