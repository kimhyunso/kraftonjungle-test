fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0


for fruit in fruits:
    if fruit == '사과':
        count += 1



def count_fruits(target:str, fruits:list):
    count = 0
    for fruit in fruits:
        if fruit == target:
            count += 1
    return count

count = count_fruits('배', fruits)
print(f'배의 갯수: {count}')

count = count_fruits('감', fruits)
print(f'감의 갯수: {count}')