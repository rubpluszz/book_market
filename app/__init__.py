from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

from app import routes
