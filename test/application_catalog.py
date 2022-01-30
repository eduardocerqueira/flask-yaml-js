import yaml
from app.util import load_app_catalog
from os.path import join


"""
pytest -srvx application_catalog.py
"""

CATALOOG_PATH = "../catalog"


def test_load_app_index():
    """ load application catalog index, loading level 1 """
    applications = load_app_catalog(catalog_path=CATALOOG_PATH)
    for app in applications["index"]:
        print(f"NAME: {app['name']} PATH: {app['path']}")

    assert "name" and "path" in app


def test_load_application_descriptor():
    """ load application's descriptor, loading level 2 """
    applications = load_app_catalog(catalog_path=CATALOOG_PATH)

    for app in applications["index"]:
        with open(join(CATALOOG_PATH, app["path"]), "r") as app_record:
            app_descriptor = yaml.safe_load(app_record)

        print(app_descriptor)
        assert "name" and "repo" in app_descriptor
