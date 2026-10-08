#!/usr/bin/env python3
"""Check a color palette for color-vision deficiency (CVD) and grayscale safety.

Zero dependencies (standard library only).

Usage:
  python check_palette.py --type qualitative "#E69F00" "#56B4E9" "#009E73"
  python check_palette.py --type sequential  "#fde725" "#5ec962" "#21918c" "#3b528b" "#440154"
  python check_palette.py --type diverging   "#8c510a" "#d8b365" "#f5f5f5" "#5ab4ac" "#01665e"
  python check_palette.py --json --type qualitative "#E69F00" "#56B4E9"

What it checks:
  qualitative  - minimum pairwise color difference (CIEDE2000) under normal vision,
                 deuteranopia, protanopia, tritanopia, and grayscale.
  sequential   - lightness (CIE L*) changes monotonically, in color and under each CVD.
  diverging    - the midpoint is the lightest color, the two arms are balanced
                 in lightness, and the end colors stay distinct under each CVD.

The thresholds are heuristics. Simulations use the Machado, Oliveira & Fernandes (2009)
matrices at full severity (the "-anopia" forms are the worst case for the "-anomaly" forms).
This only checks the palette. Still look at the finished figure in a CVD simulator,
because thin lines and small points make colors much harder to tell apart.
"""
import argparse
import json
import math
import sys

# Machado et al. (2009), severity 1.0, applied in linear RGB.
CVD_MATRICES = {
    "deuteranopia": [[0.367322, 0.860646, -0.227968],
                     [0.280085, 0.672501, 0.047413],
                     [-0.011820, 0.042940, 0.968881]],
    "protanopia": [[0.152286, 1.052583, -0.204868],
                   [0.114503, 0.786281, 0.099216],
                   [-0.003882, -0.048116, 1.051998]],
    "tritanopia": [[1.255528, -0.076749, -0.178779],
                   [-0.078411, 0.930809, 0.147602],
                   [0.004733, 0.691367, 0.303900]],
}


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"not a hex color: #{h}")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02X}" for c in rgb)


def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c):
    c = max(0.0, min(1.0, c))
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def simulate(rgb, kind):
    if kind == "normal":
        return rgb
    lin = [srgb_to_linear(c) for c in rgb]
    if kind == "grayscale":
        y = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
        g = linear_to_srgb(y)
        return (g, g, g)
    m = CVD_MATRICES[kind]
    out = [sum(m[r][k] * lin[k] for k in range(3)) for r in range(3)]
    return tuple(linear_to_srgb(c) for c in out)


def rgb_to_lab(rgb):
    r, g, b = (srgb_to_linear(c) for c in rgb)
    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
    y = (0.2126729 * r + 0.7151522 * g + 0.0721750 * b) / 1.00000
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116

    fx, fy, fz = f(x), f(y), f(z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def ciede2000(lab1, lab2):
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cb = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cb ** 7 / (Cb ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360
    h2p = math.degrees(math.atan2(b2, a2p)) % 360
    dLp = L2 - L1
    dCp = C2p - C1p
    if C1p * C2p == 0:
        dhp = 0
    elif abs(h2p - h1p) <= 180:
        dhp = h2p - h1p
    elif h2p - h1p > 180:
        dhp = h2p - h1p - 360
    else:
        dhp = h2p - h1p + 360
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp / 2))
    Lbp = (L1 + L2) / 2
    Cbp = (C1p + C2p) / 2
    if C1p * C2p == 0:
        hbp = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hbp = (h1p + h2p) / 2
    elif h1p + h2p < 360:
        hbp = (h1p + h2p + 360) / 2
    else:
        hbp = (h1p + h2p - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hbp - 30)) + 0.24 * math.cos(math.radians(2 * hbp))
         + 0.32 * math.cos(math.radians(3 * hbp + 6)) - 0.20 * math.cos(math.radians(4 * hbp - 63)))
    dtheta = 30 * math.exp(-(((hbp - 275) / 25) ** 2))
    Rc = 2 * math.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7))
    Sl = 1 + 0.015 * (Lbp - 50) ** 2 / math.sqrt(20 + (Lbp - 50) ** 2)
    Sc = 1 + 0.045 * Cbp
    Sh = 1 + 0.015 * Cbp * T
    Rt = -math.sin(math.radians(2 * dtheta)) * Rc
    return math.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2
                     + Rt * (dCp / Sc) * (dHp / Sh))


VISIONS = ["normal", "deuteranopia", "protanopia", "tritanopia", "grayscale"]


def check_qualitative(colors, min_de):
    report = {}
    for v in VISIONS:
        labs = [rgb_to_lab(simulate(hex_to_rgb(c), v)) for c in colors]
        worst = None
        problems = []
        for i in range(len(colors)):
            for j in range(i + 1, len(colors)):
                d = ciede2000(labs[i], labs[j])
                if worst is None or d < worst[0]:
                    worst = (d, colors[i], colors[j])
                if d < min_de:
                    problems.append({"pair": [colors[i], colors[j]], "deltaE": round(d, 1)})
        report[v] = {
            "min_deltaE": round(worst[0], 1) if worst else None,
            "closest_pair": [worst[1], worst[2]] if worst else None,
            "pairs_below_threshold": problems,
        }
    notes = []
    if len(colors) > 8:
        notes.append("More than 8 categories: use direct labels or a coarser grouping "
                     "instead of relying on color (aim for 3-5).")
    elif len(colors) > 5:
        notes.append("6-8 categories: workable with a CVD-safe palette, but consider direct "
                     "labeling and redundant shapes.")
    return report, notes


