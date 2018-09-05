import re
from html import unescape

with open('dp.html') as f:
    html = f.read()

#*?と*は同じだがなるべく短い文字列には*?を用いる
s = re.findall(r'<a itemprop = "url".*?</ul>\s*</a></li>', html, re.DOTALL)
print(s)    #for文回らないと思ったらそもそもヒットしてねぇw
for partial_html in s:
    #URLをitemprop = "url"をもつaタグのhrefから取ってくる
    url = re.search(r'<a itemprop = "url" href= "(.*?)" >', partial_html).group(1)
    url = 'https://gihyo.jp' + url  #後ろにつなげていく
    #本のタイトルをitemprop = "name"を持つｐタグから持ってくる
    title = re.search(r'<p itemprop = "name".*?</p>', partial_html).group(0)
    title = title.replace('<br/>', '')  #
    title = re.sub(r'<.*?>', '', title)
    title = unescape(title)
    print(url, title)