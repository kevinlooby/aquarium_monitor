from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api

from controllers import water_parameters_bp

app = Flask(__name__)
app.secret_key = ''

api = Api(app)
CORS(app)

bps = (
    water_parameters_bp,
)

for bp in bps:
    app.register_blueprint(bp)


@app.route('/', methods=['GET'])
def home():
    return jsonify("Hello, backend here.")


if __name__ == '__main__':
    app.run(port=8090, debug=False)
