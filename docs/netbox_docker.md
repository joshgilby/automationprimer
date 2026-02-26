# Install NetBox Community Docker Image

The open source edition of NetBox is conveniently distributed as a docker image. We will walk through the installation on Ubuntu 24.04.

## Update Linux Environment and Install Prerequisites

```
sudo apt -y update && sudo apt -y upgrade
sudo apt -y install git docker.io docker-compose-v2 python3.12-venv
sudo usermod -a -G docker `whoami`
sudo reboot
```
## Clone the ```netbox-docker``` Repository

```
mkdir -p ~/projects && cd ~/projects
git clone -b release https://github.com/netbox-community/netbox-docker.git
cd netbox-docker
```

## Deploy the Image

Deployment depends on settings in ```docker-compose.override.yml```. We can copy the example file and edit it if needed:

```
cp docker-compose.override.yml.example docker-compose.override.yml
```

Now we can bring up the docker instance:

```
docker compose pull
docker compose up
```

When docker compose completes, it may indicate that the netbox-docker-netbox-1 container is unhealthy. This is usually not a problem. The container is still starting up and will complete in a few minutes.

When the netbox installation is complete, you will see the netbox homepage at http://localhost:8000

Finally, create an administrative user for NetBox:

```
docker compose exec netbox /opt/netbox/netbox/manage.py createsuperuser
```

# Further Reading
- [netbox-docker Repository](https://github.com/netbox-community/netbox-docker)