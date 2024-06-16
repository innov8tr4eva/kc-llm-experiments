import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.responses.streamlit_response import StreamlitResponse
import os
from dotenv import load_dotenv
from queries.employee_queries import queryEmpDataFromROS, queryMinEmpDataFromROS
from queries.employee_queries import get_emp_graphql_data

load_dotenv()

url = os.environ.get("ROS_API_URL")
query = queryMinEmpDataFromROS()
token = os.environ.get("ROS_API_TOKEN")

result = get_emp_graphql_data(url, query, token)
result_df = pd.DataFrame(result)


st.header("Natural queries with employee data", divider="rainbow")

gateway_base_url = "http://apis.sitetest3.simulpong.com/ml-gateway-service/v1/"


llm = OpenAI(
    api_token=st.secrets["OPENAI_API_KEY"],
    model="gpt-4o",
    # api_token=st.secrets["ROS_ML_GATEWAY_KEY"],
    # base_url=gateway_base_url,
    temperature=0,
    seed=26,
)


# creating a SmartDataframe object
smart_result_df = SmartDataframe(result_df, config={"llm": llm})

# displaying the results dataframe
st.dataframe(result_df)

# intialize the chatbot
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on the app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What would you like to know about employee data?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(
        {"role": "user", "content": prompt, "verbose": True}
    )
    # assistant response
    with st.chat_message("assistant"):
        response = smart_result_df.chat(prompt)
        if "png" in str(response):
            st.image(response)
        else:
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
