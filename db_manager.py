from config_reader import ReadConfig
from sqlalchemy.orm import *
from sqlalchemy import *


class DBManager:
    def __init__(self):
        read_config = ReadConfig()
        self.config = read_config.read()

    def get_session(self):

        pg_config = dict(self.config.items('pg_config', {}))
        if pg_config:
            connection_sting = "postgresql://" + pg_config['user'] + ':' + pg_config['passwd'] + '@' + \
                               pg_config['host'] + '/' + pg_config['db']
        else:
            connection_sting = "postgresql://postgres:password@localhost/ridecell"

        sql_engine = create_engine(connection_sting)

        session_maker = sessionmaker(bind=sql_engine)
        conn = sql_engine.connect()
        session = session_maker(bind=conn)
        return session

    def close_session(self, session):
        try:
            session.close()
        except Exception as e:
            print 'Error:', e
            pass