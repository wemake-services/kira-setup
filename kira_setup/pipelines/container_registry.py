from gitlab.v4.objects import Project


def cleanup_policy(project: Project) -> None:
    """
    Configure container registry cleanup policy.

    API: https://docs.gitlab.com/user/packages/container_registry/reduce_container_registry_storage/#cleanup-policy
    """
    project.container_expiration_policy_attributes = {
        'enabled': True,
        'cadence': '1d',  # Run cleanup every day
        'keep_n': 5,  # 5 newest semver tags
        'name_regex': r'^\d+\.\d+\.\d+$',  # Plain semver only
        'name_regex_keep': '^(latest|dev)$',  # Always keep
    }

    project.save()
