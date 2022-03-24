
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot():
    data = pd.read_csv("C:/Users/venkatesh.r.mullangi/Desktop/apperal/Data/data_output.csv")

    values = data['Cluster'].to_numpy()
    material = data['Raw Material']
    cost = data['Cost']

    # Figure Size
    fig, ax = plt.subplots(figsize =(16, 9))

    clrs = ['green' if (x == 0) else 'red' for x in values ]

    # Horizontal Bar Plot
    ax.barh(material, cost, color = clrs)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)

    # Add x, y gridlines
    ax.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)

    # Show top values
    ax.invert_yaxis()

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                 str(round((i.get_width()), 2)),
                 fontsize = 10, fontweight ='bold',
                 color ='grey')

    # Function add a legend
    colors = {'Non-Sustainable':'red', 'Sustainable':'green'}
    labels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)

    # Add Plot Title
    ax.set_title('Raw material and their price in Rupees',
                 loc ='left', )

    # Show Plot
    #plt.show()
    st.pyplot(fig)

def app():
    st.title('Apparel Data')
    param = st.radio(
         "Choose a Parameter",
         ('Price', 'Other'))

    if param == 'Price':
         plot()
    elif param == 'Other':
         st.write('...')
