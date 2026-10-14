# Blend-Mode Sticky Type

A giant "BRAND" wordmark rides along the left edge while light, deep, photo and brand-gradient sections scroll beneath it, with the real content sitting beside it. `mix-blend-mode: difference` inverts the letters against whatever passes underneath: near-black over paper, warm white over the deep band, cream and peach over the brand gradient. As each seam slides through, it splits single letters into two colours. On phones the wordmark becomes a full-width band pinned to the top. Depends on `tokens/variables.css`.

**Motion:** scroll only: the wordmark pins with `position: sticky` and inverts live as sections pass · section content rises in on a `view()` timeline where supported (scroll scrub, motion allowed only) · button lift and press (`--dur-2`, `--ease-spring`) and arrow nudge (`--dur-3`).

## HTML

```html
<div class="blend-text-demo">
  <div class="blend-text-demo__block">
    <p class="blend-text-demo__note">A giant wordmark rides the left edge and inverts over every section it crosses.</p>
    <p class="blend-text-demo__hint">
      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
      Scroll
    </p>
  </div>

  <div class="blend-text">
    <div class="blend-text__stage" aria-hidden="true">
      <div class="blend-text__rail"><span class="blend-text__mark">BRAND</span></div>
    </div>

    <section class="blend-text__section" aria-labelledby="blend-text-about">
      <div class="blend-text__inner">
        <p class="blend-text__eyebrow"><span class="blend-text__index">01</span> Who we are</p>
        <h2 id="blend-text-about" class="blend-text__title">Springfield's crew since 2009.</h2>
        <p class="blend-text__lead">Plumbers, electricians and heating engineers who work as one crew, so a single visit fixes the whole problem rather than just your part of it.</p>
        <dl class="blend-text__facts">
          <div class="blend-text__fact"><dt>Technicians</dt><dd>38</dd></div>
          <div class="blend-text__fact"><dt>Depots</dt><dd>3</dd></div>
          <div class="blend-text__fact"><dt>Average rating</dt><dd>4.9/5</dd></div>
        </dl>
        <a class="blend-text__link" href="#crew">
          Meet the crew
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
      </div>
    </section>

    <section class="blend-text__section blend-text__section--deep" aria-labelledby="blend-text-services">
      <div class="blend-text__inner">
        <p class="blend-text__eyebrow"><span class="blend-text__index">02</span> What we fix</p>
        <h2 id="blend-text-services" class="blend-text__title">One call covers the whole house.</h2>
        <ol class="blend-text__services" role="list">
          <li class="blend-text__service"><span class="blend-text__num" aria-hidden="true">01</span><strong>Leaks &amp; burst pipes</strong><span class="blend-text__service-copy">Traced with thermal cameras and fixed without tearing up floors.</span></li>
          <li class="blend-text__service"><span class="blend-text__num" aria-hidden="true">02</span><strong>Boilers &amp; water heaters</strong><span class="blend-text__service-copy">Serviced, repaired or replaced, usually the same day.</span></li>
          <li class="blend-text__service"><span class="blend-text__num" aria-hidden="true">03</span><strong>Wiring &amp; panels</strong><span class="blend-text__service-copy">Panel upgrades, EV chargers and fault-finding by licensed electricians.</span></li>
          <li class="blend-text__service"><span class="blend-text__num" aria-hidden="true">04</span><strong>Drains &amp; sewer lines</strong><span class="blend-text__service-copy">Camera surveys, jetting and trenchless repairs.</span></li>
        </ol>
      </div>
    </section>

    <section class="blend-text__section blend-text__section--photo" aria-labelledby="blend-text-job">
      <img class="blend-text__photo" src="riverside-repipe.jpg" alt="" width="1600" height="1067" loading="lazy" decoding="async">
      <div class="blend-text__inner">
        <p class="blend-text__eyebrow"><span class="blend-text__index">03</span> From the job sheet</p>
        <h2 id="blend-text-job" class="blend-text__title">A Riverside re-pipe, done in a day.</h2>
        <figure class="blend-text__quote">
          <blockquote><p>"They re-routed the whole kitchen's pipework without lifting a single board of the floor we'd just laid."</p></blockquote>
          <figcaption>Dana K. · Riverside</figcaption>
        </figure>
        <ul class="blend-text__tags" role="list">
          <li class="blend-text__tag">Copper to PEX</li>
          <li class="blend-text__tag">9 hours</li>
          <li class="blend-text__tag">2 technicians</li>
        </ul>
      </div>
    </section>

    <section class="blend-text__section blend-text__section--brand" aria-labelledby="blend-text-book">
      <div class="blend-text__inner">
        <p class="blend-text__eyebrow"><span class="blend-text__index">04</span> Book the crew</p>
        <h2 id="blend-text-book" class="blend-text__title">Booked by noon, fixed by dinner.</h2>
        <p class="blend-text__lead">Same-day slots across Westlake, Northside and Riverside. Upfront prices, written quotes and no call-out fee.</p>
        <div class="blend-text__actions">
          <a class="blend-text__btn" href="#book">
            Book a visit
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </a>
          <a class="blend-text__btn blend-text__btn--ghost" href="tel:+15555550123">
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
            (555) 555-0123
          </a>
        </div>
      </div>
    </section>
  </div>

  <div class="blend-text-demo__block">
    <p class="blend-text-demo__note">The wordmark lets go with the last section, and the page carries on.</p>
  </div>
</div>
```

