from datetime import datetime
from .. import db


class StringJwt(db.Model):
    """ Log Model for storing log related details """
    __tablename__ = "stringjwt"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    string = db.Column(db.String(256), nullable=False)
    access_token = db.Column(db.String(256), nullable=True)
    update_at = db.Column(db.DateTime, nullable=True)
    delete_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    delete_flag = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<Log '{}'>".format(self.update_at)

