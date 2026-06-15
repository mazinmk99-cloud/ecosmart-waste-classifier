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

