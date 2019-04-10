# -*- coding: utf-8 -*-

from gitlab.v4.objects import Project


def approvals(project: Project) -> None:
    """
    Configures how approvals work for merge requests.

    API: https://docs.gitlab.com/ee/api/merge_request_approvals.html
    """
    approvals = project.approvals.get()

    approvals.approvals_before_merge = 1
    approvals.reset_approvals_on_push = True
    approvals.disable_overriding_approvers_per_merge_request = True

    approvals.save()
