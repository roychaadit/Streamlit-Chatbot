import streamlit as st
from streamlit_chat import message
from Config_Streamlit import *
from Helper_Module import *




if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]



streamit_page_config()

streamlit_markdown()

insert_logo()


st.sidebar.title("AI Assistant")
uploaded_files = st.sidebar.file_uploader("Choose a PDF or Text file", type=['pdf', 'txt'], accept_multiple_files=True)


upload_documents_button = st.sidebar.button("Upload Documents", key="upload_documents")
train_model_button = st.sidebar.button("Train Model", key="train_model")
reset_model_button = st.sidebar.button("Reset Model", key="reset_model")
clear_conversation_button = st.sidebar.button("Clear Conversation", key="clear_conversation")



if upload_documents_button:
    st.text("Uploading documents...")
    upload_documents(uploaded_files)
    st.text("Documents uploaded successfully!")

if clear_conversation_button:
    st.text("Clearing conversation...")
    clear_conversation()
    st.text("Conversation cleared successfully!")

if reset_model_button:
    st.text("Resetting model...")
    reset_model()
    st.text("Model reset successfully!")

if train_model_button:
    st.text("Training model...")
    train_model()
    st.text("Model trained successfully!")
    

response_container = st.container()
container = st.container()


with container:
    with st.form(key='my_form', clear_on_submit=True):
        query = st.text_area("User:", key='input', height=50)
        submit_button = st.form_submit_button(label='Send')
        
    if query and submit_button:
        print("\n\n")
        print("#" * 100)
        st.session_state['messages'].append({"role": "user", "content": query})
        chat_history = st.session_state['chat_history']
        print(chat_history)
        question, answer, chat_response = get_response(query, chat_history)
        st.session_state['chat_history'].append((question, answer))
        st.session_state['messages'].append({"role": "assistant", "content": chat_response})
        st.session_state['past'].append(question)
        st.session_state['generated'].append(chat_response)
        print("*" * 100)


if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="identicon", seed="Casper")
            message(st.session_state["generated"][i], key=str(i), avatar_style="identicon", seed="Rocky")