## CSS

```css
/* Demo scroll room (demo only) */
.blend-text-demo__block {
  display: grid; place-content: center; justify-items: center; gap: 1rem; min-height: 65vh; padding: 3rem var(--gutter);
  background: var(--surface-muted); color: var(--text-muted); font-family: var(--font-sans); text-align: center;
}
.blend-text-demo__note { max-width: 26rem; margin: 0; color: var(--text-main); font: 500 1.125rem/1.5 var(--font-display); letter-spacing: -0.01em; }
.blend-text-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.blend-text-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* Root: the isolated group the wordmark blends into (the sections, never the page behind) */
.blend-text {
  --blend-text-size: min(25vw, 24vh);
  --blend-text-band: calc(var(--blend-text-size) * 0.8 + 1.5rem);
  position: relative; isolation: isolate; overflow-x: clip;
  background: var(--surface-light); font-family: var(--font-sans);
}

/* Stage: the sticky element itself carries the blend. Sticky creates a stacking context, so a blend on a child would only mix with the stage's empty pixels */
.blend-text__stage {
  position: sticky; top: 0; z-index: 1;
  height: var(--blend-text-band); margin-bottom: calc(var(--blend-text-band) * -1);
  color: var(--surface-light); pointer-events: none; mix-blend-mode: difference;
}
.blend-text__rail {
  position: relative; display: flex; align-items: center; height: 100%;
  max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter);
}
.blend-text__rail::after { content: ""; position: absolute; left: var(--gutter); right: var(--gutter); bottom: 0; height: 1px; background: currentColor; opacity: 0.6; }
.blend-text__mark { font: 700 var(--blend-text-size)/0.8 var(--font-display); letter-spacing: var(--tracking-tight); white-space: nowrap; }

/* Sections: backgrounds sit near black or near white so the inverted letters always read */
.blend-text__section {
  --blend-text-fg: var(--text-main);
  --blend-text-muted: var(--text-muted);
  --blend-text-line: var(--border-subtle);
  --blend-text-focus: var(--primary);
  position: relative; isolation: isolate; display: grid; align-items: center;
  min-height: 85vh; min-height: 85svh; padding-block: calc(var(--blend-text-band) + 2.5rem) 4rem;
  background: var(--surface-light); color: var(--blend-text-fg);
}
.blend-text__section--deep {
  --blend-text-fg: var(--text-inverse);
  --blend-text-muted: var(--text-inverse-muted);
  --blend-text-line: var(--border-inverse);
  --blend-text-focus: var(--text-inverse);
  background: radial-gradient(60% 55% at 85% 0%, color-mix(in srgb, var(--primary) 22%, transparent), transparent 70%), var(--surface-deep);
}
.blend-text__section--photo {
  --blend-text-muted: color-mix(in srgb, var(--text-main) 85%, var(--surface-light));
  --blend-text-line: color-mix(in srgb, var(--text-main) 18%, transparent);
  background: var(--surface-muted);
}
.blend-text__photo { position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%; object-fit: cover; filter: grayscale(1) contrast(1.1); }
.blend-text__section--photo::before {
  content: ""; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(100deg, color-mix(in srgb, var(--surface-light) 92%, transparent) 15%, color-mix(in srgb, var(--surface-light) 84%, transparent));
}
.blend-text__section--brand {
  --blend-text-fg: var(--text-inverse);
  --blend-text-muted: color-mix(in srgb, var(--text-inverse) 80%, var(--text-inverse-muted));
  --blend-text-line: var(--border-inverse);
  --blend-text-focus: var(--text-inverse);
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 45%, var(--surface-deep)), color-mix(in srgb, var(--primary-2) 40%, var(--surface-deep)));
}
.blend-text__section--brand::before {
  content: ""; position: absolute; inset: 0; z-index: -1;
  background-image: linear-gradient(var(--border-inverse) 1px, transparent 1px), linear-gradient(90deg, var(--border-inverse) 1px, transparent 1px);
  background-size: 3.5rem 3.5rem;
  -webkit-mask-image: radial-gradient(ellipse 70% 80% at 80% 50%, black, transparent 75%);
  mask-image: radial-gradient(ellipse 70% 80% at 80% 50%, black, transparent 75%);
}
.blend-text__inner { width: 100%; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }

/* Type */
.blend-text__eyebrow {
  display: flex; align-items: center; gap: 0.75rem; margin: 0;
  color: var(--blend-text-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.blend-text__index { padding: 0.3125rem 0.5rem; border-radius: var(--radius-full); box-shadow: inset 0 0 0 1px var(--blend-text-line); color: var(--blend-text-fg); }
.blend-text__title {
  max-width: 16ch; margin: 1.25rem 0 0; font: 600 clamp(2.25rem, 1.2rem + 3.6vw, 4.25rem)/1.02 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.blend-text__lead { max-width: 36rem; margin: 1.25rem 0 0; color: var(--blend-text-muted); font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem); line-height: 1.6; }

/* Section 1: facts (number above label, dt/dd order kept) and a text link */
.blend-text__facts {
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; max-width: 34rem;
  margin: 2.5rem 0 0; padding-top: 1.5rem; border-top: 1px solid var(--blend-text-line);
}
.blend-text__fact { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.5rem; }
.blend-text__fact dt { color: var(--blend-text-muted); font: 500 0.75rem/1.3 var(--font-mono); letter-spacing: 0.04em; text-transform: uppercase; }
.blend-text__fact dd { margin: 0; font: 600 clamp(1.75rem, 1.2rem + 2vw, 2.5rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.blend-text__link {
  display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.75rem; margin-top: 1.5rem; color: var(--primary); font-weight: 600;
  text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 0.3em;
}

/* Section 2: service index */
.blend-text__services { display: grid; max-width: 46rem; margin: 2.5rem 0 0; padding: 0; list-style: none; border-bottom: 1px solid var(--blend-text-line); }
.blend-text__service { display: grid; grid-template-columns: 2.5rem minmax(0, 1fr); gap: 0.25rem 0.75rem; padding: 1.125rem 0; border-top: 1px solid var(--blend-text-line); }
.blend-text__service strong { font: 600 1.125rem/1.3 var(--font-display); letter-spacing: -0.01em; }
.blend-text__num { grid-row: span 2; color: var(--blend-text-muted); font: 500 0.8125rem/1.7 var(--font-mono); }
.blend-text__service-copy { color: var(--blend-text-muted); font-size: 0.9375rem; line-height: 1.55; }

/* Section 3: quote and tags over the photo */
.blend-text__quote { max-width: 38rem; margin: 2rem 0 0; padding-left: 1.5rem; border-left: 2px solid var(--blend-text-fg); }
.blend-text__quote blockquote { margin: 0; font: 500 clamp(1.25rem, 1rem + 1vw, 1.625rem)/1.4 var(--font-display); letter-spacing: -0.01em; }
.blend-text__quote p { margin: 0; }
.blend-text__quote figcaption { margin-top: 1rem; color: var(--blend-text-muted); font: 500 0.8125rem/1.4 var(--font-mono); }
.blend-text__tags { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 2rem 0 0; padding: 0; list-style: none; }
.blend-text__tag {
  padding: 0.375rem 0.75rem; border-radius: var(--radius-full); font: 500 0.8125rem/1.3 var(--font-mono);
  background: color-mix(in srgb, var(--surface-light) 60%, transparent); box-shadow: inset 0 0 0 1px var(--blend-text-line);
}

/* Section 4: actions */
.blend-text__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2.25rem; }
.blend-text__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font: 600 0.9375rem/1.2 var(--font-sans); text-decoration: none;
  box-shadow: var(--highlight), 0 14px 36px -14px color-mix(in srgb, var(--primary-2) 70%, transparent);
  transition: transform var(--dur-2) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.blend-text__btn:hover { transform: translateY(-2px); }
.blend-text__btn:active { transform: scale(0.97); }
.blend-text__btn--ghost { background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.blend-text :is(.blend-text__btn, .blend-text__link) svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.blend-text :is(.blend-text__btn:not(.blend-text__btn--ghost), .blend-text__link):hover svg { transform: translateX(3px); }
.blend-text :is(.blend-text__btn, .blend-text__link) { scroll-margin-top: calc(var(--blend-text-band) + 1rem); }
.blend-text :is(.blend-text__btn, .blend-text__link):focus-visible { outline: 2px solid var(--blend-text-focus); outline-offset: 3px; }

/* Desktop: the wordmark turns into a full-height spine on the left; content moves beside it */
@media (min-width: 768px) {
  .blend-text {
    --blend-text-size: clamp(6rem, 26vh, 15rem);
    --blend-text-band: 0px;
    --blend-text-rail: calc(var(--blend-text-size) * 0.8);
  }
  .blend-text__stage { height: 100vh; height: 100svh; margin-bottom: -100vh; margin-bottom: -100svh; }
  .blend-text__mark { writing-mode: vertical-rl; transform: rotate(180deg); }
  .blend-text__rail::after { top: 14%; bottom: 14%; left: calc(var(--gutter) + var(--blend-text-rail) + 1.5rem); right: auto; width: 1px; height: auto; }
  .blend-text__section { padding-block: clamp(4.5rem, 12vh, 7rem); }
  .blend-text__inner { padding-left: calc(var(--gutter) + var(--blend-text-rail) + 3.5rem); }
}
@media (min-width: 1024px) {
  .blend-text__services { grid-template-columns: 1fr 1fr; column-gap: 2.5rem; }
}

/* Content rises in as it scrolls past the wordmark (scroll scrub; static where unsupported or motion is reduced) */
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .blend-text__inner > * { animation: blend-text-rise linear both; animation-timeline: view(); animation-range: entry 5% entry 60%; }
  }
}
@keyframes blend-text-rise { from { opacity: 0; translate: 0 2.5rem; } }
```

