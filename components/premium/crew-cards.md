# Crew Cards

Team cards for the technicians a homeowner can ask for by name. Each portrait sits in an organic blob over a role-coloured gradient shape. On hover the blob morphs into a new shape while the shape behind it turns, the "jobs completed" count spins up like an odometer, the card tilts towards the pointer, and the request button and socials slide up into colour. On phones the cards become a full-bleed scroll-snap row. Depends on `tokens/variables.css`.

**Motion:** portrait blob morph (CSS `d: path()` on an SVG `clipPath`, or `border-radius` where `d` isn't supported; `--dur-5`, `--ease-spring`) · backing shape turn (`--dur-5`, `--ease-spring`) · odometer digit roll (`--dur-5` × 1.4, `--ease-out`, staggered) · pointer tilt and lift (`--dur-4`, `--ease-out`) · dock slide-up (`--dur-4`, `--ease-spring`, staggered).

## HTML

```html
<section class="crew-cards" aria-labelledby="crew-cards-title" data-crew-cards>
  <div class="crew-cards__inner">
    <header class="crew-cards__head">
      <div>
        <p class="crew-cards__eyebrow">The crew</p>
        <h2 id="crew-cards-title" class="crew-cards__title">Licensed pros you can ask for by name.</h2>
        <p class="crew-cards__lead">Every technician is background-checked, certified for the work they do and rated by the Springfield homeowners they've helped.</p>
      </div>
      <a class="crew-cards__all" href="#team">
        Meet all 24 pros
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </a>
    </header>

    <ul class="crew-cards__list" role="list" aria-label="Technicians">
      <li class="crew-cards__item">
        <article class="crew-cards__card crew-cards__card--plumbing" aria-labelledby="crew-cards-dana" style="--crew-cards-clip: url(#crew-cards-clip-dana); --crew-cards-morph: path('M0.46 0.01C0.76 0 1 0.26 0.99 0.54C0.98 0.8 0.82 0.99 0.58 0.97C0.3 0.95 0.02 0.74 0.01 0.44C0 0.18 0.2 0.02 0.46 0.01Z')">
          <div class="crew-cards__media">
            <span class="crew-cards__shape-bg" aria-hidden="true"></span>
            <div class="crew-cards__photo"><img src="dana.jpg" width="480" height="480" alt="Portrait of Dana Whitfield" loading="lazy" decoding="async"></div>
            <svg class="crew-cards__defs" width="0" height="0" aria-hidden="true" focusable="false"><clipPath id="crew-cards-clip-dana" clipPathUnits="objectBoundingBox"><path class="crew-cards__blob" d="M0.58 0.03C0.82 0.04 0.98 0.2 0.97 0.42C0.96 0.7 0.8 0.97 0.52 0.98C0.24 0.99 0.04 0.8 0.03 0.55C0.02 0.28 0.3 0.02 0.58 0.03Z" /></clipPath></svg>
            <p class="crew-cards__status"><span class="crew-cards__dot" aria-hidden="true"></span>Next free Thu</p>
          </div>
          <div class="crew-cards__body">
            <h3 id="crew-cards-dana" class="crew-cards__name">Dana Whitfield</h3>
            <p class="crew-cards__role">Master plumber · Westlake</p>
            <ul class="crew-cards__chips" role="list" aria-label="Certifications"><li>Master Plumber</li><li>Backflow</li><li>EPA Lead-Safe</li></ul>
            <p class="crew-cards__jobs"><span class="crew-cards__count">1,284</span> jobs completed</p>
          </div>
          <div class="crew-cards__dock">
            <a class="crew-cards__request" href="#book">Request Dana <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
            <ul class="crew-cards__socials" role="list">
              <li><a href="#linkedin" aria-label="Dana on LinkedIn"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zM4 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4z" /></svg></a></li>
              <li><a href="#instagram" aria-label="Dana on Instagram"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M8 3h8a5 5 0 0 1 5 5v8a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5V8a5 5 0 0 1 5-5zM12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM17.5 6.5h.01" /></svg></a></li>
            </ul>
          </div>
        </article>
      </li>

      <li class="crew-cards__item">
        <article class="crew-cards__card crew-cards__card--hvac" aria-labelledby="crew-cards-marcus" style="--crew-cards-clip: url(#crew-cards-clip-marcus); --crew-cards-morph: path('M0.56 0.01C0.84 0.03 0.99 0.16 0.98 0.4C0.97 0.72 0.76 0.98 0.46 0.99C0.18 1 0.03 0.78 0.02 0.5C0.01 0.22 0.28 0 0.56 0.01Z')">
          <div class="crew-cards__media">
            <span class="crew-cards__shape-bg" aria-hidden="true"></span>
            <div class="crew-cards__photo"><img src="marcus.jpg" width="480" height="480" alt="Portrait of Marcus Reyes" loading="lazy" decoding="async"></div>
            <svg class="crew-cards__defs" width="0" height="0" aria-hidden="true" focusable="false"><clipPath id="crew-cards-clip-marcus" clipPathUnits="objectBoundingBox"><path class="crew-cards__blob" d="M0.44 0.04C0.72 0 0.97 0.22 0.96 0.48C0.95 0.76 0.84 0.95 0.56 0.97C0.28 0.99 0.06 0.84 0.04 0.58C0.02 0.3 0.18 0.08 0.44 0.04Z" /></clipPath></svg>
            <p class="crew-cards__status"><span class="crew-cards__dot" aria-hidden="true"></span>Next free tomorrow</p>
          </div>
          <div class="crew-cards__body">
            <h3 id="crew-cards-marcus" class="crew-cards__name">Marcus Reyes</h3>
            <p class="crew-cards__role">HVAC technician · Northside</p>
            <ul class="crew-cards__chips" role="list" aria-label="Certifications"><li>NATE</li><li>EPA 608</li><li>Heat pumps</li></ul>
            <p class="crew-cards__jobs"><span class="crew-cards__count">962</span> jobs completed</p>
          </div>
          <div class="crew-cards__dock">
            <a class="crew-cards__request" href="#book">Request Marcus <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
            <ul class="crew-cards__socials" role="list">
              <li><a href="#linkedin" aria-label="Marcus on LinkedIn"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zM4 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4z" /></svg></a></li>
              <li><a href="#instagram" aria-label="Marcus on Instagram"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M8 3h8a5 5 0 0 1 5 5v8a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5V8a5 5 0 0 1 5-5zM12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM17.5 6.5h.01" /></svg></a></li>
            </ul>
          </div>
        </article>
      </li>

      <li class="crew-cards__item">
        <article class="crew-cards__card crew-cards__card--electrical" aria-labelledby="crew-cards-priya" style="--crew-cards-clip: url(#crew-cards-clip-priya); --crew-cards-morph: path('M0.42 0.02C0.7 0 0.96 0.18 0.97 0.44C0.98 0.74 0.82 0.97 0.58 0.98C0.3 0.99 0.04 0.86 0.02 0.58C0 0.3 0.16 0.04 0.42 0.02Z')">
          <div class="crew-cards__media">
            <span class="crew-cards__shape-bg" aria-hidden="true"></span>
            <div class="crew-cards__photo"><img src="priya.jpg" width="480" height="480" alt="Portrait of Priya Shah" loading="lazy" decoding="async"></div>
            <svg class="crew-cards__defs" width="0" height="0" aria-hidden="true" focusable="false"><clipPath id="crew-cards-clip-priya" clipPathUnits="objectBoundingBox"><path class="crew-cards__blob" d="M0.5 0.02C0.8 0.02 1 0.3 0.98 0.56C0.96 0.82 0.7 1 0.42 0.97C0.16 0.94 0 0.68 0.02 0.4C0.04 0.14 0.24 0.02 0.5 0.02Z" /></clipPath></svg>
            <p class="crew-cards__status"><span class="crew-cards__dot" aria-hidden="true"></span>Next free Fri</p>
          </div>
          <div class="crew-cards__body">
            <h3 id="crew-cards-priya" class="crew-cards__name">Priya Shah</h3>
            <p class="crew-cards__role">Licensed electrician · Riverside</p>
            <ul class="crew-cards__chips" role="list" aria-label="Certifications"><li>Master Electrician</li><li>EV chargers</li><li>Panel upgrades</li></ul>
            <p class="crew-cards__jobs"><span class="crew-cards__count">2,071</span> jobs completed</p>
          </div>
          <div class="crew-cards__dock">
            <a class="crew-cards__request" href="#book">Request Priya <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
            <ul class="crew-cards__socials" role="list">
              <li><a href="#linkedin" aria-label="Priya on LinkedIn"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zM4 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4z" /></svg></a></li>
              <li><a href="#instagram" aria-label="Priya on Instagram"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M8 3h8a5 5 0 0 1 5 5v8a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5V8a5 5 0 0 1 5-5zM12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM17.5 6.5h.01" /></svg></a></li>
            </ul>
          </div>
        </article>
      </li>

      <li class="crew-cards__item">
        <article class="crew-cards__card crew-cards__card--roofing" aria-labelledby="crew-cards-sam" style="--crew-cards-clip: url(#crew-cards-clip-sam); --crew-cards-morph: path('M0.58 0.03C0.82 0.04 0.98 0.2 0.97 0.42C0.96 0.7 0.8 0.97 0.52 0.98C0.24 0.99 0.04 0.8 0.03 0.55C0.02 0.28 0.3 0.02 0.58 0.03Z')">
          <div class="crew-cards__media">
            <span class="crew-cards__shape-bg" aria-hidden="true"></span>
            <div class="crew-cards__photo"><img src="sam.jpg" width="480" height="480" alt="Portrait of Sam Okafor" loading="lazy" decoding="async"></div>
            <svg class="crew-cards__defs" width="0" height="0" aria-hidden="true" focusable="false"><clipPath id="crew-cards-clip-sam" clipPathUnits="objectBoundingBox"><path class="crew-cards__blob" d="M0.46 0.01C0.76 0 1 0.26 0.99 0.54C0.98 0.8 0.82 0.99 0.58 0.97C0.3 0.95 0.02 0.74 0.01 0.44C0 0.18 0.2 0.02 0.46 0.01Z" /></clipPath></svg>
            <p class="crew-cards__status"><span class="crew-cards__dot" aria-hidden="true"></span>Next free Mon</p>
          </div>
          <div class="crew-cards__body">
            <h3 id="crew-cards-sam" class="crew-cards__name">Sam Okafor</h3>
            <p class="crew-cards__role">Roofing &amp; gutters · Springfield</p>
            <ul class="crew-cards__chips" role="list" aria-label="Certifications"><li>Roofing licence</li><li>Storm repair</li><li>Gutter guards</li></ul>
            <p class="crew-cards__jobs"><span class="crew-cards__count">738</span> jobs completed</p>
          </div>
          <div class="crew-cards__dock">
            <a class="crew-cards__request" href="#book">Request Sam <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
            <ul class="crew-cards__socials" role="list">
              <li><a href="#linkedin" aria-label="Sam on LinkedIn"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zM4 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4z" /></svg></a></li>
              <li><a href="#instagram" aria-label="Sam on Instagram"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M8 3h8a5 5 0 0 1 5 5v8a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5V8a5 5 0 0 1 5-5zM12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM17.5 6.5h.01" /></svg></a></li>
            </ul>
          </div>
        </article>
      </li>
    </ul>
  </div>
</section>
```

## CSS

```css
/* Section */
.crew-cards { background: linear-gradient(180deg, var(--surface-light), var(--surface-muted)); color: var(--text-main); font-family: var(--font-sans); }
.crew-cards :is(.crew-cards__all, .crew-cards__request, .crew-cards__socials) svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.crew-cards__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.crew-cards__head { display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 1.5rem 2rem; margin-bottom: 2.5rem; }
.crew-cards__head > div { max-width: 38rem; }
.crew-cards__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.crew-cards__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.crew-cards__lead { margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.crew-cards__all {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.125rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: box-shadow var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.crew-cards__all:hover { transform: translateY(-1px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-md); }
.crew-cards__all svg, .crew-cards__request svg { transition: transform var(--dur-3) var(--ease-spring); }
.crew-cards__all:hover svg, .crew-cards__request:hover svg { transform: translateX(3px); }

/* Phones: a full-bleed scroll-snap row with soft edges */
.crew-cards__list {
  display: flex; gap: 1rem; margin: 0 calc(var(--gutter) * -1); padding: 0.75rem var(--gutter) 2rem; list-style: none;
  overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-inline: var(--gutter); overscroll-behavior-x: contain; scrollbar-width: none;
  -webkit-mask: linear-gradient(90deg, transparent, black var(--gutter), black calc(100% - var(--gutter)), transparent);
  mask: linear-gradient(90deg, transparent, black var(--gutter), black calc(100% - var(--gutter)), transparent);
}
.crew-cards__list::-webkit-scrollbar { display: none; }
.crew-cards__item { flex: 0 0 min(80%, 18.5rem); scroll-snap-align: start; }

/* Card: tilts toward the pointer (angles set by JS), lifts on hover */
.crew-cards__card {
  --crew-cards-role: var(--primary);
  --crew-cards-ink: color-mix(in srgb, var(--crew-cards-role) 55%, var(--text-main)); /* button fill: white text 4.6:1+ */
  position: relative; isolation: isolate; display: flex; flex-direction: column; height: 100%;
  padding: 0.625rem; border-radius: var(--radius-2xl); background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-lg);
  transform: perspective(900px) translateY(var(--crew-cards-lift, 0px)) rotateX(var(--crew-cards-rx, 0deg)) rotateY(var(--crew-cards-ry, 0deg));
  transition: transform var(--dur-4) var(--ease-out), box-shadow var(--dur-4) var(--ease-out);
}
.crew-cards__card--hvac { --crew-cards-role: var(--primary-2); }
.crew-cards__card--electrical { --crew-cards-role: var(--accent); }
.crew-cards__card--roofing { --crew-cards-role: color-mix(in srgb, var(--danger) 70%, var(--warning)); }
.crew-cards__card::after { /* soft light that follows the pointer */
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; pointer-events: none; opacity: 0;
  background: radial-gradient(22rem circle at var(--crew-cards-mx, 50%) var(--crew-cards-my, 0%), color-mix(in srgb, var(--crew-cards-role) 10%, transparent), transparent 60%);
  transition: opacity var(--dur-3);
}
.crew-cards__card:hover {
  --crew-cards-lift: -6px;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl), 0 24px 48px -28px var(--crew-cards-role);
}
.crew-cards__card:hover::after { opacity: 1; }

/* Portrait: role-coloured shape behind, blob-clipped photo in front */
.crew-cards__media {
  position: relative; display: flex; aspect-ratio: 1 / 0.9; overflow: hidden; border-radius: calc(var(--radius-2xl) - 0.375rem);
  background:
    radial-gradient(circle at 1px 1px, color-mix(in srgb, var(--crew-cards-role) 24%, transparent) 1px, transparent 1.5px) 0 0 / 14px 14px,
    radial-gradient(90% 75% at 50% 100%, color-mix(in srgb, var(--crew-cards-role) 18%, var(--surface-light)), transparent 72%),
    color-mix(in srgb, var(--crew-cards-role) 6%, var(--surface-muted));
}
.crew-cards__shape-bg {
  position: absolute; left: 24%; top: 10%; width: 62%; aspect-ratio: 1;
  border-radius: 62% 38% 46% 54% / 50% 58% 42% 50%;
  background: linear-gradient(140deg, var(--crew-cards-role), color-mix(in srgb, var(--crew-cards-role) 28%, var(--surface-light)));
  box-shadow: 0 20px 40px -18px var(--crew-cards-role);
  transform: rotate(-12deg);
  transition: transform var(--dur-5) var(--ease-spring), border-radius var(--dur-5) var(--ease-spring);
}
.crew-cards__photo {
  position: relative; width: 72%; aspect-ratio: 1; margin: auto auto 6%; overflow: hidden;
  border-radius: 58% 42% 46% 54% / 46% 52% 48% 54%; /* blob fallback where CSS d isn't supported */
  background: color-mix(in srgb, var(--crew-cards-role) 22%, var(--surface-light));
  transition: border-radius var(--dur-5) var(--ease-spring);
}
.crew-cards__photo img { display: block; width: 100%; height: 100%; object-fit: cover; transition: transform var(--dur-5) var(--ease-out); }
.crew-cards__defs { position: absolute; width: 0; height: 0; }
@supports (d: path("M0 0")) {
  .crew-cards__photo { border-radius: 0; clip-path: var(--crew-cards-clip); }
  .crew-cards__blob { transition: d var(--dur-5) var(--ease-spring); }
}
@media (prefers-reduced-motion: no-preference) {
  .crew-cards__card:is(:hover, :focus-within) .crew-cards__shape-bg { transform: rotate(16deg) scale(1.08); border-radius: 44% 56% 58% 42% / 58% 42% 58% 42%; }
  .crew-cards__card:is(:hover, :focus-within) .crew-cards__blob { d: var(--crew-cards-morph); }
  .crew-cards__card:is(:hover, :focus-within) .crew-cards__photo img { transform: scale(1.06); }
}
@supports not (d: path("M0 0")) {
  @media (prefers-reduced-motion: no-preference) {
    .crew-cards__card:is(:hover, :focus-within) .crew-cards__photo { border-radius: 42% 58% 60% 40% / 56% 44% 56% 44%; }
  }
}
.crew-cards__status {
  position: absolute; top: 0.75rem; left: 0.75rem; display: inline-flex; align-items: center; gap: 0.375rem; margin: 0;
  padding: 0.3125rem 0.625rem; border-radius: var(--radius-full); font-size: 0.75rem; font-weight: 600;
  background: color-mix(in srgb, var(--surface-light) 90%, transparent); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
}
@supports (backdrop-filter: blur(1px)) {
  .crew-cards__status { background: var(--glass); backdrop-filter: blur(var(--blur-md)) saturate(1.4); }
}
.crew-cards__dot { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 20%, transparent); }

/* Body */
.crew-cards__body { padding: 1rem 0.5rem 0; }
.crew-cards__name { margin: 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.crew-cards__role { display: flex; align-items: center; gap: 0.5rem; margin: 0.375rem 0 0; color: var(--text-muted); font-size: 0.875rem; }
.crew-cards__role::before { content: ""; flex: none; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--crew-cards-role); }
.crew-cards__chips { display: flex; flex-wrap: wrap; gap: 0.375rem; margin: 0.875rem 0 0; padding: 0; list-style: none; }
.crew-cards__chips li {
  padding: 0.25rem 0.625rem; border-radius: var(--radius-full); font-size: 0.75rem; font-weight: 600;
  background: color-mix(in srgb, var(--crew-cards-role) 10%, var(--surface-light));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--crew-cards-role) 24%, transparent);
}
.crew-cards__jobs { display: flex; align-items: flex-end; /* digit cells clip, so align edges, not baselines */ gap: 0.5rem; margin: 1rem 0 0; padding-top: 0.875rem; border-top: 1px dashed var(--border-subtle); color: var(--text-muted); font-size: 0.8125rem; }
.crew-cards__count { color: var(--text-main); font: 600 1.5rem/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }

/* Odometer (built by JS): each digit is a 0–9 strip, twice round, parked on its digit */
.crew-cards__odo { display: inline-flex; letter-spacing: 0; }
.crew-cards__digit { display: inline-block; height: 1em; overflow: hidden; }
.crew-cards__strip { display: block; transform: translateY(calc((10 + var(--crew-cards-d, 0)) * -1em)); }
.crew-cards__strip > span { display: block; height: 1em; }
.crew-cards__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
@media (prefers-reduced-motion: no-preference) {
  .crew-cards__card:is(:hover, :focus-within) .crew-cards__strip { animation: crew-cards-roll calc(var(--dur-5) * 1.4) var(--ease-out) calc(var(--crew-cards-c, 0) * 70ms) both; }
}

/* Dock: always visible; on hover-capable screens it rests low and quiet, then slides up into colour */
.crew-cards__dock { display: flex; align-items: center; gap: 0.5rem; margin-top: auto; padding: 1.125rem 0.25rem 0.25rem; }
.crew-cards__request {
  flex: 1; display: inline-flex; align-items: center; justify-content: center; gap: 0.375rem; min-height: 2.75rem; padding: 0 0.875rem;
  border-radius: var(--radius-full); background: var(--crew-cards-ink); color: var(--text-inverse); white-space: nowrap;
  box-shadow: inset 0 0 0 1.5px var(--crew-cards-ink), var(--highlight-inverse), 0 10px 20px -12px var(--crew-cards-ink);
  font-size: 0.875rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-4) var(--ease-spring), background-color var(--dur-3), color var(--dur-3), box-shadow var(--dur-3);
}
.crew-cards__socials { display: flex; gap: 0.375rem; margin: 0; padding: 0; list-style: none; }
.crew-cards__socials li { transition: transform var(--dur-4) var(--ease-spring); }
.crew-cards__socials li:nth-child(2) { transition-delay: var(--stagger); }
.crew-cards__socials a {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: 50%;
  background: var(--surface-muted); color: var(--text-muted); box-shadow: inset 0 0 0 1px var(--border-subtle);
  transition: background-color var(--dur-2), color var(--dur-2);
}
.crew-cards__socials a:hover { background: color-mix(in srgb, var(--crew-cards-role) 12%, var(--surface-light)); color: var(--crew-cards-ink); }
@media (hover: hover) {
  .crew-cards__request, .crew-cards__socials li { transform: translateY(0.625rem); }
  .crew-cards__request { background: transparent; color: var(--crew-cards-ink); box-shadow: inset 0 0 0 1.5px color-mix(in srgb, var(--crew-cards-ink) 35%, transparent); }
  .crew-cards__card:is(:hover, :focus-within) :is(.crew-cards__request, .crew-cards__socials li) { transform: none; }
  .crew-cards__card:is(:hover, :focus-within) .crew-cards__request {
    background: var(--crew-cards-ink); color: var(--text-inverse);
    box-shadow: inset 0 0 0 1.5px var(--crew-cards-ink), var(--highlight-inverse), 0 10px 20px -12px var(--crew-cards-ink);
  }
}
.crew-cards__card .crew-cards__request:active { transform: scale(0.97); }
.crew-cards a:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

@media (min-width: 768px) {
  .crew-cards__list { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; margin: 0; padding: 0; overflow: visible; -webkit-mask: none; mask: none; }
}
@media (min-width: 1024px) {
  .crew-cards__list { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1.25rem; }
}
@media (prefers-reduced-motion: reduce) {
  .crew-cards *, .crew-cards *::before, .crew-cards *::after { animation: none !important; }
  .crew-cards__card { transform: none; }
}
@keyframes crew-cards-roll { from { transform: translateY(0); } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
let uid = 0;

document.querySelectorAll('[data-crew-cards]').forEach((root) => {
  root.querySelectorAll('.crew-cards__card').forEach((card) => {
    // Page-unique clipPath ids, so several crews can share a page
    const clip = card.querySelector('clipPath');
    clip.id = `crew-cards-clip-${++uid}`;
    card.style.setProperty('--crew-cards-clip', `url(#${clip.id})`);

    // Odometer: each digit becomes a 0–9 strip (twice round) that spins up on hover or focus;
    // the real number stays in visually hidden text
    const count = card.querySelector('.crew-cards__count');
    const value = count.textContent.trim();
    const odo = document.createElement('span');
    odo.className = 'crew-cards__odo';
    odo.setAttribute('aria-hidden', 'true');
    let column = 0;
    for (const char of value) {
      const cell = document.createElement('span');
      if (/\d/.test(char)) {
        cell.className = 'crew-cards__digit';
        cell.style.cssText = `--crew-cards-d: ${char}; --crew-cards-c: ${column++}`;
        cell.innerHTML = `<span class="crew-cards__strip">${'01234567890123456789'.replace(/\d/g, '<span>$&</span>')}</span>`;
      } else {
        cell.textContent = char;
      }
      odo.append(cell);
    }
    const label = document.createElement('span');
    label.className = 'crew-cards__sr';
    label.textContent = value;
    count.replaceChildren(label, odo);

    // Tilt toward a mouse pointer, one update per frame
    let frame = 0;
    let point = null;
    card.addEventListener('pointermove', (e) => {
      if (e.pointerType !== 'mouse' || reduce.matches) return;
      point = e;
      frame ||= requestAnimationFrame(() => {
        frame = 0;
        const r = card.getBoundingClientRect();
        const x = (point.clientX - r.left) / r.width;
        const y = (point.clientY - r.top) / r.height;
        card.style.setProperty('--crew-cards-ry', `${(x - 0.5) * 10}deg`);
        card.style.setProperty('--crew-cards-rx', `${(0.5 - y) * 8}deg`);
        card.style.setProperty('--crew-cards-mx', `${x * 100}%`);
        card.style.setProperty('--crew-cards-my', `${y * 100}%`);
      });
    }, { passive: true });
    card.addEventListener('pointerleave', () => {
      cancelAnimationFrame(frame);
      frame = 0;
      card.style.removeProperty('--crew-cards-rx');
      card.style.removeProperty('--crew-cards-ry');
    });
  });
});
```

## Notes

- Each card is an `<article>` labelled by the technician's name, with the certifications as a labelled list. The roll-up count keeps the real number in visually hidden text, and the spinning digit strips are `aria-hidden`. The request link and socials are always visible and reachable, never hidden. On hover or keyboard focus they slide up and fill with the role colour, and on touch screens they rest in that raised state.
- The morph is an SVG `clipPath` whose path changes through a CSS `d: path()` transition (Chromium, Firefox). Where `@supports (d: path(...))` fails (Safari at the time of writing), the portrait falls back to a `border-radius` blob that morphs the same way. JS gives every clipPath a page-unique id, so several crews can share a page. Without JS the portraits are still blob-clipped, the count is plain text and nothing tilts.
- Reduced motion: no morph, no tilt and no digit roll. Hover and focus only change colour, and the dock's small shift is instant.
- Phones get a full-bleed scroll-snap row with faded edges and the next card peeking in; tabbing to a card's links scrolls it into view. From 768px it's a two-column grid, and from 1024px four columns.
- Contrast: the request button uses `--crew-cards-ink` (the role colour mixed 55% with `--text-main`), so its white text is at least 4.6:1 for all four roles, including amber, and the outlined rest state is 4.8:1 on white. Chips are `--text-main` on a 10% role tint (12.6:1 or better).
- To adapt it, set the role colour with one custom property per modifier (`--crew-cards-role`). New blob shapes go in `--crew-cards-morph` and the clipPath `d`, keeping the same `M` + four `C` + `Z` structure so the two can interpolate. Portraits are ordinary lazy-loaded `<img>`s with `width`/`height`.
