"""Stream type classes for tap-voipstudio."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_voipstudio.client import VOIPStudioStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"

class CDRS(VOIPStudioStream):
    """Stream for CDRs endpoint"""

    name = "cdrs"
    path = "/cdrs"
    primary_keys = ["call_id"]

    schema_filepath = SCHEMAS_DIR / "cdrs.json"  # noqa: ERA001
