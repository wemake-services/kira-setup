# Version history

We follow Semantic Versions since the `1.0.0` release.
Versions before `1.0.0` are `0Ver`-based:
incremental in minor, bugfixes only are patches.


## WIP

### Features

- Added mandatory squash merge for all merge requests via `squash_option = 'always'`


## Version 0.2.2

### Bugfixes

- Fixed unsynchronized labels with `kira-stale` bot, #6
- Fixed validation labels to use `validation:*` names instead of `validation::*`,
  allowing multiple validation labels to be assigned simultaneously, #6


## Version 0.2.0

### Features

- Added support for configuring a Container Registry cleanup policy during
  project setup, #85
- Added `--skip` to selectively disable individual setup pipeline steps, #92

### Bugfixes

- Fixed setup for fresh GitLab projects where push rules do not exist yet, #89
- Fixed scoped labels to use `scope::value` names and correct priority
  handling, #93


## Version 0.1.0

- Initial release
