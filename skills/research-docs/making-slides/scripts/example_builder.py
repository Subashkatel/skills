"""Reference slide builder for the making-slides skill (self-contained).

Demonstrates the full pattern on a real 4-slide deck (a QEC control-loop
simulator example): dual pptx+matplotlib backends, modular type scale,
letterspaced caps titles, ink-only text with color reserved for data marks.
Usage: python example_builder.py [out.pptx] [preview_dir]

Original deck notes follow.

Style follows the user's examples (Dally "Hardware for Deep Learning" Hot Chips
deck, Fan BAICS talk): plain white slides, one centered bold title, ONE focal
element per slide, numbers annotated directly on the diagram, no boxed panels,
kickers, or footers.

Every number on these slides comes from one actual run:

    simulate(RunSpec(ops=cnot_plus_two_t_circuit(),
                     decoder=PerRoundDecoder(tau_us=1.0)), verbose=True)

Trace landmarks (microseconds):
    Op0 CNOT rounds 0.000-6.600 (6 x 1.1), Op1 T 6.600-9.900 (3 x 1.1)
    round hop: fires 1.100 -> controller 1.250 (t_qc) -> decoder 3.250 (t_cd)
    decodes: Op0 W0 8.750-14.750, Op0 W1 15.250-21.250,
             Op1 W0 21.750-27.750 (ready = 21.250 + t_dd 0.5),
             Op2 W0 38.350-44.350
    Op0 result 22.250: Pauli-frame update only (Clifford, no QPU instruction)
    Op1 decision: publish 28.750 (t_do) -> controller 32.750 (t_oc)
                  -> chip 32.900 (t_cq); Op2 starts, stalled since 9.900
    chip_done 36.200, fully_done 45.350
    scoreboard: 4 windows, 20 idle memory rounds, peak 9 payloads buffered

Text is written as native pptx text boxes (crisp at any zoom, editable) and the
same layout is mirrored to high-dpi PNG previews with matplotlib.
"""
from pathlib import Path
import glob
import sys

try:
    from lxml import etree
    from pptx import Presentation
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
    from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
    from pptx.oxml.ns import qn
    from pptx.util import Inches, Pt
except ImportError as error:
    raise SystemExit(f"{error}\nInstall the deck dependencies first: "
                     "pip install python-pptx (pulls lxml and Pillow)")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch


def _register_preview_serif():
    """Find a Palatino-class serif for the preview; fall back gracefully.

    The pptx itself just names "Palatino Linotype" — the viewer's machine
    resolves it. Only the matplotlib preview needs a real local font file.
    """
    for pattern in ("/usr/share/fonts/urw-base35/P052-*.otf",     # Linux URW
                    "/usr/share/fonts/**/P052*.otf"):
        files = glob.glob(pattern, recursive=True)
        if files:
            for font_file in files:
                font_manager.fontManager.addfont(font_file)
            return ["P052", "DejaVu Serif"]
    installed = {f.name for f in font_manager.fontManager.ttflist}
    for family in ("Palatino Linotype", "Palatino", "Book Antiqua",
                   "URW Palladio L"):
        if family in installed:
            return [family, "DejaVu Serif"]
    return ["DejaVu Serif"]                       # always present with mpl


matplotlib.rcParams["font.family"] = _register_preview_serif()

OUT_PPTX = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("slides.pptx")
PREVIEW_DIR = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("slide_previews")

PAGE_W, PAGE_H = 13.333, 7.5

# validated palette (dataviz reference, light mode), slots 1-3 in fixed order
BLUE = "#2a78d6"    # QPU / forward path
AQUA = "#1baf7a"    # decoder
YELLOW = "#eda100"  # feedback / decision
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#8a887f"
STALL_FILL = "#f1f0ec"
STALL_EDGE = "#9b998f"
WHITE = "#ffffff"

# One versatile family (Bringhurst 6.5.1; Proportional Web §1.1.1): Palatino.
# Office renders Palatino Linotype; Linux substitutes URW P052 by metrics.
FONT = "Palatino Linotype"

