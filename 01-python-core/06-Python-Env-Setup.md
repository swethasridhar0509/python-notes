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