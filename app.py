import streamlit as st
import pandas as pd
import duckdb

df = pd.DataFrame(
    {
        "a": [1, 2, 3, 4],
        "b": [10, 20, 30, 40],
    }
)

with st.sidebar:
    st.write("Hello World Gaye!!!")

    option = st.selectbox(
        "Selectionnez une formation à suivre",
        ["Joins", "group By", "Windows Functions"],
        index=None,
        placeholder="Choisir une formation...",
        # accept_new_options=True,
    )

st.write("Vous avez choissi : ", option)
sql_query = st.text_area("Veuillez saisir la requête")

if sql_query != "":
    result = duckdb.query(str(sql_query)).df()
else:
    result = pd.DataFrame({})


st.write(result)
