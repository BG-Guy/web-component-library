"""Build a single-page live gallery of every pattern in the component library.

Usage: python3 -I build_gallery.py <repo-root> <shell.html> <out.html>
Parses components/*.md, extracts each pattern's HTML/CSS/JS, swaps image paths
for labelled SVG placeholders, and embeds everything as JSON into the shell page.
"""
import hashlib
import json
import re
import sys
import urllib.parse
from pathlib import Path

PREMIUM_GROUPS = [
    ("Navigation & menus", ["floating-navbar", "morphing-dropdown", "split-menu", "curtain-menu", "perspective-menu",
                            "gooey-menu", "radial-menu", "dock-nav", "notch-tabbar", "island-nav", "swipe-drawer",
                            "drilldown-menu", "command-palette"]),
    ("Heroes", ["aurora-hero", "beam-grid-hero", "search-hero", "tilted-wall-hero", "orbit-hero", "reel-hero", "xray-hero"]),
    ("Headlines & type", ["kinetic-headline", "scramble-text", "weight-wave", "fill-text", "path-text", "circle-text"]),
    ("Scroll stories", ["scroll-timeline", "sticky-showcase", "horizontal-scroll", "zoom-through", "stacking-cards",
                        "text-mask-zoom", "wipe-gallery", "velocity-marquee", "column-parallax", "focus-list",
                        "depth-tunnel", "scroll-compare", "blueprint-draw", "parallax-scene"]),
    ("Blending sections", ["chameleon-sections", "blend-text", "section-stack", "seam-melt", "liquid-divider",
                           "curtain-split", "overlap-glass", "card-morph"]),
    ("Content sections", ["bento-grid", "feature-tabs", "stat-counters", "pricing-plans", "smooth-accordion",
                          "logo-marquee", "testimonial-wall"]),
    ("Cards & galleries", ["drag-carousel", "lightbox-gallery", "holo-card", "swipe-deck", "expand-panels",
                           "hover-preview-list", "coverflow", "wallet-pass", "hotspot-explorer", "crew-cards",
                           "infinite-canvas", "folder-stack"]),
    ("Forms & booking", ["floating-label-form", "quote-wizard", "booking-calendar", "estimate-calculator",
                         "coverage-checker", "job-tracker", "otp-input", "file-drop", "star-rating"]),
    ("Feedback & utilities", ["premium-buttons", "spring-modal", "toast-stack", "chat-widget", "confetti",
                              "theme-switch", "custom-cursor"]),
    ("Retro", ["crt-terminal", "pixel-arcade", "win95-window", "synthwave-hero", "vhs-glitch", "neo-brutalist",
               "swiss-poster", "groovy-70s", "skeuo-thermostat", "split-flap"]),
    ("Footers", ["cta-footer", "reveal-footer", "circle-footer", "type-footer", "unfold-footer", "curve-footer",
                 "marquee-footer"]),
]
GROUPS = [(f"Premium · {name}", [f"premium/{stem}" for stem in stems]) for name, stems in PREMIUM_GROUPS] + [
    ("Navigation", ["navigation", "navbar-variants", "mobile-navigation", "tabs-and-wayfinding"]),
    ("Page sections", ["heroes", "trust-and-stats", "cards-and-grids", "card-variants", "content-blocks",
                       "process-steps", "gallery", "carousels", "faq", "cta-sections", "footer", "footer-variants"]),
    ("Controls and feedback", ["buttons", "forms", "form-controls", "feedback", "modals"]),
    ("Visual effects", ["backgrounds", "animations", "transitions"]),
]

# Full-bleed modules render edge to edge; everything else gets a padded demo container.
RAW_FILES = {"navigation", "navbar-variants", "mobile-navigation", "heroes", "footer", "footer-variants",
             "backgrounds", "cta-sections"}
RAW_PATTERNS = {("carousels", 4), ("animations", 3), ("animations", 4), ("feedback", 3), ("feedback", 4)}

