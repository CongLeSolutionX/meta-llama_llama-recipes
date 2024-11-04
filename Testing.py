import json
import urllib.request
url = 'https://data.ca.gov/api/3/action/datastore_search?resource_id=f0ded01d-06d3-4366-adc2-24917af2dddb&limit=5&q=title:jones'  
fileobj = urllib.request.urlopen(url)
response_dict = json.loads(fileobj.read())
print(response_dict)