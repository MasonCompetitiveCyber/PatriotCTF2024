from flask_mysqldb import MySQL

mysql = MySQL()

def query_db(query, args=(), one=False):
    cursor = mysql.connection.cursor()
    cursor.execute(query, args)
    rv = [dict((cursor.description[idx][0], value)
        for idx, value in enumerate(row)) for row in cursor.fetchall()]
    return (rv[0] if rv else None) if one else rv

def call_procedure(proc_name, args=(), one=False):
    cur = mysql.connection.cursor()
    cur.callproc(proc_name, args)
    mysql.connection.commit()
    rv = [result.fetchall() for result in cur.fetchall()]
    cur.close()
    return (rv[0][0] if rv and rv[0] else None) if one else rv
