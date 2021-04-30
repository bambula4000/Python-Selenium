a = [{"name": "sasa", "age": 15}, {"name": "sasa", "age": 165}, {"name": "vova", "age": 22}]


def getFirst(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(j)
            if a[i]["name"] == a[j]["name"]:
                print('s')

    print(a)


# getFirst(a)



n = int(input())
for i in range(n):
    a = int(input())
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
else:
    print('Ни одного отрицательного числа не встретилось')
