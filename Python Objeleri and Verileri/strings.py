name = 'Mahmut'     #bu 6 tane farklı karakter içeriyor bir grup gibi düşünebiliriz. 
surname ='Arslan'
age = 21

# print('My name is'+ name + ' '+ 'and I am' + age +'years old.')
# str'ler ile str'ler toplanır int'ler toplanmaz.

print('My name is '+ name + ' '+ 'and I am ' + str(age) +' years old.')

print('My name is '+ name + ' '+ 'and \nI am ' + str(age) +' years old.')

greeting = 'My name is '+ name + ' '+ 'and \nI am ' + str(age) +' years old.'

print(greeting)


#str'lerde sistem otomatik olarak index numarası atar elemanlarına.

# Mahmut                    M a h m u t
# 012345 or                -6-5-4-3-2-1   'e karşılık gelir.

print(greeting[0])
print(greeting[5])
print(len(greeting))
print(greeting[-1])
print(greeting[2:8])
print(greeting[3: ])
print(greeting[ :18])
print(greeting[2:40:2])  #en son yazdığımız 2 => 2 karakterden bir tanesini al demek.