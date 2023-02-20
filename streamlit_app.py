from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import requests

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

placeholderTxt = "Type the number here"
st.subheader("Please enter a :blue[Test number] or a :blue[Screen number] from Overflow")
st.text_input(
    "",
    placeholderTxt,
    key="placeholder",
)

req = requests.Session()
if (st.session_state.placeholder == ""):
    st.markdown("", unsafe_allow_html=False) 
if (st.session_state.placeholder == placeholderTxt):
    st.markdown("", unsafe_allow_html=False) 
else:
    url = 'https://us-central1-snappyvms.cloudfunctions.net/notion-tests-coverage?testNum=' + st.session_state.placeholder
    x = requests.get(url)
    st.markdown(x.text, unsafe_allow_html=False)











