from matplotlib import pyplot as plt
players=['ram', 'shyam', 'jadu', 'hdmtp']
score=[12,25,88,97]
plt.bar(players, score, color='yellow')
plt.title('Score Card')
plt.xlabel('players')
plt.ylabel('score')
plt.show()
