import os

from flask import Flask, render_template, session, send_from_directory, redirect
from flask_cors import CORS

from frontend.controllers import index_bp

# Create the Flask app and RESTful API
app = Flask(__name__)
app.secret_key = ''

# Enable cross-origin resource sharing
CORS(app)

# Register blueprints
app.register_blueprint(index_bp)


# Handled 404 errors
@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('pages/error.html'), 404


# Additional routing for homepage
@app.route('/')
def index(path=None):
    return redirect('/index')


# Serve static JS files
@app.route('/js/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join('../backend', 'static', 'js'), filename)


if __name__ == '__main__':
    app.run(debug=False)
