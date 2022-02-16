from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment

from datetime import datetime


app = Flask(__name__)
# bootstrap = Bootstrap(app)
# moment = Moment(app)

@app.route("/")
def home():
    return render_template('home.html', current_time=datetime.utcnow())

@app.route("/contact.html")
def contact():
    return render_template('contact.html', current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', current_time=datetime.utcnow()), 500


if __name__ == '__main__':
    app.run(debug=True)


