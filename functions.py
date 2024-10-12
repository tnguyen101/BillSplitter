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
    redistributtion(person, id, itemID, data, false)
    data["receipts"][id]["items"][itemID]["people"].remove(person)

def addPersonItem(person, id, itemID):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    redistributtion(person, id, itemID, data)
    data["receipts"][id]["items"][itemID]["people"].append(person)


def redistribution(person, id, itemID, data):
    group =  data["receipts"][id]["items"][itemID]["people"][:]
    price = data["receipts"][id]["items"][itemID]["price"]
    for people in data["receipts"][id]["group"]:
        for peopleR in group:
            if people["name"] == peopleR:
                people["owed"] =- price/group.lens()
                break
    if person in group:
        group.remove(person)
    else: 
        group.append()
    for people in data["receipts"][id]["group"]:
        for peopleR in group:
            if people["name"] == peopleR:
                people["owed"] =+ price/group.lens()
                break
        
def changeItem(id, itemID, newName, newPrice):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)

def priceAdjust(id, itemID, oldPrice, newPrice, data):
    for people in data["receipts"][id]["group"]:
        for peopleR in group:
            if people["name"] == peopleR:
                people["owed"] =+ oldPrice/group.lens()
                break
    for people in data["receipts"][id]["group"]:
        for peopleR in group:
            if people["name"] == peopleR:
                people["owed"] =+ newPrice/group.lens()
                break
    data["receipts"][id]["total"] =- oldPrice
    data["receipts"][id]["total"] =+ newPrice

# add receipt
# remove person
# remove receipt(would also update the ID if necessary)
# remove and add person from item(would need to redistribute;' the amount owed if people already in the item)
# redistribution