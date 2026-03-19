from pathlib import Path
import requests

from src.config import RAW_DATA_DIR

BASE_URL = "https://full-stack-assets.s3.eu-west-3.amazonaws.com/MLOps/Accidents/"
FILES_TO_DOWNLOAD = [
    "caracteristiques-2021.csv",
    "lieux-2021.csv",
    "usagers-2021.csv",
    "vehicules-2021.csv",
]


def download_file(url: str, destination: Path) -> None:
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    with open(destination, "wb") as file:
        file.write(response.content)


def run_ingestion() -> None:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Raw data folder: {RAW_DATA_DIR}")

    for filename in FILES_TO_DOWNLOAD:
        file_url = BASE_URL + filename
        destination = RAW_DATA_DIR / filename

        print(f"Downloading {filename} ...")
        download_file(file_url, destination)
        print(f"Saved to {destination}")

    print("Ingestion completed successfully.")


if __name__ == "__main__":
    run_ingestion()