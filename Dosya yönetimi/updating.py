
# with open("newfile.txt", "r+", encoding= "utf-8") as file :
#     file.seek(20)
#     file.write("test")


# with open("newfile.txt", "r+", encoding= "utf-8") as file :
#     print(file.read()) 

#********* update at end of  the page *********
# with open("newfile.txt", "a", encoding="utf-8")  as file:                # a dediğimizde crüsör dosyanın en sonuna geliyor ve oradan başlıyor eklemeye.
#     file.write("\nEmel Turan")

# with open("newfile.txt", "r", encoding= "utf-8") as file :
#     print(file.read()) 

# #********* update at top of the page *********

# with open("newfile.txt", "r+", encoding= "utf-8") as file :
#     content = file.read()
#     content = "Efe turan\n" + content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt", "r", encoding= "utf-8") as file :
#     print(file.read()) 


# #********* update at middle of the page *********


with open("newfile.txt", "r+", encoding= "utf-8") as file :
    list = file.readlines()
    list.insert(1, "Ali Korkmaz\n")
    file.seek(0)
    for i in list:
        file.write(i)

with open("newfile.txt", "r", encoding= "utf-8") as file :
    print(file.read())
