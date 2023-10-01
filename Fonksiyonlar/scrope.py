#global scope
x = 'global x'

def function():
    #local scope
    # x = 'local x'
    print(x)

function()
print(x)

#####################

#global
name= 'Mehmet'

def Changename(new_name):
    #local
    name = new_name
    print(name)


Changename('Ada')
print(name)

#####################


name = 'global string'

def greeting():
    # name = 'Çinar'
     
    def hello():
        # name = 'Ada'
        print('Hello '+ name)
    
    hello()

greeting()
print(name)


####################

x = 50
def test(x):
    print(f'x : {x}')


    x = 100 
    print(f'changed x to {x}')

test(x)
print(x)


x = 50
def test():
    global x
    print(f'x : {x}')


    x = 100 
    print(f'changed x to {x}')

test()
print(x)


