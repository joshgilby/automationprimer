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

The command `wsl --list --online` will show the linux distributions that are available to download and install:
<pre><code>
</code> The following is a list of valid distributions that can be installed.
Install using 'wsl.exe --install <Distro>'.
 
NAME                            FRIENDLY NAME
Ubuntu                          Ubuntu
Debian                          Debian GNU/Linux
kali-linux                      Kali Linux Rolling
Ubuntu-20.04                    Ubuntu 20.04 LTS
Ubuntu-22.04                    Ubuntu 22.04 LTS
Ubuntu-24.04                    Ubuntu 24.04 LTS
OracleLinux_7_9                 Oracle Linux 7.9
OracleLinux_8_10                Oracle Linux 8.10
OracleLinux_9_5                 Oracle Linux 9.5
openSUSE-Leap-15.6              openSUSE Leap 15.6
SUSE-Linux-Enterprise-15-SP6    SUSE Linux Enterprise 15 SP6
openSUSE-Tumbleweed             openSUSE Tumbleweed
</code></pre>

To install Ubuntu 24.04 LTS, run the command:
```
wsl --install Ubuntu-24.04
```
