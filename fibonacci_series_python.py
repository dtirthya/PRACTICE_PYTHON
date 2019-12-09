n = int(input("ENTER: "))
a = 0
b = 1
if n == 1:
    print(a)
elif n == 2:
    print(a)
    print(b)
else:	
    print(a)
    print(b)	
    for i in range(0,n-2):
        c = a + b
        print(c)
        a = b
        b = c
		
		
		
	
