import MeCab
import re  # 正規表現
import urllib3
from bs4 import BeautifulSoup

def sloth():
    slothlib_path = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
    http = urllib3.PoolManager() #urlib3系のおまじない
    slothlib_file = http.request('GET', slothlib_path)
    soup = BeautifulSoup(slothlib_file.data, 'lxml')
    soup = str(soup).split()  # soupは文字列じゃないので注意
    soup.pop(0) #htmlタグを殲滅せよ
    soup.pop()
    #SlothLibに存在しないストップワードを自分で追加↓
    mydict = ['内閣総理大臣', '安倍晋三', '君','先','いわば']
    soup.extend(mydict)
    return soup

def onesl():
    slothlib_path = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/OneLetterJp.txt'
    http = urllib3.PoolManager()  # urlib3系のおまじない
    slothlib_file = http.request('GET', slothlib_path)
    soup2 = BeautifulSoup(slothlib_file.data, 'lxml')
    soup2 = str(soup2).split()  # soupは文字列じゃないので注意
    soup2.pop(0)  # htmlタグを殲滅せよ
    soup2.pop()
    return soup2

def del_sloth(wakati_file):
    for stopwords in sloth():
        while stopwords in wakati_file:
            wakati_file.remove(stopwords)
    #print("第一段階しゅーりょー")
    """
        try:
            owakati.remove(stopwords)
        except ValueError:
            pass
    """ 
    for singleword in onesl():
        while singleword in wakati_file:
            wakati_file.remove(singleword)
    #print("第二段階しゅーりょー")
    """    
        try:
            owakati.remove(singleword)
            
        except ValueError:
            pass
    """
    return wakati_file

def wakati(filepass):
    re_half = re.compile(r'[!-~]')  # 半角記号,数字,英字
    re_full = re.compile(r'[︰-＠]')  # 全角記号
    re_full2 = re.compile(r'[、。・’〜：＜＞＿｜「」｛｝【】『』〈〉“”○〔〕]')
    re_other = re.compile(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+')
    re_n = re.compile('\n')  # 改行文字
    re_space = re.compile(r'[\s+]')

    result = ""
    with open(filepass, 'r', encoding='utf8') as f:
        #re.sub(置き換える表現、何に置き換えるか、元ファイル)
        for line in f:
            line = re_half.sub("", line)
            line = re_full.sub("", line)
            line = re_full2.sub("", line)
            line = re_other.sub("", line)
            line = re_space.sub("", line)
            line = re_n.sub("", line)
            result += line
    return result

def count(file):
    word_list = []  # 一般名詞を格納するリスト
    counts_dicts = {}  # 単語をカウントする辞書
    tagger = MeCab.Tagger()  # 引数なしで分かちと形態素解析両方
    tagger.parse('')  # unicodeErrerを防ぐためらしい
    mecabfile = tagger.parse(file).split()
    
    for tmp in mecabfile:
        # リストにするため空白と","で分割
        tmp.split('[\t,]')
        if tmp[0] == 'EOS' or tmp[0] == '' or tmp[0] == 't' or tmp[0] == 'ー':
            pass
        # 一般名詞の単語をリストに追加
        elif tmp[1] == '名詞' and tmp[2] == '一般':
            word_list.append(tmp)

    # 単語をカウント
    for count in word_list:
        # 辞書に入っていなければ値を1
        if count[0] not in counts_dicts:
            counts_dicts.setdefault(count[0], 1)

        #辞書に入っているならインクリメント
        else:
            counts_dicts[count[0]] += 1

    # 辞書を降順に出力
    for words, times in sorted(counts_dicts.items(), key=lambda x: - x[1]):
        #if times > 0:
        print(str(words) + ": " + str(times))


if __name__ == '__main__':
    owakati = wakati("result.txt")
    #with open("result.txt", 'w') as f:
    #    f.write(str(owakati))
    print("にゃーん")
    count(owakati)
