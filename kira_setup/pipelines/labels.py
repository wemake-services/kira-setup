# -*- coding: utf-8 -*-

from gitlab.v4.objects import Project

_LABELS = {
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

    'notification:first': '#D1D100',
    'notification:last': '#F0AD4E',
}


def _is_prioritized(label: str) -> bool:
    """
    Tells if label is prioritized or not.

    >>> _is_prioritized('feature')
    True

    >>> _is_prioritized('deadline:miss')
    False

    """
    return ':' not in label


def create(project: Project) -> None:
    """
    Creates all labels that are required for our projects.

    API: https://docs.gitlab.com/ee/api/labels.html
    """
    for label, color in _LABELS.items():
        project.labels.create({
            'name': label,
            'color': color,
            'priority': _is_prioritized(label),
        })
