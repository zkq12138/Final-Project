import streamlit as st
import pandas as pd


def log_reg():
    users = pd.read_table('users.txt', sep=' ', header=None)#: Reading a text file named "users.txt" and storing the data in a Pandas DataFrame called `users`. The file contains usernames and corresponding passwords separated by spaces.
    st.markdown('''<h2 style='color: blue;text-align: center;'>⌚Luxury Watches</h2>''', unsafe_allow_html=True)# Using the `st.markdown` function to display a heading for the web application.
    st.markdown('''
        <p>Explore the world of luxury timepieces with this comprehensive Luxury Watches Dataset. This collection offers a rich source of data on high-end wristwatches, featuring details on brands, models, materials, complications, and more. Whether you're a horology enthusiast, a data scientist, or a watch industry professional, this dataset provides valuable insights into the fascinating realm of luxury watchmaking.</p>
        <p>Dataset Highlights:</p>
        <p>Detailed information on luxury watch brands and models.<p>
        <p>Specifications including watch materials, references, and complications.</p>
        <p>A treasure trove for watch collectors, researchers, and enthusiasts.</p>
        <p>Unlock the secrets of haute horlogerie and embark on a data-driven journey through the world of luxury watches. Download my dataset today and start your horological exploration.</p>
        <p>Data source: <a>https://www.kaggle.com/datasets/yoerireumkens/timepiece-treasures-a-luxury-watches-dataset</a></p>
        ''', unsafe_allow_html=True)
#Using the `st.markdown` function to display a formatted text with information about the dataset
   #Displays a text input box for users to enter their username. The `label` parameter sets the label text, the `key` parameter assigns a unique key to the input box,
    #and the `placeholder` parameter sets the placeholder text.
    st.text_input(label="username", key="username", placeholder="Please enter your username")
    #Displays a text input box for users to enter their password. The `label` parameter sets the label text,
    #the `key` parameter assigns a unique key to the input box, the `type` parameter sets the input type to password (hides the entered text), and the `placeholder` parameter sets the placeholder text.
    st.text_input(label="password", key="password", type='password', placeholder="Please enter the corresponding password")
    #Checks if the "Login" button is clicked.
    if st.button("Login", type="primary"):
        #Checks if the entered username is not in the list of usernames from the `users` DataFrame. If true, displays an error message.
        if st.session_state["username"] not in users[0].tolist():
            st.error('No such user')
            st.stop()
        #Checks if the entered username is in the list of usernames from the `users` DataFrame and if the entered password matches the corresponding password in the DataFrame. 
        #If true, sets the session state variable "user" to the entered username.
        elif st.session_state["username"] in users[0].tolist() and st.session_state["password"] == users.set_index(0).loc[st.session_state["username"]][1]:
            st.session_state["user"] = st.session_state["username"]
            st.experimental_rerun()
        # Displays an error message if the entered username and password are incorrect.
        else:
            st.error('Login parameters are incorrect, please try again')
            st.stop()
#Author:Shengbin Liang and Xiuqi Liang
