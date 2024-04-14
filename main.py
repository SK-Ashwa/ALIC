import streamlit as st

def run_html_file(html_file_path):
    with open(html_file_path, "r") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=1000, scrolling=True)

def main():
    st.title("Display HTML File in Streamlit")

    html_file_path = "D:\VS Code - 2\ALIC\index.html"  # Update this with the path to your HTML file

    run_html_file(html_file_path)

if __name__ == "__main__":
    main()

