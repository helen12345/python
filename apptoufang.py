# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 16:07:15 2018

@author: hanhong
"""
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 添加层
 import pandas as pd 
 import regex
 import time
 import pickle
 from functools import reduce
 beijing = pd.read_csv(r'C:\Users\admin\Desktop\AppTouFang\beijing2.csv')
 buyuser = pd.read_csv(r'C:\Users\admin\Desktop\buyuser.csv')
 beijing['y'] = beijing['imei'].apply(lambda x: 1 if x in list(buyuser['imei']) else 0)
 beijing_buy = beijing[ beijing['y']==1]
 hosthc = pd.read_csv(r'C:\Users\admin\Desktop\AppTouFang\hosthc.csv')
 hosthc['A'] = hosthc['A'].apply( lambda x: ';'+x)
 beijing_buy['site_pipei'] = beijing_buy['site']
 
#==============================================================================
# class BaseReplacer:
#     def __init__(self, pattern_replace_pair_list=[]):
#         self.pattern_replace_pair_list = pattern_replace_pair_list
# 
#     def transform(self, text):
#         for pattern, replace in self.pattern_replace_pair_list:
#             try:
#                 text = regex.sub(pattern, replace, text)
#             except:
#                 pass
#         return text
#     
# class WordReplacer(BaseReplacer):
#     def __init__(self):
#         self.pattern_replace_pair_list =  [ tuple((hosthc['A'][i],hosthc['site'][i])) for i in range(len( hosthc)) ]
# 
# processor = WordReplacer()
# tic = time.time()
# beijing_buy['site_pipei'] = beijing_buy['site_pipei'].apply(processor.transform)
# toc = time.time()
# print('vectorized version:' +str((toc - tic)*1000)  +'ms')
#==============================================================================

#==============================================================================
# c['tianmao']= c['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
# for i in range(len( x.strip('#').split(';'))) if 'tianmao' in x.strip('#').split(';')[i]] )
# 
# c['vivo']= c['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
# for i in range(len( x.strip('#').split(';'))) if 'vivo' in x.strip('#').split(';')[i]] )
#==============================================================================
    
#提取对应网站信息  
beijing['farfetch']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'farfetch' in x.strip('#').split(';')[i]] )

#求pv和
beijing['farfetch2'] = beijing['farfetch'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

#del(c['taobao'])
beijing['ofashion']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'ofashion' in x.strip('#').split(';')[i]] )

#求pv和
beijing['ofashion2'] = beijing['ofashion'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

tic = time.time()
beijing['wandougongzhu']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'wandougongzhu' in x.strip('#').split(';')[i]] )
toc = time.time()
print('vectorized version:' +str((toc - tic)*1000)  +'ms') 
#求pv和
beijing['wandougongzhu2'] = beijing['wandougongzhu'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

tic = time.time()
beijing['kaola']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'kaola' in x.strip('#').split(';')[i]] )
toc = time.time()
print('vectorized version:' +str((toc - tic)*1000)  +'ms') 
#求pv和
beijing['kaola2'] = beijing['kaola'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

tic = time.time()
beijing['secoo']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'secoo' in x.strip('#').split(';')[i]] )
toc = time.time()
print('vectorized version:' +str((toc - tic)*1000)  +'ms') 
#求pv和
beijing['secoo2'] = beijing['secoo'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

tic = time.time()
beijing['xiaohongshu']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'xiaohongshu' in x.strip('#').split(';')[i]] )
toc = time.time()
print('vectorized version:' +str((toc - tic)*1000)  +'ms') 
#求pv和
beijing['xiaohongshu2'] = beijing['xiaohongshu'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

tic = time.time()
beijing['msparis']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'msparis' in x.strip('#').split(';')[i]] )
toc = time.time()
print('vectorized version:' +str((toc - tic)*1000)  +'ms') 
#求pv和
beijing['msparis2'] = beijing['msparis'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))


tic = time.time()
beijing['yi23']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'yi23' in x.strip('#').split(';')[i]] )
toc = time.time()
print('vectorized version:' +str((toc - tic)*1000)  +'ms') 
#求pv和
beijing['yi232'] = beijing['yi23'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))



tic = time.time()
beijing['goshare2']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'goshare2' in x.strip('#').split(';')[i]] )
toc = time.time()
print('vectorized version:' +str((toc - tic)*1000)  +'ms') 
#求pv和
beijing['goshare22'] = beijing['goshare2'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

tic = time.time()
beijing['soyoung']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'soyoung' in x.strip('#').split(';')[i]] )
toc = time.time()
print('vectorized version:' +str((toc - tic)*1000)  +'ms') 
#求pv和
beijing['soyoung2'] = beijing['soyoung'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))


##########优先级中


beijing['airbnb']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'airbnb' in x.strip('#').split(';')[i]] )
#求pv和
beijing['airbnb2'] = beijing['airbnb'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))



beijing['agoda']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'agoda' in x.strip('#').split(';')[i]] )
#求pv和
beijing['agoda2'] = beijing['agoda'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))


beijing['tripadvisor']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'tripadvisor' in x.strip('#').split(';')[i]] )
#求pv和
beijing['tripadvisor2'] = beijing['tripadvisor'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

beijing['itunes']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'itunes' in x.strip('#').split(';')[i]] )
#求pv和
beijing['itunes2'] = beijing['itunes'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))


########优先级低
beijing['enjoy']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'enjoy' in x.strip('#').split(';')[i]] )
#求pv和
beijing['enjoy2'] = beijing['enjoy'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

beijing['yhouse']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'yhouse' in x.strip('#').split(';')[i]] )
#求pv和
beijing['yhouse2'] = beijing['yhouse'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

###########自己加
beijing['diditaxi']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'diditaxi' in x.strip('#').split(';')[i]] )
#求pv和
beijing['diditaxi2'] = beijing['diditaxi'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

beijing['apple']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'apple' in x.strip('#').split(';')[i]] )
#求pv和
beijing['apple2'] = beijing['apple'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))

beijing['taobao']= beijing['site'].apply( lambda x:  [x.strip('#').split(';')[i] 
for i in range(len( x.strip('#').split(';'))) if 'taobao' in x.strip('#').split(';')[i]] )
#求pv和
beijing['taobao2'] = beijing['taobao'].apply( lambda x : 0 if x == [] else 
 reduce( lambda x,y: x+y, [int(x[i].split(':')[-1]) for i in range(len(x))]))


output = open(r'F:\pythonfile\data\apptoufang\beijing2.pkl', 'wb')
pickle.dump(beijing, output)
output.close()

#删掉网站名称
for site in ['farfetch','ofashion','wandougongzhu','kaola','secoo','xiaohongshu','msparis','yi23',
             'goshare2','soyoung','airbnb','agoda','tripadvisor','itunes','enjoy','yhouse']:
    del( beijing[site])
#总pv
beijing['all_pv'] = beijing.iloc[:,3:].sum(axis = 1)
beijing_buy = beijing[ beijing['y']==1]


register = pd.read_csv(r'C:\Users\admin\Desktop\AppTouFang\register.csv')
beijing['register'] = beijing['imei'].apply(lambda x: 1 if x in list(register['imei']) else 0)

beijing['kaola|xiaohongshu'] = beijing[['kaola2','xiaohongshu2']].sum(axis = 1)
####转化成 0 1
beijing['kaola|xiaohongshu_1_0'] = beijing['kaola|xiaohongshu'].apply( lambda x: 1 if x>0 else 0)



#==============================================================================
# for site in ['diditaxi','apple','taobao']:
#    del(beijing[site])
#==============================================================================
    #==============================================================================
#     
# pattern_replace_pair_list = []
# for i in range(len( hosthc)):
#      li.append( tuple((hosthc['A'][i],hosthc['site'][i])))
#==============================================================================
     
#pattern_replace_pair_list = [ tuple((hosthc['A'][i],hosthc['site'][i])) for i in range(len( hosthc)) ]
