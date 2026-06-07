from collections.abc import Callable
from contextlib import suppress
from functools import wraps
from typing import ParamSpec, TypeVar

from gitlab.exceptions import GitlabCreateError

ParamT = ParamSpec('ParamT')
ReturnT = TypeVar('ReturnT')


def idempotent(
    function: Callable[ParamT, ReturnT],
) -> Callable[ParamT, ReturnT | None]:
    """Shallows 304 errors, making actions repeatable."""

    @wraps(function)
    def decorator(
        *args: ParamT.args,
        **kwargs: ParamT.kwargs,
    ) -> ReturnT | None:
        with suppress(GitlabCreateError):
            return function(*args, **kwargs)

        return None

    return decorator
