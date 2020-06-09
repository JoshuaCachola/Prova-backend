from flask import Flask, jsonify
from flask_cors import cross_origin, CORS
from flask_migrate import Migrate
from .config import Configuration
from .routes import main
from .auth import AuthError, requires_auth
from .models import db, User, Route


app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(main.bp)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
db.init_app(app)
Migrate(app, db)


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


# This doesn't need authentication
@app.route("/api/public")
@cross_origin(headers=["Content-Type", "Authorization"])
def public():
    response = "Hello from a public endpoint! You don't need to be authenticated to see this."
    return jsonify(message=response)


# This needs authentication
@app.route("/api/private")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def private():
    response = "Hello from a private endpoint! You need to be authenticated to see this."
    return jsonify(message=response)
