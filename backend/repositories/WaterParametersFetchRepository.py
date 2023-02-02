from flask_restful import Resource
import numpy as np


class WaterParametersFetchRepository(Resource):

    def get_ph(self):
        n = 100
        values = np.random.rand(10000 + n) * 3 + 5.5
        return np.convolve(values, np.ones(n)/n, 'valid')
