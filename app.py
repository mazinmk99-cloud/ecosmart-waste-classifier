import streamlit as st

# വെബ്സൈറ്റിന്റെ പേര്
st.title("EcoSmart: AI-Powered Waste Classifier")

# ചെറിയൊരു വിവരണം
st.write("ഈ ആപ്പ് ഉപയോഗിച്ച് നിങ്ങൾക്ക് വേസ്റ്റ് ഇനങ്ങളെ തിരിച്ചറിയാം!")

# ഫോട്ടോ അപ്‌ലോഡ് ചെയ്യാനുള്ള ഓപ്ഷൻ
uploaded_file = st.file_uploader("ഒരു വേസ്റ്റ് ഇനത്തിന്റെ ഫോട്ടോ അപ്‌ലോഡ് ചെയ്യുക...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='അപ്‌ലോഡ് ചെയ്ത ചിത്രം', use_container_width=True)
    st.write("ഇതൊരു മനോഹരമായ തുടക്കമാണ്! അടുത്ത ഘട്ടത്തിൽ നമ്മൾ ഇതിൽ AI മോഡൽ ആഡ് ചെയ്യും.")
import streamlit as st
from transformers import pipeline
from PIL import Image

# വെബ്സൈറ്റിന്റെ തലക്കെട്ട്
st.title("EcoSmart: AI Waste Classifier")
st.write("ഒരു വേസ്റ്റ് ഫോട്ടോ അപ്‌ലോഡ് ചെയ്താൽ ഇത് എന്താണെന്ന് ഞാൻ പറഞ്ഞുതരാം!")

# ഫോട്ടോ അപ്‌ലോഡ് ചെയ്യാനുള്ള ഓപ്ഷൻ
uploaded_file = st.file_uploader("ഫോട്ടോ തിരഞ്ഞെടുക്കൂ...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='അപ്‌ലോഡ് ചെയ്തത്', use_container_width=True)
    
    # AI മോഡൽ ലോഡ് ചെയ്യുന്നു (Hugging Face-ൽ നിന്ന്)
    st.write("AI വിശകലനം ചെയ്യുന്നു...")
    classifier = pipeline("image-classification", model="microsoft/resnet-50")
    results = classifier(image)
    
    # ഫലം കാണിക്കുന്നു
    st.write("ഫലം:")
    for res in results:
        st.write(f"- {res['label']}: {round(res['score']*100, 2)}%")

