import json

def question_collection():
    data = []
    
    while True:
        question = input("ASKBOT: ".lower())
        if question =="update":
            with open('./lib/ai/training/data/nn_command_qcollection.json', 'w') as f:
                json.dump(data,f)

        if question == "quit":
            break

        else:
            
            data.append([question])
            
question_collection()