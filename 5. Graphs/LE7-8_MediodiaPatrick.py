import sys

def add_vertex(data, v):
    graph = data[0]
    vertices = data[1]
    vertices_no = data[2]

    vertices_no += 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
        
    temp = []
    for i in range(vertices_no):
        temp.append(0)
    graph.append(temp)

    return graph, vertices, vertices_no

def add_egde(data, v1, v2, e):
    graph = data[0]
    vertices = data[1]
    vertices_no = data[2]

    graph[vertices.index(v1)][vertices.index(v2)] = e

    return graph, vertices, vertices_no

def main():
    vertices = []
    vertices_no = 0

    graph = []
    data = [graph, vertices, vertices_no]

    #vertices to be added to the graph
    locations = [ "cabuyao", "calamba", "los banos", "bay"
                 ,"alaminos", "san pablo", "calauan", "victoria"
                 ,"nagcarlan", "pila", "sta. cruz", "liliw"
                 , "magdalena", "pagsanjan", "majayjay" ]

    #add elements in locations list as vertices
    for location in locations:
        data = add_vertex(data, location)

    #edges to connect the elements in the graph
    connections = [["cabuyao", "calamba", 12],
                   ["calamba", "los banos", 20],
                   ["calamba", "alaminos", 27],
                   ["los banos", "bay", 7],
                   ["alaminos", "san pablo", 9],
                   ["bay", "victoria", 20],
                   ["bay", "calauan", 11],
                   ["san pablo", "calauan", 11],
                   ["san pablo", "nagcarlan", 24],
                   ["san pablo", "majayjay", 25],
                   ["calauan", "victoria", 14],
                   ["calauan", "nagcarlan", 12],
                   ["victoria", "pila", 6],
                   ["nagcarlan", "pila", 13],
                   ["nagcarlan", "sta. cruz", 18],
                   ["nagcarlan", "liliw", 8],
                   ["pila", "sta. cruz", 6],
                   ["sta. cruz", "magdalena", 10],
                   ["sta. cruz", "pagsanjan", 10],
                   ["magdalena", "liliw", 9],
                   ["liliw", "majayjay", 5],
                   ["majayjay", "pagsanjan", 25]]

    #iteritively add edges too existing vertices
    for connection in connections:
        #add edge from vertex 1 to vertex 2
        data = add_egde(data, connection[0], connection[1], connection[2])
        #since graph is undirected add edege from vertex 2 to 1
        data = add_egde(data, connection[1], connection[0], connection[2])

    while True:
        choice = input("\nGraph Menu: \n\n1. Show shortest path from initial node to a destination node" 
                    + "\n2. Show shortest path to all nodes from an initial node"
                    + "\n3. Show all paths from initial node to destination"
                    + "\nX. Exit"
                    + "\n\nEnter your choice : ")

        if choice == "1":
            start = input("\nEnter start node: ").lower()
            destination = input("Enter destination node: ").lower()
            
            #check for if location in locations list and if start is equal to destination
            if start not in locations or destination not in locations:
                print("\nInvalid Location")
                continue

            print(f"\nShortest Path from {start} to {destination}\n")
            if start == destination:
                print(start)
                continue
            dijkstra(data, start, destination)

        elif choice == "2":
            start = input("\nEnter start node: ").lower()

            if start not in locations:
                print("\nInvalid Location")
                continue
            
            print(f"\nShortest Path from {start} to all other nodes\n")
            for location in locations:
                if start != location:
                    dijkstra(data, start, location)
        
        elif choice == "3":
            global visited
            n = len(vertices)
            path = []

            for element in vertices:
                visited.append(False)
            
            start = input("\nEnter start node: ").lower()
            destination = input("Enter destination node: ").lower()

            #check for if location in locations list
            if start not in locations or destination not in locations:
                print("\nInvalid Location")
                continue

            print(f"\nAll paths from {start} to {destination}\n")
            depthFirstSearch(data, start, destination, path)
        
        elif choice.upper() == "X":
            exit()
        
        else:
            print("\nInvalid Input")
        
