import sys
import json

def removeReceipt(id):
    with open("receipt_data2.json", 'r') as file:
        data = json.load(file)
        for i in range(id, len(data["receipts"])):
            data["receipts"][i]["id"] -= 1
        data["receipts"].pop(id)
    with open("receipt_data2.json", 'w') as file:
        json.dump(data, file, indent = 4)

if __name__ == "__main__":
    r_id = sys.argv[1]
    removeReceipt(int(r_id))