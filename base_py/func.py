def arg1(*a):
    print("引数*aの時", a, type(a))

def arg2(**a):
    print("引数**aの時", a, type(a))

def mapmemo():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    div = lambda i: (i % 2) != 0
    x2 = lambda x: x * 2
    nums1 = list(filter(div,nums))
    print("filterを用いて奇数のみに絞ると",nums1)
    print("mapを用いてlist全てにlambdaを適用", list(map(x2, nums1)))

def sortmemo():
    rank = {"a": 10, "b": 5, "c": 30, "d": 20, "e": 0}
    sort = sorted(rank.items(), key=lambda i: i[1], reverse=True)
    print("ソート前は{0},{1}\nソート後は{2},{3}".format(rank,type(rank),sort,type(sort)))

if __name__ == '__main__':
    arg1(1, 2, 3)
    arg2(a=1, b=2, c=3)
    print()
    mapmemo()
    sortmemo()
