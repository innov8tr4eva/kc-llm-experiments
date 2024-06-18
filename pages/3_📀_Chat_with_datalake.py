import openai
import streamlit as st
import pandas as pd

openai.api_key = st.secrets["OPENAI_API_KEY"]
from llama_index.agent.openai import OpenAIAgent
from llama_index.tools.database import DatabaseToolSpec


db_spec = DatabaseToolSpec(
    scheme=st.secrets["DB_SCHEME"],
    host=st.secrets["DB_HOST"],
    port=st.secrets["DB_PORT"],
    user=st.secrets["DB_USER"],
    password=st.secrets["DB_PASSWORD"],
    dbname=st.secrets["DB_NAME"],
)

tools = db_spec.to_tool_list()

for tool in tools:
    st.write(tool.metadata.name)
    st.write(tool.metadata.description)
    st.write(tool.metadata.fn_schema)

st.header("Natural queries with datalake", divider="rainbow")

st.header("this is not working yet")

gateway_base_url = "http://apis.sitetest3.simulpong.com/ml-gateway-service/v1/"

agent = OpenAIAgent.from_tools(
    tools,
    # api_token=st.secrets["ROS_ML_GATEWAY_KEY"],
    # base_url=gateway_base_url,
    verbose=True,
)


# llm = OpenAI(
#     api_token=st.secrets["OPENAI_API_KEY"],
#     model="gpt-4o",
#     # api_token=st.secrets["ROS_ML_GATEWAY_KEY"],
#     # base_url=gateway_base_url,
#     temperature=0,
#     seed=26,
# )


# intialize the chatbot
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on the app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Explore the datalake"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(
        {"role": "user", "content": prompt, "verbose": True}
    )
    # assistant response
    with st.chat_message("assistant"):
        response = agent.chat(prompt)
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
