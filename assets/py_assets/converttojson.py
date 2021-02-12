import pandas
import json

df = pandas.read_csv('./assets/data/csv/nn_commands.csv')

result = df.to_json('./lib/ai/training/nn_commands_test.json', orient='records', lines=True)
s1=json.dumps(result)
parsed = json.loads(s1)
json.dumps(parsed, indent=4) 