from bs4 import BeautifulSoup
import json
import html5lib
import requests
import pandas as pd

def get_html_page(url):

    headers = {
        'authority': 'en.wikipedia.org',
        'path': '/wiki/List_of_largest_banks?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01',
        'accept': 'application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Summary/1.2.0"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    source = response.text
    return source

def put_page_data_into_file(file_name, data_source):
    with open(file_name, 'w') as file:
        file.write(data_source)

def get_data_from_file(file_name):
    with open(file_name) as file:
        source = file.read()
    return source

def extract_data_and_write_to_json_file(list_with_data, file_name):

    for bank in list_with_data[1:]:
        data_bank = bank.text.strip().strip().replace('[', '').replace(']', '').split('\n\n')
        print(data_bank)
        data = {'Bank Rank': data_bank[0], 'Bank name': data_bank[1].strip(), 'Market cap(US$ billion)': round(float(data_bank[2]), 2)}
        print(data)
        with open(file_name, 'a') as file:
            file.write(json.dumps(data)+'\n')

def create_pandas_dataframe(list_with_columns, name_of_json_file_with_data):

    dataframe = pd.read_json(name_of_json_file_with_data, lines=True)
    extracted_data = pd.DataFrame(
        columns=list_with_columns)
    extracted_data = extracted_data.append(dataframe, ignore_index=False)
    print(extracted_data)

    return extracted_data
