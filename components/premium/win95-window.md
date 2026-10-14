# Windows 95 Desktop

A teal Windows 95 desktop where the quote form lives in a real window. Double-click (or press Enter on) "My Home", "Quote.exe" or "Recycle Bin" to open a window. Windows drag by the title bar, minimise into the taskbar with the classic zoom-to-button flight, maximise to fill the desktop and close, while the active window's title bar lights up navy-to-blue. Sending the quote opens a "Scheduling technician…" dialog with flying paperwork and a block-by-block progress bar. The Start button opens a menu with a vertical "Brand 95" banner, and the tray clock keeps real time. On phones the icons form a grid and only one window shows at a time, full width, with no dragging. Depends on `tokens/variables.css`.

**Motion:** minimise and restore flight between window and taskbar button (WAAPI, 260 ms, `--ease-out` curve) · progress fills in whole blocks (JS steps) · paperwork arc while scheduling (4 × 1.1s, only while the dialog is busy) · bevel presses are instant, as in 1995.

## HTML

```html
<section class="win95" aria-labelledby="win95-title" data-win95>
  <h2 id="win95-title" class="win95__sr">Brand 95: request a quote</h2>

  <svg class="win95__sprite" aria-hidden="true" focusable="false">
    <symbol id="win95-i-home" viewBox="0 0 32 32">
      <g class="win95__px-ink"><rect x="20" y="5" width="4" height="7" /></g>
      <g class="win95__px-maroon"><rect x="21" y="6" width="2" height="6" /></g>
      <g class="win95__px-ink"><rect x="14" y="4" width="4" height="2" /><rect x="12" y="6" width="8" height="2" /><rect x="10" y="8" width="12" height="2" /><rect x="8" y="10" width="16" height="2" /><rect x="6" y="12" width="20" height="2" /><rect x="4" y="14" width="24" height="2" /><rect x="4" y="16" width="24" height="1" /><rect x="6" y="16" width="20" height="13" /></g>
      <g class="win95__px-maroon"><rect x="15" y="5" width="2" height="2" /><rect x="13" y="7" width="6" height="2" /><rect x="11" y="9" width="10" height="2" /><rect x="9" y="11" width="14" height="2" /><rect x="7" y="13" width="18" height="2" /><rect x="5" y="15" width="22" height="1" /></g>
      <g class="win95__px-light"><rect x="7" y="17" width="13" height="11" /></g>
      <g class="win95__px-face"><rect x="20" y="17" width="5" height="11" /></g>
      <g class="win95__px-ink"><rect x="13" y="20" width="6" height="9" /><rect x="8" y="19" width="4" height="4" /><rect x="20" y="19" width="4" height="4" /></g>
      <g class="win95__px-navy"><rect x="14" y="21" width="4" height="7" /></g>
      <g class="win95__px-blue"><rect x="9" y="20" width="2" height="2" /><rect x="21" y="20" width="2" height="2" /></g>
      <g class="win95__px-yellow"><rect x="16" y="24" width="1" height="1" /></g>
    </symbol>
    <symbol id="win95-i-quote" viewBox="0 0 32 32">
      <g class="win95__px-ink"><rect x="6" y="3" width="17" height="26" /></g>
      <g class="win95__px-light"><rect x="7" y="4" width="15" height="24" /></g>
      <g class="win95__px-navy"><rect x="9" y="6" width="10" height="2" /></g>
      <g class="win95__px-shadow"><rect x="9" y="10" width="11" height="1" /><rect x="9" y="13" width="11" height="1" /><rect x="9" y="16" width="8" height="1" /></g>
      <g class="win95__px-ink"><rect x="8" y="20" width="9" height="6" /><rect x="23" y="6" width="5" height="16" /><rect x="24" y="22" width="3" height="1" /><rect x="25" y="23" width="1" height="2" /></g>
      <g class="win95__px-yellow"><rect x="9" y="21" width="7" height="4" /><rect x="24" y="9" width="3" height="10" /></g>
      <g class="win95__px-maroon"><rect x="24" y="7" width="3" height="2" /><rect x="11" y="22" width="3" height="2" /></g>
      <g class="win95__px-hilite"><rect x="24" y="19" width="3" height="2" /></g>
    </symbol>
    <symbol id="win95-i-bin" viewBox="0 0 32 32">
      <g class="win95__px-ink"><rect x="7" y="6" width="18" height="4" /><rect x="9" y="10" width="14" height="19" /></g>
      <g class="win95__px-light"><rect x="8" y="7" width="16" height="2" /></g>
      <g class="win95__px-hilite"><rect x="10" y="10" width="12" height="18" /></g>
      <g class="win95__px-shadow"><rect x="12" y="11" width="1" height="16" /><rect x="15" y="11" width="1" height="16" /><rect x="18" y="11" width="1" height="16" /><rect x="10" y="27" width="12" height="1" /></g>
      <g class="win95__px-light"><rect x="10" y="11" width="1" height="15" /></g>
    </symbol>
    <symbol id="win95-i-papers" viewBox="0 0 32 32">
      <g class="win95__px-ink"><rect x="10" y="1" width="7" height="6" /><rect x="16" y="2" width="7" height="5" /></g>
      <g class="win95__px-light"><rect x="11" y="2" width="5" height="4" /></g>
      <g class="win95__px-hilite"><rect x="17" y="3" width="5" height="3" /></g>
    </symbol>
    <symbol id="win95-i-folder" viewBox="0 0 32 32">
      <g class="win95__px-ink"><rect x="3" y="6" width="11" height="4" /><rect x="3" y="9" width="26" height="19" /></g>
      <g class="win95__px-folder"><rect x="4" y="7" width="9" height="3" /><rect x="4" y="10" width="24" height="17" /></g>
      <g class="win95__px-light"><rect x="4" y="10" width="24" height="1" /></g>
      <g class="win95__px-folder-lo"><rect x="4" y="13" width="24" height="1" /><rect x="4" y="25" width="24" height="2" /></g>
    </symbol>
    <symbol id="win95-i-speaker" viewBox="0 0 16 16">
      <g fill="currentColor"><rect x="2" y="6" width="3" height="4" /><rect x="5" y="5" width="1" height="6" /><rect x="6" y="4" width="1" height="8" /><rect x="7" y="3" width="1" height="10" /><rect x="9" y="6" width="1" height="4" /><rect x="11" y="4" width="1" height="8" /></g>
    </symbol>
    <symbol id="win95-g-min" viewBox="0 0 9 9"><rect x="1" y="6" width="6" height="2" fill="currentColor" /></symbol>
    <symbol id="win95-g-max" viewBox="0 0 9 9"><g fill="currentColor"><rect x="0" y="0" width="9" height="2" /><rect x="0" y="2" width="1" height="7" /><rect x="8" y="2" width="1" height="7" /><rect x="0" y="8" width="9" height="1" /></g></symbol>
    <symbol id="win95-g-restore" viewBox="0 0 9 9"><g fill="currentColor"><rect x="2" y="0" width="7" height="2" /><rect x="2" y="2" width="1" height="1" /><rect x="8" y="2" width="1" height="4" /><rect x="7" y="5" width="1" height="1" /><rect x="0" y="3" width="7" height="2" /><rect x="0" y="5" width="1" height="3" /><rect x="6" y="5" width="1" height="3" /><rect x="0" y="8" width="7" height="1" /></g></symbol>
    <symbol id="win95-g-close" viewBox="0 0 9 9"><g fill="currentColor"><rect x="0" y="1" width="2" height="1" /><rect x="6" y="1" width="2" height="1" /><rect x="1" y="2" width="2" height="1" /><rect x="5" y="2" width="2" height="1" /><rect x="2" y="3" width="4" height="1" /><rect x="3" y="4" width="2" height="1" /><rect x="2" y="5" width="4" height="1" /><rect x="1" y="6" width="2" height="1" /><rect x="5" y="6" width="2" height="1" /><rect x="0" y="7" width="2" height="1" /><rect x="6" y="7" width="2" height="1" /></g></symbol>
  </svg>

  <div class="win95__desk">
    <ul class="win95__icons" role="list" data-win95-js inert>
      <li><button class="win95__icon" type="button" data-win95-open="win95-home"><svg class="win95__icon-img" viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-home" /></svg><span class="win95__icon-label">My Home</span></button></li>
      <li><button class="win95__icon" type="button" data-win95-open="win95-quote"><svg class="win95__icon-img" viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-quote" /></svg><span class="win95__icon-label">Quote.exe</span></button></li>
      <li><button class="win95__icon" type="button" data-win95-open="win95-bin"><svg class="win95__icon-img" viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-bin" /><use class="win95__papers" href="#win95-i-papers" /></svg><span class="win95__icon-label">Recycle Bin</span></button></li>
    </ul>

    <!-- Quote window: open by default (and the whole no-JS experience) -->
    <div class="win95__window is-front" id="win95-quote" role="dialog" aria-labelledby="win95-quote-title" style="--win95-x: 8.5rem; --win95-y: 1.25rem; --win95-w: 34rem">
      <div class="win95__titlebar">
        <button class="win95__move" type="button" aria-describedby="win95-quote-tip" data-win95-js inert>
          <svg class="win95__app" viewBox="0 0 32 32" width="16" height="16" aria-hidden="true" focusable="false"><use href="#win95-i-quote" /></svg>
          <span id="win95-quote-title">Request a Quote</span>
        </button>
        <span class="win95__tip" id="win95-quote-tip" aria-hidden="true">Arrow keys move · Enter maximizes</span>
        <div class="win95__controls" data-win95-js inert>
          <button class="win95__ctl" type="button" data-win95-act="min" aria-label="Minimize"><svg viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-min" /></svg></button>
          <button class="win95__ctl win95__ctl--max" type="button" data-win95-act="max" aria-label="Maximize"><svg class="win95__g-max" viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-max" /></svg><svg class="win95__g-restore" viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-restore" /></svg></button>
          <button class="win95__ctl win95__ctl--close" type="button" data-win95-act="close" aria-label="Close"><svg viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-close" /></svg></button>
        </div>
      </div>
      <div class="win95__body win95__body--quote">
        <div class="win95__wizard" aria-hidden="true">
          <svg viewBox="0 0 32 32" width="64" height="64" shape-rendering="crispEdges" focusable="false"><use href="#win95-i-home" /></svg>
          <span>Brand 95<br>Setup</span>
        </div>
        <form class="win95__form" action="#" method="post">
          <p class="win95__intro">Tell us what needs fixing. A Springfield technician calls you back within the hour.</p>
          <div class="win95__row">
            <label class="win95__field">Name<input class="win95__input" name="name" autocomplete="name" required data-win95-focus></label>
            <label class="win95__field">Phone<input class="win95__input" name="phone" type="tel" autocomplete="tel" required></label>
          </div>
          <label class="win95__field">Service
            <span class="win95__select">
              <select class="win95__input" name="service">
                <option>Plumbing</option><option>Electrical</option><option>Heating &amp; cooling</option><option>Roofing</option><option>Handyman</option>
              </select>
            </span>
          </label>
          <fieldset class="win95__group">
            <legend>Preferred time</legend>
            <label class="win95__radio"><input type="radio" name="time" value="morning" checked>Morning</label>
            <label class="win95__radio"><input type="radio" name="time" value="afternoon">Afternoon</label>
            <label class="win95__radio"><input type="radio" name="time" value="evening">Evening</label>
          </fieldset>
          <label class="win95__field">What's wrong?<textarea class="win95__input" name="details" rows="3"></textarea></label>
          <label class="win95__check"><span class="win95__box"><input type="checkbox" name="urgent"><span class="win95__tick" aria-hidden="true"></span></span>It's an emergency (24/7 line)</label>
          <div class="win95__actions">
            <button class="win95__btn win95__btn--default" type="submit">Send</button>
            <button class="win95__btn" type="reset">Clear</button>
          </div>
        </form>
      </div>
      <div class="win95__statusbar" aria-hidden="true"><span>Ready</span><span>Springfield · Westlake · Northside</span></div>
    </div>

    <div class="win95__window" id="win95-home" role="dialog" aria-labelledby="win95-home-title" style="--win95-x: 17rem; --win95-y: 5rem; --win95-w: 27rem" hidden>
      <div class="win95__titlebar">
        <button class="win95__move" type="button" aria-describedby="win95-home-tip">
          <svg class="win95__app" viewBox="0 0 32 32" width="16" height="16" aria-hidden="true" focusable="false"><use href="#win95-i-home" /></svg>
          <span id="win95-home-title">My Home</span>
        </button>
        <span class="win95__tip" id="win95-home-tip" aria-hidden="true">Arrow keys move · Enter maximizes</span>
        <div class="win95__controls">
          <button class="win95__ctl" type="button" data-win95-act="min" aria-label="Minimize"><svg viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-min" /></svg></button>
          <button class="win95__ctl win95__ctl--max" type="button" data-win95-act="max" aria-label="Maximize"><svg class="win95__g-max" viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-max" /></svg><svg class="win95__g-restore" viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-restore" /></svg></button>
          <button class="win95__ctl win95__ctl--close" type="button" data-win95-act="close" aria-label="Close"><svg viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-close" /></svg></button>
        </div>
      </div>
      <div class="win95__menubar" aria-hidden="true"><span>File</span><span>Edit</span><span>View</span><span>Help</span></div>
      <div class="win95__body">
        <ul class="win95__files" role="list">
          <li><svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-folder" /></svg><span><b>Kitchen</b>Faucet fixed 3/12</span></li>
          <li><svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-folder" /></svg><span><b>Bathroom</b>Annual check due</span></li>
          <li><svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-folder" /></svg><span><b>Attic</b>Insulation OK</span></li>
          <li><svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-folder" /></svg><span><b>Garage</b>Door tuned 8/24</span></li>
        </ul>
      </div>
      <div class="win95__statusbar"><span>4 object(s)</span><span>Next visit: Wed 15, 10–12</span></div>
    </div>

    <div class="win95__window" id="win95-bin" role="dialog" aria-labelledby="win95-bin-title" style="--win95-x: 21rem; --win95-y: 9rem; --win95-w: 24rem" hidden>
      <div class="win95__titlebar">
        <button class="win95__move" type="button" aria-describedby="win95-bin-tip">
          <svg class="win95__app" viewBox="0 0 32 32" width="16" height="16" aria-hidden="true" focusable="false"><use href="#win95-i-bin" /></svg>
          <span id="win95-bin-title">Recycle Bin</span>
        </button>
        <span class="win95__tip" id="win95-bin-tip" aria-hidden="true">Arrow keys move · Enter maximizes</span>
        <div class="win95__controls">
          <button class="win95__ctl" type="button" data-win95-act="min" aria-label="Minimize"><svg viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-min" /></svg></button>
          <button class="win95__ctl win95__ctl--max" type="button" data-win95-act="max" aria-label="Maximize"><svg class="win95__g-max" viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-max" /></svg><svg class="win95__g-restore" viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-restore" /></svg></button>
          <button class="win95__ctl win95__ctl--close" type="button" data-win95-act="close" aria-label="Close"><svg viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-close" /></svg></button>
        </div>
      </div>
      <div class="win95__body">
        <ul class="win95__trash" role="list">
          <li><svg viewBox="0 0 32 32" width="16" height="16" aria-hidden="true" focusable="false"><use href="#win95-i-quote" /></svg>leaky_faucet.old</li>
          <li><svg viewBox="0 0 32 32" width="16" height="16" aria-hidden="true" focusable="false"><use href="#win95-i-quote" /></svg>drafty_window.bak</li>
          <li><svg viewBox="0 0 32 32" width="16" height="16" aria-hidden="true" focusable="false"><use href="#win95-i-quote" /></svg>mystery_wiring.tmp</li>
        </ul>
        <p class="win95__note" role="status"></p>
        <div class="win95__actions"><button class="win95__btn" type="button" data-win95-act="empty">Empty Recycle Bin</button></div>
      </div>
    </div>

    <div class="win95__window win95__window--progress" id="win95-progress" role="dialog" aria-labelledby="win95-progress-title" aria-describedby="win95-progress-status" style="--win95-x: 14rem; --win95-y: 8.5rem; --win95-w: 23rem" hidden>
      <div class="win95__titlebar">
        <button class="win95__move" type="button" aria-describedby="win95-progress-tip">
          <span id="win95-progress-title">Scheduling technician…</span>
        </button>
        <span class="win95__tip" id="win95-progress-tip" aria-hidden="true">Arrow keys move · Enter maximizes</span>
        <div class="win95__controls">
          <button class="win95__ctl win95__ctl--close" type="button" data-win95-act="close" aria-label="Close"><svg viewBox="0 0 9 9" width="9" height="9" aria-hidden="true" focusable="false"><use href="#win95-g-close" /></svg></button>
        </div>
      </div>
      <div class="win95__body">
        <div class="win95__flight" aria-hidden="true">
          <svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" focusable="false"><use href="#win95-i-folder" /></svg>
          <span class="win95__paper"></span>
          <svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" focusable="false"><use href="#win95-i-home" /></svg>
        </div>
        <p class="win95__status" id="win95-progress-status" role="status">Finding the nearest technician…</p>
        <div class="win95__meter" role="progressbar" aria-labelledby="win95-progress-title" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><span class="win95__meter-fill"></span></div>
        <p class="win95__eta">From: Brand HQ, Westlake<br>To: your place, Springfield</p>
        <div class="win95__actions"><button class="win95__btn" type="button" data-win95-act="close" data-win95-focus>Cancel</button></div>
      </div>
    </div>
  </div>

  <div class="win95__taskbar">
    <div class="win95__taskbar-inner">
      <details class="win95__start">
        <summary class="win95__start-btn"><svg viewBox="0 0 32 32" width="16" height="16" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-home" /></svg>Start</summary>
        <div class="win95__menu">
          <span class="win95__banner" aria-hidden="true"><b>Brand</b>95</span>
          <ul class="win95__menu-list" role="list">
            <li data-win95-js hidden><button class="win95__menu-item" type="button" data-win95-open="win95-quote"><svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-quote" /></svg>Request a Quote</button></li>
            <li data-win95-js hidden><button class="win95__menu-item" type="button" data-win95-open="win95-home"><svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-home" /></svg>My Home</button></li>
            <li data-win95-js hidden><button class="win95__menu-item" type="button" data-win95-open="win95-bin"><svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-bin" /></svg>Recycle Bin</button></li>
            <li class="win95__menu-split"><a class="win95__menu-item" href="tel:+15555550123"><svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-speaker" /></svg>Call (555) 555-0123</a></li>
            <li><a class="win95__menu-item" href="mailto:hello@example.com"><svg viewBox="0 0 32 32" width="32" height="32" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-quote" /></svg>hello@example.com</a></li>
          </ul>
        </div>
      </details>
      <ul class="win95__tasks" role="list" aria-label="Open windows">
        <li><button class="win95__task" type="button" aria-pressed="true" data-win95-task="win95-quote" data-win95-js inert><svg viewBox="0 0 32 32" width="16" height="16" aria-hidden="true" focusable="false"><use href="#win95-i-quote" /></svg><span>Request a Quote</span></button></li>
        <li hidden><button class="win95__task" type="button" aria-pressed="false" data-win95-task="win95-home"><svg viewBox="0 0 32 32" width="16" height="16" aria-hidden="true" focusable="false"><use href="#win95-i-home" /></svg><span>My Home</span></button></li>
        <li hidden><button class="win95__task" type="button" aria-pressed="false" data-win95-task="win95-bin"><svg viewBox="0 0 32 32" width="16" height="16" aria-hidden="true" focusable="false"><use href="#win95-i-bin" /></svg><span>Recycle Bin</span></button></li>
      </ul>
      <div class="win95__tray">
        <svg viewBox="0 0 16 16" width="16" height="16" shape-rendering="crispEdges" aria-hidden="true" focusable="false"><use href="#win95-i-speaker" /></svg>
        <time class="win95__clock" data-win95-js hidden></time>
      </div>
    </div>
  </div>
</section>
```

