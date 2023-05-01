import streamlit as st 
import pandas as pd
# Slidebar
st.sidebar.markdown("Creado por Fidel Castillo")

#Main contenido
st.title("Mi primera app Streamlit")

df=pd.read_csv("db_Placement.csv")

st.write(df.degree_p)
st.bar_chart(df.degree_p.head(10))
