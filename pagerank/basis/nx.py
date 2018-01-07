# -*- coding: utf-8 -*-

import networkx as nx

dg = nx.DiGraph()

dg.add_nodes_from(["A", "B", "C", "D", "E"])

dg.add_edge("A", "B")
dg.add_edge("A", "C")
dg.add_edge("A", "D")
dg.add_edge("B", "D")
dg.add_edge("C", "E")
dg.add_edge("D", "E")
dg.add_edge("B", "E")
dg.add_edge("E", "A")

print(*dg.neighbors("A"))
