import pathlib


def get_project_root():
    """Returns project root folder."""
    return pathlib.Path(__file__).parent.parent.parent


def get_production_model_dir():
    """Returns production model directory."""
    return get_project_root() / "server" / "tnyml" / "models"
