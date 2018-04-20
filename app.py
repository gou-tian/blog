from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


@app.route('/secret')
@login_required
def secret():
    return '仅允许认证用户访问！'


if __name__ == '__main__':
    app.run()