# Modular type scale (Bringhurst 3.1.1 "don't compose without a scale";
# Proportional Web fractions of a 12 pt root: 7/8, 1, 9/8, 5/4, 3/2, 2, 5/2, 3).
# Every text size on these slides is one of these steps.
SIZE_XS, SIZE_S, SIZE_M, SIZE_L, SIZE_XL = 10.5, 12, 13.5, 15, 18
SIZE_STAT, SIZE_TITLE = 24, 30
CAPS_TRACKING = 0.07   # letterspacing for strings of capitals (2.1.6: 5-10%)


def _rgb(hex_color):
    return RGBColor.from_string(hex_color.lstrip("#"))


class SlideCanvas:
    """One slide drawn to both backends: pptx shapes and a matplotlib mirror."""

    def __init__(self, pptx_slide, mpl_ax):
        self.shapes = pptx_slide.shapes
        self.ax = mpl_ax
        self._z = 2.0

    def _next_z(self):
        """Monotonic zorder so matplotlib paints in call order, like pptx."""
        self._z += 0.01
        return self._z

    # ------------------------------------------------------------ primitives

    def box(self, x, y, w, h, fill=WHITE, edge=None, edge_w=1.25,
            radius=0.05, dash=None):
        shape = self.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y),
            Inches(w), Inches(h))
        shape.adjustments[0] = min(0.5, radius / min(w, h))
        shape.shadow.inherit = False
        if fill is None:
            shape.fill.background()
        else:
            shape.fill.solid()
            shape.fill.fore_color.rgb = _rgb(fill)
        if edge is None:
            shape.line.fill.background()
        else:
            shape.line.color.rgb = _rgb(edge)
            shape.line.width = Pt(edge_w)
            if dash:
                ln = shape.line._get_or_add_ln()
                d = etree.SubElement(ln, qn("a:prstDash"))
                d.set("val", "dash")
        shape.text_frame.paragraphs[0].text = ""

        patch = FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f"round,pad=0,rounding_size={radius}",
            facecolor=fill if fill else "none",
            edgecolor=edge if edge else "none",
            linewidth=edge_w, linestyle="--" if dash else "-",
            zorder=self._next_z())
        self.ax.add_patch(patch)

    def text(self, x, y, w, h, content, size, color=INK, bold=False,
             italic=False, align="left", valign="top", leading=1.2,
             tracking=None):
        tb = self.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        tf = tb.text_frame
        tf.word_wrap = True
        for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
            setattr(tf, side, 0)
        tf.vertical_anchor = {"top": MSO_ANCHOR.TOP, "middle": MSO_ANCHOR.MIDDLE,
                              "bottom": MSO_ANCHOR.BOTTOM}[valign]
        pptx_align = {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER,
                      "right": PP_ALIGN.RIGHT}[align]
        for i, line in enumerate(content.split("\n")):
            para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            para.alignment = pptx_align
            para.line_spacing = leading
            run = para.add_run()
            run.text = line
            font = run.font
            font.name = FONT
            font.size = Pt(size)
            font.bold = bold
            font.italic = italic
            font.color.rgb = _rgb(color)
            if tracking:
                # letterspacing, in hundredths of a point
                rPr = run._r.get_or_add_rPr()
                rPr.set("spc", str(int(round(tracking * size * 100))))

        mpl_x = {"left": x, "center": x + w / 2, "right": x + w}[align]
        mpl_y = {"top": y, "middle": y + h / 2, "bottom": y + h}[valign]
        mpl_content = content
        if tracking:
            # approximate letterspacing with hair spaces in the preview
            mpl_content = "\n".join(" ".join(line)
                                    for line in content.split("\n"))
        self.ax.text(mpl_x, mpl_y, mpl_content, fontsize=size, color=color,
                     weight="bold" if bold else "normal",
                     style="italic" if italic else "normal",
                     ha=align, va={"top": "top", "middle": "center",
                                   "bottom": "bottom"}[valign],
                     linespacing=leading + 0.15)

    def line(self, x1, y1, x2, y2, color, width=1.5, dash=None, arrow=False):
        conn = self.shapes.add_connector(
            MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1),
            Inches(x2), Inches(y2))
        conn.shadow.inherit = False
        conn.line.color.rgb = _rgb(color)
        conn.line.width = Pt(width)
        ln = conn.line._get_or_add_ln()
        if dash:
            d = etree.SubElement(ln, qn("a:prstDash"))
            d.set("val", "dash")
        if arrow:
            tail = etree.SubElement(ln, qn("a:tailEnd"))
            tail.set("type", "triangle")
            tail.set("w", "med")
            tail.set("len", "med")

        z = self._next_z()
        if arrow:
            annotation = self.ax.annotate(
                "", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=width,
                                shrinkA=0, shrinkB=0, mutation_scale=14,
                                linestyle="--" if dash else "-"))
            annotation.arrow_patch.set_zorder(z)
        else:
            self.ax.plot([x1, x2], [y1, y2], color=color, lw=width,
                         linestyle="--" if dash else "-",
                         solid_capstyle="butt", zorder=z)

    def arrow(self, x1, y1, x2, y2, color, width=1.75):
        self.line(x1, y1, x2, y2, color, width, arrow=True)

    def elbow_arrow(self, points, color, width=1.75):
        """Polyline with an arrowhead on the final segment."""
        for (ax_, ay), (bx, by) in zip(points[:-2], points[1:-1]):
            self.line(ax_, ay, bx, by, color, width)
        (px, py), (qx, qy) = points[-2], points[-1]
        self.arrow(px, py, qx, qy, color, width)

    def title(self, text_value):
        """Letterspaced capitals in the text weight (2.1.6, 3.5.1: weight
        decreases as size increases). Pass the string already in capitals —
        upper() would corrupt µ."""
        self.text(0.7, 0.5, 11.93, 0.55, text_value, SIZE_STAT, INK,
                  align="center", tracking=CAPS_TRACKING)

    def component(self, x, y, w, h, name, fill, sub=None, text_color=WHITE,
                  name_size=SIZE_L):
        """Dally-style flat colored box with a centered label."""
        self.box(x, y, w, h, fill=fill, edge=None, radius=0.06)
        if sub:
            self.text(x, y + 0.15, w, 0.4, name, name_size, text_color,
                      bold=True, align="center")
            self.text(x, y + h - 0.42, w, 0.3, sub, SIZE_XS, text_color,
                      align="center")
        else:
            self.text(x, y, w, h, name, name_size, text_color, bold=True,
                      align="center", valign="middle")


