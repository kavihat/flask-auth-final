"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name

import pytest

from click.testing import CliRunner

from app import create_app
from app.cli import create_log_folder


@pytest.fixture()
def application():
    """This makes the app"""
    application = create_app()
    application.config.update({
        "TESTING": True,
    })
    CliRunner().invoke(create_log_folder)
    yield application


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()
