import os 
import datetime

result = dir(os)
result = os.name


####dizin değiştirme
# os.chdir('C:\\')
# os.chdir('..')
# os.chdir('../..')

#### Klasör oluşturma
# os.mkdir('newdirectory')
# os.makedirs('newdirectory/newdirec') 
# os.rename("newdirectory", "newfile")
# os.rmdir("newdirectory")

# Listeleme(listing)
# result= os.listdir()
# result= os.listdir('/Users\\')

# for file in os.listdir():
#     if file.endswith('.py'):
#         print(file)


#### Etkin dizin öğrenme
# result = os.getcwd()

# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # Creating date
# result = datetime.datetime.fromtimestamp(result.st_atime) # Last accessed date
# result = datetime.datetime.fromtimestamp(result.st_mtime) # Changing date

# os.system("pages.exe")


#### Path

# result = os.path.abspath("_os.py")   
result = os.path.abspath("/Users/mea/Desktop/Advanced Python Module/_os.py")
result = os.path.abspath(os.path.abspath("_os.py"))
result = os.path.exists("_os.py")
result = os.path.exists("/Users/mea/Desktop/Advanced Python Module")
result = os.path.isdir("_os.py")
result = os.path.isdir("/Users/mea/Desktop/Advanced Python Module")
result = os.path.isfile("/Users/mea/Desktop/Advanced Python Module")
result = os.path.join("/Users", "attempt","attempt1")
result = os.path.split("/Users/attempt1")
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]

print(result)