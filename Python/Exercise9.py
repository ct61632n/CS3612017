n = [[3, 8, 5], [8, 10, 6, 2, 8, 1]]
def Combine(i):
    newlist = []
    for each_list in i:
        for each_number in each_list:
            newlist.append(each_number)
    return newlist
print( Combine(n))
