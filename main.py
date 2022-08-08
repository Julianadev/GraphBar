import matplotlib.pyplot as pyplot

labels = ('Python', 'Javascript', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)
sizes = [45, 10, 15, 30, 22]

# set up the bar chart
pyplot.bar(index, sizes, tick_label = labels, color=('red', 'green', 'blue', 'yellow', 'orange'))

# configure the Layout
pyplot.ylabel('Usadas')
pyplot.xlabel('Linguagens de Programação')

# display
pyplot.show()
