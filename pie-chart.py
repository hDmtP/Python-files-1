from matplotlib import pyplot as plt
Players=('Steve Jobs', 'Larry Page', 'Bill Gates', 'Mark Zuckerberg', 'Elon Musk')
score=[20, 20, 20, 15, 25]
explode=(0, 0, 0, 0, 0.1)
fig1, ax1=plt.subplots()
ax1.pie(score, explode=explode, labels=Players, autopct='%1.1f%%', shadow=True, startangle=72)
ax1.axis('equal') # equal aspect ratio ensures that pie is drawn as circle
plt.show()


# spelling mistakes occured at 'labels'