import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
#from pages.test import data as ap_data


df=pd.read_excel("C:/Users/venkatesh.r.mullangi/Desktop/apperal/Data/Physical properties.xlsx")
data4 = pd.read_csv("C:/Users/venkatesh.r.mullangi/Desktop/apperal/Data/data4.csv")
material_data = pd.read_excel("C:/Users/venkatesh.r.mullangi/Desktop/apperal/Data/materail_composition.xlsx")

df = pd.merge(df, data4, on='Material')



#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')
#Replace NaN with an empty string
df['Description'] = df['Description'].fillna('')
#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(df['Description'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['Material']).drop_duplicates()

# Function that takes in rawmaterial as input and outputs most similar Rawmaterials
def get_recommendations(Material, cosine_sim=cosine_sim):

    idx = indices[Material]
    # Get the pairwsie similarity scores of all rawmaterials with that raw material
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the raw materials based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 5 most similar raw materials
    sim_scores = sim_scores[1:6]

    # Get the raw material indices
    material_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar materials
    return df['Material'].iloc[material_indices]

#def sus_plot():



def app():
    #st.write(material_data)
    Raw_Material = df['Material'].drop_duplicates()
    Material_Choice = st.sidebar.selectbox('Select a Raw Material:', Raw_Material)

    if st.button('Get_Recommendation'):
        Alternate_Material = get_recommendations(Material_Choice)
        Alternate_Material = pd.DataFrame({'Material':Alternate_Material.to_list()})
        Alternate_Material = pd.merge(Alternate_Material,df, on='Material').drop(columns = ['Description'])
        Alternate_Material['Cluster'].loc[df['Cluster'] == 0.0] = 'Sustainable'
        Alternate_Material['Cluster'].loc[df['Cluster'] == 1.0] = 'Unsustainable'
        st.write(Alternate_Material)

    else:
        st.write('Please Select a Raw Materail and click the button to get ALternative Raw Materail ')
