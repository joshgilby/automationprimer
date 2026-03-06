# Integrating netbox with nornir

Nornir is a powerful automation framework for performaing tasks on many devices. While nornir has a basic built in inventory system, netbox can provide more robust functionality via the NetBoxInventory2 plugin.  In this lab we will develop automations using the NetBox inventory plugin for nornir, starting with a simple configuration backup utility and working toward more advanced use cases.

## Lab Setup

This lab requires an instance of netbox, and at least one network device running Arista eos. If these are not available, check out my labs on [installing a netbox-docker instance](netbox_docker.md) and [setting up containerlab](containerlab.md).

## The Basics 

First, let's take a look at a skeletal framework for running nornir. This stub is the basis for all of the automations in this lab:

``` python {title="nornir_stub.py" linenums=1}
import pynetbox
import os
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from napalm import get_network_driver

# Gather configuration from environment
url=os.environ.get('NETBOX_URL')
token=os.environ.get('NETBOX_TOKEN')
device_user=os.environ.get('DEV_USER')
device_pass=os.environ.get('DEV_PASS')

# Initialize nornir
nr = InitNornir(
    inventory={
        "plugin":"NetBoxInventory2",
        "options": {
            "nb_url": url,
            "nb_token": token,
            "include": "config_context"
        },
        "transform_function": "load_credentials",
        "transform_function_options": {
            "username": device_user,
            "password": device_pass
        }
    }
)

# Define a task
def some_task(task:Task) -> Result:
    """
    task to be run against all devices
    """

# Execute the task
result=nr.run(task=some_task)
print_result(result)
```

Breaking down the stub:

- Lines 1-7 import dependencies
- Lines 9-13 gather configuration information from environment variables
- Lines 15-30 instantiate a nornir object, which we will use to iterate over all of our devices
- Lines 32-36 are an empty function, which we will replace with something functional
- Lines 38-40 instruct nornir to run the empty function against the device inventory and print the results

Let's expand this stub to do something useful.

## Back up Device Configuration

Now that we understand nornir basics, replace ```some_task()``` with a new function, ```config_backup()```, which fetches the configuration from a device and writes it into the local ```backups``` directory.

??? tip "Hint 1"

    The napalm configuration management library is frequently used with nornir. In particular, look at ```get_network_driver()``` and ```get_config(advanced)```. Examples are available in the [documentation for napalm](https://napalm.readthedocs.io/en/latest/tutorials/changing_the_config.html).

??? tip "Hint 2"

    When nornir invokes a task, it passes data about the target host in ```task.host``` object. We will need to reference the ```task.host.hostname```, ```task.host.username```, and ```task.host.password``` attributes.

??? example "A possible solution"

    ``` python {hl_lines="32-39 42" linenums='1'}

    import pynetbox
    import os
    from nornir import InitNornir
    from nornir.core.task import Task, Result
    from nornir_utils.plugins.functions import print_result
    from nornir_napalm.plugins.tasks import napalm_get
    from napalm import get_network_driver

    # Gather configuration from environment
    url=os.environ.get('NETBOX_URL')
    token=os.environ.get('NETBOX_TOKEN')
    device_user=os.environ.get('DEV_USER')
    device_pass=os.environ.get('DEV_PASS')

    # Initialize nornir
    nr = InitNornir(
        inventory={
            "plugin":"NetBoxInventory2",
            "options": {
                "nb_url": url,
                "nb_token": token,
                "include": "config_context"
            },
            "transform_function": "load_credentials",
            "transform_function_options": {
                "username": device_user,
                "password": device_pass
            }
        }
    )

    # Define backup function
    def config_backup(task:Task) -> Result:
        driver=get_network_driver('eos')
        device=driver( task.host.hostname, task.host.username, task.host.password )
        device.open()
        thisconfig=device.get_config()["running"]
        with open(f"backups/{task.host.name}.cfg", "w") as cfg:
            cfg.write(thisconfig)

    # Execute the task
    result=nr.run(task=config_backup)
    print_result(result)
    ```

With just a few lines of code, we now have a method for backing up our network devices in a repeatable, consistent manner. In the next section, we will use nornir to deploy configuration to devices.

## Manage Device Configuration

NetBox provides more than just a device inventory. It can also manage configuration data: interface details, IP addressing, et al. Much of this data can be modeled within NetBox itself. NetBox has built in logic to manage devices, interfaces, connections, circuits, and more. We can also use ***configuration context*** to manage data related to our network.

Simply put, configuration context is any arbitrary information that we want to associate with a NetBox object as structured data, and we can use that data in our automations. As an example, we will create a configuration context in NetBox to include the TACACS servers we want our devices to authenticate against. Our automation will configure the devices based on that configuration context.

### Create Configuration Context

### Render Intended Configuration

### Compare Device Configuration to Intent

### Apply Intended Configuration to Device
