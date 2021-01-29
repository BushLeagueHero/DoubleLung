import json
import itertools

data = json.load(open("./discord_bots/doublelung_resources/tags.json"))

json_array=[]
final_array=[]
final_string=''

for list in data:
    for i in range(0,len(list)+1):
        for subset in itertools.permutations(list,i):
            final_array.append(final_string.join(subset))

    json_array.append(final_array)
    final_array=[]

with open("./discord_bots/doublelung_resources/tags.json",'w') as outfile:
    json.dump(json_array,outfile)
