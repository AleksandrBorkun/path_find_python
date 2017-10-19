class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, current):
        a = []
        arr = self.edges[current]
        for i in range(len(arr)):
            if arr[i] != 1000:
                a.append(i)
        return a

    def create_graph(self, size):
        for i in range(size):
            a = []
            for j in range(size):
                a.append(1000)
            self.edges[i] = a

    def insert_edge(self, begin, end):
        self.edges[begin][end] = 1
        self.edges[end][begin] = 1

    #  this method generate adjacency matrix of your graph from double array (from tetris structure to graph(tree))
    #  look here for e.p.
    #  (RUS) : https://habrahabr.ru/post/65367/
    #  (ENG) : http://www.geeksforgeeks.org/graph-and-its-representations/
    def generate_adj_matrix(self, visual_map):
        length = len(visual_map)
        for i in range(length):
            for j in range(length):
                if i != 0 and visual_map[i - 1][j] != 0 and visual_map[i][j] != 0:
                    self.insert_edge(length * (i - 1) + j, length * i + j)
                if j == length - 1:
                    continue
                if visual_map[i][j] != 0 and visual_map[i][j + 1] != 0:
                    self.insert_edge(length * i + j, length * i + j + 1)
