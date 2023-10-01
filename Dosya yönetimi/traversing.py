with open('newfile.txt', 'r', encoding= 'utf-8') as file:
    # content = file.read()
    # print(content) 
    # file.seek(11) #konumu koyduğumuz sayıya atar
    # print(file.tell())  #konum verir
    # content2 = file.read()
    # print(content2)

#--------------------------------------------------
    content = file.read(11)
    print(content) 
    file.seek(0) #konumu koyduğumuz sayıya atar
    print(file.tell())  #konum verir
    content2 = file.read()
    print(content2)