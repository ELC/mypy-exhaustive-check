import pytest
from mypy.plugin import FunctionContext

from mypy_exhaustive_check import PluginDispatcher


@pytest.mark.usefixtures("_mock_type_to_plugin_no_plugins")
def test_plugin_dispatcher_call_no_compatible_plugins(
    function_context: FunctionContext,
    plugin_dispatcher: PluginDispatcher,
) -> None:
    result = plugin_dispatcher(function_context)
    assert result == function_context.default_return_type


@pytest.mark.usefixtures("_mock_type_to_plugin_single_plugin")
def test_plugin_dispatcher_call_with_compatible_plugins(
    function_context: FunctionContext,
    plugin_dispatcher: PluginDispatcher,
) -> None:
    result = plugin_dispatcher(function_context)

    assert result == function_context.default_return_type
