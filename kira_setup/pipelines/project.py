# -*- coding: utf-8 -*-

from gitlab.v4.objects import Project

#: Enforces conventional commits,
#: see https://github.com/wemake-services/kira-release
regex = r'^(revert: )?(feat|fix|docs|refactor|chore)(\(.+\))?:.{1,50}refs #\d+'


def star(project: Project) -> None:
    """
    Stars the given project.

    API: https://docs.gitlab.com/ee/api/projects.html#star-a-project
    """
    project.star()


def configure(project: Project) -> None:
    """
    Configures basic things for a new project.

    API: https://docs.gitlab.com/ee/api/projects.html#edit-project
    """
    project.resolve_outdated_diff_discussions = True
    project.only_allow_merge_if_pipeline_succeeds = True
    project.only_allow_merge_if_all_discussions_are_resolved = True
    project.merge_method = 'ff'

    project.save()


def push_rules(project: Project) -> None:
    """
    Sets all required push rules for the project.

    API: https://docs.gitlab.com/ee/api/projects.html#push-rules-starter
    """
    rules = project.pushrules.get()
    rules.deny_delete_tag = True
    rules.member_check = True
    rules.prevent_secrets = True

    rules.branch_name_regex = r'^issue-\d+$'
    rules.commit_message_regex = regex

    rules.save()
