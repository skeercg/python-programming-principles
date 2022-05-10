from tkinter import OFF
import psycopg2
import config

try: 
    connection = psycopg2.connect(
        dbname = config.dbname, 
        user = config.user, 
        password = config.password, 
        host = config.host
    )

    connection.autocommit = True

    cursor = connection.cursor()

    # cursor.execute(
    #     """CREATE TABLE unique_phonebook(
    #         id serial PRIMARY KEY,
    #         name varchar(50) NOT NULL UNIQUE,
    #         phone varchar(50) NOT NULL
    #     );"""
    # )

    # name_pattern = '%'
    # phone_pattern = '%'

    # cursor.execute(
    #     """SELECT name, phone
    #     FROM unique_phonebook
    #     WHERE 
    #         name LIKE %s AND phone LIKE %s;""", (name_pattern, phone_pattern,)
    # )

    # name = 'Maxim'
    # phone = '77771231266'

    # cursor.execute(
    #     """INSERT INTO unique_phonebook (name, phone) 
    #     VALUES (%s, %s)
    #     ON CONFLICT (name)
    #     DO 
    #     UPDATE SET phone = EXCLUDED.phone""", (name, phone,)
    # )

    # n = 2
    # names = ['Dias', 'Askar']
    # phones = ['87779992233', '76667777182']

    # cursor.execute(
    #     """DO $$
    #     DECLARE
    #         names VARCHAR(50)[] := %s;
    #         phones VARCHAR(50)[] := %s;
    #     BEGIN
    #         FOR i IN 1..%s LOOP
    #             INSERT INTO unique_phonebook (name, phone)
    #             VALUES (names[i], phones[i]);
    #         END LOOP;
    #     END; $$""", (names, phones, n,)
    # )

    # limit = 5
    # offset = 2

    # cursor.execute(
    #     """SELECT * FROM unique_phonebook LIMIT %s OFFSET %s""", (limit, offset,)
    # )

    # name_pattern = '%'
    # phone_pattern = '%'

    # cursor.execute(
    #     """DELETE FROM unique_phonebook
    #     WHERE name LIKE %s OR phone LIKE %s""", (name_pattern, phone_pattern,)
    # )

    cursor.execute("""SELECT * FROM unique_phonebook;""")

    print(cursor.fetchall())

except Exception as exception:
    print("Error occured", exception)
finally:
    if connection:
        cursor.close()
        connection.close()


