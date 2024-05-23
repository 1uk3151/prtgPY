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


# Pull RenamingTemplate.csv into a dataframe
renamingTemplate = os.fspath(pathlib.Path(__file__).parent / 'RenamingTemplate.csv')
df = pandas.read_csv(renamingTemplate)

for x in range(len(df.index)):
    row = df.loc[x]
    objid = row.OBJID
    newName = f"{row.NEW_NAME} ({row.HOST})"
    url = f"http://{server_name}/api/rename.htm?id={objid}&value={newName}&apitoken={api_token}"
    response = requests.post(url=url, verify=False)


