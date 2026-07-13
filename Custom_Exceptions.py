'''
Exceptions
 Student Not found
 Student Already Existed
'''

class StudentNotFound(Exception):
    def __init__(self, *args):
        super().__init__('No Student is existed with that roll number')

class StudentAlreadyExisted(Exception):
    def __init__(self, *args):
        super().__init__('Student Already Existed')

class StudentAgeInvalid(Exception):
    def __init__(self, *args):
        super().__init__('Student Age must be greater than 18')