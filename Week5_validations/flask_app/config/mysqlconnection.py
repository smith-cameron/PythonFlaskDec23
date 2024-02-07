
#< a cursor is the object we use to interact with the database
# < pymysql will be installed via pipenv for each project 
    # . pipenv install flask pymysql
    # . python -m pipenv install flask pymysql
import pymysql.cursors
#< this class will give us an instance of a connection to our database

class MySQLConnection:
    def __init__(self, db_schema):
        #! change the user and password as needed
        connection = pymysql.connect(host='localhost',
#> Update user to match YOUR mysql root user on your machine
                                    user='root',
#> Update password to match YOUR mysql password on your machine
                                    password='rootroot',
                                    db=db_schema,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=False)
        #< establish the connection to the database
        self.connection = connection

    #< query_db -> method to query the database
    def query_db(self, query: str, data: dict = None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print(">>>>>Running Query>>>>>", query)
                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # < INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # < SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    #< UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                #!!!!!!!!! if the query fails the method will return FALSE !!!!!!!!!!!
                print("!!!!!Something went wrong in MYSQL!!!!!", e)
                return False
            finally:
                #< close the connection
                self.connection.close()

#< connect receives the database we're using and uses it to create an instance of MySQLConnection
# < it is the function we will be calling in our models
def connect(db_schema):
    return MySQLConnection(db_schema)