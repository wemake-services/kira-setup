import argparse

import gitlab
from gitlab.v4.objects import Project

from kira_setup.logging import report_progress
from kira_setup.pipelines import labels, merge_requests, project, protected


def _get_project(context: argparse.Namespace) -> Project:
    gl = gitlab.Gitlab(
        f'https://{context.domain}',
        context.token,
        timeout=10,
    )

    return gl.projects.get(context.path)


def _start_pipeline(current_project: Project) -> None:
    pipeline = [
        # Project:
        project.star,
        project.configure,
        project.push_rules,
        # Merge Requests:
        merge_requests.approval_rules,
        # Labels:
        labels.create_labels,
        # Protection Rules:
        protected.branches,
        protected.tags,
    ]

    for pipeline_item in pipeline:
        report_progress(pipeline_item)(current_project)


def start_pipeline(context: argparse.Namespace) -> None:
    """Main function to start the whole project-setup pipeline."""
    _start_pipeline(_get_project(context))
