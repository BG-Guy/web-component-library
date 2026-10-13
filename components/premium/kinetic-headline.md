# Kinetic Headline

Typography that performs. Add `data-kinetic` to any heading or paragraph:

- `rise`: words lift out of a blur in sequence when the text enters view.
- `scrub`: a paragraph lights up word by word as you scroll through it.
- `.kinetic-text__mark`: a highlighter sweeps across a phrase.
- `.kinetic-text__underline`: a hand-drawn stroke draws itself under a phrase.

Depends on `tokens/variables.css`.

**Motion:** staggered rise with blur and slight rotation (`--dur-5`) · highlighter sweep · SVG stroke draw · scroll-linked word reveal (scroll-driven animations).

## HTML

```html
<section class="kinetic-text-demo" aria-labelledby="kinetic-title">
  <p class="kinetic-text-demo__eyebrow">Why homeowners switch</p>
  <h2 id="kinetic-title" class="kinetic-text kinetic-text-demo__title" data-kinetic="rise">
    We show up on time, <mark class="kinetic-text__mark">quote before we start</mark>, and get it right
    <span class="kinetic-text__underline">the first time<svg viewBox="0 0 200 14" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M3 10 C 45 3, 110 2, 197 8" pathLength="1" /></svg></span>.
  </h2>
  <p class="kinetic-text kinetic-text-demo__body" data-kinetic="scrub">
    Every visit starts with a written, flat-rate price. Our technicians are licensed, background-checked
    and trained to leave your home cleaner than they found it. If something we fixed fails within five
    years, we come back and make it right, free.
  </p>
</section>
```

## CSS

```css
/* Before the script runs: hide rise headings only when JS is on (no flash), with a failsafe reveal */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .kinetic-text[data-kinetic="rise"]:not(.kinetic-text--ready) { opacity: 0; animation: kinetic-failsafe 0s 2.5s forwards; }
}
@keyframes kinetic-failsafe { to { opacity: 1; } }

.kinetic-text__w { display: inline-block; }

/* Rise: words lift out of a blur, one after another */
@media (prefers-reduced-motion: no-preference) {
  .kinetic-text--ready[data-kinetic="rise"] .kinetic-text__w {
    opacity: 0; transform: translateY(0.45em) rotate(3deg); transform-origin: 0 100%; filter: blur(8px);
    transition: opacity var(--dur-5) var(--ease-out), transform var(--dur-5) var(--ease-out), filter var(--dur-4) var(--ease-out);
    transition-delay: calc(var(--i) * 45ms);
  }
  .kinetic-text--in[data-kinetic="rise"] .kinetic-text__w { opacity: 1; transform: none; filter: none; }
}

/* Highlighter: sweeps in after the words have landed */
.kinetic-text__mark {
  padding: 0 0.12em; margin: 0 -0.04em; border-radius: 0.2em; color: inherit;
  background: linear-gradient(100deg, color-mix(in srgb, var(--primary-2) 28%, transparent), color-mix(in srgb, var(--primary) 22%, transparent)) no-repeat 0 0 / 100% 100%;
  -webkit-box-decoration-break: clone; box-decoration-break: clone;
  transition: background-size calc(var(--dur-5) * 1.2) var(--ease-out) calc(var(--dur-4) + 200ms);
}
.kinetic-text--ready:not(.kinetic-text--in) .kinetic-text__mark,
.kinetic-text__mark.kinetic-text--ready:not(.kinetic-text--in) { background-size: 0% 100%; }

/* Hand-drawn underline: the stroke draws itself */
.kinetic-text__underline { position: relative; white-space: nowrap; }
.kinetic-text__underline svg { position: absolute; left: -2%; bottom: -0.16em; width: 104%; height: 0.3em; overflow: visible; }
.kinetic-text__underline path {
  fill: none; stroke: var(--primary-2); stroke-width: 3; stroke-linecap: round;
  stroke-dasharray: 1; stroke-dashoffset: 0;
  transition: stroke-dashoffset calc(var(--dur-5) * 1.3) var(--ease-out) calc(var(--dur-4) + 400ms);
}
.kinetic-text--ready:not(.kinetic-text--in) .kinetic-text__underline path { stroke-dashoffset: 1; }

/* Scrub: each word brightens at its own point in the paragraph's scroll range */
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .kinetic-text--ready[data-kinetic="scrub"] { view-timeline-name: --kinetic-scrub; view-timeline-axis: block; }
    .kinetic-text--ready[data-kinetic="scrub"] .kinetic-text__w {
      animation: kinetic-scrub linear both;
      animation-timeline: --kinetic-scrub;
      animation-range: cover calc(12% + var(--p) * 40%) cover calc(18% + var(--p) * 40%);
    }
  }
}
@keyframes kinetic-scrub { from { opacity: 0.2; filter: blur(1px); } to { opacity: 1; filter: none; } }

/* Demo layout */
.kinetic-text-demo { max-width: 56rem; margin-inline: auto; padding: clamp(4rem, 10vw, 7rem) var(--gutter); color: var(--text-main); font-family: var(--font-sans); }
.kinetic-text-demo__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.kinetic-text-demo__title { margin: 1rem 0 0; font: 600 clamp(2rem, 1.1rem + 3.8vw, 3.75rem)/1.1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.kinetic-text-demo__body { margin: 3.5rem 0 0; font: 500 clamp(1.375rem, 1rem + 1.6vw, 2rem)/1.45 var(--font-display); letter-spacing: -0.015em; }
```

