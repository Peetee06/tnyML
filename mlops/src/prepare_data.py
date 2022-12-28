import itertools
import logging
import mlflow
import click
import pandas as pd
import pathlib


@click.command()
@click.option(
    "--input_path", help="Path to data", type=click.Path(exists=True)
)
@click.option(
    "--output_path", help="Path to save prepared data", type=click.Path()
)
def prepare_data(input_path, output_path):
    """Prepare data"""
    logger = logging.getLogger(__name__)
    logger.info("Preparing data")
    input_path = pathlib.Path(input_path)
    output_path = pathlib.Path(output_path)
    with mlflow.start_run():
        # load data
        data_list = []
        for filepath in itertools.chain(
            input_path.glob("*.jpeg"),
            input_path.glob("*.jpg"),
            input_path.glob("*.png"),
        ):
            label = filepath.name.split(".")[0]
            data_list.append({"file_path": filepath, "label": label})
        # convert to dataframe
        df = pd.DataFrame(data_list)
        logger.info(df.head())
        # save data
        datafile = output_path / (input_path.name + ".csv")
        logger.info(f"Saving data to {datafile}")
        df.to_csv(datafile, index=False)
        mlflow.log_artifact(datafile, "prepared data")


if __name__ == "__main__":
    prepare_data()
