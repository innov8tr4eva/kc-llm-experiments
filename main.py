import streamlit as st

## Rendering the frontend

st.set_page_config(page_title="Examples with data analytics at Roblox", layout="wide")

# Add Title
st.header("Examples with data analytics at Roblox", divider="rainbow")

st.write(
    "This app is to demonstrate different examples of doing data analytics with Python & LLMs at Roblox. "
)

st.write("Choose an example from the sidebar.")
st.divider()
st.write("1. The first example is to explore Roblox employee data using pygwalker.")
st.write("2. The second example is to use pandasai to chat with Roblox employee data.")
