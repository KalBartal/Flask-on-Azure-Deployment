import sys
import logging
import os

# Add virtual environment packages to path
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
venv_dir = os.path.join(base_dir, 'antenv', 'lib', 'python3.9', 'site-packages')
sys.path.insert(0, venv_dir)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
