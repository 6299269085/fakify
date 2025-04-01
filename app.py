from flask import Flask, request, jsonify, render_template
import joblib
import os

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# Update the paths to point to your local files
model_path = os.path.join(app.root_path, "fake_news_model.pkl")
vectorizer_path = os.path.join(app.root_path, "tfidf_vectorizer.pkl")

# Load the trained model and vectorizer
lr = joblib.load(model_path)  # Load the logistic regression model
vectorizer = joblib.load(vectorizer_path)  # Load the vectorizer

def clean_text(text):
    # Simple text cleaning (Modify based on your dataset requirements)
    return text.lower().strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    title = request.form['title']
    text = request.form['text']
    subject = request.form['subject']
    
    # Combine inputs for prediction
    combined_input = f"{title} {text} {subject}"
    
    # Clean and vectorize the input text
    cleaned_text = clean_text(combined_input)
    vectorized_text = vectorizer.transform([cleaned_text])
    
    # Predict using the logistic regression model
    prediction = lr.predict(vectorized_text)[0]
    
    # Send result to the HTML page
    result = 'Real' if prediction == 1 else 'Fake'
    
    return render_template('index.html', result=result, title=title, text=text, subject=subject)

def handler(event, context):
    return app(event, context)


