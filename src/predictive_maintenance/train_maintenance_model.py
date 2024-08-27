# train_maintenance_model.py
"""
Script for training the Predictive Maintenance model.
"""

from sklearn.linear_model import LinearRegression
from common.data_processing import clean_data, normalize_data
import joblib

def train_model(training_data, target_data):
    """
    Trains a predictive maintenance model using Linear Regression.
    Args:
        training_data: The data to train the model on.
        target_data: The target data (maintenance outcomes).
    Returns:
        Trained model.
    """
    model = LinearRegression()
    model.fit(training_data, target_data)
    return model

if __name__ == "__main__":
    # Load and preprocess training data
    raw_training_data = "path_to_training_data"
    raw_target_data = "path_to_target_data"
    
    cleaned_data = clean_data(raw_training_data)
    normalized_data = normalize_data(cleaned_data)

    # Train the model
    model = train_model(normalized_data, raw_target_data)

    # Save the trained model
    joblib.dump(model, "models/predictive_model.pkl")
    print("Predictive maintenance model trained and saved.")
