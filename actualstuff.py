import re

def phathz(string):
    x = re.findall("-?\d+", string)
    added = 0
    if len(string) == 0:
        return 0

    if len(string) == 1:
        try:
            return(int(string))
        except:
            return("ERROR. Only accepts numbers.")
    
    if len(string) >= 3:
        for each in string:
            try:
                added += int(each)
            except:
                continue
    return added

    for i in x:
        added += int(i)
        if (x):
            return added
        else:
            return("ERROR. Only accepts numbers.")

print(phathz("//;\n1;2"))