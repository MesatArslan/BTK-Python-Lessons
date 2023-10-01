def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division (a,b):
    return a/b
def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi == "addition":
        print(f1(2,3))
    elif islem_adi == "substraction":
        print(f2(5,3))
    elif islem_adi == "multiplication":
        print(f3(3,4))
    elif islem_adi == "division":
        print(f4(10,2))
    else:
        print('Invalid Transaction...')

islem(addition, substraction, multiplication, division, "addition")
islem(addition, substraction, multiplication, division, "substraction")
islem(addition, substraction, multiplication, division, "multiplication")
islem(addition, substraction, multiplication, division, "division")
islem(addition, substraction, multiplication, division, "divisionm")
    