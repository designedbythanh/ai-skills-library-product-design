#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Thanh Nguyen
"""WCAG 2.x contrast ratio between two colors.

Usage: python3 contrast.py FOREGROUND BACKGROUND [FOREGROUND BACKGROUND ...]
Colors: #rgb, #rrggbb, #rrggbbaa (alpha blended over the background), or rgb(r, g, b).
Prints the ratio and pass/fail for normal text (4.5:1), large text (3:1) and
UI components such as switch tracks, borders and icons (3:1, WCAG 1.4.11).
"""
import re
import sys


def parse(color):
    c = color.strip().lower()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)", c)
    if m:
        r, g, b = (int(x) for x in m.groups()[:3])
        return r, g, b, float(m.group(4)) if m.group(4) else 1.0
    c = c.lstrip("#")
    if len(c) in (3, 4):
        c = "".join(ch * 2 for ch in c)
    if len(c) not in (6, 8) or not re.fullmatch(r"[0-9a-f]+", c):
        raise ValueError(f"can't read color '{color}'")
    r, g, b = (int(c[i:i + 2], 16) for i in (0, 2, 4))
    a = int(c[6:8], 16) / 255 if len(c) == 8 else 1.0
    return r, g, b, a


def blend(fg, bg):
    r, g, b, a = fg
    return tuple(round(a * f + (1 - a) * k) for f, k in zip((r, g, b), bg[:3]))


def luminance(rgb):
    def channel(v):
        v /= 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    bg_rgb = parse(bg)
    if bg_rgb[3] < 1:
        raise ValueError(f"background '{bg}' must be opaque")
    l1, l2 = luminance(blend(parse(fg), bg_rgb)), luminance(bg_rgb[:3])
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def main(args):
    if not args or len(args) % 2:
        print(__doc__.strip())
        return 2
    for fg, bg in zip(args[::2], args[1::2]):
        r = ratio(fg, bg)
        mark = lambda ok: "pass" if ok else "FAIL"
        print(f"{fg} on {bg}: {r:.2f}:1 · text {mark(r >= 4.5)} · large text {mark(r >= 3)} · UI component {mark(r >= 3)}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except ValueError as e:
        print(f"error: {e}")
        sys.exit(2)
