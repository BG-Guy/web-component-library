# Cinematic Reel Hero

A full-bleed photo reel behind a deep scrim: four slides drift in a slow Ken Burns zoom and hand over with a crossfade that blurs out the old frame. Each slide's big headline swaps line by line, rising out of a mask, while story-style segmented bars along the bottom fill per slide (click one to jump) and a floating glass "Book now" card with a rating sits bottom-right. It follows the APG auto-rotating carousel (pause button first in the tab order, hover pauses, focus stops, slides labelled "1 of 4", live region off while rotating). On phones the copy and card stack above the bars, the segment labels collapse to bars, and a swipe changes slide. Depends on `tokens/variables.css`.

**Motion:** Ken Burns zoom and pan on the active frame (linear, interval + 2.5s) · frame crossfade with blur (`--dur-5` × 1.3, `--ease-in-out`) · headline lines rise from masks and leave upwards (`--dur-5` `--ease-out` in, `--dur-3` out, `--stagger`) · copy, card and bars rise in on load · segment fill (linear, `--reel-hero-interval`). Pause/play, hover, focus and off-screen all freeze the reel.

## HTML

```html
<section class="reel-hero" aria-roledescription="carousel" aria-labelledby="reel-hero-title" data-reel-hero style="--reel-hero-interval: 7s">
  <div class="reel-hero__frames" aria-hidden="true">
    <div class="reel-hero__frame is-active" style="--reel-hero-origin: 35% 55%; --reel-hero-pan: -1.5%">
      <img src="reel-kitchen.jpg" alt="" width="1920" height="1080" fetchpriority="high">
    </div>
    <div class="reel-hero__frame" style="--reel-hero-origin: 65% 40%; --reel-hero-pan: 1.5%">
      <img src="reel-plumbing.jpg" alt="" width="1920" height="1080" loading="lazy" decoding="async">
    </div>
    <div class="reel-hero__frame" style="--reel-hero-origin: 50% 30%; --reel-hero-pan: -1%">
      <img src="reel-roof.jpg" alt="" width="1920" height="1080" loading="lazy" decoding="async">
    </div>
    <div class="reel-hero__frame" style="--reel-hero-origin: 40% 60%; --reel-hero-pan: 1%">
      <img src="reel-heat-pump.jpg" alt="" width="1920" height="1080" loading="lazy" decoding="async">
    </div>
  </div>

  <div class="reel-hero__inner">
    <button class="reel-hero__pause" type="button" aria-pressed="false" aria-label="Pause slideshow" hidden>
      <svg class="reel-hero__icon-pause" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
      <svg class="reel-hero__icon-play" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
    </button>

    <div class="reel-hero__copy">
      <h1 id="reel-hero-title" class="reel-hero__kicker"><span class="reel-hero__kicker-dot" aria-hidden="true"></span>Brand · Home repair &amp; renovation in Springfield</h1>

      <div class="reel-hero__slides" aria-live="off">
        <div class="reel-hero__slide is-active" role="group" aria-roledescription="slide" aria-label="1 of 4">
          <h2 class="reel-hero__headline"><span class="reel-hero__mask"><span class="reel-hero__rise" style="--reel-hero-l: 0">Kitchens built</span></span> <span class="reel-hero__mask"><span class="reel-hero__rise" style="--reel-hero-l: 1">around you.</span></span></h2>
          <p class="reel-hero__line">Design, permits and build by one licensed crew, at a fixed price on fixed dates.</p>
          <p class="reel-hero__credit"><svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12zM12 11.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z" /></svg>Kitchen remodel · Westlake</p>
        </div>
        <div class="reel-hero__slide" role="group" aria-roledescription="slide" aria-label="2 of 4">
          <h2 class="reel-hero__headline"><span class="reel-hero__mask"><span class="reel-hero__rise" style="--reel-hero-l: 0">Leaks fixed</span></span> <span class="reel-hero__mask"><span class="reel-hero__rise" style="--reel-hero-l: 1">before dinner.</span></span></h2>
          <p class="reel-hero__line">Same-day plumbers across Springfield, with flat-rate pricing agreed before we start.</p>
          <p class="reel-hero__credit"><svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12zM12 11.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z" /></svg>Leak repair · Northside</p>
        </div>
        <div class="reel-hero__slide" role="group" aria-roledescription="slide" aria-label="3 of 4">
          <h2 class="reel-hero__headline"><span class="reel-hero__mask"><span class="reel-hero__rise" style="--reel-hero-l: 0">Roofs ready</span></span> <span class="reel-hero__mask"><span class="reel-hero__rise" style="--reel-hero-l: 1">for any storm.</span></span></h2>
          <p class="reel-hero__line">Inspections, repairs and full replacements, backed by a 25-year workmanship warranty.</p>
          <p class="reel-hero__credit"><svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12zM12 11.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z" /></svg>Roof replacement · Riverside</p>
        </div>
        <div class="reel-hero__slide" role="group" aria-roledescription="slide" aria-label="4 of 4">
          <h2 class="reel-hero__headline"><span class="reel-hero__mask"><span class="reel-hero__rise" style="--reel-hero-l: 0">Comfort in</span></span> <span class="reel-hero__mask"><span class="reel-hero__rise" style="--reel-hero-l: 1">every season.</span></span></h2>
          <p class="reel-hero__line">Heat pump and AC installs sized to your home, with the rebate paperwork done for you.</p>
          <p class="reel-hero__credit"><svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12zM12 11.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z" /></svg>Heat pump install · Springfield</p>
        </div>
      </div>

      <div class="reel-hero__actions">
        <a class="reel-hero__btn reel-hero__btn--primary" href="#quote">
          Get a free quote
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="reel-hero__btn reel-hero__btn--glass" href="#projects">See our projects</a>
      </div>
    </div>

    <div class="reel-hero__card">
      <div class="reel-hero__card-top">
        <span class="reel-hero__faces" aria-hidden="true"><span>JM</span><span>AK</span><span>RS</span></span>
        <p class="reel-hero__rating">
          <span class="reel-hero__stars" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="13" height="13" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
            <svg viewBox="0 0 24 24" width="13" height="13" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
            <svg viewBox="0 0 24 24" width="13" height="13" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
            <svg viewBox="0 0 24 24" width="13" height="13" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
            <svg viewBox="0 0 24 24" width="13" height="13" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          </span>
          <span><strong>4.9/5</strong> · 2,300 reviews</span>
        </p>
      </div>
      <p class="reel-hero__slot"><span class="reel-hero__slot-dot" aria-hidden="true"></span>Next opening: <strong>Today 2–4pm</strong></p>
      <a class="reel-hero__book" href="#book">
        Book now
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </a>
    </div>

    <div class="reel-hero__segs">
      <button class="reel-hero__seg" type="button" aria-current="true"><span class="reel-hero__sr">Show slide 1 of 4: </span><span class="reel-hero__seg-label"><span aria-hidden="true">01</span> Kitchens</span><span class="reel-hero__seg-bar"><span class="reel-hero__seg-fill"></span></span></button>
      <button class="reel-hero__seg" type="button"><span class="reel-hero__sr">Show slide 2 of 4: </span><span class="reel-hero__seg-label"><span aria-hidden="true">02</span> Plumbing</span><span class="reel-hero__seg-bar"><span class="reel-hero__seg-fill"></span></span></button>
      <button class="reel-hero__seg" type="button"><span class="reel-hero__sr">Show slide 3 of 4: </span><span class="reel-hero__seg-label"><span aria-hidden="true">03</span> Roofing</span><span class="reel-hero__seg-bar"><span class="reel-hero__seg-fill"></span></span></button>
      <button class="reel-hero__seg" type="button"><span class="reel-hero__sr">Show slide 4 of 4: </span><span class="reel-hero__seg-label"><span aria-hidden="true">04</span> Comfort</span><span class="reel-hero__seg-bar"><span class="reel-hero__seg-fill"></span></span></button>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section: the reel sits behind a deep scrim; the inner grid pins the copy and controls to the bottom */
.reel-hero {
  --reel-hero-soft: color-mix(in srgb, var(--text-inverse) 85%, var(--text-inverse-muted));
  --reel-hero-state: running; /* every reel loop reads this, so one attribute pauses them all */
  position: relative; isolation: isolate; overflow: clip; touch-action: pan-y;
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}
.reel-hero:is([data-paused], [data-hover], [data-offscreen]) { --reel-hero-state: paused; }

/* Frames: the incoming photo fades in sharp over the outgoing one, which blurs as it goes */
.reel-hero__frames { position: absolute; inset: 0; z-index: -1; }
.reel-hero__frame {
  position: absolute; inset: 0; overflow: hidden; opacity: 0; filter: blur(16px);
  transition: opacity calc(var(--dur-5) * 1.3) var(--ease-in-out), filter calc(var(--dur-5) * 1.3) var(--ease-in-out);
}
.reel-hero__frame.is-leaving { opacity: 1; filter: blur(10px); }
.reel-hero__frame.is-active { z-index: 1; opacity: 1; filter: none; }
.reel-hero__frame img { display: block; width: 100%; height: 100%; object-fit: cover; transform-origin: var(--reel-hero-origin, 50% 50%); }
.reel-hero.is-playing .reel-hero__frame:is(.is-active, .is-leaving) img {
  animation: reel-hero-kb calc(var(--reel-hero-interval) + 2.5s) linear forwards var(--reel-hero-state);
}
.reel-hero__frames::after { /* deep scrim: heavy at the bottom and left where the copy sits */
  content: ""; position: absolute; inset: 0; z-index: 2;
  background:
    linear-gradient(to top, color-mix(in srgb, var(--surface-deep) 94%, transparent), color-mix(in srgb, var(--surface-deep) 72%, transparent) 45%, color-mix(in srgb, var(--surface-deep) 25%, transparent) 75%, color-mix(in srgb, var(--surface-deep) 55%, transparent)),
    linear-gradient(to right, color-mix(in srgb, var(--surface-deep) 55%, transparent), transparent 70%);
}

/* Layout: copy, then card, then pause + segments (the pause button is first in the DOM and tab order) */
.reel-hero__inner {
  display: grid; grid-template-columns: auto minmax(0, 1fr); grid-template-areas: "copy copy" "card card" "pause segs";
  align-content: end; gap: 1.75rem 0.875rem;
  min-height: 100vh; min-height: 100svh; max-width: var(--container-max); margin-inline: auto;
  padding: 6rem var(--gutter) 1rem;
}
.reel-hero__copy { grid-area: copy; max-width: 46rem; }
.reel-hero__card { grid-area: card; }
.reel-hero__pause { grid-area: pause; align-self: end; margin-bottom: 0.25rem; }
.reel-hero__segs { grid-area: segs; }
.reel-hero:not(.reel-hero--js) .reel-hero__segs { display: none; } /* no dead controls without JS */

/* Static parts rise in once; the slide lines have their own choreography */
.reel-hero__kicker { animation: reel-hero-fade var(--dur-5) var(--ease-out) 80ms backwards; }
.reel-hero__actions { animation: reel-hero-fade var(--dur-5) var(--ease-out) calc(160ms + 8 * var(--stagger)) backwards; }
.reel-hero__card { animation: reel-hero-card var(--dur-5) var(--ease-out) calc(160ms + 10 * var(--stagger)) backwards; }
.reel-hero__segs, .reel-hero__pause { animation: reel-hero-fade var(--dur-5) var(--ease-out) calc(160ms + 12 * var(--stagger)) backwards; }

/* Kicker: the page's <h1>, on its own glass so it reads over any photo */
.reel-hero__kicker {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.4375rem 0.875rem 0.4375rem 0.75rem; border-radius: var(--radius-lg);
  background: color-mix(in srgb, var(--surface-deep) 55%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
  font: 500 0.75rem/1.35 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
}
.reel-hero__kicker-dot { flex: none; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--gradient-brand); box-shadow: 0 0 10px var(--primary-2); }

/* Slides: stacked in one grid cell (the tallest sets the height); only the current one is visible */
.reel-hero__slides { display: grid; margin-top: 1.25rem; }
.reel-hero__slide { grid-area: 1 / 1; visibility: hidden; transition: visibility 0s linear var(--dur-4); }
.reel-hero__slide:is(.is-active, .is-leaving) { visibility: visible; transition-delay: 0s; }
.reel-hero__headline {
  margin: 0; font: 600 clamp(2.5rem, 1.1rem + 6.4vw, 6.25rem)/0.98 var(--font-display); letter-spacing: var(--tracking-display);
  text-shadow: 0 2px 24px color-mix(in srgb, var(--surface-deep) 50%, transparent);
}
/* Per-line mask: each line rises out of its own clip, and leaves upwards when the slide changes */
.reel-hero__mask { display: block; overflow: clip; padding-bottom: 0.08em; margin-bottom: -0.08em; }
.reel-hero__rise { display: block; }
.reel-hero__slide.is-active .reel-hero__rise { animation: reel-hero-rise var(--dur-5) var(--ease-out) calc(220ms + var(--reel-hero-l) * var(--stagger) * 2) backwards; }
.reel-hero__slide.is-leaving .reel-hero__rise { animation: reel-hero-out var(--dur-3) var(--ease-in-out) forwards; }
.reel-hero__line {
  max-width: 34rem; margin: 1.25rem 0 0; color: var(--reel-hero-soft);
  font-size: clamp(1rem, 0.95rem + 0.35vw, 1.1875rem); line-height: 1.6; text-wrap: pretty;
  text-shadow: 0 1px 16px color-mix(in srgb, var(--surface-deep) 60%, transparent);
}
.reel-hero__credit {
  display: inline-flex; align-items: center; gap: 0.375rem; margin: 1rem 0 0; color: var(--reel-hero-soft);
  font: 500 0.6875rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
}
.reel-hero__credit svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.reel-hero__slide.is-active :is(.reel-hero__line, .reel-hero__credit) { animation: reel-hero-fade var(--dur-5) var(--ease-out) calc(220ms + 4 * var(--stagger)) backwards; }
.reel-hero__slide.is-leaving :is(.reel-hero__line, .reel-hero__credit) { animation: reel-hero-fade-out var(--dur-3) var(--ease-in-out) forwards; }

/* CTAs */
.reel-hero__actions { display: grid; gap: 0.75rem; margin-top: 2rem; }
.reel-hero__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.5rem;
  border-radius: var(--radius-full); font: 600 0.9375rem/1 var(--font-sans); text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out), background-color var(--dur-2);
}
.reel-hero__btn svg, .reel-hero__book svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.reel-hero__btn:hover, .reel-hero__book:hover { transform: translateY(-2px); }
.reel-hero__btn:active, .reel-hero__book:active { transform: scale(0.97); }
.reel-hero__btn:hover svg, .reel-hero__book:hover svg { transform: translateX(3px); }
.reel-hero__btn--primary { background: var(--surface-light); color: var(--text-main); box-shadow: var(--highlight), 0 14px 40px -14px color-mix(in srgb, var(--surface-deep) 90%, transparent); }
.reel-hero__btn--glass {
  background: color-mix(in srgb, var(--surface-deep) 35%, transparent); color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-inverse) 24%, transparent), var(--highlight-inverse);
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
}
.reel-hero__btn--glass:hover { background: color-mix(in srgb, var(--surface-deep) 20%, transparent); }
.reel-hero :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Floating "Book now" card: one compact row on phones, a stacked glass card bottom-right on desktop */
.reel-hero__card {
  display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; gap: 0.75rem 1rem; padding: 0.875rem; border-radius: var(--radius-2xl);
  background: color-mix(in srgb, var(--surface-deep) 80%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 30px 60px -24px color-mix(in srgb, var(--surface-deep) 90%, transparent);
}
@supports (backdrop-filter: blur(1px)) {
  .reel-hero__card { background: color-mix(in srgb, var(--surface-deep) 62%, transparent); -webkit-backdrop-filter: blur(var(--blur-lg)) saturate(1.4); backdrop-filter: blur(var(--blur-lg)) saturate(1.4); }
}
.reel-hero__card-top { display: flex; align-items: center; gap: 0.75rem; min-width: 0; }
.reel-hero__rating { display: grid; gap: 0.125rem; margin: 0; color: var(--reel-hero-soft); font-size: 0.8125rem; }
.reel-hero__rating strong { color: var(--text-inverse); }
.reel-hero__stars { display: inline-flex; gap: 0.125rem; color: var(--accent); }
.reel-hero__stars svg { fill: currentColor; stroke: currentColor; stroke-width: 1.5; stroke-linejoin: round; }
.reel-hero__faces { display: none; }
.reel-hero__faces span {
  display: grid; place-items: center; width: 2rem; height: 2rem; margin-left: -0.5rem; border: 2px solid color-mix(in srgb, var(--surface-deep) 80%, var(--text-inverse)); border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font-size: 0.6875rem; font-weight: 700;
}
.reel-hero__faces span:first-child { margin-left: 0; }
.reel-hero__faces span:nth-child(2) { background: linear-gradient(135deg, var(--primary-2), color-mix(in srgb, var(--primary-2) 50%, var(--surface-deep))); }
.reel-hero__faces span:nth-child(3) { background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 50%, var(--primary))); color: var(--text-main); }
.reel-hero__slot {
  display: none; align-items: center; gap: 0.5rem; margin: 0; padding: 0.625rem 0.75rem; border-radius: var(--radius-lg);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); color: var(--reel-hero-soft); font-size: 0.8125rem;
}
.reel-hero__slot strong { color: var(--text-inverse); }
.reel-hero__slot-dot { flex: none; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 35%, transparent); }
.reel-hero__book {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.125rem; border-radius: var(--radius-full);
  background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font-size: 0.9375rem; font-weight: 600; text-decoration: none; white-space: nowrap;
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 28%, transparent), var(--shadow-glow);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}

/* Story segments: each bar fills over the interval; done bars stay full; a click jumps */
.reel-hero__segs { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.5rem; }
.reel-hero__seg {
  display: grid; align-content: end; gap: 0.5rem; min-width: 0; min-height: 2.75rem; padding: 0.5rem 0 0.75rem; border: 0; background: none; cursor: pointer;
  color: var(--reel-hero-soft); font: 500 0.6875rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-align: left; text-transform: uppercase;
  transition: color var(--dur-2);
}
.reel-hero__seg-label { display: none; gap: 0.5rem; white-space: nowrap; }
.reel-hero__seg-bar { position: relative; height: 3px; overflow: hidden; border-radius: var(--radius-full); background: color-mix(in srgb, var(--text-inverse) 26%, transparent); transition: background-color var(--dur-2); }
.reel-hero__seg-fill {
  position: absolute; inset: 0; border-radius: inherit; transform: scaleX(0); transform-origin: left;
  background: linear-gradient(90deg, color-mix(in srgb, var(--primary-2) 45%, var(--text-inverse)), var(--text-inverse));
}
.reel-hero__seg.is-done .reel-hero__seg-fill, .reel-hero__seg[aria-current="true"] .reel-hero__seg-fill { transform: none; }
.reel-hero.is-playing .reel-hero__seg[aria-current="true"] .reel-hero__seg-fill { animation: reel-hero-fill var(--reel-hero-interval) linear forwards var(--reel-hero-state); }
.reel-hero__seg:is([aria-current="true"], :hover) { color: var(--text-inverse); }
.reel-hero__seg:hover .reel-hero__seg-bar { background: color-mix(in srgb, var(--text-inverse) 42%, transparent); }

/* Pause / play */
.reel-hero__pause {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: color-mix(in srgb, var(--surface-deep) 45%, transparent); color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-inverse) 24%, transparent), var(--highlight-inverse);
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.reel-hero__pause:hover { background: color-mix(in srgb, var(--surface-deep) 25%, transparent); }
.reel-hero__pause:active { transform: scale(0.92); }
.reel-hero__pause[hidden] { display: none; }
.reel-hero__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.reel-hero__icon-play, .reel-hero__pause[aria-pressed="true"] .reel-hero__icon-pause { display: none; }
.reel-hero__pause[aria-pressed="true"] .reel-hero__icon-play { display: block; }
.reel-hero__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

@media (min-width: 768px) {
  .reel-hero__inner { padding-bottom: 1.5rem; }
  .reel-hero__actions { display: flex; flex-wrap: wrap; }
  .reel-hero__card { grid-template-columns: auto minmax(0, 1fr) auto; }
  .reel-hero__faces, .reel-hero__slot, .reel-hero__seg-label { display: flex; }
}
@media (min-width: 1024px) {
  .reel-hero__inner { grid-template-columns: auto minmax(0, 1fr) 19rem; grid-template-areas: "copy copy card" "pause segs segs"; column-gap: 1.25rem; }
  .reel-hero__card { grid-template-columns: minmax(0, 1fr); align-self: end; padding: 1.125rem; }
}
@media (prefers-reduced-motion: reduce) {
  .reel-hero *, .reel-hero *::before, .reel-hero *::after { animation: none !important; }
}

@keyframes reel-hero-kb { from { transform: scale(1); } to { transform: scale(1.14) translate(var(--reel-hero-pan, 0%), -1%); } }
@keyframes reel-hero-rise { from { transform: translateY(105%); } }
@keyframes reel-hero-out { to { transform: translateY(-105%); } }
@keyframes reel-hero-fade { from { opacity: 0; transform: translateY(12px); filter: blur(6px); } }
@keyframes reel-hero-fade-out { to { opacity: 0; transform: translateY(-8px); filter: blur(4px); } }
@keyframes reel-hero-card { from { opacity: 0; transform: translateY(20px) scale(0.96); filter: blur(8px); } }
@keyframes reel-hero-fill { from { transform: scaleX(0); } to { transform: scaleX(1); } }
```

