import os.path
import yaml

"""
pytest -srvx application_catalog.py
"""

catalog_path = "../catalog"
catalog_index = os.path.join(catalog_path, "index.yaml")


def test_load_app_index():
    with open(catalog_index, "r") as index_app:
        applications = yaml.safe_load(index_app)

    for app in applications["index"]:
        print(f"NAME: {app['name']} PATH: {app['path']}")

    assert True
