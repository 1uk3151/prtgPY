prtgPY is a collection of python scripts that make life easier when working with PRTG Network Monitor. 

Install the following modules with pip for full functionality:
pandas
pyyaml
requests
lxml

ex. "pip install pandas"

parameters.yaml - Use the parameters.yaml file to specify your PRTG server's hostname (or IP address), api token from PRTG (should be full access), csv output file, and xml output file. 

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
getDeviceInfo.py

Gets a list of all devices in your PRTG system. Creates a csv and xml file as output. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
enableLocationInheritence_ALL-DEVICES.py

Location Inheritence seems to be enabled by default when you first install PRTG. This script is helpful when trying to reorganize a previous PRTG build where location data was incorrectly added. 

Enables Location Inheritence on ALL devices in your PRTG system. The benefit of this is that you can add location data to groups and the devices within those groups will inherit that location. 
Groups are not labeled as devices in PRTG, so this script does not affect the Location settings for groups. This helps with the GeoMap feature in PRTG. (Ex. You have a site group that contains a number of devices. You can add location data to the site's group and have the devices within that group (at that site) inherit the location data. The groups can then be geo-mapped correctly.)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
getSysInfo_ALL.py

For network devices to have System Information populated in PRTG, SNMP must be enabled on the device and the SNMP settings must be entered into PRTG. 

This script will place all system information for all possible devices into a CSV and XML file. This includes the MAC Address for each interface and the Serial Number for the device itself plus any modules the device has installed. 

getSysInfo_MAC-Addr.py

Does the same as getSysInfo_ALL.py, but only outputs the MAC Addresses for each interface on each device. 

getSysInfo_SNs.py

Does the same as getSysInfo_ALL.py, but only outputs Serial Number information.

getSysInfo_Aruba-Switches.py

This script shows an example of how you can modify getSysInfo_ALL.py to select only specific data. This particular script will only output information for devices that contain "Aruba" in the device name. It will only output the data that contains the string "Serial Number" and "Switch", but not the string "Power Supply". By doing this, it narrows the data down to only SNs of switches with "Aruba" in the name and eliminates SNs for the modules associated with the device. You will likely need to run getSysInfo_ALL.py first and see what the data looks like before customizing the script to select specific data. 
