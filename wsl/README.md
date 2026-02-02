Windows Subsystem for Linux

WSL is a virtualization feature that enables one to run a linux instance (or multiple linux instances) under Windows with minimal overhead. On Windows 11, WSL is installed by default.

To verify that WSL is installed, open a command prompt and run:

```
wsl --version
```

The command should output the version of WSL and related Windows components.

```
wsl --list
```

    Windows Subsystem for Linux has no installed distributions.
    
    Use 'wsl.exe --list --online' to list available distributions
    and 'wsl.exe --install <Distro>' to install.
    
    Distributions can also be installed by visiting the Microsoft Store:
    https://aka.ms/wslstore
    Error code: Wsl/WSL_E_DEFAULT_DISTRO_NOT_FOUND
