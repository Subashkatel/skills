# Dual-backend slide builder pattern

One layout spec drives two renderers: python-pptx (the deliverable — native vector text, editable) and matplotlib (preview PNGs for visual QA). Runnable example: `scripts/example_builder.py` in this skill. Deps: `pip install python-pptx matplotlib` (python-pptx pulls lxml and Pillow); on locked-down machines install to a local dir and set `PYTHONPATH`.

## Skeleton

```python
class SlideCanvas:
    """Every primitive draws to BOTH backends with identical inch coordinates."""
    def __init__(self, pptx_slide, mpl_ax):
        self.shapes, self.ax, self._z = pptx_slide.shapes, mpl_ax, 2.0
    def _next_z(self):           # matplotlib paints in call order, like pptx
        self._z += 0.01; return self._z
    def box(self, x, y, w, h, fill, edge=None, radius=0.05, dash=None): ...
    def text(self, x, y, w, h, s, size, color, bold=False,
             align="left", valign="top", leading=1.2): ...
    def line(self, x1, y1, x2, y2, color, width, dash=None, arrow=False): ...
```

Key mechanics:

- Canvas 13.333 × 7.5 in; mpl axes `xlim(0, 13.333)`, `ylim(7.5, 0)` (y inverted) so coordinates match pptx inches 1:1; save previews at dpi ≥ 180.
- pptx text: `add_textbox`, zero margins, `word_wrap=True`, one run per line, `paragraph.line_spacing = leading`. Font sizes only from the modular scale.
- Letterspacing (caps titles, lane labels): pptx `run._r.get_or_add_rPr().set("spc", str(int(tracking*size*100)))` (hundredths of a point; 5–10% of size). Preview approximates with U+200A hair-space joins. Pass caps strings pre-uppercased — `.upper()` corrupts µ → Μ.
- Serif face: the pptx just names "Palatino Linotype" (the viewer's machine resolves it — portable by construction). Only the preview needs a local file: discover a Palatino-class face (URW P052 OTFs under `/usr/share/fonts/urw-base35` on many Linux systems; Palatino/Book Antiqua on macOS/Windows) and register it via `font_manager.fontManager.addfont`, falling back to DejaVu Serif — `_register_preview_serif()` in the example builder does exactly this. P052 has µ → τ × – but NO fleuron ❧.
- pptx arrowheads/dashes need raw XML on the line element: append `a:tailEnd type="triangle"` / `a:prstDash val="dash"` via `etree.SubElement(line._get_or_add_ln(), qn(...))` (prstDash before tailEnd).
- Disable shape shadows (`shape.shadow.inherit = False`).
- Pass `zorder=self._next_z()` to every mpl patch/line so gridlines drawn first stay under bars.
- Rounded-rect radius: `shape.adjustments[0] = radius / min(w, h)`.

## Layout constants that work

- Margins 0.7 in each side (content width 11.93); title at y ≈ 0.45, size 30 bold, centered.
- Component boxes ~2.0 × 1.05 in, gaps ≥ 0.5 in so hop labels fit between; name 15 pt bold, sublabel 10.5 pt.
- Timeline bars ~0.42 in tall with 2 px white seams between touching bars; direct labels on/above every bar; axis ticks 10.5 pt muted.
- Small labels: never let centered text spill across a marker line — right-align text ending just before the line instead.

## Verify

- Rebuild → Read every preview PNG → fix collisions → repeat until clean.
- Sanity-check the pptx: open with python-pptx, count slides and non-empty text boxes.
