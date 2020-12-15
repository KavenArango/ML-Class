# import numpy as np
# import pandas as pd
# import copy
# import math as mth
# import random
# import matplotlib.pyplot as plt

# random.seed(200)
# df = pd.DataFrame({
#     'x': [5, 10, 15, 24, 30, 55, 60, 71, 80, 85],
#     'y': [3, 15, 12, 10, 45, 52, 78, 80, 91, 70]
# })


# def distance(xy, mu):
#     return np.sqrt(np.sum((xy.sub(mu)) ** 2, axis=1))


# def mean(x):
#     return (sum(x) / len(x)) if len(x) != 0 else (sum(x) / 1)


# def makecentriods(k):
#     centroids = {
#         i+1: [random.randint(0, 80), random.randint(0, 80)]
#         for i in range(k)
#     }
#     return centroids


# def assign_cluster(df, centroids):
#     for i in centroids.keys():
#         df['dist{}'.format(i)] = (
#             distance(df[['x', 'y']], centroids[i])
#         )
#     centroid_distance_cols = ['dist{}'.format(i) for i in centroids.keys()]

#     df['closest_node'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)


# def calculate_new_centroid(k, centroids):
#     for i in centroids.keys():
#         centroids[i][0] = mean(df[df['closest_node'] == i]['x'])
#         centroids[i][1] = mean(df[df['closest_node'] == i]['y'])
#     return k


# def do_cluster(df, k):
#     centroids = makecentriods(k)
#     df = assign_cluster(df, centroids)

#     while True:
#         closest_centroids = df['closest_node'].copy(deep=True)
#         centroids = calculate_new_centroid(centroids, centroids)
#         df = assign_cluster(df, centroids)
#         if closest_centroids.equals(df['closest_node']):
#             break
#     plt.scatter(df['x'], df['y'], color=df['color'],
#                 alpha=0.2, edgecolor='k')
#     for i in centroids.keys():
#         x, y = centroids[i]
#         plt.scatter(x, y, s=100, color='green')
#     plt.show()

import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

df = pd.DataFrame({
    'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
    'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
})
colmap = {1: 'r', 2: 'g', 3: 'b', 4: 'm', 5: 'c', 6: 'y', 7: 'c'}


np.random.seed(100)
k = 4
# centroids[i] = [x, y]
centroids = {
    i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}


def assignment(df, centroids):
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = [
        'distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(
        lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df


df = assignment(df, centroids)
# print(df)


old_centroids = copy.deepcopy(centroids)


def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return k


for r in range(1):
    old_centroids = copy.deepcopy(centroids)
    centroids = update(centroids)

    fig = plt.figure(figsize=(5, 5))
    ax = plt.axes()
    plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i])
    plt.xlim(0, 80)
    plt.ylim(0, 80)
    for i in old_centroids.keys():
        old_x = old_centroids[i][0]
        old_y = old_centroids[i][1]
        dx = (centroids[i][0] - old_centroids[i][0]) * \
            0.75  # positioning arrow
        dy = (centroids[i][1] - old_centroids[i][1]) * \
            0.75  # positioning arrow
        ax.arrow(old_x, old_y, dx, dy, head_width=2,
                 head_length=3, fc=colmap[i], ec=colmap[i])
plt.show()
