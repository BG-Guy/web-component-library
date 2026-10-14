# Support Chat Widget

A floating support chat with a brand-gradient launcher, an unread badge, and a "Hi! Need help?" teaser that pops up after a few seconds. Opening it is the signature moment: the bubble itself swells and morphs into the chat panel, with a clip-path radius spring from the corner as its gradient melts away to reveal the conversation. The panel has stacked agent avatars, a reply-time status, timestamped bubbles, a typing indicator, quick replies and a demo bot. On phones the panel grows into a full-screen sheet (`100dvh`, safe-area aware) with the page locked behind it. Depends on `tokens/variables.css`.

**Motion:** launcher-to-panel morph (clip-path circle → rounded panel, `--dur-4` `--ease-out`, lift on `--ease-spring`) with the gradient fading out · contents rise in staggered (`--stagger`) · icon swap spin · teaser and badge pop (`--ease-spring`) · bubbles spring in · typing dots bounce (1.1s loop, only while typing) · status ping (3 runs).

## HTML

```html
<div class="chat-widget-demo">
  <div class="chat-widget-demo__inner">
    <p class="chat-widget-demo__eyebrow">Plumbing &amp; heating · Springfield</p>
    <h2 class="chat-widget-demo__title">Questions before you book?</h2>
    <p class="chat-widget-demo__lead">Our support team answers in minutes, seven days a week. Tap the chat bubble in the corner and ask away.</p>
    <ul class="chat-widget-demo__facts" role="list">
      <li><strong>2 min</strong><span>average first reply</span></li>
      <li><strong>8am–8pm</strong><span>every day, real people</span></li>
      <li><strong>4.9/5</strong><span>support rating</span></li>
    </ul>
  </div>
</div>

<div class="chat-widget">
  <div class="chat-widget__teaser" hidden>
    <button class="chat-widget__teaser-body" type="button">
      <span class="chat-widget__teaser-avatar" aria-hidden="true">MR</span>
      <span class="chat-widget__teaser-copy"><strong>Hi! Need help?</strong>Maria from Brand is online now.</span>
    </button>
    <button class="chat-widget__teaser-close" type="button" aria-label="Dismiss message">
      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
    </button>
  </div>

  <a class="chat-widget__launcher" href="/contact" aria-controls="chat-widget-panel">
    <span class="chat-widget__sr">Chat with us</span><span class="chat-widget__sr chat-widget__unread">, 1 unread message</span>
    <svg class="chat-widget__icon chat-widget__icon--chat" viewBox="0 0 24 24" width="26" height="26" aria-hidden="true" focusable="false"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22z" /><path d="M8.5 12h.01M12 12h.01M15.5 12h.01" /></svg>
    <svg class="chat-widget__icon chat-widget__icon--close" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
    <span class="chat-widget__badge" aria-hidden="true">1</span>
  </a>

  <dialog class="chat-widget__panel" id="chat-widget-panel" aria-labelledby="chat-widget-title">
    <div class="chat-widget__head" style="--chat-widget-i: 0">
      <span class="chat-widget__agents" aria-hidden="true"><span>MR</span><span>SK</span><span>JP</span></span>
      <div class="chat-widget__who">
        <h2 class="chat-widget__title" id="chat-widget-title">Brand support</h2>
        <p class="chat-widget__meta"><span class="chat-widget__dot" aria-hidden="true"></span>Typically replies in 2 min</p>
      </div>
      <button class="chat-widget__close" type="button" aria-label="Close chat">
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
      </button>
    </div>

    <div class="chat-widget__log" role="log" aria-labelledby="chat-widget-title" tabindex="0" style="--chat-widget-i: 1">
      <p class="chat-widget__day">Today</p>
      <div class="chat-widget__msg chat-widget__msg--agent is-new">
        <p class="chat-widget__bubble"><span class="chat-widget__sr">Maria said: </span>Hi! I’m Maria from the Springfield team. Need a hand with a leak, a booking or a quote?</p>
        <time class="chat-widget__time" datetime="09:41">09:41</time>
      </div>
      <div class="chat-widget__typing" hidden>
        <span class="chat-widget__dots" aria-hidden="true"><span></span><span></span><span></span></span>
        <span class="chat-widget__sr">Agent is typing</span>
      </div>
    </div>

    <div class="chat-widget__quick" role="group" aria-label="Quick replies" style="--chat-widget-i: 2">
      <button class="chat-widget__chip" type="button">Book a visit</button>
      <button class="chat-widget__chip" type="button">Pricing</button>
      <button class="chat-widget__chip chat-widget__chip--urgent" type="button">Emergency</button>
    </div>

    <form class="chat-widget__form" style="--chat-widget-i: 3">
      <label class="chat-widget__sr" for="chat-widget-input">Message</label>
      <input class="chat-widget__input" id="chat-widget-input" type="text" autocomplete="off" enterkeyhint="send" placeholder="Write a message…">
      <button class="chat-widget__send" type="submit" aria-label="Send">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4z" /></svg>
      </button>
    </form>

    <template class="chat-widget__tpl">
      <div class="chat-widget__msg is-new"><p class="chat-widget__bubble"><span class="chat-widget__sr"></span><span class="chat-widget__text"></span></p><time class="chat-widget__time"></time></div>
    </template>
  </dialog>
</div>
```

