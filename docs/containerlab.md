# Containerlab Deployment

## Install Containerlab

```
curl -sL https://containerlab.dev/setup | sudo -E bash -s "all"
```

## Download Network Device Images

We will work with two device platforms, Arista's cEOS and Cisco's c8000v. 

## Create Lab Configuration file

```
cat << EOF >>> ceos.clab.yml
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

