from mypy.plugin import Plugin

from .dispatcher import PluginDispatcher


def plugin(_: str) -> type[Plugin]:
    return PluginDispatcher


__all__ = ["PluginDispatcher", "plugin"]

__version__ = "0.1.0"
