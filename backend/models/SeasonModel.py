from .BaseModel import BaseModel

class SeasonModel(BaseModel):
    def GetSeasons(self):
        cursor = self.connection.connection.cursor()
        result = []
        sql = "SELECT * FROM season ORDER BY id"

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            result = False
        
        return result

    def CreateSeason(self, seasonData):
        cursor = self.connection.connection.cursor()
        result = True

        sql = "UPDATE season SET active = 0 WHERE active = 1"

        try:
            cursor.execute(sql)
            self.connection.connection.commit()
        except:
            result = 'Ocurrió un error al desactivar la temporada anterior'

        if result == True:
            seasonDate = seasonData['date']
            sql = "INSERT INTO season (date) VALUES (%s)"
            args = (seasonDate,)

            try:
                cursor.execute(sql, args)
                self.connection.connection.commit()
            except:
                result = 'Ocurrió un error al crear la nueva temporada'

        return result
    
    def GetSeasonById(self, id):
        cursor = self.connection.connection.cursor()
        sql = "SELECT * FROM season WHERE id = %s"
        args = (id,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        except:
            result = None
        
        return result
    
    def GetCurrentSeason(self):
        cursor = self.connection.connection.cursor()
        sql = "SELECT * FROM season WHERE active = 1"

        try:
            cursor.execute(sql)
            result = cursor.fetchone()
        except:
            result = False
        
        return result