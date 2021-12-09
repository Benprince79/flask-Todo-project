import mysql.connector

mybase = mysql.connector.connect(
    host = 'localhost',
    database = 'list',
    user = 'root',
    password = ''
)

mycursor = mybase.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS todo(
        ID INT NOT NULL AUTO_INCREMENT,
        task_name VARCHAR(50) NOT NULL,
        task_description VARCHAR(255) NOT NULL,
        importance INT NOT NULL,
        time TIME NOT NULL,
        date DATE NOT NULL,
        PRIMARY KEY(ID)
    )"""
)