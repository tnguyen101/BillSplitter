import sys
import json

def addItem(id, name, price, people):# works
    with open('receipt_data2.json', 'r+') as file:
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
    with open('receipt_data2.json', 'r+') as file:
        data = json.load(file)
        tempList = [x.strip() for x in people.split(',')]
        secTempList = []
        for t in tempList:
            secTempList.append({"name" : t,
                                "owed" : 0
                                })
        x = {
            "name" : name,
            "itemized" : itemized,
            "id" : len(data["receipts"]),
            "items" : [],
            "group" : secTempList,
            "total" : price
            }
        data["receipts"].append(x)
        if not itemized:
            y = {"itemID" : len(data["receipts"][x["id"]]["items"]),
                "name" : name,
                "price" : price,
                "people" : tempList
                }
            data["receipts"][x["id"]]["items"].append(y)
            for group in data["receipts"][x["id"]]["group"]:
                for peopleR in tempList:
                    if group["name"] == peopleR:
                        group["owed"] += price/len(data["receipts"][x["id"]]["items"][y["itemID"]]["people"])
                        break
        file.seek(0)
        json.dump(data, file, indent = 4)

if __name__ == "__main__":
    r_name = sys.argv[1]
    r_price = sys.argv[2]
    r_people = sys.argv[3]
    addReceipt(r_name, float(r_price), r_people, False)#works till here