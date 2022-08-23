from scrap import conf
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01'

page_source = conf.get_html_page(url)

conf.put_page_data_into_file('index.html', page_source)

source = conf.get_data_from_file('index.html')

soup = BeautifulSoup(source, 'html5lib')

all_banks = soup.find('tbody').find_next('tbody').find_next('tbody').find_next('tbody').findAll('tr')

conf.extract_data_and_write_to_json_file(all_banks, 'banks_data.json')

dataframe_columns = ['Bank Rank', 'Bank name', 'Market cap(US$ billion)']

conf.create_pandas_dataframe(dataframe_columns, 'banks_data.json')