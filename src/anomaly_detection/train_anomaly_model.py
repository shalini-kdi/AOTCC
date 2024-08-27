# train_anomaly_model.py
"""
Script for training the Anomaly Detection model.
"""

from sklearn.ensemble import IsolationForest
from common.data_processing import clean_data, normalize_data
import joblib

def train_model(training_data):
    """
    Trains an anomaly detection model using Isolation Forest.
    Args:
        training_data: The data to train the model on.
    Returns:
        Trained model.
    """
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(training_data)
    return model

if __name__ == "__main__":
    # Load and preprocess training data
    raw_training_data = "path_to_training_data"
    cleaned_data = clean_data(raw_training_data)
    normalized_data = normalize_data(cleaned_data)

    # Train the model
    model = train_model(normalized_data)

    # Save the trained model
    joblib.dump(model, "models/anomaly_model.pkl")
    print("Anomaly detection model trained and saved.")
