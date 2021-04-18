# app.py

from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css", filters="postcss")

assets.register("css", css)
css.build()

from market import routes