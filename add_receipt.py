import sys
import json

def addItem(id, name, price, people, data):# works
    tempList = [x.strip() for x in people.split(',')]
    secTempList = []
    for t in tempList:
        secTempList.append(t)
    x = {"itemID" : len(data["receipts"][id]["items"]),
        "name" : name,
        "price" : price,
        "people" : secTempList
        }
    data["receipts"][id]["items"].append(x)
    data["receipts"][id]["total"] += price
    for group in data["receipts"][id]["group"]:
        for peopleR in secTempList:
            if group["name"] == peopleR:
                group["owed"] += price/len(data["receipts"][id]["items"][x["itemID"]]["people"])
                break

def addReceipt(name, price, people, itemized, itemData):#works
    with open('receipt_data2.json', 'r') as file:
        data = json.load(file)
        itemData = json.loads(itemData)
        tempList = [x.strip() for x in people.split(',')]
        secTempList = []
        if itemized:
            tempList.remove("")
            for Item in itemData:
                for person in [x.strip() for x in Item["person"].split(',')]:
                    if person not in tempList:
                        tempList.append(person)
        for t in tempList:
            secTempList.append({"name" : t,
                                "owed" : 0
                                })
        tempBool = False
        if itemized == "true":
            tempBool = True
        x = {
            "name" : name,
            "itemized" : tempBool,
            "id" : len(data["receipts"]),
            "items" : [],
            "group" : secTempList,
            "total" : 0
            }
        data["receipts"].append(x)
        if not tempBool:
            y = {"itemID" : len(data["receipts"][x["id"]]["items"]),
                "name" : name,
                "price" : price,
                "people" : tempList
                }
            data["receipts"][x["id"]]["items"].append(y)
            data["receipts"][x["id"]]["total"] += price
            for group in data["receipts"][x["id"]]["group"]:
                for peopleR in tempList:
                    if group["name"] == peopleR:
                        group["owed"] += price/len(data["receipts"][x["id"]]["items"][y["itemID"]]["people"])
                        break
        else:
            for item in itemData:
                addItem(x["id"], item["name"], item["price"], item["person"], data)
    with open('receipt_data2.json', 'w') as file:
        json.dump(data, file, indent = 4)        

if __name__ == "__main__":
    r_name = sys.argv[1]
    r_price = sys.argv[2]
    r_people = sys.argv[3]
    r_itemized = sys.argv[4]
    r_items = sys.argv[5]
    addReceipt(r_name, float(r_price), r_people, r_itemized, r_items)#works till here