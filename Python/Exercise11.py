n=[8, 2, 3, 5, 7]
def multiply(num):  
    total = 1
    for x in num:
        total *= x  
    return total  
print(multiply((n)))

        
    
def recursion(n):
    if len(n)==1:
        return n[0]
    return recursion([n[0]]) * recursion(n[1:])
print(recursion(n))    