# ---------------------------------------------------------------- slide 1

def slide_example(c):
    c.title("THE EXAMPLE: A CNOT AND TWO DEPENDENT T GATES")

    # the three-operation circuit, centered, with per-op annotations below
    BOX_W, BOX_H, y = 2.6, 1.0, 2.5
    xs = [1.5, 5.35, 9.2]
    c.component(xs[0], y, BOX_W, BOX_H, "Op0 · CNOT(q0, q1)", BLUE)
    c.component(xs[1], y, BOX_W, BOX_H, "Op1 · T(q1)", BLUE)
    c.component(xs[2], y, BOX_W, BOX_H, "Op2 · T(q1)", YELLOW, text_color=INK)

    c.arrow(xs[0] + BOX_W, y + BOX_H / 2, xs[1] - 0.06, y + BOX_H / 2, INK_2, 2.0)
    c.arrow(xs[1] + BOX_W, y + BOX_H / 2, xs[2] - 0.06, y + BOX_H / 2, YELLOW, 2.25)
    c.text(xs[1] + BOX_W - 0.3, y - 0.42, 1.85, 0.3, "blocked", SIZE_S, INK,
           bold=True, align="center")

    notes = ["Clifford\n6 rounds of syndrome data",
             "non-Clifford\n3 rounds + a magic state",
             "may start only after Op1’s\noutcome is decoded"]
    for x, note in zip(xs, notes):
        c.text(x - 0.3, y + BOX_H + 0.25, BOX_W + 0.6, 0.6, note, SIZE_M,
               INK_2, align="center")

    c.text(0.7, 5.2, 11.93, 0.7,
           "d = 3 surface code   ·   QEC round 1.1 µs   ·   sliding window: "
           "commit 3 + buffer 3 rounds\n1 decoder unit   ·   "
           "τ = 1.0 µs per round  →  6.0 µs per window",
           SIZE_L, INK, align="center")

    c.text(0.7, 6.8, 11.93, 0.3,
           "simulate(RunSpec(ops=cnot_plus_two_t_circuit(), "
           "decoder=PerRoundDecoder(tau_us=1.0)))",
           SIZE_XS, MUTED, italic=True, align="center")


