import streamlit as st
import streamlit.components.v1 as components
from multiapp import MultiApp
from apps import about, data, Target_Feature, Thermal_Images, model_metrics, Prediction# import your app modules here
from PIL import Image

##################################################################################################################################################################################################################################################################################################################
img = Image.open('ASU-logo.png')
st.set_page_config(page_title = 'AI For AM', layout="wide", page_icon=img, initial_sidebar_state='expanded')#  layout="wide", 
### Changing the name to our desired name and with the image.


### For byte encoder
import base64
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Helper function to set a background image of our choice
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#fed8b1,#808080);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)
logo = Image.open('ASU-logo.png')
st.sidebar.image(logo, use_column_width=True)

app = MultiApp()
st.markdown("""
# Thermal-Porosity
""")


# Add all your application here
app.add_app("About", about.app)
app.add_app("Data", data.app)
app.add_app("Target Feature Analysis", Target_Feature.app)
app.add_app("Thermal_Images", Thermal_Images.app)
app.add_app("Model Metrics", model_metrics.app)
app.add_app("Prediction", Prediction.app)
# The main app
app.run()

st.sidebar.text("Designed And Deployed by:")
st.sidebar.text("Karteek Menda")