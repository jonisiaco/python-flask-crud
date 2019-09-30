import mysql.connector
from mysql.connector import errorcode

class Mysql(object):
    __instance = None

    __host = None
    __user = None
    __password = None
    __database = None

    __session = None
    __connection = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Mysql, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, host='', user='', password='', database=''):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def _open(self, dictionary = False):
        try:
            cnx = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__password,
                                          database=self.__database)
            self.__connection = cnx

            if dictionary:
                self.__session = cnx.cursor( dictionary=True, buffered=True )
            else:    
                self.__session = cnx.cursor( prepared=True )

            return self.__session

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print 'Something is wrong with your user name or password'
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print 'Database ERROR'
            else:
                print err

    def _close(self):
        self.__session.close()
        self.__connection.close()

    def _commit(self):
        self.__connection.commit()

