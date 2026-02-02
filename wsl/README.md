Windows Subsystem for Linux

WSL is a virtualization feature that enables one to run a linux instance (or multiple linux instances) under Windows with minimal overhead. By default, on Windows 11, WSL feature is installed by but no linux instances are deployed.

We can confirm by running the wsl command. We would expect the following output:
```
wsl --list
```

>Windows Subsystem for Linux has no installed distributions.
>
>Use 'wsl.exe --list --online' to list available distributions
>and 'wsl.exe --install <Distro>' to install.
>    
>Distributions can also be installed by visiting the Microsoft Store:
>https://aka.ms/wslstore
>Error code: Wsl/WSL_E_DEFAULT_DISTRO_NOT_FOUND
