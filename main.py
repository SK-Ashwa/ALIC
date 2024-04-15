import streamlit as st

# Read the content of the index.html file
with open("D:\\VS Code - 2\\ALIC\\index.html", "r") as file:
    html_content = file.read()

# Display the content using components.iframe
st.components.v1.html(html_content, height=600)
