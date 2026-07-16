from .BaseModel import BaseModel

class WarningModel(BaseModel):
    SELECT_TEMPLATE = '''
        SELECT
        warning.id,
        warning.player,
        warning.reason,
        CONCAT(YEAR(warning.date), '-', LPAD(MONTH(warning.date), 2, '0'), '-', LPAD(DAY(warning.date), 2, '0')) AS date, 
        warning.season,
        player.name as player_name,
        season.name as season_name
        FROM
        warning
        INNER JOIN player ON player.id = warning.player
        INNER JOIN season ON season.id = warning.season        
    '''

    def GetWarnings(self):
        cursor = self.connection.connection.cursor()
        result = []
        sql = self.SELECT_TEMPLATE

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            result = False
        
        return result

    def CreateWarning(self, warningData):
        cursor = self.connection.connection.cursor()

        player = warningData['player']
        reason = warningData['reason']
        season = warningData['season']
        date = warningData['date']
        sql = "INSERT INTO warning (player, reason, season, date) VALUES (%s, %s, %s, %s)"
        args = (player, reason, season, date)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
            result = True
        except:
            result = 'Ocurrió un error al crear el warning'

        return result
    
    def GetWarningById(self, id):
        cursor = self.connection.connection.cursor()
        sql = self.SELECT_TEMPLATE + ' WHERE warning.id = %s GROUP BY warning.id ORDER BY warning.date DESC' 
        args = (id,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        except:
            result = None
        
        return result
    
    def GetWarningBySeason(self, season):
        cursor = self.connection.connection.cursor()
        sql = self.SELECT_TEMPLATE + ' WHERE warning.season = %s GROUP BY warning.id ORDER BY warning.date DESC' 
        args = (season,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
        except:
            result = None
        
        return result
    
    def GetWarningByPlayer(self, player):
        cursor = self.connection.connection.cursor()
        sql = self.SELECT_TEMPLATE + ' WHERE warning.player = %s GROUP BY warning.id ORDER BY warning.date DESC'
        args = (player,)
        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
        except:
            result = None
        
        return result
    
    def DeleteWarning(self, id):
        cursor = self.connection.connection.cursor()
        sql = "DELETE FROM warning WHERE id = %s"
        args = (id,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = 'Ocurrió un error al borrar el warning'

        return result