import streamlit as st
import joblib

# 1. Configure the web page
st.set_page_config(page_title="Spam Detector AI", page_icon="🛡️", layout="centered")

# 2. Load the pipeline (Cached so it only loads once)
@st.cache_resource
def load_pipeline():
    # Paths match the files we saved in Notebooks 02 and 03
    vectorizer = joblib.load("models/count_vectorizer.pkl")
    best_model = joblib.load("models/best_svm_model.pkl")
    return vectorizer, best_model

# 3. Initialize the app safely
try:
    vectorizer, best_model = load_pipeline()
    models_loaded = True
except FileNotFoundError:
    st.error("⚠️ Model files not found! Please ensure 'count_vectorizer.pkl' and 'best_svm_model.pkl' exist in the 'models/' directory.")
    models_loaded = False

# 4. Build the UI
st.title("🛡️ Spam Message Detector")
st.markdown("Built by the Tech Master ML team. Enter a message below to classify it using our optimized SVM model.")

# Text input box
user_message = st.text_area("Message Content:", height=150, placeholder="Type or paste your message here...")

# 5. Prediction Logic
if st.button("Analyze Message"):
    if not models_loaded:
        st.error("System offline: Models missing.")
    elif user_message.strip():
        # Transform the text into numbers
        message_vec = vectorizer.transform([user_message])
        
        # Predict using the SVM
        prediction = best_model.predict(message_vec)[0]
        
        # Display results
        st.markdown("### 📊 Analysis Result")
        if prediction == "spam":
            st.error("🚨 **SPAM** - This message looks suspicious and was blocked.")
        else:
            st.success("✅ **HAM** - This message looks safe.")
    else:
        st.warning("Please enter some text to analyze.")