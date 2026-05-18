"""Tests for the User entity."""

import pytest

from entity.user import User


def test_user_stores_name_and_email() -> None:
    """Store valid user attributes."""
    # Arrange & Act
    user = User(name="Alice", email="alice@example.com")

    # Assert
    assert user.name == "Alice"
    assert user.email == "alice@example.com"


def test_user_strips_name_whitespace() -> None:
    """Normalize surrounding whitespace from user names."""
    # Arrange & Act
    user = User(name="  Alice  ", email="alice@example.com")

    # Assert
    assert user.name == "Alice"


def test_display_name_returns_user_name() -> None:
    """Return the user's display name."""
    # Arrange
    user = User(name="Alice", email="alice@example.com")

    # Act & Assert
    assert user.display_name() == "Alice"


def test_user_rejects_empty_name() -> None:
    """Reject empty user names."""
    # Act & Assert
    with pytest.raises(ValueError, match="name must not be empty"):
        User(name="", email="alice@example.com")


def test_user_rejects_invalid_email() -> None:
    """Reject email values without an at sign."""
    # Act & Assert
    with pytest.raises(ValueError, match="email must contain @"):
        User(name="Alice", email="alice.example.com")
