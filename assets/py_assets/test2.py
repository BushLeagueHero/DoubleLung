import json
from re import search

data = json.load(open('./lib/db/object.json'))
cmd_set = json.load(open('./lib/db/stat.json'))

species = "blackbear"
group = "GENERAL"

#get speciesID
def __get_speciesid(self,ctx,species):
    for i in range(0,len(data["species"])):
        if data["species"][i]["speciesid"] == species:
            species_data_set = data["species"][i]

    return species_data_set

#determine keys to use
def __determine_embed_keys(self,ctx,group):
    embed_keys = []
    for i in range(0,len(cmd_set["stats"])):
        if cmd_set["stats"][i]["group"] == group:
            embed_keys.append(cmd_set["stats"][i]["id"])
 
    return embed_keys

#determine data for each key
def __pull_key_data(self,ctx,embed_keys,species):
    key_data = []
    for key in embed_keys:
        data = species[key]
        key_data.append({key:data})
    
    return key_data

#add each stat from group in embed
def __add_stat_to_embed(self,ctx,stat,data_set):
    for i in range(0,len(cmd_set["stats"])):
        if cmd_set["stats"][i]["id"] == stat:
            stat_conf = cmd_set["stats"][i]

    name = stat_conf["description"]
    value_obj = []
    if search("lol_",stat):
        if stat == "lol_location":
            for n in range(0,len(data_set[stat])):
                value_obj.append(data_set[stat][n][0])
            values = "\n".join(i for i in value_obj)
        else:
            stat_list = {}
            for loc in range(len(data_set["lol_location"])):
                for s in data_set[stat][loc]:
                    if s not in stat_list:
                        stat_list[s] = []
                    stat_list[s].append(data_set["lol_location"][loc][0])
            
            for key,value in stat_list.items():
                value_obj.append(f"{key} ({', '.join(i for i in value)})")
            
            values = "\n".join(i for i in value_obj)
    else:
        values = "\n".join(i for i in data_set[stat])

    inline = stat_conf["inline"]

    print(name, values, inline)
    
    # embed.add_field(name=hunt_stats[stat][statkey][0],value="\n".join(i for i in stat_data), inline=hunt_stats[stat][statkey][1])

#build embed
def __build_embed(self,ctx,species,group):
    data_set = (__get_speciesid(species))  
    key_group = __determine_embed_keys(group)
    data = __pull_key_data(key_group,data_set)

    for stat in key_group:
        self.__add_stat_to_embed(stat,data_set)



__build_embed(species,group)