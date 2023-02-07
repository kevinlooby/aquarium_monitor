from common.repositories.BaseRepository import BaseRepository
import numpy as np


class WaterParametersFetchRepository(BaseRepository):

    def __init__(self, config_path):
        super().__init__(config_path)
        self.load_config()
        self.db_tables = self.config['db_tables']
        self.load_db(self.config['db_configuration'])

    def get_temperature(self):
        query_str = "select timestamp, value from {};".format(self.config['db_tables']['temperature'])

        result = self.execute_query(query_str)
        return result

    def get_ph(self):
        n = 100
        values = np.random.rand(10000 + n) * 3 + 5.5
        return np.convolve(values, np.ones(n)/n, 'valid')
