import streamlit as st
import joblib
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Spam Detection System", page_icon="🛡️")
st.title("Spam Detection System")
st.write("TechMaster Academy - Phase 03 Optimization Project")

# 2. Load Models (Commented out until Member 4 finishes tuning)
# @st.cache_resource
# def load_pipeline():
#     vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
#     best_model = joblib.load("models/best_svm_model.pkl")
#     return vectorizer, best_model
# vectorizer, best_model = load_pipeline()

# 3. User Input Section
st.markdown("### Input Message")
user_message = st.text_area("Paste the email or SMS text below:")

if st.button("Predict"):
    if user_message.strip():
        # --- Active Prediction Logic (Enable when models are ready) ---
        # message_vec = vectorizer.transform([user_message])
        # prediction = best_model.predict(message_vec)[0]
        # probabilities = best_model.predict_proba(message_vec)[0]
        # ham_prob, spam_prob = probabilities[0], probabilities[1]
        
        # --- Mock Data for current UI testing ---
        prediction = "spam"
        spam_prob, ham_prob = 0.87, 0.13
        
        # 4. Display Results
        st.markdown("### Prediction Result")
        if prediction == "spam":
            st.error("⚠️ SPAM")
        else:
            st.success("✅ HAM")
            
        col1, col2 = st.columns(2)
        col1.metric("Spam Probability", f"{spam_prob * 100:.1f}%")
        col2.metric("Ham Probability", f"{ham_prob * 100:.1f}%")
    else:
        st.warning("Please enter a message to classify.")

st.divider()

# 5. Model Evaluation Section
st.markdown("### Model Comparison & Confusion Matrix")
st.info("Metrics and final confusion matrix will be imported here once Member 4 completes the GridSearchCV optimization.")