# ---------------------------------------------------------------- slide 2

def slide_diagram(c):
    c.title("ONE TIMED LOOP: EVERY HOP HAS A PRICE")

    BOX_W, BOX_H, y = 2.05, 1.05, 2.35
    gap = (12.63 - 0.7 - 5 * BOX_W) / 4          # five boxes, even gaps
    xs = [0.7 + i * (BOX_W + gap) for i in range(5)]
    parts = [("QPU", "1 round / 1.1 µs", BLUE, WHITE),
             ("Controller", "routes packets", BLUE, WHITE),
             ("Window mgr", "commit 3 + buffer 3", BLUE, WHITE),
             ("Decoder", "1 unit · 6.0 µs/window", AQUA, WHITE),
             ("Orchestrator", "Pauli frame · decisions", YELLOW, INK)]
    for x, (name, sub, fill, tc) in zip(xs, parts):
        c.component(x, y, BOX_W, BOX_H, name, fill, sub=sub, text_color=tc)

    hop_labels = ["t_qc  0.15 µs", "t_cd  2.0 µs", "enqueue", "t_do  1.0 µs"]
    mid = y + BOX_H / 2
    for i, label in enumerate(hop_labels):
        x1, x2 = xs[i] + BOX_W, xs[i + 1]
        c.arrow(x1, mid, x2 - 0.05, mid, INK_2, 2.0)
        c.text(x1 - 0.5, y + BOX_H + 0.18, (x2 - x1) + 1.0, 0.28, label,
               SIZE_S, INK, align="center")

    # the return path: orchestrator -> (controller) -> QPU
    ry = y + BOX_H + 0.85
    c.elbow_arrow([(xs[4] + BOX_W / 2, y + BOX_H), (xs[4] + BOX_W / 2, ry),
                   (xs[0] + BOX_W / 2, ry), (xs[0] + BOX_W / 2, y + BOX_H)],
                  YELLOW, 2.25)
    c.text(0.7, ry + 0.12, 11.93, 0.32,
           "decision returns via the controller:  t_oc 4.0 µs  +  t_cq 0.15 µs",
           SIZE_M, INK, align="center")

    # the example's actual timestamps, directly under the loop
    c.text(0.7, 5.8, 11.93, 0.9,
           "In the run:  a round fired at 1.100 reaches the decoder at 3.250."
           "\nOp1’s outcome:  decoded 27.750  →  orchestrator 28.750  →  "
           "controller 32.750  →  QPU 32.900.",
           SIZE_L, INK_2, align="center")


# ---------------------------------------------------------------- slide 3

X0 = 1.15            # timeline origin (inches)
US_PER_IN = 46.0 / 11.6

def tx(t_us):
    return X0 + t_us / US_PER_IN


