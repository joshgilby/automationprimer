# Network Automation Primer
Infrastructure automation workshop for network engineers

## Overview
This workshop consists of a collection of labs to provide network engineers with an introduction to some of the tools and practices used in infrastructure automation. The labs are highly prescriptive with the intent of building a development environment and installing common tools with as little fuss as possible.

### What to Expect

Attendees can follow the introductory labs to stand up useful tools. These labs are not intended to provide anything beyond a cursory knowledge of the covered material. There is plenty of instructive material on the Internet, but it often makes assumptions, i.e. that the reader has access to a Linux instance. We aim to fill that gap by giving engineers a way to easily and reliably build an environment to develop automations without getting bogged down in the details of underlying components.

### How to use the Labs

Labs can be completed in any order as long as you meet the prerequisites. However, each lab ends with a collection of next steps. An engineer with no prior automation or Linux experience can follow the [WSL/VS Code](wsl_vscode.md) and [netbox-docker](netbox_docker.md) labs to set up a test NetBox instance without havint to learn about Linux, docker, et al. Another engineer with programming exprience might delve straight into the [netbox/nornir](netbox_nornit.md) lab.

## Prerequisites
- Attendees should have some familiarity working from a linux command line (bash)
- The labs assume a native Windows 11 environment
!!! warning

    Many labs will not work under Parallels! Attendees running OSX will need to deploy a linux VM, which is beyond the scope of this workshop.

- Intel hardware is required for most containerlab images

## Available Labs

### Introductory

- [Set up a development environment with WSL and VS Code](wsl_vscode.md)
- [Install NetBox docker image](netbox_docker.md)
- [Install Containerlab](containerlab.md) - Work in progress

### Intermediate

- [Integrate NetBox with nornir](netbox_nornir.md) - Work in progress

## Upcoming Labs
- [NetBox Introduction](netbox_intro.md)
- git
- ansible
- python
- NetBox deep dive

## Helpful Resources
- [Linux Fundamentals Course](https://www.geeksforgeeks.org/linux-unix/introduction-to-linux-operating-system/)
- [Windows Subsystem for Linux Documentation](https://learn.microsoft.com/en-us/windows/wsl/)
- [Visual Studio Code documentation](https://code.visualstudio.com/docs)
- [github training manual](https://githubtraining.github.io/training-manual/#/)
