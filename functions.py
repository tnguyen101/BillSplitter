import json

def addperson(person, id):
    with open('Recieptdata.json', 'r+') as file:
        x = {"name" : person,
             "owed" : "0"
            }
        file_data = json.load(file)
        file_data.append(x)
        file_data["receipt"]["group"].append(x)
        json.dump(file_data, file, indent = 4)

