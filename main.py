import streamlit as st
import pandas as pd
import requests

def extract(message):
    endpoint = 'http://157.10.195.156:8815/search/v2/es/extract'
    message = message.replace('_','')
    resp = requests.get(endpoint, params={'input_text': message})
    return pd.DataFrame(resp.json())

st.set_page_config(
    page_title="AI-based Extractor Interface",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

header = st.empty()
input_text = st.empty()
output_df = st.empty()

with header.container(border=True):
    col1, col2 = st.columns([0.2, 0.7])
    with col1:
        st.image('graphics/ai.png', use_column_width=True)
    with col2:
        st.markdown('##### AI-based Message Extractor')
        st.markdown("*version 1.0.0*")
        st.markdown('*release on Oct 27, 2024*')

with input_text.container(border=True):
    message = st.text_area(label='**Input message**',
                           height=20)
    col1, col2 = st.columns([0.9,0.15])
    with col2:
        button = st.button(label='Extract')

if button:
    if message == '':
        with output_df:
            st.error('Please fill the message!')
    else:
        with st.spinner(text="Processing..."):
            data = extract(message)
        with output_df.container(border=True):
            st.markdown(f'**{data.shape[0]}** *items extracted*')
            st.dataframe(data, use_container_width=True)
