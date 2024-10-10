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
# add receipt
# remove person
# remove receipt(would also update the ID if necessary)
# remove and add person from item(would need to redistribute;' the amount owed if people already in the item)
# redistribution