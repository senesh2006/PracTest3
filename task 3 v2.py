import matplotlib.pyplot as plt
import numpy as np
from buzzness import Bee

def plot_hive(hive, blist, ax):
    xvalues = [b.get_pos()[0] for b in blist if b.get_inhive()]
    yvalues = [b.get_pos()[1] for b in blist if b.get_inhive()]
    ax.imshow(hive.T, origin="lower", cmap="YlOrBr") 
    ax.scatter(xvalues, yvalues, color='yellow')
    ax.set_title("Bee Hive Simulation")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")

def plot_world(world, hive_pos, ax):
    ax.imshow(world.T, origin="lower", cmap="tab20")
    ax.add_patch(plt.Rectangle((hive_pos[0]-2, hive_pos[1]-2), 4, 4, fill=False, edgecolor='red', linewidth=2))
    ax.set_title("Bee World Simulation")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")

simlength = 1
hiveX = 30
hiveY = 25
worldX = 100
worldY = 80
hive_pos = (50, 40)

b1 = Bee("b1", (5,10))
b2 = Bee("b2", (8,12))
b3 = Bee("b3", (15,8))
b4 = Bee("b4", (20,15))
b5 = Bee("b5", (10,20))
blist = [b1, b2, b3, b4, b5]

hive = np.ones((hiveX,hiveY)) * 10
hive[10:20, 10:15] = 0  # stripe of comb in center
hive[12, 11] = 3  # some honey cells
hive[14, 12] = 5
hive[16, 13] = 2
hive[18, 14] = 4

world = np.zeros((worldX, worldY))
# create different terrain in the world
world[30:60, 20:30] = 1  # forest area
world[10:25, 40:70] = 2  # flower field 1
world[70:90, 50:70] = 3  # flower field 2
world[40:50, 60:75] = 4  # water body
world[5:15, 5:15] = 5     # rocks

for t in range(simlength):
    for b in blist:
        b.step_change()
    fig, axes = plt.subplots(1, 2, figsize=(16,6))
    fig.suptitle("Bee Simulation Environment")
    
    plot_hive(hive, blist, axes[0])
    plot_world(world, hive_pos, axes[1])
    
    fig.savefig("task3.png")
    plt.show()
