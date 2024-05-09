import JsonDataCreate
import OrderCreate
import randomGraphGenerator
import problemPDDLCreate




def Generate(customerLimit,KitchenLimit, deliveryboyLImit,nodeDulication):
    JsonDataCreate.create(customerLimit, KitchenLimit, deliveryboyLImit)
    OrderCreate.create()
    randomGraphGenerator.create(nodeDulication)
    problemPDDLCreate.create()
