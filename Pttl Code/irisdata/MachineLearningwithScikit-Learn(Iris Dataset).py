# ---------------------------------------------------------
# Program: Machine Learning on Custom Iris Dataset
# Subject: Python Practical – Machine Learning (Scikit-Learn)
# Author: <Your Name>
# ---------------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ------------------- Load Dataset -------------------
def load_dataset(filename="iris.csv"):
    """Loads dataset from CSV and encodes target labels."""
    df = pd.read_csv(filename)
    print("✅ Dataset loaded successfully!\n")
    print(df.head(), "\n")

    # Encode species names as numbers
    df["species_code"] = df["species"].astype("category").cat.codes
    X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y = df["species_code"]
    return X, y, df

# ------------------- Train and Evaluate Model -------------------
def train_and_evaluate_model(X, y):
    """Splits dataset, trains model, and evaluates performance."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"📊 Model Accuracy: {acc * 100:.2f}%")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    return model

# ------------------- Predict from User Input -------------------
def predict_sample(model):
    """Allows user to enter flower measurements for prediction."""
    print("\n--- PREDICT NEW SAMPLE ---")
    sl = float(input("Enter sepal length: "))
    sw = float(input("Enter sepal width: "))
    pl = float(input("Enter petal length: "))
    pw = float(input("Enter petal width: "))

    prediction = model.predict([[sl, sw, pl, pw]])[0]
    species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
    print(f"\n🌸 Predicted Species: {species_map.get(prediction, 'Unknown')}")

# ------------------- Main Function -------------------
def main():
    print("=== MACHINE LEARNING MODEL USING CUSTOM IRIS CSV ===\n")
    X, y, df = load_dataset()
    model = train_and_evaluate_model(X, y)
    predict_sample(model)

# ------------------- Entry Point -------------------
if __name__ == "__main__":
    main()
