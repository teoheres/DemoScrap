import requests

url = "http://www.omdbapi.com/?i=tt3896198&apikey=b35c1783"
response  = requests.get(url)

#print(response.status_code)
if response.status_code == 200:
    data = response.json().get('Title', [])
    print(data)
else:
    print("Response code not good")