## CSS

```css
/* Local Windows 95 palette, plus the four classic bevels as shadow stacks */
.win95 {
  --win95-desk: #008080;
  --win95-face: #c0c0c0;
  --win95-light: #ffffff;
  --win95-hilite: #dfdfdf;
  --win95-shadow: #808080;
  --win95-dark: #0a0a0a;
  --win95-ink: #000000;
  --win95-navy: #000080;
  --win95-blue: #1084d0;
  --win95-maroon: #800000;
  --win95-yellow: #ffff00;
  --win95-folder: #ffe680;
  --win95-folder-lo: #c0a000;
  --win95-tip: #ffffe1;
  --win95-font: Tahoma, Verdana, "Segoe UI", sans-serif;
  --win95-inactive: color-mix(in srgb, var(--win95-shadow) 75%, var(--win95-ink));
  --win95-raised: inset -1px -1px var(--win95-dark), inset 1px 1px var(--win95-light), inset -2px -2px var(--win95-shadow), inset 2px 2px var(--win95-hilite);
  --win95-pressed: inset -1px -1px var(--win95-light), inset 1px 1px var(--win95-dark), inset -2px -2px var(--win95-hilite), inset 2px 2px var(--win95-shadow);
  --win95-frame: inset -1px -1px var(--win95-dark), inset 1px 1px var(--win95-hilite), inset -2px -2px var(--win95-shadow), inset 2px 2px var(--win95-light);
  --win95-sunken: inset -1px -1px var(--win95-light), inset 1px 1px var(--win95-shadow), inset -2px -2px var(--win95-hilite), inset 2px 2px var(--win95-dark);
  position: relative; isolation: isolate; overflow: clip;
  background: var(--win95-desk); color: var(--win95-ink);
  font: 400 0.875rem/1.35 var(--win95-font);
}
@media (min-width: 768px) { .win95 { font-size: 0.8125rem; } }
.win95__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.win95__sprite { position: absolute; width: 0; height: 0; overflow: hidden; }
.win95 svg { flex: none; }

/* Icon pixels */
.win95__px-ink { fill: var(--win95-ink); }
.win95__px-light { fill: var(--win95-light); }
.win95__px-hilite { fill: var(--win95-hilite); }
.win95__px-face { fill: var(--win95-face); }
.win95__px-shadow { fill: var(--win95-shadow); }
.win95__px-navy { fill: var(--win95-navy); }
.win95__px-blue { fill: var(--win95-blue); }
.win95__px-maroon { fill: var(--win95-maroon); }
.win95__px-yellow { fill: var(--win95-yellow); }
.win95__px-folder { fill: var(--win95-folder); }
.win95__px-folder-lo { fill: var(--win95-folder-lo); }
.win95.is-empty .win95__papers { display: none; }

/* Desktop. Phones: icon grid, then one full-width window. 768px+: icon column, floating windows.
   The desk is its own stacking context, so window z-indexes never climb over the taskbar's Start menu */
.win95__desk {
  position: relative; isolation: isolate; display: grid; align-content: start; gap: 1rem; min-height: 24rem;
  max-width: var(--container-max); margin-inline: auto; padding: 1rem var(--gutter) 1.25rem;
}
@media (min-width: 768px) { .win95__desk { display: block; height: 40rem; min-height: 0; padding: 0; } }
.win95__icons { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.25rem; margin: 0; padding: 0; list-style: none; }
@media (min-width: 768px) { .win95__icons { position: absolute; top: 1rem; left: var(--gutter); grid-template-columns: 5.5rem; gap: 1.25rem; } }
.win95__icon {
  display: grid; justify-items: center; gap: 0.375rem; width: 100%; min-height: 4.5rem; padding: 0.375rem 0.25rem;
  border: 0; background: none; color: var(--win95-light); font: inherit; cursor: default;
}
.win95__icon-img { width: 2rem; height: 2rem; }
.win95__icon-label { padding: 0 0.1875rem; text-align: center; }
.win95__icon.is-selected .win95__icon-label { background: var(--win95-navy); }
.win95__icon.is-selected .win95__icon-img { filter: brightness(0.75) sepia(1) hue-rotate(185deg) saturate(3); }
.win95__icon:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }

/* Windows */
.win95__window { position: relative; display: flex; flex-direction: column; padding: 3px; background: var(--win95-face); box-shadow: var(--win95-frame); }
.win95__window[hidden], .win95__window:not(.is-front) { display: none; }
@media (min-width: 768px) {
  .win95__window {
    position: absolute; top: 0; left: 0; width: var(--win95-w, 26rem); max-width: calc(100% - 1rem); max-height: 100%;
    translate: var(--win95-x, 0) var(--win95-y, 0); transform-origin: 0 0;
  }
  .win95__window:not(.is-front):not([hidden]) { display: flex; }
  .win95__window.is-max { inset: 0; width: auto; max-width: none; translate: none; }
}

/* Title bar: lit navy-to-blue when active, darkened when inactive */
.win95__titlebar {
  position: relative; display: flex; align-items: center; gap: 2px; padding: 2px;
  background: linear-gradient(90deg, var(--win95-inactive) 0 60%, var(--win95-face)); color: var(--win95-light);
}
.win95__window.is-front .win95__titlebar { background: linear-gradient(90deg, var(--win95-navy), var(--win95-blue)); }
.win95__move {
  flex: 1; display: flex; align-items: center; gap: 0.375rem; min-width: 0; min-height: 2rem; padding: 0 0.25rem;
  border: 0; background: none; color: inherit; font: 700 0.875rem/1 var(--win95-font); text-align: left; cursor: default;
}
.win95__move span { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.win95__move:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: -3px; }
.win95__tip {
  position: absolute; top: calc(100% + 0.25rem); left: 1.5rem; z-index: 2; display: none; padding: 2px 5px;
  border: 1px solid var(--win95-ink); background: var(--win95-tip); color: var(--win95-ink); white-space: nowrap; pointer-events: none;
}
.win95__controls { display: flex; gap: 2px; }
.win95__ctl--close { margin-left: 2px; }
.win95__ctl {
  display: grid; place-items: center; width: 2rem; height: 2rem; padding: 0; border: 0;
  background: var(--win95-face); box-shadow: var(--win95-raised); color: var(--win95-ink);
}
.win95__ctl:active { box-shadow: var(--win95-pressed); }
.win95__ctl:active svg { translate: 1px 1px; }
.win95__ctl--max, .win95__g-restore, .win95__window.is-max .win95__g-max { display: none; }
.win95__window.is-max .win95__g-restore { display: block; }
@media (min-width: 768px) {
  .win95__move { min-height: 1.5rem; font-size: 0.8125rem; touch-action: none; }
  .win95__ctl { width: 1.5rem; height: 1.5rem; }
  .win95__ctl--max { display: grid; }
  .win95__titlebar:has(.win95__move:focus-visible) .win95__tip { display: block; }
}

/* Window content */
.win95__body { flex: 1; min-height: 0; overflow: auto; padding: 0.75rem; }
.win95__body--quote { display: grid; gap: 0.875rem; }
.win95__wizard { display: none; }
@media (min-width: 768px) {
  .win95__body--quote { grid-template-columns: 7.5rem minmax(0, 1fr); }
  .win95__wizard {
    display: grid; place-items: center; align-content: center; gap: 0.75rem; padding: 0.75rem;
    background: linear-gradient(180deg, var(--win95-navy), var(--win95-desk)); box-shadow: var(--win95-sunken);
    color: var(--win95-light); font-weight: 700; text-align: center;
  }
}
.win95__menubar { display: flex; gap: 0.875rem; padding: 0.25rem 0.375rem; }
.win95__statusbar { display: flex; gap: 2px; margin-top: 2px; }
.win95__statusbar span { flex: 1; min-width: 0; padding: 2px 5px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; box-shadow: inset 1px 1px var(--win95-shadow), inset -1px -1px var(--win95-light); }

/* Form controls */
.win95__form { display: grid; gap: 0.625rem; }
.win95__intro { margin: 0; }
.win95__row { display: grid; gap: 0.625rem; }
@media (min-width: 768px) { .win95__row { grid-template-columns: 1fr 1fr; } }
.win95__field { display: grid; gap: 0.25rem; }
.win95__input {
  width: 100%; min-height: 2.25rem; padding: 3px 5px; border: 0; border-radius: 0;
  background: var(--win95-light); box-shadow: var(--win95-sunken); color: var(--win95-ink); font: 1rem/1.3 var(--win95-font);
}
textarea.win95__input { min-height: 4.5rem; resize: vertical; }
@media (min-width: 768px) { .win95__input { min-height: 1.625rem; font-size: 0.8125rem; } }
.win95__input:focus-visible { outline: 2px solid var(--win95-ink); outline-offset: 1px; }
.win95__select { position: relative; display: block; }
.win95__select select { appearance: none; padding-right: 1.75rem; }
.win95__select::after {
  content: ""; position: absolute; top: 2px; right: 2px; bottom: 2px; width: 1.125rem; pointer-events: none;
  background: var(--win95-face); box-shadow: var(--win95-raised);
}
.win95__select::before {
  content: ""; position: absolute; top: 50%; right: calc(2px + 0.5625rem - 3.5px); z-index: 1; width: 7px; height: 4px; margin-top: -2px; pointer-events: none;
  background: var(--win95-ink);
  clip-path: polygon(0 0, 100% 0, 100% 25%, 85.7% 25%, 85.7% 50%, 71.4% 50%, 71.4% 75%, 57.1% 75%, 57.1% 100%, 42.9% 100%, 42.9% 75%, 28.6% 75%, 28.6% 50%, 14.3% 50%, 14.3% 25%, 0 25%);
}
.win95__group {
  display: flex; flex-wrap: wrap; gap: 0.125rem 1rem; min-width: 0; margin: 0.25rem 0 0; padding: 0.375rem 0.75rem 0.5rem;
  border: 1px solid var(--win95-shadow); box-shadow: inset 1px 1px var(--win95-light), 1px 1px var(--win95-light);
}
.win95__group legend { padding: 0 0.25rem; background: var(--win95-face); }
.win95__radio, .win95__check { display: inline-flex; align-items: center; gap: 0.375rem; min-height: 1.75rem; }
.win95__radio input {
  appearance: none; flex: none; width: 0.75rem; height: 0.75rem; margin: 0; border-radius: 50%;
  background: var(--win95-light); box-shadow: inset 1px 1px var(--win95-shadow), inset -1px -1px var(--win95-hilite), inset 2px 2px var(--win95-dark);
}
.win95__radio input:checked { background: radial-gradient(circle, var(--win95-ink) 0 2px, var(--win95-light) 2.5px); }
.win95__box { position: relative; display: inline-grid; place-items: center; }
.win95__box input { appearance: none; width: 0.8125rem; height: 0.8125rem; margin: 0; background: var(--win95-light); box-shadow: var(--win95-sunken); }
.win95__tick {
  position: absolute; width: 7px; height: 7px; visibility: hidden; pointer-events: none; background: var(--win95-ink);
  clip-path: polygon(85.71% 0, 100% 0, 100% 42.86%, 85.71% 42.86%, 85.71% 57.14%, 71.43% 57.14%, 71.43% 71.43%, 57.14% 71.43%, 57.14% 85.71%, 42.86% 85.71%, 42.86% 100%, 28.57% 100%, 28.57% 85.71%, 14.29% 85.71%, 14.29% 71.43%, 0 71.43%, 0 28.57%, 14.29% 28.57%, 14.29% 42.86%, 28.57% 42.86%, 28.57% 57.14%, 42.86% 57.14%, 42.86% 42.86%, 57.14% 42.86%, 57.14% 28.57%, 71.43% 28.57%, 71.43% 14.29%, 85.71% 14.29%);
}
.win95__box input:checked + .win95__tick { visibility: visible; }
.win95__radio input:focus-visible, .win95__box input:focus-visible { outline: 2px solid var(--win95-ink); outline-offset: 2px; }

/* Push buttons: the default button wears an extra ink frame; focus adds the dotted inner rectangle */
.win95__actions { display: flex; justify-content: flex-end; gap: 0.375rem; margin-top: 0.25rem; }
.win95__btn {
  position: relative; min-width: 5.5rem; min-height: 2.75rem; padding: 0.25rem 0.875rem; border: 0; border-radius: 0;
  background: var(--win95-face); box-shadow: var(--win95-raised); color: var(--win95-ink); font: inherit;
}
.win95__btn--default { box-shadow: 0 0 0 1px var(--win95-ink), var(--win95-raised); }
.win95__btn:active { box-shadow: var(--win95-pressed); padding: calc(0.25rem + 1px) 0.875rem calc(0.25rem - 1px) calc(0.875rem + 2px); }
.win95__btn--default:active { box-shadow: 0 0 0 1px var(--win95-ink), var(--win95-pressed); }
.win95__btn:focus-visible, .win95__ctl:focus-visible, .win95__task:focus-visible, .win95__start-btn:focus-visible { outline: 2px solid var(--win95-ink); outline-offset: 1px; }
.win95__btn:focus-visible::after { content: ""; position: absolute; inset: 4px; border: 1px dotted var(--win95-ink); pointer-events: none; }
@media (min-width: 768px) { .win95__btn { min-height: 1.75rem; } }

/* My Home and Recycle Bin contents */
.win95__files, .win95__trash { margin: 0; padding: 0.75rem; list-style: none; background: var(--win95-light); box-shadow: var(--win95-sunken); }
.win95__files { display: grid; grid-template-columns: repeat(auto-fill, minmax(5.5rem, 1fr)); gap: 0.875rem 0.5rem; }
.win95__files li { display: grid; justify-items: center; gap: 0.25rem; text-align: center; }
.win95__files b { display: block; }
.win95__trash { display: grid; gap: 0.375rem; min-height: 5rem; align-content: start; }
.win95__trash li { display: flex; align-items: center; gap: 0.375rem; }
.win95__note { margin: 0.625rem 0 0; }
.win95__note:empty { display: none; }

/* Scheduling dialog: paperwork arcs between folders; the bar fills in whole blocks */
.win95__flight { position: relative; display: flex; align-items: end; justify-content: space-between; height: 3.25rem; margin: 0.25rem 0.5rem 0.625rem; container-type: inline-size; }
.win95__paper { position: absolute; left: 1.5rem; bottom: 1.25rem; width: 0.625rem; height: 0.75rem; opacity: 0; background: var(--win95-light); box-shadow: inset 0 0 0 1px var(--win95-ink); }
.win95__window--progress.is-busy .win95__paper { animation: win95-fly 1.1s linear 4; }
.win95__status { margin: 0 0 0.5rem; }
.win95__meter { height: 1.25rem; padding: 3px; box-shadow: inset 1px 1px var(--win95-shadow), inset -1px -1px var(--win95-light); }
.win95__meter-fill {
  display: block; height: 100%;
  background: repeating-linear-gradient(90deg, var(--win95-navy) 0 0.5rem, transparent 0.5rem 0.625rem);
  clip-path: inset(0 calc(100% - var(--win95-p, 0) * 1%) 0 0);
}
@supports (width: round(down, 10px, 1px)) {
  .win95__meter-fill { clip-path: inset(0 calc(100% - round(down, var(--win95-p, 0) * 1%, 0.625rem)) 0 0); }
}
.win95__eta { margin: 0.625rem 0 0; }

/* Taskbar, Start menu (a native disclosure), tray clock */
.win95__taskbar { position: relative; z-index: 1; background: var(--win95-face); box-shadow: inset 0 1px var(--win95-hilite), inset 0 2px var(--win95-light); }
.win95__taskbar-inner { display: flex; align-items: center; gap: 0.25rem; max-width: var(--container-max); margin-inline: auto; padding: 0.25rem var(--gutter); }
.win95__start { position: relative; flex: none; }
.win95__start-btn {
  display: flex; align-items: center; gap: 0.25rem; min-height: 2.75rem; padding: 0 0.5rem; list-style: none; cursor: default;
  background: var(--win95-face); box-shadow: var(--win95-raised); font-weight: 700;
}
.win95__start-btn::-webkit-details-marker { display: none; }
.win95__start[open] > .win95__start-btn { box-shadow: var(--win95-pressed); }
.win95__menu { position: absolute; bottom: calc(100% + 0.25rem); left: 0; display: flex; width: max-content; max-width: calc(100vw - 2rem); padding: 3px; background: var(--win95-face); box-shadow: var(--win95-frame); }
.win95__banner {
  display: flex; align-items: baseline; padding: 0.5rem 0.25rem; writing-mode: vertical-rl; rotate: 180deg;
  background: linear-gradient(0deg, var(--win95-navy), var(--win95-blue)); color: var(--win95-face); font-size: 1.375rem; line-height: 1;
}
.win95__banner b { color: var(--win95-light); font-weight: 900; }
.win95__menu-list { min-width: 13rem; margin: 0; padding: 0; list-style: none; }
.win95__menu-list li[hidden] { display: none; }
.win95__menu-list li:not([hidden]) ~ .win95__menu-split { margin-top: 3px; padding-top: 3px; border-top: 1px solid var(--win95-shadow); box-shadow: inset 0 1px var(--win95-light); }
.win95__menu-item {
  display: flex; align-items: center; gap: 0.625rem; width: 100%; min-height: 2.5rem; padding: 0.25rem 1.5rem 0.25rem 0.375rem;
  border: 0; background: none; color: var(--win95-ink); font: inherit; text-align: left; text-decoration: none; cursor: default;
}
.win95__menu-item:hover, .win95__menu-item:focus-visible { background: var(--win95-navy); color: var(--win95-light); }
.win95__menu-item:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: -4px; }
.win95__tasks { display: flex; flex: 1; gap: 0.25rem; min-width: 0; margin: 0; padding: 0; list-style: none; }
.win95__tasks li { flex: 0 1 10rem; min-width: 0; }
.win95__tasks li[hidden] { display: none; }
.win95__task {
  display: flex; align-items: center; gap: 0.25rem; width: 100%; min-height: 2.75rem; padding: 0 0.375rem;
  border: 0; background: var(--win95-face); box-shadow: var(--win95-raised); color: var(--win95-ink); font: inherit; text-align: left;
}
.win95__task span { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.win95__task[aria-pressed="true"] {
  box-shadow: var(--win95-pressed); font-weight: 700;
  background: repeating-conic-gradient(var(--win95-light) 0 25%, var(--win95-face) 0 50%) 0 0 / 2px 2px;
}
.win95__tray {
  display: flex; flex: none; align-items: center; gap: 0.375rem; min-height: 1.75rem; padding: 0 0.5rem;
  box-shadow: inset 1px 1px var(--win95-shadow), inset -1px -1px var(--win95-light); white-space: nowrap; font-variant-numeric: tabular-nums;
}
.win95__clock[hidden] { display: none; }
@media (min-width: 768px) {
  .win95__start-btn, .win95__task { min-height: 1.75rem; }
  .win95__menu-item { min-height: 2.25rem; }
}

@media (prefers-reduced-motion: reduce) {
  .win95 *, .win95 *::before, .win95 *::after { animation: none !important; }
}
@keyframes win95-fly {
  0% { opacity: 1; transform: translate(0, 0) rotate(0deg); }
  50% { transform: translate(calc((100cqw - 4.5rem) / 2), -1.75rem) rotate(-120deg); }
  100% { opacity: 1; transform: translate(calc(100cqw - 4.5rem), 0) rotate(-240deg); }
}
```

