import psycopg2

try: 
    connection = psycopg2.connect(
        dbname = 'phonebook', 
        user = 'khas', 
        password = '', 
        host = 'localhost'
    )

    connection.autocommit = True

    cursor = connection.cursor()

    # cursor.execute(
    #     """CREATE TABLE phonebook(
    #         id serial PRIMARY KEY,
    #         name varchar(50) NOT NULL,
    #         phone varchar(50) NOT NULL
    #     );"""
    # )

    # cursor.execute(
    #     """INSERT INTO phonebook (name, phone)
    #     VALUES ('Ahmad', '77015554422');"""
    #     )

    # cursor.execute(
    #     """UPDATE phonebook
    #     SET name = 'Alikhan', phone = '88005553535'
    #     WHERE id = 1;"""
    #     )

    # cursor.execute(
    #     """COPY phonebook(id, name, phone) 
    #     FROM '/Users/khas/Documents/codes/pp2/Lab_10/phones.csv' 
    #     WITH (FORMAT CSV, DELIMITER ',', HEADER)"""
    #     )

    # cursor.execute(
    #     """DELETE FROM phonebook
    #     WHERE name = 'Alikhan';"""
    #     )

    cursor.execute("""SELECT * FROM phonebook;""")

    print(cursor.fetchall())

except Exception as exception:
    print("Error occured", exception)
finally:
    if connection:
        cursor.close()
        connection.close()


