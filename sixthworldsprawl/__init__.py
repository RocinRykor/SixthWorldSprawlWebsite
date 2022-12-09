import os
import sys
from . import app
models = app.models
db = app.db

# This site was started on 2021-03-17

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)

application = app.application

