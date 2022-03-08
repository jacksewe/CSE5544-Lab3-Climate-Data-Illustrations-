
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np



st.title("Lab 3")

data = pd.read_csv("https://raw.githubusercontent.com/jacksewe/data/main/ClimateData.csv")

# Stats with country, year, emissions as columns
st.header("Stats")
chart_data = data.drop(columns=['Non-OECD Economies'])
chart_data = pd.melt(chart_data, id_vars=['Country\year'], var_name='year')
chart_data['value'] = chart_data['value'].apply(pd.to_numeric, errors='coerce')
chart_data['year'] = chart_data['year'].apply(pd.to_numeric, errors='coerce')
chart_data.rename(columns={"Country\year": "country", "value":"emission"}, inplace = True)
chart_data

#Heatmap P1
st.header("P1")                                            
y_ticks = np.arange(1990, 2020, 1)  
fig = plt.figure(figsize = (6,3))  
ax = fig.add_subplot(1,1,1) 
s = ax.scatter('country', 'year', c = 'emission',data = chart_data, cmap = 'inferno_r', marker = 's',s = 15)
xaxis = plt.xticks(rotation=90, ha='center', fontsize=5)
yaxis = plt.yticks(fontsize=5)    
ax.set_yticks(y_ticks) 
#ax.grid(which='both', alpha = 0.3)                                                                                                           
#ax.grid(which='major', alpha=0.3) 
ax.set_xlabel('country', fontsize=10);
ax.set_ylabel('year', fontsize=10);
ax.set_title('Emissions of Countries by Year', size = 15)
cbar = plt.colorbar(mappable = s,ax = ax)
st.pyplot(fig)
st.caption("As we can see here the color map used here has a monotonically increasing light value.  This is means that it will be better perceived by the human brain.  This is a more honest graph because it is easy for the user to see which countries and which years have more emission, because of the sequential colormap.  This colormap is better for this graph because it can be said that the emissions can be ordered from least to greatest.")

#Heatmap P2
st.header("P2")                                            
y_ticks = np.arange(1990, 2020, 1)  
fig = plt.figure(figsize = (6,3))  
ax = fig.add_subplot(1,1,1) 
s = ax.scatter('country', 'year', c = 'emission',data = chart_data, cmap = 'rainbow', marker = 's',s = 15)
xaxis = plt.xticks(rotation=90, ha='center', fontsize=5)
yaxis = plt.yticks(fontsize=5)    
ax.set_yticks(y_ticks) 
#ax.grid(which='both', alpha = 0.3)                                                                                                           
#ax.grid(which='major', alpha=0.3) 
ax.set_xlabel('country', fontsize=10);
ax.set_ylabel('year', fontsize=10);
ax.set_title('Emissions of Countries by Year', size = 15)
cbar = plt.colorbar(mappable = s,ax = ax)
st.pyplot(fig)
st.caption("As we can see here the color map used here has the colors of a rainbow.  This type of color map does not have a particular use because of the varying light value throughout the colormap.  This means it will be harder for the human brain to perceive which value is more and which value is less.  This is a more dishonest graph because it is hard for the user to see which countries and which years have more emission, because of the varying light values.  This colormap is not a very good choice for this graph unless you want to make it confusing for the reader.")
