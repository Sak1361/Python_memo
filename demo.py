import random


def listmemo():
    listA = []
    for i in range(1, 10):
        listA.append(i)  # listにiを追加
    else:
        tupleA = tuple(listA)

    print("もとのリストは", listA)
    print("listA[:4]", listA[:4])
    print(tupleA[:4])

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    set1 = set(random.choices(letters, k=5))  # ASCIIからランダムに５こチョイス（var3.6から）
    set2 = set(random.choices(letters, k=5))
    print("1は", set1)
    print("2は", set2)
    print("１に'A'はあるか？", 'A' in set1)
    print("set1 & set2", set1 & set2)
    print("set1 | set2", set1 | set2)


def dictmemo():
    reco = {
        "A": 72, "B": 65, "C": 100, "D": 56, "E": 83, "F": 66
    }
    sum = 0
    for i in reco.values():
        sum += i
    ave = sum / len(reco)
    fmt = "|{0:<3}|{1:>4}|{2:>5}|"  # ３桁左寄せ　４桁右寄せ　５桁右寄せ
    fmt2 = "平均は{0:>3}点"
    print(fmt2.format(round(ave, 2)))
    for name, i in sorted(reco.items()):
        sub = i - ave
        sub = round(sub, 1)  # 小数点１桁に丸める
        print(fmt.format(name, i, sub))  # fmtで作った書式をformatで使用


if __name__ == '__main__':
    listmemo()
    print("\nこっからdict")
    dictmemo()
