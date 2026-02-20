# Install NetBox Community as Docker Image

The open source edition of NetBox is conveniently distributed as a docker image. We will walk through the installation on Ubuntu 24.04.

## Update Linux Environment and Install Prerequisites

```
sudo apt -y update && sudo apt -y upgrade
sudo apt -y install git docker.io docker-compose-v2 python3.12-venv
sudo usermod -a -G docker `whoami`
sudo reboot
```
## Clone the ```netbox-docker``` repository

```
mkdir -p ~/projects && cd ~/projects
git clone -b release https://github.com/netbox-community/netbox-docker.git
cd netbox-docker
```