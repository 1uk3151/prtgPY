import requests
import pandas
import yaml
import os
import pathlib

# Read parameters from yaml file
parameters_file = os.fspath(pathlib.Path(__file__).parent / 'parameters.yaml')
with open(parameters_file) as y:
    content = y.read()
parameters = yaml.load(content, Loader=yaml.FullLoader)

server_name = parameters["server_name"]
api_token = parameters["api_token"]
csv_output = parameters["csv_output"]
xml_output = parameters["xml_output"]


all_devices = []

# Get a list of all devices in the PRTG system
infourl = f"http://{server_name}/api/table.xml?content=devices&output=json&columns=objid,probe,group,device,host,tags,baselink,sensors,status&count=*&apitoken={api_token}"
response = requests.get(url=infourl, verify=False)
json_data = response.json()
devices = (json_data['devices'])


for device in devices:
    objid = device['objid']
    deviceName = device['device']
    try:
        url = f"http://{server_name}/api/table.json?id={objid}&content=sysinfo&category=system&usecaption=true&headers=key,value&columns=_key,_value&apitoken={api_token}"
        response = requests.get(url=url, verify=False)
        devicejson = response.json()
        sysinfo = devicejson['sysinfo']
 
        for i in sysinfo:
            k = "System Description" in i['key']
            if k:
                k_list = [objid, deviceName, i['key'], i['value']]
                all_devices.append(k_list)
    except:
        all_devices.append([objid, deviceName,"NO SYS INFO AVAILABLE", 0])

# Create dataframe with columns OBJID, NAME, MODEL, SN
df = pandas.DataFrame(all_devices, columns=['OBJID','NAME','ITEM','SN'])

df.to_csv(csv_output)
df.to_xml(xml_output)

    




