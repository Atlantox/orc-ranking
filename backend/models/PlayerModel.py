from .BaseModel import BaseModel

class PlayerModel(BaseModel):
    def GetPlayers(self):
        cursor = self.connection.connection.cursor()
        result = []
        sql = '''
            SELECT 
            player.id,
            player.name,
            COUNT(tournament.id) as tournaments,
            SUM(tournament_result.wins) as points,
            SUM(CASE WHEN tournament_result.winner = 1 THEN 1 ELSE 0 END) as wins
            FROM 
            player 
            INNER JOIN tournament_result ON tournament_result.player = player.id
            INNER JOIN tournament ON tournament.id = tournament_result.tournament
            WHERE
            tournament.active = 1 AND
            tournament.season = (SELECT id FROM season WHERE active = 1)
            GROUP BY
            player.id
            ORDER BY 
            player.name
            '''

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