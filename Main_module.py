# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:05:29 2023

@author: ADMIN
"""

"""Importing Libraries"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_data(file) :
    """ 
    This function takes filename as argument and
    read the data file into dataframes 
    
    """
    data = pd.read_csv(file)
    datatranspose = data.set_index('Country Name').transpose()
    return data,datatranspose
country1 = ['Brazil', 'China', 'Canada', 'Denmark', 'Finland', 'Italy']
