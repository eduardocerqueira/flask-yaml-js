from os.path import join
import yaml


def override_catalog_path(flask_app_path):
    new_path = str(flask_app_path).replace("app", "catalog")
    return new_path


def load_app_catalog(catalog_path):
    """ get applications from catalog index """
    catalog_index = join(catalog_path, "index.yaml")
    with open(catalog_index, "r") as index_app:
        applications = yaml.safe_load(index_app)
    return applications


def load_app_descriptor(catalog_path, app_path):
    """ get application descriptor """
    with open(join(catalog_path, app_path), "r") as app_record:
        app_descriptor = yaml.safe_load(app_record)
    return app_descriptor
