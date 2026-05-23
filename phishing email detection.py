import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# 🔹 Step 1: Sample dataset
data = {
    "email": [
        "Your account has been suspended click here to verify",
        "Win a free iPhone now click this link",
        "Meeting scheduled for tomorrow",
        "Please review the attached report",
        "Update your password immediately",
        "Congratulations you won a lottery claim now",
        "Project deadline extended",
        "Team lunch tomorrow at 1pm"
    ],
    "label": [
        "phishing",
        "phishing",
        "safe",
        "safe",
        "phishing",
        "phishing",
        "safe",
        "safe"
    ]
}

df = pd.DataFrame(data)

# 🔹 Step 2: Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["email"])
y = df["label"]

# 🔹 Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 🔹 Step 4: Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# 🔹 Step 5: Predictions
y_pred = model.predict(X_test)

# 🔹 Step 6: Evaluation
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", cm)

# 🔹 Test custom email
test_email = ["Click this link to reset your password immediately"]
test_vector = vectorizer.transform(test_email)
prediction = model.predict(test_vector)

print("\nTest Email Prediction:", prediction[0])