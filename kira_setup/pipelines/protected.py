# -*- coding: utf-8 -*-

import gitlab
from gitlab.v4.objects import Project


def branches(project: Project) -> None:
    """
    Creates protected branch rules.

    API: https://docs.gitlab.com/ee/api/protected_branches.html
    """
    project.protectedbranches.create({
        'name': 'master',
        'merge_access_level': gitlab.DEVELOPER_ACCESS,
        'push_access_level': gitlab.MAINTAINER_ACCESS,
    })


def tags(project: Project) -> None:
    """
    Creates protected tag rules.

    API: https://docs.gitlab.com/ee/api/protected_tags.html
    """
    project.protectedtags.create({
        'name': 'v*',
        'create_access_level': gitlab.MAINTAINER_ACCESS,
    })
