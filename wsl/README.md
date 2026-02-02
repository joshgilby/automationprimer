Windows Subsystem for Linux

WSL is a virtualization feature that enables one to run a linux instance (or multiple linux instances) under Windows with minimal overhead. By default, on Windows 11, WSL feature is installed by but no linux instances are deployed.

We can confirm by running the `wsl --list` wsl command, which would produce the following output:
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
wsl --install Ubuntu-24.04
```
During the installation, WSL will prompt for an administrative username and password. Enter values that you will remember. When the installation completes, WSL does not return to a command prompt. Instead it will bring up a `bash` shell on the newly-installed linux instance.

While we could start using our linux instance right away, it is useful to produce a base image for deploying new instances. In the bash shell apply updates:
```
sudo apt update && sudo apt -y upgrade && sudo shutdown -h now
```
Now, back at the command prompt, export and re-import the wsl instance:
```
mkdir wsl
cd wsl
mkdir images
mkdir instances
wsl --export Ubuntu-24.04 images\ubuntu-24.04-base.tar
wsl --import ubuntunetbox .\instances\ubuntunetbox images\ubuntu-24.04-base.tar UbuntuNetbox
```
