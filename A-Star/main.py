# main.py

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

import random_map
import a_star

fig,ax = plt.subplots()
ax.cla()

map = random_map.RandomMap()

# ax.set_xlim([0, map.size])
# ax.set_ylim([0, map.size])

mapData = np.zeros((map.size, map.size,3))

for i in range(map.size):
    for j in range(map.size):
        if map.IsObstacle(i,j):
            mapData[i,j] = (1, 0, 0)

        else:
            mapData[i,j] = (1, 1, 1)

mapData[0,0] = (0, 0, 1)

mapData[map.size-1,map.size-1] = (0,1,0)

ax.imshow(mapData)
plt.pause(0.1)

a_star = a_star.AStar(map)
# a_star.RunAndSaveImage(ax, plt)

# while 1:
    # plt.pause(0.1)