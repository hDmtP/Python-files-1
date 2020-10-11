'''
class Person:
    def __init__(self, fname, ftitle):
        self.firstname = fname
        self.title = ftitle

    def printname(self):
        print(self.firstname, self.title)

class Student(Person):
    pass
x = Student('Pritam', 'Dhara')
x.printname()
'''
'''
class Sondhi:
    def __init__(self, head, legs, body, hands, rorgan):
       self.first = head
       self.second = legs
       self.third = body
       self.fourth = hands
       self.fifth = rorgan
    def Human(self):
       print(self.first,self.second,self.third,self.fourth,self.fifth)

# class Persona(Sondhi):
#     pass

# x = Persona('pri','ta','m','dha','ra')
# x.Human()
y = Sondhi('pri','ta','m','dha','ra')
y.Human()
        

#  HERE __init__ STORES ALL THE ARGUMENTS_MEMORY, THUS LEADING TO LESS LINE OF CODES
'''
class Try:
    def do_something(self):
        print("https://www.youtube.com/watch?v=g6vQWURCITs&ab_channel=AmazingIndia")

if __name__ == "__main__":
    obj_list=[]
    for obj in range(69):
        obj=Try()
        obj_list.append(obj)

obj_list[0].do_something()
        
    