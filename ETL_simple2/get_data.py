import os

command_1 = 'wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip'
os.system(command_1)

#command_1 = f'wget –P /Users/martinanikola/PycharmProjects/DataEngineering/part_2/data_for_ETL https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip'
#/Users/martinanikola/PycharmProjects/DataEngineering/part_2

comm2 = 'unzip datasource.zip -d dealership_data'