import streamlit as st
import pickle
import re

# Load model and vectorizer
model = pickle.load(open('model_svm.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# Streamlit app
st.title("Sentiment Analysis App")

user_input = st.text_area("Enter text for sentiment analysis:", "")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        cleaned_text = clean_text(user_input)

        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)[0]

        if prediction == 1:
            sentiment = "Positive"
        elif prediction == 0:
            sentiment = "Negative"
        elif prediction == 2:
            sentiment = "Neutral"
        else:
            sentiment = "Unknown"

        st.success(f"*Sentiment:* {sentiment}")