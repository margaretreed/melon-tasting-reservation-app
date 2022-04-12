"""Models for tasting reservation scheduling app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)

    # reservations = a list of reservation objects
 
 
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Reservation(db.Model):
    """A reservation."""

    __tablename__ = "reservations"

    res_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    res_datetime = db.Column(db.DateTime)
    canceled = db.Column(db.Boolean)

    user = db.relationship("User", backref="reservations")

 
    def __repr__(self):
        return f'<Reservation res_id={self.res_id} email={self.email}>'




def connect_to_db(flask_app, db_uri="postgresql:///tastings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)