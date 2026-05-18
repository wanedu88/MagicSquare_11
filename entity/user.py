"""User entity for the MagicSquare domain."""

from dataclasses import dataclass


EMAIL_SEPARATOR = "@"


@dataclass(frozen=True)
class User:
    """Represents a MagicSquare user.

    Attributes:
        name: Human-readable user name.
        email: User email address.
    """

    name: str
    email: str

    def __post_init__(self) -> None:
        """Validate user attributes after initialization.

        Raises:
            ValueError: If the name is empty or the email address is invalid.
        """
        normalized_name = self.name.strip()
        if not normalized_name:
            raise ValueError("name must not be empty")

        if EMAIL_SEPARATOR not in self.email:
            raise ValueError("email must contain @")

        object.__setattr__(self, "name", normalized_name)

    def display_name(self) -> str:
        """Return the user name for display.

        Returns:
            The user's display name.
        """
        return self.name
