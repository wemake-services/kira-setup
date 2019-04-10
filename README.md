# Kira Setup Bot

[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)
[![kira-family](https://img.shields.io/badge/kira-family-pink.svg)](https://github.com/wemake-services/kira)
[![Build Status](https://travis-ci.org/wemake-services/kira-setup.svg?branch=master)](https://travis-ci.org/wemake-services/kira-setup)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/wemake-services/kira-setup/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

CLI utility to automate routine work with creating new projects.

Part of the [`@kira`](https://github.com/wemake-services/kira) bots family.


## Installation

```
pip install kira-setup
```

## Running

```
kira-setup group_or_user_name/project_name --token=YOUR_ACCESS_TOKEN
```

## Features

We use this CLI to setup high quality standards for our repository.
Features that we care about:
1. Protected `master` and tags for releases only
2. Mandatory code reviews
3. Integration with [`kira-stale`](https://github.com/wemake-services/kira-stale) and [`kira-release`](https://github.com/wemake-services/kira-release)
