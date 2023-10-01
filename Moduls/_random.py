import random

# result = dir(random)
# result = help(random)

result = random.random() #0.0 -1.0 arasında bir sayı seçer
result = random.random()* 100#0.0 -1.0 
result = random.uniform(1,100)
result = int(random.uniform(1,100))
resutl = random.randint(2,200)

greeting = 'Hello Gentelmens'
names = ['Ali', 'Mehmet', 'Melike','Cenk','Ahmet','Cengiz', 'Efe']
result = names[random.randint(0,len(names)-1)]
# result = names[random.randint(0,3)]
result = random.choice(names)
result = random.choice(greeting)

random.shuffle(names)
result = names

# liste = list(range(10))
# random.shuffle(liste)

liste = range(100)
result = random.sample(liste,5)
result = random.sample(names,2)

# result = liste
print(result)