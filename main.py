import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_toggle as tog
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go
st.set_page_config(page_title="NEXANS CABLE")
import random

session_state = st.session_state
# session_state.cache = True




st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">',
    unsafe_allow_html=True,
)
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
st.markdown("""""", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
    
                header{visibility:hidden;}
                .main {
                    margin-top: -120px;
                    padding-top:10px;
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}

            </style>
            
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: orange">
    <a class="navbar-brand" href="#"  target="_blank"> <b>Trestle Python Track</b></a>  
    </nav>
""",
    unsafe_allow_html=True,
)

st.text(" \n ")
st.text(" \n ")
st.text(" \n ")
st.text(" \n ")
st.text(" \n ")
st.text(" \n ")    
with st.form(key="Form"):
    st.header("Guess Game")
    col1,col2 = st.columns(2)
    
    with col1:

        
        extent = st.slider("Select Range",0,10)
    with col2:

        generator  = random.randint(0,extent)
        input = st.text_input("Enter the Random Number")
    button = st.form_submit_button("Click")
    if button:
        
        if int(input)==generator:
            st.write("Guess was correct",generator)
            st.balloons()
        else:
            st.write("Guess was incorrect, guess number was",generator)
    
    

