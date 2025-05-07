from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.jungle

# 삽입
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})

# 읽기
all_users = list(db.users.find({}))
print(all_users[0])

same_ages = list(db.users.find({'age':21}))
print(same_ages[0]['name'])

for user in all_users:
    print(user['name'])

user = db.users.find_one({'name':'bobby'})
print(user)

user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user)

# 수정
db.users.update_many({'age':21}, {'$set':{'age':10}})
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user)

# 삭제
db.users.delete_one({'name':'bobby'})
user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user)
