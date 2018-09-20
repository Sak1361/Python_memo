import MeCab
import re
import collections #counterを使うため
import codecs   #unicodeError対策

def re_def(filepass):
    with codecs.open(filepass, 'r', encoding='utf-8', errors='ignore')as f:
    #with open(filepass, 'r')as f:
        l = ""
        re_half = re.compile(r'[!-~]')  # 半角記号,数字,英字
        re_full = re.compile(r'[︰-＠]')  # 全角記号
        re_full2 = re.compile(r'[、。・’〜：＜＞＿｜「」｛｝【】『』〈〉“”○〔〕…――――◇]')  # 全角で取り除けなかったやつ
        re_other = re.compile(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+')
        re_n = re.compile(r'\n')  # 改行文字
        re_space = re.compile(r'[\s+]') #１以上の空白文字
        for line in f:
            line = re_half.sub("", line)
            line = re_full.sub("", line)
            line = re_full2.sub("", line)
            line = re_other.sub("", line)
            line = re_space.sub("", line)
            line = re_n.sub("", line)
            l += line
    return l

s = 0; e = 20000; stops = 200000
def owakati(all_words):
    global s, e, stops
    tagger = MeCab.Tagger()
    w = ""
    wakatifile = []
    while True:
        w += all_words[s:e]
        wakatifile.extend(tagger.parse(w).split("\n"))  #appendだとlistの中にlistを作るから
        s = e
        e += 20000
        print(s)
        if e > len(all_words):
            break
        elif e > stops:
            break
    return wakatifile

def count(filepass):
    global s, e, stops
    word_list = []
    dicts = {}  # 単語をカウントする辞書
    all_words = re_def(filepass)  #無駄な記号とかを取り除く
    print("無駄排除終了")
    l = len(all_words)
    if l > 200000:
        for i in all_words:
            word_list = []
            wakati = owakati(all_words) #分かち書きアンド形態素解析
            #tagger = MeCab.Tagger()
            #wakati = tagger.parse(all_words).split("\n")
            #with open("tmp_wakati2.txt", "w") as f:
            #    f.write(str(wakati))
            for addlist in wakati:
                addlist = re.split('[\t,]', addlist)  # 空白と","で分割
                if addlist[0] == 'EOS' or addlist[0] == '' or addlist[0] == 't' or addlist[0] == 'ー':
                    pass
                elif addlist[1] == '名詞' and addlist[2] == '一般' or addlist[1] == '名詞' and addlist[2] == '固有名詞':  # 単語リストに追加
                    word_list.extend(addlist)
            for count in word_list:
                if count[0] not in dicts:
                    dicts.setdefault(count[0], 1)
                else:
                    dicts[count[0]] += 1
            #メモリ解放
            for n, c in dicts.items():
                if c < 100:
                    del n, c
            if (l - stops) < 0:
                del wakati,word_list
                break
            else:
                stops += 200000
    return dicts

def plot(countedwords):
    #import numpy as np
    import matplotlib.pyplot as plt
    counts = {}
    c = 1
    show = 30 #何件表示する？
    for k, v in sorted(countedwords.items(), key=lambda x: x[1], reverse=True):  # 辞書を降順に入れる
        d = {str(k): int(v)}
        counts.update(d)
        c += 1
        if c > show:
            with open("result_wakati.txt", "w") as f:
                f.write(str(counts))
            break
    plt.figure(figsize=(15, 5)) #これでラベルがかぶらないくらい大きく
    plt.title('頻繁に発言したワードベスト'+str(show), size=16)
    plt.bar(range(len(counts)), counts.values(), align='center')
    plt.xticks(range(len(counts)), list(counts.keys()))
    # 棒グラフ内に数値を書く
    for x, y in zip(range(len(counts)), counts.values()):
        plt.text(x, y, y, ha='center', va='bottom')
    plt.tick_params(width=2, length=10) #ラベル大きさ 
    plt.tight_layout()  #整える
    plt.show()

if __name__ == '__main__':
    c = count("abe/2018kokkai.txt")
    plot(c)
