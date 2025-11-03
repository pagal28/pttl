#pip install scikit-learn pandas

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.datasets import load_iris

# Step 1: Load a sample dataset (Iris dataset)
iris = load_iris()
X = iris.data
y = iris.target

# Convert to DataFrame for better readability
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
print("✅ Dataset Loaded Successfully!\n")

# Step 2: Display first few rows
print("📋 First 5 rows of the dataset:")
print(df.head())

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("\n📊 Data split into training (80%) and testing (20%) sets.")

# Step 4: Train a simple Machine Learning model (Logistic Regression)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
print("\n🤖 Model training completed!")

# Step 5: Make predictions on test data
y_pred = model.predict(X_test)

# Step 6: Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"\n🎯 Model Accuracy: {accuracy*100:.2f}%")

print("\n📈 Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("\n🧩 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
