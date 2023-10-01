# try:
#     file = open('newfile2.txt')
#     print(file)
    
# except FileNotFoundError:
#     print("File doesn't found.")

# finally:
#     print('File closed.')
#     file.close()



file = open('newfile.txt', 'r', encoding= 'utf-8')

## for döngüsü

# for i in file:
#     print(i, end='')


## *********** read() fonksiyonu

# content1 = file.read()
# print('Content 1')
# print(content1)


# content2 = file.read()              
# print('Content 2')
# print(content2)
# #Dosyayı böyle yazdırdığımızda 2.içerik açılmıyor bunun nedeni ilk seferde okuduktan sonra sonuna geliyor ve yanıp sönüyor tekrar oku dediğimizde sonundan başlıyor ama içerik olmadığı için bize birşey göstermiyor.

# -----------------------------------------#



# content1 = file.read()
# print('Content 1')
# print(content1)


# file = open('newfile.txt', 'r', encoding= 'utf-8')
# content2 = file.read()              
# print('Content 2')
# print(content2)


# content = file.read(15)
# content = file.read(7)   #Her bir okumada kaldığı yerden devam ediyor.
# content = file.read(9)
# print(content)


## *********** readline() fonksiyonu


# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline())
# print(file.readline())
# print(file.readline())


## *********** readlines() fonksiyonu


liste = file.readlines()

# print(liste)
print(liste[0],end= '')
print(liste[1])
print(liste[2])

file.close()

