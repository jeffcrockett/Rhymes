import matplotlib.pyplot as plt

labels = 'Cats', 'Dogs', 'Frogs', 'Logs'
sizes = [25, 25, 40, 10]
colors = ['red', 'green', 'orange', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()
