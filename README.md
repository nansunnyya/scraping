# scraping์ฐ์ต(with python)

### ๐ ๊ตฌํ ๋ด์ฉ

### 1. scraping_analysis(์นด์นด์คํก ๋ํ๋ด์ฉ ๋ถ์)
    ํ์ผ: kakao_analysis.py

  ๐ ์นด์นด์คํก ๋ํ๋ด์ฉ์ ๋ถ์ํ์ฌ ์์ฃผ ์ธ๊ธ๋ ๋จ์ด๋ฅผ ๊ตฌ๋ฆ ํํ๋ก ๋ฐ์ดํฐ ์๊ฐํ ํ๊ธฐ

![image](https://user-images.githubusercontent.com/76245273/113110501-1d2e4300-9242-11eb-8d92-f0049f250940.png)

<br/>

### 2. scraping_img(์ด๋ฏธ์ง ๊ฐ์ ธ์์ local์ ์ ์ฅํ๊ธฐ)
    ํ์ผ: getImg.py

  ๐ BeautifulSoup์ ์ฌ์ฉํ์ฌ ์๋์ผ๋ก ํ์ด์ง ์คํฌ๋กค ๋ค์ด
  
  ๐ ์ด๋ฏธ์ง numberingํ์ฌ local์ ์ ์ฅ
  
![image](https://user-images.githubusercontent.com/76245273/113113869-b6128d80-9245-11eb-8db7-be516b70b77c.png)

<br/>

### 3. scraping_news(ํน์  ์์  ๋ด์ค ์ ๋ณด ๊ฐ์ ธ์์ excelํ์ผ๋ก ์ ์ฅํ๊ธฐ)
    ํ์ผ:news.py
  ๐ BeautifulSoup, selenium์ ์ฌ์ฉํ์ฌ ํน์  ๊ฒ์์ด์ ๋ํ ๋ด์ค ์ ๋ณด ๊ฐ์ ธ์ค๊ธฐ
  
  ๐ ๊ฐ์ ธ์จ ์ ๋ณด๋ฅผ excelํ์ผ๋ก ์ ์ฅ
  
![image](https://user-images.githubusercontent.com/76245273/113115019-f1fa2280-9246-11eb-845a-00d37c542483.png)

<br/>

### 4. scraping_sendEmail(๋ด ์ด๋ฉ์ผ์ ๋ก๊ทธ์ธํ์ฌ ๋ฉ์ผ ๋ณด๋ด๊ธฐ)
    ํ์ผ:myemail.py
  
  ๐ ์ด๋ฉ์ผ ๋ก๊ทธ์ธ ํ๊ธฐ
  
  ๐ ๋ฉ์ผ ์ ๋ณด(๋ฐ๋ ์ฌ๋ ์ ๋ณด, ๋ณด๋ด๋ ์ฌ๋ ์ ๋ณด, ๋ฉ์ผ ์ ๋ชฉ, ๋ฉ์ผ ๋ด์ฉ) ์ค์  & ํ์ผ ์ฒจ๋ถํ์ฌ ๋ฉ์ผ๋ณด๋ด๊ธฐ
