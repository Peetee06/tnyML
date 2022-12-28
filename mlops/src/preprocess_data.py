import mlflow
import pathlib
import pandas as pd
import click


@click.command()
@click.option("--data_path", help="Path to the data")
@click.option("--output_path", help="Path to the output")
def preprocess_data(data_path, output_path):
    """Preprocess Titanic data"""
    data_path = pathlib.Path(data_path)
    output_path = pathlib.Path(output_path)

    with mlflow.start_run():
        data = pd.read_csv(data_path)
        data.drop(
            ["PassengerId", "Name", "Ticket", "Cabin", "Embarked"],
            axis=1,
            inplace=True,
        )

        output_path = output_path / "train_preprocessed.csv"
        data.to_csv(output_path, index=False)
        mlflow.log_artifact(output_path, "preprocessed data")


if __name__ == "__main__":
    preprocess_data()
