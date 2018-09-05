import sys
import urllib.request
import re

#そのままopenすると403で弾かれるのでfirefoxに偽造して引っ張ってくる
f = urllib.request.Request(
    'https://gihyo.jp/dp', headers={'User-Agent': 'Mozilla/5.0'})
f = urllib.request.urlopen(f)

def header():
    encord = f.info().get_content_charset(failobj="utf-8")#headerからエンコーディングを見つけるメソッド
    print('headerから取ってきたencording:', encord, file=sys.stderr)  #標準エラー出力として標準出力とは別に出力
    text = f.read().decode(encord)
    print(text)

def meta():
    bytes_content = f.read()  #とりまバイト型で変数に格納する
    #大抵charsetは冒頭にくる（はず！）ので最初の1024バイトだけ変換しとく
    #残りはU+FFFD（REPLACEMENT CHARACTER）に置き換えて例外を発生させないように
    scan_text = bytes_content[:1024].decode('ascii', errors='replace')
    
    #デコードした部分から正規表現でcharsetを抜き出す
    match = re.search(r'charset=["\']?([\w-]+)', scan_text)
    if match:
        encord = match.group(1)
    else:
        encord = 'utf-8'
    
    print('meta情報から取ってきたencording:', encord, file=sys.stderr)
    text = bytes_content.decode(encord) #複数回リードするのはダメ？
    print(text)

if __name__ == '__main__':
    meta()
    
    '''
    a = input("headから取る？metaから取る？")
    if a == "meta":
        meta()
    else:
        header()
    '''