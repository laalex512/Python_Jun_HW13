class UserException(Exception):
    pass


class LevelException(UserException):
    def __init__(self):
        pass

    def __str__(self):
        return 'Your level access too low'


class AccessException(UserException):
    def __init__(self):
        pass

    def __str__(self):
        return 'Incorrect id or name'


class IdException(UserException):
    def __init__(self):
        pass

    def __str__(self):
        return 'ID which you enter already using'
