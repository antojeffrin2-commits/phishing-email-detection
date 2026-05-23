# phishing-email-detection
📧 Phishing Email Detection Model
📌 About

This project is a simple machine learning model that detects whether an email is Phishing or Safe based on its text content.

It uses basic natural language processing and a classification algorithm to identify patterns in emails.

🧰 Libraries Used
pandas → for handling dataset
re → for text cleaning
scikit-learn → for machine learning
⚙️ Features
📊 Trains on a dataset of phishing and safe emails
🧹 Cleans and preprocesses text
🔢 Converts text into numerical features using TF-IDF
🤖 Uses Naive Bayes for classification
📈 Displays:
Accuracy
Confusion Matrix
Classification Report
🧪 Allows real-time testing of custom emails
🧠 How It Works
1. Data Preparation

A dataset of emails is created with labels:

phishing
safe
2. Text Preprocessing

Emails are cleaned by:

converting to lowercase
removing URLs
removing special characters
3. Feature Extraction

Text is converted into numbers using TF-IDF Vectorization.

👉 This helps the model understand word importance.

4. Model Training

A Multinomial Naive Bayes model is trained on the dataset.

5. Evaluation

The model is tested and outputs:

Accuracy score
Confusion matrix
Classification report
6. Prediction

Users can input their own email text, and the model predicts:

phishing
safe
🚀 Usage

Run the script:

python phishing_model.py

Then enter email text when prompted.

Type exit to stop.

⚠️ Important Note

This is a basic model for learning purposes only.

Dataset is small
Accuracy is limited
Not suitable for real-world security use
🧠 What I Learned
basic machine learning workflow
text preprocessing techniques
TF-IDF feature extraction
classification using Naive Bayes
model evaluation methods
💬 Final Note

This project demonstrates a simple approach to detecting phishing emails using machine learning and helps build foundational understanding of cybersecurity and AI concepts.