def lightness_series(colors, vision):
    return [rgb_to_lab(simulate(hex_to_rgb(c), vision))[0] for c in colors]


def is_monotonic(seq, tol=1.0):
    inc = all(b >= a - tol for a, b in zip(seq, seq[1:]))
    dec = all(b <= a + tol for a, b in zip(seq, seq[1:]))
    return inc or dec


def check_sequential(colors):
    report = {}
    for v in VISIONS:
        L = lightness_series(colors, v)
        steps = [abs(b - a) for a, b in zip(L, L[1:])]
        report[v] = {
            "lightness": [round(x, 1) for x in L],
            "monotonic": is_monotonic(L),
            "smallest_step": round(min(steps), 1) if steps else None,
            "largest_step": round(max(steps), 1) if steps else None,
        }
    notes = []
    if not report["normal"]["monotonic"]:
        notes.append("Lightness is not monotonic: this behaves like a rainbow scale and will "
                     "create false boundaries. Use a perceptually uniform sequential scale.")
    s = report["normal"]
    if s["smallest_step"] is not None and s["smallest_step"] > 0 and s["largest_step"] / s["smallest_step"] > 3:
        notes.append("Lightness steps are very uneven (ratio > 3): the scale is not perceptually "
                     "uniform, so some data ranges will look flat and others will jump.")
    return report, notes


def check_diverging(colors, min_de):
    report = {}
    notes = []
    n = len(colors)
    mid = n // 2
    for v in VISIONS:
        L = lightness_series(colors, v)
        left, right = L[:mid + (n % 2)], L[mid:]
        center_lightest = max(L) - L[mid] <= 2.0 if n % 2 else True
        arm_l = L[:mid]
        arm_r = list(reversed(L[mid + (n % 2):]))
        imbalance = max((abs(a - b) for a, b in zip(arm_l, arm_r)), default=0.0)
        ends = ciede2000(rgb_to_lab(simulate(hex_to_rgb(colors[0]), v)),
                         rgb_to_lab(simulate(hex_to_rgb(colors[-1]), v)))
        report[v] = {
            "lightness": [round(x, 1) for x in L],
            "midpoint_is_lightest": center_lightest,
            "max_arm_lightness_imbalance": round(imbalance, 1),
            "end_colors_deltaE": round(ends, 1),
            "left_arm_monotonic": is_monotonic(left),
            "right_arm_monotonic": is_monotonic(right),
        }
        if v not in ("normal", "grayscale") and ends < min_de:
            notes.append(f"Under {v}, the two ends of the scale look alike (deltaE {ends:.1f}). "
                         "Avoid red-green (or blue-green for tritans). Try blue-orange, "
                         "blue-red, or ColorBrewer PiYG/BrBG/PuOr.")
    if report["normal"]["max_arm_lightness_imbalance"] > 8:
        notes.append("The arms are unbalanced in lightness: equal deviations will look unequal "
                     "on the two sides.")
    if n % 2 and not report["normal"]["midpoint_is_lightest"]:
        notes.append("The midpoint is not the lightest color: diverging scales should have a "
                     "light, neutral center.")
    return report, notes


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("colors", nargs="+", help="hex colors, e.g. '#E69F00'")
    p.add_argument("--type", choices=["qualitative", "sequential", "diverging"], default="qualitative")
    p.add_argument("--min-delta-e", type=float, default=10.0,
                   help="flag color pairs whose CIEDE2000 difference is below this value "
                        "(default 10; ~20+ is comfortable for small marks)")
    p.add_argument("--json", action="store_true", help="print machine-readable JSON")
    a = p.parse_args()

    try:
        colors = ["#" + c.strip().lstrip("#").upper() for c in a.colors]
        for c in colors:
            hex_to_rgb(c)
    except ValueError as e:
        sys.exit(str(e))

    if a.type == "qualitative":
        report, notes = check_qualitative(colors, a.min_delta_e)
    elif a.type == "sequential":
        report, notes = check_sequential(colors)
    else:
        report, notes = check_diverging(colors, a.min_delta_e)

    if a.type == "qualitative":
        for v in VISIONS:
            if report[v]["pairs_below_threshold"] and v != "grayscale":
                notes.append(f"Under {v}, {len(report[v]['pairs_below_threshold'])} pair(s) fall "
                             f"below deltaE {a.min_delta_e:g}: closest {report[v]['closest_pair']}.")
        if report["grayscale"]["pairs_below_threshold"]:
            notes.append("Some colors are indistinguishable in grayscale: add redundant coding "
                         "(shapes, line types, direct labels).")

    simulated = {v: [rgb_to_hex(simulate(hex_to_rgb(c), v)) for c in colors] for v in VISIONS[1:]}
    out = {"type": a.type, "colors": colors, "report": report, "simulated_colors": simulated,
           "verdict": "PASS" if not notes else "REVIEW", "notes": notes}

    if a.json:
        print(json.dumps(out, indent=2))
        return
    print(f"Palette ({a.type}): {' '.join(colors)}")
    for v in VISIONS:
        print(f"\n[{v}]")
        if v != "normal":
            print("  simulated: " + " ".join(simulated[v]))
        for k, val in report[v].items():
            print(f"  {k}: {val}")
    print(f"\nVerdict: {out['verdict']}")
    for n in notes:
        print(f"  - {n}")


if __name__ == "__main__":
    main()
