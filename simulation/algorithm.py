import math

def cost_function1(people, billboard):
    cost = 0
    for person in people:
        cost += math.sqrt((person[1] - billboard[1]) ** 2 + (person[2] - billboard[2]) ** 2)

    return cost

def cost_function2(people, billboard):
    cost = 0
    for person in people:
        dist = math.sqrt((person[1] - billboard[1]) ** 2 + (person[2] - billboard[2]) ** 2)
        cost += 1 if dist < 3 else 0
    
    return cost

def algorithm1(people, billboards, ads):
    free_billboards = [i for i in range(len(billboards))]
    for ad in ads:
        audience = [person for person in people if person[3] == ad[1]]
        best_billboard = free_billboards[0]
        best_cost = cost_function1(audience, billboards[best_billboard])
        
        for i in free_billboards[1:]:
            cost = cost_function1(audience, billboards[i])
            if cost < best_cost:
                best_cost = cost
                best_billboard = i

        billboards[best_billboard][3] = ad[0]
        free_billboards.remove(best_billboard)
    
    for i in free_billboards:
        billboards[i][3] = -1

def algorithm2(people, billboards, ads):
    free_billboards = [i for i in range(len(billboards))]

    for ad in ads:
        audience = [person for person in people if person[3] == ad[1]]
        best_billboard = free_billboards[0]
        best_cost = cost_function2(audience, billboards[best_billboard])
        
        for i in free_billboards[1:]:
            cost = cost_function2(audience, billboards[i])
            if cost > best_cost:
                best_cost = cost
                best_billboard = i

        billboards[best_billboard][3] = ad[0]
        free_billboards.remove(best_billboard)
    

    for i in free_billboards:
        billboards[i][3] = -1
