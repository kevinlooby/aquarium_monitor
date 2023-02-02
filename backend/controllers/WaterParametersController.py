from flask import Blueprint, jsonify
from flask_restful import Resource, Api

from services import WaterParametersFetchService


class WaterParametersController(Resource):

    def __init__(self):
        self.parameters_fetch_service = WaterParametersFetchService()

    def get(self):
        ph = self.parameters_fetch_service.get_ph()

        try:
            data = {
                'ph': ph,
            }

            response = jsonify(data)
            response.headers["Access-Control-Allow-Origin"] = "*"

        except KeyError:
            response = jsonify("Invalid request")
            response.status_code = 403

        return response


water_parameters_bp = Blueprint('water_parameters', __name__)
water_parameters_api = Api(water_parameters_bp)
water_parameters_api.add_resource(WaterParametersController, '/data')
