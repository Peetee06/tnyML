import pytest
from tnyml_app import flask_app


@pytest.fixture(scope="module")
def app():
    flask_app.config.update({"TESTING": True})  # type: ignore
    return flask_app


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()
