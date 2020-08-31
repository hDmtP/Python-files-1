# How to get the value from the parent class in class overriding in some simple steps:

class Parent:
    def parent_method(self):
        return "From parent class"
class child(Parent):
    def parent_method(self):
        print(super().parent_method())

child().parent_method()