import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#app.filter_data()
def app():
    #df = pd.DataFrame(data)
    def get_data():
        data = pd.read_excel("Data/Full Dataset.xlsx")
        return data

    df = get_data()

    #raw material list
    raw_material =['Cotton','Organic_cotton','LinenHemp','Jute','Other_plant','Silk','Wool','Leather','Camel','Cashmere','Alpaca','Feathers','Other_animal','Polyester','Nylon','Acrylic','Spandex','Elastane','Polyamide','Other_synthetic','Lyocell','Viscose','Acetate','Modal','Rayon','Other_regenerated','Other']

    #filtering the cloth type
    Type = df['Type'].drop_duplicates()

    #select box for raw material selection
    Type_Choice = st.sidebar.selectbox('Select Type:', Type)
    raw_material_Choice = st.sidebar.selectbox('Select Raw_Material:', raw_material)

    #print(type(Type_Choice))
    #print(type(raw_material_Choice))

    #df1 = df[(df.Type == Type_Choice) & (df.loc[df[raw_material_Choice] != 0, ('Type',raw_material_Choice)].drop_duplicates())]
    df1 = df.loc[df[raw_material_Choice] != 0, ('Type',raw_material_Choice)].drop_duplicates()

    df2 = df1[df1.Type == Type_Choice]

    st.write(df2)



    #visulization for product
    ID = df['ID']

    Item_Code = st.sidebar.selectbox('Select ID:', ID)

    st.markdown(f"you chose {Item_Code}")

    df3 = df.loc[df['ID']==Item_Code]
    df4 = df3[['ID','Type','Cotton','Organic_cotton','Linen','Hemp','Jute','Other_plant','Silk','Wool','Leather','Camel','Cashmere','Alpaca','Feathers','Other_animal','Polyester','Nylon','Acrylic','Spandex','Elastane','Polyamide','Other_synthetic','Lyocell','Viscose','Acetate','Modal','Rayon','Other_regenerated','Other']]

    df5 = df4.T[df4.any()].T
    df6 = df5.iloc[:,2:]
    lables = df6.columns
    values = df6.values.flatten()

    # Creating plot
    fig = plt.figure(figsize =(2, 2))
    plt.pie(values, labels = lables)

    # show plot
    #plt.show()
    st.pyplot(fig)
