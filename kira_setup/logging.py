from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

from termcolor import colored

ParamT = ParamSpec('ParamT')
ReturnT = TypeVar('ReturnT')


def report_progress(
    function: Callable[ParamT, ReturnT],
) -> Callable[ParamT, ReturnT]:
    """Decorates a function to print its execution status."""

    @wraps(function)
    def decorator(
        *args: ParamT.args,
        **kwargs: ParamT.kwargs,
    ) -> ReturnT:
        try:
            function_result = function(*args, **kwargs)
        except Exception as exc:
            message = f'{function.__name__} failed due to exception: {exc}'
            print(colored(message, 'red'))  # noqa: WPS421
            raise
        else:
            message = f'{function.__name__} succeed'
            print(colored(message, 'green'))  # noqa: WPS421
            return function_result

    return decorator
