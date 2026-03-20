# Containerlab Deployment

!!! warning

    This lab is a work in progress. Do not expect things to work :) .

## Install Containerlab

Create a containerlab project directory:

```
mkdir ~/projects/containerlab && cd ~/projects/containerlab
```

Run the containerlab install script:

```
bash -c "$(curl -sL https://get.containerlab.dev)"
```

Add your user to the clab_admins group:
```
sudo usermod -aG clab_admins `whoami` && newgrp clab_admins
```

## Download Network Device Images

We will work with two device platforms, Arista's cEOS and Cisco's c8000v. 

[Arista software downloads](https://www.arista.com/en/support/software-download)

Download ```cEOS-lab-4.32.0.2F.tar``` as well as the latest cEOS-lab image.

[Cisco software downloads](https://software.cisco.com/download/home)

Download ```c8000v-universalk9_16G_serial.17.15.04c.qcow2```

Copy the images to your containerlab project directory with ```explorer.exe .```.

Within the containerlab project directory run the command to import the images into the docker repository:

```
docker import cEOS-lab-4.32.0F.tar.xz ceos:4.32.0F
```

Load the latest image in the same way.

## Create Lab Configuration file

``` yaml {title="ceos.clab.yml"}
name: ceos

topology:
  nodes:
    ceos0:
      kind: arista_ceos
      image: ceos:4.32.0F
    ceos1:
      kind: arista_ceos
      image: ceos:4.32.0F

  links:
    - endpoints: ["ceos0:eth1", "ceos1:eth1"]
```

``` yaml {title="paste into terminal"}
cat << EOF > ceos.clab.yml
name: ceos

topology:
  nodes:
    ceos0:
      kind: arista_ceos
      image: ceos:4.32.0F
    ceos1:
      kind: arista_ceos
      image: ceos:4.32.0F

  links:
    - endpoints: ["ceos0:eth1", "ceos1:eth1"]
EOF
```

## Helpful resources
- [containerlab home page](https://containerlab.dev/)
- [vrnetlab - containerize a VM](https://github.com/ipspace/vrnetlab) - confirmed
- [building c8000v as a container](https://netlab.tools/labs/cat8000v/) - unconfirmed