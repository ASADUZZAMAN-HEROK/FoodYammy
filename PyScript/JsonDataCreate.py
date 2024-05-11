import json
import math
import random

MAX_X =  650
MIN_X = -MAX_X
MAX_Y =  350
MIN_Y = -MAX_Y

def create(customerLimit, KitchenLimit, deliveryboyLImit):
    count = 0
    rad = 250
    delTheta = 180/customerLimit
    deliveryboy = {}
    customer = {}

    with open("../Data/PersonNames.txt", "r") as f:
        names = f.read().split('\n')
        f.close()
        
        for name in names[:customerLimit+deliveryboyLImit]:
            count+=1
            if(count<=deliveryboyLImit):
                deliveryboy["v"+str(count)]=name
            else:
                # customer["c"+str(count-deliveryboyLImit)]={"name":name, "pos_x":rad*math.cos(math.radians(90-delTheta*(count-deliveryboyLImit-1)))+350, "pos_y":20*(count-deliveryboyLImit)}
                customer["c"+str(count-deliveryboyLImit)]={"name":name, "pos_x":random.randint(MIN_X, MAX_X), "pos_y":random.uniform(MIN_Y, MAX_Y)}

    with open("../Data/Customer.json", "w") as f:
        json.dump(customer,f)
        f.close()

    with open("../Data/DeliveryBoy.json", "w") as f:
        json.dump(deliveryboy,f)
        f.close()

    count = 0
    Kitchen = {}
    with open("../Data/KitchenName.txt", "r") as f:
        names = f.read().split('\n')
        f.close()
        for name in names[:KitchenLimit]:
            count+=1
            Kitchen["k"+str(count)]={"name":name, "pos_x":random.uniform(MIN_X, MAX_X), "pos_y":random.randint(MIN_Y, MAX_Y)}
        
    with open("../Data/Kitchens.json", "w") as f:
        json.dump(Kitchen,f)
        f.close()

