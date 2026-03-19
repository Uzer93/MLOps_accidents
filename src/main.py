import argparse

from src.data.ingest import run_ingestion
from src.data.preprocess import run_preprocessing
from src.models.train import run_training


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the MLOps accident pipeline.")
    parser.add_argument(
        "--step",
        choices=["ingest", "preprocess", "train", "all"],
        required=True,
        help="Pipeline step to run",
    )

    args = parser.parse_args()

    if args.step == "ingest":
        run_ingestion()
    elif args.step == "preprocess":
        run_preprocessing()
    elif args.step == "train":
        run_training()
    elif args.step == "all":
        run_preprocessing()
        run_training()


if __name__ == "__main__":
    main()