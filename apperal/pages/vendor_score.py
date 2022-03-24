import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def rank_suppliers():

    sup=pd.read_excel("Data/Supplier_data_another.xlsx",sheet_name='Data')
    Feature_Metadata=pd.read_excel("Data/Supplier_data_another.xlsx",sheet_name='Metadata')

    sup=sup.replace(0,0.0001)
    sup1=pd.DataFrame()
    beneficial=[]
    non_beneficial=[]
    beneficial=Feature_Metadata[(Feature_Metadata["Feature_Nature"] =="Beneficial")]['Feature'].tolist()


    for i in beneficial:
        sup1[i]=sup[i]/sup[i].max()

    non_beneficial=Feature_Metadata[(Feature_Metadata["Feature_Nature"] =="Non-Beneficial")]['Feature'].tolist()
    for i in non_beneficial:
        sup1[i]=sup[i].min()/sup[i]

    capability=[]
    performance=[]
    capability=Feature_Metadata[(Feature_Metadata["Feature_Type"] =="Capability")]['Feature'].tolist()
    performance=Feature_Metadata[(Feature_Metadata["Feature_Type"] =="Performance")]['Feature'].tolist()

    capability_len=len(capability)
    capability_weight=0.5
    for i in range(capability_len):
        sup1[capability[i]]=sup1[capability[i]]*(capability_weight/capability_len)

    performance_len=len(performance)
    performance_weight=0.5
    for i in range(performance_len):
        sup1[performance[i]]=sup1[performance[i]]*(performance_weight/performance_len)

    sup1['Score']=sup1.sum(axis=1)

    sup1['Risk_Score']=1-sup1['Score']
    sup1['Supplier']=sup['Supplier']

    sup1=sup1.sort_values(by='Risk_Score', ascending=True)

    selected_suppliers=pd.DataFrame()
    selected_suppliers=sup1[0:5]
    return(selected_suppliers)



def plotme_risk_score(plotter):
    fig1 = plt.figure(figsize=(4,2))
    #fig1.patch.set_facecolor('black')
    #fig1.patch.set_alpha(0.001)
    plotter=plotter.sort_values('Risk_Score',ascending=True)
    axis1=sns.barplot(x=plotter['Risk_Score'],y=plotter['Supplier'].head(5), data=plotter)
    plt.xlim=(0,1)
    plt.title('Supplier Risk Evaluation',weight='bold')
    plt.xlabel('Risk Score',weight='bold')
    plt.ylabel('Supplier',weight='bold')
    st.pyplot(fig1)



def plotme_price(plotter):
    fig2 = plt.figure(figsize=(4,2))
    plotter=plotter.sort_values('Price',ascending=True)
    axis1=sns.barplot(x=plotter['Price'],y=plotter['Supplier'].head(5), data=plotter)
    plt.xlim=(0,1)
    plt.title('Price Evaluation of Candidate Suppliers',weight='bold')
    plt.xlabel('Price',weight='bold')
    plt.ylabel('Supplier',weight='bold')
    st.pyplot(fig2)



def plotme_QMP(plotter):
    fig3 = plt.figure(figsize=(4,2))
    plotter=plotter.sort_values('QMP',ascending=True)
    axis1=sns.barplot(x=plotter['QMP'],y=plotter['Supplier'].head(5), data=plotter)
    plt.xlim=(0,1)
    plt.title('Quality Evaluation of Candidate Suppliers',weight='bold')
    plt.xlabel('QMP',weight='bold')
    plt.ylabel('Supplier',weight='bold')
    st.pyplot(fig3)

output=rank_suppliers()
#print(out)


#plotme_price(output)


def app():
    st.title('Supplier Score')
    #plotme(sup1)
    vendor_list = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','S14','S15','S16','S17','S18','S19','S20','S21','S22','S23']
    vendor = st.sidebar.selectbox('Select a Supplier:', vendor_list)

    '''
    col1, col2, col3 = st.columns(3)
    if col1.button('Risk_Score') or session_state.key==1 :
        st.write('Risk Score')
        plotme_risk_score(output)

    if col2.button('Price') or session_state.key==2:
        st.write('Price')
        plotme_price(output)

    if col3.button('QMP')  or session_state.key==3:
        st.write('QMP')
        plotme_QMP(output)
    '''

    param = st.radio(
         "Check the score",
         ('Risk', 'Price', 'QMP'))

    if param == 'Risk':
         st.write('Risk Score')
         plotme_risk_score(output)
    elif param == 'Price':
         st.write('Price')
         plotme_price(output)
    elif param == 'QMP':
        st.write('QMP')
        plotme_QMP(output)

    st.markdown('Select a supplier and place your order')
    col1, col2, col3 = st.columns(3)
    if col2.button('Place Order'):
        st.write(f'your order has been placed with {vendor}')
