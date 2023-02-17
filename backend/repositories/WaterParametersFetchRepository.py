from common.repositories.BaseRepository import BaseRepository
import numpy as np


class WaterParametersFetchRepository(BaseRepository):

    def __init__(self, config_path):
        super().__init__(config_path)
        self.load_config()
        self.db_tables = self.config['db_tables']
        self.load_db(self.config['db_configuration'])

    def get_temperature(self):
        return self.get_parameter('temperature')

    def get_temperature_ambient(self):
        return self.get_parameter('temp_ambient')

    def get_ph(self):
        return self.get_parameter('ph')

    def get_parameter(self, parameter):
        query_str = "select timestamp, value from {};".format(self.config['db_tables'][parameter])
        result = self.execute_query(query_str)
        return result
