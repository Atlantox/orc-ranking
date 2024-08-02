from .BaseModel import BaseModel

class TournamentModel(BaseModel):

    def CreateTournament(self, tournamentData):
        cursor = self.connection.connection.cursor()
        result = True
        tournamentDate = tournamentData['date']
        targetFormat = tournamentData['format']
        targetSeason = tournamentData['season']
        sql= "INSERT INTO tournament (date, format, season) VALUES (%s, %s, %s)"
        args = (tournamentDate, targetFormat, targetSeason)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = 'Hubo un error al crear el torneo'

        if result == True:
            sql = "SELECT MAX(id) as id FROM tournament"
            try:
                cursor.execute(sql)
                targetTournament = cursor.fetchone()
            except:
                result = 'Hubo un error al encontrar el torneo creado'

        
        if result == True:
            # Creating the tournaments results
            result = self.CreateTournamentResults(targetTournament['id'], tournamentData['participants'])

        return result

    def GetTournaments(self):
        cursor = self.connection.connection.cursor()
        sql = '''
        SELECT
            t.id,
            CONCAT(YEAR(t.date), '-', LPAD(MONTH(t.date), 2, '0'), '-', LPAD(DAY(t.date), 2, '0')) AS date, 
            t.format,
            w.name AS winner,
            p.participants
        FROM
            tournament t
        INNER JOIN (
            SELECT
                tr.tournament,
                COUNT(tr.id) AS participants
            FROM
                tournament_result tr
            GROUP BY
                tr.tournament
        ) p ON t.id = p.tournament
        INNER JOIN (
            SELECT
                tr.tournament,
                CONCAT(pl.name, ' - ', dc.name) as name
            FROM
                tournament_result tr
            INNER JOIN player pl ON tr.player = pl.id
            INNER JOIN deck dc ON dc.id = tr.deck
            WHERE
                tr.winner = 1
        ) w ON t.id = w.tournament
        WHERE
            t.season = (SELECT id FROM season WHERE active = 1) AND
            t.active = 1
        '''

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            result = False
        
        return result
    
    def GetLastTournament(self):
        cursor = self.connection.connection.cursor()
        sql = "select MAX(id) as id, date, format, season, active from tournament WHERE active = 1"
        result = True

        try:
            cursor.execute(sql)
            lastTournament = cursor.fetchone()
        except:
            result = 'Hubo un error al obtener el último torneo'

        if result == True:
            tournamentResults = self.GetTournamentResults(lastTournament['id'])
            if tournamentResults is False:
                result = 'Ocurrió un error al obtener los resultados del torneo'
        
        if result == True:
            result = {
                'data': lastTournament,
                'results': tournamentResults
            }
        
        return result

    def GetTournamentResults(self, tournamentId):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            player.name as player,
            deck.name as deck,
            tournament_result.wins,
            tournament_result.winner
            FROM 
            tournament_result
            INNER JOIN player ON player.id = tournament_result.player
            INNER JOIN deck ON deck.id = tournament_result.deck
            WHERE
            tournament_result.tournament = %s
            ORDER BY
            tournament_result.winner DESC,
            tournament_result.wins DESC
        '''

        try:
            cursor.execute(sql, (tournamentId,))
            result = cursor.fetchall()
        except:
            result = False

        return result       
    
    def GetTournamentsAndParticipantsCount(self):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            COUNT(tournament.id) as count
            FROM
            tournament
            INNER JOIN season ON season.id = tournament.season
            WHERE
            tournament.active = 1 AND
            season.active = 1'''

        try:
            cursor.execute(sql)
            tournamentsCount = cursor.fetchone()['count']
        except:
            tournamentsCount = 0
        
        sql = '''
            SELECT
            COUNT(tournament_result.id) as count
            FROM
            tournament_result
            INNER JOIN tournament ON tournament.id = tournament_result.tournament
            INNER JOIN season ON season.id = tournament.season
            WHERE
            tournament.active = 1 AND
            season.active = 1'''
        
        try:
            cursor.execute(sql)
            participantCounts = cursor.fetchone()['count']
        except:
            participantCounts = 0

        result = {
            'tournaments': tournamentsCount,
            'participants': participantCounts
        }
        
        return result

    
    def GetTournamentsOfDeck(self, deckId):
        cursor = self.connection.connection.cursor()

        sql = '''SELECT 
        tournament.id
        FROM 
        tournament
        INNER JOIN tournament_result ON tournament_result.tournament = tournament.id
        WHERE
        tournament_result.deck = %s AND
        tournament.active = 1
        '''
        args = (deckId,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result

    def GetTournamentsOfPlayer(self, playerId):
        cursor = self.connection.connection.cursor()

        sql = '''SELECT 
        tournament.id
        FROM 
        tournament
        INNER JOIN tournament_result ON tournament_result.tournament = tournament.id
        WHERE
        tournament_result.player = %s AND
        tournament.active = 1'''
        args = (playerId,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result

    def GetTournamentsOfFormat(self, formatId):
        cursor = self.connection.connection.cursor()

        sql = '''SELECT 
        tournament.id
        FROM 
        tournament
        INNER JOIN tournament_result ON tournament_result.tournament = tournament.id
        WHERE
        tournament.format = %s AND
        tournament.active = 1'''
        args = (formatId,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result

    def GetTournamentsOfSeason(self, seasonId):
        cursor = self.connection.connection.cursor()

        sql = '''SELECT 
        tournament.id
        FROM 
        tournament
        INNER JOIN tournament_result ON tournament_result.tournament = tournament.id
        WHERE
        tournament.season = %s AND
        tournament.active = 1'''
        args = (seasonId,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result
    
    def CreateTournamentResults(self, tournamentId, participants):
        cursor = self.connection.connection.cursor()
        result = True

        listArgs = []
        sql = "INSERT INTO tournament_result (tournament, player, deck, wins, winner) VALUES "
        for participant in participants:
            sql += "(%s, %s, %s, %s, %s),"
            listArgs += [tournamentId, participant['player'], participant['deck'], participant['wins'], participant['winner']]

        args = tuple(listArgs)
        sql = sql[0:-1]
        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = 'Hubo un error al crear los resultados del torneo'
        
        return result

    def DeactivateTournament(self,tournamentId):
        cursor = self.connection.connection.cursor()
        sql = "UPDATE tournament SET active = 0 WHERE id = %s"
        result = True

        try:
            cursor.execute(sql, (tournamentId,))
            self.connection.connection.commit()
        except:
            result = False
        
        return result