from .BaseModel import BaseModel

class TournamentModel(BaseModel):
    GET_TOURNAMENTS_TEMPLATE = '''
        SELECT
            t.id,
            CONCAT(YEAR(t.date), '-', LPAD(MONTH(t.date), 2, '0'), '-', LPAD(DAY(t.date), 2, '0')) AS date, 
            t.format,
            t.observation,
            t.pot,
            s.name as season,
            w.name AS winner,
            p.participants,
            t.active
        FROM
            tournament t
        INNER JOIN season s ON s.id = t.season
        INNER JOIN tournament_result tr ON tr.tournament = t.id
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
        ) w ON t.id = w.tournament'''

    def CreateTournament(self, tournamentData):
        cursor = self.connection.connection.cursor()
        result = True
        tournamentDate = tournamentData['date']
        targetFormat = tournamentData['format']
        targetSeason = tournamentData['season']
        tournamentObservation = tournamentData['observation']
        tournamentPot = tournamentData['pot']

        sql= "INSERT INTO tournament (date, format, observation, pot, season) VALUES (%s, %s, %s, %s, %s)"
        args = (tournamentDate, targetFormat, tournamentObservation, tournamentPot, targetSeason)

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

    def GetCurrentTournaments(self):
        cursor = self.connection.connection.cursor()
        sql = self.GET_TOURNAMENTS_TEMPLATE + '''
        WHERE
        t.season = (SELECT id FROM season WHERE active = 1) AND
        t.active = 1
        GROUP BY
        t.id
        ORDER BY 
        t.date DESC
        '''        

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            result = False
        
        return result
    
    def GetTournamentsOfSeason(self, seasonId):
        cursor = self.connection.connection.cursor()
        sql = self.GET_TOURNAMENTS_TEMPLATE + '''
        WHERE
        t.season = %s AND
        t.active = 1
        GROUP BY
        t.id
        ORDER BY 
        t.date DESC
        '''  

        args = (seasonId,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result
    
    def GetInactiveTournaments(self):
        cursor = self.connection.connection.cursor()
        sql = self.GET_TOURNAMENTS_TEMPLATE + '''
        WHERE
        t.active = 0
        GROUP BY
        t.id
        ORDER BY 
        t.date DESC
        '''  

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result
    
    def GetInactiveTournamentsOfSeason(self, seasonId):
        cursor = self.connection.connection.cursor()
        sql = self.GET_TOURNAMENTS_TEMPLATE + '''
        WHERE
        t.active = 0 AND
        t.season = %s
        GROUP BY
        t.id
        ORDER BY 
        t.date DESC
        '''  

        try:
            cursor.execute(sql, (seasonId,))
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result
    
    def GetActiveTournaments(self):
        cursor = self.connection.connection.cursor()
        sql = self.GET_TOURNAMENTS_TEMPLATE + '''
        WHERE
        t.active = 1
        GROUP BY
        t.id
        ORDER BY 
        t.date DESC
        '''  

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result
    
    def GetAllTournaments(self):
        cursor = self.connection.connection.cursor()
        sql = self.GET_TOURNAMENTS_TEMPLATE + ' GROUP BY t.id ORDER BY t.date DESC'

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result
    
    def GetAllTournamentsOfSeason(self, seasonId):
        cursor = self.connection.connection.cursor()
        sql = self.GET_TOURNAMENTS_TEMPLATE + ' WHERE t.season = %s GROUP BY t.id ORDER BY t.date DESC'

        try:
            cursor.execute(sql, (seasonId,))
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result
    
    def GetAllTournamentsOfSeason(self, seasonId):
        cursor = self.connection.connection.cursor()
        sql = self.GET_TOURNAMENTS_TEMPLATE + ' WHERE t.season = %s GROUP BY t.id ORDER BY t.date DESC'

        try:
            cursor.execute(sql, (seasonId,))
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result
    
    def GetActiveTournamentsOfPlayer(self, playerId, seasonId):
        cursor = self.connection.connection.cursor()
        sql = self.GET_TOURNAMENTS_TEMPLATE + ' WHERE t.active = 1 AND tr.player = %s GROUP BY t.id ORDER BY t.date DESC'
        args = [playerId]
        if seasonId is not None:
            sql += 'AND s.id = %s'
            args.append(seasonId)

        try:
            cursor.execute(sql, tuple(args))
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result
    
    def GetLastTournament(self):
        cursor = self.connection.connection.cursor()
        sql = self.GET_TOURNAMENTS_TEMPLATE + '''
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
            if lastTournament is None:
                result = []
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
        sql = self.GET_TOURNAMENTS_TEMPLATE +  '''
            WHERE
            t.id = %s
        '''
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

    def GetTournamentResultsOfPlayer(self, playerId, seasonId = None):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            tournament.id,
            CONCAT(YEAR(tournament.date), '-', LPAD(MONTH(tournament.date), 2, '0'), '-', LPAD(DAY(tournament.date), 2, '0')) AS date, 
            tournament.format,
            tournament.season,
            tournament.active,
            tournament.observation,
            player.name as player,
            deck.name as deck,
            tournament_result.wins,
            tournament_result.winner
            FROM 
            tournament
            INNER JOIN tournament_result ON tournament_result.tournament = tournament.id
            INNER JOIN player ON player.id = tournament_result.player
            INNER JOIN deck ON deck.id = tournament_result.deck
            WHERE
            tournament_result.player = %s AND
            tournament.active = 1
        '''

        args = [playerId]

        if seasonId is not None:
            sql += ' AND tournament.season = %s'
            args.append(seasonId)

        try:
            cursor.execute(sql, tuple(args))
            results = cursor.fetchall()
        except:
            results = False

        return results
    
    def GetTournamentResultsOfDeck(self, deckId, seasonId = None):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            tournament.id,
            CONCAT(YEAR(tournament.date), '-', LPAD(MONTH(tournament.date), 2, '0'), '-', LPAD(DAY(tournament.date), 2, '0')) AS date, 
            tournament.format,
            tournament.season,
            tournament.active,
            tournament.observation,
            player.name as player,
            deck.name as deck,
            tournament_result.wins,
            tournament_result.winner
            FROM 
            tournament
            INNER JOIN tournament_result ON tournament_result.tournament = tournament.id
            INNER JOIN player ON player.id = tournament_result.player
            INNER JOIN deck ON deck.id = tournament_result.deck
            WHERE
            tournament_result.deck = %s AND
            tournament.active = 1
        '''

        args = [deckId]

        if seasonId is not None:
            sql += ' AND tournament.season = %s'
            args.append(seasonId)

        try:
            cursor.execute(sql, tuple(args))
            results = cursor.fetchall()
        except:
            results = False

        return results
    
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

    def GetTournamentsAndParticipantsCountOfSeason(self, seasonId):
        cursor = self.connection.connection.cursor()
        sql = ''' SELECT COUNT(tournament.id) as count FROM tournament WHERE tournament.active = 1 '''
        seasonFilter = seasonId is not None

        if seasonFilter:
            sql += ' AND tournament.season = %s'
            args = (seasonId,)

        try:
            if seasonFilter:
                cursor.execute(sql, args)
            else:
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
            WHERE
            tournament.active = 1'''
            
        if seasonFilter:
            sql += ' AND tournament.season = %s '

        try:
            if seasonFilter:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)
            participantCounts = cursor.fetchone()['count']
        except:
            participantCounts = 0

        result = {
            'tournaments': tournamentsCount,
            'participants': participantCounts
        }
        
        return result
    
    def GetTournamentsRankingOfSeasonAndFormat(self, seasonId, targetFormat):
        cursor = self.connection.connection.cursor()
        error = ''

        totalWins = self.GetTotalPointsOfSeason(seasonId, targetFormat)
        if type(totalWins) is str:
            error = totalWins

        
        # Getting the points by player
        if error == '':
            args = (totalWins, seasonId, targetFormat['name'],)
            sql = '''
            SELECT
            player.name,
            ROUND((SUM(tournament_result.wins) * 100) / %s, 2) as percent
            FROM
            tournament_result
            INNER JOIN tournament ON tournament.id = tournament_result.tournament
            INNER JOIN player ON player.id = tournament_result.player
            WHERE
            tournament.active = 1 AND 
            tournament.season = %s AND
            tournament.format = %s
            GROUP BY
            tournament_result.player
            ORDER BY 
            percent DESC
            '''

        try:
            cursor.execute(sql, args)
            playerPoints = cursor.fetchall()
        except:
            error = 'Ocurrió un error al traer los puntos de cada jugador'

        # Getting the points by deck
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
            tournament.active = 1 AND 
            tournament.season = %s AND
            tournament.format = %s
            GROUP BY
            tournament_result.deck
            ORDER BY 
            percent DESC
            '''
        
        try:
            cursor.execute(sql, args)
            deckPoints = cursor.fetchall()
        except:
            error = 'Ocurrió un error al traer los puntos de cada mazo'


        # Getting the points by color
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
            tournament.active = 1 AND 
            tournament.season = %s AND
            tournament.format = %s
            GROUP BY
            deck_color.color
            ORDER BY 
            percent DESC
            '''
        
        try:
            cursor.execute(sql, args)
            colorPoints = cursor.fetchall()
        except:
            error = 'Ocurrió un error al traer los puntos de cada color'


        if error == '':
            result = {
                'players': playerPoints,
                'decks': deckPoints,
                'colors': colorPoints
            }
        else:
            result = error

        return result    
    
    def GetSeasonStatistics(self, seasonId):
        cursor = self.connection.connection.cursor()
        args = (seasonId, )
        error = ''
        seasonSQL = ' AND tournament.season = %s '

        # Getting tournament counts by format
        sql = '''
            SELECT 
            COUNT(tournament.id) as count,
            tournament.format
            FROM
            tournament
            WHERE
            tournament.active = 1
        ''' + seasonSQL + '''
            GROUP BY
            tournament.format            
        '''

        try:
            cursor.execute(sql, args)
            tournamentsByFormat = cursor.fetchall()

        except:
            error = 'Hubo un error al obtener los torneos por formato'

        if error == '':
            # Getting participants by format
            sql = '''
                SELECT 
                COUNT(tournament_result.player) as count,
                tournament.format
                FROM
                tournament_result
                INNER JOIN tournament ON tournament.id = tournament_result.tournament
                WHERE
                tournament.active = 1
            ''' + seasonSQL + '''
                GROUP BY
                tournament.format
            '''

            try:
                cursor.execute(sql, args)
                participantsByFormat = cursor.fetchall()

            except:
                error = 'Hubo un error al obtener los participantes por formato'


        if error == '':
            # Getting persons by format
            sql = '''
                SELECT
                COUNT(DISTINCT tournament_result.player) as count,
                tournament.format
                FROM
                tournament_result
                INNER JOIN tournament ON tournament.id = tournament_result.tournament
                WHERE
                tournament.active = 1
            ''' + seasonSQL + '''
                GROUP BY
                tournament.format
            '''
            try:
                cursor.execute(sql, args)
                personsByFormat = cursor.fetchall()

            except:
                error = 'Hubo un error al obtener las personas por formato'
        
        if error != '':
            result = error
        else:
            result = {
                'tournaments': tournamentsByFormat,
                'participants': participantsByFormat,
                'persons': personsByFormat
            }

        return result
    
    def GetTotalPotOfSeason(self, seasonId, formatId):
        cursor = self.connection.connection.cursor()
        sql = '''
        SELECT 
        SUM(tournament.pot) as pot 
        FROM
        tournament 
        INNER JOIN game_format ON game_format.name = tournament.format
        WHERE 
        tournament.season = %s AND 
        game_format.id = %s
        '''

        args = (seasonId, formatId)
        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()

            if result is None:
                result = 0        
            else:
                result = result['pot']        
        except:
            result = 'Ocurrió un error al traer el número de jugadores individuales' 

        return result


    def GetTournamentsIndividualPlayersOfSeason(self, seasonId):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT DISTINCT
            player.id
            FROM
            player
            INNER JOIN tournament_result ON tournament_result.player = player.id
            INNER JOIN tournament ON tournament.id = tournament_result.tournament     
            WHERE
            tournament.active = 1     
        '''

        if seasonId is not None:
            sql += ' AND tournament.season = %s '


        try:
            if seasonId is not None:
                args = (seasonId,)
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)

            players = cursor.fetchall()

            if players is None:
                players = 0
            else:
                players = len(players)
                
        except:
            players = 'Ocurrió un error al traer el número de jugadores individuales' 

        return players

    def GetTotalPointsOfSeason(self, seasonId, targetFormat = None):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            SUM(tournament_result.wins) as total_wins
            FROM
            tournament_result
            INNER JOIN tournament ON tournament.id = tournament_result.tournament
            WHERE
            1 
        '''

        args = []
        
        if seasonId is not None:
            sql += ' AND tournament.season = %s '
            args.append(seasonId)

        if targetFormat is not None:
            sql += ' AND tournament.format = %s '
            args.append(targetFormat['name'])

        try:
            if [seasonId, targetFormat] == [None, None]:
                cursor.execute(sql)
            else:
                args = tuple(args)
                cursor.execute(sql, args)

            totalWins = cursor.fetchone()['total_wins']

            if totalWins is None:
                totalWins = 0
        except:
            totalWins = 'Ocurrió un error al traer la suma total de puntos' 

        return totalWins

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
 
    def CreateTournamentResults(self, tournamentId, participants):
        cursor = self.connection.connection.cursor()
        result = True

        listArgs = []
        sql = "INSERT INTO tournament_result (tournament, player, deck, wins, winner) VALUES "
        for participant in participants:
            sql += "(%s, %s, %s, %s, %s),"
            listArgs += [tournamentId, participant['player'], participant['deck'], float(participant['wins']), participant['winner']]

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