import streamlit as st
from openai import OpenAI

st.header("Natural queries with employee data", divider="rainbow")

gateway_base_url = "http://apis.sitetest3.simulpong.com/ml-gateway-service/v1/"
client = OpenAI(api_key=st.secrets["ROS_ML_GATEWAY_KEY"], base_url=gateway_base_url)

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
# set default model
if "openai_model" not in st.session_state:
    st.session_state.openai_model = "openai/gpt-4-turbo"

# intialize the chatbot
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on the app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you today?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    # assistant response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state.openai_model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        # print(stream)
        response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
