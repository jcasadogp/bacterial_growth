import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Help", page_icon="📤", layout='wide')

add_logo("figs/logo_sidebar3.png", height=100)
with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.image('figs/HelpBanner.png')

st.markdown("![badge](https://img.shields.io/badge/status-under%20development-orange?style=for-the-badge)")

teo_info = st.expander("**All About Bacterial Growth Data**")
teo_info.write('hello')

data_info = st.expander("**Our Database**")
data_info.write('hello')

upload_info = st.expander("**How to Upload My Data?**")
upload_info.write('hello')

ex_info = st.expander("**Uploading Data: Applied Examples**")
ex_info.write('hello')

ques_info = st.expander("**Frequently Asked Questions**")
ques_info.write('hello')

more_info = st.expander("**Need More information?**")
more_info.write('hello')