"""
median_lifestyle_charts.py -- layperson-friendly charts for MEDIAN_LIFESTYLE.md.

Generates three PNGs from the same numbers median_lifestyle.py reports:
  fig1_median_in_context.png  -- how big the median figure is vs what people earn
  fig2_labour_abundant.png    -- self-care credit dwarfs all productive labour
  fig3_compression.png        -- inequality compression today vs Aequitas (log)

Run:  python median_lifestyle_charts.py
"""
from __future__ import annotations

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from median_lifestyle import (
    Inputs, total_labour_hours, mean_consumption_hours_domestic,
    median_bundle_hours, self_care_credit_per_capita, total_self_care_credit,
    accrual_ceiling_ratio,
)

HERE = os.path.dirname(os.path.abspath(__file__))

# Accessible, print-safe palette (colourblind-friendly)
BLUE = "#2b6cb0"
ORANGE = "#dd6b20"
GRAY = "#718096"
GREEN = "#2f855a"
RED = "#c53030"

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 15,
    "axes.titleweight": "bold",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def _annotate_h(ax, bars, vals, suffix=" h", fmt="{:,.0f}"):
    for b, v in zip(bars, vals):
        ax.text(b.get_width() + max(vals) * 0.01, b.get_y() + b.get_height() / 2,
                fmt.format(v) + suffix, va="center", ha="left", fontsize=11)


def fig1_median_in_context(x: Inputs):
    med_lo, med_hi = median_bundle_hours(x)
    med_mid = (med_lo + med_hi) / 2
    sc = self_care_credit_per_capita(x)
    full_year = x.avg_annual_hours
    ceiling = x.rho * 24 * 365

    labels = [
        "Labour a MEDIAN\nlifestyle commands",
        "One full-time\nwork-year",
        "Self-care credit\nalone (per person)",
        "Most anyone may\never consume (cap)",
    ]
    vals = [med_mid, full_year, sc, ceiling]
    colors = [ORANGE, GRAY, BLUE, GREEN]

    fig, ax = plt.subplots(figsize=(9, 4.6))
    y = range(len(labels))
    bars = ax.barh(list(y), vals, color=colors)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("hours of human labour per year")
    ax.set_title("How big is a median lifestyle, in hours of work?")
    _annotate_h(ax, bars, vals)
    # show the median as a range
    ax.annotate(f"range {med_lo:,.0f}–{med_hi:,.0f} h",
                xy=(med_mid, 0), xytext=(med_mid, -0.55),
                ha="center", fontsize=10, color=ORANGE)
    ax.set_xlim(0, ceiling * 1.18)
    ax.margins(y=0.12)
    fig.tight_layout()
    out = os.path.join(HERE, "fig1_median_in_context.png")
    fig.savefig(out, dpi=130)
    plt.close(fig)
    return out


def fig2_labour_abundant(x: Inputs):
    sc_tot = total_self_care_credit(x) / 1e9
    prod = total_labour_hours(x) / 1e9
    ratio = sc_tot / prod

    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    labels = ["Self-care credit\n(~10 h/day, EVERY human)",
              "ALL productive labour\n(everyone's jobs)"]
    vals = [sc_tot, prod]
    bars = ax.bar(labels, vals, color=[BLUE, GRAY], width=0.6)
    ax.set_ylabel("billion hours per year (whole USA)")
    ax.set_title("Labour is abundant: self-care credit dwarfs all the jobs")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + max(vals) * 0.015,
                f"{v:,.0f} B h", ha="center", fontsize=12, fontweight="bold")
    ax.annotate(f"{ratio:.1f}× larger",
                xy=(0, sc_tot), xytext=(0.5, sc_tot * 0.72),
                ha="center", fontsize=13, color=RED, fontweight="bold")
    ax.set_ylim(0, max(vals) * 1.15)
    fig.tight_layout()
    out = os.path.join(HERE, "fig2_labour_abundant.png")
    fig.savefig(out, dpi=130)
    plt.close(fig)
    return out


def fig3_compression(x: Inputs):
    ratio = accrual_ceiling_ratio(x)
    labels = ["TODAY:\nlargest incomes\nvs the median",
              "TODAY:\nenergy & material\nfootprints",
              "AEQUITAS:\nthe cap"]
    # ranges (low, high) as multiples of the median
    lows = [1e4, 10, ratio]
    highs = [1e5, 100, ratio]
    mids = [(l * h) ** 0.5 for l, h in zip(lows, highs)]
    colors = [RED, ORANGE, GREEN]

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    bars = ax.bar(labels, mids, color=colors, width=0.6)
    ax.set_yscale("log")
    ax.set_ylabel("times bigger than a median lifestyle  (log scale)")
    ax.set_title("How much Aequitas compresses inequality")
    # error bars to show the ranges for the first two
    for i, (b, l, h, m) in enumerate(zip(bars, lows, highs, mids)):
        if h > l:
            ax.plot([b.get_x() + b.get_width() / 2] * 2, [l, h],
                    color="black", lw=1.4)
            ax.text(b.get_x() + b.get_width() / 2, h * 1.15,
                    f"{l:,.0f}–{h:,.0f}×", ha="center", fontsize=11,
                    fontweight="bold")
        else:
            ax.text(b.get_x() + b.get_width() / 2, m * 1.25,
                    f"{m:.1f}×", ha="center", fontsize=13, fontweight="bold",
                    color=GREEN)
    ax.yaxis.set_major_formatter(FuncFormatter(
        lambda v, _: f"{v:,.0f}×" if v >= 1 else f"{v:g}×"))
    ax.set_ylim(1, 3e5)
    fig.tight_layout()
    out = os.path.join(HERE, "fig3_compression.png")
    fig.savefig(out, dpi=130)
    plt.close(fig)
    return out


def main():
    x = Inputs()
    outs = [fig1_median_in_context(x), fig2_labour_abundant(x), fig3_compression(x)]
    for o in outs:
        print("wrote", os.path.basename(o))


if __name__ == "__main__":
    main()
