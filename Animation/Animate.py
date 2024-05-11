from tkinter import PhotoImage
import turtle
import json
import re
import time


customers = {}
kitchens = {}
vehicles  = {}
graph = {}
orders = {}

shiftX = 500
shiftY = 350
   
with open("../Data/Customer.json", "r") as f:
    customers=json.load(f)
    f.close()
with open("../Data/Kitchens.json", "r") as f:
    kitchens=json.load(f)
    f.close()
with open("../Data/DeliveryBoy.json", "r") as f:
    vehicles=json.load(f)
    f.close()
with open("../Data/Graph.json", "r") as f:
    graph=json.load(f)
    f.close()
with open("../Data/Order.json", "r") as f:
    orders=json.load(f)
    f.close()

nodeLoc = graph["LocOfNode"]
LocNode = graph["NodeOfLoc"]

kitchenPens = {}
customerPens = {}
vehiclePen={}

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
screen.bgpic("../Asset/map.png")

kitchenIcon = PhotoImage(file="../Asset/kitchen.gif")

pen = turtle.Turtle()
pen.pencolor("black")
pen.penup()
pen.speed(0)
pen.hideturtle()

for (k,i) in zip(kitchens.keys(),range(0,len(kitchens.keys()))):
    pos_x = kitchens[k]["pos_x"]
    pos_y = kitchens[k]["pos_y"]
    screen.addshape(k, turtle.Shape("image", kitchenIcon))
    kitchenPens[k]=turtle.Turtle(k)
    kitchenPens[k].speed(10)
    kitchenPens[k].penup()
    kitchenPens[k].setposition(pos_x, pos_y)
    pen.goto(pos_x-50, pos_y-35)
    pen.write(kitchens[k]["name"])

customerIcon = PhotoImage(file="../Asset/customer.gif")
for (c,i) in zip(customers.keys(),range(0,len(customers.keys()))):
    pos_x = customers[c]["pos_x"]
    pos_y = customers[c]["pos_y"]
    screen.addshape(c, turtle.Shape("image", customerIcon))
    customerPens[c]=turtle.Turtle(c)
    customerPens[c].penup()
    customerPens[c].speed(10)
    customerPens[c].setposition(pos_x, pos_y)
    pen.goto(pos_x-15, pos_y+5)
    pen.write(customers[c]["name"])


vehicleNodeNoFoodIcon = PhotoImage(file="../Asset/carNoFood.gif")
vehicleNodeFoodIcon = PhotoImage(file="../Asset/car.gif")
turtle.register_shape("../Asset/car.gif")
turtle.register_shape("../Asset/carNoFood.gif")

for (v,i) in zip(vehicles.keys(),range(0,len(vehicles.keys()))):
    posKey = nodeLoc["n"+str(i+1)]

    pos_x = customers[posKey]["pos_x"]
    pos_y = customers[posKey]["pos_y"]-25
    screen.addshape(v, turtle.Shape("image", vehicleNodeNoFoodIcon))
    vehiclePen[v]=turtle.Turtle(v)
    vehiclePen[v].penup()
    vehiclePen[v].speed(7)
    vehiclePen[v].setposition(pos_x, pos_y)



def drawLine(cur_x, cur_y, next_x, next_y):
    pen.penup()
    pen.goto(cur_x, cur_y)
    pen.pendown()
    pen.goto(next_x, next_y)
    pen.penup()

for cur in graph["AdjList"].keys():
    for next in graph["AdjList"][cur]:
        From = graph["LocOfNode"][cur]
        to = graph["LocOfNode"][next]
        FromPen = customerPens[From] if From[0]=='c' else kitchenPens[From]
        toPen = customerPens[to] if to[0]=='c' else kitchenPens[to]
        cur_x, cur_y = FromPen.pos()
        next_x, next_y = toPen.pos()
        drawLine(cur_x, cur_y, next_x, next_y)

def updateFoodCount(k, count):
    cur_x, cur_y = kitchenPens[k].pos()
    pen.penup()
    pen.goto(cur_x-25, cur_y+25)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    pen.setheading(0)
    for _ in range(2):
        pen.forward(70)  # Adjust size as needed
        pen.right(-90)
        pen.forward(15)  # Adjust size as needed
        pen.right(-90)
    pen.end_fill()
    pen.penup()
    pen.goto(cur_x-25, cur_y+25)
    pen.pendown()
    pen.color("black")
    pen.write("ready = "+str(count), font=("Arial", 8,"normal"))
    pen.penup()

def updateDeliveryStatus(k, color):
    cur_x, cur_y = customerPens[k].pos()
    pen.penup()
    pen.goto(cur_x+35, cur_y-15)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(8)
    pen.end_fill()
    pen.penup()


kitFoodCount = {}

for c in orders.keys():
    k = orders[c]
    if k in kitFoodCount.keys():
        kitFoodCount[k]+=1 
    else:
        kitFoodCount[k]=1
    updateFoodCount(k, kitFoodCount[k])
    updateDeliveryStatus(c,"red")


planJson = {}
with open("../Result/PlanningResult.json", "r") as f:
    planJson=json.load(f)

plans = planJson["result"]["output"]["plan"].split("\n")

for plan in plans:
    item = re.split(r'[()\s]', plan)
    item = [x for x in item if x]
    if(len(item)==0):
        continue
    if item[0]=="MOVE":
        v = item[1].lower()
        src = nodeLoc[item[2].lower()]
        dest = nodeLoc[item[3].lower()]
        x, y = kitchenPens[dest].pos() if dest[0]=='k' else customerPens[dest].pos()
        vehiclePen[v].speed(4)
        # vehiclePen[v].tilt(45)
        vehiclePen[v].goto(x,y)
    elif item[0]=="PICKUPFOOD":
        v = item[1].lower()
        k = item[2].lower()
        kitFoodCount[k]-=1
        updateFoodCount(k,kitFoodCount[k])
        time.sleep(1)
        vehiclePen[v].speed(4)
        vehiclePen[v].shape("../Asset/car.gif")
    elif item[0] == "DELIVERFOOD":
        v = item[1].lower()
        c = item[2].lower()
        vehiclePen[v].speed(4)
        vehiclePen[v].shape("../Asset/carNoFood.gif")
        time.sleep(1)
        updateDeliveryStatus(c,"green")

        
        


























screen.exitonclick()

