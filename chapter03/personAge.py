people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

# for person in people:
#     print(f'{person["name"]}의 나이는 {person["age"]}입니다.')

def person_age(target:str):
    for person in people:
        if target == person['name']:
            return person['age']
    return '해당하는 이름이 없습니다.'


age = person_age('bob')
print(f'bob의 나이는 {age}입니다.')
