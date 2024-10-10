import json

def addperson(person, id):
    x = {"name" : person,
        "owed" : "0"
        }
    with open('recieptdata.json', 'r+') as file:
        data = json.load(file)
    for receipt in data["receipts"]:
        if id == receipt["ID"]:
            receipt["group"].append(x)
            break
    json.dump(data, file, indent = 4)

def rmperson(person, id):
    with open('recieptdata.json', 'r+') as file:
        data = json.load(file)
    for receipt in data["receipts"]:
        if id == receipt["ID"]:
            for item in receipt["items"]:

            receipt["group"].remove(person)
            
def removePersonItem(person, item, id):
    
def redistribution(person, item, id):
    with open('recieptdata.json', 'r+') as file:
        data = json.load(file)
    for receipt in data["receipts"]:
        if id == receipt["ID"]:
            for item in receipt["items"]:


# add receipt
# remove person
# remove receipt(would also update the ID if necessary)
# remove and add person from item(would need to redistribute;' the amount owed if people already in the item)
# redistribution