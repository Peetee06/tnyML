import mlflow
from ludwig.api import LudwigModel
from ludwig.contribs.mlflow import MlflowCallback
import pandas as pd
import pathlib
import click


@click.command()
@click.option("--data_path", help="Path to data", type=click.Path(exists=True))
@click.option(
    "--model_config_path",
    help="Path to model config",
    type=click.Path(exists=True),
)
@click.option(
    "--output_path", help="Path to save trained model", type=click.Path()
)
@click.option(
    "--model_name",
    help="Name of the model",
    type=click.STRING,
)
@click.option(
    "--experiment_name",
    help="Name of the experiment",
    type=click.STRING,
)
def train(
    data_path, model_config_path, output_path, model_name, experiment_name
):
    """Train model"""
    data_path = pathlib.Path(data_path)
    output_path = pathlib.Path(output_path)
    with mlflow.start_run():
        # load data
        df = pd.read_csv(data_path)

        # create model with mlflow callback
        # will log metrics, artifacts, and model
        model = LudwigModel(
            config=model_config_path,
            logging_level=20,
            callbacks=[MlflowCallback()],
        )
        # train model
        model.train(
            dataset=df,
            experiment_name=experiment_name,
            model_name=model_name,
            output_directory=output_path,
        )


if __name__ == "__main__":
    train()
