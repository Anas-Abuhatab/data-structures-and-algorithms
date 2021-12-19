from breadth_first_graph.breadth_first_graph import Graph

def test_breadth_first_single():
    graph = Graph()
    a = graph.add_node('a')
    actual = graph.breadth_first(a)
    assert actual == [a.value]

def test_breadth_first_multiple():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    actual = graph.breadth_first(a)
    assert actual == [a.value, b.value, c.value]

def test_breadth_first_many():
    graph = Graph()
    a = graph.add_node('Prandora')
    b = graph.add_node('Arendelle')
    c = graph.add_node('Metroville')
    d = graph.add_node('Monstroplolis')
    e = graph.add_node('Narnia')
    f = graph.add_node('Naboo')
    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(b, d)
    graph.add_edge(c, d)
    graph.add_edge(c, e)
    graph.add_edge(c, f)
    graph.add_edge(d, f)
    graph.add_edge(f, e)
    actual = graph.breadth_first(a)
    assert actual == [a.value, b.value, c.value, d.value, e.value, f.value]
