import os

from hyfi import HyFI, about, global_config  # type: ignore

from ._version import __version__  # type: ignore

# Read the package name from the current directory
__package_name__ = os.path.basename(os.path.dirname(__file__))

# Extract package information
about.__package_name__ = __package_name__

# Initialize the logger
HyFI.setLogger()


def get_version() -> str:
    """Get the package version."""
    return __version__
