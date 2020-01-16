import re

def add(string):
    # converting string to raw string
    string = r'{}'.format(string)
    # Extract numbers (both positive and negative) into a string numbers list x
    integers = re.findall(r"-?\d+", string)
    total_sum = 0
    negatives = extractNegatives(integers)
    if len(string) == 0:
        return 0

    if len(string) == 1:
        try:
            return(int(string))
        except:
            return("ERROR. Only accepts numbers.")

    if len(string) >= 3:
        if len(negatives) > 0:
            error_msg = 'ERROR: negatives not allowed '
            for number in negatives:
                # first check if it is the last number so that you don't add a comma
                if negatives.index(number) != len(negatives) - 1:
                    error_msg += str(number) + ','
                else:
                    error_msg += str(number)
            raise Exception (error_msg)
        else:
            for number in integers:
                if int(number) < 1000:
                    total_sum += int(number)
    return total_sum

# helper function to return a list of negative numbers
def extractNegatives(numbers_list):
    negatives = []
    for number in numbers_list:
        if int(number) < 0:
            negatives.append(int(number))
    return negatives

# print(add("//;\n1;2"))
# print(add("-1,-2,3,4"))