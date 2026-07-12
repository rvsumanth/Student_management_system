import json
from Custom_Exceptions import *

class Student:
    def __init__(self, name: str, age: int,dob: str, phone: int, address: str, roll: int, branch: str, fees: int):
        self._name = name
        self._age = age
        self._dob = dob
        self._phone = phone
        self._address = address
        self._roll = roll
        self._branch = branch
        self._fees = fees

        try:
            with open('data.json', 'r') as f:
                all_data = json.load(f)

        except(FileNotFoundError, json.JSONDecodeError):
            all_data = {}
        
        student_key = str(self._roll)

        if student_key in all_data:
            raise StudentAlreadyExisted()
        else:
            all_data[student_key] = {
                'name': self._name,
                'age': self._age,
                'dob': self._dob,
                'phone': self._phone,
                'address': self._address,
                'branch': self._branch,
                'fees': self._fees
            }
            with open('data.json', 'w') as f:
                json.dump(all_data, f, indent = 4)
        

    @property
    def student_details(self, id: int) -> dict:
       try:
            with open('data.json', 'r') as f:
              data = json.dump(f)
        
       except (FileNotFoundError, json.JSONDecodeError) as e:
           print(f'Error: {e}')
        
       else:
           if str(id) in data:
               return data[str(id)]
           
        


    @student_details.setter
    def student_details(self,name: str, age: int, phone: int, address: str, roll: str, branch: str, fees: int):
        if name:
            self._name = name
        else:
            raise ValueError('Invalid Name')
        
        if age < 18:
            raise ValueError('Invalid Age')
        else:
            self._age = age

        if phone:
            self._phone = phone
        else:
            raise ValueError('Invalid phone')
        
        if address:
            self._address = address
        else:
            raise ValueError('Invalid address')
        
        if roll: 
            self._roll = roll
        else:
            raise ValueError('Invalid roll number')
        
        if branch:
            self._branch = branch
        else:
            raise ValueError('Invalid branch')
        
        if fees < 0:
            raise ValueError('Invalid Amount')
        else:
            self._fees = fees


    def remove_student(self, roll):
        if roll