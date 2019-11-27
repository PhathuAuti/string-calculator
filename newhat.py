import re

strng = "The3 rain2 in Spain-10"

x = re.findall("-?\d+", strng)
q = 0
for i in x:
    q+=int(i)

if (x):
  print(q)
else:
  print("ERROR. Only accepts numbers.")
