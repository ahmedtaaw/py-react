import psycopg2
import psycopg2.extras


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
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('DROP TABLE IF EXISTS users')

    create_script = ''' CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    '''
    cur.execute(create_script)
    insert_script = '''INSERT INTO users (name, email, password) 
    VALUES (%s, %s, %s)'''
    insert_value = [('pablo','pablo@gmail', '123456'),
                    ('osman','osman@gmail', '123456'),
                    ('simo','simo@gmail', '123456')]
    for record in insert_value:
        cur.execute(insert_script, record)

    cur.execute('SELECT * FROM users')
    for record in cur.fetchall():
        print(record['name'], record['email'], record['password'])

    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()