import distutils.dir_util
import click
import mlflow

import utils


@click.command()
@click.option("--model_name", help="Name of the model")
@click.option("--model_version", help="Version of the model", type=int)
def deploy_model(model_name, model_version):
    """Deploy model to production"""
    client = mlflow.MlflowClient()
    with mlflow.start_run():
        model_path = get_model_path(model_name, model_version, client)
        production_models_path = utils.get_production_model_dir()
        distutils.dir_util.copy_tree(
            str(model_path), str(production_models_path / model_name)
        )
        client.transition_model_version_stage(
            name=model_name,
            version=model_version,
            stage="Production",
        )


def get_model_path(model_name, model_version, client):
    """Get path to model"""
    models = client.search_model_versions(f"name='{model_name}'")
    model = [m for m in models if m.version == model_version][0]
    model_path = model.source.replace("file://", "")
    return model_path


if __name__ == "__main__":
    deploy_model()
