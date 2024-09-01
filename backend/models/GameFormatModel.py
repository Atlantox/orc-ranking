from .BaseModel import BaseModel

class GameFormatModel(BaseModel):
    def GetFormats(self):
        cursor = self.connection.connection.cursor()
        result = []
        sql = "SELECT * FROM game_format"

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            result = False
        
        return result
    
    def GetFormatsPlayedInSeason(self, seasonId):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT DISTINCT
            game_format.id,
            game_format.name
            from
            game_format  
            INNER JOIN tournament ON tournament.format = game_format.name
            WHERE
            tournament.active = 1
        '''

        if seasonId is not None:
            sql += ' AND tournament.season = %s '

        sql +=  " ORDER BY game_format.name "
        try:
            if seasonId is not None:
                args = (seasonId,)
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)

            formats = cursor.fetchall()

            if formats == tuple():
                formats = []
                
        except:
            formats = 'Ocurrió un error al traer los formatos jugados' 

        

        return formats

    def CreateFormat(self, formatData):
        name = formatData['name']
        cursor = self.connection.connection.cursor()
        result = True

        sql = "INSERT INTO game_format (name) VALUES (%s)"
        args = (name,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        return result
    
    def GetFormatByName(self, name):
        cursor = self.connection.connection.cursor()

        sql = "SELECT * FROM game_format WHERE name = %s"
        args = (name,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        except:
            result = None
        
        return result
    
    def GetFormatById(self, id):
        cursor = self.connection.connection.cursor()

        sql = "SELECT * FROM game_format WHERE id = %s"
        args = (id,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        except:
            result = None
        
        return result
    
    def UpdateFormat(self, formatId, formatData):
        newName = formatData['name']
        cursor = self.connection.connection.cursor()
        result = True

        sql = "UPDATE game_format SET name = %s WHERE id = %s"
        args = (newName, formatId,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        
        return result
    
    def DeleteFormat(self, formatId):
        cursor = self.connection.connection.cursor()
        result = True

        sql = "DELETE FROM game_format WHERE id = %s"
        args = (formatId,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        
        return result