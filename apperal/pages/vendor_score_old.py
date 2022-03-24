import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def rank_suppliers():
    sup=pd.read_excel("C:/Users/venkatesh.r.mullangi/Desktop/apperal/Data/Supplier_data_another.xlsx",sheet_name='Data')
    Feature_Metadata=pd.read_excel("C:/Users/venkatesh.r.mullangi/Desktop/apperal/Data/Supplier_data_another.xlsx",sheet_name='Metadata')

    #Feature_Metadata
    sup=sup.replace(0,0.0001)
    #sup

    sup1=pd.DataFrame()
    beneficial=[]
    non_beneficial=[]
    # Taking out beneficial criteria (where we want maximum profit)
    beneficial=Feature_Metadata[(Feature_Metadata["Feature_Nature"] =="Beneficial")]['Feature'].tolist()
    # print("Beneficial Criteria",beneficial)
    # As per AHP (Analytical Hierarchy Processing) of MCDM (Multi Criteria Decision Making Methods),

    for i in beneficial:
    #     print(i)
        sup1[i]=sup[i]/sup[i].max()
    #     print(sup1)


    # Taking out non-beneficial criteria (where we want minimum values)
    non_beneficial=Feature_Metadata[(Feature_Metadata["Feature_Nature"] =="Non-Beneficial")]['Feature'].tolist()
    #print("Non-Beneficial Criteria",non_beneficial)
    for i in non_beneficial:
    #     print(i)
        sup1[i]=sup[i].min()/sup[i]
    #     print(sup1)

    sup1



    capability=[]
    performance=[]
    capability=Feature_Metadata[(Feature_Metadata["Feature_Type"] =="Capability")]['Feature'].tolist()
    performance=Feature_Metadata[(Feature_Metadata["Feature_Type"] =="Performance")]['Feature'].tolist()

    capability_len=len(capability)
    capability_weight=0.5
    for i in range(capability_len):
    #     print(capability[i])
        sup1[capability[i]]=sup1[capability[i]]*(capability_weight/capability_len)

    performance_len=len(performance)
    performance_weight=0.5
    for i in range(performance_len):
    #     print(performance[i])
        sup1[performance[i]]=sup1[performance[i]]*(performance_weight/performance_len)

    sup1

    sup1['Score']=sup1.sum(axis=1)
    # sup1['score']=sup1['QMP']+sup1['SA']+sup1['PMC']+sup1['Mgt']+sup1['DD']+sup1['CR']+sup1['Quality']+sup1['Price']+sup1['Delivery']+sup1['CRP']+sup1['Other']
    sup1


    sup1['Supplier']=sup['Supplier']
    sup1=sup1.sort_values(by='Score', ascending=False)
#     sup1

    return(sup1)


sup1=rank_suppliers()


def plotme(sup_plot):
    fig = plt.figure(figsize=(12,8))
    # sup1=sup1.sort_values('Score',ascending=False)
    axis1=sns.barplot(x=sup_plot['Score'],y=sup_plot['Supplier'], data=sup_plot)
    plt.xlim=(0,1)
    plt.title('Supplier Ranking Visualization',weight='bold')
    plt.xlabel('Ranking Score',weight='bold')
    plt.ylabel('Supplier',weight='bold')
    #plt.savefig('suppliers_rank.png')
    st.pyplot(fig)


def app():
    st.title('Supplier Score')
    plotme(sup1)
    vendor_list = ['S1','S2','S3','S4','S5']
    vendor = st.sidebar.selectbox('Select a Supplier:', vendor_list)

    col1, col2, col3 = st.columns(3)
    if col2.button('Place your Order'):
        st.write(f'Order has been placed with Supplier {vendor}')
    else:
        st.write('please select a Supplier and place your order')
