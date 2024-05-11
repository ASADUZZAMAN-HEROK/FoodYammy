import json
import math
import random

MAX_X =  650
MIN_X = -MAX_X
MAX_Y =  350
MIN_Y = -MAX_Y
node_coordinates = []

def euclideanDistance(u, v):
    return math.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)


def isDistantEnough(x, y, threshold=150):
    curr_node = (x, y)
    for node in node_coordinates:
        if(euclideanDistance(node, curr_node) < threshold):
            return False
    return True

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
                while True:
                    x = random.randint(MIN_X, MAX_X)
                    y = random.uniform(MIN_Y, MAX_Y)
                    if isDistantEnough(x, y):
                        customer["c"+str(count-deliveryboyLImit)]={"name":name, "pos_x":x, "pos_y":y}
                        node_coordinates.append((x, y))
                        break

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
            # Kitchen["k"+str(count)]={"name":name, "pos_x":random.uniform(MIN_X, MAX_X), "pos_y":random.randint(MIN_Y, MAX_Y)}
            while True:
                    x = random.uniform(MIN_X, MAX_X)
                    y = random.randint(MIN_Y, MAX_Y)
                    if isDistantEnough(x, y):
                        Kitchen["k"+str(count)]={"name":name, "pos_x":x, "pos_y":y}
                        node_coordinates.append((x, y))
                        break
        
    with open("../Data/Kitchens.json", "w") as f:
        json.dump(Kitchen,f)
        f.close()

