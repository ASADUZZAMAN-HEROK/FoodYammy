import json
import random

customers = {}
kitchens = {}

with open("../Data/Customer.json", "r") as f:
    customers = json.load(f)

with open("../Data/Kitchens.json", "r") as f:
    kitchens = json.load(f)


Keys = list(customers.keys())+list(kitchens.keys())
numberOfNode = len(Keys)

graph = {}
graph["NodeOfLoc"] = {}
graph["AdjList"]={}
graph["LocOfNode"]={}

#node creation:
for i in range(0,numberOfNode):
    graph["NodeOfLoc"][Keys[i]]="n"+str(i+1)
    graph["LocOfNode"]["n"+str(i+1)]=Keys[i];


Keys =  [val for val in Keys for _ in range(0, 10)]
random.shuffle(Keys)






for i in range(0,len(Keys)):
    if(Keys[i]==Keys[i-1]):
        continue
    u = graph["NodeOfLoc"][Keys[i]]
    v = graph["NodeOfLoc"][Keys[i-1]]
    if u in graph["AdjList"].keys():
        graph["AdjList"][u].add(v)
    else:
        graph["AdjList"][u]={v}

for keys in graph["AdjList"].keys():
    graph["AdjList"][keys]=list(graph["AdjList"][keys])

with open("../Data/Graph.json", "w") as f:
    json.dump(graph, f)
    f.close()



