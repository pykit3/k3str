"""
k3str is a collection of string operation utilities.

    >>> repr(to_bytes('我'))
    "b'\\\\xe6\\\\x88\\\\x91'"

"""

from .str_ext import (
    default_encoding,
    to_bytes,
    to_utf8,
)

__all__ = [
    "default_encoding",
    "to_bytes",
    "to_utf8",
]


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3str")
