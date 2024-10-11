import json

def addperson(person, id):
    x = {"name" : person,
        "owed" : "0"
        }
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    data["receipts"][id]["person"].append(x)
    json.dump(data, file, indent = 4)

def rmperson(person, id):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    for receipt in data["receipts"]:
        if id == receipt["ID"]:
            for item in receipt["items"]:

            receipt["group"].remove(person)
            
def removePersonItem(person, id, itemID):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    redistributtion(person, id, itemID)
    data["receipts"][id]["item"][itemID]["people"].remove(person)


def redistribution(person, id, itemID):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    group = []
    price = data["receipts"][id]["item"][itemID]["price"]
    for people in data["receipts"][id]["item"][itemID]["people"]:
        group.append(person)
    for people in data["receipts"][id]["group"]:
        for peopleR in group:
            if people["name"] == peopleR:
                people["owed"] =- price/group.lens()
                break
    group.remove(person)
    for people in data["receipts"][id]["group"]:
        for peopleR in group:
            if people["name"] == peopleR:
                people["owed"] =+ price/group.lens()
                break
        


# add receipt
# remove person
# remove receipt(would also update the ID if necessary)
# remove and add person from item(would need to redistribute;' the amount owed if people already in the item)
# redistribution