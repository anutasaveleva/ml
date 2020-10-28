import numpy as np
import random
import matplotlib.pyplot as plt

cluster_num = 3
iter_num = 10
point_num = 30


# Finding distance between points
def dist(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Initializing random points for clasterization
def init_arr(n):
    arrx = np.array([random.uniform(0, 10) for i in range(n)])
    arry = np.array([random.uniform(0, 10) for i in range(n)])
    return arrx, arry


def cluster(k, x, y, x_cc, y_cc):
    clust = []
    for i in range(0, point_num):
        min = dist(x[i], y[i], x_cc[0], y_cc[0])
        min_num = 0
        for j in range(1, cluster_num):
            if min > dist(x[i], y[i], x_cc[j], y_cc[j]):
                min = dist(x[i], y[i], x_cc[j], y_cc[j])
                min_num = j
        clust.append(min_num)
    return clust

def recalc_centers(x_axis,y_axis,clusters, err):
    pass


a, b = init_arr(point_num)
#Finding center of points
x_cc = np.mean(a)
y_cc = np.mean(b)
r = []
for i in range(0, point_num):
    r.append(dist(a[i], b[i], x_cc, y_cc))
R = max(r)
x_c, y_c = [], []
for i in range(0, cluster_num):
    x_c.append(R * np.cos(2 * np.pi * i / cluster_num) + x_cc)
    y_c.append(R * np.sin(2 * np.pi * i / cluster_num) + y_cc)

# Cluster colors
colors = ['r','g','blue','y','black']
cl = cluster(cluster_num, a, b, x_c, y_c)
cl1 = []
for i in cl:
    cl1.append(colors[i])
plt.scatter(a, b, color=cl1)


# Centers of clusters are stars
plt.scatter(x_c, y_c, color=colors[:cluster_num], marker="*", s=100)
plt.show()
optimized = True

