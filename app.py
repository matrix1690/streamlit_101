import streamlit as st
import pandas as pd
import duckdb

df = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': [10, 20, 30, 40],
})

st.write("Hello World Gaye!!!")

sql_query = st.text_area('Veuillez saisir la requête')

if sql_query != "":
    result = duckdb.query(str(sql_query)).df()
else:
    result = pd.DataFrame({})




st.write(result)


