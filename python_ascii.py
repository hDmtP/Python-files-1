import string
import random

result = string.ascii_letters
print(result)

# def cheCk(value):
#     for letter in value:
#         if letter not in result:
#             return False
#     return True
# input1 = str(input())
# input2 = str(input())
# input3 = str(input())

# print(input1, "--> ",  cheCk(input1))
# print(input2, "--> ",  cheCk(input2))
# print(input3, "--> ",  cheCk(input3))

def rand_pass(size):
    generate_pass = ''.join([random.choice(result+string.digits)for n in range(size)])
    return generate_pass
inPut = int(input("Enter password lenght: "))
password = rand_pass(inPut)
print(password)

def rand_pass_(size, scope=(result+string.digits)):
    generate_pass = ''.join([random.choice(scope)for n in range(size)])
    return generate_pass
password_ = rand_pass_(inPut, "PritamDhara23122002")
print(password_)

