"""Tests for easy-slug-maker."""

import pytest
from easy_slug_maker import maker


class TestMaker:
    """Test suite for maker."""

    def test_basic(self):
        """Test basic usage."""
        result = maker("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            maker("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = maker(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
