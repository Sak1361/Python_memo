import MeCab
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import urllib3

fname = 'abe.txt'
fname_parsed = 'abe.txt.mecab'

def to_mecab():
    #「fname」を形態素解析して[fname_parsed]に保存する
    with open(fname) as data_file, \
            open(fname_parsed, mode='w') as out_file:

        mecab = MeCab.Tagger('-d /var/lib/mecab/dic/mecab-ipadic-neologd')
        out_file.write(mecab.parse(data_file.read()))

def make_lines():
    '''
    各形態素を
    ・表層形（surface）
    ・基本形（base）
    ・品詞（pos）
    ・品詞細分類1（pos1）
    の4つをキーとする辞書に格納し、1文ずつ、この辞書のリストとして返す

    戻り値：
    1文の各形態素を辞書化したリスト
    '''
    with open(fname_parsed) as file_parsed:
        morphemes = []
        for line in file_parsed:
            cols = line.split('\t')# 表層形はtab区切り、それ以外は','区切りでバラす
            if(len(cols) < 2):
                raise StopIteration     # 区切りがなければ終了
            res_cols = cols[1].split(',')

            # 辞書作成、リストに追加
            morpheme = {
                'surface': cols[0],
                'base': res_cols[6],
                'pos': res_cols[0],
                'pos1': res_cols[1]
            }
            morphemes.append(morpheme)

            # 品詞細分類1が'句点'なら文の終わりと判定
            if res_cols[1] == '句点':
                yield morphemes
                morphemes = []

def sloth():
    import urllib3
    from bs4 import BeautifulSoup

    slothlib_path = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
    http = urllib3.PoolManager()
    #↑urlib3系のおまじない
    slothlib_file = http.request('GET', slothlib_path)
    soup = BeautifulSoup(slothlib_file.data, 'lxml')
    soup = str(soup).split()  # soupは文字列じゃないので注意
    #SlothLibに存在しないストップワードを自分で追加↓
    mydict = ['いる', '内閣総理大臣', 'おり', 'ない', 'あり', 'ある', 'いく', 'なっ', 'する', 'あっ']
    soup.extend(mydict)
    return soup


# 形態素解析
to_mecab()

# Counterオブジェクトに単語をセット
word_counter = Counter()
for line in make_lines():
    for morpheme in line:
        if morpheme['pos'] == '動詞' or morpheme['pos'] == '名詞' or morpheme['pos'] == '形容詞':
            if len(morpheme['surface']) > 3:
                if not morpheme['surface'] in sloth():
                    #リストに入れないと、１文字づつカウントしてしまう
                    word_counter.update([morpheme['surface']])
# 頻度上位30語の取得
size = 30
#ｓｉｚｅの数だけ、上位の単語を表示する
list_word = word_counter.most_common(size)
print(list_word)

# 単語（x軸用）と出現数（y軸用）のリストに分解
list_zipped = list(zip(*list_word))
words = list_zipped[0]
counts = list_zipped[1]

# グラフで使うフォント情報(デフォルトのままでは日本語が表示できない)
fp = FontProperties(
    fname='/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf'
)

# 棒グラフのデータ指定
plt.bar(
    range(0, size),     # x軸の値（0,1,2...9）
    counts,             # それに対応するy軸の値
    align='center'      # x軸における棒グラフの表示位置
)

# x軸のラベルの指定
plt.xticks(
    range(0, size),     # x軸の値（0,1,2...
    words,              # それに対応するラベル
    fontproperties=fp   # 使うフォント情報
)

# x軸の値の範囲の調整
plt.xlim(
    xmin=-1, xmax=size  # -1〜10（左右に1の余裕を持たせて見栄え良く）
)

# グラフのタイトル、ラベル指定
plt.title(
    '37. 頻度上位30語',    # タイトル
    fontproperties=fp   # 使うフォント情報
)
plt.xlabel(
    '出現頻度が高い30語',  # x軸ラベル
    fontproperties=fp   # 使うフォント情報
)
plt.ylabel(
    '出現頻度',         # y軸ラベル
    fontproperties=fp   # 使うフォント情報
)

# グリッドを表示
plt.grid(axis='y')

# 表示
plt.show()
