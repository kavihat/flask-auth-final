"""This test the logging"""
import os

from click.testing import CliRunner
runner = CliRunner()


def test_create_log_folder():
    """This test the logging"""
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs')
    assert os.path.exists(logdir) is True
