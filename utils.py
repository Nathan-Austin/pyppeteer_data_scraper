from configparser import ConfigParser
import psycopg2


def config(filename='database.ini', section='postgresql'):
    """takes secret login info from database.ini to be used to connect to postgres"""
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def commit_to_dataBase(query):
    """ Connect to the PostgreSQL database server """
    conn = None

    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
        # execute a statement
        cur.execute(query)
        conn.commit()
        cur.close()



    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        # close the communication with the PostgreSQL


    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

