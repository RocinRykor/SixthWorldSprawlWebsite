import os
import sys

# This site was started on 2021-03-17

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)

import app
from app import db
from app import models
from app import login_manager


application = app.application
