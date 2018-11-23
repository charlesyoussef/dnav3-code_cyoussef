import os
import sys
import requests
from pprint import pprint

requests.packages.urllib3.disable_warnings()

here = os.path.abspath(os.path.dirname(__file__))

there1 = os.path.abspath(os.path.join(here, "..\.."))
there2 = os.path.abspath(os.path.join(here, "../.."))

sys.path.insert(0,there1)
sys.path.insert(0,there2)
import env_lab

dnac_host = env_lab.DNA_CENTER["host"]
dnac_port = env_lab.DNA_CENTER["port"]
dnac_username = env_lab.DNA_CENTER["username"]
dnac_password = env_lab.DNA_CENTER["password"]

def get_token(host, port, user, passwd):
    login_url = "https://{0}:{1}/api/system/v1/auth/token".format(host, port)
    result = requests.post(login_url, auth=requests.auth.HTTPBasicAuth(user, passwd), verify=False)
    output = result.json()
    token = output["Token"]
    return token

def form_url(host, port, object):
    return "https://{0}:{1}/api/v1/{2}".format(host, port, object)


def get_uri_with_token (host, port, token, url_suffix):
    uri = form_url(host, port, url_suffix)
    headers = {'X-auth-token': token}
    try:
        response = requests.get(uri, headers=headers, verify=False)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit()
    return response.json()

def ip_to_id(ip):
    token = get_token(dnac_host, dnac_port, dnac_username, dnac_password)
    suffix = "network-device?managementIpAddress=" + str(ip)
    response = get_uri_with_token(dnac_host, dnac_port, token, suffix)
    return response["response"][0]["id"]

def get_modules(id):
    token = get_token(dnac_host, dnac_port, dnac_username, dnac_password)
    suffix = "network-device/module?deviceId={}".format(id)
    return get_uri_with_token(dnac_host, dnac_port, token, suffix)

def print_info(modules):
    print("{0:30}{1:30}{2:30}{3:30}".format("Module Name", "Serial Number", "Part Number", "Field Replaceable"))
    for module in modules["response"]:
        MSN = "N/A" if module["serialNumber"] == '' else module["serialNumber"]
        MPN = "N/A" if module["partNumber"] == '' else module["partNumber"]
        print("{0:30}{1:30}{2:30}{3:30}".format(module["name"], MSN, MPN, module["isFieldReplaceable"]))


def main():
    if len(sys.argv) > 1:
        device_ip_address = sys.argv[1]
    else:
        print("Usage of the script is: python putting_it_all_together_my_version.py IP_address_of_device.")
        sys.exit()
    token = get_token(dnac_host, dnac_port, dnac_username, dnac_password)
    """
    suffix = "network-device"
    response = get_uri_with_token(dnac_host, dnac_port, token, suffix)
    device_list = response["response"]
    print("{0:30}{1:30}{2:30}{3:30}".format("Hostname", "IP address", "Platform", "Uptime"))
    for device in device_list:
        uptime = "N/A" if device["upTime"] is None else device["upTime"]
        print("{0:30}{1:30}{2:30}{3:30}".format(device["hostname"], device["managementIpAddress"], device["platformId"], uptime))
    """
    dev_id = ip_to_id(device_ip_address)
    modules = get_modules(dev_id)
    print_info(modules)


if __name__ == '__main__':
    main()

