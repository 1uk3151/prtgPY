Install the following modules with pip:
pandas
pyyaml
requests
lxml

Use the parameters.yaml file to specify your PRTG server's hostname (or IP address), api token from PRTG (should be full access), csv output file, and xml output file. 

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
getDeviceInfo.py

Gets a list of all devices in your PRTG system. Creates a csv and xml file as output. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
enableLocationInheritence_ALL-DEVICES.py

Location Inheritence seems to be enabled by default on all devices. This script is helpful when trying to reorganize a previous PRTG build where location data was incorrectly added. 

Enables Location Inheritence on ALL devices in your PRTG system. The benefit of this is that you can add location data to groups and the devices within those groups will inherit that location. 
Groups are not labeled as devices in PRTG, so this script does not affect the Location settings for groups. This helps with the GeoMap feature in PRTG. (Ex. You have a site group that contains a number of devices. You can add location data to the site's group and have the devices within that group (at that site) inherit the location data. The groups can then be geo-mapped correctly.)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
