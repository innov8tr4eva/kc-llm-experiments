import requests
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
from queries.employee_queries import queryEmpDataFromROS
from queries.employee_queries import get_emp_graphql_data


url = os.environ.get("ROS_API_URL")
query = queryEmpDataFromROS()
token = os.environ.get("ROS_API_TOKEN")

result = get_emp_graphql_data(url, query, token)
result_df = pd.DataFrame(result)

## Rendering the frontend

st.set_page_config(page_title="Explore Roblox Employee Data", layout="wide")

# Add header
st.header("Explore Roblox Employee Data", divider="rainbow")


# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":

    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(result_df, spec="./gw_config.json", spec_io_mode="rw")


renderer = get_pyg_renderer()

renderer.explorer()


# @st.cache_data
# def render_dataframe(dataframe):
#     return st.dataframe(dataframe)


# render_dataframe(result_df)
