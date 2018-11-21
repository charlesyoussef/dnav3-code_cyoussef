#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    json_data = file.read()


# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.

dict_data = json.loads(json_data)
print("Following are the interfaces along with their IP address information:")
for interface in dict_data["ietf-interfaces:interfaces"]["interface"]:
    interface_address_info = interface["ietf-ip:ipv4"]["address"][0]
    print(" The interface name is {}, the IP address is {}, the subnet is {}.".format(interface["name"],interface_address_info["ip"], interface_address_info["netmask"]))
