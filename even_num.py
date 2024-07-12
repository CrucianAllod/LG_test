def myIsEven(value: int) -> bool:
    return bin(value)[-1] == '0'
 

print(myIsEven(1))

