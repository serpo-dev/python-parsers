import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = 'https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji'
FILE_NAME = 'result.txt'


def parse(url=URL_TEMPLATE):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    kanji_names = soup.find_all('a', {'class': 'extiw'})
    text_arr = []
    for kanji in kanji_names:
        text_arr.append(kanji.text[0])
    return text_arr


result_arr = parse(URL_TEMPLATE)
result_arr.pop()
result_arr.pop()
result_str = "','".join(result_arr)
result_str = "'" + result_str + "'"
with open(FILE_NAME, 'a+', encoding="utf-8") as f:
    f.write(result_str)

'''
 w  write mode
r  read mode
a  append mode

w+  create file if it doesn't exist and open it in (over)write mode
    [it overwrites the file if it already exists]
r+  open an existing file in read+write mode
a+  create file if it doesn't exist and open it in append mode
'''