def slide_timeline(c):
    c.title("THE RUN: 0 → 45.35 µs")

    LANES = [("QPU", 2.15), ("DECODER", 3.65), ("FEEDBACK", 5.05)]
    BAR_H = 0.42

    axis_y = 6.0
    for t in range(0, 50, 5):
        x = tx(t)
        c.line(x, 1.85, x, axis_y, "#e9e7e0", 0.75)
        c.text(x - 0.3, axis_y + 0.06, 0.6, 0.25, str(t), SIZE_XS, MUTED,
               align="center")
    c.text(tx(46.5), axis_y + 0.06, 0.7, 0.25, "µs", SIZE_XS, MUTED)
    for label, y in LANES:
        c.text(0.02, y + BAR_H / 2 - 0.1, 1.02, 0.3, label, SIZE_S, INK,
               align="right", tracking=CAPS_TRACKING)

    # --- QPU lane
    y = LANES[0][1]
    for t1, t2 in ((0.0, 6.6), (6.6, 9.9), (32.9, 36.2)):
        c.box(tx(t1) + 0.015, y, tx(t2) - tx(t1) - 0.03, BAR_H, fill=BLUE,
              edge=None, radius=0.04)
    c.text(tx(3.3) - 1.2, y - 0.30, 2.4, 0.25, "Op0 CNOT", SIZE_S, INK,
           bold=True, align="center")
    c.text(tx(8.25) - 0.95, y - 0.30, 1.9, 0.25, "Op1 T", SIZE_S, INK,
           bold=True, align="center")
    c.text(tx(34.55) - 0.95, y - 0.30, 1.9, 0.25, "Op2 T", SIZE_S, INK,
           bold=True, align="center")
    c.box(tx(9.9) + 0.015, y, tx(32.9) - tx(9.9) - 0.03, BAR_H,
          fill=STALL_FILL, edge=STALL_EDGE, edge_w=1.0, dash=True, radius=0.04)
    c.text(tx(9.9), y + 0.08, tx(32.9) - tx(9.9), 0.28,
           "stalled 23.0 µs — waiting for Op1’s decoded outcome", SIZE_S,
           INK_2, align="center", italic=True)

    # --- decoder lane
    y = LANES[1][1]
    for t1, t2, label in ((8.75, 14.75, "Op0 · W0"), (15.25, 21.25, "Op0 · W1"),
                          (21.75, 27.75, "Op1 · W0"), (38.35, 44.35, "Op2 · W0")):
        c.box(tx(t1) + 0.015, y, tx(t2) - tx(t1) - 0.03, BAR_H, fill=AQUA,
              edge=None, radius=0.04)
        c.text(tx(t1), y + 0.08, tx(t2) - tx(t1), 0.28, label, SIZE_S, WHITE,
               bold=True, align="center")
    c.text(tx(8.75), y - 0.30, 4.2, 0.25, "each window: 6 rounds × τ = 6.0 µs",
           SIZE_S, INK_2)

    # --- feedback lane
    y = LANES[2][1]
    c.box(tx(28.75) + 0.015, y, tx(32.9) - tx(28.75) - 0.03, BAR_H,
          fill=YELLOW, edge=None, radius=0.04)
    c.text(tx(32.9) - 8.0, y - 0.30, 7.9, 0.25,
           "decision travels 28.750 → 32.900", SIZE_S, INK, bold=True,
           align="right")
    c.line(tx(22.25), y - 0.04, tx(22.25), y + BAR_H + 0.04, YELLOW, 2.5)
    c.text(tx(22.25) - 3.3, y + 0.5, 3.1, 0.25, "22.250 · Op0 result:",
           SIZE_S, INK_2, align="right")
    c.text(tx(22.25) - 3.3, y + 0.74, 3.1, 0.25, "Pauli-frame update only",
           SIZE_S, INK_2, align="right")

    # markers (the colored dashed lines carry identity; the labels stay in ink)
    c.line(tx(36.2), 1.85, tx(36.2), axis_y, BLUE, 1.5, dash=True)
    c.text(tx(36.2) - 2.35, 1.55, 2.2, 0.25, "QPU done 36.200", SIZE_S, INK,
           bold=True, align="right")
    c.line(tx(45.35), 1.85, tx(45.35), axis_y, AQUA, 1.5, dash=True)
    c.text(tx(45.35) - 1.95, 1.55, 1.9, 0.25, "all decoded 45.350", SIZE_S,
           INK, bold=True, align="right")

    c.text(0.7, 6.75, 11.93, 0.35,
           "The QPU computes for 13.2 of its 36.2 µs — one stall is 64% of its schedule.",
           SIZE_L, INK, italic=True, align="center")


# ---------------------------------------------------------------- slide 4

