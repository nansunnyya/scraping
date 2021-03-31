
from wordcloud import WordCloud

from PIL import Image
import numpy as np


text=''
with open("KakaoTalk_20201002_0050_17_865_group.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text+=line.split('] ')[2].replace('ㅠㅠ','').replace('그냥','').replace('이모티콘\n','').replace('사진','').replace('삭제된 메시지입니다.','').replace('저도','').replace('저는','')

print(text)



mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/나눔고딕.ttf',background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")



