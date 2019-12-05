#Adam Gronowski
#20051808
#CMPE 365 Assignment1
#Dijkstra's Algorithm

import math
inf = math.inf

file1 = open("2019_Lab_2_flights_real_data.txt", "r")

# N is the total number of destinations
N = int(file1.readline())

weights=[]

with file1 as f:
    for line in f:
        data = list(map(int, line.split()))
        weights.append(data)

#Student number 20051808
#Find route from city 08 to 18

start_city = 8
end_city = 18

length = weights.__len__()

cost = [inf] * N
estimate = [inf] * N
reached = [False] * N
#vertex is called a candidate if at least one path to it is known
candidates = [False] * N
predecessor = [-1] * N

#1st vertex
cost[start_city] = 0
estimate[start_city] = 0
reached[start_city] = True
total_reached = 1

# find neighbours of first city
for i in range(length):
    # all neighbours found
    if weights[i][0] > start_city:
        break
    # source is the start city
    if weights[i][0] == start_city:
        destination = weights[i][1]
        if weights[i][3] < estimate[destination]:
            estimate[destination] = weights[i][3]
            candidates[destination] = True
            predecessor[destination] = start_city
best_candidate = start_city

while total_reached < N:
    best_candidate_estimate = inf
    #find neighbours of best candidate, reach lowest one
    for i in range(length):
        # all neighbours found
        if weights[i][0] > best_candidate:
            break
        # source is the best candidate
        if weights[i][0] == best_candidate:
            destination = weights[i][1]
            # destination is a candidate
            if candidates[destination]:
                # new best estimate
                if weights[i][3] < best_candidate_estimate:
                    best_candidate_estimate = weights[i][3]
                    best_candidate = destination

    reached[best_candidate] = True
    candidates[best_candidate] = False
    cost[best_candidate] = estimate[best_candidate]
    total_reached += 1

    #find neighbours of best candidate, update estimates
    for i in range(length):
        # all neighbours found
        if weights[i][0] > best_candidate:
            break
        # source is the best candidate
        if weights[i][0] == best_candidate:
            destination = weights[i][1]
            # departure time is greater than arrival of source
            if not reached[destination] and weights[i][2] > cost[best_candidate]:
                if weights[i][3] < estimate[destination]:
                    estimate[destination] = weights[i][3]
                    candidates[destination] = True
                    predecessor[destination] = best_candidate

# print routes
print('Optimal route from ' + str(start_city) + ' to ' + str(end_city))
print(' ')
optimal_route = []
current_path = end_city

# valid route exists
if cost[end_city] != inf:
    while current_path != start_city:
        optimal_route.append(current_path)
        current_path = predecessor[current_path]

    optimal_route.append(start_city)
    optimal_route.reverse()
    for i in range(optimal_route.__len__() -1 ):
        print("Fly from " + str(optimal_route[i]) + ' to ' + str(optimal_route[i+1]))

    print('')
    print('Arrive at ' + str(end_city) + ' at time ' + str(cost[end_city]))      
else:
    print('no valid route exists')
