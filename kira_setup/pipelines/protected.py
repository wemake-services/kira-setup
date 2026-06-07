from gitlab import const
from gitlab.v4.objects import Project

from kira_setup.decorators import idempotent


@idempotent
def branches(project: Project) -> None:
    """
    Creates protected branch rules.

    API: https://docs.gitlab.com/ee/api/protected_branches.html
    """
    project.protectedbranches.create({
        'name': 'master',
        'merge_access_level': const.DEVELOPER_ACCESS,
        'push_access_level': const.MAINTAINER_ACCESS,
    })


@idempotent
def tags(project: Project) -> None:
    """
    Creates protected tag rules.

    API: https://docs.gitlab.com/ee/api/protected_tags.html
    """
    project.protectedtags.create({
        'name': 'v*',
        'create_access_level': const.MAINTAINER_ACCESS,
    })
