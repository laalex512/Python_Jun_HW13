'''Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.'''

from my_exceptions import PersonNameError, PersonAgeError


class Person:
    def __init__(self, full_name, age, city='Minsk'):
        self.full_name = full_name
        self.__age = age
        self.city = city

    def birthday(self):
        self.__age += 1

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.__age


def check_fullname(text: str):
    """Простенькая проверка имени на количество слов - возврат -1;
     заглавную первую, остальные прописные, отсутствие цифр - возврат номера слова с ошибкой;
     если все норм - возврат 0
     """

    words = text.split()
    if len(words) < 2:
        return -1
    for number, word in enumerate(words, 1):
        if word[0].islower() or word[0].isdigit():
            return number
        for i in range(1, len(word)):
            if word[i].isupper() or word[i].isdigit():
                return number
    return 0


if __name__ == '__main__':
    name = input('Введите имя человека: ')
    print(check_fullname(name))
    if check_fullname(name):
        raise PersonNameError(check_fullname(name))
    try:
        age = int(input('Введите возраст: '))
    except ValueError:
        raise PersonAgeError(-1)
    if age < 0:
        raise PersonAgeError(1)
    person1 = Person(name, age)
    print('Все ок')
