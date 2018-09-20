import MeCab
import re #正規表現

m = MeCab.Tagger('-Owakati')    #分かち書き
n = MeCab.Tagger('-Ochasen')    #形態素解析
a = input("分かち書き：")
wakati = m.parse(a).strip() #stripで文字除去、引数なしは空文字除去
keitai = n.parse(a)
print(type(wakati),wakati)
print(keitai)