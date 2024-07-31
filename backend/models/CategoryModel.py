from .BaseModel import BaseModel

class CategoryModel(BaseModel):
    def GetCategories(self):
        cursor = self.connection.connection.cursor()
        sql = "SELECT * FROM category"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def GetCategoryNames(self):
        ''' Return a list of the names of all categories '''
        cursor = self.connection.connection.cursor()
        sql = "SELECT name FROM category"
        cursor.execute(sql)
        categories = cursor.fetchall()
        categoryNames = []
        if categories is not None:
            categoryNames = [c['name'] for c in categories]

        return categoryNames
            

    def CreateCategory(self, categoryData):
        name = categoryData['name']
        cursor = self.connection.connection.cursor()
        result = True

        sql = "INSERT INTO category (name) VALUES (%s)"
        args = (name,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False

        return result
    
    def GetCategoryByName(self, name):
        cursor = self.connection.connection.cursor()

        sql = "SELECT * FROM category WHERE name = %s"
        args = (name,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        except:
            result = None
        
        return result
    
    def GetCategoryById(self, id):
        cursor = self.connection.connection.cursor()

        sql = "SELECT * FROM category WHERE id = %s"
        args = (id,)

        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        except:
            result = None
        
        return result
    
    def GetCategoriesByIdList(self, categoryIds):
        cursor = self.connection.connection.cursor()

        sql = "SELECT * FROM category WHERE id IN (" + ('%s,' * len(categoryIds))[:-1] + ')'
        args = tuple(categoryIds)

        try:
            cursor.execute(sql, args,)
            result = cursor.fetchall()
        except:
            result = None
        
        return result

    def AddCategoriesToBook(self, bookId, categories):
        cursor = self.connection.connection.cursor()
        result = True

        arrayValues = []
        sql = "INSERT INTO book_category (book, category) VALUES "
        for category in categories:
            sql += "(%s, %s),"
            arrayValues.append(bookId)
            arrayValues.append(category)
        
        sql = sql[0:-1]  # Skipping the last comma

        try:
            cursor.execute(sql, tuple(arrayValues))
            self.connection.connection.commit()
        except:
            result = False

        return result

    def GetCategoriesOfBook(self, id):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            category.id,
            category.name
            FROM
            category
            INNER JOIN book_category ON book_category.category = category.id
            INNER JOIN book ON book.id = book_category.book
            WHERE
            book.id = %s
            '''
        
        args = (id,)

        try:
            cursor.execute(sql, args)
            categories = cursor.fetchall()
        except:
            categories = None

        if categories is None:
            categories = []
        
        ordered_categories = []
        for category in categories:
            ordered_categories.append(category)
        
        return ordered_categories
    
    def CategoriesExists(self, ids):
        ''' Gets a list of Ids and check if all exists, if not return false'''
        cursor = self.connection.connection.cursor()
        orderedIds = ''
        arrayIds = []
        
        orderedIds = orderedIds[0:-1]
        sql = "SELECT * FROM category WHERE id IN ("
        for id in ids:
            sql += "%s,"
            arrayIds.append(id)
        sql = sql[0:-1] + ')'

        try:
            cursor.execute(sql, tuple(arrayIds))
            categories = cursor.fetchall()
        except:
            categories = None

        if categories is None:
            result = False
        else:
            result = len(categories) == len(ids)

        return result
    
    def UpdateCategory(self, categoryId, categoryData):
        newName = categoryData['name']
        cursor = self.connection.connection.cursor()
        result = True

        sql = "UPDATE category SET name = %s WHERE id = %s"
        args = (newName, categoryId,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        
        return result
    
    def UpdateCategoriesOfBook(self, bookId, categories):
        cursor = self.connection.connection.cursor()
        result = True

        sql = "DELETE FROM book_category WHERE book = %s"
        args = (bookId,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
            self.AddCategoriesToBook(bookId, categories)
        except:
            result = False

        return result
    
    def DeleteCategory(self, categoryId):
        cursor = self.connection.connection.cursor()
        result = True

        sql = "DELETE FROM category WHERE id = %s"
        args = (categoryId,)

        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        
        return result