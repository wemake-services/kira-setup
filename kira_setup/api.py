# -*- coding: utf-8 -*-

import gitlab
from gitlab.v4.objects import Project

from kira_setup.logging import report_progress
from kira_setup.pipelines import labels, merge_requests, project, protected


def _get_project(context) -> Project:
    gl = gitlab.Gitlab(
        'https://' + context.domain,
        context.token,
        timeout=10,
    )

    return gl.projects.get(context.path[0])


def _start_pipeline(current_project: Project) -> None:
    pipeline = [
        project.star,
        project.configure,
        project.push_rules,

        merge_requests.approvals,

        labels.create,

        protected.branches,
        protected.tags,
    ]

    for pipeline_item in pipeline:
        report_progress(pipeline_item)(current_project)  # type: ignore


def start_pipeline(context) -> None:
    """Main function to start the whole project-setup pipeline."""
    current_project = _get_project(context)
    _start_pipeline(current_project)
