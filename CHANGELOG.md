# Version history

We follow Semantic Versions since the `1.0.0` release.
Versions before `1.0.0` are `0Ver`-based:
incremental in minor, bugfixes only are patches.


## Version 0.2.0

- Added support for configuring a Container Registry cleanup policy during
  project setup.
- Added `--skip` to selectively disable individual setup pipeline steps.
- Fixed setup for fresh GitLab projects where push rules do not exist yet.
- Fixed scoped labels to use `scope::value` names and correct priority
  handling.


## Version 0.1.0

- Initial release
