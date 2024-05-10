from enum import unique
from ssl import _create_unverified_context
from private import db,app,login_manager
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))