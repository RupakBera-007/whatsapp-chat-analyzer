import streamlit as st

st.sidebar.title("Whatsapp Chats Analyzer")

st.title("📊 WhatsApp Chat Analyzer")
st.write("Upload your chat file to start analysis")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
