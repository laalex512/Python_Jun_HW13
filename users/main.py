from pathlib import Path
from user_processing import UserProcessing

if __name__ == '__main__':

    file = Path('users.json')
    proc1 = UserProcessing(file)
    proc1.print_list()
    while True:
        inp = input('Continue (y/n): ')
        if inp == 'y':
            proc1.add_user()
        else:
            proc1.write_to_json()
            proc1.print_list()
            break
