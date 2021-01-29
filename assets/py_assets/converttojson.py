import pandas
import json

df = pandas.read_csv('./assets/data/csv/weapon.csv')

result = df.to_json('./lib/db/weapon.json', orient='records', lines=True)
s1=json.dumps(result)
parsed = json.loads(s1)
json.dumps(parsed, indent=4) 