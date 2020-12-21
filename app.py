from config import DB_USER, DB_PASS, DB_HOST, DB_NAME
from db import initialize_db, models
from flask import Flask
from rest import initialize_app
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}'.format(
    DB_USER=DB_USER, DB_PASS=DB_PASS, DB_HOST=DB_HOST, DB_NAME=DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = initialize_db(app)
migrate = Migrate(app, db)
initialize_app(app=app)


if __name__ == '__main__':
    app.run(debug=True)
