import sqlite3

def create_db_new():
    db = sqlite3.connect('users.db', check_same_thread=False)
    sql = db.cursor()
    sql.execute('''CREATE TABLE IF NOT EXISTS USERS(
        user_id INTEGER,
        first_name VARCHAR,
        messageid INT,
        message VARCHAR)''')
    sql.execute('''CREATE TABLE IF NOT EXISTS blocked(
        user_id INT)''')
    sql.execute('''CREATE TABLE IF NOT EXISTS user(
        user_id INT)''')
    sql.close()
    db.close()


def database_query(query: str,spec_args):
    """Performs database commands.
    :params:
    query: str - this should be your command to be executed"""
    db = sqlite3.connect('users.db', check_same_thread=False)
    with db:
        sql = db.cursor()
        sql.execute(query,spec_args)
        result = sql.fetchall()
    if db:
        db.commit()
        sql.close()

    return result
def database_query_spec(query: str):
    """Performs database commands.
    :params:
    query: str - this should be your command to be executed"""
    db = sqlite3.connect('users.db', check_same_thread=False)
    with db:
        sql = db.cursor()
        sql.execute(query)
        result = sql.fetchall()
    if db:
        db.commit()
        sql.close()

    return result
