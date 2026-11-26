#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Deadpan Forecasts entry: writes one forecast line to /output/entry.txt.

Winner of an 8-candidate in-session tournament: real forecast scaffolding
(temperature, drizzle, rain probability) with one deadpan twist at the end.
The line is 144 characters, inside the 1-160 gate, with no trailing newline.
"""
import os

LINE = "Port Sallow: 18 degrees, light drizzle all morning, and a 40% chance of rain this afternoon, rising to 100% the moment you hang the washing out."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
