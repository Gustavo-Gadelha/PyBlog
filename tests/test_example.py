import os


def test_example():
    assert os.environ.get('SECRET_KEY') != ''