## JS

```js
document.querySelectorAll('[data-reel-hero]').forEach((hero) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const slides = [...hero.querySelectorAll('.reel-hero__slide')];
  const frames = [...hero.querySelectorAll('.reel-hero__frame')];
  const segs = [...hero.querySelectorAll('.reel-hero__seg')];
  const region = hero.querySelector('.reel-hero__slides');
  const pause = hero.querySelector('.reel-hero__pause');
  const count = slides.length;
  let current = 0;

  hero.classList.add('reel-hero--js');
  slides.forEach((slide, i) => { slide.inert = i !== 0; });

  // APG: the live region stays off while the show rotates and turns polite once it's stopped
  const rotating = () => hero.classList.contains('is-playing') && !hero.hasAttribute('data-paused');
  const syncLive = () => region.setAttribute('aria-live', rotating() ? 'off' : 'polite');
  const stop = (on = true) => {
    hero.toggleAttribute('data-paused', on);
    pause.setAttribute('aria-pressed', String(on));
    syncLive();
  };

  // Show a slide: old frame/slide → is-leaving (blur out, lines rise away), new one → is-active
  const go = (index) => {
    const next = (index + count) % count;
    if (next === current) return;
    [slides, frames].forEach((set) => set.forEach((el, i) => {
      el.classList.toggle('is-leaving', i === current);
      el.classList.toggle('is-active', i === next);
    }));
    slides.forEach((slide, i) => { slide.inert = i !== next; });
    segs.forEach((seg, i) => {
      seg.classList.toggle('is-done', i < next);
      if (i === next) seg.setAttribute('aria-current', 'true');
      else seg.removeAttribute('aria-current');
    });
    current = next;
  };

  // Auto-rotation: the active segment's fill animation is the timer, so pausing it (CSS) pauses the clock
  if (!reduce) {
    hero.classList.add('is-playing');
    pause.hidden = false;
  }
  syncLive();
  hero.addEventListener('animationend', (e) => {
    if (e.animationName === 'reel-hero-fill') go(current + 1);
  });
  pause.addEventListener('click', () => stop(!hero.hasAttribute('data-paused')));

  // Hover pauses for as long as the mouse stays; focus anywhere but the pause button stops rotation (APG)
  hero.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse') hero.setAttribute('data-hover', ''); });
  hero.addEventListener('pointerleave', () => hero.removeAttribute('data-hover'));
  hero.addEventListener('focusin', (e) => { if (e.target !== pause && rotating()) stop(); });
  new IntersectionObserver(([entry]) => hero.toggleAttribute('data-offscreen', !entry.isIntersecting)).observe(hero);

  // Manual navigation stops rotation: segments, ←/→ while focus is inside, and horizontal swipes
  segs.forEach((seg, i) => seg.addEventListener('click', () => { stop(); go(i); }));
  hero.addEventListener('keydown', (e) => {
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    e.preventDefault();
    stop();
    go(current + (e.key === 'ArrowRight' ? 1 : -1));
    if (segs.includes(document.activeElement)) segs[current].focus();
  });
  let start = null;
  hero.addEventListener('pointerdown', (e) => {
    if (e.pointerType !== 'mouse') start = { x: e.clientX, y: e.clientY };
  }, { passive: true });
  hero.addEventListener('pointercancel', () => { start = null; });
  hero.addEventListener('pointerup', (e) => {
    if (!start) return;
    const dx = e.clientX - start.x;
    const dy = e.clientY - start.y;
    start = null;
    if (Math.abs(dx) > 48 && Math.abs(dx) > Math.abs(dy) * 1.5) {
      stop();
      go(current + (dx < 0 ? 1 : -1));
    }
  });
});
```

