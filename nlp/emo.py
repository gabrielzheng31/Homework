# -*- coding: utf-8 -*-

import thulac
import xml.dom.minidom

dict = []
emo_dict = {}
sen_result = []

with open("BosonNLP_sentiment_score.txt", "r") as f:
    for line in f.readlines():
        tmp = line.split()
        if len(tmp)!=0:
            dict.append(tmp[0])
            emo_dict[tmp[0]] = tmp[1]
            
#with open("dict", "w") as g:
#    for word in dict:
#        g.write(word+"\n")

thulac = thulac.thulac(user_dict='dict')
     
dom = xml.dom.minidom.parse('ipad.xml')
root = dom.documentElement
sentence = root.getElementsByTagName('sentence')
for line in sentence:
    score = 0
    tmp = {}
    #tmp['id'] = line.getAttribute("id")
    tmp['opinionated'] = line.getAttribute("opinionated")
    list = thulac.cut(line.firstChild.data)
    for word in list:
        score += float(emo_dict.get(word[0], 0))
    score /= len(list)
    tmp['score'] = score
    sen_result.append(tmp)
    
print(sen_result)
