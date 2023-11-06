import streamlit as st
from streamlit_option_menu import option_menu
from log_reg import log_reg
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Luxury Watches",
    page_icon="⌚",
)

if 'data' not in st.session_state:
    data = pd.read_csv('watch_data.csv')
    st.session_state["data"] = data
else:
    data = st.session_state["data"]

if "user" not in st.session_state:
    log_reg()
else:
    selected = option_menu(None, ["Routine analysis", "Material analysis"], orientation="horizontal",
                           icons=["list-task", "list-task"], default_index=0)
    if selected == 'Routine analysis':
        st.text_area(
            "desc1",
            "In the bubble diagram below, the main contents analyzed are: \n   To explore variations in the price and "
            "quantity of different Complication watches, hover over each bubble to view the specific brand, "
            "quantity and specific dial type", disabled=True, label_visibility='hidden', key='desc1'
        )
        df = pd.concat([data[["Brand", "Complication", 'Price']].groupby(['Brand', 'Complication']).mean(),
                        data[["Brand", "Complication"]].value_counts()], axis=1).reset_index()
        df = pd.merge(df, data[["Brand", "Dial"]].groupby('Brand').count(), on='Brand')
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
        st.text_area(
            "desc2",
            "In the bar chart below, the main contents analyzed are: \n    Explore the top watches in the average "
            "price of different models", disabled=True, label_visibility='hidden', key='desc2'
        )
        N = st.slider('Select the top N to be displayed', 5, 30, 10)
        fig = px.bar(
            round(data[["Model", "Price"]].groupby('Model').mean().sort_values(by='Price')[-N:], 3).reset_index(),
            y="Model",
            x="Price",
            color="Price",
            orientation='h',
            text="Price"
        )

        st.plotly_chart(fig, use_container_width=True)
        if st.button("Log out", type="primary"):
            st.session_state.pop('user')
            st.experimental_rerun()
    elif selected == 'Material analysis':
        st.text_area(
            "desc3",
            "In the combined line chart below, the main contents analyzed are: \n    Explore the average price "
            "distribution of each specific material in the three types of materials used by different brands of "
            "watches", disabled=True, label_visibility='hidden', key='desc3'
        )
        brand = st.selectbox("Please select a watch brand", data["Brand"].unique())
        data = data[data["Brand"] == brand]
        df = pd.DataFrame()
        for col in ['Case material', 'Bracelet material', 'Lunette Material']:
            df = pd.concat([df, data[[col, "Price"]].groupby(col).mean()], axis=1)
        df.columns = ['Case material', 'Bracelet material', 'Lunette Material']
        fig = go.Figure()

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
        st.plotly_chart(fig, use_container_width=True)
        if st.button("Log out", type="primary"):
            st.session_state.pop('user')
            st.experimental_rerun()
