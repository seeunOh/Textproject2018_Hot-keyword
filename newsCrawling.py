import requests                 # url 요청
from lxml.html import parse     # html양식으로 파싱
from io import StringIO

#date = 20181205

def crawl(date):
    politics_url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=100&date=' + str(
        date)
    economy_url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=101&date=' + str(
        date)
    social_url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=102&date=' + str(
        date)
    culture_url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=' + str(
        date)
    world_url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=104&date=' + str(
        date)

    kind = [politics_url, economy_url, social_url, culture_url, world_url]
    kind_text = ['정치', '경제', '사회', '생활', '세계', ]

    # 네이버 뉴스 웹 크롤링
    for i in range(0, 5):
        text = requests.get(kind[i]).text

        text_source = StringIO(text)
        parsed = parse(text_source)

        doc = parsed.getroot()

        tables = doc.findall('.//table')
        table = tables[0]

        uls = table.findall('.//ol')
        ul = uls[0]

        a = ul.findall('.//a')

        # 뉴스 기사 리스트에 저장
        news_list = []
        for news in a:
            newstext = news.text_content().strip()
            if newstext != "" and newstext != "동영상기사":
                news_list.append(newstext)

        # 뉴스 기사 불필요 내용 제거
        result_politics = []
        for k in range(0, len(news_list)):
            temp = str(news_list[k])
            where = temp.find(']')
            where2 = temp.find('(')

            if where != -1 and where2 != -1 and where < len(temp) / 2:  # (,]둘다 잇
                result_politics.append(temp[where + 1:where2])

            elif where != -1 and where < len(temp) / 2:  # ]잇
                result_politics.append(temp[where + 1:])

            elif where2 != -1 and where < len(temp) / 2:  # (잇
                result_politics.append(temp[:where2])

            else:  # 둘다 없
                result_politics.append(temp)

        # 뉴스기사 텍스트에 분야별로 저장
        cnt2 = 1
        politics_file = open(kind_text[i] + ".txt", "w")
        print('------------------------' + kind_text[i] + '------------------------')
        for a in result_politics:
            print(cnt2, '.', a)
            politics_file.write(a.lstrip())
            politics_file.write('\n')
            cnt2 += 1
        politics_file.close()

    return




