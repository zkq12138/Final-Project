import streamlit as st


def log_reg():
    st.markdown('''<h2 style='color: blue;text-align: center;'>⌚Luxury Watches</h2>''', unsafe_allow_html=True)
    st.markdown('''
        <p>Explore the world of luxury timepieces with this comprehensive Luxury Watches Dataset. This collection offers a rich source of data on high-end wristwatches, featuring details on brands, models, materials, complications, and more. Whether you're a horology enthusiast, a data scientist, or a watch industry professional, this dataset provides valuable insights into the fascinating realm of luxury watchmaking.</p>
        <p>Dataset Highlights:</p>
        <p>Detailed information on luxury watch brands and models.<p>
        <p>Specifications including watch materials, references, and complications.</p>
        <p>A treasure trove for watch collectors, researchers, and enthusiasts.</p>
        <p>Unlock the secrets of haute horlogerie and embark on a data-driven journey through the world of luxury watches. Download my dataset today and start your horological exploration.</p>
        <p>Data source: <a>https://www.kaggle.com/datasets/yoerireumkens/timepiece-treasures-a-luxury-watches-dataset</a></p>
        ''', unsafe_allow_html=True)

    st.text_input(label="username", key="username", placeholder="Please enter your username")
    st.text_input(label="password", key="password", type='password', placeholder="Please enter the corresponding password")
    if st.button("Login", type="primary"):
        st.session_state["user"] = st.session_state["username"]
        st.experimental_rerun()
