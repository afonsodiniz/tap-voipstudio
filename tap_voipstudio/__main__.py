"""VOIPStudio entry point."""

from __future__ import annotations

from tap_voipstudio.tap import TapVOIPStudio

TapVOIPStudio.cli()
