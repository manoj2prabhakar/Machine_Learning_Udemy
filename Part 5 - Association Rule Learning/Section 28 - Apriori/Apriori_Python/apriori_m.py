#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 08:04:14 2017

@author: manoj2prabhakar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

#Make the list of the products to supply it to apriori
transactions = []
for i in range(0, dataset.shape[0]):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
        
#Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, 
                min_support = 0.0028, 
                min_confidence = 0.2, 
                min_lift = 3, 
                min_length = 2)

#Visualizing the results
results = list(rules)

def inspect(results):
    rh          = [tuple(result[2][0][0])[0] for result in results]
    lh          = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(rh, lh, supports, confidences, lifts))

# the line creates a date frame which is accessible from Variable explorer
resultDataFrame=pd.DataFrame(inspect(results))

