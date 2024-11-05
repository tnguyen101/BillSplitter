import sys
import json

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

def addPersonItem(person, id, itemID):# works
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

if __name__ == "__main__":
    r_id = sys.argv[1]
    r_action = sys.argv[2]