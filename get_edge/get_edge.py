from queues import Queue
from graph import Graph, Vertex, Edge


def direct_flight(g, lst):
    g = Graph()
    cost = 0
    q = Queue()
    
    for city in lst:
        q.enqueue(city)
    
    while q:
        current = q.dequeue()
        neighs = g.get_neighbors(current)
        n = len(neighs) - 1

        for i in range(0, n):
            if neighs[i].vertex.value == q.front.value:
                cost += neighs[i].weight
            else:
                return f'{False}, $0'
    return f'{True}, ${cost}'