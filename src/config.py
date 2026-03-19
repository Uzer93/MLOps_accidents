from pathlib import Path

# Root of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Main folders
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "preprocessed"

SRC_DIR = PROJECT_ROOT / "src"
MODELS_DIR = SRC_DIR / "models"

# Preprocessed dataset files
X_TRAIN_PATH = PROCESSED_DATA_DIR / "X_train.csv"
X_TEST_PATH = PROCESSED_DATA_DIR / "X_test.csv"
Y_TRAIN_PATH = PROCESSED_DATA_DIR / "y_train.csv"
Y_TEST_PATH = PROCESSED_DATA_DIR / "y_test.csv"

# Model artifacts
MODEL_PATH = MODELS_DIR / "trained_model.joblib"
TEST_FEATURES_PATH = MODELS_DIR / "test_features.json"