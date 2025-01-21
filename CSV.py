import streamlit as st

def main():
    st.set_page_config(page_title="Ask your CSV 📈")
    st.header("Ask your CSV 📈")

    user_csv = st.file_uploader("Upload your CSV file", type="csv")



    if __name__ == "__main__":
        main()