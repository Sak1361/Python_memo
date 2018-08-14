import random


def listmemo():
    listA = []
    for i in range(1, 10):
        listA.append(i)
    else:
        tupleA = tuple(listA)

    print(listA)

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    set1 = set(random.choices(letters, k=5))
    set2 = set(random.choices(letters, k=5))
    print("1は", set1)
    print("2は", set2)
    print("１と２で重複する？", set1 in set2)


if __name__ == '__main__':
    listmemo()
