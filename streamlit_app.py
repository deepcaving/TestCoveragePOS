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

st.text_input(
    "Please enter a Test number or a Screen number from Overflow",
    "",
    key="placeholder",
)

req = requests.Session()
url = 'https://us-central1-snappyvms.cloudfunctions.net/notion-tests-coverage?testNum=' + st.session_state.placeholder
x = requests.get(url)
st.markdown(x.text, unsafe_allow_html=False)
st.cache_resource.clear()








