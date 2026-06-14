import argparse
from types import MappingProxyType
from typing import Final

import gitlab
from gitlab.v4.objects import Project

from kira_setup.logging import report_progress
from kira_setup.pipelines import (
    container_registry,
    labels,
    merge_requests,
    project,
    protected,
)

PIPELINE_STEPS: Final = MappingProxyType({
    # Project:
    'star': project.star,
    'configure': project.configure,
    'push-rules': project.push_rules,
    # Merge Requests:
    'approval-rules': merge_requests.approval_rules,
    # Labels:
    'labels': labels.create_labels,
    # Protection Rules:
    'protect-branches': protected.branches,
    'protect-tags': protected.tags,
    # Container Registry:
    'cleanup-policy': container_registry.cleanup_policy,
})


def _get_project(context: argparse.Namespace) -> Project:
    gl = gitlab.Gitlab(
        f'https://{context.domain}',
        context.token,
        timeout=10,
    )

    return gl.projects.get(context.path)


def _start_pipeline(
    current_project: Project,
    context: argparse.Namespace,
) -> None:
    for step, action in PIPELINE_STEPS.items():
        if step in context.skip:
            continue

        report_progress(action)(current_project)


def start_pipeline(context: argparse.Namespace) -> None:
    """Main function to start the whole project-setup pipeline."""
    _start_pipeline(_get_project(context), context)
