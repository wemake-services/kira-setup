# -*- coding: utf-8 -*-

import gitlab
from gitlab.v4.objects import Project

from kira_setup.logging import report_progress
from kira_setup.pipelines import labels, merge_requests, project, protected


def _get_project(context) -> Project:
    gl = gitlab.Gitlab(
        'https://{0}'.format(context.domain),
        context.token,
        timeout=10,
    )

    return gl.projects.get(context.path)


def _start_pipeline(current_project: Project) -> None:
    pipeline = [
        project.star,
        project.configure,
        project.push_rules,

        merge_requests.approval_rules,

        labels.create_labels,

        protected.branches,
        protected.tags,
    ]

    for pipeline_item in pipeline:
        report_progress(pipeline_item)(current_project)  # type: ignore


def start_pipeline(context) -> None:
    """Main function to start the whole project-setup pipeline."""
    _start_pipeline(_get_project(context))
