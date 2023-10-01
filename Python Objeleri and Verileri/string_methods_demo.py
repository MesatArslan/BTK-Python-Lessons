website = "https://www.sadikturan.com"
course = "Python Course: Baştan sona python programlama rehberiniz.(40 hours)"
#1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

result=' Hello World '.strip()
result=' Hello World '.lstrip() #if we just want to delete on the left
result=' Hello World '.rstrip()#if we just want to delete on the right

#2- 'www.sadıkturan.com' içindeki sadıkturan bilgisi haricindeki her karakteri silin.

result ="www.sadikturan.com".strip('w.moc')


#3- course karakter dizin tüm karakterlerini küçük yapın.
result = course.lower()
result = course.upper()
result = course.title()

#4- 'website' içinde kaç tane a karakteri vardır? (count('a'))

result = website.count('a')
result = website.count('www')
result = website.count('www',0,10)#0 ile 10.karakter arasına bakar.

#5- 'website' www ile başlayıp com ile bitiyor mu?

result = website.startswith('www')
result = website.endswith('com')

#6- 'website' içinde '.com' ifadesinu bulunuz.

result = website.find('.com')
result = website.find('.com',0,10)#is there it between 0 to 10
result = course.find('python')
result = course.rfind('python')

#7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpa,isdigit)

result = course.isalpha()
result = "Hello".isalpha()
result = course.isdigit()
result = "256326".isdigit()

#8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip, sağına ve soluna * ekleyiniz.

result = "Contents".center(50)
result = "Contents".center(50,'*')
result = "Contents".ljust(50,'*')

#9- 'course' ifadesindeki tüm boşluk karakterlerini _ ile değiştiriniz.

result = course.replace(' ', '-')
result = course.replace(' ', '-', 5)
result = course.replace(' ', '')

#10- 'Hello World' karakter dizindeki 'World' ifadesini 'there' olarak değiştiriniz.

result = "Hello World".replace('World','there')

#11- 'course' karakter dizini boşluk karakterlerinden ayırın.

result = course.split(' ')
result = result[2]

print(result)