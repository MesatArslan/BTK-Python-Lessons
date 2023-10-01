x = 5
hak = 5 
contunie = 'e'


result = 5 < x < 10

# and
 
#True, True => True
#True, False => False
result = ( x > 5 )  and ( x < 10 )
result = ( hak > 0) and ( contunie == 'e')


# or 

result = (x >0 ) or ( x % 2 == 0)

# True, True => True
# True, False => True
# False, False => False


# not

result = not(x > 0)

# Is x an even number between 5-10?

result = (x > 5) and (x < 10) and (x % 2 == 0)

print(result)
