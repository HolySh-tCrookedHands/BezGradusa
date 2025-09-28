import sqlite3

class LowLevelBase:
    def __init__(self):
        self.userBase = sqlite3.connect('DB/users.db')
        self.basketBase = sqlite3.connect('DB/basket.db')
        self.itemsBase = sqlite3.connect('DB/items.db')
    
        self.userCursor = self.userBase.cursor()
        self.basketCursor = self.basketBase.cursor()
        self.itemsCursor = self.itemsBase.cursor()

        self.userCursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )            
            """
        )
        self.userBase.commit()

        self.basketBase.execute(
            """
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                userId TEXT NOT NULL,
                items TEXT
            )            
            """
        )
        self.basketBase.commit()

        self.itemsCursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                info TEXT NOT NULL,
                price INTEGER NOT NULL,
            )            
            """
        )
        self.itemsCursor.commit()

    

class Users(LowLevelBase):
    def __init__(self):
        super().__init__()

    def addUser(self):
        pass

    def getUserById(self):
        pass

    def getUserByLogin(self):
        pass

    def verifyUserByCookie(self):
        pass

    def loginUser(self):
        pass


class Basket(LowLevelBase):
    def __init__(self, id:int):
        """id объязательный по нему находиться нужная карзина"""
        super().__init__()
    
    def getItems(self):
        pass

    def addItem(self):
        pass

    def clearBasket(self):
        pass

class Items(LowLevelBase):
    def __init__(self):
        super().__init__()