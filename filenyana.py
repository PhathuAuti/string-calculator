import re

def phathz(strng):
    added = 0
    if len(strng) == 0:
        return 0

    if len(strng) == 1:
        try:
            return(int(strng))
        except:
            return("ERROR. Only accepts numbers.")
    
    if len(strng) == 3:
        for each in strng:
            try:
                added += int(each)
            except:
                continue
            return added

    if len(strng) > 3:
        for each in strng:
            try:
                added += int(each)
            except:
                continue
            return added
    x = re.findall("-?\d+", strng)
    for i in x:
        added += int(i)
        if (x):
            return added
        else:
            return("ERROR. Only accepts numbers.")

print(phathz("1,2,3"))