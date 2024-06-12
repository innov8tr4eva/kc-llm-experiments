# kc-pygwalker-demo

Demo repo for the capabilities of pygwalker

1.  Install the following packages

```
pip install pygwalker streamlit
```

2. Copy .env.local to .env and set your ROS API key there

3. Run the following command

```
streamlit run main.py
```

4. Streamlit will launch an app.

5. Clicking on pygwalker demo on the sidebar should open up with a pygwalker interface for exploring employee data

![pygwalker visualize](pyg-visualize.png)

6. You can use the data tab to get an overview of all fields in the results

![pygwalker data](pyg-data.png)

7. You can also chat with your data in the chat tab after you setup an account in Kanaries

![pygwalker chat](pyg-chat.png)
