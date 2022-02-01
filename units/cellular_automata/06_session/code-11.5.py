import matplotlib
matplotlib.use('TkAgg')
import numpy
import pylab

''' Current challenges:
Plots are shown side by sade for exercise 11.3, but an unused, empty window appears automatically on the background.
'''

n = 100 # size of space: n x n

def initialize(p):
    global config, nextconfig, density, ax1, ax2
    config = pylab.zeros([n, n])
    fig, (ax1, ax2) = pylab.subplots(2)
    density = []
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if pylab.random() < p else 0
    nextconfig = pylab.zeros([n, n])

def observe():
    global config, nextconfig, density,ax1, ax2
    #pylab.subplot(1,2,2)
    ax1.plot([i for i in range(len(density))], density)
    ax2.imshow(config, vmin = 0, vmax = 1, cmap = pylab.cm.binary)

def query_game_life(current, sum):
    output = 0
    if current == 0:
        if sum == 3: # given itself is not 1
            output = 1
    else:
        if sum == 3 or sum == 4: # given itself is 1
            output = 1
    return output

def update():
    global config, nextconfig, density
    for x in range(n):
        for y in range(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += config[(x + dx) % n, (y + dy) % n]
            nextconfig[x, y] = query_game_life(nextconfig[x, y], count) # modified rule
    config, nextconfig = nextconfig, config
    density.append(numpy.sum(config)/(n*n)) #altered to add density


import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
# self.modelInitFunc = func[0]
# self.modelDrawFunc = func[1]
# self.modelStepFunc = func[2]    