from .BaseModel import BaseModel

class DeckModel(BaseModel):
    def GetDecks(self):
        cursor = self.connection.connection.cursor()
        result = []
        sql = "SELECT * FROM deck ORDER BY name"

        try:
            cursor.execute(sql)
            decks = cursor.fetchall()
        except:
            decks = False

        if decks != False:
            result = self.GetDecksWithColors(decks)
    
        return result

    def CreateDeck(self, deckData):
        name = deckData['name']
        colors = set(deckData['colors'])
        cursor = self.connection.connection.cursor()
        result = True

        sql = "INSERT INTO deck (name) VALUES (%s)"
        args = (name,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False

        if result == True:
            sql = "SELECT MAX(id) as id FROM deck"
            try:
                cursor.execute(sql)
                newDeck = cursor.fetchone()
                if newDeck is None:
                    result = 'Deck no encontrado'
            except:
                result = 'Ocurrió un error inesperado al obtener el deck creado'

        if result == True:
            result = self.AssignColorsToDeck(newDeck['id'], colors)            

        return result
    
    def GetDecksWithColors(self, decks):
        result = []
        for deck in decks:
            deckColors = self.GetColorsOfDeck(deck['id'])
            toAdd = {
                'id': deck['id'],
                'name': deck['name'],
                'colors': deckColors
            }
            result.append(toAdd)
        
        return result
    
    def GetColorsOfDeck(self, deckId):
        cursor = self.connection.connection.cursor()
        result = []
        sql = "SELECT color FROM deck_color WHERE deck = %s"
        args = (deckId,)
        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            result = [c['color'] for c in result]
        except:
            result = False

        return result
    
    def AssignColorsToDeck(self, deckId, colors):
        cursor = self.connection.connection.cursor()
        result = True
        try:
            sql = "INSERT INTO deck_color (deck, color) VALUES "
            listArgs = []
            for color in colors:
                sql +=  "(%s, %s),"
                listArgs += [deckId, color]

            sql = sql[0:-1]
            args = tuple(listArgs)
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = 'Ocurrió un error al asignar los colores al deck'

        return result
    
    def DeleteColorsOfDeck(self, deckId):
        cursor = self.connection.connection.cursor()
        sql = "DELETE FROM deck_color WHERE deck = %s"
        result = True

        try:
            cursor.execute(sql, (deckId,))
            self.connection.connection.commit()
        except:
            result = False
        
        return result
    
    def GetDeckByName(self, name):
        cursor = self.connection.connection.cursor()
        sql = "SELECT * FROM deck WHERE name = %s"
        args = (name,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
            result = self.GetDecksWithColors([result])
            if len(result) > 0:
                result = result[0]
        except:
            result = None
        
        return result
    
    def GetDeckById(self, id):
        cursor = self.connection.connection.cursor()
        sql = "SELECT * FROM deck WHERE id = %s"
        args = (id,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
            result = self.GetDecksWithColors([result])
            if len(result) > 0:
                result = result[0]
        except:
            result = None
        
        return result
    
    def UpdateDeck(self, deckId, deckData):
        cursor = self.connection.connection.cursor()
        result = True

        if 'name' in deckData:
            newName = deckData['name']
            sql = "UPDATE deck SET name = %s WHERE id = %s"
            args = (newName, deckId,)

            try:
                cursor.execute(sql, args)
                self.connection.connection.commit()
            except:
                result = 'Ocurrió un error al actualizar el nombre del deck'

        if result == True and 'colors' in deckData:
            deleted = self.DeleteColorsOfDeck(deckId)
            if deleted:
                result = self.AssignColorsToDeck(deckId, set(deckData['colors']))
            else:
                result = 'Ocurrió un error al borrar los colores anteriores del deck'
        
        return result
    
    def DeleteDeck(self, deckId):
        cursor = self.connection.connection.cursor()
        result = True

        sql = "DELETE FROM deck WHERE id = %s"
        args = (deckId,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        
        return result