"""This test the logging"""
import os

from click.testing import CliRunner

from app import create_log_folder

runner = CliRunner()


def test_create_response_folder():
    """This test the logging"""
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0

def test_create_request_log():
    request = runner.invoke(create_log_folder)
    assert request.exit_code == 0

def test_path_exist():
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs')
    assert os.path.exists(logdir) is True

