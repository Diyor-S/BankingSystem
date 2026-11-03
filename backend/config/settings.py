"""
Configuration Module for Banking System.
"""

from __future__ import annotations


class Settings:
    run: RunConfig = RunConfig.get_enabled()


settings = Settings()
