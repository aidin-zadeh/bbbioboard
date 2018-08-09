

import os, inspect
from flask import Flask

CURR_FILE =  inspect.getabsfile(inspect.currentframe())
CURR_DIR = os.path.dirname(CURR_FILE)
ROOT_DIR = os.path.dirname(CURR_DIR)

# set up Flask web server
app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
from bbbioboard import views