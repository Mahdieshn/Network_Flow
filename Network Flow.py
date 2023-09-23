import pickle
import pandas as pd
import numpy as np
import random 
import matplotlib.pyplot as plt


# Read Edges
edges = pd.read_pickle("graphs\\case1\\case1\\edges.pkl")

#Read Capacity
capacities = pd.read_pickle("graphs\\case1\\case1\\capacities.pkl")


# Create first generation
def create_first_generation(capacities):
    first_generation = []
    for capacity in capacities:
        flow_list = []
        for flow in capacity:
            flow_list.append(random.randint(0, flow)) 
        first_generation.append(flow_list)  
    return first_generation


# Crossover
def crossover(graph1 , graph2):

    new_graph1 = []
    new_graph2 = []

    # Create New Graph1
    count = 0
    for capacitiy in range(len(graph1)):
        if count <= (len(graph1)/2)  :
            new_graph1.append(graph1[capacitiy])
        else :
            new_graph1.append(graph2[capacitiy])
        count += 1

    # Create New Graph2
    count = 0
    for capacitiy in range(len(graph2)):
        if count <= (len(graph2)/2) :
            new_graph2.append(graph2[capacitiy])
        else :
            new_graph2.append(graph1[capacitiy])
        count+= 1


    return (new_graph1 , new_graph2)



# Calculate Sum Outflow
def sum_outflow(graph):
    sum_outflow_list =[]
    for capacity in graph:
        sum_outflow = 0
        for outflow in capacity:
            sum_outflow += outflow
        sum_outflow_list.append(sum_outflow)
    return sum(sum_outflow_list)


# Ftiness Function
def fitness(graph):


    # Calculate Sum Outflow
    sum_outflow_list =[]
    for capacity in graph:
        sum_outflow = 0
        for outflow in capacity:
            sum_outflow += outflow
        sum_outflow_list.append(sum_outflow)

    

    # Calculate Sum Inflow
    sum_inflow_list = []
    for capacity in range(len(graph)) :
        sum_inflow = 0
        for inflow in range(len(graph)) :
            sum_inflow += graph[inflow][capacity]
        sum_inflow_list.append(sum_inflow)

    


    diffrence_list = []  
    for node in range(1 , len(graph)-1):
        
        # Check Balance
        if sum_inflow_list[node] != sum_outflow_list[node] :
            diffrence = abs(sum_inflow_list[node]-sum_outflow_list[node])
            diffrence_list.append(diffrence)
            fitness = 1/sum(diffrence_list)
    return (fitness)


# Create First Generation
graph_list= []
for i in range (30):
    graph = create_first_generation(capacities)
    graph_list.append(graph)


x = []
y = []
# Run Algorithm
def run():

    iterations = 0
    while True :
        num = int(input("Please Insert 1"))
        if num == 1 :  
            
            
                
            
            # Calculate Fitness
            fitness_list = []
            for graph in graph_list :
                fitness_list.append(fitness(graph))
            
            # Find best Fitness
            fitness_list1 = fitness_list
            max_list= []
            for i in range(2):
                max_fitness = max(fitness_list1)
                max_index = fitness_list1.index(max_fitness)
                max_list.append(max_index)
                fitness_list1.remove(max_fitness)

            # Crossover
            new_gen = crossover(graph_list[max_list[0]], graph_list[max_list[1]])
            

            # Print Result
            for graph in new_gen :
                new_fitness = fitness(graph)
                fitness_list.append(new_fitness)
                # Next Genenration
                graph_list.append(graph)
                
            print ("Iteration", iterations , "best fitnsess is" , max(fitness_list) , "and sum flow is" , sum_outflow(graph) )


            # Remove worst Fitness
            min_list= []
            for i in range(2):
                min_fitness = min(fitness_list)
                min_index = fitness_list.index(min_fitness)
                min_list.append(min_index)
                fitness_list.remove(min_fitness)
                graph_list.remove(graph_list[min_index])


            # Create generation for diversity
            for i in range(10):
                graph_list.append(create_first_generation(capacities))

            
            


            y.append(iterations)
            x.append(max(fitness_list))

            plt.plot(x, y)
            plt.show()

            

            iterations += 1

        else :
            continue

run()


