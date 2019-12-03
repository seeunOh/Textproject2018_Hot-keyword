from konlpy.tag import Twitter
from collections import Counter
from nltk import bigrams

kind_text = ['정치', '경제', '사회', '생활', '세계']

hotkey = []
for i in range(0, 5):
    file = open(kind_text[i]+".txt", "r")
    lines = file.read()
    newstext = lines.split('\n')
    file.close()

    twitter = Twitter()
    sentences_tag = []
    for sentence in newstext:
        morph = twitter.pos(sentence)
        sentences_tag.append(morph)
        # print(morph) #형태소
        # print('-'*30)

    # print(sentences_tag) #전체의 단어(형태소 모으기)
    # print(len(sentences_tag))
    # print('\n'*3)

    noun_adj_list = []
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective']:
                noun_adj_list.append(word)
    # print('------------')
    # print(noun_adj_list)    #명사,형용사만 모으기

    counts = Counter(noun_adj_list)
    # print(counts)
    # print(counts.most_common(20))

    # 형태소 분석후 명사,형용사

    # print('-----바이그램---')
    gram_list = list(bigrams(noun_adj_list))
    # print(gram_list)

    biresult = []
    for i in range(0, len(gram_list)):
        biresult.append(gram_list[i][0] + " " + gram_list[i][1])
    # print(biresult)

    result2 = set([x for x in biresult if biresult.count(x) > 1])
    # print('----중복 값 찾기----')
    result2 = list(result2)
    # print(result2)

    if not result2:
        tempResult = counts.most_common(10)
        for i in tempResult:
            result2.append(i[0])

    # print('----중복 값 없을시 그냥----')
    # print(result2)

    if len(result2) > 10:
        result2 = result2[:10]

    elif len(result2) < 10:
        tempResult2 = counts.most_common(10-len(result2))
        for j in tempResult2:
            result2.append(j[0])

    # print('---최종 핫 키워드---')
    #print(result2)
    hotkey.append(result2)

print(hotkey)


