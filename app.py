import streamlit as st
from streamlit_option_menu import option_menu
from log_reg import log_reg
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##Set the page configuration of the' streamlint 'application, including page titles and icons.
st.set_page_config(
    page_title="Luxury Watches",
    page_icon="⌚",
)
## Check if the data exists in the session state.
##Read data from a CSV file
if 'data' not in st.session_state:
    data = pd.read_csv('watch_data.csv')
    st.session_state["data"] = data
else:
    data = st.session_state["data"]
##Check if user information exists in the session state.
##Author: Tianxiang Liu
if "user" not in st.session_state:
    log_reg()
else:##If there is user information, a different option menu will be displayed.
    selected = option_menu(None, ["Routine analysis", "Material analysis"], orientation="horizontal",
                           icons=["list-task", "list-task"], default_index=0)
    if selected == 'Routine analysis':## If the user selects the' Routine analysis' option, routine analysis will be performed.
      ##Create a text area in the application to display the analysis description.
        st.text_area(
            "desc1",
            "In the bubble diagram below, the main contents analyzed are: \n   To explore variations in the price and "
            "quantity of different Complication watches, hover over each bubble to view the specific brand, "
            "quantity and specific dial type", disabled=True, label_visibility='hidden', key='desc1'
        )
       ##Grouping data based on brand and complexity, and calculating average prices and quantities.
        df = pd.concat([data[["Brand", "Complication", 'Price']].groupby(['Brand', 'Complication']).mean(),
                        data[["Brand", "Complication"]].value_counts()], axis=1).reset_index()
        df = pd.merge(df, data[["Brand", "Dial"]].groupby('Brand').count(), on='Brand')
        ## Create a bubble chart to display the relationship between different brands, complexity, and prices.
        fig = px.scatter(
            df,
            x="count",
            y="Price",
            size="Dial",
            color="Complication",
            hover_name="Brand",
            log_x=True,
            size_max=50,
        )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
 #Author: Hongcheng Fu
        st.text_area(
            "desc2",
            "In the bar chart below, the main contents analyzed are: \n    Explore the top watches in the average "
            "price of different models", disabled=True, label_visibility='hidden', key='desc2'
        )
        N = st.slider('Select the top N to be displayed', 5, 30, 10)##Create a slider to select and display the top N top watches.
       ##Create a bar chart to display the average price of different watch models.
        fig = px.bar(
            round(data[["Model", "Price"]].groupby('Model').mean().sort_values(by='Price')[-N:], 3).reset_index(),
            y="Model",
            x="Price",
            color="Price",
            orientation='h',
            text="Price"
        )

        st.plotly_chart(fig, use_container_width=True)
        ## If the "Log out" button is clicked, the user information in the session state is cleared and the application is rerun
        if st.button("Log out", type="primary"):
            st.session_state.pop('user')
            st.experimental_rerun()
  #Author: Yangjun Gai         
    elif selected == 'Material analysis':##If the user selects the' Material analysis' option, material analysis will be performed. 
        st.text_area(
            "desc3",
            "In the combined line chart below, the main contents analyzed are: \n    Explore the average price "
            "distribution of each specific material in the three types of materials used by different brands of "
            "watches", disabled=True, label_visibility='hidden', key='desc3'
        )
        brand = st.selectbox("Please select a watch brand", data["Brand"].unique())##Create a drop-down box to select a specific watch brand.
        data = data[data["Brand"] == brand]
        df = pd.DataFrame()
        for col in ['Case material', 'Bracelet material', 'Lunette Material']:
            df = pd.concat([df, data[[col, "Price"]].groupby(col).mean()], axis=1)##Traverse through three different material types.
        df.columns = ['Case material', 'Bracelet material', 'Lunette Material']
        fig = go.Figure()
##Add three line chart trajectory to display the average price distribution of different material types.
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df["Case material"],
            mode='lines',
            name='Case material'))

        fig.add_trace(go.Scatter(
            x=df.index,
            y=df["Bracelet material"],
            mode='lines',
            name='Bracelet material'))

        fig.add_trace(go.Scatter(
            x=df.index,
            y=df["Lunette Material"],
            mode='lines+markers',
            name='Lunette Material'))
        st.plotly_chart(fig, use_container_width=True)##Draws a line chart in the application.
        ## If the "Log out" button is clicked, the user information in the session state is cleared and the application is rerun.
    #Author: Kaiqi Zhou
        if st.button("Log out", type="primary"):
            st.session_state.pop('user')
            st.experimental_rerun()
