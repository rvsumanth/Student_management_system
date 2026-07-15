from Custom_Exceptions import *
import json

def collect_student_details(id) -> dict:
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    if age < 18: 
        raise StudentAgeInvalid() 
    dob = input('Enter dob: ')
    phone  = int(input('Enter Phone number: '))
    state = input('Enter state: ')
    district = input('Enter District: ')
    city = input('Enter City: ')
    pincode = input('Enter Pincode: ')
    branch = input('Enter Branch: ')
    fees = int(input('Enter fees: '))
    return {
                'roll number': id,
                'name': name,
                'age': age,
                'dob': dob,
                'phone': phone,
                'Address':{
                            'state': state,
                            'district': district,
                            'city': city,
                            'pincode': pincode,
                        },
                'branch': branch,
                'fees': fees
            }

def collect_cred_data() -> dict:
    role = input('Enter role: ')
    username = input('Enter username: ')
    password = input('Enter Password: ')
    if role and  username and password is not None:
        return {
            'role': role,
            'username': username,
            'password': password
        }
    else:
        raise ValueError('Null Values are not accepted')
     
def login(id: int, username: str, password: str) -> bool:
    try:
        with open('user_data.json', 'r') as f:
            all_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False
    
    if str(id) in all_data:
        if all_data[str(id)]['username'] == username:
            if all_data[str(id)]['password'] == password:
                return True
            else:
                return False
        else:
            return False
    else: 
        return False
    
