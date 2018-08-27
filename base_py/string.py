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
    reco = {"A": 72, "B": 65, "C": 100, "D": 56, "E": 83, "F": 66}
    sum = 0
    for i in reco.values():
        sum += i
    ave = sum / len(reco)
    fmt = "|{0:<3}|{1:>4}|{2:>5}|"  # ３桁左寄せ　４桁右寄せ　５桁右寄せ
    fmt2 = "平均は{0:>3}点"
    print("キーは", reco.keys())
    print("値は", reco.values())
    print(fmt2.format(round(ave, 2)))
    for name, i in sorted(reco.items()):
        sub = i - ave
        sub = round(sub, 1)  # 小数点１桁に丸める
        print(fmt.format(name, i, sub))  # fmtで作った書式をformatで使用

def stringmemo():
    letters = 'abcdefghijklmnopqrstuvwxyz,'
    randtext = "".join(random.choices(letters, k=50))
    print("生成した文字列は", randtext)
    print("文字数は", len(randtext))
    print("34番目の文字は", randtext[33])
    sptext = randtext.split(",")
    print(sptext)
    randtext = randtext.replace(",", "")
    print("','を除いた文字数は", len(randtext))
    count = {}
    for i in randtext:
        li = i.upper()
        if li in count:
            count[li] += 1
        else:
            count[li] = 1
    print("３個以上被ったのは")
    for j, k in sorted(count.items()):
        if k >= 3:
            print("|{0:>2}は{1}回|".format(j, k), end="")
    else:
        print()


if __name__ == '__main__':
    listmemo()
    print("\n---こっからdict---\n")
    dictmemo()
    print("\n---こっから文字列操作---\n")
    stringmemo()
