import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


class DataBaseBehavior:

    @staticmethod
    def create_connection():
        try:
            return psycopg2.connect(
                f"dbname='{os.environ.get('POSTGRES_DB')}'"
                f"user='{os.environ.get('POSTGRES_USER')}' "
                f"host='{os.environ.get('POSTGRES_HOST')}' "
                f"password='{os.environ.get('POSTGRES_PASSWORD')}'"
            )
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        except (Exception, psycopg2.OperationalError) as error:
            print(error)

    @staticmethod
    def destroy_connection(connection):
        if connection is not None:
            connection.commit()
            connection.close()

    @staticmethod
    def execute_sql(cursor, query, values=None):
        records = None
        try:
            if 'INSERT' in query:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
        except (Exception, psycopg2.Error) as error:
            print(error)
        finally:
            if cursor is not None:
                cursor.close()
            return records


class DataBaseManager(DataBaseBehavior):

    def create_table(self, query):
        conn = self.create_connection()
        cursor = conn.cursor()
        self.execute_sql(cursor, query)
        self.destroy_connection(conn)

    def drop_table(self, table_name):
        query = f"DROP TABLE {table_name}"
        conn = self.create_connection()
        cursor = conn.cursor()
        self.execute_sql(cursor, query)
        self.destroy_connection(conn)

    def insert_data_into_crash_canvas_history(self, values: tuple):
        query = f"INSERT INTO crash_canvas_history (uuid, rate, date_hour) VALUES (%s,%s,%s)"
        conn = self.create_connection()
        cursor = conn.cursor()
        self.execute_sql(cursor, query, values)
        self.destroy_connection(conn)
