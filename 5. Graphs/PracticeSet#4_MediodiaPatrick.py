def add_vertex(data, v):
    graph = data[0]
    vertices = data[1]
    vertices_no = data[2]

    if v in vertices:
        print("Veter",v,"already exists")

    else:
        vertices_no = vertices_no + 1
        vertices.append(v)
        
        #add 0 at end of current vertex list
        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)
        
        #add a new row to matrix for new vertex
        temp = []
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)

    return graph, vertices, vertices_no

def add_edge(data, v1, v2, e):
    