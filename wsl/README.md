# Windows Subsystem for Linux / Visual Studio Code Lab

Windows Subsystem for Linux (WSL) and Visual Studio Code (VS Code) are two popular tools for network automation. Together, they provide an integrated development environment for cross-platform development. In this lab, we will deploy an instance of Ubuntu-24.04 via WSL and connect to the instance with VS Code.

## Windows Subsystem for Linux

WSL is a virtualization feature in Windows 11 that enables one to run a linux instance (or multiple linux instances) under Windows with minimal overhead. This allows developers to write code for a linux environment from within Windows. Running linux locally removes constraints around network capacity, latency, availability, and security.

### Check WSL Version

Ensure that the latest version of WSL is installed. Open a command prompt and run:

```
wsl --version
```

If necessary, upgrade WSL to the latest version (2.6.3.0 as of this writing):

```
wsl --update
```

### Install Ubuntu-24.04

By default, on Windows 11, WSL feature is installed by but no linux instances are deployed.

We can confirm by running `wsl --list` which would produce the following output:

>Windows Subsystem for Linux has no installed distributions.
>
>Use 'wsl.exe --list --online' to list available distributions
>and 'wsl.exe --install <Distro>' to install.
>    
>Distributions can also be installed by visiting the Microsoft Store:
>https://aka.ms/wslstore
>Error code: Wsl/WSL_E_DEFAULT_DISTRO_NOT_FOUND

The command `wsl --list --online` will show the linux distributions that are available to download and install.

To install Ubuntu 24.04 LTS, run the command:
```
wsl --install --distribution Ubuntu-24.04 --name ubuntu-netbox
```
During the installation, WSL will prompt for an administrative username and password. Enter values that you will remember. When the installation completes, WSL does not return to a command prompt. Instead it will bring up a `bash` shell on the newly-installed linux instance.

That completes the WSL installation. You should now have a linux instance running on your Windows host. Running `wsl -d ubuntu-netbox` from a terminal will open a shell on the linux instance. It will also show up as an app named 'ubuntu-netbox' in the start menu.

You can use the WSL instance as it is, or continue on to integrate WSL with VS Code. 

## Visual Studio Code

VS Code is an integrated development environment, combining several software development features into a single package. To start, we will use it as a file explorer, text editor, and terminal. Later, we will explore additional features such as source control, build automation, and debugging.

### Install VS Code

Visit the [Visual Studio Download page](https://code.visualstudio.com/download) and dowload the installer for your platform.

# References

WSL
- [Set up a WSL development environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment)
