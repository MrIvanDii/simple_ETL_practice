import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

tmpfile = "dealership_temp.tmp"               # file used to store all extracted data
logfile = "dealership_logfile.txt"            # all event logs will be stored in this file
targetfile = "dealership_transformed_data.csv"   # file where transformed data is stored

#CSV extract Function
def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe
#extract_from_csv('/Users/martinanikola/PycharmProjects/DataEngineering/part_2/dealership_data/used_car_prices1.csv')

#JSON Extract Function
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe
#print(extract_from_csv('/Users/martinanikola/PycharmProjects/DataEngineering/part_2/dealership_data/used_car_prices1.json'))

#XML Extract Function
def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for car in root:
        car_model = car.find("car_model").text
        year_of_manufacture = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        dataframe = dataframe.append({"car_model": car_model, "year_of_manufacture": year_of_manufacture, "price": price, "fuel": fuel}, ignore_index=True)
    return dataframe
#print(extract_from_xml('/Users/martinanikola/PycharmProjects/DataEngineering/part_2/dealership_data/used_car_prices1.xml'))

# Extract Function
def extract():
    extracted_data = pd.DataFrame(
        columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])

    # process all csv files
    for csvfile in glob.glob("dealership_data/*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)

        # process all json files
        for jsonfile in glob.glob("dealership_data/*.json"):
            extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)

        # process all xml files
        for xmlfile in glob.glob("dealership_data/*.xml"):
            extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)

        return extracted_data
#print(extract())

# Transform
# Round the price columns to 2 decimal places
def transform(data):
    data['price'] = round(data.price, 2)

    return data
#print(transform(extract()))

# Loading
def load(targetfile, data_to_load):
    data_to_load.to_csv(targetfile)

# Logging
def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt", "a") as f:
        f.write(timestamp + ',' + message + '\n')


# Running ETL Process
log("ETL Job Started")
log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")
print(extracted_data)

log("Transform phase Started")
transformed_data = transform(extracted_data)
log("Transform phase Ended")
transformed_data

log("Load phase Started")
load(targetfile, transformed_data)
log("Load phase Ended")

log("ETL Job Ended")