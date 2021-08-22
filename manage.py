import sys
from application.db import DataBaseManager
from application import proc_main


def run_scripts(param):
    db = DataBaseManager()
    sql = f"CREATE TABLE IF NOT EXISTS crash_canvas_history (" \
          f"id SERIAL, " \
          f"UUID VARCHAR NOT NULL, " \
          f"RATE VARCHAR NOT NULL, " \
          f"DATE_HOUR VARCHAR NOT NULL" \
          f");"
    if 'create_table' in param:
        db.create_table(sql)
    elif 'drop_table' in param:
        db.drop_table('crash_canvas_history')
    elif 'runserver' in param:
        proc_main()


if __name__ == '__main__':
    run_scripts(sys.argv)
