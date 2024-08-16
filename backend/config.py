class DevelopmentCondfig:
    DEBUG = False
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'orc_ranking'
    MYSQL_CURSORCLASS = 'DictCursor' 

config = {
    'development': DevelopmentCondfig
}