## Notes

- **Stacking:** the blend sits on `.blend-text__stage`, the sticky element itself, and the root carries `isolation: isolate`. Sticky positioning always creates a stacking context, so a blend on a child of the stage would only mix with the stage's own transparent pixels and render plain white. The isolated root is the group the stage blends into: every section inside it, and nothing on the page behind. Keep the stage a direct child of the root, and never add `isolation`, `transform`, `opacity`, `filter` or `will-change` to a wrapper between them, or the blend loses its backdrop. Sections may isolate themselves; the photo section does, to layer its image and scrim.
- **Backgrounds near the extremes:** difference against white returns the inverse of what's underneath, so mid-tones invert to mid-tones. The raw brand gradient would leave the letters at about 2:1. The brand band is therefore mixed 55–60% toward `--surface-deep`, and the photo sits greyscale under a white scrim of at least 84%. Inverted letters measure 21:1 on the light section, 17.9:1 on deep (12.6:1 at its glow), 6.9–7.7:1 on brand, and at least 10:1 on the photo.
- **Text contrast:** light 14.6 (main), 4.8 (muted) and 5.2 (link) · deep 18.8 / 7.7 (6.3 under the glow) · photo at least 10.1 / 6.3 at the scrim's darkest · brand at least 10.7 / 9.2.
- **Accessibility:** the wordmark is `aria-hidden` and `pointer-events: none`, so it never blocks clicks or selection, and every section has its own `<h2>`. On phones the band overlaps text as it scrolls under, like any sticky header. Sections pad their tops to start below it, and links get a `scroll-margin-top` equal to the band so keyboard focus is never scrolled beneath it.
- **No JS.** Section content rises in on a `view()` timeline only where supported and motion is allowed; elsewhere it's static. Elements already in view at load are past their range, so nothing flashes. Swap the word freely, but keep it to about six capitals, or lower `--blend-text-size` for longer words.
