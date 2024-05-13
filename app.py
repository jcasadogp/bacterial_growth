import streamlit as st
from streamlit_extras.app_logo import add_logo
from st_pages import show_pages_from_config
from streamlit_extras.badges import badge

# Preload CSS file
@st.cache_resource
def load_css():
    with open("style.css") as css:
        return css.read()

st.set_page_config(page_title="µGrowthDB", page_icon="🔍", layout='wide')

add_logo("figs/logo_sidebar3.png", height=100)


st.markdown(f'<style>{load_css()}</style>', unsafe_allow_html=True)



st.image('figs/logo.png')
st.write('')
st.write('')
st.write('')
st.write('')


st.markdown("![badge](https://img.shields.io/badge/status-under%20development-orange?style=for-the-badge)")


st.markdown(
    """
    **Welcome to µGrowthDB**

    This database aims to provide comprehensive information on the growth dynamics of bacterial species found in the human gut microbiome.
    Users can explore growth rates, bacterial communities, pH, metabolites, and other relevant factors influencing bacterial proliferation
    within the gut environment.

    Our main objective is to serve as a comprehensive resource for researchers interested in studying the growth dynamics of bacterial species within the human gut microbiome.
    By providing access to curated data and facilitating analysis and comparison of growth characteristics, we aim to contribute to advancements in gut microbiome research
    and our understanding of its implications for human health and disease.


    **Search Bacterial Growth Data:**

    Users can search for experimental data collected from bacterial growth studies. The search can be filtered by different experimental conditions and characteristicas like
    study name, bacterial strains, metabolites, culture media and pH.

    **Download Different Datasets:**

    All the data at µGrowthDB is available for everyone. To further analyze and compare different datasets we offer the feature of downloading several datasets at ones. Accessing to
    the raw data is usefull to further analize and visualize the growth data.

    **Upload Bacterial Growth Data:**

    At µGrowthDB, we recognize the invaluable contributions of researchers in advancing our understanding of gut microbiome dynamics. To share bacterial growth data publicly
    plays a crucial role in increasing scientific progress and collaboration within the research community. We allow reasearcher to upload their experimental growth data by following a series of
    steps that allow us to keep an adquate quality control over the data.

    **Visualize Bacterial Growth Curves:**

    Users can visualize all the different bacterial growth experiments in the database, this means plotting accurate growth curves accross different conditions. Another key feature is the possibility
    to compare the growth curves between different studies at once.




    """)
st.write('')
st.write('')

show_pages_from_config()
