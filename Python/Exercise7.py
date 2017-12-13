#prints list 
def List():
    list = ['a','b','c','d','e']
    for i in (list):
        print (i)
    
List()
print("\n")
#prints list reversed
def Listrev():
    list = ['a','b','c','d','e']
    for i in reversed(list):
        print(i,)
Listrev()
print("\n")

#prints len of the list
def Size():
    list = ['a','b','c','d','e']
    lenoflist = 0
    for i in (list):
        lenoflist += 1
		
    print(lenoflist)
print("The size of the list is") 
Size()
