import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def cluster():
    data = pd.read_excel("Data/dataset_rawmaterials_consumption_Algo_input.xlsx")

    data1 = data.dropna()
    numer = data1[["WaterConsumption","EnergyConsumption","co2e","GHGemissions",
             ]]

    scaler = StandardScaler()
    numer = pd.DataFrame(scaler.fit_transform(numer))
    numer.columns = ["WaterConsumption_Scaled","EnergyConsumption_scaled",
                     "co2e_scaled","GHGemissions_scaled"]


    km = KMeans(n_clusters=2, random_state=123, n_init=30)
    km.fit(numer)

    clusters = km.predict(numer)
    numer["Cluster"] = clusters

    data1 = pd.concat([numer,data], axis='columns')

    data2 = pd.DataFrame(data1['Cluster'], data1['Raw Material'])
    data2.reset_index(inplace=True)

    data3 = pd.DataFrame(data1['Cluster'])
    data4 = pd.concat([data3,data1["Raw Material"]], axis='columns')
    
    return data4
