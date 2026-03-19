## Baseline pipeline
1. import_raw_data.py
- Downloads 4 CSV files from S3
- Saves them into data/raw

2. make_dataset.py
- Reads raw CSVs
- Merges and cleans data
- Creates target and features
- Splits into train/test
- Saves X_train, X_test, y_train, y_test into data/preprocessed

3. train_model.py
- Loads preprocessed CSVs
- Trains RandomForestClassifier
- Saves trained_model.joblib

4. predict_model.py
- Loads trained model
- Predicts from JSON or manual input

Here we need to make the current workflow clean, modular, and reproducible.
So stop treating it as separate scripts and start treating it as a system:

- easier to understand
- easier to rerun
- less dependent on manual typing
- less fragile
- easier to test
- ready for later automation

Pipeline Outline:
src/
│
├── data/
│   ├── ingest.py : Downloads raw data
│   ├── preprocess.py : preprocessing data
│
├── models/
│   ├── train.py : loads preprocessed data, trains model/s, saves them
│   ├── predict.py : loads trained model and performs predictions
│   ├── evaluate.py : Computes metrics and saves them
│
├── utils/
│   ├── paths.py 
│   ├── io.py
│   └── logger.py
│
├── config.py : stores folder paths adn key parameters in one place
├── main.py : central pipeline runner

Part A: No need for manual paths input
Part B: cetralize all paths
Part C: Scripts transformed into functions
Part D: single entry point

1. Understood tha data
2. Keeping the same behavior (model, dataset logic, outputs and structure), make central launcher, add evaluation step (Phase 1), same functionality, cleaner architecture


config.py = all paths in one place
ingest.py = download raw data
train.py = train the model
main.py = one command to run steps



