import json

def itemizeReceipt(id):
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
        data["receipts"][id]["itemized"] = not data["receipts"][id]["itemized"]
        file.seek(0)
        json.dump(data, file, indent = 4)

def addPerson(person, id):# works
    x = {"name" : person,
        "owed" : 0
        }
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
        data["receipts"][id]["group"].append(x)
        file.seek(0)
        json.dump(data, file, indent = 4)

def addItem(id, name, price, people):# works
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
        x = {"itemID" : len(data["receipts"][id]["items"]),
            "name" : name,
            "price" : price,
            "people" : people
            }
        data["receipts"][id]["items"].append(x)
        data["receipts"][id]["total"] += price
        for group in data["receipts"][id]["group"]:
            for peopleR in people:
                if group["name"] == peopleR:
                    group["owed"] += price/len(data["receipts"][id]["items"][x["itemID"]]["people"])
                    break
        file.seek(0)
        json.dump(data, file, indent = 4)

def addReceipt(name, price, people, itemized):#works
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
        tempList = []
        for p in people:
            tempList.append({"name" : p,
                             "owed" : 0
                             })
        x = {
            "name" : name,
            "itemized" : itemized,
            "id" : len(data["receipts"]),
            "items" : [],
            "group" : tempList,
            "total" : 0
            }
        data["receipts"].append(x)
        if not itemized:
            y = {"itemID" : len(data["receipts"][x["id"]]["items"]),
                "name" : name,
                "price" : price,
                "people" : people
                }
            data["receipts"][x["id"]]["items"].append(y)
            data["receipts"][x["id"]]["total"] += price
            for group in data["receipts"][x["id"]]["group"]:
                for peopleR in people:
                    if group["name"] == peopleR:
                        group["owed"] += price/len(data["receipts"][x["id"]]["items"][y["itemID"]]["people"])
                        break
        file.seek(0)
        json.dump(data, file, indent = 4)

def addPersonItem(person, id, itemID): #works
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
        redistribution(person, id, itemID, data)
        file.seek(0)
        json.dump(data, file, indent = 4)

def removePerson(person, id):# works
    with open('receipt_data.json', 'r') as file:
        data = json.load(file)
        for item in data["receipts"][id]["items"]:
            if person in item["people"]:
                redistribution(person, id, item["itemID"], data)
        for i in range(0, len(data["receipts"][id]["group"])):
            if person == data["receipts"][id]["group"][i]["name"]:
                data["receipts"][id]["group"].pop(i)
                break
    with open("receipt_data.json", 'w') as file:
        json.dump(data, file, indent = 4)

def removeItem(id, itemID):# works
    with open('receipt_data.json', 'r') as file:
        data = json.load(file)
        for i in range(itemID + 1, len(data["receipts"][id]["items"])):
            data["receipts"][id]["items"][i]["itemID"] -= 1
        priceAdjust(id, itemID, data["receipts"][id]["items"][itemID]["price"], 0, data, False)
        del data["receipts"][id]["items"][itemID]
    with open("receipt_data.json", 'w') as file:
        json.dump(data, file, indent = 4)

def removeReceipt(id):#works
    with open("receipt_data.json", 'r') as file:
        data = json.load(file)
        for i in range(id, len(data["receipts"])):
            data["receipts"][i]["id"] -= 1
        data["receipts"].pop(id)
    with open("receipt_data.json", 'w') as file:
        json.dump(data, file, indent = 4)


def removePersonItem(person, id, itemID):#works
    with open('receipt_data.json', 'r') as file:
        data = json.load(file)
        redistribution(person, id, itemID, data)
    with open("receipt_data.json", 'w') as file:
        json.dump(data, file, indent = 4)

def changeItem(id, itemID, newName, newPrice):# works
    with open('receipt_data.json', 'r') as file:
        data = json.load(file)
        data["receipts"][id]["items"][itemID]["name"] = newName
        if data["receipts"][id]["items"][itemID]["price"] != newPrice:#if price are the same then it won't call the function
            priceAdjust(id, itemID, data["receipts"][id]["items"][itemID]["price"], newPrice, data, True)
        data["receipts"][id]["items"][itemID]["price"] = newPrice
    with open("receipt_data.json", 'w') as file:
        json.dump(data, file, indent = 4)

def priceAdjust(id, itemID, oldPrice, newPrice, data, changing):# works
    for people in data["receipts"][id]["group"]:
        for peopleR in data["receipts"][id]["items"][itemID]["people"]:
            if people["name"] == peopleR:
                people["owed"] -= oldPrice/len(data["receipts"][id]["items"][itemID]["people"])
                break
    # the condition below is for removing the item and if it does then it won't run that part
    if changing:
        for people in data["receipts"][id]["group"]:
            for peopleR in data["receipts"][id]["items"][itemID]["people"]:
                if people["name"] == peopleR:
                    people["owed"] += newPrice/len(data["receipts"][id]["items"][itemID]["people"])
                    break
    data["receipts"][id]["total"] -= oldPrice
    if changing :
        data["receipts"][id]["total"] += newPrice

def redistribution(person, id, itemID, data):#works
    price = data["receipts"][id]["items"][itemID]["price"]
    for people in data["receipts"][id]["group"]:
        for peopleR in data["receipts"][id]["items"][itemID]["people"]:
            if people["name"] == peopleR:
                people["owed"] -= price/len(data["receipts"][id]["items"][itemID]["people"])
                break
    if person in data["receipts"][id]["items"][itemID]["people"]:
        data["receipts"][id]["items"][itemID]["people"].remove(person)
    else: 
        data["receipts"][id]["items"][itemID]["people"].append(person)
    for people in data["receipts"][id]["group"]:
        for peopleR in data["receipts"][id]["items"][itemID]["people"]:
            if people["name"] == peopleR:
                people["owed"] += price/len(data["receipts"][id]["items"][itemID]["people"])
                break

# addReceipt("Sushi dinner", 0, ["Anthony", "Travis", "Nyan"], True)
# remove person(done)
# remove receipt(would also update the ID if necessary)(done)
# remove and add person from item(would need to redistribute;' the amount owed if people already in the item)(done)
# redistribution(done)

# addReceipt()
# addPerson("Dave", 2)
# addItem() works
# addPersonItem("Travis", 0, 2)
# removePersonItem("Dave", 0, 1)
# removeReceipt(1)
# changeItem(0, 2, "Dinner", 60)
# removeItem(0, 0)
# removePerson("Anthony", 0)
