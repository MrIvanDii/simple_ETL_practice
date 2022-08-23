from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

#Getting page data
url = 'https://en.wikipedia.org/wiki/List_of_largest_banks?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01'
headers = {
        'authority': 'en.wikipedia.org',
        'path': '/wiki/List_of_largest_banks?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01',
        'accept': 'application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Summary/1.2.0"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
response = requests.get(url, headers=headers)
html_data = response.text

soup = BeautifulSoup(html_data, 'html.parser')

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])
#print(data)


for row in soup.find_all('tbody')[3].find_all('tr')[1:]:
    col = row.find_all('td')
    dta = {"Name": col[1].text.strip(), "Market Cap (US$ Billion)": round(float(col[2].text.strip().replace('[', '').replace(']', '')), 2)}
    data = data.append(dta, ignore_index=True)


result = data.to_json(orient="records", force_ascii=False)
print(result)
result1 = data.to_json(orient="columns")
print(result1)
