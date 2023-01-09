# prjxCore

## Install

`pip install https://github.com/projx/prjxcore/archive/refs/tags/v0.22.tar.gz`

'pip install --upgrade https://github.com/projx/prjxcore/archive/refs/tags/v0.23.tar.gz'

`pip install  git+https://github.com/projx/prjxcore.git`

`pip install --upgrade git+https://github.com/projx/prjxcore.git`

Version Note:
- [v0.23](https://github.com/projx/prjxcore/archive/refs/tags/v0.23.tar.gz) - Added Factory class, This is utility class for loading/saving (pickling) objects, also has functions for creating references to classes and functions, so they can be dynamically created.
- [v0.22](https://github.com/projx/prjxcore/archive/refs/tags/v0.22.tar.gz) - Updated ConfigManager with new functions
- [v0.21](https://github.com/projx/prjxcore/archive/refs/tags/v0.21.tar.gz) - Fix AppLog output format
- [v0.20](https://github.com/projx/prjxcore/archive/refs/tags/v0.20.tar.gz) - Removed debug code caused unecessary output
- [v0.19](https://github.com/projx/prjxcore/archive/refs/tags/v0.19.tar.gz) - Added Uptime Kuma webhook manager.
- [v0.18](https://github.com/projx/prjxcore/archive/refs/tags/v0.18.tar.gz) - Tweaks to ConfigManager.
- [v0.17](https://github.com/projx/prjxcore/archive/refs/tags/v0.17.tar.gz) - Fixed AppLog constructor, which was not passing the file-logging path through
- [v0.16](https://github.com/projx/prjxcore/archive/refs/tags/v0.16.tar.gz) - Tweaks
- v0.15 - Added set_section() and create "main" default section in ConfigManager
- v0.14 - Added AppTimer, provide a stopwatch for function / app execution time.
- v0.13 - Added ConfigManager.set_all() to allow setting on all elements progmatically.
- v0.12 - Initial split out.