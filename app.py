import requests
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer
import streamlit as st
import os
from queries.employee_queries import getEmpDataFromROS


def get_graphql_data(url, query, token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    data = {
        "query": query,
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    return response.json()["data"]["employees"]["nodes"]


url = "https://api.ros.rbx.com/graphql"
query = getEmpDataFromROS()
token = os.environ.get("ROS_API_TOKEN")


result = get_graphql_data(url, query, token)
result_df = pd.DataFrame(result)

## Rendering the frontend

st.set_page_config(page_title="Explore Roblox Employee Data", layout="wide")

# Add Title
st.title("Explore Roblox Employee Data")


# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":

    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(result_df, spec="./gw_config.json", spec_io_mode="rw")


renderer = get_pyg_renderer()

renderer.explorer()
