driver = webdriver.Chrome('C:/Users/Sunhee/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=%EA%B3%B0%EB%8F%8C%EC%9D%B4+%ED%91%B8%EC%9A%B0&oquery=%ED%91%B8%EC%9A%B0&tqi=hbdh3sp0YiRssRAdU2hssssssEl-145076")
time.sleep(5) #5초동안 페이지 로딩 기다리기

#페이지 스크롤 다운
body = driver.find_element_by_css_selector('body')
for i in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

getImgs = soup.select('div > a > img')
num=1
for getImg in getImgs:
    print(getImg['src'])
    img = getImg['src']
    dload.save(img, f'img/c{num}.jpg')
    num+=1

driver.quit() # 끝나면 닫아주기