## CSS

```css
.chat-widget, .chat-widget-demo {
  --chat-widget-muted: color-mix(in srgb, var(--text-muted) 75%, var(--text-main));
  --chat-widget-accent: color-mix(in srgb, var(--primary) 80%, var(--text-main));
}
.chat-widget { --chat-widget-edge: 1rem; --chat-widget-size: 3.5rem; font-family: var(--font-sans); }
.chat-widget svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.chat-widget :is(button, a):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.chat-widget__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }

/* Launcher: brand-gradient bubble with an unread badge; its icon spins to a chevron while open */
.chat-widget__launcher {
  position: fixed; right: var(--chat-widget-edge); bottom: var(--chat-widget-edge); z-index: var(--z-toast);
  display: grid; place-items: center; width: var(--chat-widget-size); height: var(--chat-widget-size); border-radius: 50%;
  background: var(--gradient-brand); color: var(--text-inverse); text-decoration: none;
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 35%, transparent), var(--shadow-glow), var(--shadow-lg);
  transition: transform var(--dur-3) var(--ease-spring);
}
.chat-widget__launcher:hover { transform: scale(1.06); }
.chat-widget__launcher:active { transform: scale(0.94); }
.chat-widget__icon { grid-area: 1 / 1; transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring); }
.chat-widget__icon--close, .chat-widget__launcher[aria-expanded="true"] .chat-widget__icon--chat { opacity: 0; transform: rotate(-90deg) scale(0.5); }
.chat-widget__launcher[aria-expanded="true"] .chat-widget__icon--close { opacity: 1; transform: none; }
.chat-widget__badge {
  position: absolute; top: -0.125rem; right: -0.125rem; display: grid; place-items: center; min-width: 1.25rem; height: 1.25rem; padding: 0 0.3125rem;
  border-radius: 999px; background: var(--danger); color: var(--text-inverse); font: 700 0.6875rem/1 var(--font-sans); box-shadow: 0 0 0 2px var(--surface-light);
  animation: chat-widget-pop var(--dur-4) var(--ease-spring) 1.2s both;
  transition: transform var(--dur-3) var(--ease-out), opacity var(--dur-2);
}
.chat-widget.is-read .chat-widget__badge { opacity: 0; transform: scale(0); }
.chat-widget.is-read .chat-widget__unread { display: none; }

/* Teaser: a speech bubble that pops out of the launcher's corner */
.chat-widget__teaser {
  position: fixed; right: var(--chat-widget-edge); bottom: calc(var(--chat-widget-edge) + var(--chat-widget-size) + 0.75rem); z-index: var(--z-toast);
  display: flex; align-items: flex-start; width: min(18.5rem, calc(100% - 2 * var(--chat-widget-edge)));
  border-radius: var(--radius-xl) var(--radius-xl) 0.375rem var(--radius-xl); background: var(--surface-light); color: var(--text-main);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
  transform-origin: 100% 100%; animation: chat-widget-pop var(--dur-4) var(--ease-spring) both;
}
.chat-widget__teaser[hidden] { display: none; }
.chat-widget__teaser-body {
  flex: 1; display: flex; align-items: center; gap: 0.75rem; min-width: 0; padding: 0.875rem 0 0.875rem 0.875rem; border: 0; border-radius: inherit;
  background: none; color: inherit; font: inherit; text-align: left; cursor: pointer;
}
.chat-widget__teaser-copy { color: var(--chat-widget-muted); font-size: 0.8125rem; line-height: 1.4; }
.chat-widget__teaser-copy strong { display: block; color: var(--text-main); font: 600 0.9375rem/1.3 var(--font-display); letter-spacing: var(--tracking-tight); }
.chat-widget__teaser-close {
  flex: none; display: grid; place-items: center; width: 2rem; height: 2rem; margin: 0.375rem; padding: 0; border: 0; border-radius: 50%;
  background: none; color: var(--chat-widget-muted); cursor: pointer; transition: background-color var(--dur-2), color var(--dur-2);
}
.chat-widget__teaser-close:hover { background: var(--surface-muted); color: var(--text-main); }

/* Avatars: shared by the teaser and the header */
.chat-widget__teaser-avatar, .chat-widget__agents span {
  flex: none; display: grid; place-items: center; width: 2.25rem; height: 2.25rem; border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
  color: var(--text-inverse); font: 700 0.6875rem/1 var(--font-sans);
}
.chat-widget__agents { display: flex; flex: none; }
.chat-widget__agents span { margin-left: -0.625rem; box-shadow: 0 0 0 2px var(--surface-light); }
.chat-widget__agents span:first-child { margin-left: 0; }
.chat-widget__agents span:nth-child(2) { background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 55%, var(--primary-2))); color: var(--surface-deep); }
.chat-widget__agents span:nth-child(3) { background: linear-gradient(135deg, color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)), var(--surface-deep)); }

/* Panel: a full-screen sheet on phones. It starts clipped to the launcher's circle, covered in its gradient, and grows */
.chat-widget__panel {
  --chat-widget-from: inset(calc(100% - var(--chat-widget-edge) - var(--chat-widget-size)) var(--chat-widget-edge) var(--chat-widget-edge) calc(100% - var(--chat-widget-edge) - var(--chat-widget-size)) round calc(var(--chat-widget-size) / 2));
  --chat-widget-to: inset(0 round 0);
  position: fixed; inset: 0; z-index: var(--z-popover); overflow: hidden;
  width: 100%; max-width: none; height: 100vh; height: 100dvh; max-height: none; margin: 0; padding: 0; border: 0;
  background: var(--surface-light); color: var(--text-main);
  clip-path: var(--chat-widget-from);
  transition: clip-path var(--dur-4) var(--ease-spring), translate var(--dur-4) var(--ease-spring);
}
.chat-widget__panel[open] { display: flex; flex-direction: column; }
.chat-widget__panel[data-state="open"] { clip-path: var(--chat-widget-to); translate: none; }
.chat-widget__panel::backdrop { background: transparent; }
.chat-widget__panel::after {
  content: ""; position: absolute; inset: 0; z-index: 1; pointer-events: none;
  background: var(--gradient-brand); transition: opacity var(--dur-4) var(--ease-out);
}
.chat-widget__panel[data-state="open"]::after { opacity: 0; }
.chat-widget__panel[data-state="open"] > :not(template) { animation: chat-widget-rise var(--dur-4) var(--ease-out) calc(var(--chat-widget-i, 0) * var(--stagger) + 120ms) both; }
html:has(.chat-widget__panel:modal) { overflow: hidden; }

/* Header */
.chat-widget__head {
  display: flex; align-items: center; gap: 0.875rem; padding: max(1rem, env(safe-area-inset-top)) 1rem 1rem 1.25rem; border-bottom: 1px solid var(--border-subtle);
  background:
    radial-gradient(120% 160% at 0% 0%, color-mix(in srgb, var(--primary) 10%, transparent), transparent 60%),
    radial-gradient(100% 160% at 100% 0%, color-mix(in srgb, var(--primary-2) 8%, transparent), transparent 60%);
}
.chat-widget__who { flex: 1; min-width: 0; }
.chat-widget__title { margin: 0; font: 600 1.0625rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.chat-widget__meta { display: flex; align-items: center; gap: 0.4375rem; margin: 0.25rem 0 0; color: var(--chat-widget-muted); font-size: 0.8125rem; }
.chat-widget__dot { position: relative; flex: none; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); }
.chat-widget__dot::after { content: ""; position: absolute; inset: 0; border-radius: 50%; background: var(--success); animation: chat-widget-ping 1.6s var(--ease-out) 3; }
.chat-widget__close {
  flex: none; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-muted); color: var(--chat-widget-muted); transition: background-color var(--dur-2), color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.chat-widget__close:hover { background: var(--border-subtle); color: var(--text-main); transform: translateY(2px); }

/* Conversation */
.chat-widget__log { flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 0.75rem; padding: 1.25rem 1rem; overflow-y: auto; overscroll-behavior: contain; }
.chat-widget__log:focus-visible { outline: 2px solid transparent; box-shadow: inset 0 0 0 2px var(--primary); }
.chat-widget__day { align-self: center; margin: 0 0 0.25rem; padding: 0.25rem 0.625rem; border-radius: 999px; background: var(--surface-muted); color: var(--chat-widget-muted); font: 500 0.6875rem/1.4 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.chat-widget__msg { display: grid; justify-items: start; gap: 0.25rem; max-width: 86%; transform-origin: 0 100%; }
.chat-widget__msg.is-new { animation: chat-widget-in var(--dur-4) var(--ease-spring) both; }
.chat-widget__msg--me { align-self: flex-end; justify-items: end; transform-origin: 100% 100%; }
.chat-widget__bubble {
  margin: 0; padding: 0.625rem 0.875rem; border-radius: 1.125rem 1.125rem 1.125rem 0.375rem; overflow-wrap: anywhere;
  background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); font-size: 0.9375rem; line-height: 1.45;
}
.chat-widget__msg--me .chat-widget__bubble {
  border-radius: 1.125rem 1.125rem 0.375rem 1.125rem; background: linear-gradient(135deg, var(--primary), var(--primary-hover));
  color: var(--text-inverse); box-shadow: inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 20%, transparent), 0 8px 20px -10px var(--primary);
}
.chat-widget__time { padding-inline: 0.375rem; color: var(--chat-widget-muted); font: 0.6875rem var(--font-mono); }
.chat-widget__typing {
  align-self: flex-start; display: inline-flex; padding: 0.875rem 1rem; border-radius: 1.125rem 1.125rem 1.125rem 0.375rem;
  background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle);
}
.chat-widget__typing[hidden] { display: none; }
.chat-widget__dots { display: flex; gap: 0.3125rem; }
.chat-widget__dots span { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--chat-widget-muted); animation: chat-widget-bounce 1.1s var(--ease-in-out) infinite; }
.chat-widget__dots span:nth-child(2) { animation-delay: 0.15s; }
.chat-widget__dots span:nth-child(3) { animation-delay: 0.3s; }

/* Quick replies and composer */
.chat-widget__quick { display: flex; gap: 0.5rem; padding: 0 1rem 0.75rem; overflow-x: auto; scrollbar-width: none; }
.chat-widget__chip {
  flex: none; display: inline-flex; align-items: center; gap: 0.4375rem; height: 2.25rem; padding: 0 0.875rem; border: 0; border-radius: 999px; cursor: pointer;
  background: color-mix(in srgb, var(--primary) 8%, var(--surface-light)); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 25%, transparent);
  color: var(--chat-widget-accent); font: 600 0.8125rem var(--font-sans);
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.chat-widget__chip:hover { background: color-mix(in srgb, var(--primary) 14%, var(--surface-light)); }
.chat-widget__chip:active { transform: scale(0.95); }
.chat-widget__chip--urgent::before { content: ""; width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--danger); box-shadow: 0 0 0 3px color-mix(in srgb, var(--danger) 18%, transparent); }
.chat-widget__form { display: flex; gap: 0.5rem; padding: 0.75rem 1rem max(0.75rem, env(safe-area-inset-bottom)); border-top: 1px solid var(--border-subtle); }
.chat-widget__input {
  flex: 1; min-width: 0; height: 2.75rem; padding: 0 1rem; border: 0; border-radius: 999px;
  background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); color: var(--text-main); font: 1rem var(--font-sans);
  transition: box-shadow var(--dur-2);
}
.chat-widget__input::placeholder { color: var(--chat-widget-muted); opacity: 1; }
.chat-widget__input:focus { outline: 2px solid transparent; box-shadow: inset 0 0 0 1px var(--primary), var(--focus-ring); }
.chat-widget__send {
  flex: none; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--primary); color: var(--text-inverse); box-shadow: var(--shadow-glow); transition: transform var(--dur-3) var(--ease-spring);
}
.chat-widget__send svg { transition: transform var(--dur-3) var(--ease-spring); }
.chat-widget__send:hover svg { transform: translate(2px, -2px); }
.chat-widget__send:active { transform: scale(0.9); }

/* Demo page behind the widget */
.chat-widget-demo {
  min-height: 40rem; color: var(--text-main); font-family: var(--font-sans);
  background: radial-gradient(70% 50% at 100% 100%, color-mix(in srgb, var(--primary-2) 12%, transparent), transparent 70%), var(--surface-muted);
}
.chat-widget-demo__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(3.5rem, 9vw, 6rem) var(--gutter) 8rem; }
.chat-widget-demo__eyebrow { margin: 0; color: var(--chat-widget-accent); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.chat-widget-demo__title { max-width: 14ch; margin: 0.875rem 0 0; font: 600 clamp(2.25rem, 1.4rem + 4vw, 4rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.chat-widget-demo__lead { max-width: 32rem; margin: 1.25rem 0 0; color: var(--chat-widget-muted); font-size: 1.0625rem; line-height: 1.6; }
.chat-widget-demo__facts { display: grid; gap: 0.75rem; margin: 2.5rem 0 0; padding: 0; list-style: none; }
.chat-widget-demo__facts li { display: grid; gap: 0.25rem; padding: 1rem 1.125rem; border-radius: var(--radius-xl); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm); }
.chat-widget-demo__facts strong { font: 600 1.375rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.chat-widget-demo__facts span { color: var(--chat-widget-muted); font-size: 0.875rem; }

/* Wider screens: a floating panel above the launcher; it starts lowered onto the launcher, then lifts */
@media (min-width: 768px) {
  .chat-widget { --chat-widget-edge: 1.5rem; }
  .chat-widget__panel {
    --chat-widget-from: inset(calc(100% - var(--chat-widget-size)) 0 0 calc(100% - var(--chat-widget-size)) round calc(var(--chat-widget-size) / 2));
    --chat-widget-to: inset(-3rem round 0); /* room for the shadow */
    inset: auto var(--chat-widget-edge) calc(var(--chat-widget-edge) + var(--chat-widget-size) + 1rem) auto;
    width: 23.5rem; height: min(40rem, calc(100vh - 9rem)); border-radius: var(--radius-2xl);
    box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl), 0 30px 80px -30px color-mix(in srgb, var(--primary) 45%, transparent);
    translate: 0 calc(var(--chat-widget-size) + 1rem);
  }
  .chat-widget-demo__facts { grid-template-columns: repeat(3, minmax(0, 12rem)); }
}

/* Reduced motion: no morph, no bounce; the panel simply appears */
@media (prefers-reduced-motion: reduce) {
  .chat-widget__panel { clip-path: none; translate: none; }
  .chat-widget__panel::after { display: none; }
  .chat-widget *, .chat-widget *::before, .chat-widget *::after { animation: none !important; }
}

@keyframes chat-widget-pop { from { opacity: 0; scale: 0.6; } }
@keyframes chat-widget-rise { from { opacity: 0; translate: 0 0.75rem; } }
@keyframes chat-widget-in { from { opacity: 0; scale: 0.85; translate: 0 0.5rem; } }
@keyframes chat-widget-bounce { 0%, 60%, 100% { transform: none; opacity: 0.55; } 30% { transform: translateY(-0.3125rem); opacity: 1; } }
@keyframes chat-widget-ping { to { transform: scale(2.6); opacity: 0; } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const wide = matchMedia('(min-width: 768px)');
// Demo bot: canned replies picked by keyword. Swap send() for your chat provider's API.
const REPLIES = [
  [/book|visit|slot|appoint/i, 'Lovely! Our next free window is tomorrow, 10–12, in Westlake, Northside or Riverside. Shall I hold it for you?'],
  [/emergenc|urgent|burst|flood/i, 'For a burst pipe or no heating, call (555) 555-0123 now. An engineer is on call 24/7 and usually with you within the hour.'],
  [/pric|cost|quote|\$/i, 'Call-outs are a flat $89, and most leak repairs land between $149 and $220. You always get a written quote before we start.'],
];
const FALLBACK = 'Thanks! I’ll pick this up in about 2 minutes. If it’s urgent, call (555) 555-0123.';

document.querySelectorAll('.chat-widget').forEach((root, n) => {
  const uid = `chat-widget-${n}`;
  const [launcher, panel, title, log, typing, form, input, teaser, tpl] = ['launcher', 'panel', 'title', 'log', 'typing', 'form', 'input', 'teaser', 'tpl']
    .map((part) => root.querySelector(`.chat-widget__${part}`));
  let closing = 0, reply = 0;

  // Unique ids per instance; with JS the /contact link becomes the disclosure button for the panel
  panel.id = `${uid}-panel`;
  title.id = `${uid}-title`;
  form.querySelector('label').htmlFor = input.id = `${uid}-input`;
  panel.setAttribute('aria-labelledby', title.id);
  log.setAttribute('aria-labelledby', title.id);
  Object.entries({ role: 'button', 'aria-controls': panel.id, 'aria-haspopup': 'dialog', 'aria-expanded': 'false' })
    .forEach(([k, v]) => launcher.setAttribute(k, v));

  // Phones get a modal full-screen sheet; wider screens a non-modal floating panel
  const open = () => {
    clearTimeout(closing);
    teaser.hidden = true;
    if (!panel.open) wide.matches ? panel.show() : panel.showModal();
    root.classList.add('is-read');
    launcher.setAttribute('aria-expanded', 'true');
    requestAnimationFrame(() => requestAnimationFrame(() => { panel.dataset.state = 'open'; }));
    input.focus({ preventScroll: true });
    log.scrollTop = log.scrollHeight;
  };
  const close = () => {
    if (panel.dataset.state !== 'open') return;
    delete panel.dataset.state;
    launcher.setAttribute('aria-expanded', 'false');
    closing = setTimeout(() => { panel.close(); launcher.focus(); }, reduce.matches ? 0 : 560); // --dur-4
  };

  launcher.addEventListener('click', (e) => {
    e.preventDefault();
    if (panel.dataset.state === 'open') close(); else open();
  });
  launcher.addEventListener('keydown', (e) => { if (e.key === ' ') { e.preventDefault(); launcher.click(); } });
  panel.addEventListener('keydown', (e) => { if (e.key === 'Escape') { e.preventDefault(); close(); } });
  panel.addEventListener('cancel', (e) => { e.preventDefault(); close(); });
  panel.addEventListener('close', () => { delete panel.dataset.state; launcher.setAttribute('aria-expanded', 'false'); });
  panel.querySelector('.chat-widget__close').addEventListener('click', close);

  // Teaser pops up after a few seconds, once per session
  let dismissed = false;
  try { dismissed = sessionStorage.getItem('chat-widget-teaser') === 'off'; } catch { /* storage blocked */ }
  if (!dismissed) setTimeout(() => { if (!panel.open) teaser.hidden = false; }, 4000);
  teaser.addEventListener('click', (e) => {
    if (e.target.closest('.chat-widget__teaser-body')) return open();
    if (!e.target.closest('.chat-widget__teaser-close')) return;
    teaser.hidden = true;
    launcher.focus();
    try { sessionStorage.setItem('chat-widget-teaser', 'off'); } catch { /* storage blocked */ }
  });

  // Messages go into the role="log" before the typing indicator, so each one is announced once
  const add = (text, who) => {
    const msg = tpl.content.firstElementChild.cloneNode(true);
    const now = new Date();
    msg.classList.add(`chat-widget__msg--${who}`);
    msg.querySelector('.chat-widget__sr').textContent = who === 'me' ? 'You said: ' : 'Maria said: ';
    msg.querySelector('.chat-widget__text').textContent = text;
    msg.querySelector('time').dateTime = now.toISOString();
    msg.querySelector('time').textContent = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    log.insertBefore(msg, typing);
    log.scrollTo({ top: log.scrollHeight, behavior: reduce.matches ? 'auto' : 'smooth' });
  };
  const send = (text) => {
    if (!(text = text.trim())) return;
    add(text, 'me');
    clearTimeout(reply);
    const answer = (REPLIES.find(([re]) => re.test(text)) || [null, FALLBACK])[1];
    reply = setTimeout(() => {
      typing.hidden = false;
      log.scrollTop = log.scrollHeight;
      reply = setTimeout(() => { typing.hidden = true; add(answer, 'agent'); }, 900 + answer.length * 10);
    }, 500);
  };
  form.addEventListener('submit', (e) => { e.preventDefault(); send(input.value); input.value = ''; });
  root.querySelectorAll('.chat-widget__chip').forEach((chip) => chip.addEventListener('click', () => { send(chip.textContent); input.focus(); }));
  log.addEventListener('animationend', (e) => e.target.classList.remove('is-new')); // don't replay on reopen
});
```

