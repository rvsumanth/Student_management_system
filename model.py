import json
from utils import *
from Custom_Exceptions import *


class Student:
    def __init__(self, name: str, age: int, dob: str, phone: int, state: str, 
                 district: str, city: str, pincode: int, roll: int, branch: str, 
                 fees: int):
        self._name = name
        self._age = age
        self._dob = dob
        self._phone = phone
        self._state = state
        self._district = district
        self._city = city
        self._pincode = pincode
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
                'roll number': self._roll,
                'name': self._name,
                'age': self._age,
                'dob': self._dob,
                'phone': self._phone,
                'Address':{
                            'state': self._state,
                            'district': self._district,
                            'city': self._city,
                            'pincode': self._pincode,
                        },
                'branch': self._branch,
                'fees': self._fees
            }
            with open('data.json', 'w') as f:
                json.dump(all_data, f, indent = 4)
        

    def get_student(self, id: int) -> dict:
       try:
            with open('data.json', 'r') as f:
              data = json.load(f)
        
       except (FileNotFoundError, json.JSONDecodeError):
           return False
        
       else:
           if str(id) in data:
               return data[str(id)]
           else:
               raise StudentNotFound()
           
           
    def update_student(self, id):
        try: 
            with open('data.json' , 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Error: {e}')
        
        if str(id) in data:
            collect_info = collect_student_details(id)
            with open('data.json', 'w') as f:
                data[str(id)] = collect_info
                json.dump(data, f, indent= 4)
        else:
            raise StudentNotFound()
        
        
    def delete_student(self, id) -> bool:
        try:
            with open('data.json' , 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return False
        
        if str(id) in data:
            del data[str(id)]
            with open('data.json', 'w') as f:
                json.dump(data, f, indent = 4)
            return True
        else:
            raise StudentNotFound()
        return False
    


class User_data():
    def __init__(self, role: str, id: int, Username: str, Password: str):
        self.id = id
        try:
            with open('data.json', 'r') as f:
                all_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print('database is Empty')
        else:
            student_key = str(self.id)
            if student_key in all_data:
                self.role = role
                self.username = Username
                self.password = Password
                try: 
                    with open('user_data.json', 'r') as f:
                        cred_data = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    cred_data = {}
                cred_data[student_key] = {
                    'role' : self.role,
                    'username': self.username,
                    'password': self.password
                }
                with open('user_data.json','w') as f:
                    json.dump(cred_data, f, indent = 4)
            else:
                raise StudentNotFound('Student doesnot exist please create student data first')
        
    def update_cred(self, id) -> bool:
        try:
            with open('user_data.json', 'r') as f:
                all_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return False
        
        student_key = str(id)
        if student_key in all_data:
            data = collect_cred_data()
            with open('user_data.json', 'w') as f:
                all_data[str(id)] = data
                json.dump(all_data, f, indent = 4)
            return True
        else:
            raise StudentNotFound()
        
        
        
        




        
        







