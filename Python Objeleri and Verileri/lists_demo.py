# 1- "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

arabalar = ['BMW', 'Mercedes', 'Opel', 'Mazda']

# 2- Liste kaç elemanlıdır.

print(len(arabalar))


# 3- Listenin ilk ve son elemanı nedir?

result = arabalar[0]
result = arabalar[-1]

# 4- Mazda değerini Toyota değeri ile değiştirin.

arabalar[-1] = 'Toyota'

# 5- Mercedes listenin bir elemanı mıdır?

result = 'Mercedes' in arabalar

# 6- Listenin -2 indexindeki değer nedir?

result = arabalar[-2]

# 7- Listenin ilk 3 elemanını alın.

result = arabalar[0:3]
result = arabalar[:3]
result = arabalar[-2:]

# 8- Listenin son 2 elemanı yerine Totoya ve Renault değerlerini ekleyin.

arabalar[-2:] = ['Toyota', 'Renault']

# 9- Listenin üzerine Audi ve Nissan değerlerini ekleyin.

result = arabalar + ['Audi', 'Nissan']

# 10- Listenin son elemanını silin.

del arabalar[-1]

# 11- Liste elemanlarını tersten yazdırın.

result = arabalar[::-1]

# 12-Aşağıdaki verileri bir liste içinde yazındırın.
     #studentA: Yiğit Bilgi  2010, ( 70,60,70)
     #studentB: Sena Turan   1999, (80,80,70)
     #studentC: Ahmet Dikici 1998, (70,80,70)

studentA = ['Yiğit', 'Bilgi', '2010', ['70', '60', '70']]
studentB = ['Sena', 'Turan', '1999', ['80', '80', '70']]
studentC = ['Ahmet', 'Dikici', '1998', ['70', '80', '70']]

# 13- Liste elemanlarını ekrana yazdırınız.
result = studentA + studentB + studentC


print(result)
print(arabalar)