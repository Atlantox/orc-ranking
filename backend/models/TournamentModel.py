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
        ORDER BY
        t.date DESC
        LIMIT 1
        '''
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
            tournamentColors = self.GetTournamentsColorPresence(lastTournament['id'])
            if tournamentColors is False:
                result = 'Ocurrió un error al obtener la presencia de colores del torneo'
        
        if result == True:
            result = {
                'data': lastTournament,
                'colors': tournamentColors,
                'results': tournamentResults
            }
        
        return result
    
    def GetTournamentById(self, tournamentId):
        cursor = self.connection.connection.cursor()
        sql = "SELECT * FROM tournament WHERE id = %s"
        args = (tournamentId,)
        result = True

        try:
            cursor.execute(sql, args)
            targetTournament = cursor.fetchone()
        except:
            result = 'Hubo un error al obtener el torneo solicitado'

        if result == True:
            if targetTournament is None:
                result = 'No se encontró el torneo solicitado'

        if result == True:
            tournamentResults = self.GetTournamentResults(targetTournament['id'])
            if tournamentResults is False:
                result = 'Ocurrió un error al obtener los resultados del torneo'

        if result == True:
            tournamentColors = self.GetTournamentsColorPresence(targetTournament['id'])
            if tournamentColors is False:
                result = 'Ocurrió un error al obtener la presencia de colores del torneo'
        
        if result == True:
            result = {
                'data': targetTournament,
                'colors': tournamentColors,
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

    def GetTournamentsColorPresence(self, tournamentId):
        cursor = self.connection.connection.cursor()
        result = []
        sql = '''
            SELECT 
            color.name as color,
            COUNT(color.name) as quantity
            FROM
            color
            INNER JOIN deck_color ON deck_color.color = color.name
            INNER JOIN deck ON deck.id = deck_color.deck
            INNER JOIN tournament_result ON tournament_result.deck = deck.id
            WHERE
            tournament_result.tournament = %s
            GROUP BY
            color.name
            ORDER BY quantity DESC'''
        
        try:
            cursor.execute(sql, (tournamentId,))
            colors = cursor.fetchall()

            totalColors = 0
            for color in colors:
                totalColors += color['quantity']
            
            to_add = {}
            for color in colors:
                to_add = color
                percent = (color['quantity'] * 100) / totalColors
                to_add['percent'] = round(percent, 2)
                result.append(to_add)

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

    def GetTournamentsAndParticipantsCountOfSeason(self, seasonId):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            COUNT(tournament.id) as count
            FROM
            tournament
            WHERE
            tournament.active = 1 AND
            tournament.season = %s'''

        try:
            cursor.execute(sql, (seasonId,))
            tournamentsCount = cursor.fetchone()['count']
        except:
            tournamentsCount = 0
        
        sql = '''
            SELECT
            COUNT(tournament_result.id) as count
            FROM
            tournament_result
            INNER JOIN tournament ON tournament.id = tournament_result.tournament
            WHERE
            tournament.active = 1 AND
            tournament.season = %s'''
        
        try:
            cursor.execute(sql, (seasonId,))
            participantCounts = cursor.fetchone()['count']
        except:
            participantCounts = 0

        result = {
            'tournaments': tournamentsCount,
            'participants': participantCounts
        }
        
        return result
    
    def GetTournamentsRankingOfSeason(self, seasonId):
        cursor = self.connection.connection.cursor()
        error = ''
        # Getting the total points in tournaments of the season
        sql = '''
            SELECT
            SUM(tournament_result.wins) as total_wins
            FROM
            tournament_result
            INNER JOIN tournament ON tournament.id = tournament_result.tournament
            WHERE
            tournament.season = %s
        '''
        args = (seasonId,)

        try:
            cursor.execute(sql, args)
            totalWins = cursor.fetchone()['total_wins']
        except:
            error = 'Ocurrió un error al traer la suma total de puntos'

        if error == '':
            sql = '''
            SELECT
            player.name,
            ROUND((SUM(tournament_result.wins) * 100) / %s, 2) as percent
            FROM
            tournament_result
            INNER JOIN tournament ON tournament.id = tournament_result.tournament
            INNER JOIN player ON player.id = tournament_result.player
            WHERE
            tournament.season = %s
            GROUP BY
            tournament_result.player
            ORDER BY 
            percent DESC
            '''
        args = (totalWins, seasonId,)

        try:
            cursor.execute(sql, args)
            playerPoints = cursor.fetchall()
        except:
            error = 'Ocurrió un error al traer los puntos de cada jugador'

        if error == '':
            sql = '''
            SELECT
            deck.name,
            ROUND((SUM(tournament_result.wins) * 100) / %s, 2) as percent
            FROM
            tournament_result
            INNER JOIN tournament ON tournament.id = tournament_result.tournament
            INNER JOIN deck ON deck.id = tournament_result.deck
            WHERE
            tournament.season = %s
            GROUP BY
            tournament_result.deck
            ORDER BY 
            percent DESC
            '''
        args = (totalWins, seasonId,)
        
        try:
            cursor.execute(sql, args)
            deckPoints = cursor.fetchall()
        except:
            error = 'Ocurrió un error al traer los puntos de cada mazo'


        if error == '':
            sql = '''
            SELECT
            deck_color.color,
            ROUND((SUM(tournament_result.wins) * 100) / %s, 2) as percent
            FROM
            tournament_result
            INNER JOIN tournament ON tournament.id = tournament_result.tournament
            INNER JOIN deck ON deck.id = tournament_result.deck
            INNER JOIN deck_color ON deck_color.deck = deck.id
            WHERE
            tournament.season = %s
            GROUP BY
            deck_color.color
            ORDER BY 
            percent DESC
            '''
        args = (totalWins, seasonId,)
        
        try:
            cursor.execute(sql, args)
            colorPoints = cursor.fetchall()
        except:
            error = 'Ocurrió un error al traer los puntos de cada mazo'


        if error == '':
            result = {
                'players': playerPoints,
                'decks': deckPoints,
                'colors': colorPoints
            }
        else:
            result = error

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