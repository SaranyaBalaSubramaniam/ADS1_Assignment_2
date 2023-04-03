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

def filter_bar_graph(data) :
    
    """
    Defining function for filtering years and 
    countries for plotting bar chart and returning the data
    
    """
    data = data[['Country Name', 'Indicator Name', '1990', '2000', '1994', '2013', '2019', '2020']]
    data = data[(data["Country Name"] == "Brazil")|
              (data["Country Name"] == "India")|
              (data["Country Name"] == "Canada")|
              (data["Country Name"] == "Denmark")|
              (data["Country Name"] == "Finland")|
              (data["Country Name"] == "Italy")]
    return data

#Function for plotting bar graph
def barplot(data, label1, label2) :
    plt.figure(figsize = (28, 20), layout = 'constrained')
    sp = plt.subplot(1, 1, 1)
    x = np.arange(6)
    width = 0.2
    
    bar1 = sp.bar(x, data["1990"], width, label = 1990, color = "Black")
    bar2 = sp.bar(x+width, data["1994"], width, label = 1994, color = "Blue")
    bar3 = sp.bar(x+width*2, data["2000"], width, label = 2000, color = "green")
    
    sp.set_xlabel("COUNTRY", fontsize = 40)
    sp.set_ylabel(label1, fontsize = 40)
    sp.set_title(label2, fontsize = 40)
    sp.set_xticks(x, country1, fontsize = 30, rotation = 90)
    sp.legend(fontsize = 30)
   
    sp.bar_label(bar1, padding = 2, rotation = 90, fontsize = 20)
    sp.bar_label(bar2, padding = 2, rotation = 90, fontsize = 20)
    sp.bar_label(bar3, padding = 2, rotation = 90, fontsize = 20)
    plt.savefig("barplot.png")#Saving Barplot
    plt.show()
    plt.close()
    
#Reading data from csv file to data frames using the function get_data 
df_pop, pop_data1 = get_data("CSV_files/population_growth.csv")
df_pop = filter_bar_graph(df_pop)
df_Arable, Arable_data1 = get_data("CSV_files/Arable land.csv")
df_Arable = filter_bar_graph(df_Arable)   

#Plotting barplot for Population growth and Arable land
barplot(df_pop, "Growth of population in Billions", "Population Growth")
barplot(df_Arable, "Growth of Land", " THE GROWTH OF ARABLE LAND ")
