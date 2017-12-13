a =[1,2,3,4,5,6]
print(a)
b=a
b[1]=6
print(a)# a[1] changed to 6 because b=a
c=a[:]
c
c[2] = 24
print(a)# List a[] did not change but, List element c[2] in list c changed to 24
print(c)
def set_first_elem_to_zero(l):
    l[0] = 0
    return l
n=[2,4,5,6]
print(set_first_elem_to_zero(n))
