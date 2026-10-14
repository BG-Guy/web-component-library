# Photo Drop Upload

A "show us the problem" photo uploader for a booking flow. The drop zone is the label of a real file input, and a stack of three photo cards sits in it. Drag files over the zone and the cards fan out, the border turns into marching ants and the zone leans forward. Each photo lands as a row with a dimmed thumbnail and a progress ring that fills, then a green check badge springs on. Removed rows slide away and the rows below close the gap. On touch screens the copy changes to "Add photos" (the picker offers the camera), and rows keep the name readable by putting the progress ring on the thumbnail. Depends on `tokens/variables.css`.

**Motion:** card fan on hover/drag (`--dur-4`, `--ease-spring`, half-`--stagger` offsets) · marching-ants border (0.6s linear loop, only while dragging) · zone lean (`scale`, `--ease-spring`) · title crossfade (`--dur-3`) · rows drop in (`--dur-4`, `--ease-out`, `--stagger`) · thumbnail pop · progress ring (`--dur-3`, `--ease-out`) · check badge spring + tick draw · remove: slide-out (`--dur-2`) then FLIP close-up (`--dur-4`, `--ease-spring`).

## HTML

```html
<div class="file-drop-demo">
  <section class="file-drop is-ready" aria-labelledby="file-drop-heading" data-file-drop>
    <p class="file-drop__eyebrow">Step 2 of 3 · Photos</p>
    <h2 id="file-drop-heading" class="file-drop__heading">Show us the problem</h2>
    <p class="file-drop__lead">A few clear photos of the leak, damage or part help us quote accurately and bring the right parts on the first visit.</p>

    <label class="file-drop__zone">
      <svg class="file-drop__ants" aria-hidden="true" focusable="false"><rect width="100%" height="100%" rx="23" /></svg>
      <span class="file-drop__stack" aria-hidden="true">
        <span class="file-drop__photo file-drop__photo--a">
          <span class="file-drop__art"><svg viewBox="0 0 24 24" width="26" height="26" focusable="false"><path d="M2 8h8a4 4 0 0 1 4 4v10" /><path d="M18.5 12s-2 2.3-2 3.7a2 2 0 0 0 4 0c0-1.4-2-3.7-2-3.7z" /></svg></span>
        </span>
        <span class="file-drop__photo file-drop__photo--b">
          <span class="file-drop__art"><svg viewBox="0 0 24 24" width="26" height="26" focusable="false"><path d="M3 11 12 4l9 7M5.5 9.5V20h13V9.5M10 20v-5h4v5" /></svg></span>
        </span>
        <span class="file-drop__photo file-drop__photo--c">
          <span class="file-drop__art"><svg viewBox="0 0 24 24" width="26" height="26" focusable="false"><rect x="3" y="4" width="18" height="16" rx="2.5" /><path d="m3 16 5-5 4 4 2.5-2.5L21 19M15.5 8.5h.01" /></svg></span>
          <span class="file-drop__plus"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M12 5v14M5 12h14" /></svg></span>
        </span>
      </span>
      <span class="file-drop__cta" id="file-drop-cta">
        <span class="file-drop__says">
          <span class="file-drop__say file-drop__say--idle"><span class="file-drop__fine">Drop photos here</span><span class="file-drop__coarse">Add photos</span></span>
          <span class="file-drop__say file-drop__say--drag" aria-hidden="true">Release to add them</span>
        </span>
        <span class="file-drop__sub"><span class="file-drop__fine">or <span class="file-drop__browse">browse your files</span></span><span class="file-drop__coarse">Take one now or <span class="file-drop__browse">pick from your library</span></span></span>
      </span>
      <span class="file-drop__hint" id="file-drop-hint">JPG, PNG or HEIC · up to 8 photos, 10 MB each</span>
      <input class="file-drop__input" type="file" name="photos" multiple accept="image/*" aria-labelledby="file-drop-cta" aria-describedby="file-drop-hint">
    </label>

    <ul class="file-drop__list" role="list" aria-label="Photos to send">
      <li class="file-drop__item is-done" data-size="2400000">
        <span class="file-drop__thumb">
          <span class="file-drop__frame">
            <img src="under-sink-leak.jpg" alt="" width="52" height="52">
            <svg class="file-drop__fallback" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><rect x="3" y="4" width="18" height="16" rx="2.5" /><path d="m3 16 5-5 4 4 2.5-2.5L21 19" /></svg>
          </span>
          <span class="file-drop__badge" aria-hidden="true"><svg viewBox="0 0 24 24" width="12" height="12" focusable="false"><path d="m5.5 12.5 4 4 9-9" pathLength="1" /></svg></span>
        </span>
        <span class="file-drop__meta">
          <span class="file-drop__name">under-sink-leak.jpg</span>
          <span class="file-drop__info"><span class="file-drop__size">2.4 MB</span><span class="file-drop__dot" aria-hidden="true">·</span><span class="file-drop__state">Uploaded</span></span>
        </span>
        <button class="file-drop__remove" type="button" aria-label="Remove under-sink-leak.jpg">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
        </button>
        <input type="hidden" name="keep" value="ph_2041">
      </li>
      <li class="file-drop__item is-done" data-size="1800000">
        <span class="file-drop__thumb">
          <span class="file-drop__frame">
            <img src="cabinet-damage.jpg" alt="" width="52" height="52">
            <svg class="file-drop__fallback" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><rect x="3" y="4" width="18" height="16" rx="2.5" /><path d="m3 16 5-5 4 4 2.5-2.5L21 19" /></svg>
          </span>
          <span class="file-drop__badge" aria-hidden="true"><svg viewBox="0 0 24 24" width="12" height="12" focusable="false"><path d="m5.5 12.5 4 4 9-9" pathLength="1" /></svg></span>
        </span>
        <span class="file-drop__meta">
          <span class="file-drop__name">cabinet-damage.jpg</span>
          <span class="file-drop__info"><span class="file-drop__size">1.8 MB</span><span class="file-drop__dot" aria-hidden="true">·</span><span class="file-drop__state">Uploaded</span></span>
        </span>
        <button class="file-drop__remove" type="button" aria-label="Remove cabinet-damage.jpg">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
        </button>
        <input type="hidden" name="keep" value="ph_2042">
      </li>
    </ul>

    <div class="file-drop__summary">
      <svg class="file-drop__ok" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="10" /><path d="m8 12.5 3 3 5-6" /></svg>
      <p class="file-drop__status" role="status">2 photos ready</p>
      <span class="file-drop__total">4.2 MB</span>
    </div>
    <p class="file-drop__privacy">
      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><rect x="5" y="11" width="14" height="10" rx="2" /><path d="M8 11V8a4 4 0 0 1 8 0v3" /></svg>
      Only your Brand technician sees these photos.
    </p>

    <template class="file-drop__template">
      <li class="file-drop__item is-new">
        <span class="file-drop__thumb">
          <span class="file-drop__frame">
            <img alt="" width="52" height="52" decoding="async">
            <svg class="file-drop__fallback" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><rect x="3" y="4" width="18" height="16" rx="2.5" /><path d="m3 16 5-5 4 4 2.5-2.5L21 19" /></svg>
          </span>
          <span class="file-drop__ring" aria-hidden="true"><svg viewBox="0 0 24 24" width="26" height="26" focusable="false"><circle class="file-drop__ring-track" cx="12" cy="12" r="9" /><path class="file-drop__ring-bar" d="M12 3a9 9 0 1 1 0 18a9 9 0 1 1 0-18" pathLength="1" /></svg></span>
          <span class="file-drop__badge" aria-hidden="true"><svg viewBox="0 0 24 24" width="12" height="12" focusable="false"><path d="m5.5 12.5 4 4 9-9" pathLength="1" /></svg></span>
        </span>
        <span class="file-drop__meta">
          <span class="file-drop__name"></span>
          <span class="file-drop__info"><span class="file-drop__size"></span><span class="file-drop__dot" aria-hidden="true">·</span><span class="file-drop__state">Queued</span></span>
        </span>
        <button class="file-drop__remove" type="button" aria-label="Remove photo">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
        </button>
      </li>
    </template>
  </section>
</div>
```

