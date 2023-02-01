from flask import Blueprint, Response, render_template, make_response
from flask_restful import Resource, Api


class IndexController(Resource):

    def get(self):

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('pages/index.html'), 200, headers)


index_bp = Blueprint('index', __name__)
index_api = Api(index_bp)
index_api.add_resource(IndexController, '/index')
