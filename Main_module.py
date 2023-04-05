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
country2 = ['Brazil', 'France', 'Germany', 'India', 'Spain', 'United States']

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

def filter_line_plot(data) :
    """
    Defining function for filtering years and 
    countries for plotting line plot and returning the data
    
    """
    data = data[['Country Name', 'Indicator Name', '1991', '1997', '2004', '2010', '2016', '2019']]
    data = data[(data["Country Name"] == "Brazil")|
              (data["Country Name"] == "France")|
              (data["Country Name"] == "Germany")|
              (data["Country Name"] == "India")|
              (data["Country Name"] == "Spain")|
              (data["Country Name"] == "United States")]
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
    sp.set_xticks(x, country1, fontsize = 30)
    sp.legend(fontsize = 30)
   
    sp.bar_label(bar1, padding = 2, rotation = 90, fontsize = 20)
    sp.bar_label(bar2, padding = 2, rotation = 90, fontsize = 20)
    sp.bar_label(bar3, padding = 2, rotation = 90, fontsize = 20)
    plt.savefig("barplot.png")#Saving Barplot
    plt.show()
    plt.close()
    
#Function for plotting Line plot   
def line_plot(data, label1, label2) :
    plt.figure(figsize = (15, 15), layout = 'constrained')
    data_index = data.set_index('Country Name')
    transpose_data = data_index.transpose()
    transpose_data = transpose_data.drop(index = ['Indicator Name'])
    for i in range(len(country2)):
        plt.plot(transpose_data.index, transpose_data[country2[i]], label = country2[i])
    plt.title(label2, size = 18)
    plt.xlabel("----YEARS----", size = 20)
    plt.ylabel(label1, size = 20)
    plt.xticks(rotation = 45 , size = 15)
    plt.yticks(size = 20)
    plt.legend(fontsize = 15)
    plt.savefig("lineplot.png")#Saving Lineplot
    plt.show() 
    plt.close()
    
def pop_growth_mean() :   
  """
  
  Function to calculate the mean of population growth for 5 countries
  """
  dataf1,dataf2 = get_data("CSV_files/population_growth.csv")
  data = dataf1.set_index('Country Name')
  transpose = data.transpose()
  #Droping unneccessary columns
  transpose = transpose.drop(index = 'Indicator Code')
  transpose = transpose.drop(index = 'Indicator Name')  
  transpose = transpose.drop(index = 'Country Code')
  clean_data = transpose.fillna(0)
  mean = clean_data[["Brazil", "China", "Canada", "Denmark", "Finland", "Italy"]].describe()
  return mean

#Reading bar-data from csv file to data frames using the function get_data 
df_pop, pop_data1 = get_data("CSV_files/population_growth.csv")
df_pop = filter_bar_graph(df_pop)
df_Arable, Arable_data1 = get_data("CSV_files/Arable land.csv")
df_Arable = filter_bar_graph(df_Arable)  

#Reading line-data from csv file to data frames using the function get_data 
CO2_data, CO2_data1 = get_data("CSV_files/CO2_emission.csv")
CO2data = filter_line_plot(CO2_data)
CO2data.iloc[:,2:] = CO2data.iloc[:,2:]/1000000
CO2_data = CO2data
Cereal_data, Cereal_data1 = get_data("CSV_files/cereal.csv")
Cereal_data = filter_line_plot(Cereal_data)

 

#Plotting barplot for Population growth and Arable land
barplot(df_pop, "Growth of population in Billions", "Population Growth")
barplot(df_Arable, "Growth of Land", " THE GROWTH OF ARABLE LAND ")

#Plotting line plot for CO2 Emission and Cereal Yield
line_plot(CO2_data, "CO2 Emission", "CO2 Emission")
line_plot(Cereal_data, "Cereal yield", "Cereal Yield")

#Statistical function for returning mean for population growth data
pop_mean = pop_growth_mean()
print(pop_mean) 
print(pop_mean.mean())
 

##Writing data to csv file
pop_mean = pop_mean.to_csv("mean_of_population_growth.csv")
    