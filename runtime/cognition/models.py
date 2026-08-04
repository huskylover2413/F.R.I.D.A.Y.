"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/cognition/models.py

Purpose:
    Defines Cognition response models.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.7.0
Release:
    Cognition
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Response:
    """
    Final response produced by Cognition.
    """

    message: str

    success: bool = True