import re

strng = "The3 rain2 in Spain-10"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("-?\d+", strng)
q = 0
for i in x:
    q+=int(i)

print(q)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
