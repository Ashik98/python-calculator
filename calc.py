#def do_math(n1,n2):
#    return n1 + n2
#m1= do_math(5,7)
#m2= do_math(6,8)
#m3=do_math(m1,m2)
#print("first sum is",m1, "second sum is",m2 ,"and third sum is",m3)
 
#check="hamburger"
#if check == 1:
#    print("its 1")
#elif check == 2:
 #   print("hell")
#elif check == 3:
 #   print("hell")
#else:
#    print("cool")

#list=["6601","si","404","0012"]
#for item in list:
 #   print("he is",item)

import re
print("my calculator")
print("type 'quit' to end")
prev=0
run=True
def performMath():
    global run
    global prev
    equation=""
    if prev == 0:
        equation=input("enter Your equation:")
    else:
        equation=input(str(prev))
    if equation == 'quit':
        print("tata good bye")
        run=False
    else:
        equation=re.sub('[a-zA-Z,.;:()" "]', '', equation)
        if prev == 0:
            prev=eval(equation)
        else:
            prev=eval(str(prev)+equation)
while run:
    performMath()