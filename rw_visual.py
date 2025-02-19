import matplotlib.pyplot as plt

from random_walk import RandomWalk 

while True:
    #create a random walk and fill
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #plot
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize = (10, 6), dpi=128)
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap='Blues', edgecolors='none', s=1)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #removing the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    running = input("Make another walk? (y/n)")
    if running == 'n':
        break
