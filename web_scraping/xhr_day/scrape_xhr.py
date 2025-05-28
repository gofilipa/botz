from bs4 import BeautifulSoup
import requests

query = "how can i"

url = (
    "https://www.bing.com/AS/Suggestions?pt=page.home&mkt=en-us&qry="
    + query
    + "&cp=9&csr=1&msbqf=false&pths=1&cvid=6AE710F2D778431589574CB8424EFF70"
)

response = requests.get(url)

response
dir(response)
response.text
response.content
response.json()

parsed = response.json()

# what kind of data structure?
# pull out the completions
parsed
parsed['s'][0]
parsed['s'][0]['q']
parsed['s'][1]['q']
parsed['s'][2]['q']

# write a loop that prints just the completions
for item in parsed['s']:
    print(item['q'])
