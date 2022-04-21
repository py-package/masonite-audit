"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
from src.masonite_audit.mixins import Audit


class User(Model, SoftDeletesMixin, Authenticates, Audit):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __hidden__ = ["password"]
    __auth__ = "email"
