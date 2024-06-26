"""VOIPStudio tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_voipstudio import streams


class TapVOIPStudio(Tap):
    """VOIPStudio tap class."""

    name = "tap-voipstudio"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_url",
            th.StringType,
            default="https://l7api.com/v1.2/voipstudio",
            description="The url for the API service",
        ),
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        )
    ).to_dict()

    def discover_streams(self) -> list[streams.VOIPStudioStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.CDRS(self)
        ]


if __name__ == "__main__":
    TapVOIPStudio.cli()
