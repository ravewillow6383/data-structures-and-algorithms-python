import pytest
from breadth_first import Graph

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

def test_single_vertex():
    g = Graph()
    dogs = g.add_vertex('dogs')

    visited = []

    def visit(vertex):
        visited.append(vertex.value)

    g.breadth_first(dogs, visit)

    assert visited == ['dogs']


def test_empty():
    g= Graph()
    dogs = g.add_vertex('')

    visited = []

    def visit(vertex):
        visited.append(vertex.value)


    g.breadth_first(dogs, visit)

    assert visited == ['']

    

    assert visited == ['dogs', 'cats', 'ferrets']
