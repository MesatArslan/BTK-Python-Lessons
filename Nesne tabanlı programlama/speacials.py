myList = [1,2,3]
# myString = 'my string'


# print(len(myList))
# print(len(myString))
# print(type(myList))
# print(type(myString))




class Movie():
    def __init__(self, title, director, duraction):
        self.title = title
        self.director = director
        self.duraction = duraction
        print('Movie Objects created.')
    
    def __str__(self):
        return f"{self.title} by { self.director}"
    
    def __len__(self):
        return self.duraction
    
    def __del__(self):
        print('Film deleted.')
    
    

m = Movie('Film name', 'Film director', 'Film duraction')

# print(str(myList))
# print(str(m))
# print(len(myList))
# print(len(m))

del m

