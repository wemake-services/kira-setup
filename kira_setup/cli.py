import argparse

from kira_setup.api import PIPELINE_STEPS, start_pipeline


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Project group / name')
    parser.add_argument('-t', '--token', type=str, help='Auth token')
    parser.add_argument(
        '-d',
        '--domain',
        default='gitlab.com',
        type=str,
        help='GitLab domain address, change if you use custom installation',
    )
    parser.add_argument(
        '--skip',
        action='append',
        choices=PIPELINE_STEPS.keys(),
        default=[],
        help='Skip a pipeline step, repeat this option to skip multiple steps',
    )
    return parser


def main() -> None:
    """Runs all pipeline actions."""
    parser = _create_parser()
    args = parser.parse_args()
    start_pipeline(args)
