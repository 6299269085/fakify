# Fakify - Fake News Detection

An **end-to-end project of Supervised Machine Learning**, trained on more than **24,000 news articles** (both fake and true) with an achieved accuracy of **98%**. This project leverages **Logistic Regression** and **TF-IDF Vectorization** to classify news articles as **Fake** or **Real** based on their content.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Stages of Development](#stages-of-development)
- [Deployment](#deployment)
- [Installation & Usage](#installation--usage)
- [Future Improvements](#future-improvements)

## Project Overview

Fake news detection is a crucial task in today's digital world. This project aims to classify news articles as either **Fake** or **Real** using Machine Learning techniques. The dataset contains articles labeled as either "Fake" or "True," allowing the model to learn patterns that distinguish real news from fabricated content.

## Dataset

- The dataset consists of **24,000+ news articles**, labeled as "Fake" and "True."
- Features include **title, text, and subject**.
- Preprocessing includes **text cleaning, removing stopwords, and vectorizing using TF-IDF**.

## Stages of Development

### **Stage 1: Data Collection and Preprocessing**

- The dataset was cleaned to remove unnecessary characters, punctuation, and stopwords.
- TF-IDF Vectorization was applied to convert text into numerical features.

### **Stage 2: Model Selection and Training**

- The **Logistic Regression** model was selected due to its efficiency in text classification tasks.
- The dataset was split into **training (80%)** and **testing (20%)**.
- The model achieved an accuracy of **98%**.

### **Stage 3: Building the Flask API**

- A **Flask application** was developed to serve the model.
- The app provides a simple web interface for users to input a news article and get a prediction.

### **Stage 4: Frontend Development**

- The frontend is built with **HTML, CSS, and JavaScript** and is hosted on **Netlify**.
- The frontend interacts with the backend via **API calls**.

### **Stage 5: Deployment on Render**

- The Flask backend is **deployed on Render**, making the API accessible online.
- A **POST request** is used to send user input to the model and receive predictions.

## Deployment

- **Backend:** Hosted on **Render**
- Users can enter the title, text, and subject of a news article to check its authenticity.

## Installation & Usage

1. **Clone the repository:**
   ```sh
   git clone https://github.com/6299269085/fakify.git
   cd fakify
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Flask app:**
   ```sh
   python app.py
   ```
4. **Access the app at:** `(https://fakify-r4ro.onrender.com)`

## Future Improvements

- Integrating **deep learning models** for better accuracy.
- Enhancing the **user interface**.
- Expanding the dataset with **multilingual news articles**.

---

Developed with ❤️ by Rishav Raj 🚀

