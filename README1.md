# 🐦 Twitter Sentiment Analysis using NLP

Classify tweets into positive, negative, or neutral sentiments using machine learning.

---

## 🚀 Live Demo

- 🔗 Streamlit App: https://twitteranalysis-nlp-va4wiwxv4inwapp4pkzvxcq.streamlit.app  
- 📂 GitHub Repo: https://github.com/stevejoy-9381/twitterAnalysis-nlp  

---

## 📌 Problem Statement

Social media platforms like Twitter generate massive amounts of textual data every day.  
Understanding public sentiment from this data is important for businesses, marketing, and decision-making.

This project aims to automatically classify tweets into **positive, negative, or neutral sentiment** using NLP techniques.

---

## 💡 Solution Overview

This project uses a **traditional machine learning pipeline**:

- Text preprocessing (cleaning, normalization)
- Feature extraction using **TF-IDF**
- Classification using **Logistic Regression**

👉 TF-IDF converts text into numerical features, while Logistic Regression is a strong baseline model for text classification tasks :contentReference[oaicite:1]{index=1}  

---

## ⚙️ Tech Stack

- Python  
- Scikit-learn  
- Pandas, NumPy  
- NLTK / Text preprocessing  
- Streamlit  

---

## 📊 Dataset

- Source: Kaggle — **Sentiment140 Dataset**
- Contains **1.6 million labeled tweets**
- Labels:
  - Positive  
  - Negative  
  - Neutral (processed/derived)

👉 This dataset is widely used as a benchmark for sentiment analysis tasks :contentReference[oaicite:2]{index=2}  

---

## 🤖 Model Details

- Model: Logistic Regression  
- Feature Extraction: TF-IDF  
- Task: Multi-class classification  
- Accuracy: **80%**  

### Preprocessing Steps:
- Removing URLs, mentions, hashtags  
- Lowercasing text  
- Removing stopwords  
- Stemming / normalization  

👉 Preprocessing is essential because tweets contain noisy text such as hashtags, mentions, and slang :contentReference[oaicite:3]{index=3}  

---

## 📊 Features

- 🧠 Classifies tweet sentiment in real time  
- ⚡ Fast prediction using lightweight ML model  
- 📊 Handles large-scale tweet datasets  
- 🌐 Interactive Streamlit web app  

---

## 📸 Screenshots

(Add screenshots of your app here)

Example:
