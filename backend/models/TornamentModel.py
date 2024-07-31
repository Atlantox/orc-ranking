from .BaseModel import BaseModel

class TournamentModel(BaseModel):
    def GetTournaments(self):
        cursor = self.connection.connection.cursor()
        sql = "SELECT * FROM tournament"

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

    def CreateReader(self, readerData):
        cursor = self.connection.connection.cursor()
        result = True

        sql = '''
            INSERT INTO
            reader
            (
                cedula,
                names,
                surnames,
                gender,
                birthdate,
                phone,
                is_teacher
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            '''
        args = (
            readerData['cedula'],
            readerData['names'],
            readerData['surnames'],
            readerData['gender'],
            readerData['birthdate'],
            readerData['phone'],
            readerData['is_teacher']
        )
                
        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False

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
    
    def UpdateReader(self, readerId, readerData):
        result = True
        cursor = self.connection.connection.cursor()
        arrayValues = []
        sql = "UPDATE reader SET "
        for column, value in readerData.items():
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