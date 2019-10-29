# main.py

import numpy as np
import matplotlib.pyplot as plt

import a_star
from map import RandomMap

fig,ax = plt.subplots()
ax.cla()

map = RandomMap()
mapData = np.zeros((map.size, map.size,3), int)

map.SetupMap()

for grid in map.grid:
    i = grid.x
    j = grid.y
    if grid.value == -2:
        mapData[i,j] = (128,128,128) # Wall is gray
    elif grid.value == -1:
        mapData[i,j] = (0,0,0) # Obstacles' is black
    else:
        mapData[i,j] = (256,256,256) # Rest of map is white

ax.set_xlim([-1, map.size])
ax.set_ylim([-1, map.size])

ax.imshow(mapData)

a_star = a_star.AStar(map)
# a_star.RunAndSaveImage(ax, plt)

while 1:
    plt.pause(0.1)