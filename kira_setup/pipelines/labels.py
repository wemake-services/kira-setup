# -*- coding: utf-8 -*-

from types import MappingProxyType

from gitlab.v4.objects import Project

from kira_setup.decorators import idempotent

_LABELS = MappingProxyType({
    'bug': '#FF0000',
    'feature': '#428BCA',
    'documentation': '#69D100',
    'research': '#5843AD',

    'deadline:soft': '#AD4363',
    'deadline:hard': '#D10069',
    'deadline:miss': '#CC0033',

    'validation:labels': '#A295D6',
    'validation:stale': '#A295D6',
    'validation:invalid': '#7F8C8D',
    'validation:estimate': '#D9534F',

    'notification:first': '#D1D100',
    'notification:last': '#F0AD4E',
})


def _is_prioritized(label: str) -> int:
    """
    Tells if label is prioritized or not.

    >>> assert _is_prioritized('feature')
    >>> assert not _is_prioritized('deadline:miss')

    """
    return 0 if ':' in label else 1


def create_labels(project: Project) -> None:
    """
    Creates all labels that are required for our projects.

    API: https://docs.gitlab.com/ee/api/labels.html
    """
    safe_create = idempotent(project.labels.create)  # type: ignore
    for label, color in _LABELS.items():
        safe_create({
            'name': label,
            'color': color,
            'priority': _is_prioritized(label),
        })
