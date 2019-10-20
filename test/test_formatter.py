"""Test Formatter"""

from src.formatter import format_row


def test_formatter(mocker):
    """Docstring"""
    assert format_row(mocker) == 2
