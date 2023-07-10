import copy
import json
from pathlib import Path

from user import User
from user_exceptions import AccessException, LevelException, IdException

EMPTY_DICT = {
    "1": {},
    "2": {},
    "3": {},
    "4": {},
    "5": {},
    "6": {},
    "7": {},
}


class UserProcessing:
    def __init__(self, file: Path):
        self.file = file
        self.user_list = self.read_from_json()
        current_user_name = input('Enter your name: ')
        current_user_id = input('Enter your id: ')
        self.operator = User(1, current_user_id, current_user_name)
        # Сравнение юзеров происходит по id и name, поэтому не обращаем внимание на level = 1
        if self.operator in self.user_list:
            self.operator = self.user_list[self.user_list.index(self.operator)]
            print(f'operator: {self.operator}')
        else:
            raise AccessException()

    def add_user(self):
        input_data = input("Enter name, ID, access level(1-7) to add: ")
        name, user_id, level = input_data.split(', ')
        if level < self.operator.level:
            if self.is_valid_id(user_id):
                self.user_list.append(User(level, user_id, name))
            else:
                raise IdException
        else:
            raise LevelException

    def is_valid_id(self, user_id):
        for user in self.user_list:
            if user_id == user.user_id:
                return False
        return True

    def read_from_json(self):
        current_data = copy.deepcopy(EMPTY_DICT)
        if self.file.is_file():
            with open(self.file, 'r', encoding='utf-8') as f:
                current_data = json.load(f)
        user_list = []
        for level, user in current_data.items():
            for user_id, name in user.items():
                user_list.append(User(level, user_id, name))
        return user_list

    def write_to_json(self):
        current_data = copy.deepcopy(EMPTY_DICT)
        for user in self.user_list:
            current_data[user.level][user.user_id] = user.name
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(current_data, f, ensure_ascii=False, indent=2)

    def print_list(self):
        print()
        for user in self.user_list:
            print(user)
