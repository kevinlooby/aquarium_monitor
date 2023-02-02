from flask_restful import Resource

from repositories.WaterParametersFetchRepository import WaterParametersFetchRepository


class WaterParametersFetchService(Resource):

    def __init__(self):
        self.repository = WaterParametersFetchRepository()

    def get_ph(self):
        return list(self.repository.get_ph())
