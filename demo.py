
class Student:
   class_work="ece"
   def __init__(self, name, roll_no):
       self.name=name
       self.roll_no=roll_no



s1 = Student("venkat", 30504)

s2 = Student("shannu", 30505)

s1.name="deepu"

print(s1.name)

print(s2.roll_no)

print(s2.class_work)
print(__name__)
#if __name__== '__main__' :
   # print("execute the code")







