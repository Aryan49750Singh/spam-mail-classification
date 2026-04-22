import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.set_page_config(page_title="Spam Detector", page_icon="📬")

st.title("📬 Spam Mail Detector")
st.write("Enter a message to check whether it is Spam or Ham")

# User input
user_input = st.text_area("Enter your message here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message")
    else:
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)

        if prediction[0] == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam (Ham)")
