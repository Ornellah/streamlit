### Import
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Cach data @st.cache_data

@st.cache_data
def load_data():
    df = pd.read_csv('data.csv').dropna()
    return df

### Config
st.set_page_config(
    page_title="Dashboard Marketing",
    page_icon="🚀",
    layout="wide"
)

df = load_data()

def page_1():
    ### Title et markdown : st.title et st.markdown

    st.title("Votre Dashboard intéractif avec Streamlit 🎨")
    st.markdown("""
        Bienvenue sur votre Dashboard interactif !

        ### Comment utiliser `Streamlit`      
        """)


    ### Checkbox st.checkbox
    if st.checkbox("Découvrir les données brutes")==True:
        st.write(df)


    ### Selectbox st.selectbox

    # st.selectbox("Choisissez une ville", ["Paris","Lyon","Marseille"])


    ### Forms st.form, st.form_submit_button et st.select_slider

    # with st.form(key="my_form"):
    #     age = st.select_slider("Quel est votre âge ?",options=range(18,81,1))
    #     submit = st.form_submit_button(label="Soumettre")
        
    #     if submit==True:
    #         st.write(f"Merci pour votre réponse ! Vous avez {age} ans.") 


    ### Columns st.columns
    col1, col2 = st.columns(2)

    with col1:
        # st.write('colonne 1')
        ville = st.selectbox("Choisissez une ville", ["Paris","Lyon","Marseille"])
        st.write(f"Vous avez choisi la ville de {ville}.")
        
    with col2:
        # st.write('colonne 2')
        with st.form(key="my_form"):
            age = st.select_slider("Quel est votre âge ?",options=range(18,81,1))
            submit = st.form_submit_button(label="Soumettre")
            
            if submit==True:
                st.write(f"Merci pour votre réponse ! Vous avez {age} ans.") 


    ### Graphique Histogramme avec matplotlib.pyplot, seaborn et st.pyplot
    fig = plt.figure()
    sns.violinplot(x="Profession",y="Age",data=df)
    st.pyplot(fig)

    ### Image avec st.image
    img = plt.imread("img.jpg")
    st.image(img,width=300)

    ### Graphique Histogramme px.histogram et st.plotly_chart
    genre = st.radio("Choisissez un genre", df.Gender.unique())
    st.write(f"Vous avez choisi le genre {genre}.")
    fig = px.histogram(df[df.Gender==genre].Age)
    st.plotly_chart(fig)


    ### Graphique Pie chart px.pie et st.plotly_chart
    gender = df.Gender.value_counts()
    fig = px.pie(values=gender.values, names=gender.index, title="Répartition des genres")
    st.plotly_chart(fig)

    ### + De graphiques ici : https://plotly.com/python/

def page_2():
    st.title("Page 2")
    st.write("Bienvenue sur la page")

