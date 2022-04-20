"""This test the logging"""
import os


def is_path_exist(logfile):
    root = os.path.dirname(os.path.abspath(__file__))
    logfile = os.path.join(root, '../app/logs/'+logfile)
    assert os.path.exists(logfile) is True


def test_log_files_exists(client):
    client.get("/")
    is_path_exist('app.log')
    is_path_exist('request.log')



