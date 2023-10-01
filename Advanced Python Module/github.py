import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '2a0cebe35888589a756953098fb345a5c26fc79b'
    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()

    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def createRepository(self,name):
        response=requests.post(self.api_url+'/user/repos?access_token='+ self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://sadikturan.com",
            "private": False,
            "has issues": True,
            "has projects": True,
            "has wiki": True
            })

        return response.json()


github = Github()


while True:
    select = input("1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\nYour select: ")


    if select =='4':
        break
    else:
        if select == '1':
            username = input('Username: ')
            result = github.getUser(username)
            print(f"Name: {result['name']} Public repos: {result['public_repos']} Followers: {result['followers']}")

        elif select == '2':
            username = input('Username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['Name'])
        elif select == '3':
            name = input('Repository Name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print('Wrong selection...')