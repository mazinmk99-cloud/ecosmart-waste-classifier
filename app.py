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
    
    # AI മോഡൽ ലോഡ് ചെയ്യുന്നു
    st.write("AI വിശകലനം ചെയ്യുന്നു...")
    try:
        classifier = pipeline("image-classification", model="microsoft/resnet-50")
        results = classifier(image)
        
        # ഫലം കാണിക്കുന്നു
        st.write("ഫലം:")
        for res in results:
            st.write(f"- {res['label']}: {round(res['score']*100, 2)}%")
    except Exception as e:
        st.write(f"എന്തോ കുഴപ്പം സംഭവിച്ചു: {e}")

