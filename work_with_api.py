import requests
import json
res = requests.get('http://isbndb.com/api/v2/json/B0X402YC/books?q=science')
#print(res.text)
book_info = json.loads(res.text)
for element in book_info['data']:
    #print(element)
    print(element['author_data'])
