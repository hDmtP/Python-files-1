from matplotlib import pyplot as plt

n=int(input("How many players do you want?\n"))
no_of_Players=0
Players=[]
scores=[]
explodes=[]

while no_of_Players!=n:
    Player=str(input("Enter Player name: "))
    score=int(input("Enter Player's score: "))
    explode=float(input("Enter Player's explode amount in fraction: "))
    Players.append(Player)
    scores.append(score)
    explodes.append(explode)
    no_of_Players+=1
    

print(Players)   
print(scores)
print(explodes) 

print("Elements saved!\n")

fig1, ax1=plt.subplots()
ax1.pie(scores, explode=explodes, labels=Players, autopct='%1.1f%%', shadow=True, startangle=(360/n))
ax1.axis('equal')
print("Do you want to see the pie-chart?\n")
confirm=str(input("(y/n): "))
if confirm=='y':
    plt.show()
    