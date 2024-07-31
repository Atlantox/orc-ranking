from argon2 import PasswordHasher
from uuid import uuid4

from .BaseModel import BaseModel

class UserModel(BaseModel):
    def CreateUser(self, userData):
        cursor = self.connection.connection.cursor()
        result = True
        newToken = self.GetNewToken()
        hasher = PasswordHasher()
        sql = '''
                INSERT INTO
                user
                (
                    nickname,
                    username,
                    password,
                    level,
                    token
                )
                VALUES
                (
                    '{0}',
                    '{1}',
                    '{2}',
                    '{3}',
                    '{4}'
                )
                '''.format(
                    userData['nickname'],
                    hasher.hash(userData['username']),
                    hasher.hash(userData['password']),
                    userData['level'],
                    newToken
                )
        try:
            cursor.execute(sql)
            self.connection.connection.commit()
        except:
            result = False

        return result

    def GetUserByToken(self, token):
        '''
        Obtain the request, check if the token exists and if the user exists
        '''
        if token is not None:
            cursor = self.connection.connection.cursor()
            sql = "SELECT * FROM user WHERE token = '{0}'".format(token)
            cursor.execute(sql)
            user = cursor.fetchone()

            if user is None:
                result = 'Usuario no encontrado'
            else:
                result = user
        else:
            result = 'Authenticación requerida'
        
        return result
    
    def GetNewToken(self):
        tentativeToken = '{0}-{1}'.format(uuid4(), uuid4())
        cursor = self.connection.connection.cursor()
        sql = "SELECT token FROM user WHERE token = '{0}'"
        cursor.execute(sql.format(tentativeToken))
        tokenExists = cursor.fetchone()

        # Creamos tokens hasta que creemos uno único que no exista
        while tokenExists is not None:
            tentativeToken = '{0}-{1}'.format(uuid4(), uuid4())
            cursor.execute(sql.format(tentativeToken))
            tokenExists = cursor.fetchone()

        return tentativeToken
    
    def GetUsersPublicData(self):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT 
            id, 
            nickname, 
            level, 
            CONCAT(YEAR(created_at), '-', LPAD(MONTH(created_at), 2, '0'), '-', LPAD(DAY(created_at), 2, '0')) AS created_at, 
            active 
            FROM 
            user'''
        
        cursor.execute(sql,)
        users = cursor.fetchall()
        return users
    
    def GetUserPublicData(self, token):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT 
            id, 
            nickname, 
            level, 
            CONCAT(YEAR(created_at), '-', LPAD(MONTH(created_at), 2, '0'), '-', LPAD(DAY(created_at), 2, '0')) AS created_at, 
            active 
            FROM 
            user
            WHERE token = %s'''
        
        cursor.execute(sql, (token,))
        targetUser = cursor.fetchone()
        targetUser['permissons'] = self.GetUserPermissons(token)
        return targetUser
    
    def GetUserById(self, id):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT 
            id, 
            nickname, 
            level, 
            CONCAT(YEAR(created_at), '-', LPAD(MONTH(created_at), 2, '0'), '-', LPAD(DAY(created_at), 2, '0')) AS created_at, 
            active 
            FROM 
            user
            WHERE id = %s'''
        
        cursor.execute(sql, (id,))
        targetUser = cursor.fetchone()
        return targetUser
    
    def GetUserPermissons(self, token):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            permisson.name
            FROM
            permisson
            INNER JOIN user ON user.level = permisson.level
            WHERE
            user.token = %s

        '''
        
        cursor.execute(sql, (token,))
        permissons = cursor.fetchall()

        result = []
        if permissons is not None:
            for permisson in permissons:
                result.append(permisson['name'])
        else:
            result = None
        return result

    def UsernameExists(self, recievedUsername):
        cursor = self.connection.connection.cursor()
        hasher = PasswordHasher()

        sql = "SELECT username FROM user"
        cursor.execute(sql)
        usernames = cursor.fetchall()
        found = False

        if usernames is not None:
            for user in usernames:
                if found: break

                try:
                    hasher.verify(user['username'], recievedUsername)
                    found = True
                    break
                except Exception as err:
                    pass

        return found
    
    def NicknameExists(self, nickname):
        cursor = self.connection.connection.cursor()

        sql = "SELECT nickname FROM user WHERE nickname = %s"
        args = (nickname,)
        cursor.execute(sql, args)
        targetUser = cursor.fetchone()
        found = targetUser is not None

        return found
    
    def TryLogin(self, username, password):
        cursor = self.connection.connection.cursor()
        hasher = PasswordHasher()
        sql = "SELECT username, password, token FROM user"
        cursor.execute(sql)
        users = cursor.fetchall()
        result = False

        if users is not None:
            for user in users:
                if result: break

                try:
                    hasher.verify(user['username'], username)
                    hasher.verify(user['password'], password)
                    result = user['token']
                    break
                except Exception as err:
                    pass

        return result
    
    def UserHasPermisson(self, userId, permisson):
        cursor = self.connection.connection.cursor()
        sql = '''
            SELECT
            permisson.name
            FROM
            permisson
            INNER JOIN user_level ON user_level.name = permisson.level
            INNER JOIN user ON user.level = user_level.name
            WHERE
            user.id = '{0}' AND
            permisson.name = '{1}'
            '''.format(userId, permisson)

        cursor.execute(sql)
        result = cursor.fetchone()
        return result is not None
    
    def UpdateUser(self, userId, userData):
        result = True
        cursor = self.connection.connection.cursor()
        arrayValues = []
        hasher = PasswordHasher()
        sql = "UPDATE user SET "
        for column, value in userData.items():
            sql += "{0} = %s,".format(column)
            if column in ['password', 'username']:
                arrayValues.append(hasher.hash(value))
            else:
                arrayValues.append(value)
        
        sql = sql[0:-1] + " WHERE id = %s"
        arrayValues.append(userId)
        args = tuple(arrayValues)
        
        try:
            cursor.execute(sql, args)
            self.connection.connection.commit()
        except:
            result = False
        
        return result