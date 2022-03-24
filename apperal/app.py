import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports
from multipage import MultiPage
from pages import apperal,visualizations,similarity_score,test,vendor_score,bar_plot # import your pages here

# Create an instance of the app
app = MultiPage()

# Title of the main page
#display = Image.open('Logo.png')
#isplay = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
#col1, col2 = st.beta_columns(2)
#col1.image(display, width = 400)
#col2.title("Data Storyteller Application")

# Add all your application here
#app.add_page("Main Page", apperal.app)
#app.add_page("visualizations", visualizations.app)
app.add_page("Apparel", test.app)
app.add_page("Raw Material Recommendation", similarity_score.app)
app.add_page("Vendor Scores", vendor_score.app)
app.add_page("Sustainable Raw Material", bar_plot.app)



# The main app
app.run()
