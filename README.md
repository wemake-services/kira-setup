# Kira Setup Bot

[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake-services.github.io)
[![kira-family](https://img.shields.io/badge/kira-family-pink.svg)](https://github.com/wemake-services/kira)
[![Build Status](https://github.com/wemake-services/kira-setup/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/wemake-services/kira-setup/actions/workflows/test.yml)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/wemake-services/kira-setup/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

CLI utility to automate routine work with new projects.

Part of the [`@kira`](https://github.com/wemake-services/kira) bots family.

`kira-setup` does not create a repository. It configures an existing GitLab
project so new repositories start with the same engineering standards.

## Features

- [x] Configures GitLab project defaults for a stricter merge flow
- [x] Requires passing pipelines before merge
- [x] Requires all discussions to be resolved before merge
- [x] Sets fast-forward only merge strategy
- [x] Configures merge request approval rules
- [x] Protects the `master` branch and release tags matching `v*`
- [x] Enforces push rules for branch names and commit messages
- [x] Prevents secret pushes and enables member checks
- [x] Creates a standard label set for triage and workflow
- [x] Configures container registry cleanup policy

## Installation

Requirements:

- Python 3.11+
- An existing GitLab project
- A GitLab access token with permission to manage project settings

```bash
pip install kira-setup
```

## Quick Start

Run the CLI against an existing project:

```bash
kira-setup group-or-user/project-name --token YOUR_ACCESS_TOKEN
```

For self-hosted GitLab:

```bash
kira-setup group-or-user/project-name \
  --token YOUR_ACCESS_TOKEN \
  --domain gitlab.example.com
```

To skip specific setup steps, repeat `--skip` with the stable step name:

```bash
kira-setup group-or-user/project-name \
  --token YOUR_ACCESS_TOKEN \
  --skip labels \
  --skip protect-tags
```

Available `--skip` values:

- `star`
- `configure`
- `push-rules`
- `approval-rules`
- `labels`
- `protect-branches`
- `protect-tags`
- `cleanup-policy`

## Why Use It

We use this CLI to make repository setup repeatable across projects.
Instead of applying the same GitLab rules manually every time, `kira-setup`
brings a new repository to the expected baseline in a single command.

## Related Projects

- [`kira`](https://github.com/wemake-services/kira): the full bots family
- [`kira-stale`](https://github.com/wemake-services/kira-stale): stale issue and
  pull request automation
- [`kira-release`](https://github.com/wemake-services/kira-release): automated
  semantic releases