## JS

```js
// Wrap each word in a span (inside nested marks/underlines too), numbered for staggering
const kineticSplit = (el) => {
  const words = [];
  const walk = (node) => {
    [...node.childNodes].forEach((child) => {
      if (child.nodeType === Node.TEXT_NODE) {
        const frag = document.createDocumentFragment();
        child.textContent.split(/(\s+)/).forEach((part) => {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.append(part); return; }
          const span = document.createElement('span');
          span.className = 'kinetic-text__w';
          span.textContent = part;
          words.push(span);
          frag.append(span);
        });
        child.replaceWith(frag);
      } else if (child.nodeType === Node.ELEMENT_NODE && child.namespaceURI !== 'http://www.w3.org/2000/svg') {
        walk(child);
      }
    });
  };
  walk(el);
  return words;
};

// Mark each effect "in" once it scrolls into view
const kineticIO = new IntersectionObserver((entries) => entries.forEach((entry) => {
  if (!entry.isIntersecting) return;
  entry.target.classList.add('kinetic-text--in');
  kineticIO.unobserve(entry.target);
}), { rootMargin: '0px 0px -12% 0px' });

document.querySelectorAll('.kinetic-text[data-kinetic]').forEach((el) => {
  if (el.dataset.kinetic === 'rise' || el.dataset.kinetic === 'scrub') {
    if (/^H[1-6]$/.test(el.tagName)) el.setAttribute('aria-label', el.textContent.replace(/\s+/g, ' ').trim());
    const words = kineticSplit(el);
    words.forEach((w, i) => {
      w.style.setProperty('--i', i);
      w.style.setProperty('--p', (i / Math.max(words.length - 1, 1)).toFixed(3));
    });
  }
  el.classList.add('kinetic-text--ready');
  kineticIO.observe(el);
});
```

## Notes

- Content is never lost. Without JS everything shows in its final state, and the `scripting` media query plus a 2.5s failsafe means a heading can't stay hidden if the script fails.
- Under reduced motion the words aren't hidden or moved; marks and underlines simply appear.
- Headings get an `aria-label` with their full text, so screen readers read one phrase rather than per-word fragments.
- `scrub` needs scroll-driven animations (Chromium, Safari 26+). Elsewhere the paragraph is simply fully visible. Keep scrub text short (2–4 lines) and large; it's a statement, not body copy.
- A standalone highlighter outside a rise heading: `<mark class="kinetic-text kinetic-text__mark" data-kinetic="mark">`.
- One kinetic heading per screen. Several animating at once loses the effect.
