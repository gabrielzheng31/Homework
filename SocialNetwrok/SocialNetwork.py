# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

data = []

with open('email-Eu-core.txt', 'r') as f:
    for line in f.readlines():
        temp = line.split()
        if(temp[0] == temp[1]):
            print(temp[0])
        data.append(tuple(line.split()));

G.add_edges_from(data)
#for G in nx.connected_component_subgraphs(G):
#    print(nx.average_shortest_path_length(G))

graphs = list(nx.connected_component_subgraphs(G))
for g in graphs:
    print(nx.info(g))

print(nx.degree_histogram(G))