## Notes

- APG auto-rotating carousel: the section is the carousel (`aria-roledescription="carousel"`, named by its `<h1>`), and each slide is a `group` with `aria-roledescription="slide"` labelled "1 of 4". The pause button (`aria-pressed`, "Pause slideshow") is the first focusable element. Mouse hover pauses until the pointer leaves. Focus on anything other than the pause button stops rotation until the button is pressed again, and so do segment clicks, ←/→ and swipes. The slides' live region is `off` while rotating and `polite` once stopped. Inactive slides are `inert` and `visibility: hidden`.
- The `<h1>` is the stable brand line (the glass kicker); each slide's big headline is an `<h2>`, so the page heading never changes under a reader. The photos are mood imagery (`alt=""`, in an `aria-hidden` layer), and each slide's text carries the message. The first photo is eager with `fetchpriority="high"`; the rest are `loading="lazy"`.
- Timing: the active segment's fill animation is the clock (`--reel-hero-interval`, default 7s). Its `animationend` advances the reel, and the pause button, hover and off-screen states all pause the fill and the Ken Burns zoom through one variable, `--reel-hero-state`. A paused reel resumes exactly where it stopped.
- Without JS it's a static hero on slide 1 (no rotation, no zoom; the segments are hidden). Reduced motion: no auto-rotation, no Ken Burns and no line animations, and slide changes from the segments, ←/→ or a swipe become instant cuts; the pause button isn't shown.
- Contrast: the scrim is at least 72% `--surface-deep` under the slide text and 55% at the left edge. Even over a pure-white photo, the headline stays above 6:1, and the body line and credit (`--reel-hero-soft`) stay above 9:1 where they sit. The kicker and booking card carry their own deep glass (worst case 10:1). The Book now button label is white on `--primary`→`--primary-hover` (5.2:1 or better).
- Use your own photos (any 16:9 or wider; `--reel-hero-origin` and `--reel-hero-pan` aim each zoom). Add or remove slides by keeping slides, frames and segments in step and updating the "n of N" labels.
