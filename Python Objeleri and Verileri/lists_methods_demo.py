names = ['Ali', 'Hakan', 'Yağmur', 'Deniz']
years = [1998, 2000, 1998, 1997]

#1-Add the name Cenk to the end of list.
# names.append('Cenk')

#2-Add the name Sena to the top of list.
# names.insert(0, 'Sena')
# names.insert(-1, 'Mehmet')
# names.insert(len(names), '')

#3-Let's delete the name Deniz from the list.
# names.remove('Deniz')
# names.pop()         #eğer değer vermessek listenin en son elemanını siler
# names.pop(1)

#4-What is the index of the name of the Deniz.
index = names.index('Deniz')
# names.pop(index)
print(index)

#5-Is Ali a member of the list?
result = 'Ali' in names
result = names.index('Ali')
print(result)

#6-Reverse list elements.
names.reverse()

#7-Sort list elements alphabetically.
names.sort()

#8-Sort the list of years numerically.
years.sort()

#9- str ='Chevrolet,Dacia' convert string to list.
str ='Chevrolet,Dacia'
result = str.split(',')
print(result)

#10-What is the largest and smallest element of the array years.
min = min(years)
max = max(years)
print(min)
print(max)

#11-How many 1998 elements are in years array.
result = years.count(1998)
print(result)

#12-Delete all the elements of the array years.
# years.clear()

#13-Store 3 brand information you will receive from the user in a list.
markalar = []

marka = input("marka:  ")
markalar.append(marka)

marka = input("marka:  ")
markalar.append(marka)

marka = input("marka:  ")
markalar.append(marka)



print(markalar)
print(years)
print(names)