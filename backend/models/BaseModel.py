class BaseModel():
    def __init__(self, connection):
        self.connection = connection

    def CreateBinnacle(self, userId, action, ip):
        cursor = self.connection.connection.cursor()
        created = True
        sql = '''
            INSERT INTO
            binnacle
            (
                user,
                action,
                ip_address
            )
            VALUES
            (
                %s,
                %s,
                %s
            )
            '''
        args = (userId, action, ip,)
        
        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            created = False

        return created