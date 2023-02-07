import decimal
import json

import pymysql


def decimal_default(obj):
    """
    Convert decimal.Decimal object to float

    Parameters
    ----------
    obj : object

    Returns
    -------
    float

    Raises
    ------
    TypeError
        If obj is not of type decimal.Decimal

    """

    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError


class MySQLConnector:

    def __init__(self, host, database, user, password):
        """

        Parameters
        ----------
        port : int
            Port on server where MySQL is hosted

        db_name : str
            Name of the database to be connected on the instance

        host : str
            Endpoint URL to connect to MySQL AWS RDS instance

        user : str
            Username to access the database instance

        password :
            Password to access the database instance

        """

        self.database = database
        self.user = user
        self.host = host
        self.password = password
        self.conn = None

    def mysql_connect(self):
        """
        Open connection to MySQL database

        """

        self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password,
                                    db=self.database)

    def mysql_close(self):
        """
        Close connection to MySQL database

        """

        self.conn.close()

    # def execute_query_sorted_keys(self, query_str):
    #     """
    #     Execute a SELECT query and sort the returned data by key.
    #
    #     Parameters
    #     ----------
    #     query_str : str
    #         Database query
    #
    #     Returns
    #     -------
    #     str
    #         Sorted data as JSON formatted string
    #
    #     """
    #
    #     cursor = self.conn.cursor()
    #     cursor.execute(query_str)
    #     result = cursor.fetchall()
    #     row_headers = [x[0] for x in cursor.description]  # this will extract row headers
    #
    #     json_data = []
    #
    #     if len(row_headers) == 1:
    #         for r in result:
    #             json_data.append(r[0])
    #         cursor.close()
    #         return json.dumps(json_data)
    #
    #     for result in result:
    #         json_data.append(dict(zip(row_headers, result)))
    #
    #     cursor.close()
    #
    #     return json.dumps(sorted(json_data), sort_keys=True)

    # def execute_query_str_first_record(self, query_str):
    #     """
    #     Return only the first record received from the database
    #
    #     Parameters
    #     ----------
    #     query_str : str
    #         Database query
    #
    #     Returns
    #     -------
    #     tuple or None
    #
    #     """
    #
    #     cursor = self.conn.cursor()
    #     cursor.execute(query_str)
    #     result = cursor.fetchall()
    #
    #     if not cursor.rowcount:
    #         print("No results found")
    #
    #     cursor.close()
    #
    #     for row in result:
    #         return row[0]
    #
    #     return None

    def get_cursor(self):
        """
        Get the database cursor object

        Returns
        -------
        Cursor
            PyMySQL cursor object

        """

        return self.conn.cursor()

    def insert_query(self, query):
        cursor = self.conn.cursor()

        try:
            cursor.execute(query)
            self.conn.commit()
            cursor.close()
            return True

        # TODO: specify exception
        except:
            self.conn.rollback()
            cursor.close()
            return False

    def execute_query_get_records(self, query_str):
        """
        Execute a query for getting records as specified in query_str.

        Parameters
        ----------
        query_str : str
            Database query

        Returns
        -------
        json_data : list[dict]
            Query results as list of JSON records

        """

        cursor = self.conn.cursor()
        cursor.execute(query_str)
        results = cursor.fetchall()

        row_headers = [x[0] for x in cursor.description]  # this will extract row headers

        json_data = []

        if len(row_headers) == 1:
            for r in results:
                json_data.append(r[0])
            cursor.close()
            return json.dumps(json_data)

        for result in results:
            json_data.append(dict(zip(row_headers, result)))

        cursor.close()

        return json_data

    def execute_query_get_array_json(self, query_str):
        """
        Execute a query as specified in query_str

        Parameters
        ----------
        query_str : str
            The database query

        Returns
        -------
        results : tuple
            The data returned from the database

        """

        cursor = self.conn.cursor()
        cursor.execute(query_str)
        results = cursor.fetchall()

        row_headers = [x[0] for x in cursor.description]  # this will extract row headers

        json_data = []

        if len(row_headers) == 1:
            for r in results:
                json_data.append(r[0])
            cursor.close()
            return json.dumps(json_data)

        cursor.close()

        return results
