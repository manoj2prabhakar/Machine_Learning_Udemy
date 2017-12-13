#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:20:19 2017

@author: manoj2prabhakar
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

#Using dendrogram to find the optimal number of clusters

import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()

#Fitting Hierarchical clustering to the dataset
from sklearn.cluster import AgglomerativeClustering as ac
hc = ac(n_clusters = 5, affinity = 'euclidean' , linkage = 'ward')
y_hc = hc.fit_predict(X)

#Visualize the Cluster
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], c = 'red', s = 100, label = 'Careful')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], c = 'blue', s = 100, label = 'Standard')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], c = 'green', s = 100, label = 'Target')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], c = 'cyan', s = 100, label = 'Careless')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], c = 'magenta', s = 100, label = 'Sensible')
plt.title('Cluster of Customers')
plt.xlabel('Customers')
plt.ylabel('Annual Income ($)')
plt.legend()
plt.show()