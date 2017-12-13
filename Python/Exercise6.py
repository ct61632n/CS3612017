#A B
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True   
#c
print( is_prime(9))

def is_prime2(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status

for n in range(1,40):
    if is_prime2(n):
        if n==97:
           print( n)
        else:
           print (n,"",)
#D
def FirstNprimes(n):
    answer = []
    count = 2
    while count < n:
        for a in range(2,(2+1)):
            if count % a == 0 and count!=a:
                break
        else:
            answer.append(count)
        count += 1
    return answer
print(FirstNprimes(100))
