import json
from Custom_Exceptions import *

class Student:
    def __init__(self,id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

        try:
            with open('data.json','r') as f:
                all_data = json.load(f)

        except (FileNotFoundError, json.JSONDecodeError):
            all_data = {}
        
        student_key = str(self.id)
        if student_key in all_data:
            raise StudentAlreadyExisted()
        else:
            all_data[student_key] = {
                'name' : self.name,
                'age': self.age
             }
            print(all_data)
            with open('data.json', 'w') as f:
                json.dump(all_data, f, indent=4)
            

x = Student(1, 'sumanth', 22)