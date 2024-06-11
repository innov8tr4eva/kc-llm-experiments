# kc-pygwalker-demo

Demo repo for the capabilities of pygwalker

1.  Install the following packages

```
pip install pygwalker streamlit
```

2. Copy .env.local to .env and set your ROS API key there

3. Run the following command

```
streamlit run app.py
```

4. A new window should open up with a pygwalker interface for exploring employee data

![pygwalker visualize](pyg-visualize.png)

5. You can use the data tab to get an overview of all fields in the results

![pygwalker data](pyg-data.png)

6. You can also chat with your data in the chat tab after you setup an account in Kanaries

![pygwalker chat](pyg-chat.png)
