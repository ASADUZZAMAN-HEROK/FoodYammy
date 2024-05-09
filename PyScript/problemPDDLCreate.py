import json

def create():
    customers = {}
    kitchens = {}
    orders = {}
    vehicles  = {}
    graph = {}

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


    def getDist(cur, next):
        x_diff= cur["pos_x"]-next["pos_x"]
        y_diff= cur["pos_y"] - next["pos_y"]
        return x_diff*x_diff + y_diff*y_diff


    with open('../PDDL/FoodYammyProblem.pddl', 'w') as out:
        out.write("(define (problem FoodYammyProblem)\n")
        out.write("\t(:domain FoodYammyDomain)\n")
        out.write("\t(:objects\t")

        for c in customers.keys():
            out.write(c+" ")
        out.write('- customer\n\t\t\t\t')

        for k in kitchens.keys():
            out.write(k+" ")
        out.write('- kitchen\n\t\t\t\t')

        for v in vehicles.keys():
            out.write(v+" ")
        out.write('- vehicle\n\t\t\t\t')

        for n in graph["LocOfNode"].keys():
            out.write(n+" ")
        out.write('- node)\n')

        out.write('\t(:init\n')
        out.write('\t(= (total_distance) 0)\n')

        nodeIdx = 1
        for c in customers.keys():
            out.write("\t(location_C "+c+" n"+str(nodeIdx)+")\n")
            nodeIdx+=1
        
        for k in kitchens.keys():
            out.write("\t(location_K "+k+" n"+str(nodeIdx)+")\n")
            nodeIdx+=1
        
        nodeIdx = 1
        for v in vehicles.keys():
            out.write("\t(location_V "+v+" n"+str(nodeIdx)+")\n")
            nodeIdx+=1
        
        for v in vehicles.keys():
            out.write("\t(standBy "+v+")\n")
        
        for c in orders.keys():
            out.write("\t(K_HasFood_C "+orders[c]+" "+c+")\n")
        
        for cur in graph["AdjList"].keys():
            for next in graph["AdjList"][cur]:
                out.write("\t(road "+cur+" "+next+")\n")
        
        for cur in graph["AdjList"].keys():
            for next in graph["AdjList"][cur]:
                From = graph["LocOfNode"][cur]
                to = graph["LocOfNode"][next]

                From = customers[From] if From[0]=='c' else kitchens[From]
                to = customers[to] if to[0]=='c' else kitchens[to]

                dist = getDist(From, to)
                out.write("\t(= (distance "+cur+" "+next+") "+ str(dist)+")\n")
        
        out.write("\t)\n")
        out.write("\t(:goal (and ")

        for c in orders.keys():
            out.write(" (delivered "+c+") ")
        out.write("))\n")
        out.write("\t(:metric minimize (total_distance))\n)\n")
        out.close()





