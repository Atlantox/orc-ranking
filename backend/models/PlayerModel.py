from .BaseModel import BaseModel

class PlayerModel(BaseModel):
    def GetPlayers(self):
        cursor = self.connection.connection.cursor()
        result = []
        sql = "SELECT * FROM player ORDER BY name"

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            result = False
        
        return result

    def CreatePlayer(self, playerData):
        name = playerData['name']
        cursor = self.connection.connection.cursor()
        result = True

        sql = "INSERT INTO player (name) VALUES (%s)"
        args = (name,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False

        return result
    
    def GetPlayerByName(self, name):
        cursor = self.connection.connection.cursor()

        sql = "SELECT * FROM player WHERE name = %s"
        args = (name,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        except:
            result = None
        
        return result
    
    def GetPlayerById(self, id):
        cursor = self.connection.connection.cursor()

        sql = "SELECT * FROM player WHERE id = %s"
        args = (id,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        except:
            result = None
        
        return result
    
    def UpdatePlayer(self, playerId, playerData):
        newName = playerData['name']
        cursor = self.connection.connection.cursor()
        result = True

        sql = "UPDATE player SET name = %s WHERE id = %s"
        args = (newName, playerId,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        
        return result
    
    def DeletePlayer(self, playerId):
        cursor = self.connection.connection.cursor()
        result = True

        sql = "DELETE FROM player WHERE id = %s"
        args = (playerId,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        
        return result