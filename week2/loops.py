
mydictionary = { 'name':'Allen', 'age':20, 'height':2.5 }
mylist = [2,3,4,'allen', 'kojo']


print(mydictionary['age'])
a=4
b=6

print('====== LOOP 1 ========')
# for loop
for i in range(0,3):
    # print(a+b)
    print(mylist[i])


print('====== LOOP 2 =========')
for i in mylist:
    print(i)


print('====== LOOP 3 =========')
for i in mydictionary:
    print(mydictionary[i])






