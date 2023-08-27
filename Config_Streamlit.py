import os
import base64
import streamlit as st
from PIL import Image

logo_path="logo.png"
favicon_image = Image.open("favicon.png")

hide_streamlit_style = """
                <style>
                [data-testid="stSidebar"][aria-expanded="true"]{
                min-width: 250px;
                max-width: 250px;
                }
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

def streamlit_markdown():
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def streamit_page_config():
    st.set_page_config(
        page_title="ChatBot",
        page_icon=favicon_image,
        layout="wide",
        initial_sidebar_state="expanded"
    )

def insert_logo():
    if os.path.isfile(logo_path):
        with open(logo_path, "rb") as img_file:
            logo_base64 = base64.b64encode(img_file.read()).decode('utf-8')
        st.sidebar.markdown(
            f'<img src="data:image/png;base64,{logo_base64}" style="max-width:200px;">', 
            unsafe_allow_html=True,
        )
    else:
        st.sidebar.text("Logo not found!")