'''Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
'''


class User:

    def __init__(self, level, user_id, name):
        self.level = level
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f'{self.name}: id = {self.user_id}, level access = {self.level}'

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id
