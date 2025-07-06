# import requests
import pandas as pd

url = 'https://api.spacexdata.com/v4/launches'

df = pd.read_json(url)


#response = requests.get('https://api.spacexdata.com/v4/launches')
#data = response.json()

#df = pd.DataFrame(data)

# print(df.head(5))

# print(df.columns)

print(df.dtypes)