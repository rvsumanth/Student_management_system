'''
Exceptions
 Student Not found
 Student Already Existed
'''

class StudentNotFound(Exception):
    def __init__(self):
        super().__init__('Student Not Found')

class StudentAlreadyExisted(Exception):
    def __init__(self, *args):
        super().__init__('Student Already Existed')