"""
Type : DFS implementation to find all possible paths from source to destination Node
website link : https://www.geeksforgeeks.org/find-paths-given-source-destination/
"""

def depthFirstSearch(data, start, end, path):
    global visited
    
    graph = data[0]
    vertices = data[1]
    vertices_no = data[2] 

    startIndex = vertices.index(start)
    destinationIndex = vertices.index(end)
    
    #set visited value of current index to true
    visited[startIndex] = True
    #append current index to path
    path.append(startIndex)
    
    totalWeight = 0
    #if start = destination that means our path is complete, now print it
    if startIndex == destinationIndex:
        totalLineLength = 0
        for index in range(len(path)-1):   
            totalLineLength += len(vertices[path[index]])
            #next line if it reacher maximum python console line length of 79 for better formatting of printing
            if totalLineLength > 79:
                totalLineLength = 0
                print()
            totalWeight += graph[path[index]][path[index+1]]
            print(f'{vertices[path[index]]}', end = " -> ")
                
        print(f'{vertices[path[-1]]}\nWith a total distance of {totalWeight}\n')

    else:
        #get neighbor of current element and recursively call depthFirstSearch with start being set to these neighbors
        for i, row in enumerate(graph):
            if i == startIndex:
                for j, column in enumerate(graph):
                    if graph[i][j] != 0 and visited[j] == False:
                        depthFirstSearch(data, vertices[j], end, path)

    path.pop()
    visited[startIndex] = False

"""
Took Inpiration from : SuryaPratapK (github username)
Type : Dijkstra Algorithm - using list implementation
GitHub repository link : https://gist.github.com/SuryaPratapK/531ec1fd8efdaeb0c098b89a7a1a9d3e?fbclid=IwAR2V0YG7o9MWzxhZCWJ3pvC1rOvUjzuZYOIsyPs_z0BOp_Irr5Pz5xF-2Tw
"""

def dijkstra(data, start, end):
    graph = data[0]
    vertices = data[1]
    vertices_no = data[2]

    infinity = sys.maxsize

    values = [] #holds weight to get to that element
    parent = [] #hold parent of element in that index
    processed = [] #holds processed elements
          
    #initializing values
    #when accesing these lists, the indexes of location are parallel
    for value in vertices:
        parent.append(-1) #-1 signifies that parent is not yet set, this might be misinterpreted to being last index so be careful
        values.append(infinity) #sets current weight to get to the elements to a large number
        processed.append(False) #sets processed value for each element to false

    #get index from vertices list
    startIndex = vertices.index(start)
    endIndex = vertices.index(end)

    #set value of element to start dijkstra to 0 so that it will start from there
    values[startIndex] = 0
    #set start node to no parent set which is -1 in our case
    parent[startIndex] = -1

    for i in range(len(vertices)-1):
        #get lowest vertex total weight that has not yet been processed
        u = getLowestVertex(values, processed)
        #set parallel processed index to true
        processed[u] = True
        
        for j in range(len(vertices)):
            #if matrix value !=0 and not proccesed and weight not inifinity and new path which is total weight + new edge to take is less than current path to that node
            if graph[u][j] != 0 and processed[j] == False and values[u] != infinity and (values[u] + graph[u][j]) < values[j]:
                #set value at index of element to new path
                values[j] = values[u] + graph[u][j] 
                parent[j] = u

    #print paths
    #maybe this can be done recursively? come back to this later
    path = []
    path.append(vertices[endIndex])
    parentIndex = parent[endIndex]

    while True:
        path.append(vertices[parentIndex])
        if vertices.index(vertices[parentIndex]) == startIndex:
            break
        parentIndex = parent[parentIndex]

    #reverse it for printing
    path.reverse()

    for i in range(len(path)-1):
        print(path[i], end = " -> ")
    print(f'{path[-1]}\nWith a total distance of {values[vertices.index(end)]}\n')
 
def getLowestVertex(values, processed):
    minimum = sys.maxsize
    vertex = 0

    for index, value in enumerate(processed):
        if processed[index] == False and values[index] < minimum:
            vertex = index
            minimum = values[index]

    return vertex

visited = []
main()












