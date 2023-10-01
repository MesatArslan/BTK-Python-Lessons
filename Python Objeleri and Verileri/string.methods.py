message = " Hello there. I am using computer."

# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()

# message = message.strip()
# message = message.split() 
# message = message.split('.') 
message = message.split() 
message = ' '.join(message) # eğer kelimeler ayrı ise birleştirmek için
# message = '***'.join(message)

# index = message.find('using')
# isfound = message.startswith('H')
# isfound = message.endswith('m')
# print(isfound)

# message = message.replace('using','playing')
# message = message.replace(' ','*').replace('ç','c').replace('ö','o')

message = message.center(100)

print(message)   
# print(message[2])
