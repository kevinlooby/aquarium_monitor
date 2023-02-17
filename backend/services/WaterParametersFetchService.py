from flask_restful import Resource
import os
from backend import resources

from backend.repositories.WaterParametersFetchRepository import WaterParametersFetchRepository


class WaterParametersFetchService(Resource):

    def __init__(self):
        self.repository = WaterParametersFetchRepository(os.path.join(os.path.dirname(resources.__file__), "db_config.yml"))

    def get_ph(self):
        return self.repository.get_ph()

    def get_temperature(self):
        return self.repository.get_temperature()

    def get_temperature_ambient(self):
        return self.repository.get_temperature_ambient()
