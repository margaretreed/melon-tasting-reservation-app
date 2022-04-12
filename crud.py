"""CRUD operations."""

from model import db, User, Reservation, connect_to_db

def create_user(username, email, fname, lname):
    """Create and return a new user."""

    user = User(username=username, email=email, fname=fname, lname=lname)

    return user

def create_reservation(user_id, res_datetime):
    """Create and return a new reservation."""

    reservation = Reservation(user_id=user_id, res_datetime=res_datetime, canceled=False)

    return reservation

# Query all reservations made by a user
def get_user_reservations(username):
     """Return a reservation object by it's username"""
    user = User.query.filter_by(username=username)

     return User.reservations

# Print all available times within range

# Cancel Reservation

# Edit reservation