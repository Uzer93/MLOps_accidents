from src.data.make_dataset import main as make_dataset_main


def run_preprocessing() -> None:
    print("Starting preprocessing...")
    make_dataset_main()
    print("Preprocessing completed successfully.")


if __name__ == "__main__":
    run_preprocessing()