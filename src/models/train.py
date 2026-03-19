import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from src.config import X_TRAIN_PATH, Y_TRAIN_PATH, MODEL_PATH


def run_training() -> None:
    print(f"Loading X_train from: {X_TRAIN_PATH}")
    print(f"Loading y_train from: {Y_TRAIN_PATH}")

    X_train = pd.read_csv(X_TRAIN_PATH)
    y_train = pd.read_csv(Y_TRAIN_PATH)

    # Convert y_train from DataFrame with one column into a 1D array/Series
    y_train = y_train.squeeze()

    print("Training RandomForestClassifier...")
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to: {MODEL_PATH}")
    print("Training completed successfully.")


if __name__ == "__main__":
    run_training()