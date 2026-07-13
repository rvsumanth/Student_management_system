from Custom_Exceptions import *

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
