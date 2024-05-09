
import json

count = 0
pos_y = 20

customerLimit = 20
KitchenLimit = 5
deliveryboyLImit = 5

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
            customer["c"+str(count-deliveryboyLImit)]={"name":name, "pos_x":800, "pos_y":20*(count-deliveryboyLImit)}


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
        Kitchen["k"+str(count)]={"name":name, "pos_x":200, "pos_y":20*count}
    

with open("../Data/Kitchens.json", "w") as f:
    json.dump(Kitchen,f)
    f.close()

