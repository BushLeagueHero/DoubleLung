import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

import json
from itertools import permutations

species_data_set = json.load(open('./lib/ai/training/data/test/nn_species_test.json'))
location_data_set = json.load(open('./lib/ai/training/data/test/nn_location_test.json'))
weapon_data_set = json.load(open('./lib/ai/training/data/test/nn_weapon_test.json'))
ammo_data_set = json.load(open('./lib/ai/training/data/test/nn_ammo_test.json'))
caller_data_set = json.load(open('./lib/ai/training/data/test/nn_caller_test.json'))
scent_data_set = json.load(open('./lib/ai/training/data/test/nn_scent_test.json'))

def generate_command_tags(file,command):
    command_tags = []

    for key in file[command]:
        for key,value in key.items():
            for i in range(1,len(value)+1):
                l = [''.join(i) for i in permutations(value,i)]
                for w in l:
                    if w not in command_tags:
                        command_tags.append(stemmer.stem(w))

    return command_tags

species_tags = generate_command_tags(species_data_set,"species")
location_tags = generate_command_tags(location_data_set,"location")
weapon_tags = generate_command_tags(weapon_data_set,"weapon")
ammo_tags = generate_command_tags(ammo_data_set,"ammo")
caller_tags = generate_command_tags(caller_data_set,"caller")
scent_tags = generate_command_tags(scent_data_set,"scent")

update = {"intents":[   {"tag":"species","pattern":species_tags,"respone":"species"},
                        {"tag":"species","pattern":location_tags,"respone":"location"},
                        {"tag":"species","pattern":weapon_tags,"respone":"weapon"},
                        {"tag":"species","pattern":ammo_tags,"respone":"ammo"},
                        {"tag":"species","pattern":caller_tags,"respone":"caller"},
                        {"tag":"species","pattern":scent_tags,"respone":"scent"},
            ]
        }

with open('./lib/ai/training/data/test/nn_commands_test.json','w') as f:
    json.dump(update,f)