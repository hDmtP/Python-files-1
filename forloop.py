'''
dfdf=["fdjfh", "jfeojf", "df65+f", 78, 56,1, 2, 3, 89, 456, 466]

for item in dfdf:
    if str(item).isnumeric() and item<4:
        print(item)
'''

list1 = [ ["Harry", 1], ["Larry", 2],
          ["Carry", 6], ["Marie", 250]]
dict1 = dict(list1)

for item in dict1:
    print(item)
for item, lollypop in dict1.items():
    print(item, "and lolly is ", lollypop)
# items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

# for item in items:
#     if str(item).isnumeric() and item>=6:
#         print(item)

