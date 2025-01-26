from mypy.plugin import Plugin

from .dispatcher import PluginDispatcher


def plugin(_: str) -> type[Plugin]:
    return PluginDispatcher


__version__ = "0.0.0"
