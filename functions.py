import json

def addperson(person, id):
    x = {"name" : person,
        "owed" : "0"
        }
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    data["receipts"][id]["person"].append(x)
    json.dump(data, file, indent = 4)

def addItem(id, name, price, people):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    temp = []
    if !isinstance(people, list):
        temp.append(people)
    elif(people != ""):
        temp = people
    x = {"itemID" : data["receipt"][id]["items"].lens(),
         "name" : name,
         "price" : price,
         "people" : temp
        }
    json.dump(data, file, indent = 4)

def addPersonItem(person, id, itemID):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    redistributtion(person, id, itemID, data)
    data["receipts"][id]["items"][itemID]["people"].append(person)
    json.dump(data, file, indent = 4)

def removePerson(person, id):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    for item in data["receipts"][id]["items"]:
        if person in item["people"]:
            redistributtion(person, id, item["itemID"], data)
            data["receipts"][id]["items"][itemID]["people"].remove(person)
    receipt["group"].remove(person)
    json.dump(data, file, indent = 4)

def removeItem(id, itemID):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    for i in range(0, data["receipts"][id]["items"].lens()) 
        if itemID < data["receipts"][id]["items"][i][itemID]:
            data["receipts"][id]["items"][i]["itemID"]--
    priceAdjust(id, itemID, data["receipts"][id]["items"][itemID]["price"], 0, data, False)
    del data["receipts"][id]["items"][itemID]
    json.dump(data, file, indent = 4)

    

def removePersonItem(person, id, itemID):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    redistributtion(person, id, itemID, data)
    data["receipts"][id]["items"][itemID]["people"].remove(person)
    json.dump(data, file, indent = 4)

def changeItem(id, itemID, newName, newPrice):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
    data["receipts"][id]["items"][itemID]["name"] = newName
    if data["receipts"][id]["items"][itemID]["price"] == newPrice:#if price are the same then it won't call the function
        priceAdjust(id, itemID, data["receipts"][id]["items"][itemID]["price"], newPrice, data, True)
    json.dump(data, file, indent = 4)

def priceAdjust(id, itemID, oldPrice, newPrice, data, changing):
    for people in data["receipts"][id]["group"]:
        for peopleR in group:
            if people["name"] == peopleR:
                people["owed"] =- oldPrice/group.lens()
                break
    # the condition below is for removing the item and if it does then it won't run that part
    if changing:
        for people in data["receipts"][id]["group"]:
            for peopleR in group:
                if people["name"] == peopleR:
                    people["owed"] =+ newPrice/group.lens()
                    break
    data["receipts"][id]["total"] =- oldPrice
    if changing :
        data["receipts"][id]["total"] =+ newPrice

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

# add receipt
# remove person(done)
# remove receipt(would also update the ID if necessary)
# remove and add person from item(would need to redistribute;' the amount owed if people already in the item)(done)
# redistribution(done)