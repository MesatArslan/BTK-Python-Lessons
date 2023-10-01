## Cash Dispenser Application


Sadikaccount = {
    'name': 'Sadık Turan',
    'account no': '1325677',
    'balance': 4000,
    'side account': 2000
}

Alikaccount = {
    'name': 'Ali Turan',
    'account no': '1235677',
    'balance': 6000,
    'side account': 7000
}

def withdrawmoney(account, amount):
    print(f"Hello {account['name']}")

    if (account['balance'] >= amount):
        account['balance'] -= amount
        print('You can withdraw.')
    else:
        suma = account['balance'] + account['side account']

        if (suma >= amount):
            sideacountusing = input('Use side account (Y/N)?: ')

            if  sideacountusing == 'Y' :
              sideaccountusingamount = amount - account['balance']
              account['balance']
              account['balance'] -= sideaccountusingamount
              print('You can withdraw.')
            else:
                print(f"You have {account['balance']} on your account {account['account no']} ")
        else:
            print('Sorry, Your balance is not enough.')


def inquireaccount(account):
    print(f"You have {account['balance']} dolar on the {account['account no']}. Side account limit is {account['side account']} dolar.")
withdrawmoney(Sadikaccount,3000)
inquireaccount(Sadikaccount)
print('****************')
withdrawmoney(Sadikaccount,1000)
inquireaccount(Sadikaccount) 


