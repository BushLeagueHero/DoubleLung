import pandas
import json

df = pandas.read_csv('./assets/data/csv/location.csv')

result = df.to_json('./lib/db/location.json', orient='records', lines=True)
s1=json.dumps(result)
parsed = json.loads(s1)
json.dumps(parsed, indent=4) 