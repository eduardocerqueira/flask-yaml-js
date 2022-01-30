from flask import Flask
from app.util import load_app_catalog, override_catalog_path

app = Flask(__name__)

app.config.update(
    catalog_path=override_catalog_path(app.root_path)
)


@app.route('/')
def index():
    applications = load_app_catalog(app.config.get("catalog_path"))
    print(applications)
    return applications


@app.route('/hello')
def hello():
    return 'Hello, World'