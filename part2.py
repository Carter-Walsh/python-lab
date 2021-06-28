# 2 open open Cupcakes.csv

open_file = open("CupcakeInvoices.csv")


# 3 print each row
for line in open_file:
    print(line)

# 4 Loop through all the data and print the type of cupcake purchased
for line in open_file:
  line = line.rstrip("/n").split(",")
  print(line[2])

# 5 Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
arr = []
for line in open_file:
  line = line.strip().split(",")
  arr.append(line)

for i in arr:
  print(round(int(i[3])*float(i[4]),2))

# 6 
total = 0
for i in arr:
  current_total = round(int(i[3])*float(i[4]),2)
  total += current_total

print(round(total, 2))

# 7 
open_file.close()

