# scraping연습(with python)

### 구현 내용

#### 1. scraping_analysis(카카오톡 대화내용 분석)
    파일: kakao_analysis.py

  카카오톡 대화내용을 분석하여 자주 언급된 단어를 구름 형태로 데이터 시각화 하기

![image](https://user-images.githubusercontent.com/76245273/113110501-1d2e4300-9242-11eb-8d92-f0049f250940.png)






#### 2. scraping_img(이미지 가져와서 local에 저장하기)
    파일: getImg.py

  1) BeautifulSoup을 사용하여 자동으로 페이지 스크롤 다운
  2) 이미지 numbering하여 local에 저장
  
![image](https://user-images.githubusercontent.com/76245273/113113869-b6128d80-9245-11eb-8db7-be516b70b77c.png)


#### 3. scraping_news(특정 시점 뉴스 정보 가져와서 excel파일로 저장하기)
    파일:news.py
  1)BeautifulSoup, selenium을 사용하여 특정 검색어에 대한 뉴스 정보 가져오기
  2)가져온 정보를 excel파일로 저장
  
![image](https://user-images.githubusercontent.com/76245273/113115019-f1fa2280-9246-11eb-845a-00d37c542483.png)


#### 4. scraping_sendEmail(내 이메일에 로그인하여 메일 보내기)
    파일:myemail.py
  
  1)이메일 로그인 후, 메일 정보 설정 후 파일 첨부하여 메일보내기
