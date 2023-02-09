from common.repositories.BaseRepository import BaseRepository


class SensorRepository(BaseRepository):

    def __init__(self, config_path):
        super().__init__(config_path)
        self.load_config()
        self.db_tables = self.config['db_tables']
        self.load_db(self.config['db_configuration'])

    def insert_value(self, timestamp, value, table):
        query_str = "INSERT INTO {} (timestamp, value) VALUES ('{}', {});".format(table, timestamp, value)
        self.db_insert(query_str)