## CSS

```css
/* Demo backdrop */
.file-drop-demo {
  display: grid; place-items: center; min-height: 40rem; padding: 3rem var(--gutter);
  background:
    radial-gradient(55% 45% at 10% 0%, color-mix(in srgb, var(--primary-2) 10%, transparent), transparent 70%),
    radial-gradient(50% 45% at 100% 100%, color-mix(in srgb, var(--primary) 9%, transparent), transparent 70%),
    var(--surface-muted);
}

/* Card */
.file-drop {
  width: min(100%, 36rem); padding: clamp(1.25rem, 0.75rem + 2.5vw, 2rem);
  border-radius: var(--radius-2xl); background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl);
}
.file-drop__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.file-drop__heading { margin: 0.5rem 0 0; font: 600 clamp(1.5rem, 1.2rem + 1.2vw, 1.875rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.file-drop__lead { max-width: 32rem; margin: 0.625rem 0 0; color: var(--text-muted); line-height: 1.55; text-wrap: pretty; }

/* Drop zone: the label of the real file input */
.file-drop__zone {
  position: relative; isolation: isolate; display: grid; justify-items: center; margin-top: 1.5rem;
  padding: 1.75rem 1rem 1.5rem; border-radius: var(--radius-2xl); cursor: pointer; text-align: center;
  background: radial-gradient(80% 70% at 50% 0%, color-mix(in srgb, var(--primary) 6%, transparent), transparent 70%), var(--surface-muted);
  transition: scale var(--dur-4) var(--ease-spring);
}
.file-drop__zone::before {
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; opacity: 0; pointer-events: none;
  background:
    radial-gradient(45% 55% at 50% 30%, color-mix(in srgb, var(--primary) 14%, transparent), transparent 70%),
    color-mix(in srgb, var(--primary) 4%, var(--surface-light));
  transition: opacity var(--dur-3) var(--ease-out);
}
.file-drop__zone.is-dragging::before { opacity: 1; }
.file-drop__zone:has(.file-drop__input:focus-visible) { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Dashed border drawn in SVG so the dashes follow the corners and can march */
.file-drop__ants { position: absolute; top: 1px; left: 1px; width: calc(100% - 2px); height: calc(100% - 2px); overflow: visible; pointer-events: none; }
.file-drop__ants rect {
  rx: calc(var(--radius-2xl) - 1px); fill: none; stroke: color-mix(in srgb, var(--text-muted) 45%, transparent);
  stroke-width: 1.5; stroke-dasharray: 8 6; transition: stroke var(--dur-3) var(--ease-out);
}
.file-drop__zone:hover .file-drop__ants rect { stroke: color-mix(in srgb, var(--primary) 55%, transparent); }
.file-drop__zone.is-dragging .file-drop__ants rect { stroke: var(--primary); }

/* Photo-card stack */
.file-drop__stack { position: relative; width: 11rem; height: 6.5rem; margin-bottom: 1.25rem; }
.file-drop__photo {
  position: absolute; bottom: 0; left: calc(50% - 2.25rem); display: grid; width: 4.5rem; aspect-ratio: 4 / 5;
  padding: 0.3125rem 0.3125rem 0.875rem; border-radius: 0.625rem; background: var(--surface-light);
  box-shadow: 0 12px 24px -12px color-mix(in srgb, var(--surface-deep) 40%, transparent), inset 0 0 0 1px var(--border-subtle);
  transform: translate(var(--file-drop-x, 0), var(--file-drop-y, 0)) rotate(var(--file-drop-r, 0deg)) scale(var(--file-drop-s, 1));
  transition: transform var(--dur-4) var(--ease-spring);
}
.file-drop__photo--a { --file-drop-x: -1.5rem; --file-drop-y: -0.25rem; --file-drop-r: -9deg; }
.file-drop__photo--b { --file-drop-x: 1.5rem; --file-drop-y: -0.375rem; --file-drop-r: 8deg; transition-delay: calc(var(--stagger) / 2); }
.file-drop__photo--c { --file-drop-r: -2deg; transition-delay: var(--stagger); }
.file-drop__art { display: grid; place-items: center; border-radius: 0.375rem; color: var(--text-inverse); }
.file-drop__art svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.file-drop__photo--a .file-drop__art {
  background: radial-gradient(circle at 75% 20%, color-mix(in srgb, var(--surface-light) 30%, transparent), transparent 50%),
    linear-gradient(160deg, var(--primary-2), color-mix(in srgb, var(--primary-2) 55%, var(--surface-deep)));
}
.file-drop__photo--b .file-drop__art { background: linear-gradient(160deg, var(--accent), var(--warning)); }
.file-drop__photo--c .file-drop__art {
  background: radial-gradient(circle at 30% 20%, color-mix(in srgb, var(--surface-light) 30%, transparent), transparent 55%), var(--gradient-brand);
}
.file-drop__plus {
  position: absolute; top: -0.5rem; right: -0.5rem; display: grid; place-items: center; width: 1.5rem; height: 1.5rem; border-radius: 50%;
  background: var(--primary); color: var(--text-inverse);
  box-shadow: 0 0 0 3px var(--surface-light), 0 6px 14px -4px color-mix(in srgb, var(--primary) 70%, transparent);
  scale: 0; transition: scale var(--dur-4) var(--ease-spring);
}
.file-drop__plus svg { fill: none; stroke: currentColor; stroke-width: 2.5; stroke-linecap: round; }
.file-drop__zone.is-dragging .file-drop__plus { scale: 1; }

/* Fan on hover (a little) and on drag (fully); none under reduced motion */
@media (prefers-reduced-motion: no-preference) and (hover: hover) {
  .file-drop__zone:hover .file-drop__photo--a { --file-drop-x: -2.125rem; --file-drop-r: -13deg; }
  .file-drop__zone:hover .file-drop__photo--b { --file-drop-x: 2.125rem; --file-drop-r: 12deg; }
  .file-drop__zone:hover .file-drop__photo--c { --file-drop-y: -0.25rem; }
}
@media (prefers-reduced-motion: no-preference) {
  .file-drop__zone.is-dragging { scale: 1.015; }
  .file-drop__zone.is-dragging .file-drop__ants rect { animation: file-drop-march 0.6s linear infinite; }
  .file-drop__zone.is-dragging .file-drop__photo--a { --file-drop-x: -3.5rem; --file-drop-y: -0.5rem; --file-drop-r: -19deg; }
  .file-drop__zone.is-dragging .file-drop__photo--b { --file-drop-x: 3.5rem; --file-drop-y: -0.625rem; --file-drop-r: 18deg; }
  .file-drop__zone.is-dragging .file-drop__photo--c { --file-drop-y: -0.875rem; --file-drop-r: 0deg; --file-drop-s: 1.08; }
}

/* Copy: the title crossfades while dragging; touch screens get their own wording */
.file-drop__cta { display: grid; gap: 0.25rem; }
.file-drop__says { display: grid; font: 600 1.125rem/1.3 var(--font-display); letter-spacing: var(--tracking-tight); }
.file-drop__say { grid-area: 1 / 1; transition: opacity var(--dur-3) var(--ease-out), translate var(--dur-3) var(--ease-out); }
.file-drop__say--drag { opacity: 0; translate: 0 0.5rem; color: var(--primary); }
.file-drop__zone.is-dragging .file-drop__say--idle { opacity: 0; translate: 0 -0.5rem; }
.file-drop__zone.is-dragging .file-drop__say--drag { opacity: 1; translate: 0 0; }
.file-drop__sub { color: var(--text-muted); font-size: 0.9375rem; }
.file-drop__browse { color: var(--primary); font-weight: 600; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 3px; }
.file-drop__hint { margin-top: 0.875rem; color: var(--text-muted); font: 500 0.75rem/1.4 var(--font-mono); }
.file-drop__coarse { display: none; }
@media (hover: none) and (pointer: coarse) {
  .file-drop__fine { display: none; }
  .file-drop__coarse { display: inline; }
}

/* The input: a styled native picker without JS, visually hidden (still focusable) with JS */
.file-drop__input { max-width: 100%; margin-top: 1rem; color: var(--text-muted); font: 500 0.8125rem var(--font-sans); }
.file-drop__input::file-selector-button {
  margin-right: 0.75rem; padding: 0.5rem 1rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--text-main); color: var(--surface-light); font: 600 0.8125rem var(--font-sans);
}
.file-drop--js .file-drop__input {
  position: absolute; width: 1px; height: 1px; margin: -1px; padding: 0; border: 0;
  overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap;
}

/* File rows */
.file-drop__list { display: grid; gap: 0.5rem; margin: 1rem 0 0; padding: 0; list-style: none; }
.file-drop__list:not(:has(> .file-drop__item)) { margin-top: 0; }
.file-drop__item {
  display: grid; grid-template-columns: auto minmax(0, 1fr) auto; align-items: center; gap: 0.75rem;
  padding: 0.5rem 0.5rem 0.5rem 0.625rem; border-radius: var(--radius-xl); background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
}
.file-drop__item.is-new { animation: file-drop-in var(--dur-4) var(--ease-out) calc(var(--file-drop-i, 0) * var(--stagger)) both; }
.file-drop__thumb { position: relative; width: 3.25rem; height: 3.25rem; }
.file-drop__frame {
  display: grid; place-items: center; width: 100%; height: 100%; overflow: hidden; border-radius: 0.875rem;
  background: var(--surface-muted); color: var(--text-muted); box-shadow: inset 0 0 0 1px var(--border-subtle);
}
.file-drop__frame img { grid-area: 1 / 1; width: 100%; height: 100%; object-fit: cover; filter: saturate(0.4) brightness(0.92); transition: filter var(--dur-4) var(--ease-out); }
.file-drop__item.is-new .file-drop__frame img { animation: file-drop-pop var(--dur-4) var(--ease-spring) calc((var(--file-drop-i, 0) + 2) * var(--stagger)) both; }
.file-drop__item.is-done .file-drop__frame img { filter: none; }
.file-drop__fallback { grid-area: 1 / 1; display: none; fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.file-drop__item.is-broken .file-drop__frame img { display: none; }
.file-drop__item.is-broken .file-drop__fallback { display: block; }

/* Progress ring over the thumbnail, then a check badge on its corner */
.file-drop__ring {
  position: absolute; inset: 0; display: grid; place-items: center; border-radius: 0.875rem;
  background: color-mix(in srgb, var(--surface-deep) 45%, transparent); color: var(--text-inverse);
  transition: opacity var(--dur-3) var(--ease-out);
}
.file-drop__ring-track, .file-drop__ring-bar { fill: none; stroke: currentColor; stroke-width: 2.5; }
.file-drop__ring-track { opacity: 0.3; }
.file-drop__ring-bar { stroke-linecap: round; stroke-dasharray: 1; stroke-dashoffset: calc(1 - var(--file-drop-p, 0)); transition: stroke-dashoffset var(--dur-3) var(--ease-out); }
.file-drop__item.is-done .file-drop__ring { opacity: 0; }
.file-drop__badge {
  position: absolute; right: -0.375rem; bottom: -0.375rem; display: grid; place-items: center; width: 1.375rem; height: 1.375rem; border-radius: 50%;
  background: var(--success); color: var(--text-inverse); box-shadow: 0 0 0 2px var(--surface-light);
  scale: 0; transition: scale var(--dur-4) var(--ease-spring);
}
.file-drop__badge path { fill: none; stroke: currentColor; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 1; stroke-dashoffset: 1; transition: stroke-dashoffset var(--dur-3) var(--ease-out); }
.file-drop__item.is-done .file-drop__badge { scale: 1; }
.file-drop__item.is-done .file-drop__badge path { stroke-dashoffset: 0; transition-delay: calc(var(--stagger) * 3); }

.file-drop__meta { display: grid; gap: 0.125rem; min-width: 0; }
.file-drop__name { overflow: hidden; font-size: 0.9375rem; font-weight: 600; white-space: nowrap; text-overflow: ellipsis; }
.file-drop__info { color: var(--text-muted); font: 500 0.75rem/1.4 var(--font-mono); font-variant-numeric: tabular-nums; }
.file-drop__dot { margin-inline: 0.375rem; }
.file-drop__item.is-done .file-drop__state { color: var(--success); }
.file-drop__remove {
  display: grid; place-items: center; width: 2.25rem; height: 2.25rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: transparent; color: var(--text-muted);
  transition: background-color var(--dur-2) var(--ease-out), color var(--dur-2) var(--ease-out), transform var(--dur-3) var(--ease-spring);
}
.file-drop__remove:hover { background: color-mix(in srgb, var(--danger) 10%, transparent); color: var(--danger); }
.file-drop__remove:active { transform: scale(0.9); }
.file-drop__remove:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.file-drop__remove svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; }
.file-drop:not(.file-drop--js) .file-drop__remove { display: none; }

/* Summary and footnote */
.file-drop__summary { display: flex; align-items: center; gap: 0.5rem; margin-top: 1rem; }
.file-drop__ok { display: none; flex: none; }
.file-drop__ok circle { fill: var(--success); }
.file-drop__ok path { fill: none; stroke: var(--text-inverse); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
.file-drop.is-ready .file-drop__ok { display: block; animation: file-drop-pop var(--dur-4) var(--ease-spring) both; }
.file-drop__status { flex: 1; margin: 0; font-size: 0.9375rem; font-weight: 600; }
.file-drop__total { color: var(--text-muted); font: 500 0.8125rem var(--font-mono); font-variant-numeric: tabular-nums; }
.file-drop__privacy {
  display: flex; align-items: center; gap: 0.5rem; margin: 1.25rem 0 0; padding-top: 1rem;
  border-top: 1px solid var(--border-subtle); color: var(--text-muted); font-size: 0.8125rem;
}
.file-drop__privacy svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

@media (min-width: 768px) {
  .file-drop__zone { padding: 2.25rem 2rem 2rem; }
}
@media (prefers-reduced-motion: reduce) {
  .file-drop *, .file-drop *::before, .file-drop *::after { animation: none !important; }
}
@keyframes file-drop-march { to { stroke-dashoffset: -14; } }
@keyframes file-drop-in { from { opacity: 0; transform: translateY(-0.75rem) scale(0.97); filter: blur(4px); } }
@keyframes file-drop-pop { from { opacity: 0; transform: scale(0.6); } }
```

