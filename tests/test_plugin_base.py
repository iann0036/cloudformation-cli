# fixture and parameter have the same name
# pylint: disable=redefined-outer-name,useless-super-delegation,protected-access
from unittest.mock import call, patch

import pytest
from rpdk.core.filters import FILTER_REGISTRY
from rpdk.core.plugin_base import LanguagePlugin, __name__ as plugin_base_name


class TestLanguagePlugin(LanguagePlugin):
    MODULE_NAME = __name__

    def init(self, project):
        return super().init(project)

    def generate(self, project):
        return super().generate(project)

    def package(self, project, zip_file):
        return super().package(project, zip_file)


@pytest.fixture
def plugin():
    return TestLanguagePlugin()


def test_language_plugin_module_not_set():
    # overriding the abstract method set means an abstract class can be instantiated
    with patch.object(LanguagePlugin, "__abstractmethods__", set()):
        plugin = LanguagePlugin()  # pylint: disable=abstract-class-instantiated
    with pytest.raises(RuntimeError):
        plugin._module_name  # pylint: disable=pointless-statement


def test_language_plugin_init_no_op(plugin):
    plugin.init(None)


def test_language_plugin_generate_no_op(plugin):
    plugin.generate(None)


def test_language_plugin_package_no_op(plugin):
    plugin.package(None, None)


def test_language_plugin_setup_jinja_env_defaults(plugin):
    env = plugin._setup_jinja_env()
    assert env.loader
    assert env.autoescape

    for name in FILTER_REGISTRY:
        assert name in env.filters

    assert env.get_template("test.txt")


def test_language_plugin_setup_jinja_env_overrides(plugin):
    loader = object()
    autoescape = object()
    env = plugin._setup_jinja_env(autoescape=autoescape, loader=loader)
    assert env.loader is loader
    assert env.autoescape is autoescape

    for name in FILTER_REGISTRY:
        assert name in env.filters


def test_language_plugin_setup_jinja_env_no_spec(plugin):
    with patch(
        "rpdk.core.plugin_base.importlib.util.find_spec", return_value=None
    ) as mock_spec, patch("rpdk.core.plugin_base.PackageLoader") as mock_loader:
        env = plugin._setup_jinja_env()

    mock_spec.assert_called_once_with(plugin._module_name)
    mock_loader.assert_has_calls([call(plugin._module_name), call(plugin_base_name)])

    assert env.loader
    assert env.autoescape

    for name in FILTER_REGISTRY:
        assert name in env.filters
