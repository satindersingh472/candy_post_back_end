
# import mariadb
import mariadb
# import db creds file
import dbcreds

# connect db will connect to the database using dbcreds and return the cursor
# if there is an error in connecting it will try to find out the error 
# and print the error and return the error
def connect_db():
    try:
        conn = mariadb.connect(user=dbcreds.user, host= dbcreds.host, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor
        return cursor()
    except mariadb.OperationalError as error:
        print('Operational Error: ',error)
        return str(error)
    except mariadb.ProgrammingError as error:
        print('Programming Error: ',error)
        return str(error)
    except AttributeError as error:
        print('Attribute Error:',error)
        return str(error)
    except NameError as error:
        print('Name Error:',error)
        return str(error)
    except Exception as error:
        print('Unknown Error: ', error)
        return str(error)
    
# execute statment will use the cursor and 2 other arguments 
# after running the statement it will store the result into result variable and return it
# if there is any error it will find out the error
# and print out the name of error and information about the error
def execute_statement(cursor,statement,list=[]):
    try:
        cursor.execute(statement,list)
        result = cursor.fetchall()
        return result
    except mariadb.IntegrityError as error:
        print('Integrity Error: ',error)
        return str(error)
    except mariadb.ProgrammingError as error:
        print('Programming Error: ',error)
        return str(error)
    except TypeError as error:
        print('Type Error: ',error)
        return str(error)
    except Exception as error:
        print('Unknown Error:',error)
        return str(error)

# close connection will use the cursor to close the connection
# if failed then try to print the error with appropriate message and information about the error
def close_connection(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()
    except AttributeError as error:
        print('Attribute Error', error)
        return str(error)
    except Exception as error:
        print('Unknown Error: ',error)
        return str(error)

# conn_exe_close will use the connect_db(),
# execute_statment() and close_connection()
# will shrink the code to one line when needed to run a stored procedure from a database
def conn_exe_close(statement,list):
    cursor = connect_db()
    if(cursor == None):
        return 'Connection Error'
    result = execute_statement(cursor,statement,list)
    close_connection(cursor)
    return result

