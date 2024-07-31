from .BaseModel import BaseModel

class BinnacleModel(BaseModel):    
    def GetBinnacle(self):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            user.nickname,
            user.id as user_id,
            binnacle.action,
            binnacle.ip_address,
            CONCAT(YEAR(binnacle.date), '-', LPAD(MONTH(binnacle.date), 2, '0'), '-', LPAD(DAY(binnacle.date), 2, '0'), ' ', TIME(binnacle.date)) AS created_at
            FROM
            binnacle
            INNER JOIN user ON user.id = binnacle.user
            ORDER BY
            binnacle.date DESC
            '''
        
        try:
            cursor.execute(sql)
            binnacle = cursor.fetchall()
            if binnacle == tuple():
                binnacle = []
        except:
            binnacle = []

        return binnacle
    
    def GetBinnacleOfUser(self, userId):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            user.nickname,
            user.id as user_id,
            binnacle.action,
            binnacle.ip_address,
            CONCAT(YEAR(binnacle.date), '-', LPAD(MONTH(binnacle.date), 2, '0'), '-', LPAD(DAY(binnacle.date), 2, '0'), ' ', TIME(binnacle.date)) AS created_at
            FROM
            binnacle
            INNER JOIN user ON user.id = binnacle.user
            WHERE 
            user.id = %s
            ORDER BY
            binnacle.date DESC'''
        
        try:
            cursor.execute(sql, (userId,))
            binnacle = cursor.fetchall()
            if binnacle == tuple():
                binnacle = []
        except:
            binnacle = []
        
        return binnacle
    
    def GetBinnacleBetweenDates(self, initialDate, finalDate):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            user.nickname,
            user.id as user_id,
            binnacle.action,
            binnacle.ip_address,
            CONCAT(YEAR(binnacle.date), '-', LPAD(MONTH(binnacle.date), 2, '0'), '-', LPAD(DAY(binnacle.date), 2, '0'), ' ', TIME(binnacle.date)) AS created_at
            FROM
            binnacle
            INNER JOIN user ON user.id = binnacle.user
            WHERE 
            binnacle.date BETWEEN %s AND %s
            ORDER BY
            binnacle.date DESC'''
        
        try:
            cursor.execute(sql, (initialDate, finalDate,))
            binnacle = cursor.fetchall()
            if binnacle == tuple():
                binnacle = []
        except:
            binnacle = []
        
        return binnacle
    
    def GetBinnacleOfUserBetweenDates(self, userId, initialDate, finalDate):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            user.nickname,
            user.id as user_id,
            binnacle.action,
            binnacle.ip_address,
            CONCAT(YEAR(binnacle.date), '-', LPAD(MONTH(binnacle.date), 2, '0'), '-', LPAD(DAY(binnacle.date), 2, '0'), ' ', TIME(binnacle.date)) AS created_at
            FROM
            binnacle
            INNER JOIN user ON user.id = binnacle.user
            WHERE 
            user.id = %s AND
            binnacle.date BETWEEN %s AND %s
            ORDER BY
            binnacle.date DESC'''
        
        try:
            cursor.execute(sql, (userId, initialDate, finalDate,))
            binnacle = cursor.fetchall()
            if binnacle == tuple():
                binnacle = []
        except:
            binnacle = []
        
        return binnacle