# Preview frame behaviour: fixed-height frames scroll internally so sticky, fixed and
# scroll-driven patterns can be seen working; "filler" adds placeholder page content.
FRAME = {
    ("navigation", 1): dict(mode="fixed", h=560, filler="after"),
    ("animations", 1): dict(mode="fixed", h=560, filler="before"),
    ("animations", 2): dict(mode="fixed", h=560, filler="before"),
    ("animations", 3): dict(mode="fixed", h=520, filler="after"),
    ("animations", 4): dict(mode="fixed", h=560, filler="after"),
    ("tabs-and-wayfinding", 6): dict(mode="fixed", h=600),
    ("tabs-and-wayfinding", 7): dict(mode="fixed", h=520, filler="after"),
    ("buttons", 9): dict(mode="fixed", h=480, filler="after"),
    ("cta-sections", 2): dict(mode="fixed", h=600, filler="after", width="phone"),
    ("feedback", 2): dict(mode="auto", min=380),
    ("feedback", 4): dict(mode="auto", min=380),
    ("modals", 1): dict(mode="auto", min=520),
}
PREMIUM_WRAP = {"morphing-dropdown"}
PREMIUM_FRAME = {
    "floating-navbar": dict(mode="fixed", h=560, filler="after"),
    "morphing-dropdown": dict(mode="auto", min=560),
    "kinetic-headline": dict(mode="fixed", h=640, filler="after"),
    "scroll-timeline": dict(mode="fixed", h=680),
    "sticky-showcase": dict(mode="fixed", h=680),
    "toast-stack": dict(mode="auto", min=460),
    "spring-modal": dict(mode="auto", min=660),
    "lightbox-gallery": dict(mode="auto", min=600),
    # Round 2: scroll-driven and pinned demos scroll inside a fixed frame
    **{stem: dict(mode="fixed", h=680) for stem in [
        "horizontal-scroll", "zoom-through", "stacking-cards", "text-mask-zoom", "wipe-gallery",
        "velocity-marquee", "column-parallax", "focus-list", "depth-tunnel", "scroll-compare",
        "blueprint-draw", "parallax-scene", "liquid-divider", "seam-melt", "curtain-split",
        "chameleon-sections", "blend-text", "section-stack", "path-text", "fill-text",
        "reveal-footer", "circle-footer", "type-footer", "unfold-footer", "curve-footer", "marquee-footer"]},
    # Page-level menus and widgets designed for a phone
    **{stem: dict(mode="fixed", h=640, width="phone") for stem in [
        "gooey-menu", "radial-menu", "perspective-menu", "curtain-menu", "swipe-drawer", "chat-widget"]},
    "notch-tabbar": dict(mode="fixed", h=560, width="phone"),
    "island-nav": dict(mode="fixed", h=600, width="phone"),
    "drilldown-menu": dict(mode="fixed", h=600, width="phone"),
    "split-menu": dict(mode="fixed", h=640),
    "dock-nav": dict(mode="fixed", h=520),
    "circle-text": dict(mode="fixed", h=600),
    "infinite-canvas": dict(mode="fixed", h=600),
    "card-morph": dict(mode="auto", min=660),
    "command-palette": dict(mode="auto", min=560),
    "search-hero": dict(mode="auto", min=600),
}
FILE_FRAME = {
    "navbar-variants": dict(mode="fixed", h=560, filler="after"),
    "mobile-navigation": dict(mode="fixed", h=680, filler="after", width="phone"),
}

FENCE = re.compile(r"^```(\w+)\n(.*?)^```", re.M | re.S)
PALETTE = [
    ("#0f2a4a", "#1d6fa5", "#5eead4", "#f59e0b"), ("#1f3b2c", "#4d7c0f", "#bef264", "#fde68a"),
    ("#4a1d1d", "#c2410c", "#fdba74", "#fef3c7"), ("#0b1324", "#334155", "#94a3b8", "#60a5fa"),
    ("#123c3a", "#0d9488", "#99f6e4", "#fef9c3"), ("#2a1b3d", "#be185d", "#fda4af", "#fcd34d"),
    ("#1e293b", "#2563eb", "#93c5fd", "#5eead4"), ("#3a2a12", "#a16207", "#fcd34d", "#fff7ed"),
]
BEFORE = ("#3f3a33", "#78716c", "#d6d3d1", "#a8a29e")
AFTER = ("#0f3b39", "#0d9488", "#ccfbf1", "#fef9c3")


