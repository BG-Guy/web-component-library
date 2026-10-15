# Milestone Sparks

A small reward for reading on, on a deep surface. Each heading marked `data-amb-sparks` gets a one-time burst the first time it comes fully into view: 6–12 four-point stars and dots fan up and out from behind it while a soft halo swells and fades (under 1.2s), leaving a faint glow behind the heading. While you scroll, a few twinkles spark near the side edges, ahead in the scroll direction, and fade within about 0.7s; they stop the moment you stop. Everything comes from a pool of 28 elements animated with transform and opacity. Depends on `tokens/variables.css`.

**Motion:** heading burst (Web Animations, 0.7–1.05s plus up to 120ms stagger, `cubic-bezier(0.16, 1, 0.3, 1)`) · halo swell and fade (1.1s) · lingering heading glow fades in (`--dur-5`, `--ease-out`) · edge twinkles while scrolling (0.5–0.75s) · cards lift with `--ease-spring`.

## HTML

```html
<div class="amb-sparks-demo">
  <div class="amb-sparks" aria-hidden="true">
    <span class="amb-sparks__halo"></span><span class="amb-sparks__halo"></span>
    <div class="amb-sparks__field">
      <span class="amb-sparks__star"></span><span class="amb-sparks__star"></span><span class="amb-sparks__star"></span><span class="amb-sparks__star"></span>
      <span class="amb-sparks__star"></span><span class="amb-sparks__star"></span><span class="amb-sparks__star"></span><span class="amb-sparks__star"></span>
      <span class="amb-sparks__star"></span><span class="amb-sparks__star"></span><span class="amb-sparks__star"></span><span class="amb-sparks__star"></span>
      <span class="amb-sparks__star"></span><span class="amb-sparks__star"></span><span class="amb-sparks__star"></span><span class="amb-sparks__star"></span>
      <span class="amb-sparks__dot"></span><span class="amb-sparks__dot"></span><span class="amb-sparks__dot"></span><span class="amb-sparks__dot"></span><span class="amb-sparks__dot"></span>
      <span class="amb-sparks__dot"></span><span class="amb-sparks__dot"></span><span class="amb-sparks__dot"></span><span class="amb-sparks__dot"></span><span class="amb-sparks__dot"></span>
    </div>
  </div>

  <section class="amb-sparks-demo__hero" aria-labelledby="amb-sparks-title">
    <div class="amb-sparks-demo__inner">
      <p class="amb-sparks-demo__eyebrow">Brand Home Services · Springfield</p>
      <h2 id="amb-sparks-title" class="amb-sparks-demo__display" data-amb-sparks>Your to-do list, <span>done properly.</span></h2>
      <p class="amb-sparks-demo__lead">Repairs, renovations and seasonal upkeep from one trusted crew, with a photo update at every milestone.</p>
      <div class="amb-sparks-demo__actions">
        <a class="amb-sparks-demo__btn amb-sparks-demo__btn--primary" href="#amb-sparks-book">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-sparks-demo__btn amb-sparks-demo__btn--ghost" href="tel:+15555550123">(555) 555-0123</a>
      </div>
      <p class="amb-sparks-demo__hint">
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6.3 6.3l2.1 2.1M15.6 15.6l2.1 2.1M6.3 17.7l2.1-2.1M15.6 8.4l2.1-2.1" /></svg>
        Read on: each section lights up
      </p>
    </div>
  </section>

  <section class="amb-sparks-demo__section" aria-labelledby="amb-sparks-services">
    <div class="amb-sparks-demo__inner">
      <p class="amb-sparks-demo__eyebrow">What we take off your list</p>
      <h2 id="amb-sparks-services" class="amb-sparks-demo__title" data-amb-sparks>Small fixes to whole rooms.</h2>
      <ul class="amb-sparks-demo__cards" role="list">
        <li class="amb-sparks-demo__card">
          <span class="amb-sparks-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18v3h3l6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z" /></svg></span>
          <h3><a href="#amb-sparks-book">Repairs</a></h3>
          <p>Doors, drywall, fixtures and the jobs that have waited all year.</p>
          <p class="amb-sparks-demo__price">from <b>$95</b> / hour</p>
        </li>
        <li class="amb-sparks-demo__card">
          <span class="amb-sparks-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M3 21h18M5 21V8l7-5 7 5v13" /><path d="M9 21v-6h6v6" /></svg></span>
          <h3><a href="#amb-sparks-book">Renovations</a></h3>
          <p>Kitchens and bathrooms planned, built and finished by one crew.</p>
          <p class="amb-sparks-demo__price">from <b>$12,000</b></p>
        </li>
        <li class="amb-sparks-demo__card">
          <span class="amb-sparks-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" /><path d="m9 15 2 2 4-4" /></svg></span>
          <h3><a href="#amb-sparks-book">Seasonal upkeep</a></h3>
          <p>Gutters, filters and smoke alarms checked four times a year.</p>
          <p class="amb-sparks-demo__price">from <b>$79</b> / visit</p>
        </li>
        <li class="amb-sparks-demo__card">
          <span class="amb-sparks-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M12 9v4M12 17h.01" /><path d="M10.3 3.9 2.4 18a2 2 0 0 0 1.7 3h15.8a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z" /></svg></span>
          <h3><a href="#amb-sparks-book">Emergencies</a></h3>
          <p>A real person answers 24/7, with a technician on the way within the hour.</p>
          <p class="amb-sparks-demo__price">callout <b>$149</b></p>
        </li>
      </ul>
    </div>
  </section>

  <section class="amb-sparks-demo__section" aria-labelledby="amb-sparks-proof">
    <div class="amb-sparks-demo__inner amb-sparks-demo__proof">
      <div>
        <p class="amb-sparks-demo__eyebrow">Neighbours agree</p>
        <h2 id="amb-sparks-proof" class="amb-sparks-demo__title" data-amb-sparks>1,800 homes, 4.9 stars.</h2>
        <dl class="amb-sparks-demo__stats">
          <div><dt>jobs finished this year</dt><dd>6,400</dd></div>
          <div><dt>average rating</dt><dd>4.9</dd></div>
          <div><dt>quote you can trust</dt><dd>Fixed</dd></div>
        </dl>
      </div>
      <figure class="amb-sparks-demo__quote">
        <blockquote><p>"Every evening I got a photo of what was finished that day. Watching the list shrink was half the fun."</p></blockquote>
        <figcaption><strong>Jordan M.</strong> · Northside</figcaption>
      </figure>
    </div>
  </section>

  <section class="amb-sparks-demo__section amb-sparks-demo__cta" id="amb-sparks-book" aria-labelledby="amb-sparks-cta">
    <div class="amb-sparks-demo__inner">
      <h2 id="amb-sparks-cta" class="amb-sparks-demo__display amb-sparks-demo__display--sm" data-amb-sparks>What's next <span>on your list?</span></h2>
      <p class="amb-sparks-demo__lead">Westlake, Northside, Riverside and the rest of Springfield. Free quotes, fixed prices.</p>
      <div class="amb-sparks-demo__actions">
        <a class="amb-sparks-demo__btn amb-sparks-demo__btn--primary" href="mailto:hello@example.com">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-sparks-demo__btn amb-sparks-demo__btn--ghost" href="tel:+15555550123">Call (555) 555-0123</a>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* Layer: behind its section by default, behind the whole page with --page.
   Particles are positioned in the layer's own coordinates, so no sticky frame is needed. */
.amb-sparks {
  --amb-sparks-c1: color-mix(in srgb, var(--accent) 80%, var(--text-inverse));    /* gold */
  --amb-sparks-c2: color-mix(in srgb, var(--primary-2) 60%, var(--text-inverse)); /* teal */
  --amb-sparks-c3: color-mix(in srgb, var(--primary) 55%, var(--text-inverse));   /* blue */
  position: absolute; inset: 0; z-index: -1; overflow: clip; pointer-events: none;
}
.amb-sparks--page { position: fixed; }
.amb-sparks::after { /* contrast guard: a veil of the page colour, 0–1 */
  content: ""; position: absolute; inset: 0;
  background: var(--surface-deep); opacity: var(--amb-sparks-scrim, 0);
}

/* Pool: hidden until a Web Animation plays it, then hidden again */
.amb-sparks__field { position: absolute; inset: 0; opacity: 0.45; } /* group opacity caps every pixel, even overlaps */
.amb-sparks__halo, .amb-sparks__star, .amb-sparks__dot { position: absolute; top: 0; left: 0; visibility: hidden; opacity: 0; }
.amb-sparks__halo {
  width: 20rem; height: 8rem; margin: -4rem 0 0 -10rem; border-radius: 50%;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 45%, transparent), color-mix(in srgb, var(--primary-2) 12%, transparent) 60%, transparent);
}
.amb-sparks__star { width: 1.125rem; height: 1.125rem; margin: -0.5625rem 0 0 -0.5625rem; color: var(--amb-sparks-c1); }
.amb-sparks__star:nth-child(3n + 2) { color: var(--amb-sparks-c2); }
.amb-sparks__star:nth-child(3n) { color: var(--amb-sparks-c3); }
.amb-sparks__star:nth-child(4n) { width: 0.75rem; height: 0.75rem; margin: -0.375rem 0 0 -0.375rem; }
.amb-sparks__star::before { /* pre-blurred glow, no filter */
  content: ""; position: absolute; inset: -70%; border-radius: 50%;
  background: radial-gradient(closest-side, color-mix(in srgb, currentColor 40%, transparent), transparent);
}
.amb-sparks__star::after { /* four-point star */
  content: ""; position: absolute; inset: 0; background: currentColor;
  clip-path: polygon(50% 0, 59% 41%, 100% 50%, 59% 59%, 50% 100%, 41% 59%, 0 50%, 41% 41%);
}
.amb-sparks__dot {
  width: 0.375rem; height: 0.375rem; margin: -0.1875rem 0 0 -0.1875rem; border-radius: 50%;
  background: currentColor; box-shadow: 0 0 0.5rem 0.0625rem currentColor; color: var(--amb-sparks-c1);
}
.amb-sparks__dot:nth-child(even) { color: var(--amb-sparks-c2); }

/* Marked headings: a faint glow behind the text. It's the whole effect without JS or under reduced
   motion; with motion it appears once the heading's burst has played. */
[data-amb-sparks] { position: relative; isolation: isolate; }
[data-amb-sparks]::before {
  content: ""; position: absolute; inset: -0.8em 0; z-index: -1; pointer-events: none;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 30%, transparent), transparent);
  transition: opacity var(--dur-5) var(--ease-out);
}
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  [data-amb-sparks]:not([data-amb-sparks="lit"])::before { opacity: 0; }
  [data-amb-sparks=""]::before { animation: amb-sparks-failsafe 0.6s 2.5s forwards; } /* JS never ran: show the still */
}
@keyframes amb-sparks-failsafe { to { opacity: 1; } }

/* Demo page: a deep landing page with milestones to reach */
.amb-sparks-demo {
  position: relative; isolation: isolate; color: var(--text-inverse); font-family: var(--font-sans);
  background:
    radial-gradient(60rem 30rem at 15% 0%, color-mix(in srgb, var(--primary) 18%, transparent), transparent 70%),
    radial-gradient(40rem 30rem at 100% 55%, color-mix(in srgb, var(--primary-2) 9%, transparent), transparent 70%),
    var(--surface-deep);
}
.amb-sparks-demo__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.amb-sparks-demo__hero { display: grid; align-items: center; min-height: 90vh; min-height: 90svh; padding-block: 5rem 4rem; }
.amb-sparks-demo__section { padding-block: clamp(4.5rem, 10vw, 7rem); }
.amb-sparks-demo__eyebrow {
  display: flex; align-items: center; gap: 0.625rem; margin: 0;
  font: 600 0.75rem/1.3 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.amb-sparks-demo__eyebrow::before {
  content: ""; flex: none; width: 0.625rem; height: 0.625rem; background: var(--accent);
  clip-path: polygon(50% 0, 62% 38%, 100% 50%, 62% 62%, 50% 100%, 38% 62%, 0 50%, 38% 38%);
}
.amb-sparks-demo__display {
  max-width: 14ch; margin: 1.5rem 0 0; font: 600 clamp(2.5rem, 1.3rem + 5vw, 5rem)/0.98 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-sparks-demo__display span, .amb-sparks-demo__title span {
  background: linear-gradient(100deg, var(--text-inverse) 10%, color-mix(in srgb, var(--accent) 55%, var(--text-inverse)) 90%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.amb-sparks-demo__display--sm { max-width: 16ch; font-size: clamp(2.25rem, 1.4rem + 3.6vw, 3.75rem); }
.amb-sparks-demo__lead { max-width: 34rem; margin: 1.5rem 0 0; font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; }
.amb-sparks-demo__title {
  max-width: 20ch; margin: 1rem 0 0; font: 600 clamp(1.875rem, 1.2rem + 2.6vw, 3rem)/1.05 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-sparks-demo__hint { display: flex; align-items: center; gap: 0.5rem; margin: 3rem 0 0; font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.amb-sparks-demo__hint svg { flex: none; fill: none; stroke: var(--accent); stroke-width: 2; stroke-linecap: round; }
.amb-sparks-demo a:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Buttons */
.amb-sparks-demo__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
.amb-sparks-demo__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem;
  border-radius: var(--radius-full); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out), background-color var(--dur-2);
}
.amb-sparks-demo__btn svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-sparks-demo__btn:hover { transform: translateY(-2px); }
.amb-sparks-demo__btn:active { transform: scale(0.97); }
.amb-sparks-demo__btn--primary { background: var(--surface-light); color: var(--text-main); box-shadow: 0 12px 40px -12px color-mix(in srgb, var(--accent) 70%, transparent); }
.amb-sparks-demo__btn--ghost { background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.amb-sparks-demo__btn--ghost:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }

/* Service cards: near-opaque panels, so muted copy keeps its contrast */
.amb-sparks-demo__cards {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr)); gap: 1rem;
  margin: 2.5rem 0 0; padding: 0; list-style: none;
}
.amb-sparks-demo__card {
  position: relative; display: grid; align-content: start; gap: 0.5rem; padding: 1.5rem; border-radius: var(--radius-2xl);
  background: linear-gradient(var(--glass-inverse), var(--glass-inverse)), color-mix(in srgb, var(--surface-deep) 92%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 24px 48px -24px var(--surface-deep);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-sparks-demo__card:hover {
  transform: translateY(-4px);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--accent) 40%, transparent), var(--highlight-inverse), 0 28px 56px -24px color-mix(in srgb, var(--accent) 30%, transparent);
}
.amb-sparks-demo__card h3 { margin: 0.75rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-sparks-demo__card h3 a { color: inherit; text-decoration: none; }
.amb-sparks-demo__card h3 a::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-2xl); }
.amb-sparks-demo__card h3 a:focus-visible { outline: none; }
.amb-sparks-demo__card h3 a:focus-visible::after { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.amb-sparks-demo__card p { margin: 0; color: var(--text-inverse-muted); line-height: 1.55; }
.amb-sparks-demo__card .amb-sparks-demo__price { margin-top: 0.75rem; color: var(--text-inverse); font: 500 0.8125rem var(--font-mono); }
.amb-sparks-demo__price b { font-size: 1.125rem; font-weight: 600; }
.amb-sparks-demo__icon {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: var(--radius-lg); color: var(--accent);
  background: color-mix(in srgb, var(--accent) 12%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--accent) 28%, transparent);
}
.amb-sparks-demo__icon svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }

/* Proof */
.amb-sparks-demo__proof { display: grid; gap: 2.5rem; align-items: center; }
.amb-sparks-demo__stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; margin: 2.25rem 0 0; }
.amb-sparks-demo__stats div { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.375rem; padding-top: 1rem; border-top: 1px solid var(--border-inverse); }
.amb-sparks-demo__stats dt { font-size: 0.8125rem; line-height: 1.4; }
.amb-sparks-demo__stats dd { margin: 0; font: 600 clamp(1.5rem, 1.2rem + 1.4vw, 2.25rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-sparks-demo__quote {
  margin: 0; padding: 1.75rem; border-radius: var(--radius-2xl);
  background: linear-gradient(var(--glass-inverse), var(--glass-inverse)), color-mix(in srgb, var(--surface-deep) 92%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.amb-sparks-demo__quote blockquote { margin: 0; }
.amb-sparks-demo__quote blockquote p { margin: 0; font: 500 clamp(1.125rem, 1rem + 0.6vw, 1.375rem)/1.45 var(--font-display); letter-spacing: -0.01em; }
.amb-sparks-demo__quote figcaption { margin-top: 1.25rem; color: var(--text-inverse-muted); font-size: 0.875rem; }
.amb-sparks-demo__quote strong { color: var(--text-inverse); }
.amb-sparks-demo__cta { padding-bottom: clamp(6rem, 18vh, 10rem); }

@media (min-width: 768px) {
  .amb-sparks-demo__proof { grid-template-columns: 1.1fr 0.9fr; gap: 4rem; }
  .amb-sparks-demo__quote { padding: 2.25rem; }
}
```

