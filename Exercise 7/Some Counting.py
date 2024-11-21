#Some Counting

a=0  
b=0
c=0
d=0
e=0

print("\n0 - 50:")
for a in range(0,51):
    print(a) 
    
print("\n50 - 0:")
for b in reversed(range(0,51)):
    print(b)
    
print("\n30 - 50:")
for c in range(30,51):
    print(c)

print("\n50 - 10 With Increments Of 2:")
for d in reversed(range(10,51,2)):
    print(d)
    
print("\n100 - 200 With Increments Of 5:")
for e in range(100,201,5):
    print(e)