#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from kira_setup.api import start_pipeline


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
    return parser


def main() -> None:
    """Runs all pipeline actions."""
    parser = _create_parser()
    args = parser.parse_args()
    start_pipeline(args)
