def phathz(string):
    added = 0
# def separate(word): 
#     return [char for char in word]

    if len(string) == 0:
        return 0

    if len(string) == 1:
        try:
            return(int(string))
        except:
            return("ERROR. Only accepts numbers.")
    
    if len(string) == 3:
        for each in string:
            try:
                added += int(each)
            except:
                continue
            return added

    if len(string) > 3:
        for each in string:
            try:
                added += int(each)
            except:
                continue
            return added
