import requests
import pandas

# Parameters
server_name = "10.41.1.80"
api_token = "EIKIVEQP3BGUGITQ7FXAH4HC2QGFSISZGKKA3TYJFU======"
csv_output = "C:\\Users\\Administrator\\Documents\\ArubaSNs.csv"
xml_output = "C:\\Users\\Administrator\\Documents\\ArubaSNs.xml"

# Get a list of all devices in the PRTG system
infourl = f"http://{server_name}/api/table.xml?content=devices&output=json&columns=objid,probe,group,device,host,tags,baselink,sensors,status&count=*&apitoken={api_token}"
response = requests.get(url=infourl, verify=False)
json_data = response.json()
devices = (json_data['devices'])

# Begin parsing json data
sn_list = []
for device in devices:
    name = device['device']

    # API call will only be run on devices with 'Aruba' in the device name
    if "Aruba" in name:
        objid = device['objid']
        deviceName = device['device']
        try:
            url = f"http://{server_name}/api/table.json?id={objid}&content=sysinfo&category=system&usecaption=true&headers=key,value&columns=_key,_value&apitoken={api_token}"
            response = requests.get(url=url, verify=False)
            devicejson = response.json()
            sysinfo = devicejson['sysinfo']

            # Only entries that contain the words 'Serial Number' and 'Switch', but do not contain 'power supply' will be listed in the output. 
            for i in sysinfo:
                key = i['key']
                k = key.startswith('Serial Number')
                x = "Switch" in key
                y = "power supply" in key
                if k and x:
                    if not y:
                        k_list = [objid, deviceName, key, i['value']]
                        sn_list.append(k_list)
        except:
            sn_list.append([objid, deviceName,"NO SYS INFO AVAILABLE", 0])

# Create dataframe with columns OBJID, NAME, MODEL, SN
df = pandas.DataFrame(sn_list, columns=['OBJID','NAME','MODEL','SN'])

df.to_csv(csv_output)
df.to_xml(xml_output)

    




