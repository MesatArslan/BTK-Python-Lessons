#Key-Value

#41  => Kocaeli    34=> İstanbul

Cities = ['Kocaeli', 'İstanbul']
plates = [41, 34]
print(plates[Cities.index('İstanbul')])
print(plates[Cities.index('Kocaeli')])

#print(plates['Kocaeli'])     => 41
#print(plates['İstanbul'])    => 34

plates = {'Kocaeli':41, 'İstanbul':34}

print(plates['Kocaeli'])
print(plates['İstanbul'])

plates['Ankara']  = 6
plates['Kocaeli'] = 'New value'

print(plates)


users = {
    'Sadıkturan':{
        'age': 36,
        'email': 'sadık@gmail.com',
        'address': 'Kocaeli',
        'phone': '234214234'
    },
    'Çınaraltun':{
        'age': 2,
        'email': 'çınar@gmail.com',
        'address': 'İstanbul',
        'phone': '234214234'
    }
}
print(users['Sadıkturan'])
print(users['Çınaraltun']['age'])
print(users['Çınaraltun']['email'])
print(users['Çınaraltun']['address'])
