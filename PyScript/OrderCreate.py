import json
import random

def create():

    customers = {}
    kitchens = {}

    with open("../Data/Customer.json", "r") as f:
        customers = json.load(f)

    with open("../Data/Kitchens.json", "r") as f:
        kitchens = json.load(f)

    customersKeys = customers.keys()
    kitchenKeys = list(kitchens.keys())

    random.shuffle(kitchenKeys)
    count = len(kitchenKeys)

    Order = {}
    idx = 0
    for key in customersKeys:
        Order[key]=kitchenKeys[idx%count]
        idx+=1

    with open("../Data/Order.json", "w") as f:
        json.dump(Order, f)
        f.close()


