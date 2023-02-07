from flask_restful import Resource

from backend.repositories.WaterParametersFetchRepository import WaterParametersFetchRepository


class WaterParametersFetchService(Resource):

    def __init__(self):
        self.repository = WaterParametersFetchRepository()

    def get_ph(self):
        return self.repository.get_temperature()

    def get_temperature(self):
        return self.repository.get_temperature()
