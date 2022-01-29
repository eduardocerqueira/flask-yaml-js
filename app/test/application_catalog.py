import os.path
import yaml

"""
pytest -srvx application_catalog.py
"""

catalog_path = "../catalog"
catalog_index = os.path.join(catalog_path, "index.yaml")


def test_load_app_index():
    """ load application catalog index, loading level 1 """
    with open(catalog_index, "r") as index_app:
        applications = yaml.safe_load(index_app)

    for app in applications["index"]:
        print(f"NAME: {app['name']} PATH: {app['path']}")

    assert "name" and "path" in app


def test_load_application_descriptor():
    """ load application's descriptor, loading level 2 """
    with open(catalog_index, "r") as index_app:
        applications = yaml.safe_load(index_app)

    for app in applications["index"]:
        with open(os.path.join(catalog_path, app["path"]), "r") as app_record:
            app_descriptor = yaml.safe_load(app_record)

        print(app_descriptor)
        assert "name" and "repo" in app_descriptor
