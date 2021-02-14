'''
    This is the entry file for the application
'''
# Flask imports
from flask import Flask
from flask_cors import CORS

# Gevent imports for production-grade deployment
from gevent.pywsgi import WSGIServer

# Import our Route Blueprints
from routes.users import users

# Initialize flask
app = Flask(__name__)

# Register our blueprints with the app so it can route to them
app.register_blueprint(users)

# Initialize WSGIServer
http_server = WSGIServer(('', 5000), app)

# Initialize CORS for local testing
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Send it
http_server.serve_forever()
