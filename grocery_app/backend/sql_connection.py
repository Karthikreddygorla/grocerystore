import mysql.connector 

__cnx=None
def get_sql_connection():
    print("opening mysql connection")
    global __cnx
    if __cnx is None: #only creating when it was none
        __cnx= mysql.connector.connect(
            user='root',
            password='302003',
            host='127.0.0.1',
            database='grocery_store'
        )
    return __cnx