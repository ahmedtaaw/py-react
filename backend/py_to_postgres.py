import psycopg2

hostname = 'localhost'
database = 'tdb'
username = 'tuser'
pwd = '11223344'
port_id = 5432

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=hostname, 
        database=database, 
        user=username, 
        password=pwd, 
        port=port_id
        )
    cur = conn.cursor()
    
    create_script = ''' CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    '''

    cur.execute(create_script)
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()