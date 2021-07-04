import streamlit as st
import pandas as pd
import altair as alt

st.title('Mi primera app con streamlit')
st.subheader('Tabla de datos básica')

url="https://raw.githubusercontent.com/KaonToPion/datasets/main/brain.csv"
brain=pd.read_csv(url)

#Mostrar una tabla
st.table(brain.head())


hist_brain = alt.Chart(brain).mark_bar().encode(
    x=alt.X('Brain Weight',bin=alt.Bin(maxbins=100)),
    y="count()"
).properties(
    width=300,
    height=150,
    title="Relación peso del cerebro y del cuerpo"
).interactive()

hist_body = alt.Chart(brain).mark_bar().encode(
    x=alt.X('Body Weight',bin=alt.Bin(maxbins=100)),
    y="count()"
).properties(
    width=300,
    height=150,
    title="Relación peso del cerebro y del cuerpo"
).interactive()

scatter_brain_body = alt.Chart(brain).mark_circle().encode(
    x='Body Weight',
    y='Brain Weight'
).properties(
    width=700,
    height=300,
    title="Relación peso del cerebro y del cuerpo"
).interactive()

comp_brain = (hist_brain|hist_body)&scatter_brain_body
comp_brain
