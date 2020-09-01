from matplotlib import pyplot as plt
num=int(input("How many players do you want?\n"))
no_of_Players=0
players=[]
scores=[]

while no_of_Players!=num:
    Player=str(input("Enter Player name: "))
    score=int(input("Enter Player's score: "))
    players.append(Player)
    scores.append(score)
    no_of_Players+=1

print(players)   
print(scores)

print("Elements saved!\n")

print("Do you want to see the bar graph?\n")
confirm=int(input("(yes=1/no=0): "))
conFirm = bool(confirm)


if conFirm==True:
    color=str(input("Which color will you pick for your bar graph?(red/blue/green/yellow/black): "))
    plt.bar(players, scores, color=color)
    plt.title('Score Card')
    plt.xlabel('players')
    plt.ylabel('score')
    plt.show()

else:
    print("see you soon! GoodBye")