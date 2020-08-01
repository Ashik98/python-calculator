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
