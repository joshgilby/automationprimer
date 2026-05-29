# Containerlab Deployment

Containerlab provides a virtual network environment to use for testing and development.

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

We will work with Arista's cEOS platform, as it is distributed as a container image. It is possible to run Cisco's c8000v and Palo Alto's PA-VM-KVM virtual machine images by containerizing them with vrnetlab. 


Download ```cEOS-lab-4.32.0.2F.tar``` as well as the latest cEOS-lab image:

[Arista software downloads](https://www.arista.com/en/support/software-download)

Copy the images to your containerlab project directory with ```explorer.exe .```.

Within the containerlab project directory run the command to import the images into the docker repository:

```
docker import cEOS-lab-4.32.0.2F.tar.xz ceos:4.32.0F
```

Load the latest image in the same way.

## Create Lab Configuration File

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

??? tip
    Create the file in whatever directory you will invoke containerlab using a text editor. Alternatively, you can paste the following into a bash shell:
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

## Deploy the Lab

With the topology defined, and container images loaded into the registry, we can launch the lab with the ```containerlab deploy``` command. 

This command searches the current working directory for topology files ending in .clab.yml, and launches a lab for each topology file found. In this case, it will launch the topology defined in ceos.clab.yml and should produce output similar to the following:

```
jgilby@S4n-jgilby:~/projects/containerlab$ containerlab deploy --reconfigure
13:36:59 INFO Containerlab started version=0.72.0
13:36:59 INFO Parsing & checking topology file=ceos.clab.yml
13:36:59 INFO Destroying lab name=ceos
13:36:59 INFO Removed container name=clab-ceos-ceos0
13:36:59 INFO Removed container name=clab-ceos-ceos1
13:36:59 INFO Removing host entries path=/etc/hosts
13:36:59 INFO Removing SSH config path=/etc/ssh/ssh_config.d/clab-ceos.conf
13:36:59 INFO Removing directory path=/home/jgilby/projects/containerlab/clab-ceos
13:36:59 INFO Creating lab directory path=/home/jgilby/projects/containerlab/clab-ceos
13:37:00 INFO Creating container name=ceos0
13:37:00 INFO Creating container name=ceos1
13:37:00 INFO Running postdeploy actions for Arista cEOS 'ceos1' node
13:37:00 INFO Created link: ceos0:eth1 ▪┄┄▪ ceos1:eth1
13:37:00 INFO Running postdeploy actions for Arista cEOS 'ceos0' node
13:37:29 INFO Adding host entries path=/etc/hosts
13:37:29 INFO Adding SSH config for nodes path=/etc/ssh/ssh_config.d/clab-ceos.conf
13:37:29 INFO containerlab version
  🎉=
  │ A newer containerlab version (0.74.3) is available!
  │ Release notes: https://containerlab.dev/rn/0.74/#0743
  │ Run 'clab version upgrade' or see https://containerlab.dev/install/ for other installation options.
╭─────────────────┬──────────────┬─────────┬───────────────────╮
│       Name      │  Kind/Image  │  State  │   IPv4/6 Address  │
├─────────────────┼──────────────┼─────────┼───────────────────┤
│ clab-ceos-ceos0 │ arista_ceos  │ running │ 172.20.20.3       │
│                 │ ceos:4.32.0F │         │ 3fff:172:20:20::3 │
├─────────────────┼──────────────┼─────────┼───────────────────┤
│ clab-ceos-ceos1 │ arista_ceos  │ running │ 172.20.20.2       │
│                 │ ceos:4.32.0F │         │ 3fff:172:20:20::2 │
╰─────────────────┴──────────────┴─────────┴───────────────────╯
```

You can see the state of your lab with the ```containerlab inspect``` command, or decommission the lab with ```containerlab destroy```. See ```containerlab -h``` for all available commands.

## Connect to a Lab Device

Run ```ssh admin@172.20.20.2``` with the default password of 'admin' to connect to a lab device.

!!! success
    You now have a virtual network to develop against.

    ## Next Steps

    ### Learn more about containerlab
    
    - [containerlab home page](https://containerlab.dev/)
    - [vrnetlab - containerize a VM](https://github.com/ipspace/vrnetlab)
