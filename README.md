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

enableLocationInheritence.py

Enables Location Inheritence on ALL devices in your PRTG system. The benefit of this is that you can add location data to groups and the devices within those groups will inherit that location. 
This helps with the GeoMap feature in PRTG. 
