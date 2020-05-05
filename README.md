# OpenMiner Website

[![License](https://img.shields.io/badge/license-LGPLv2.1%2B-blue.svg)](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html)

## Description

This is the official [OpenMiner](https://github.com/Unarelith/OpenMiner) website source code.

This website acts as a content database for the [launcher](https://github.com/Unarelith/openminer_launcher) and a running instance can be found [here](https://openminer.app).

## Dependencies

- Python 3
- pip

## How to use

### With virtualenv (recommended)

- Run `virtualenv myenv`
- Run `source myenv/bin/activate` (the name may be different depending on your shell)
- Run `pip install -r requirements.txt` (only if the previous command worked)
- Run `./manage.py migrate`
- Run `./manage.py runserver`

**Note:** You'll need to run `source myenv/bin/activate` before using `manage.py` if you closed your shell.

### Without virtualenv (not recommended)

- Run `sudo pip install -r requirements.txt`
- Run `./manage.py migrate`
- Run `./manage.py runserver`

**Note:** This method is not recommended because it will install `openminer_web` dependencies to your system instead of using a local folder.

## License

The code is licensed under LGPL v2.1.

