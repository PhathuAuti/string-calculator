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

    
    

# #print(add("700"))

# #print(len("1,2"))
# # 
string = "1,2"

if len(string) == 0:
    print(0)

if len(string) == 1:
    try:
        print(int(string)) 
    except:
        print("ERROR. Only accepts numbers.")

if len(string) == 3:
    added = 0
    for each in string:
        try:
            added += int(each)
        except:
            continue
print(added)


