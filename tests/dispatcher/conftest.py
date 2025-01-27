from collections.abc import Callable, Generator
from typing import Union
from unittest.mock import MagicMock, patch

import pytest
from mypy.options import Options
from mypy.plugin import FunctionContext, Plugin
from mypy.types import Instance, Type

from mypy_exhaustive_check import PluginDispatcher


class DummyPlugin(Plugin):
    def get_function_hook(
        self,
        fullname: str,  # noqa: ARG002 # pylint: disable=unused-argument
    ) -> Callable[[FunctionContext], Union[Type, Instance]]:
        return self

    @staticmethod
    def is_context_compatible(_: FunctionContext) -> bool:
        return True

    @classmethod
    def type(cls) -> type[Plugin]:
        return cls

    def __call__(self, ctx: FunctionContext) -> Union[Type, Instance]:
        return ctx.default_return_type


@pytest.fixture
def function_context() -> FunctionContext:
    ctx = MagicMock(spec=FunctionContext)
    ctx.default_return_type = MagicMock(spec=Type)
    return ctx


@pytest.fixture
def plugin_dispatcher() -> PluginDispatcher:
    return PluginDispatcher(options=Options())


@pytest.fixture
def _mock_type_to_plugin_no_plugins() -> Generator[None]:
    with patch("mypy_exhaustive_check.dispatcher.dispatcher.CHECK_TYPE_TO_PLUGIN", {}):
        yield


@pytest.fixture
def dummy_plugin() -> type[Plugin]:
    return DummyPlugin


@pytest.fixture
def _mock_type_to_plugin_single_plugin(
    dummy_plugin: type[Plugin],
) -> Generator[None]:
    with patch(
        "mypy_exhaustive_check.dispatcher.dispatcher.CHECK_TYPE_TO_PLUGIN",
        {"mock_plugin": dummy_plugin},
    ):
        yield
