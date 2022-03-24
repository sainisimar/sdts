import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from pages import apperal,visualizations,similarity_score
from streamlit_echarts import st_echarts
#import SessionState

'''
def render_pie_simple():
    print('lables and values',data())
    #lables,values = data()
    #print(lables,values)

    options = {
        "title": {"text": "apperal", "subtext": "", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left",},
        "series": [
            {
                "name": "apperal data",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 0.4, "name": "Cotton"},
                    {"value": 0.6, "name": "Organic_cotton"},
                    #{"value": 580, "name": "3"},
                    #{"value": 484, "name": "4"},
                    #{"value": 300, "name": "5"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
    st_echarts(
        options=options, height="600px",
    )

ST_PIE_DEMOS = {
    "Pie: Simple Pie": (
        render_pie_simple,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-simple",
    ),

}
'''

def data():
    #reading the data
    @st.cache
    def get_data():
        data = pd.read_excel("Data/partial_data.xlsx")
        return data

    df = get_data()

    Type = df['Type'].drop_duplicates()

    Type_Choice = st.sidebar.selectbox('Select Type:', Type,key='1')
    #Type_Choice = st.sidebar.selectbox('Select Type:', Type,key='2')

    st.markdown(f"you chose {Type_Choice}")

    df1 = df.loc[df['Type']==Type_Choice]
    df2 = df1[['ID','Type','Cotton','Organic_cotton','Linen','Hemp','Jute','Other_plant','Silk','Wool','Leather','Camel','Cashmere','Alpaca','Feathers','Other_animal','Polyester','Nylon','Acrylic','Spandex','Elastane','Polyamide','Other_synthetic','Lyocell','Viscose','Acetate','Modal','Rayon','Other_regenerated','Other']]

    df3 = df2.T[df2.any()].T
    df4 = df3.iloc[:,2:]
    labels = df4.columns
    values = df4.values.flatten()
    #labels1 = labels
    df4.to_excel('Data/materail_composition.xlsx')

    return labels,values

def render_pie_simple():
    labels,values = data()
    fig = go.Figure(
    go.Pie(
    labels = labels,
    values = values,
    hoverinfo = "label+percent",
    textinfo = "value"))
    st.plotly_chart(fig)



def app():
    st.title('Apparel Data')
    render_pie_simple()
    #recommendations()

    #labels,values,labels1 = data()
    #col1, col2, col3 = st.columns(3)
    #if col2.button('Get_Recommendation'):
        #for i in range(len(labels1)):
        #st.write('Hello')

    #else:
        #st.write('none')