def inline_md(text):
    """Escape, then render `code` and **bold** for descriptions."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)


def placeholder(name, w, h):
    base = re.sub(r"-(large|thumb)(?=\.)", "", name.rsplit("/", 1)[-1])
    if "before" in base:
        c1, c2, c3, c4 = BEFORE
    elif "after" in base:
        c1, c2, c3, c4 = AFTER
    else:
        c1, c2, c3, c4 = PALETTE[int(hashlib.md5(base.encode()).hexdigest(), 16) % len(PALETTE)]
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}'><defs>"
           f"<linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='{c1}'/><stop offset='1' stop-color='{c2}'/></linearGradient>"
           f"<radialGradient id='a' cx='.78' cy='.22' r='.62'><stop offset='0' stop-color='{c3}' stop-opacity='.85'/><stop offset='1' stop-color='{c3}' stop-opacity='0'/></radialGradient>"
           f"<radialGradient id='b' cx='.18' cy='.88' r='.55'><stop offset='0' stop-color='{c4}' stop-opacity='.6'/><stop offset='1' stop-color='{c4}' stop-opacity='0'/></radialGradient>"
           f"</defs><rect width='{w}' height='{h}' fill='url(#g)'/><rect width='{w}' height='{h}' fill='url(#a)'/><rect width='{w}' height='{h}' fill='url(#b)'/>")
    if w >= 140:
        size = max(9, min(h * 0.055, w / 18, 16))
        svg += (f"<text x='{w * 0.05:.0f}' y='{h - size * 1.2:.0f}' font-family='system-ui,sans-serif' font-size='{size:.0f}' "
                f"fill='white' fill-opacity='.72'>{base}</text>")
    return "data:image/svg+xml," + urllib.parse.quote(svg + "</svg>")


IMG_EXT = r"\.(?:jpe?g|png|webp|avif|gif|svg)"


def attr(tag, name):
    m = re.search(rf'\b{name}="(\d+)"', tag)
    return int(m.group(1)) if m else None


def swap_assets(html):
    """Replace local image paths with placeholders and neutralise external iframes."""
    def fix_tag(m):
        tag = m.group(0)
        w, h = attr(tag, "width") or 800, attr(tag, "height") or 600

        def repl(a):
            val = a.group(2)
            if re.match(r"(data:|https?:|#|about:)", val) or not re.search(IMG_EXT + r"$", val):
                return a.group(0)
            return f'{a.group(1)}="{placeholder(val, w, h)}"'
        return re.sub(r'\b(src|poster)="([^"]+)"', repl, tag)
    html = re.sub(r"<(?:img|video)\b[^>]*>", fix_tag, html, flags=re.S)
    # Links straight to a large image (lightboxes): match the inner thumbnail's artwork
    def fix_link(m):
        tag, inner = m.group(1), m.group(2)
        img = re.search(r"<img\b[^>]*>", inner)
        w, h = (attr(img.group(0), "width") or 800, attr(img.group(0), "height") or 600) if img else (800, 600)
        tag = re.sub(r'href="([^"]+' + IMG_EXT + r')"', lambda a: f'href="{placeholder(a.group(1), w * 2, h * 2)}"', tag)
        return tag + inner
    html = re.sub(r"(<a\b[^>]*>)(.*?</a>)", fix_link, html, flags=re.S)
    # Image paths that scripts copy into an <img> later (e.g. thumbnail buttons)
    html = re.sub(r'\bdata-src="([^"]+' + IMG_EXT + r')"',
                  lambda m: f'data-src="{placeholder(m.group(1), 1200, 800)}"', html)
    return re.sub(r'(<iframe\b[^>]*?\bsrc=")https?://[^"]*(")', r"\1about:blank\2", html, flags=re.S)


def swap_css_urls(css):
    return re.sub(r"url\((['\"]?)([^)'\"]+" + IMG_EXT + r")\1\)",
                  lambda m: f'url("{placeholder(m.group(2), 800, 600)}")', css)


def js_lines(js):
    return sum(1 for ln in js.splitlines() if ln.strip() and not ln.strip().startswith("//"))


def subsections(text, level):
    """Split text on headings of the given level; returns [(heading, body)], preamble first."""
    parts = re.split(rf"^{'#' * level} (.+)$", text, flags=re.M)
    out = [("", parts[0])]
    out += [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]
    return out


def blocks(text, lang):
    return [b for lg, b in FENCE.findall(text) if lg == lang]


def prose(text):
    """First paragraphs of prose before any code or list, as one line."""
    text = FENCE.sub("", text)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    keep = [p for p in paras if not p.startswith(("-", "|", "#"))]
    return " ".join(" ".join(p.split()) for p in keep)


def file_intro(text):
    body = re.split(r"^## ", text, maxsplit=1, flags=re.M)[0]
    body = re.sub(r"^\*\*Fonts:\*\*.*$", "", body, flags=re.M)
    body = re.sub(r"^# .*$", "", body, count=1, flags=re.M)
    desc = prose(body)
    desc = re.sub(r"\s*Depends on `tokens/variables\.css`\.?", "", desc)
    bullets = re.findall(r"^- (.+)$", body, flags=re.M)
    return desc, bullets


FONT_URL = re.compile(r"https://fonts\.googleapis\.com/css2\?[^\s)>`'\"]+")


def make_pattern(stem, n, title, desc, html, css, js_list, raw, chips, premium=False, fonts=()):
    cfg = dict(mode="auto", min=140, max=1600 if premium else 900, filler=None, width="full")
    if premium:
        cfg.update(PREMIUM_FRAME.get(stem, {}))
        wrap = stem in PREMIUM_WRAP
    else:
        cfg.update(FILE_FRAME.get(stem, {}))
        cfg.update(FRAME.get((stem, n), {}))
        wrap = stem not in RAW_FILES and (stem, n) not in RAW_PATTERNS
    return dict(id=f"{stem}-{n}", n=n, title=title, desc=inline_md(desc), chips=chips, wrap=wrap, cfg=cfg,
                html=swap_assets(html), css=swap_css_urls(css), js=js_list, raw=raw, fonts=list(fonts))


def parse_multi(stem, text):
    sections = subsections(text, 2)[1:]
    pats, base = [], None
    for heading, body in sections:
        m = re.match(r"(\d+)\.\s+(.+)", heading)
        if not m:
            continue
        n, title = int(m.group(1)), m.group(2).strip()
        subs = subsections(body, 3)
        desc = prose(subs[0][1])
        get = lambda key, lang: "\n".join(b for h, s in subs if h.upper().startswith(key) for b in blocks(s, lang))
        html, css, js = get("HTML", "html"), get("CSS", "css"), get("JS", "js")
        raw = dict(html=html, css=css, js=js)
        if n == 1:
            base = raw
        chips = [f"JS · {js_lines(js)} lines" if js else "No JS"]
        css_all, js_all = css, [js] if js else []
        if "Builds on 1." in desc and base and n != 1:
            chips.append("Builds on #1")
            css_all = base["css"] + "\n" + css
            js_all = ([base["js"]] if base["js"] else []) + js_all
        pats.append(make_pattern(stem, n, title, desc, html, css_all, js_all, raw, chips))
    return pats


def parse_single(stem, text, file_title, premium=False):
    desc, bullets = file_intro(text)
    secs = {h.split()[0].upper(): b for h, b in subsections(text, 2)[1:] if h}
    css = "\n".join(blocks(secs.get("CSS", ""), "css"))
    js = "\n".join(blocks(secs.get("JS", ""), "js"))
    chips = [f"JS · {js_lines(js)} lines" if js else "No JS"]
    html_subs = [(h, b) for h, b in subsections(secs.get("HTML", ""), 3)[1:] if blocks(b, "html")]
    if not html_subs:
        html = "\n".join(blocks(secs.get("HTML", ""), "html"))
        fonts = FONT_URL.findall(text.split("## HTML")[0]) if premium else []
        return [make_pattern(stem, 1, file_title, desc, html, css, [js] if js else [],
                             dict(html=html, css=css, js=js), chips, premium, fonts)]
    pats = []
    for i, (heading, body) in enumerate(html_subs, 1):
        key = re.sub(r"^[A-Z]\.\s*", "", heading).split()[0].lower()
        match = next((b for b in bullets if re.sub(r"^\*\*([A-Z]\.\s*)?", "", b).lower().startswith(key)), "")
        sub_desc = re.sub(r"^\*\*[^*]+\*\*\s*", "", match) or desc
        extra = prose(body)
        html = "\n".join(blocks(body, "html"))
        title = re.sub(r"^[A-Z]\.\s*", "", heading)
        pats.append(make_pattern(stem, i, title, (sub_desc + " " + extra).strip(), html, css,
                                 [js] if js else [], dict(html=html, css=css, js=js), chips))
    return pats


def main():
    root, shell_path, out_path = map(Path, sys.argv[1:4])
    data = dict(tokens=(root / "tokens/variables.css").read_text(), groups=[])
    total = 0
    for group, stems in GROUPS:
        files = []
        for rel in stems:
            stem = rel.split("/")[-1]
            premium = rel.startswith("premium/")
            text = (root / "components" / f"{rel}.md").read_text()
            title = re.search(r"^# (.+)$", text, re.M).group(1).strip()
            desc, _ = file_intro(text)
            multi = re.search(r"^## 1\. ", text, re.M)
            pats = parse_multi(stem, text) if multi else parse_single(stem, text, title, premium)
            total += len(pats)
            files.append(dict(stem=stem, title=title, desc=inline_md(desc), path=f"components/{rel}.md",
                              patterns=pats))
        data["groups"].append(dict(name=group, files=files))
    data["total"] = total
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = shell_path.read_text().replace("__DATA__", payload).replace("__TOTAL__", str(total)).replace("__FILES__", str(sum(len(g["files"]) for g in data["groups"])))
    out_path.write_text(out)
    print(f"{total} patterns, {sum(len(g['files']) for g in data['groups'])} files, "
          f"{len(out.encode()) / 1024:.0f} KB -> {out_path}")


if __name__ == "__main__":
    main()