## JS

```js
document.querySelectorAll('[data-win95]').forEach((root) => {
  const $ = (selector) => root.querySelector(selector);
  const [desk, start, progress, clock, meter] = ['desk', 'start', 'window--progress', 'clock', 'meter'].map((part) => $(`.win95__${part}`));
  const windows = [...root.querySelectorAll('.win95__window')];
  const [wide, reduce] = ['(min-width: 768px)', '(prefers-reduced-motion: reduce)'].map((query) => matchMedia(query));
  const task = (win) => $(`[data-win95-task="${win.id}"]`);
  const visible = (el) => Boolean(el?.getClientRects().length);
  const openers = new Map();
  let [z, pointer, drag] = [1, 'mouse', null];
  root.classList.add('win95--js');
  root.querySelectorAll('[data-win95-js]').forEach((el) => { el.hidden = false; el.inert = false; });

  // The topmost open window is active: lit title bar, pressed taskbar button
  const front = (win) => {
    if (win) win.style.zIndex = ++z;
    const top = windows.filter((w) => !w.hidden).sort((a, b) => b.style.zIndex - a.style.zIndex)[0];
    windows.forEach((w) => {
      w.classList.toggle('is-front', w === top);
      task(w)?.setAttribute('aria-pressed', String(w === top));
      if (task(w)) task(w).parentElement.hidden = w.hidden && !w.classList.contains('is-min');
    });
  };
  const open = (win, from) => {
    if (from) openers.set(win, from);
    win.hidden = false;
    win.classList.remove('is-min');
    front(win);
    (win.querySelector('[data-win95-focus]') || win.querySelector('.win95__move')).focus();
  };
  // Close or minimise, then hand focus back: taskbar button, opener, desktop icon or Start
  const close = (win, min) => {
    clearInterval(win.timer);
    win.hidden = true;
    win.classList.toggle('is-min', Boolean(min));
    front();
    const back = min ? task(win) : openers.get(win);
    (visible(back) ? back : $(`.win95__icon[data-win95-open="${win.id}"]`) || start.firstElementChild).focus();
  };
  // Minimise and restore fly between the window and its taskbar button, as in 1995
  const fly = (win, reverse) => {
    const to = task(win);
    if (reduce.matches || !visible(to)) return Promise.resolve();
    const [a, b] = [win, to].map((el) => el.getBoundingClientRect());
    const frames = [{ transform: 'none', opacity: 1 }, { transform: `translate(${b.left - a.left}px, ${b.top - a.top}px) scale(${b.width / a.width}, ${b.height / a.height})`, opacity: 0.3 }];
    return win.animate(reverse ? frames.reverse() : frames, { duration: 260, easing: 'cubic-bezier(0.16, 1, 0.3, 1)' }).finished;
  };
  const maximise = (win) => {
    if (!wide.matches) return;
    const max = win.classList.toggle('is-max');
    win.querySelector('[data-win95-act="max"]')?.setAttribute('aria-label', max ? 'Restore' : 'Maximize');
  };
  // Desktop-relative position, clamped so a strip of title bar always stays reachable
  const pos = (win) => { const [a, d] = [win, desk].map((el) => el.getBoundingClientRect()); return [a.left - d.left, a.top - d.top]; };
  const place = (win, x, y) => {
    win.style.setProperty('--win95-x', `${Math.round(Math.min(desk.clientWidth - 64, Math.max(64 - win.offsetWidth, x)))}px`);
    win.style.setProperty('--win95-y', `${Math.round(Math.min(desk.clientHeight - 32, Math.max(0, y)))}px`);
  };
  root.addEventListener('pointerdown', (event) => {
    pointer = event.pointerType;
    const win = event.target.closest('.win95__window');
    const bar = event.target.closest('.win95__move');
    if (win) front(win);
    if (!bar || !wide.matches || event.button !== 0 || win.classList.contains('is-max')) return;
    const [x, y] = pos(win);
    drag = { win, x, y, x0: event.clientX - x, y0: event.clientY - y };
    bar.setPointerCapture(event.pointerId);
  });
  root.addEventListener('pointermove', (event) => {
    if (!drag) return;
    drag.x = event.clientX - drag.x0;
    drag.y = event.clientY - drag.y0;
    drag.frame ||= requestAnimationFrame(() => { if (drag) { place(drag.win, drag.x, drag.y); drag.frame = 0; } });
  }, { passive: true });
  ['pointerup', 'pointercancel'].forEach((type) => root.addEventListener(type, () => { drag = null; }));

  // Escape closes the Start menu, else the focused window; arrows move a focused title bar (Shift: 32px)
  root.addEventListener('keydown', (event) => {
    const win = event.target.closest('.win95__window');
    if (event.key === 'Escape' && start.open) { start.open = false; start.firstElementChild.focus(); return; }
    if (event.key === 'Escape' && win) { close(win); return; }
    const step = { ArrowLeft: [-1, 0], ArrowRight: [1, 0], ArrowUp: [0, -1], ArrowDown: [0, 1] }[event.key];
    if (!step || !event.target.matches('.win95__move') || !wide.matches || win.classList.contains('is-max')) return;
    event.preventDefault();
    const [x, y] = pos(win);
    const by = event.shiftKey ? 32 : 8;
    place(win, x + step[0] * by, y + step[1] * by);
  });
  // One handler for icons, Start items, title bars, window buttons and taskbar buttons
  root.addEventListener('click', (event) => {
    const el = event.target.closest('[data-win95-open], [data-win95-act], [data-win95-task], .win95__move');
    root.querySelectorAll('.win95__icon').forEach((icon) => icon.classList.toggle('is-selected', icon === el));
    if (!el) return;
    const id = el.dataset.win95Open || el.dataset.win95Task;
    const win = id ? $(`#${id}`) : el.closest('.win95__window');
    let act = el.dataset.win95Act;
    // Mouse: one click selects an icon, a double-click (detail 2) opens it; keys, touch and AT open at once
    if (el.dataset.win95Task) act = win.classList.contains('is-front') ? 'min' : 'restore';
    else if (id) act = el.matches('.win95__icon') && pointer === 'mouse' && event.detail === 1 ? '' : 'open';
    else if (!act && event.detail !== 1) act = 'max';
    if (act === 'open') { start.open = false; open(win, el); }
    if (act === 'restore') { const was = win.hidden; open(win); if (was) fly(win, true); }
    if (act === 'min') fly(win).then(() => close(win, true));
    if (act === 'max') maximise(win);
    if (act === 'close') close(win);
    if (act === 'empty') {
      win.querySelector('.win95__trash').replaceChildren();
      win.querySelector('.win95__note').textContent = 'Recycle Bin is empty. Brand hauls away old fixtures for free.';
      root.classList.add('is-empty');
    }
  });
  root.addEventListener('focusin', (event) => {
    const win = event.target.closest('.win95__window');
    if (win && !win.classList.contains('is-front')) front(win);
  });

  // Send opens the scheduling dialog: the bar fills in random-sized chunks, then confirms the booking
  $('.win95__form').addEventListener('submit', (event) => {
    event.preventDefault();
    const say = (text, label) => { $('.win95__status').textContent = text; progress.querySelector('[data-win95-focus]').textContent = label; };
    const fill = (done) => { meter.style.setProperty('--win95-p', done); meter.setAttribute('aria-valuenow', done); };
    let done = 0;
    fill(0);
    say('Finding the nearest technician…', 'Cancel');
    progress.classList.add('is-busy');
    open(progress, event.submitter);
    clearInterval(progress.timer);
    progress.timer = setInterval(() => {
      fill(done = reduce.matches ? 100 : Math.min(100, done + 5 * (1 + Math.floor(Math.random() * 3))));
      if (done < 100) return;
      clearInterval(progress.timer);
      progress.classList.remove('is-busy');
      say('Booked! Sam K. from Westlake will call you within 15 minutes.', 'OK');
      event.target.reset();
    }, 180);
  });
  // Start is a native <details> disclosure; outside clicks and tabbing away also close it
  document.addEventListener('click', (event) => { if (!start.contains(event.target)) start.open = false; });
  start.addEventListener('focusout', (event) => { if (event.relatedTarget && !start.contains(event.relatedTarget)) start.open = false; });

  const tick = () => { const now = new Date(); clock.dateTime = now.toISOString(); clock.textContent = now.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' }); };
  tick();
  setInterval(tick, 15000);
  front(windows.find((w) => !w.hidden));
});
```

## Notes

- Each window is a non-modal `role="dialog"` named by its title. Opening a window moves focus into it (to the first field for the quote form), and closing returns focus to whatever opened it, or to the taskbar button after a minimise. Escape closes the focused window. A focused title bar is a button that moves the window with the arrow keys (Shift for 32px steps) and maximises on Enter; a Win95 yellow tooltip says so, and the same text is its `aria-describedby`. Desktop icons open on Enter or Space, a single tap, or a mouse double-click (a single mouse click only selects, as in 1995).
- The Start menu is a native `<details>` disclosure: never `role="menu"`, no arrow-key trap. It also closes on Escape, an outside click or tabbing away. Taskbar buttons are toggles (`aria-pressed`) for the active window. The scheduling dialog's progress bar is a real `role="progressbar"`, and its outcome is announced through `role="status"`.
- Without JS, the quote window is open with a working form (point `action` at your endpoint), the Start menu still opens and shows the phone and email links, and the JS-only chrome (icons, window buttons, taskbar button) is `inert` until the script wires it.
- Contrast: white title text is at least 6.5:1 across the first 70% of the navy→blue bar, and inactive bars start at #606060 (6.3:1; Win98's own grey-on-grey was 2.2:1). Ink on face grey is 11.5:1, icon labels on teal 4.8:1, tooltip 20.6:1. Focus rings are ink on grey (11.5:1) and `--text-inverse` on teal or navy (4.6:1 or more), because `--primary` would be 1.1–2.8:1 here.
- Under reduced motion, the minimise flight and paperwork loop are skipped and the progress bar jumps straight to done. The flight uses the individual `translate` property for position, so WAAPI `transform` composes on top. Whole-block progress uses CSS `round()` inside `@supports`, with smooth clipping as the fallback. Adding a window is mostly copy-and-paste: a `.win95__window` with an id, an icon or menu item with `data-win95-open`, and an optional taskbar `<li>`. The JS is scoped per desktop, but the `win95-*` ids are not, so a second desktop on the same page needs its own id prefix.
