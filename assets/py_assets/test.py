import json

obj_data = json.load(open('./lib/db/object.json'))

stat_list=[]
stat_group=[]

for d in obj_data:
    for key in obj_data[d]:
        for i in key:
            if i not in stat_list:
                stat_list.append(i)
                stat_group.append(d)

push_data = []

with open('./lib/db/stats.json','w') as tf:
    for i in stat_list:
        index = stat_list.index(i)
        if stat_group[index] == "species":
            stat_dict = {"statid":i,"description":"DESCRIPTION","inline":False,"cmd_set":stat_group[index],"sort":0,"group":"GROUP"}
        else:
            stat_dict = {"statid":i,"description":"DESCRIPTION","inline":False,"cmd_set":stat_group[index],"sort":0,}
        push_data.append(stat_dict)

    final_dict = {"stats":push_data}
    json.dump(final_dict,tf,indent=4)