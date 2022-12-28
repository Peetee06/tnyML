import pathlib
import zipfile
import mlflow
import click


@click.command()
@click.option(
    "--file_path",
    default="data/raw/train.zip",
    help="Path to extract data from",
    type=click.Path(exists=True),
)
@click.option(
    "--output_path",
    default="data/extracted",
    help="Path to save extracted data",
)
def extract(file_path, output_path):
    """Extract data from a zip file"""
    file_path = pathlib.Path(file_path)
    output_path = pathlib.Path(output_path)
    with mlflow.start_run():
        # extract files
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(output_path)
        filestem = file_path.stem  # get the file name without the extension
        output_path = output_path / filestem
        mlflow.log_artifact(output_path, "extracted data")


if __name__ == "__main__":
    extract()
