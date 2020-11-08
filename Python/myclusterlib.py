#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as mth
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def euclidian_distance(x, y, centroid_x, centroid_y):
    dist = mth.sqrt((x-centroid_x)**2 + (y - centroid_y)**2)
    return dist

def assign_cluster(C1X, C1Y, C2X, C2Y, data):
    newdata = pd.DataFrame([])
    i = 0
    if(len(data['x']) != len(data['y'])):
        raise Exception('There seems to be missing entries in the data! The columns do not have the same length!')
        
    while i < len(data['x']):
        e_dist_C1 = euclidian_distance(data['x'][i], data['y'][i], C1X, C1Y)
        e_dist_C2 = euclidian_distance(data['x'][i], data['y'][i], C2X, C2Y)
        if e_dist_C1 < e_dist_C2:
            ass_cluster = 'C1'
        else:
            ass_cluster = 'C2'
        newdata = newdata.append({
            'DataPoint_x' : data['x'][i],
            'DataPoint_y' : data['y'][i],
            'e_dist_C1' : e_dist_C1,
            'e_dist_C2' : e_dist_C2,
            'Assigned_Cluster' : ass_cluster
            }, ignore_index=True)
        i += 1
    newdata = newdata[['DataPoint_x', 'DataPoint_y', 'e_dist_C1', 'e_dist_C2', 'Assigned_Cluster']]
    
    return newdata

def mean(x):
    return round((sum(x) / len(x)), 2)

def calc_new_centroid(ass_cluster):
    i = 0
    cluster1_x = []
    cluster1_y = []
    cluster2_x = []
    cluster2_y = []
    while i < len(ass_cluster.index):
        if ass_cluster['Assigned_Cluster'][i] == 'C1':
            cluster1_x.append(ass_cluster['DataPoint_x'][i])
            cluster1_y.append(ass_cluster['DataPoint_y'][i])
        else:
            cluster2_x.append(ass_cluster['DataPoint_x'][i])
            cluster2_y.append(ass_cluster['DataPoint_y'][i])
        i += 1

    return mean(cluster1_x), mean(cluster1_y), mean(cluster2_x), mean(cluster2_y)


def do_label(cluster):
    j = 0
    labels = []
    while (j < len(cluster["Assigned_Cluster"])):
        if (cluster["Assigned_Cluster"][j] == 'C1'):
            labels.append(0)
        else:
            labels.append(1)
        j += 1
    return labels

def do_cluster(in_data):
    centroid1_x = in_data['x'][0]
    centroid1_y = in_data['y'][0]
    centroid2_x = in_data['x'][1]
    centroid2_y = in_data['y'][1]

    while True:
        ac = assign_cluster(centroid1_x, centroid1_y, centroid2_x, centroid2_y, in_data)
        new_centroid1_x, new_centroid1_y, new_centroid2_x, new_centroid2_y = calc_new_centroid(ac)
        
        labels = do_label(ac)
        
        plt.scatter(ac['DataPoint_x'], ac['DataPoint_y'], c=labels, cmap='rainbow') 
        plt.scatter([new_centroid1_x, new_centroid2_x] ,[new_centroid1_y, new_centroid2_y],  s= 100, color='green')
        plt.show()
        if ((centroid1_x == new_centroid1_x) and (centroid1_y == new_centroid1_y) and (centroid2_x == new_centroid2_x) and (centroid2_y == new_centroid2_y)):
            break
        else:
            centroid1_x = new_centroid1_x
            centroid1_y = new_centroid1_y
            centroid2_x = new_centroid2_x
            centroid2_y = new_centroid2_y
        
    return new_centroid1_x, new_centroid1_y, new_centroid2_x, new_centroid2_y, ac


# In[ ]:




