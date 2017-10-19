from queue import Queue
from pathfind import Graph


class PathFinder:
    def __init__(self):
        pass

    def weigh_find(self, start, goal, graph):
        frontier = Queue()
        frontier.put(start)
        visited = {}
        visited[start] = True
        came_from = {}
        while not frontier.empty():
            current = frontier.get()
            temp = current
            for next in graph.neighbors(current):
                if next not in visited:
                    frontier.put(next)
                    came_from[next] = temp
                    visited[next] = True

        current = goal
        path = [current]
        while current != start:
            current = came_from.get(current)
            path.append(current)
        path.reverse()  # optional
        return path
