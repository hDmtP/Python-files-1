import random
print("\t\t\tPrint as many as integers as you wish. Give a space after each integer\t\t\t\n")
a=list(map(int, input().rstrip().split()))
ai_choice = random.choice(a)
ai_choices = random.choices(a)
print(ai_choice)
print(ai_choices)