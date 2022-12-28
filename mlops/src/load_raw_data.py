import pathlib
import zipfile
from kaggle.api import KaggleApi
import click
import mlflow


@click.command()
@click.option(
    "--competition", default="dogs-vs-cats", help="Kaggle competition name"
)
@click.option(
    "--output_path", default="data/raw", help="Path to save raw data"
)
def load_raw_data(competition, output_path):
    """Download raw data from Kaggle"""
    output_path = pathlib.Path(output_path)
    with mlflow.start_run():
        kaggle = KaggleApi()
        kaggle.authenticate()
        kaggle.competition_download_files(
            competition=competition, path=output_path
        )
        # unzip files
        with zipfile.ZipFile(
            output_path / f"{competition}.zip", "r"
        ) as zip_ref:
            zip_ref.extractall(output_path)
        train_data_path = output_path / "train.zip"
        test_data_path = output_path / "test1.zip"
        mlflow.log_artifact(train_data_path, "raw train data")
        mlflow.log_artifact(test_data_path, "raw test data")


if __name__ == "__main__":
    load_raw_data()
