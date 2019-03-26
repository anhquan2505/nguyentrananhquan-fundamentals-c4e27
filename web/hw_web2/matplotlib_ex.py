from matplotlib import pyplot

# prepare data
machine_types=[18,2,4]
# prepare labels
machine_names=['mac','linux','pc']
#  draw pie
pyplot.pie(machine_types, labels =machine_names, autopct="%.1f%%", shadow=True, explode=[0,0.2,0])
pyplot.axis('equal')
pyplot.title("cho thai")
# show
pyplot.show()