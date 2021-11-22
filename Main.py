import doctest

import networkx as nx
import matplotlib.pyplot as plt


MAX_VAL=-9999

def vcg_cheapest_path(graph, source, target):
    """
    >>> G = nx.Graph()
    >>> G.add_edge('a', 'b', weight=3)
    >>> G.add_edge('a', 'c', weight=5)
    >>> G.add_edge('a', 'd', weight=10)
    >>> G.add_edge('b', 'c', weight=1)
    >>> G.add_edge('b', 'd', weight=4)
    >>> G.add_edge('c', 'd', weight=1)
    >>> G.add_edge('d', 'e', weight=2)
    >>> vcg_cheapest_path(G, 'a', 'd')
    ('a', 'b') Pays: -4
    ('a', 'c') Pays: 0
    ('a', 'd') Pays: 0
    ('b', 'c') Pays: -2
    ('b', 'd') Pays: 0
    ('c', 'd') Pays: -3
    ('d', 'e') Pays: 0
    >>> vcg_cheapest_path(G,'b','c')
    ('a', 'c') Pays: 0
    ('a', 'd') Pays: 0
    ('a', 'b') Pays: 0
    ('b', 'd') Pays: 0
    ('b', 'c') Pays: -5
    ('c', 'd') Pays: 0
    ('d', 'e') Pays: 0
    >>> vcg_cheapest_path(G,'b','e')
    ('a', 'c') Pays: 0
    ('a', 'd') Pays: 0
    ('a', 'b') Pays: 0
    ('b', 'd') Pays: 0
    ('b', 'c') Pays: -3
    ('c', 'd') Pays: -3
    ('d', 'e') Pays:  -9999
    >>> vcg_cheapest_path(G,'b','d')
    ('a', 'c') Pays: 0
    ('a', 'd') Pays: 0
    ('a', 'b') Pays: 0
    ('b', 'd') Pays: 0
    ('b', 'c') Pays: -3
    ('c', 'd') Pays: -3
    ('d', 'e') Pays: 0
    >>> vcg_cheapest_path(G,'a','e')
    ('a', 'c') Pays: 0
    ('a', 'd') Pays: 0
    ('a', 'b') Pays: -4
    ('b', 'd') Pays: 0
    ('b', 'c') Pays: -2
    ('c', 'd') Pays: -3
    ('d', 'e') Pays:  -9999
    >>> vcg_cheapest_path(G,'a','g')
    Traceback (most recent call last):
    ...
    networkx.exception.NetworkXNoPath: No path to g.



    """

    distance, path = nx.single_source_dijkstra(graph, source, target)
    path = list(zip(path, path[1:]))
    # print(path)
    distance *= -1

    for e in graph.edges:
        if e not in path:
            print(f"{e} Pays: 0")
        else:
            w = graph.edges[e[0], e[1]]['weight'] * -1
            graph.remove_edge(e[0], e[1])
            try:
                new_distance = nx.single_source_dijkstra(graph, source, target)[0] * -1
                print(f"{e} Pays: {new_distance - (distance - w)}")
            except  nx.NetworkXNoPath as ex:
                print(f"{e} Pays:  {MAX_VAL}")
            finally:
                graph.add_edge(e[0], e[1], weight=w * -1)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

