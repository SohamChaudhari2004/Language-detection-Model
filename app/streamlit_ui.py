import streamlit as st
import requests

# API URL
API_URL = "https://language-detection-model-saa3.onrender.com/predict"

# Customizing the UI theme
st.set_page_config(
    page_title="Language Detection App",
    page_icon="🌍",
    layout="centered"
)

# Stylish Header
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🌍 Language Detection App</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;color:#FFFFFF'>Enter any text below and let the AI detect its language!</p>",
    unsafe_allow_html=True
)

# Input Section
st.markdown("### 📝 Enter the Text Below")
user_input = st.text_input("Enter your text here", label_visibility="collapsed")

# Detect Language Button
if st.button("🔍 Detect Language", use_container_width=True):
    if user_input.strip():
        try:
            response = requests.post(API_URL, json={"text": user_input})

            if response.status_code == 200:
                result = response.json()
                detected_lang = result["language"]
                
                # Displaying result
                st.success("✅ Language Detected!")
                st.markdown(
                    f"<div style='background-color: #e8f5e9; padding: 10px; border-radius: 10px; text-align: center;'>"
                    f"<h3 style='color: #2E7D32;'>🌐 {detected_lang}</h3>"
                    f"</div>",
                    unsafe_allow_html=True
                )
            else:
                st.error("⚠️ Something went wrong. Please try again.")
            

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter some text to detect its language.")

# Footer Section
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Made with ❤️ by <b>Soham Chaudhari</b></p>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'><a href='https://github.com/SohamChaudhari2004' target='_blank'>🔗 GitHub</a></p>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center; color: #FFFFFF;'>Made using Streamlit and FastAPI with docker</h3>",
    unsafe_allow_html=True
)