## JS

```js
const fmt = (bytes) => (bytes < 1e6 ? `${Math.max(1, Math.round(bytes / 1e3))} KB` : `${(bytes / 1e6).toFixed(1)} MB`);
const plural = (n) => `${n} photo${n === 1 ? '' : 's'}`;
const MAX_FILES = 8;
const MAX_BYTES = 10e6;

document.querySelectorAll('[data-file-drop]').forEach((root) => {
  const $ = (part, el = root) => el.querySelector(`.file-drop__${part}`);
  const [zone, input, list, status, total, template] = ['zone', 'input', 'list', 'status', 'total', 'template'].map((p) => $(p));
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const token = (name) => getComputedStyle(root).getPropertyValue(name).trim();
  // Rows already in the HTML are photos attached earlier (sent back as hidden "keep" inputs)
  const items = [...list.children].map((el) => ({ el, name: $('name', el).textContent, size: Number(el.dataset.size) || 0, done: true }));
  let depth = 0;
  root.classList.add('file-drop--js');

  const watchImage = (img) => {
    const broken = () => img.closest('.file-drop__item').classList.add('is-broken');
    if (img.complete && !img.naturalWidth) broken();
    else img.addEventListener('error', broken, { once: true });
  };
  list.querySelectorAll('img').forEach(watchImage);

  const summarize = (note = '') => {
    const pending = items.filter((it) => !it.done).length;
    const line = !items.length ? '' : pending ? `Uploading ${plural(pending)}…` : `${plural(items.length)} ready`;
    const text = `${note} ${line}`.trim();
    if (status.textContent !== text) status.textContent = text;
    total.textContent = items.length ? fmt(items.reduce((sum, it) => sum + it.size, 0)) : '';
    root.classList.toggle('is-ready', items.length > 0 && !pending);
  };

  // Mirror the list into the real input, so a plain form submit sends exactly these files
  const sync = () => {
    try {
      const dt = new DataTransfer();
      items.forEach((it) => it.file && dt.items.add(it.file));
      input.files = dt.files;
    } catch { /* no DataTransfer constructor: rely on upload() */ }
  };

  // Simulated upload. Swap for fetch/XHR and feed real progress (0–1) into setProgress()
  const setProgress = (item, p) => {
    item.el.style.setProperty('--file-drop-p', p.toFixed(3));
    $('state', item.el).textContent = p < 1 ? `${Math.round(p * 100)}%` : 'Uploaded';
    if (p < 1) return;
    item.done = true;
    item.el.classList.add('is-done');
    summarize();
  };
  const upload = (item, p = 0) => {
    item.timer = setTimeout(() => {
      p = Math.min(1, p + 0.06 + Math.random() * 0.18);
      setProgress(item, p);
      if (p < 1) upload(item, p);
    }, 160 + Math.random() * 260);
  };

  const add = (files) => {
    const skipped = [];
    let batch = 0;
    for (const file of files) {
      const key = `${file.name}:${file.size}:${file.lastModified}`;
      if (items.some((it) => it.key === key)) continue;
      const why = !file.type.startsWith('image/') ? 'not a photo' : file.size > MAX_BYTES ? 'over 10 MB' : items.length >= MAX_FILES ? `${MAX_FILES}-photo limit` : '';
      if (why) { skipped.push(`${file.name} (${why})`); continue; }
      const el = template.content.firstElementChild.cloneNode(true);
      const item = { el, key, file, name: file.name, size: file.size, done: false, url: URL.createObjectURL(file) };
      const img = el.querySelector('img');
      img.src = item.url;
      watchImage(img);
      $('name', el).textContent = file.name;
      $('size', el).textContent = fmt(file.size);
      $('remove', el).setAttribute('aria-label', `Remove ${file.name}`);
      el.style.setProperty('--file-drop-i', batch++);
      items.push(item);
      list.append(el);
      upload(item);
    }
    sync();
    summarize(skipped.length ? `Skipped ${skipped.join(', ')}.` : '');
  };

  const remove = (item) => {
    if (!item || item.leaving) return;
    item.leaving = true;
    clearTimeout(item.timer);
    if (item.url) URL.revokeObjectURL(item.url);
    const index = items.indexOf(item);
    items.splice(index, 1);
    sync();
    summarize(`Removed ${item.name}.`);
    // Focus moves to the next row's remove button, else the previous one, else the input
    const next = items[index] || items[index - 1];
    (next ? $('remove', next.el) : input).focus();
    // Exit, then slide the rows below up into the gap (FLIP)
    const close = () => {
      const rest = items.map((it) => it.el);
      const before = rest.map((el) => el.getBoundingClientRect().top);
      item.el.remove();
      if (reduce.matches) return;
      rest.forEach((el, n) => {
        const dy = before[n] - el.getBoundingClientRect().top;
        if (dy) el.animate([{ transform: `translateY(${dy}px)` }, { transform: 'none' }], { duration: parseFloat(token('--dur-4')), easing: token('--ease-spring') });
      });
    };
    if (reduce.matches) return close();
    item.el.animate([{ opacity: 1, transform: 'none' }, { opacity: 0, transform: 'translateX(1.5rem) scale(0.96)' }],
      { duration: parseFloat(token('--dur-2')), easing: token('--ease-out'), fill: 'forwards' }).finished.then(close);
  };

  // Drag state: count enter/leave pairs so moving over the cards doesn't flicker
  const hasFiles = (e) => [...(e.dataTransfer?.types || [])].includes('Files');
  zone.addEventListener('dragenter', (e) => {
    if (!hasFiles(e)) return;
    e.preventDefault();
    depth += 1;
    zone.classList.add('is-dragging');
  });
  zone.addEventListener('dragover', (e) => {
    if (!hasFiles(e)) return;
    e.preventDefault();
    e.dataTransfer.dropEffect = 'copy';
  });
  zone.addEventListener('dragleave', () => {
    depth = Math.max(0, depth - 1);
    if (!depth) zone.classList.remove('is-dragging');
  });
  zone.addEventListener('drop', (e) => {
    e.preventDefault();
    depth = 0;
    zone.classList.remove('is-dragging');
    add(e.dataTransfer.files);
  });
  input.addEventListener('change', () => add(input.files));
  list.addEventListener('click', (e) => {
    const button = e.target.closest('.file-drop__remove');
    if (button) remove(items.find((it) => it.el.contains(button)));
  });
  summarize();
});
```

