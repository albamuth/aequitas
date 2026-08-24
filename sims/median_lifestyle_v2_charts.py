"""
median_lifestyle_v2_charts.py -- charts for the rewritten MEDIAN_LIFESTYLE.md,
from the rigorous bottom-up results (Tracks 1-4). Values are the logged results in
median_lifestyle_RESULTS.md (stable; sourced there).

  figA_breakdown.png   -- the 4-track total, domestic vs foreign
  figB_domestic.png    -- where the domestic hours are (by sector group)
  figC_foreign.png     -- which countries the offshore hours are in

Run:  python median_lifestyle_v2_charts.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BLUE, TEAL, ORANGE, GRAY, GREEN, RED = (
    "#2b6cb0", "#2c7a7b", "#dd6b20", "#718096", "#2f855a", "#c53030")

plt.rcParams.update({
    "font.size": 12, "axes.titlesize": 15, "axes.titleweight": "bold",
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white", "axes.spines.top": False,
    "axes.spines.right": False,
})

# --- per-adult h/yr, from the tracks ---
T1, T2, T3, T4 = 772, 45, 785, 18      # consumption, housing, imports(foreign), pollution(mid)
TOTAL = T1 + T2 + T3 + T4
DOMESTIC = T1 + T2 + T4
FOREIGN = T3


def figA():
    fig, ax = plt.subplots(figsize=(9.5, 3.4))
    segs = [("Consumption\n(domestic)", T1, BLUE),
            ("Housing\nbuild", T2, TEAL),
            ("Imports\n(FOREIGN labour)", T3, ORANGE),
            ("Pollution\nclean-up", T4, GRAY)]
    left = 0
    for label, val, color in segs:
        ax.barh(0, val, left=left, color=color, height=0.5)
        if val > 30:
            ax.text(left + val / 2, 0, f"{val}", ha="center", va="center",
                    color="white", fontweight="bold", fontsize=12)
        left += val
    ax.set_xlim(0, TOTAL * 1.02)
    ax.set_ylim(-1, 1.2)
    ax.set_yticks([])
    ax.set_xlabel("hours of human labour per year")
    ax.set_title(f"What a median US adult's lifestyle costs: ~{TOTAL:,} hours/year")
    # legend row
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for _, _, c in segs]
    ax.legend(handles, [s[0].replace("\n", " ") for s in segs],
              loc="upper center", bbox_to_anchor=(0.5, -0.35), ncol=4, frameon=False,
              fontsize=10)
    ax.annotate(f"≈ 0.9 of one person's full-time work-year  ·  "
                f"{100*FOREIGN/TOTAL:.0f}% performed abroad",
                xy=(TOTAL/2, 0.85), ha="center", fontsize=11, color=RED,
                fontweight="bold")
    fig.tight_layout()
    out = os.path.join(HERE, "figA_breakdown.png")
    fig.savefig(out, dpi=130, bbox_inches="tight")
    plt.close(fig)
    return out


def figB():
    # national domestic hours by sector group (billion h/yr); Track 1 total ~199B
    groups = [("Healthcare", 34), ("Retail & wholesale", 39),
              ("Food service", 22), ("Housing services", 8),
              ("Everything else", 199 - 34 - 39 - 22 - 8)]
    labels = [g[0] for g in groups]
    vals = [g[1] for g in groups]
    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    bars = ax.barh(labels, vals, color=[BLUE]*4 + [GRAY])
    ax.invert_yaxis()
    ax.set_xlabel("billion hours per year (US total)")
    ax.set_title("Where the domestic hours go — services lead")
    for b, v in zip(bars, vals):
        ax.text(v + 1.5, b.get_y() + b.get_height()/2, f"{v} B",
                va="center", fontsize=11)
    ax.set_xlim(0, max(vals)*1.18)
    fig.tight_layout()
    out = os.path.join(HERE, "figB_domestic.png")
    fig.savefig(out, dpi=130)
    plt.close(fig)
    return out


def figC():
    # foreign origin of embodied labour (billion h/yr), EXIOBASE
    origins = [("Rest of Asia-Pacific", 52.8), ("India", 40.4), ("China", 33.9),
               ("Mexico", 18.4), ("Rest of Americas", 13.8),
               ("Rest of Africa", 9.5), ("Indonesia", 6.0), ("Middle East", 5.5)]
    labels = [o[0] for o in origins]
    vals = [o[1] for o in origins]
    fig, ax = plt.subplots(figsize=(8.5, 4.4))
    bars = ax.barh(labels, vals, color=ORANGE)
    ax.invert_yaxis()
    ax.set_xlabel("billion hours per year embodied in US consumption")
    ax.set_title("Whose hands: the FOREIGN half of a US lifestyle")
    for b, v in zip(bars, vals):
        ax.text(v + 0.6, b.get_y() + b.get_height()/2, f"{v}",
                va="center", fontsize=11)
    ax.set_xlim(0, max(vals)*1.15)
    ax.set_xlabel("billion hours per year embodied in US consumption\n"
                  "(low-wage economies pack the most HOURS into each dollar)")
    fig.tight_layout()
    out = os.path.join(HERE, "figC_foreign.png")
    fig.savefig(out, dpi=130)
    plt.close(fig)
    return out


def figD():
    """Average vs median per person, and the 'needs multiple Earths' note."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2),
                                   gridspec_kw={"width_ratios": [1, 1]})
    # left: avg vs median lifestyle (labour), close together
    ax1.bar(["Median\nperson", "Average\nperson"], [1045, 1250],
            color=[GRAY, BLUE], width=0.6)
    for x, v in zip([0, 1], [1045, 1250]):
        ax1.text(x, v + 20, f"{v:,}", ha="center", fontweight="bold")
    ax1.set_ylabel("hours of labour commanded / yr")
    ax1.set_title("Lifestyle: nearly equal", fontsize=13)
    ax1.set_ylim(0, 1500)
    ax1.annotate("only 1.2× apart", xy=(0.5, 1150), ha="center", color=RED,
                 fontweight="bold", fontsize=11)
    # right: if everyone lived like the average American -> Earths needed
    cats = ["Land", "Carbon", "Materials", "Labour"]
    earths = [3.7, 2.7, 1.5, 1.5]   # multiples of what's available
    colors = [RED, ORANGE, ORANGE, GRAY]
    bars = ax2.barh(cats, earths, color=colors)
    ax2.axvline(1.0, color="black", lw=1.2, ls="--")
    ax2.text(1.02, 3.4, "sustainable limit", fontsize=9, rotation=90, va="top")
    for b, v in zip(bars, earths):
        ax2.text(v + 0.05, b.get_y()+b.get_height()/2, f"{v}×", va="center",
                 fontweight="bold")
    ax2.set_xlim(0, 4.2)
    ax2.invert_yaxis()
    ax2.set_xlabel("× what the planet / workforce can supply")
    ax2.set_title("...but the footprint needs several Earths", fontsize=13)
    fig.suptitle("Average vs median — and why the average can't go global",
                 fontweight="bold", fontsize=15)
    fig.tight_layout()
    out = os.path.join(HERE, "figD_average.png")
    fig.savefig(out, dpi=130)
    plt.close(fig)
    return out


if __name__ == "__main__":
    for f in (figA(), figB(), figC(), figD()):
        print("wrote", os.path.basename(f))
