from model import *

x = Student('sumdfvkjnanth', 12, '29-10-2004', 9949132469, 
            'andhra','prakasam', 'ongole', 523001,1, 'AIML', 40000)
y = Student('sumdfvkjnanth', 12, '29-10-2004', 9949132469, 
            'andhra','prakasam', 'ongole', 523001,2, 'AIML', 40000)

print(x. get_student(1))

x.update_student(2)

if x.delete_student(1):
    print('deleted data')