## Notes

- The whole zone is the `<label>` of a real `<input type="file" multiple accept="image/*">`. Tab focuses the input and outlines the zone, and Enter or Space opens the picker (on phones that includes the camera). `aria-labelledby` gives it a short name ("Drop photos here or browse your files"), and the format and limit hint is its description. Rows sit in a `role="list"`, each remove button is named after its file, and focus moves to a neighbouring row (or back to the input) when a row is removed.
- One polite `role="status"` line carries "Uploading 2 photos…", "3 photos ready", removals and skipped files (wrong type, over 10 MB, over the 8-photo limit). Per-row percentages are visual only, so screen readers aren't flooded.
- Without JS the input shows as a styled native picker inside the zone and submits with its form. Earlier photos show as static rows, and their remove buttons are hidden. With JS, the visible list is mirrored back into `input.files` via `DataTransfer`, so a normal submit still sends exactly what's listed. Object URLs are revoked on removal.
- Reduced motion: no fan, no marching ants and no lean. The border just turns solid primary while dragging. Row entrances, the exit and the FLIP are skipped, and the progress ring steps instead of gliding. The ants run only while files are held over the zone, so they never move on their own.
- Contrast: `--text-muted` copy stays at least 4.5:1 on the muted zone and on its 4% drag tint (the brighter glow sits behind the cards, not the text). The drag title uses `--primary` (about 4.9:1).
- To use real uploads, replace `upload()` with fetch/XHR and pass progress into `setProgress()`. Change `MAX_FILES`/`MAX_BYTES` and the hint together. The border radius lives in both the `rx` attribute and the CSS `rx` property, so keep them in step if you change `--radius-2xl`. `:has()` drives the zone focus outline.
