import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'x': [5, 10, 15, 24, 30, 55, 60, 71, 80, 85],
    'y': [3, 15, 12, 10, 45, 52, 78, 80, 91, 70]
})
colors = {1: 'r', 2: 'g', 3: 'b', 4: 'm', 5: 'c', 6: 'y'}


def distance(xy, mu):
    return np.sqrt(np.sum((xy.sub(mu)) ** 2, axis=1))


def assignment(df, centroids):
    for i in centroids.keys():
        df['distomu_{}'.format(i)] = (
            distance(df[['x', 'y']], centroids[i])
        )
    centroid_distance_cols = ['distomu_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distomu_')))
    df['color'] = df['closest'].map(lambda x: colors[x])
    return df


def update(k, centroids):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return k


def getDataAndUpdate(df, k):
    centroids = {
        i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
        for i in range(k)
    }
    df = assignment(df, centroids)
    while True:
        closest_centroids = df['closest'].copy(deep=True)
        centroids = update(centroids, centroids)
        df = assignment(df, centroids)
        if closest_centroids.equals(df['closest']):
            break
    plt.scatter(df['x'], df['y'], color=df['color'],
                alpha=0.2, edgecolor='k')
    for i in centroids.keys():
        x, y = centroids[i]
        plt.scatter(x, y, s=100, color='green')
    plt.show()


while True:
    getDataAndUpdate(df, k=2)
