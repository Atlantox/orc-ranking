from .BaseModel import BaseModel

class PlayerModel(BaseModel):
    def GetPlayers(self):
        cursor = self.connection.connection.cursor()
        result = []

        sql = '''
            SELECT
            play.id,
            play.name,
            t_result.tournaments,
            t_result.points,
            t_result.wins
            FROM
            player play
            LEFT JOIN(
                SELECT
                tournament_result.player as player,
                COUNT(tournament_result.tournament) as tournaments,
                SUM(tournament_result.wins) as points,
                SUM(CASE WHEN tournament_result.winner = 1 THEN 1 ELSE 0 END) as wins
                FROM
                tournament_result
                INNER JOIN tournament ON tournament.id = tournament_result.tournament
                WHERE
                tournament.active = 1 AND
                tournament.season = (SELECT id FROM season WHERE active = 1)
                GROUP BY
                tournament_result.player
            ) t_result ON t_result.player = play.id
            ORDER BY
            play.name
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
    
    def GetPlayerCount(self):
        cursor = self.connection.connection.cursor()
        sql = '''SELECT COUNT(id) as count FROM player'''

        try:
            cursor.execute(sql)
            playerCount = cursor.fetchone()['count']
        except:
            playerCount = 0

        return playerCount
    
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