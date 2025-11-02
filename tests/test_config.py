"""Unit tests for src/config.py."""

import importlib
from pathlib import Path
from unittest.mock import mock_open, patch

from ..src import config as c


@patch.object(Path, "open", new_callable=mock_open, read_data="v0.0.1")
def test_config_load_version_success(mocked_open):
    """Unit test for loading config (version) from file."""
    importlib.reload(c)
    assert c.VERSION == "v0.0.1"
    mocked_open.assert_called_once_with(encoding="utf-8")


@patch.object(Path, "open", side_effect=FileNotFoundError("File Not Found"))
def test_config_load_version_file_not_found(mocked_open):
    """Unit test for loading config (version) with FileNotFound exception."""
    importlib.reload(c)
    assert c.VERSION == ""
    mocked_open.assert_called_once_with(encoding="utf-8")


@patch.object(Path, "open", side_effect=PermissionError("Permission denied"))
def test_config_load_version_permission_denied(mocked_open):
    """Unit test for loading config (version) with FileNotFound exception."""
    importlib.reload(c)
    assert c.VERSION == ""
    mocked_open.assert_called_once_with(encoding="utf-8")
