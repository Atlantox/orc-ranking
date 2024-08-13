from .BaseModel import BaseModel
from .TournamentModel import TournamentModel

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
    
    def GetPlayerStatistics(self, playerId, seasonId = None):
        tournamentModel = TournamentModel(self.connection)

        totalPoints = tournamentModel.GetTotalPointsOfSeason(seasonId)
        if type(totalPoints) is str():
            return totalPoints
        
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            COUNT(tournament_result.id) as tournaments,
            SUM(tournament_result.winner) as wins,
            SUM(tournament_result.wins) as points,
            ROUND((SUM(tournament_result.wins) * 100) / %s, 2) as points_percent
            FROM
            tournament_result
            INNER JOIN tournament ON tournament.id = tournament_result.tournament
            WHERE
            tournament_result.player = %s AND 
            tournament.active = 1
        '''
        args = [totalPoints, playerId]

        if seasonId is not None:
            sql += ' AND tournament.season = %s '
            args.append(seasonId)            

        sql += ' GROUP BY tournament.id '

        try:
            cursor.execute(sql, tuple(args))
            result = cursor.fetchone()
        except:
            result = 'Ocurrió un error al obtener las estadísticas del jugador solicitado'

        if result is None: 
            result = {
                'tournaments': 0,
                'wins': 0,
                'points': 0,
                'points_percent': 0
            }
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