def slide_stall(c):
    c.title("WHERE THE 23.0 µs STALL GOES")

    scale = 11.0 / 23.0
    bx0, by, bh = 1.15, 2.2, 0.55
    segments = [(11.85, STALL_FILL, STALL_EDGE), (6.0, AQUA, None),
                (1.0, YELLOW, None), (4.0, YELLOW, None), (0.15, YELLOW, None)]
    x = bx0
    seg_x = []
    for width_us, fill, edge in segments:
        w = width_us * scale
        c.box(x + 0.012, by, w - 0.024, bh, fill=fill, edge=edge,
              edge_w=1.0, radius=0.04)
        seg_x.append((x, w))
        x += w

    c.text(seg_x[0][0], by + 0.15, seg_x[0][1], 0.3, "waiting  11.85 µs",
           SIZE_M, INK_2, align="center")
    c.text(seg_x[1][0], by + 0.15, seg_x[1][1], 0.3, "decode  6.0 µs",
           SIZE_M, WHITE, bold=True, align="center")
    c.text(seg_x[3][0], by + 0.15, seg_x[3][1], 0.3, "t_oc  4.0", SIZE_M, INK,
           bold=True, align="center")
    mid2 = seg_x[2][0] + seg_x[2][1] / 2
    c.line(mid2, by - 0.28, mid2, by - 0.04, MUTED, 1.0)
    c.text(mid2 - 1.1, by - 0.56, 2.2, 0.25, "t_do  1.0", SIZE_S, INK_2,
           align="center")
    mid4 = seg_x[4][0] + seg_x[4][1] / 2
    c.line(mid4, by - 0.28, mid4, by - 0.04, MUTED, 1.0)
    c.text(mid4 - 1.1, by - 0.56, 2.2, 0.25, "t_cq  0.15", SIZE_S, INK_2,
           align="center")
    c.text(bx0, by + bh + 0.12, 3.0, 0.25, "9.900 µs · Op1 body done", SIZE_S,
           INK_2)
    c.text(bx0 + 11.0 - 3.0, by + bh + 0.12, 3.0, 0.25,
           "32.900 µs · Op2 starts", SIZE_S, INK_2, align="right")

    # sparse breakdown with the numbers (Dally-style)
    bullets = [
        ("11.85 µs", "waiting — the one decoder unit is busy with Op0’s two "
                     "windows, then a 0.5 µs window handoff (t_dd)"),
        ("6.0 µs", "decoding Op1’s window (6 rounds × τ 1.0 µs)"),
        ("5.15 µs", "communication — publish 1.0 (t_do) + decision return "
                    "4.0 (t_oc) + delivery 0.15 (t_cq)"),
    ]
    y = 4.0
    for number, caption in bullets:
        c.text(1.7, y, 1.7, 0.35, number, SIZE_XL, INK, bold=True,
               align="right")
        c.text(3.65, y + 0.07, 8.5, 0.35, caption, SIZE_M, INK_2)
        y += 0.6

    c.text(0.7, 6.0, 11.93, 0.35,
           "Whole run:  4 windows decoded  ·  20 idle memory rounds emitted  ·  "
           "peak 9 syndrome payloads buffered", SIZE_M, INK_2, align="center")
    c.text(0.7, 6.6, 11.93, 0.4,
           "The feedback loop, not decoder throughput, sets the pace.",
           SIZE_XL, INK, italic=True, align="center")


# ------------------------------------------------------------------- build

def build():
    PREVIEW_DIR.mkdir(exist_ok=True)
    presentation = Presentation()
    presentation.slide_width = Inches(PAGE_W)
    presentation.slide_height = Inches(PAGE_H)
    blank_layout = presentation.slide_layouts[6]

    slide_fns = [slide_example, slide_diagram, slide_timeline, slide_stall]
    for index, draw in enumerate(slide_fns, 1):
        pptx_slide = presentation.slides.add_slide(blank_layout)
        fig = plt.figure(figsize=(PAGE_W, PAGE_H))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, PAGE_W)
        ax.set_ylim(PAGE_H, 0)
        ax.axis("off")
        draw(SlideCanvas(pptx_slide, ax))
        fig.savefig(PREVIEW_DIR / f"slide_{index}.png", dpi=180,
                    facecolor="white")
        plt.close(fig)

    presentation.core_properties.title = "decsim — simulator example"
    presentation.save(OUT_PPTX)
    print(OUT_PPTX)
    print(PREVIEW_DIR)


if __name__ == "__main__":
    build()
