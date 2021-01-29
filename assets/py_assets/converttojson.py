import pandas
import json

df = pandas.read_csv('./discord_bots/doublelung_resources/species_intents.csv')

result = df.to_json('./discord_bots/doublelung_resources/species_intents.csv', orient='records', lines=True)
s1=json.dumps(result)
parsed = json.loads(s1)
json.dumps(parsed, indent=4) 