import streamlit as st
from pg_predict import show_pg_predict
from pg_explore import show_pg_explore

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_pg_predict()
else:
    show_pg_explore()
