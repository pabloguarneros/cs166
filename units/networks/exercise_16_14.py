import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import random as rd

n = 16 # number of nodes
k = 4 # number of neighbors of each node

def initialize():
    global g
    g = nx.grid_graph(dim=[4,4])
    for i in g.adj:
        for j in g.adj[i]:
            g.add_edge(i, j)
    g.count = 0

def observe():
    global g
    cla()
    nx.draw(g)

def update():
    global g
    g.count += 1
    if g.count % 20 == 0: # rewiring once in every 20 steps
        nds = list(g.nodes)
        i = rd.choice(nds)
        if g.degree[i] > 0:
            g.remove_edge(i, rd.choice(list(g.neighbors(i))))
            nds.remove(i)
            for j in g.neighbors(i):
                nds.remove(j)
            g.add_edge(i, rd.choice(nds))

    # simulation of node movement
    g.pos = nx.spring_layout(g, iterations = 5)

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])