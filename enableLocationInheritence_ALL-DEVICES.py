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


# Get a list of all devices in the PRTG system
infourl = f"http://{server_name}/api/table.xml?content=devices&output=json&columns=objid,probe,group,device,host,tags,baselink,sensors,status&count=*&apitoken={api_token}"
response = requests.get(url=infourl, verify=False)
json_data = response.json()
devices = (json_data['devices'])

all_devices = []

# Enable Location Inheritence on ALL devices in PRTG system. Status code 200 means that it was successful. 
objid_list = []
for device in devices:
    objid_list.append(device['objid'])

for objid in objid_list:
    url = (f"http://{server_name}/editsettings?id={objid}&locationgroup=1&apitoken={api_token}")
    response = requests.post(url=url, verify=False)
    result = [objid, response.status_code]
    all_devices.append(result)


# Print OBJID and Status Code to a CSV file. Status Code 200 means that it was successful. Look up HTTP status for more information. 
df = pandas.DataFrame(all_devices, columns=['OBJID', 'STATUS_CODE'])
df.to_csv(csv_output)





