import json
import os


class User:
    def __init__(self, username, password ,email):
        self.username = username
        self.password = password
        self.email    = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        #load users from .json file
        self.loadUsers()
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file :
                users = json.load(file)
                for user in users:
                 user = json.loads(user)
                 newUser = User(username = user['username'], password= user['password'], email = user['email'])
                 self.users.append(newUser)
            print(self.users)

    def Register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("User created.")

    def Login(self, username, password):
       
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Log in done.')
                break    
    
    def Logout(self):
        self.isLoggedIn = False
        self.currentUser= {}
        print('Exist done.')

    def Identity(self):
        if self.isLoggedIn:
            print(f'Username: {self.currentUser.username}')
            
        else:
            print('Login not supported.')

    def savetoFile(self):
        list = []    


        for user in self.users:
            list.append(json.dumps(user.__dict__))


        with open('users.json', 'w') as file:
            json.dump(list, file)


repository = UserRepository()

while True:
    print("menü".center(50,'*'))
    select = input('1-Register\n2-Log in\n3-Log out\n4-Identity\n5-exit\nYour select:')
    if select == '5':
        break
    else:
        if select == '1':
            #Register
            username = input('Username: ')  
            Password = input('Password: ')  
            email = input('Email: ')
            user = User(username= username, password=Password, email=email)  
            repository.Register(user)
        elif select == '2':
            if repository.isLoggedIn:
                print('You are still login.')
            else:
                username = input('Username: ')
                password = input('Password: ')

                repository.Login(username, password)

        elif select == '3':
            repository.Logout()
            

        elif select == '4':
            repository.Identity()
        else:
            print('Wrong Select...')
