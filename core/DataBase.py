import sqlite3
from core.Cookie import Cookie
    
class Users:
    def __init__(self):
        try:
            self.userBase = sqlite3.connect('data.db')
            print('подключение успешно')
        except Exception as e:
            pass
        self.userCursor = self.userBase.cursor()
        self.cookie = Cookie()

        self.userCursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL,
                cookie_t TEXT NOT NULL
            )            
            """
        )
        self.userBase.commit()
        self.userBase.close()

    def addUser(self, username, password, email):
        userBase = sqlite3.connect('data.db')
        userCursor = userBase.cursor()
        data = self.getUserByLogin(username)
        if data != False:
            return 403
        else:
            token = self.cookie.encode_text(f'{username}')
            userCursor.execute(
                'INSERT INTO Users (username, password, email, cookie_t) VALUES (?, ?, ?, ?)', 
                (username, password, email, token)
            )
            userBase.commit()
            userBase.close()
            return token

    def getUserById(self, id):
        # Выбираем всех пользователей
        userBase = sqlite3.connect('data.db')
        userCursor = userBase.cursor()
        userCursor.execute('SELECT * FROM Users')
        users = userCursor.fetchall()

        # Выводим результаты
        for user in users:
            print(user)
        
        userBase.close()

    def getUserByLogin(self, login: str):
        try:
            # Выбираем пользователя с конкретным логином
            userBase = sqlite3.connect('data.db')
            userCursor = userBase.cursor()
            userCursor.execute("SELECT * FROM Users WHERE username = ?", (login,))
            user = userCursor.fetchone()
            if user:
                return user  # возвращаем найденного пользователя (кортеж или объект)
            else:
                return False  # пользователь не найден
        except Exception as e:
            print("Ошибка при поиске пользователя:", e)
            return False

    def loginUser(self, login, password):
        user = self.getUserByLogin(login)
        if user != False:
            if user[2] == password:
                return user[4]
    
    def encode_pass(self, password) -> str:
        pass

    def decode_pass(self, text) -> str:
        pass 


# class Basket:
#     def __init__(self):
#         self.basketBase = sqlite3.connect('data.db')
#         self.basketCursor = self.basketBase.cursor()
#         self.basketBase.execute(
#             """
#             CREATE TABLE IF NOT EXISTS Basket (
#                 id INTEGER PRIMARY KEY,
#                 userId TEXT NOT NULL,
#                 items TEXT
#             )            
#             """
#         )
#         self.basketBase.commit()
    
#     def getItemsByUser(self, userId):
#         pass

#     def addItemByBasket(self, id):
#         pass

#     def clearBasket(self, id):
#         pass

class Items:
    def __init__(self):
        itemsBase = sqlite3.connect('product.db')
        itemsCursor = itemsBase.cursor()

        itemsCursor.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                info TEXT NOT NULL,
                price INTEGER NOT NULL,
                rank TEXT NOT NULL
            )            
            """
        )
        itemsCursor.execute(
            """
            CREATE TABLE IF NOT EXISTS rank (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                info TEXT NOT NULL,
                tag TEXT NOT NULL
            )
            """
        )
        itemsBase.commit()
        itemsBase.close()
    
    def excute(self, sqlStr, parm):
        itemsBase = sqlite3.connect('product.db')
        itemsCursor = itemsBase.cursor()

        itemsCursor.execute(
            sqlStr,
            parm
        )

        itemsBase.commit()
        itemsBase.close()
    
    def search(self, sqlStr, parm=(), allOrOne:str='all'):
        itemsBase = sqlite3.connect('product.db')
        itemsCursor = itemsBase.cursor()

        if parm == ():
            itemsCursor.execute(sqlStr)
        else:
            itemsCursor.execute(sqlStr, parm)
        
        
        if allOrOne == 'all':
            data =  itemsCursor.fetchall()
        else:
            data = itemsCursor.fetchone()
        itemsBase.close()
        return data
    
    def getItemTitle(self, title) -> dict:
        data = self.search('SELECT * FROM items WHERE title = ?', (title,))
        print(data)

    def getItemId(self, id) -> dict: 
        pass

    def getByRank(self, rank) -> dict:
        data = self.search('SELECT * FROM items WHERE tag = ?', (rank, ))
        response = {}
        for i in data:
            response[i[0]] = {
                "title":i[1],
                "info":i[2],
                "price":i[3],
                "tag":i[4],
                'image':i[5]
            }
        return response


