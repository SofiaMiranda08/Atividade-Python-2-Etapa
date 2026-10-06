import streamlit as st
import pandas as pd

nome = "Sofia"
idade = 18

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})

st.title("Meu primeiro dash")
st.subheader(nome)
st.write("Olá, mundo")
st.write(f"Meu nome é {nome} e tenho {idade} anos.")
st.write(df)
