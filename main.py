import streamlit as st
import pickle

# -------------------------------
# Load your saved model
# -------------------------------
@st.cache_resource
def load_model():
    with open("pipeline_model2.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("Text Classification App")
st.write("Paste your text below and get prediction from your trained model.")

user_text = st.text_area("Enter text:", height=200)

if st.button("Predict"):
    if user_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        pred = model.predict([user_text])[0]

        # Convert model output to positive/negative
        if pred == "negative" or pred == "Negative" or pred == 0:
            result = "Negative"
        else:
            result = "Positive"

        st.success(f"### 🔮 Prediction: **{result}**")

