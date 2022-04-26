"""Tests for Codemy"""
from importlib import metadata

from codemy import __version__


def test_version():
    """Test the version matches what's expected"""
    assert __version__ == metadata.version("codemy")
