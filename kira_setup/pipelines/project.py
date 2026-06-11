from gitlab.exceptions import GitlabGetError, GitlabParsingError
from gitlab.v4.objects import Project

from kira_setup.decorators import idempotent

#: Used to enforce one-task = one-branch,
#: also has a fallback for dependabot updates:
branch_regex = r'^(issue-\d+)|(dependabot.*)|(renovate.*)|(master)$'

#: Enforces conventional commits,
#: see https://github.com/wemake-services/kira-release
commit_regex = r"""
^(revert: )?
(feat|fix|docs|build|refactor|chore)
(\(.+\))?:
.{1,50}(refs #\d+)?
"""


@idempotent
def star(project: Project) -> None:
    """
    Stars the given project.

    API: https://docs.gitlab.com/api/project_starring/
    """
    project.star()


def configure(project: Project) -> None:
    """
    Configures basic things for a new project.

    API: https://docs.gitlab.com/api/projects/#manage-projects/
    """
    project.resolve_outdated_diff_discussions = True
    project.only_allow_merge_if_pipeline_succeeds = True
    project.only_allow_merge_if_all_discussions_are_resolved = True
    project.merge_method = 'ff'

    project.save()


def push_rules(project: Project) -> None:
    """
    Sets all required push rules for the project.

    API: https://docs.gitlab.com/api/project_push_rules/

    GitLab may return either `404` or `null` when push rules have not been
    created yet. `python-gitlab` expects a dictionary response
    for `project.pushrules.get()`, so a `null` response becomes
    `None` and raises `GitlabParsingError`.

    To handle both cases, this function first tries to fetch existing push
    rules and falls back to creating them when the server reports that they
    do not exist yet.
    """
    payload = {
        'deny_delete_tag': True,
        'member_check': True,
        'prevent_secrets': True,
        'branch_name_regex': branch_regex,
        'commit_message_regex': commit_regex.replace('\n', ''),
    }

    try:
        rules = project.pushrules.get()
    except (GitlabGetError, GitlabParsingError):
        project.pushrules.create(payload)
    else:
        for rule_name, rule_value in payload.items():
            setattr(rules, rule_name, rule_value)

        rules.save()
