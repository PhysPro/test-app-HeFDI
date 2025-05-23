import streamlit as st
# !pip install mag4
import mag4 as mg
import pandas as pd

elements = ['Si', 'Mg', 'Mn']

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

mg.available_datasets()[['Source', 'Short Title', 'Title']]

#pd.available_dataframes()
col1, col2 = st.columns(2)

with col1:
    st.header("Data")
    st.write("Select data")
    st.selectbox("x axis", elements)

    with col2:
        st.header("Plot")
        st.write("Graph")