## JS

```js
document.querySelectorAll('.amb-sparks').forEach((layer) => {
  const page = layer.classList.contains('amb-sparks--page'), host = page ? document.documentElement : layer.parentElement;
  const scope = page ? document : host; // the headings it celebrates
  const stars = [...layer.querySelectorAll('.amb-sparks__star')], dots = [...layer.querySelectorAll('.amb-sparks__dot')];
  const halos = [...layer.querySelectorAll('.amb-sparks__halo')], marks = [...scope.querySelectorAll('[data-amb-sparks]')];
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return; // the CSS still: a faint glow behind each marked heading

  const ease = 'cubic-bezier(0.16, 1, 0.3, 1)', rand = (a, b) => a + Math.random() * (b - a);
  const take = (list) => list.find((el) => !el.getAnimations().length); // the pool: 28 elements, reused
  const play = (el, frames, opts) => el.animate(frames.map((k) => ({ ...k, visibility: 'visible' })), opts);
  let VW = innerWidth, VH = innerHeight, raf = 0, lastY = null, travel = 0, dir = 1, visible = page;

  // One-time burst behind a heading: 6–12 stars and dots fan up and out, and a halo swells and fades (under 1.2s)
  const burst = (el) => {
    const l = layer.getBoundingClientRect(), r = el.getBoundingClientRect(); // one-off reads per burst
    const cx = r.left + r.width / 2 - l.left, cy = r.top + r.height / 2 - l.top;
    el.dataset.ambSparks = 'lit'; // leaves a faint glow behind the heading
    const halo = take(halos);
    if (halo) {
      const sx = (r.width + 96) / 320, sy = (r.height + 64) / 128, at = `translate(${cx}px, ${cy}px)`;
      play(halo, [
        { transform: `${at} scale(${sx * 0.4}, ${sy * 0.4})`, opacity: 0 },
        { transform: `${at} scale(${sx}, ${sy})`, opacity: 1, offset: 0.3 },
        { transform: `${at} scale(${sx * 1.2}, ${sy * 1.2})`, opacity: 0 },
      ], { duration: 1100, easing: ease });
    }
    for (let i = 0, n = 6 + Math.floor(Math.random() * 7); i < n; i++) {
      const p = take(i % 3 === 2 ? dots : stars) || take(stars) || take(dots);
      if (!p) break;
      // Start along the heading, fan upward and sideways (away from the copy below), spin a little
      const ox = cx + rand(-0.4, 0.4) * r.width, oy = cy + rand(-0.2, 0.2) * r.height;
      const a = -Math.PI / 2 + rand(-1, 1) * 1.75, d = rand(40, 130), spin = rand(-180, 180);
      const tx = ox + Math.cos(a) * d, ty = oy + Math.sin(a) * d;
      play(p, [
        { transform: `translate(${ox}px, ${oy}px) scale(0.2) rotate(0deg)`, opacity: 0 },
        { transform: `translate(${ox + (tx - ox) * 0.6}px, ${oy + (ty - oy) * 0.6}px) scale(1) rotate(${spin * 0.6}deg)`, opacity: 1, offset: 0.35 },
        { transform: `translate(${tx}px, ${ty}px) scale(0) rotate(${spin}deg)`, opacity: 0 },
      ], { duration: rand(700, 1050), delay: rand(0, 120), easing: ease });
    }
  };

  // While scrolling: a twinkle near a side edge, ahead in the scroll direction, for every 240px of travel
  const twinkle = (l) => {
    const p = take(stars);
    if (!p) return;
    const x = (Math.random() < 0.5 ? rand(0.02, 0.12) : rand(0.88, 0.98)) * VW - l.left;
    const y = (dir > 0 ? rand(0.6, 0.95) : rand(0.05, 0.4)) * VH - l.top;
    play(p, [
      { transform: `translate(${x}px, ${y}px) scale(0) rotate(0deg)`, opacity: 0 },
      { transform: `translate(${x}px, ${y}px) scale(0.8) rotate(45deg)`, opacity: 1, offset: 0.4 },
      { transform: `translate(${x}px, ${y - dir * 16}px) scale(0) rotate(90deg)`, opacity: 0 },
    ], { duration: rand(500, 750), easing: 'ease-out' });
  };
  const frame = () => {
    raf = 0;
    const l = layer.getBoundingClientRect(), y = page ? scrollY : -l.top; // the one layout read per frame
    if (lastY !== null && y !== lastY) { dir = Math.sign(y - lastY); travel = Math.min(720, travel + Math.abs(y - lastY)); }
    lastY = y;
    for (; travel >= 240; travel -= 240) twinkle(l);
  };

  // Each marked heading bursts once, the first time it's fully in view
  const io = new IntersectionObserver((entries) => entries.forEach((e) => {
    if (!e.isIntersecting) return;
    io.unobserve(e.target);
    burst(e.target);
  }), { rootMargin: '0px 0px -12% 0px', threshold: 1 });
  marks.forEach((m) => { m.dataset.ambSparks = 'ready'; io.observe(m); });

  // Event-driven: one frame per scroll, nothing at all while idle, off-screen or in a hidden tab
  addEventListener('scroll', () => {
    if (!raf && visible && document.visibilityState === 'visible') raf = requestAnimationFrame(frame);
  }, { passive: true });
  addEventListener('resize', () => { VW = innerWidth; VH = innerHeight; }, { passive: true });
  if (!page) new IntersectionObserver(([e]) => { visible = e.isIntersecting; lastY = null; }).observe(host);
});
```

