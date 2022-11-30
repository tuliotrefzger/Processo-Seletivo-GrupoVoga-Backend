from .. import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        rep = (
            "User: "
            + str(self.id)
            + "\n"
            + "Name: "
            + self.name
            + "\n"
            + "Email: "
            + self.email
            + "\n"
            + "Phone number: "
            + self.phone_number
            + "\n"
            + "Date created: "
            + self.date_created
            + "\n"
        )
        return rep