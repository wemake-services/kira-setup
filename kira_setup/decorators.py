# -*- coding: utf-8 -*-

from contextlib import suppress
from functools import wraps

from gitlab.exceptions import GitlabCreateError


def idempotent(function):
    """Shallows 304 errors, making actions repeatable."""
    @wraps(function)
    def decorator(*args, **kwargs):
        with suppress(GitlabCreateError):
            return function(*args, **kwargs)
    return decorator
