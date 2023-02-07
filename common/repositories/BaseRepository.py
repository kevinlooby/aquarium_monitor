from common.repositories.MySQLConnector import MySQLConnector
import yaml


class BaseRepository:

    def __init__(self, config_path):
        self.config = None
        self.config_path = config_path
        self.db = None

    def load_config(self):
        with open(self.config_path, 'r') as f:
            print(self.config_path)
            self.config = yaml.safe_load(f)

    def load_db(self, config):
        """
        Adds an instance of MySQLConnector as an attribute for interfacing with mySQL

        Parameters
        ----------
        port : int
            Database port number

        db : str
            Name of the database

        db_endpoint : str
            Endpoint of the database

        db_user : str
            Database username

        db_password : str
            Password associated with database username

        """
        self.db = MySQLConnector(**config)

    def db_connect(self):
        self.db.mysql_connect()

    def db_close(self):
        self.db.mysql_close()

    def db_get_json(self, query_str):
        """

        Parameters
        ----------
        query_str : str
            The database query

        Returns
        -------
        dict
            Output of execute query function

        """

        return self.db.execute_query_get_array_json(query_str)

    def execute_query(self, query_str):
        self.db_connect()
        result = self.db_get_json(query_str)
        self.db_close()

        return result

    def db_insert(self, query_str):
        success = self.db.insert_query(query_str)
        if not success:
            raise Exception('Database insert failed.')
