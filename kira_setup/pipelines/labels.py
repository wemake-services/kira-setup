from types import MappingProxyType
from typing import Final

from gitlab.v4.objects import Project

from kira_setup.decorators import idempotent

_LABELS: Final = MappingProxyType({
    # Common:
    'bug': '#FF0000',
    'feature': '#428BCA',
    'documentation': '#69D100',
    'research': '#5843AD',
    'dependencies': '#0080ff',
    # Deadline:
    'deadline::soft': '#AD4363',
    'deadline::hard': '#D10069',
    'deadline::miss': '#CC0033',
    # Validation:
    'validation::labels': '#A295D6',
    'validation::stale': '#A295D6',
    'validation::invalid': '#7F8C8D',
    'validation::estimate': '#D9534F',
    # Notification:
    'notification::first': '#D1D100',
    'notification::last': '#F0AD4E',
    # Merge Request:
    'mr::processed': '#E6E6FA',
})


def _is_prioritized(label: str) -> int:
    """
    Tells if label is prioritized or not.

    >>> assert _is_prioritized('feature')
    >>> assert not _is_prioritized('deadline:miss')

    """
    return 0 if '::' in label else 1


def create_labels(project: Project) -> None:
    """
    Creates all labels that are required for our projects.

    API: https://docs.gitlab.com/api/labels/
    """
    safe_create = idempotent(project.labels.create)
    for label, color in _LABELS.items():
        safe_create({
            'name': label,
            'color': color,
            'priority': _is_prioritized(label),
        })
