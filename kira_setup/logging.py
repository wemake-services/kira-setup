# -*- coding: utf-8 -*-

from functools import wraps

from termcolor import colored


def report_progress(function):
    """Decorates a function to print its execution status."""
    @wraps(function)
    def decorator(*args, **kwargs):
        try:
            function_result = function(*args, **kwargs)
            message = '{0} succeed'.format(function.__name__)
            print(colored(message, 'green'))  # noqa: T001
            return function_result
        except Exception as exc:
            message = '{0} failed due to exception: {1}'.format(
                function.__name__, exc,
            )

            print(colored(message, 'red'))  # noqa: T001
            raise

    return decorator
