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

## Download Network Device Images

We will work with two device platforms, Arista's cEOS and Cisco's c8000v. 

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
