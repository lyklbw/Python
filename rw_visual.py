import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    
    rw=RandomWalk(50000)
    rw.fill_walk()

    #plt.figure(dpi=128,figsize=(10,6))了解相关参数之后使用，不然效果不佳

    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)
    point_number=list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Blues,edgecolor="none",s=1)

    plt.scatter(0,0,c='green',edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)

    


    plt.show()

    keep_running = input("Mkae another walk? (y/n): ")
    if keep_running == 'n':
        break