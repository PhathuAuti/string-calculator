# a = "1,2"
# print(a.split(","))

# total = 0

# for num in a.split(","):
#     try:
#         total += int(num)
#     except:
#         print("error, only accept numbers")

# print(total)


# def add(nums):
#     # counter = 0
#     # for value in nums :
#     #     counter += value
#     # return counter
#     if nums == "":
#         return 0
#     if len(nums) == 1:
#         return int(nums)
#     if len(nums) == 3:

def separate(word): 
    return [char for char in word]
    

# #print(add("700"))

# #print(len("1,2"))
# # 
string = "//[***]\n1***2***30"

if len(string) == 0:
    print(0)

if len(string) == 1:
    try:
        print(int(string)) 
    except:
        print("ERROR. Only accepts numbers.")

added = 0
if len(string) == 3:
    for each in string:
        try:
            added += int(each)
        except:
            continue
# print(added)

if len(string) > 3:
    for each in separate(string):
        try:
            added += int(each)
        except:
            continue
print(added)

# Python3 program to Split string into characters 
  
      
# Driver code 
word = "//[***]\n1***2***30"
print(separate(word))
