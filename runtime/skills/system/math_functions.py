"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/system/math_functions.py

Purpose:
    Approved mathematical functions and constants.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    13.3
==========================================================
"""

from __future__ import annotations

import math
import statistics

CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": math.inf,
}

FUNCTIONS = {
    # Basic
    "abs": abs,
    "round": round,

    # Powers
    "sqrt": math.sqrt,
    "pow": pow,

    # Trigonometry
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,

    # Angle Conversion
    "degrees": math.degrees,
    "radians": math.radians,

    # Logarithms
    "log": math.log,
    "log10": math.log10,
    "log2": math.log2,
    "exp": math.exp,

    # Miscellaneous
    "factorial": math.factorial,
    "ceil": math.ceil,
    "floor": math.floor,
    "gcd": math.gcd,
    "lcm": math.lcm,
    "comb": math.comb,
    "perm": math.perm,
    "hypot": math.hypot,
    "dist": math.dist,

    # Statistics
    "mean": statistics.mean,
    "median": statistics.median,
    "fmean": statistics.fmean,
}