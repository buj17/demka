import copy

from database.models import User


class CurrentUser:
    _current_user: User | None = None

    @classmethod
    def set_current_user(cls, user: User):
        cls._current_user = user

    @classmethod
    def get_current_user(cls) -> User | None:
        return copy.deepcopy(cls._current_user)

    @classmethod
    def clear_current_user(cls):
        cls._current_user = None
