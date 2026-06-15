import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

st.title("EcoSmart: AI Waste Classifier")
st.write("ഇതൊരു പ്രൊഫഷണൽ AI ആപ്പാണ്!")

uploaded_file = st.file_uploader("ഒരു വേസ്റ്റ് ഫോട്ടോ അപ്‌ലോഡ് ചെയ്യുക...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='അപ്‌ലോഡ് ചെയ്ത ചിത്രം', use_container_width=True)
    st.write("AI മോഡൽ പ്രോസസ്സ് ചെയ്യുന്നു...")
    
    # ഇവിടെ നമ്മൾ സിമ്പിൾ ആയി ഒരു മെസ്സേജ് കാണിക്കുന്നു
    # AI മോഡൽ ഫയൽ (model.h5) പിന്നീട് നമുക്ക് ആഡ് ചെയ്യാം
    st.success("ആപ്പ് വിജയകരമായി പ്രവർത്തിക്കുന്നു! AI മോഡൽ ഇന്റഗ്രേഷൻ ഉടൻ പൂർത്തിയാകും.")
