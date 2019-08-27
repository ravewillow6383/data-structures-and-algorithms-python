import pytest
from graphs import Graph, Vertex

def test_exists():
    assert Graph
    assert Vertex

# Node can be successfully added to the graph
def test_add_single():
    g = Graph()
    dogs = g.add_vertex('dogs')
    assert isinstance(dogs, Vertex)
    assert dogs.value == 'dogs'


def test_add_multiple():
    g = Graph()
    dogs = g.add_vertex('dogs')
    cats = g.add_vertex('cats')
    ferrets = g.add_vertex('ferrets')
    assert dogs.value == 'dogs'
    assert cats.value == 'cats'
    assert ferrets.value == 'ferrets'

def test_get_single():
    g = Graph()
    dogs = g.add_vertex('dogs')
    vertx = g.get_vertices()
    assert [vertex.value for vertex in vertx] == ['dogs']

# A collection of all nodes can be properly retrieved from the graph
def test_get_multiple():
    g = Graph()
    dogs = g.add_vertex('dogs')
    cats = g.add_vertex('cats')
    ferrets = g.add_vertex('ferrets')
    vertx = g.get_vertices()
    assert len(vertx) == 3
    assert {vertex.value for vertex in vertx} == set(['dogs', 'cats', 'ferrets'])

# The proper size is returned, representing the number of nodes in the graph
def test_length():
    g = Graph()
    dogs = g.add_vertex('dogs')
    cats = g.add_vertex('cats')
    assert len(g) == 2

# An empty graph properly returns none
def test_empty():
    g = Graph()
    assert g.get_vertices() == None

# An edge can be successfully added to the graph
def test_add_edge():
    g = Graph()
    dogs = g.add_vertex('dogs')
    cats = g.add_vertex('cats')
    ferrets = g.add_vertex('ferrets')
    g.add_edge(dogs, cats, 15)
    g.add_edge(dogs, ferrets, 12)

    pet_edge = dogs.neighbors[0]

# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
def test_get_neighbors():
    g = Graph()
    dogs = g.add_vertex('dogs')
    cats = g.add_vertex('cats')
    ferrets = g.add_vertex('ferrets')
    g.add_edge(dogs, cats, 15)
    g.add_edge(dogs, ferrets, 12)


    neighbors = g.get_neighbors(dogs)

    assert neighbors[0].vertex.value == 'cats'
    assert neighbors[0].weight == 15

    assert neighbors[1].vertex.value == 'ferrets'
    assert neighbors[1].weight == 12

# A graph with only one node and edge can be properly returned
def test_get_single_edge():
    g = Graph()
    dogs = g.add_vertex('dogs')
    g.add_edge(dogs, dogs, 15)

def test_breadth_first():
    g = Graph()
    dogs = g.add_vertex('dogs')
    cats = g.add_vertex('cats')
    ferrets = g.add_vertex('ferrets')
    g.add_edge(dogs, cats, 15)
    g.add_edge(dogs, ferrets, 12)

    visited = []

    def visit(vertex):
        visited.append(vertex.value)

    g.breadth_first(dogs, visit)

    assert visited == ['dogs', 'cats', 'ferrets']
