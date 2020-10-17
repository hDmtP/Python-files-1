class NewType():
    attr = "Hello NewType"

New = NewType()

print(type(New))
print(New.attr)