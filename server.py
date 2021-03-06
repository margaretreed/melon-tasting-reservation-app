"""Server for tasting reservation scheduling app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)

from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
# move to secrets.sh
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route('/scheduler')
def scheduler():
    """View scheduling tool"""

    return render_template('scheduler.html')

@app.route('/appointments')
def appointments():
    """View scheduled appointments"""

    return render_template('appointments.html')
    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)