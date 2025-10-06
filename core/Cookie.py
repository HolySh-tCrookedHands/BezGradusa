import os
import json
from random import choice

BASE_DIR = os.path.dirname(__file__)

class Cookie:
    def __init__(self):
        """класс для работы с cookie"""
        self.flie = os.path.join(BASE_DIR, "cookie.json")
        self.folder = os.path.join(BASE_DIR, "core")
        self.listWord = [
            'level', 'dimasik'
            'fijma', 'kabanchik',
            'loli', 'book'
        ]
        with open(f'{BASE_DIR}/WordSpecial.json') as f:
            self.mapping = json.load(f)['mapping']
            self.reverse_mapping = {v: k for k, v in self.mapping.items()}

    
    def encode_text(self,text: str) -> str:
        """Кодирует строку в токен"""
        result = []
        for char in text:
            if char in self.mapping:
                result.append(self.mapping[char])
            else:
                result.append(char) # если символ не найден, оставляем как есть
        return "m".join(result) # добавляем разделитель, чтобы было однозначно

    def decode_text(self,token: str) -> str:
        """Декодирует токен обратно в строку"""
        parts = token.split("m")
        result = []
        for code in parts:
            if code in self.reverse_mapping:
                result.append(self.reverse_mapping[code])
            else:
                result.append("?") # если кода нет в таблице
        return "".join(result)

    def getData(self) -> dict:
        """
            функция для получени данных из файла cookie.json
            возвращяет словарь со значениями
        """
        with open(self.file) as f:
            data = json.load(f)
        return data

    def setData(self, data) -> bool:
        """
            функция для записи новых, или обновления старых куки
            возвращяет True или False
        """
        try:
            with open(self.file, 'w') as f:
                f.write(
                    json.dumps(
                        data,
                        indent=4,
                        ensure_ascii=False
                    )
                )
            return True
        except Exception as e:
            return False
        
    # def generateToken(self) -> str:

if __name__ == '__main__':
    api = Cookie()
    trnaslate_to = api.encode_text('TnSiRt')
    print(trnaslate_to)
    trnaslate_form = api.decode_text(trnaslate_to)
    print(trnaslate_form)