## Notes

- **Accessibility:** without JS the launcher is a plain link to `/contact`. With JS it becomes a disclosure button (`aria-expanded`, `aria-controls`) for a `<dialog>` panel. On wider screens the panel is non-modal, so the page stays usable. On phones it's a modal full-screen sheet (`showModal()`) with the page inert and scroll locked. Escape and the header chevron close it and return focus to the launcher, and opening puts focus in the message field.
- The conversation is a `role="log"`. New bubbles go in before the typing indicator, so each is announced once with "You said" or "Maria said". Showing the indicator announces its visually hidden "Agent is typing". The scrollable log is keyboard-focusable, and the unread count is in the launcher's name until the panel is opened.
- **Install:** put `.chat-widget` once before `</body>`. All its parts are `position: fixed` (launcher and teaser on `--z-toast`, panel on `--z-popover`). Replace the demo bot in `send()` with your provider's API and keep `add()` for rendering. The teaser shows after 4s, once per session (`sessionStorage`, try/catch).
- **Motion:** the panel starts clipped to the launcher's exact circle and covered in the same gradient, then grows into the panel as the gradient fades. Closing plays it in reverse back into the bubble. Typing dots only loop while a reply is coming (under 3s), and the status dot pings three times. Under reduced motion the panel just appears and nothing bounces.
- **Contrast:** muted text uses `--chat-widget-muted` (≈ 5.9:1 on white), your bubbles put `--text-inverse` on `--primary` to `--primary-hover` (≥ 5.2:1), chips are ≥ 5.6:1, and the unread badge is 4.8:1.
