# Pour le lancer : streamlit run bienici.py
import pandas as pd
import pymongo
import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import json
from math import pi


# Recup BDD $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0')
sinfun = client.BIEN_ICI.Appartement
sinfun.find_one()

cursor = sinfun.find()
entries = list(cursor)
entries[:5]

Maison = pd.DataFrame(entries)

#print(type(Maison["Prix du m2"][5]))




# streamlit $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
st.set_option('deprecation.showPyplotGlobalUse', False) # enlever les warning sur st

# BARPLOT **********************************************************************************************************************************************************************************
codePostal = []
contient = False
#print(type(codePostal))

for i in range(len(Maison["Code Postal"])):
    codePostal.append(Maison["Code Postal"][i])

codePostal = list(set(codePostal))
#print(codePostal)

moyenne = [0 for i in range(len(codePostal))]
cpt = [0 for i in range(len(codePostal))]

for i in range(len(Maison["Code Postal"])):
    for j in range(len(codePostal)):
        if Maison["Code Postal"][i] == codePostal[j]:
            moyenne[j] += int(Maison["Prix du m2"][i])
            cpt[j] += 1

for i in range(len(moyenne)):
    moyenne[i] /= cpt[i]

#print(moyenne)
#autre = [0 for i in range(len(codePostal))]
bar = pd.DataFrame({ "Moyenne": moyenne, "cpt":cpt,"code": codePostal})


y_pos = np.arange(len(bar["code"]))
plt.bar(y_pos, bar["Moyenne"])
plt.xticks(y_pos, bar["code"], rotation=90)
plt.title("Moyenne Prix au m2 par ville")
#plt.subplots_adjust(bottom=0.4, top=0.99)
#plt.show()
#fig = plt.subplot()
#st.pyplot(fig)
st.pyplot()

# BOUGIES *******************************************************************************************************************************************

code = [int(Maison["Code Postal"][i]) for i in range(len(Maison["Code Postal"]))]
prix = [int(Maison["Prix (€)"][i]) for i in range(len(Maison["Prix (€)"]))]
df = pd.DataFrame({"Code Postal" : code, "Prix (€)": prix})
# boxplot
ax = sns.boxplot(x="Code Postal", y="Prix (€)", data=df)
# add stripplot
ax = sns.stripplot(x="Code Postal", y="Prix (€)", data=df, color="orange", jitter=0.2, size=4.5)
plt.xticks(rotation=90)
# add title
plt.title("Moyenne des prix en euros par ville")
# show the graph
plt.show()
st.pyplot()

# BASIC RADAR CHART *******************************************************************************************************************************
def nbrAppartVille(codePostal):
    tab = [0 for i in range(6)]
    for i in range(len(Maison["Nbr de Pieces"])):
        if Maison["Code Postal"][i] == codePostal:
            tab[int(Maison["Nbr de Pieces"][i])] += 1

    for i in range(len(tab)):
        print(tab[i])

    rad = pd.DataFrame({
        "valeurs": ["1", "2", "3", "4" , "5", "6"],
        "1": tab[0],
        "2": tab[1],
        "3": tab[2],
        "4": tab[3],
        "5": tab[4],
        "6": tab[5]
    })

    # number of variable
    categories=list(rad)[1:]
    N = len(categories)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=rad.loc[0].drop('valeurs').values.flatten().tolist()
    values += values[:1]
    values

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories, color='grey', size=5)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10,20], ["10","20"], color="grey", size=5)
    plt.ylim(0,30)

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.title("Nbr Pieces Apparts "+ codePostal, size=11, y=1.1)


    # Show the graph
    plt.show()
    st.pyplot()

nbrAppartVille('92250')
nbrAppartVille('92000')
#nbrAppartVille('92800')


# BASIC RADAR CHART 2 *****************************************************************************************************************************************
title = ["Code Postal","Prix (€)","Surface (m2)","Prix du m2","Nbr de Pieces"]
radar = pd.DataFrame({
    "titre" : title,
    "Prix": [248,228,269,199,202.464],
    "Prix m2": [31.39,63.18,62.31,57.58,69.22],
    "Nbr de Piece": [4,2,2,2,1],
    "surface": [79,34,43,33,29]
    
})


# number of variable
categories=list(radar)[1:]
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=radar.loc[0].drop('titre').values.flatten().tolist()
values += values[:1]
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories, color='grey', size=5)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([50,100,150,200,250], ["50","100", "150", "200", "250"], color="grey", size=5)
plt.ylim(0,250)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# Fill area
ax.fill(angles, values, 'b', alpha=0.1)


# Show the graph
plt.show()
st.pyplot()
st.text("Prix (en centaine de milliers d'euros)")
st.text("Prix m2 (en centaine d'euros)")
st.text("surface (en m2)")
st.text("Nombre de pieces")

# BASIC RADAR CHART 3 ********************************************************************************************************************************
# ------- PART 1: Define a function that do a plot for one line of the dataset!
 
def make_spider( row, title, color):

    # number of variable
    categories=list(radar)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(2,2,row+1, polar=True, )

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 6.5)
    ax.set_theta_direction(-1)


    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=5)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([50,100,150,200,250], ["50","100", "150", "200", "250"], color="grey", size=5)
    plt.ylim(0,275)

    # Ind1
    values=radar.loc[row].drop("titre").values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)

    # Add a title
    plt.title(title, size=11, color=color, y=1.1)

# ------- PART 2: Apply the function to all individuals
# initialize the figure
my_dpi=96
plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)

# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(radar.index))

# Loop to plot
for row in range(0, len(radar.index)-1):
    make_spider(row=row, title='Appartement '+ str(row+1), color=my_palette(row))

plt.show()
st.pyplot()

st.text("Prix (en centaine de milliers d'euros)")
st.text("Prix m2 (en centaine d'euros)")
st.text("surface (en m2)")
st.text("Nombre de pieces")



# Test Plot (JSP lequel) *******************************************************************************************************************************************************
#sns.regplot(x=Maison["Nbr de Pieces"], y=Maison["Surface (m2)"])
#st.pyplot()
# plt.plot( 'Surface (m2)', 'Nbr de Pieces', "", data=Maison, linestyle='', marker='o')
# plt.xlabel('Value of X')
# plt.ylabel('Value of Y')
# plt.xticks(rotation=90)
# plt.title('Overplotting looks like that:', loc='left')
# plt.show()
# st.pyplot()

# Test De carte des Hauts-de-Seine ***************************************************************************************************************************************************************
# Carte des Haut-de-Seine : (prix du mettre carrée ne moy par ville)

# with open('/Users/yann/Documents/cours_Ynov/Ydays/Data/bien_ici/HDS.json', 'r') as f:
#     HautDeSeineJson = json.load(f)
# #print(type(HautDeSeineJson["features"]))

# for i in range(len(HautDeSeineJson["features"])):
#     HautDeSeineJson["features"][i]["id"]= HautDeSeineJson["features"][i]["properties"]["code"]

# print(HautDeSeineJson)

# #Build the choropleth
# fig = px.choropleth(df, 
#     geojson=HautDeSeineJson, 
#     locations='code',
#     color='Moyenne',
#     color_continuous_scale="Viridis",
#     range_color=(0, 100),
#     #scope="france",
#     labels={'Moyenne':'Moyenne'}
# )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# # Improve the legend
# fig.update_layout(coloraxis_colorbar=dict(
#     thicknessmode="pixels", thickness=20,
#     lenmode="pixels", len=200,
#     yanchor="top", y=0.8,
#     ticks="outside",
#     dtick=5
# ))

# fig.show()


