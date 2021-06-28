import matplotlib.pyplot as plt
import numpy as np
data = open("CupcakeInvoices.csv")

chocolate = 0
vanilla = 0
strawberry = 0

for line in data:
  line = line.rstrip("/n").split(",")
  if line[2] == "Chocolate":
      chocolate += int(line[3]) * float(line[4])
  elif line[2] == "Vanilla":
      vanilla += int(line[3]) * float(line[4])
  else:
      strawberry += int(line[3]) * float(line[4])


# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

arr = [chocolate, vanilla, strawberry]

people = ("Chocalate", "Vanilla", "Strawberry")
y_pos = np.arange(len(people))
performance = arr
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Number of cupcakes')
ax.set_title('Cupcake Comparison')

plt.show()