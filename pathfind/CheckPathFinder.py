from pathfind.Graph import SimpleGraph
from pathfind.WeighFind import PathFinder

'''
    Let's create our map(visual_map) using two-dimensional array
    1 - is place where we can go
    0 - place where we cant go
    For e.g.
        
        1 1 1 1 1
        1 0 0 0 1   
        1 0 0 0 1
        1 0 0 0 1
        1 1 1 1 1 
                
'''
## like this
visual_map = [[1, 1, 1, 1, 1],
              [1, 0, 0, 0, 1],
              [1, 0, 0, 0, 1],
              [1, 0, 0, 0, 1],
              [1, 1, 1, 1, 1]]


## use generate_adj_matrix to convert visual_map to Matrix of Adjacency
graph = SimpleGraph()
graph.create_graph(25)
graph.generate_adj_matrix(visual_map)

## Time to find shortest path from 0 to 24-th element
## We expected [0, 1, 2, 3, 4, 9, 14, 19, 24]
##  ... or [0, 5, 10, 15, 20, 21, 22, 23, 24]

finder = PathFinder()
print(finder.weigh_find(0, 24, graph))

