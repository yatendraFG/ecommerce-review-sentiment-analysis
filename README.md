# ecommerce-review-sentiment-analysis

E-commerce Data Sentiment Analysis API
This project is a simple Flask API that predicts the sentiment (Positive, Negative, Neutral) of user reviews based on an e-commerce dataset.

It uses:

A trained SVM (Support Vector Machine) model

TF-IDF Vectorizer for text preprocessing

Flask to serve the prediction endpoint

🚀 Features
Predict sentiment of any text input (review, comment, feedback, etc.)

Easy-to-use API with JSON input

Built using Flask and Scikit-learn

Ready for integration into frontend apps or mobile apps

🛠 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/ecommerce-sentiment-analysis-api.git
cd ecommerce-sentiment-analysis-api
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # For Windows
# or
source venv/bin/activate  # For Mac/Linux
Install required libraries

bash
Copy
Edit
pip install -r requirements.txt
Ensure you have the following files:

model_svm.pkl → (your trained SVM model)

vectorizer.pkl → (your TF-IDF vectorizer)

Run the Flask App

bash
Copy
Edit
python app.py
App will start at:
http://127.0.0.1:5000/

📩 API Usage
Endpoint: /predict
Method: POST
Content-Type: application/json

Request Body Example:
json
Copy
Edit
{
  "text": "This product is amazing! I love it."
}
Response Example:
json
Copy
Edit
{
  "sentiment": "Positive"
}
🔥 Example cURL Request
bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"text\":\"The delivery was late and the packaging was damaged.\"}"
📚 Project Structure
bash
Copy
Edit
/ecommerce-sentiment-analysis-api
│
├── app.py               # Flask app
├── model_svm.pkl         # Trained sentiment model
├── vectorizer.pkl        # TF-IDF Vectorizer
├── requirements.txt      # List of required Python packages
└── README.md             # Project documentation
📦 Requirements
Flask

scikit-learn

numpy

pickle

(optional) pandas (for data exploration)

Install all at once:

bash
Copy
Edit
pip install -r requirements.txt
🙏 Acknowledgments
Dataset: [Custom E-commerce Reviews Dataset] or [Kaggle datasets]

Libraries: Flask, Scikit-learn, Python

📜 License
This project is licensed under the MIT License.

🎯 That's it! Now you can easily use your API for real-world e-commerce sentiment analysis!
Would you like me to also prepare a sample requirements.txt file for you? (so you can deploy this easily!)
