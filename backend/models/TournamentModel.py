from .BaseModel import BaseModel

class TournamentModel(BaseModel):

    def GetTournaments(self):
        cursor = self.connection.connection.cursor()
        sql = '''
        SELECT
        tournament.date,
        tournament.season,
        tournament.format,
        player.name as winner
        FROM
        tournament
        INNER JOIN tournament_result ON tournament_result.tournament = tournament.id
        INNER JOIN player ON player.id = tournament_result.player
        WHERE
        tournament_result.winner = 1
        '''

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            result = False
        
        return result
    
    def GetTournamentsOfDeck(self, deckId):
        cursor = self.connection.connection.cursor()

        sql = '''SELECT 
        tournament.id
        FROM 
        tournament
        INNER JOIN tournament_result ON tournament_result.tournament = tournament.id
        WHERE
        tournament_result.deck = %s'''
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
        tournament_result.player = %s'''
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
        tournament.format = %s'''
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
        tournament.season = %s'''
        args = (seasonId,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            if result == tuple():
                result = []
        except:
            result = None
        
        return result

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

    
    def GetReaderByCedula(self, cedula):
        cursor = self.connection.connection.cursor()

        sql = '''
            SET @percent = %;
            SELECT
            id,
            cedula,
            names,
            surnames,
            gender,
            phone,
            is_teacher,
            CONCAT(YEAR(birthdate), '-', LPAD(MONTH(birthdate), 2, '0'), '-', LPAD(DAY(birthdate), 2, '0')) AS birthdate 
            FROM
            reader
            WHERE
            cedula = %s
            '''
        args = (cedula,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        except:
            result = None
        
        return result
    
    def GetReaderById(self, id):
        cursor = self.connection.connection.cursor()

        sql = '''
            SELECT
            id,
            cedula,
            names,
            surnames,
            gender,
            phone,
            is_teacher,
            CONCAT(YEAR(birthdate), '-', LPAD(MONTH(birthdate), 2, '0'), '-', LPAD(DAY(birthdate), 2, '0')) AS birthdate 
            FROM
            reader
            WHERE
            id = %s
            '''
        args = (id,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        except:
            result = None
        
        return result
    
    def UpdateReader(self, readerId, tournamentData):
        result = True
        cursor = self.connection.connection.cursor()
        arrayValues = []
        sql = "UPDATE reader SET "
        for column, value in tournamentData.items():
            sql += "{0} = %s,".format(column)
            arrayValues.append(value)
        
        sql = sql[0:-1] + " WHERE id = %s"
        arrayValues.append(readerId)
        args = tuple(arrayValues)
        
        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        
        return result
    
    def DeleteReader(self, readerId):
        result = True
        cursor = self.connection.connection.cursor()
        result = True
        
        sql = "DELETE FROM reader WHERE id = %s"
        args = (readerId,)
        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        
        return result