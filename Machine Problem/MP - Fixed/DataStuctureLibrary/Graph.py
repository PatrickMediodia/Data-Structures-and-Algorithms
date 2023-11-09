#Graph Adjacency Matrix Representation
class Graph:
    def __init__(self, matrix, vertices):
        self.matrix = matrix
        self.vertices = vertices

    def add_vertex(self, vertex):
        self.vertices.append(vertex)
        if len(self.vertices) > 1:
            for vertex in self.matrix:
                vertex.append(None)

        temp = []
        for index in range(len(self.vertices)):
            temp.append(None)
        self.matrix.append(temp)

    def add_egde(self, vertex1, vertex2, edge):
        self.matrix[vertex1][vertex2] = edge