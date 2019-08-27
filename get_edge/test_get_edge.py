from queues import Queue
from get_edge import direct_flight
from graph import Graph
import pytest

def test_exists():
    assert direct_flight

def test_vanilla():
    g = Graph()
    dogs = g.add_vertex('paris')
    cats = g.add_vertex('rome')
    ferrets = g.add_vertex('seattle')
    g.add_edge('paris', 'rome', 25)
    g.add_edge('rome', 'seattle', 75)

    cities = ['paris', 'rome']

    assert direct_flight(g, cities) == True, '$25'