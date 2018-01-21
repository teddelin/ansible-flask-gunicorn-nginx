from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from main.views import main

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test_admin:test123@db1:5432/test_db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(main)

from main import models

if __name__ == "__main__":
    app.run(host='0.0.0.0')
