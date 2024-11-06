import sys
import json

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

def addReceipt():#works
    with open('receipt_data.json', 'r+') as file:
        data = json.load(file)
        x = {
            "id" : len(data["receipts"]),
            "items" : [],
            "group" : [],
            "total" : 0
            }
        data["receipts"].append(x)
        file.seek(0)
        json.dump(data, file, indent = 4)

if __name__ == "__main__":
    r_name = sys.argv[1]
    r_price = sys.argv[2]
    r_people = sys.argv[3]
    addReceipt()#works till here
    addItem(0, r_name, float(r_price), r_people)