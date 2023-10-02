import pandas as pd

# customers = {
#     'CustomerId' : [1,2,3,4],
#     'Firstname' : ['Ahmet','Ali','Hasan','Canan'],
#     'Lastname' : ['Yilmaz', 'Korkmaz','Çelik','Toprak']
# }

# orders = {
#     'ordersId' : [10,11,12,13],
#     'CustomerId': [1,2,5,7],
#     'Orderdate': ['2010-07-04','2010-08-04','2010-07-07','2010-07-11']
# }


# df_customers = pd.DataFrame(customers, columns=['CustomerId','Firstname','Lastname'])
# df_orders = pd.DataFrame(orders, columns = ['ordersId','CustomerId','Orderdate'])


# print(df_customers)
# print(df_orders) 

# result = pd.merge(df_orders,df_customers, how = 'inner')
# result = pd.merge(df_orders,df_customers, how = 'left')
# result = pd.merge(df_orders,df_customers, how = 'outer')
# result = pd.merge(df_orders,df_customers, how = 'right')



customersA = {
    'CustomerId' : [1,2,3,4],
    'Firstname' : ['Ahmet','Ali','Hasan','Canan'],
    'Lastname' : ['Yilmaz', 'Korkmaz','Çelik','Toprak']

}


customersB= {
    'CustomerId' : [4,5,6,7],
    'Firstname' : ['Yağmur','Çinar','Cengiz','Can'],
    'Lastname' : ['Bilge', 'Turan','Yilmaz','Turan']

}

df_customersA = pd.DataFrame(customersA, columns=['CustomerId','Firstname','Lastname'])
df_customersB = pd.DataFrame(customersB, columns=['CustomerId','Firstname','Lastname'])

result = pd.concat([df_customersA, df_customersB])
result = pd.concat([df_customersA, df_customersB],axis=1)
print(result)

