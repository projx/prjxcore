# prjxCore

## Install

`pip install https://github.com/projx/prjxcore/archive/refs/tags/v0.37.tar.gz`

`python3.11 -m pip install https://github.com/projx/prjxcore/archive/refs/tags/v0.37.tar.gz`

`pip install --upgrade https://github.com/projx/prjxcore/archive/refs/tags/v0.37.tar.gz`

`pip install  git+https://github.com/projx/prjxcore.git`

`pip install --upgrade git+https://github.com/projx/prjxcore.git`

Version Note:
- [v0.37](https://github.com/projx/prjxcore/archive/refs/tags/v0.37.tar.gz) - Updated CMDRunner to be able to run Python function, as well as CLI commands
- [v0.36](https://github.com/projx/prjxcore/archive/refs/tags/v0.36.tar.gz) - Updated CMDRunner to tidy up error handling
- [v0.35](https://github.com/projx/prjxcore/archive/refs/tags/v0.35.tar.gz) - Fixed Typo
- [v0.34](https://github.com/projx/prjxcore/archive/refs/tags/v0.34.tar.gz) - Updated CMDRunner to tidy up error handling
- [v0.33](https://github.com/projx/prjxcore/archive/refs/tags/v0.33.tar.gz) - Updated KumaHook to add SSL verify supress parameter
- [v0.32](https://github.com/projx/prjxcore/archive/refs/tags/v0.32.tar.gz) - Added "load_to_dict()" to ConfigManager
- [v0.31](https://github.com/projx/prjxcore/archive/refs/tags/v0.31.tar.gz) - Added CLI wrapper "CMDRunner" along with a factory class to create CLI commands.
- [v0.27](https://github.com/projx/prjxcore/archive/refs/tags/v0.27.tar.gz) - Update ConfigManager to allow saving of seperate sections to seperate files, also added function to clear all config.
- [v0.26](https://github.com/projx/prjxcore/archive/refs/tags/v0.26.tar.gz) - Fixed couple of typos
- [v0.25](https://github.com/projx/prjxcore/archive/refs/tags/v0.25.tar.gz) - Temporarily disabled SSL check for Kuma Hook
- [v0.24](https://github.com/projx/prjxcore/archive/refs/tags/v0.24.tar.gz) - Fix for Base class 
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