## Notes

- **Placement.** The layer is decorative (`aria-hidden`, `pointer-events: none`). By default it's the first child of a `position: relative; isolation: isolate` section, and particles are placed in the layer's own coordinates, so bursts sit exactly behind their headings and scroll with them. Add `.amb-sparks--page` to fix it behind the whole page instead: it then celebrates marked headings anywhere in the document, and sections need transparent backgrounds. Use one ambient background per page. Mark section headings with `data-amb-sparks`; the component gives them `position: relative; isolation: isolate` so their glow sits just behind the text, inside the heading's box, which can't cause sideways scroll.
- **Contrast.** All particles sit in one group capped at 45% opacity, so even overlapping stars can't exceed it, and there are no white sparkles. Worst case in the demo: body copy in `--text-inverse` over a gold star inside the halo is 4.5:1, and over the halo alone 11.5:1. Bursts fan upward and sideways, away from the copy below each heading, and twinkles stay in the outer 12% of each side. Muted copy appears only on the near-opaque cards (7:1). Set `--amb-sparks-scrim` (0–1) to lay a `--surface-deep` veil over the layer.
- **Performance.** A fixed pool of 28 elements (16 stars, 10 dots, 2 halos) is animated only through transform and opacity Web Animations, and returns to `visibility: hidden` when each animation ends. When the pool is busy, extra particles are skipped. Glows are pre-blurred radial gradients, with no `filter` and no canvas. There's no continuous loop: one rAF frame per scroll event batch, a single `getBoundingClientRect`, and nothing while idle, off-screen or in a hidden tab. Burst triggers are IntersectionObservers.
- **Motion budget.** Every animation is a one-shot: bursts last under 1.2s and play once per heading, and twinkles last under 0.75s and spawn only from scroll travel (one per 240px, at most three at once). Nothing moves on its own, so no pause control is needed.
- **Reduced motion and no JS.** Marked headings show a static faint glow behind them, with no bursts or twinkles. With scripting on, the glows wait for their bursts, and a 2.5s CSS failsafe reveals them if JS never runs. To retheme, change `--amb-sparks-c1`–`c3` (re-check them at the 45% cap) and the halo gradient.
