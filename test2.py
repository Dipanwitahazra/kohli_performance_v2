multiplyx=lambda var1,var2:var1*var2
print(multiplyx(5,6))



temp=56
def test():
    print("Value of temp before the function",temp)

def test():
    global temp
    temp=9
    print("Value of temp inside the function: ",temp)

test()
print("value of temp after the function: ",temp)