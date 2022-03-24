import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

df=pd.read_excel("Data/Physical properties.xlsx")
data4 = pd.read_csv("Data/data4.csv")

df = pd.merge(df, data4, on='Material')

#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')
#Replace NaN with an empty string
df['Description'] = df['Description'].fillna('')
#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(df['Description'])
#Output the shape of tfidf_matrix
tfidf_matrix.shape
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
    df1 = pd.DataFrame(data = sim_scores)
    df1.columns = ['material_indices', 'Score']


    # Get the raw material indices
    material_indices = [i[0] for i in sim_scores]

    df2 = df[['Material']].iloc[material_indices]
    df2.reset_index(inplace = True)
    df3 = pd.concat([df1,df2], axis = 1)

    # Return the top 5 most similar materials
    return df3

def sus_plot():
    material_data = pd.read_excel("Data/materail_composition.xlsx")
    material_data=material_data.drop(['Unnamed: 0'],axis=1)
    material_data=material_data.T
    material_data.reset_index(inplace=True)
    material_data = material_data.rename(columns = {'index':'Material'})
    material_data = material_data.rename(columns = {0:'Composition'})
    merged_data=pd.merge(material_data, data4, on='Material', how='left')
    Cluster = merged_data['Cluster'].to_numpy()
    material = merged_data['Material']
    comp = merged_data['Composition']
    # Figure Size
    # explode=[0.1,0,0]
    fig, ax = plt.subplots(figsize =(1, 1))

    fig.patch.set_facecolor('black')
    fig.patch.set_alpha(0.001)
    clrs = ['green' if (x == 0) else 'red' for x in Cluster ]
    patches, texts, autotexts = ax.pie(comp,labels = material, autopct ='% 1.1f %%',colors=clrs,shadow = False, startangle = 90)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(4)
    for texts in texts:
        texts.set_color('white')
        texts.set_fontsize(4)


    ax.axis('equal')
    plt.title('''Product Composition
              (Sustainable and non Sustainable proportions)''',
         color = 'white', fontsize = '6')

    st.pyplot(fig)



def app():
    #st.write('Sustainable')
    sus_plot()

    Raw_Material = df['Material'].drop_duplicates()
    Material_Choice = st.sidebar.selectbox('Select a Raw Material:', Raw_Material)
    col1, col2, col3 = st.columns(3)
    if col2.button('Get_Recommendation'):
        Alternate_Material = get_recommendations(Material_Choice)
        Alternate_Material = Alternate_Material[['Material','Score']]
        #Alternate_Material = pd.merge(Alternate_Material,df, on='Material').drop(columns = ['Description'])
        #Alternate_Material['Cluster'].loc[df['Cluster'] == 0.0] = 'Sustainable'
        #Alternate_Material['Cluster'].loc[df['Cluster'] == 1.0] = 'Unsustainable'

        st.write(Alternate_Material)

    else:
        st.write('Please Select a Raw Materail and click the button to get ALternative Raw Materail ')
