import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.title('Apperal Data')
    #st.write('This is a table')

    #reading the data
    @st.cache
    def get_data():
        data = pd.read_excel("Data/Full Dataset.xlsx")
        return data

    df = get_data()
    st.write(df)

    Type = df['Type'].drop_duplicates()
    EI = df['EI'].drop_duplicates()
    Manufacturing_location  = df['Manufacturing_location'].drop_duplicates()
    Use_location = df['Use_location'].drop_duplicates()
    Reusability_label = df['Reusability_label'].drop_duplicates()
    Recylability_label = df['Recylability_label'].drop_duplicates()

    #models = df['model']
    #engines = df['engine']
    #components = df['components']

    Type_Choice = st.sidebar.selectbox('Select Type:', Type)
    '''
    EI_Choice  = st.sidebar.selectbox('Select EL:', EI)
    Manufacturing_location = st.sidebar.selectbox('Select Manufacturing_location:', Manufacturing_location)
    Use_location = st.sidebar.selectbox('Select Use_location:', Use_location)
    Reusability_label = st.sidebar.selectbox('Reusability_label:', Reusability_label)
    Recylability_label = st.sidebar.selectbox('Recylability_label:', Recylability_label)

    #Filtering DataFrame
    st.title('Filtered Data')
    #df.loc[df['Type']=Type_Choice

    df1 = df[(df.Type == Type_Choice) & (df.EI== EI_Choice) & (df.Manufacturing_location==Manufacturing_location)&
    (df.Use_location==Use_location)&(df.Reusability_label==Reusability_label)&(df.Recylability_label==Recylability_label)]
    '''



    #st.write(df1)
