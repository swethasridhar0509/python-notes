# Python Environment Setup

## **Updating Windows Installation**

1. **Windows update** automatically downloads and installs:
    - Security patches.
    - Bug fixes.
    - Feature updates
    - Driver updates for hardware compatibility.
2. **Check for updates:** open **Settings > Windows Update**. 
    - Download and Install.
    - Restart.
    - Turn on **Automatic Updates.**
3. **Check OS version:** Press Windows + R → Press Enter.

## Managing Software in Windows

1. **Installer Files (.exe, .msi):** 
    - Manual Installation required.
    - Download the .exe file from the official site and install.
    - Manual Updates required.
2. **Package Managers:** Tools that automate software installation, updates, and removal from the terminal.
    - **Winget** (built-in/Windows 11) - contains only verified apps.
    - **Chocolatey -**  contains community apps as well.
3. Winget does not require separate installation.

## Installing and Using Chocolatey

1. **Waiver Execution Policy:**
    - Execution policy restricts users from executing shell scripts locally or from the Internet.
    - **RemoteSigned** - Allows local and signed scripts.
    - `Set-ExecutionPolicy CurrentUser RemoteSigned`
2. **Install Chocolatey**  -  `iwr -useb [community.chocolatey.org/install.ps1](http://community.chocolatey.org/install.ps1) | iex` 
3. **Check version** - `choco —version` 
4. **Install software** - `choco install <package-name> --version 3.11.4`
5. **Upgrade software** - `choco upgrade <package-name> --version <version-number>` 
6. **Uninstall** **software** - `choco uninstall <package-name>` 

## Installing Software

1. Install git - `choco install git`
2. Install VS Code - `choco install vscode`
3. Install python - `choco install python`

## Python Tools

### Pyenv - Version Management 

1. pyenv is a tool to install, manage and switch between multiple Python versions on the same system.
2. Installing pyenv - `choco install pyenv-win`
2. Installing specific version - `pyenv install 3.11.6`
3. Check all available version using - `pyenv install --list`
4. Check installed versions - `pyenv versions`
5. Set global version - `pyenv global 3.11.6` 
6. Project Specific - `pyenv local 3.11.6`


### Pip - Package Manager

1. **Pip** is the **standard package manager** for Python.
2. It allows us to install and uninstall packages that aren't part of the **Python Standard Library** from PyPI repository.
3. Check if pip is installed - `pip --version`

### Running PIP as a Module

1. Running pip directly might cause issues when,
    - Multiple python versions are installed.
    - `pip` isn't in the system `PATH`.
2. **Multiple versions** - In this case, running pip directly might result in unintended behavior. The package might get installed in the wrong version. This will result in `ModuleNotFoundError`.

### Virtual Environments

1. An Isolated Python Environment that allows us to install and manage dependencies separately for each project.
2. It contains python interpreter and packages independent of the global system.
3. **Avoid Dependency Conflicts** - different projects may require diff versions of packages.
4. **Prevent Global Pollution** - Avoid globally installing packages.
5. **Reproducible Environments** - replicate same env using `requirements.txt` file.
6. **Testing** - create virtual environments with diff python versions for testing.
7. Using `pip` inside a virtual environment will install packages only in the environment.

### Requirements Files 

1. Creating virtual environment - `python -m venv <env name>`
2. Activate environment - `env/Scripts/activate`
3. Adding packages - `pip install <package-name>`
4. Removing packages - `pip uninstall <package-name==version>`
5. By default, pip installs the latest version.
6. To reproduce the environment freeze the requirements - `pip freeze > requirements.txt`
7. To install from requirement file - `pip install -r requirements.txt`

### Poetry - Dependency Management & Packaging Tool

1. Poetry is a tool that does dependency management, virtual environment, packaging and dependency locking.
2. pyproject.toml - Contains project metadata.
3. poetry.lock - Dependency locking file. 
4. Automatic Virtual Enviroment management.
5. Install Poetry - `pip install poetry`
6. Verify - `poetry --version`


