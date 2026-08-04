"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/loader/exceptions.py

Purpose:
    Defines exceptions used by the Service Loader.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.3.0
Release:
    Awakening
==========================================================
"""

from __future__ import annotations


class ServiceLoaderError(Exception):
    """
    Base exception for Service Loader failures.
    """


class DuplicateServiceError(ServiceLoaderError):
    """
    Raised when a service is registered more than once.
    """


class InvalidServiceError(ServiceLoaderError):
    """
    Raised when an invalid Service is encountered.
    """