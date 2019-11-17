# -*- coding: utf-8 -*-

##1390개의 정류장
##1, 뭐해야하믄 데이터 슬라이싱
##2. 데이터 필요없는거 제거
##3. 데이터 저장
##4. 데이터 특정 추출
##   A. 월화수목금토일 해서 주로 사람들이 어디에 많이 가는지
##   B. 어디에 부족해지고 어디에 과포화가 될 것인지 예상

import os
from IPython.display import display
import numpy as np
from pandas.tests.frame.test_validate import dataframe
import bike
import pandas
import json

path_dir = './bike'
file_list = os.listdir(path_dir)
file_list.sort()

list_file=[]


for i in range(0,len(file_list)):
    list_file+=[file_list[i].replace('.json','')]




dataA = pandas.DataFrame(pandas.read_json('bike/'+list_file[144]+'.json'))
dataB = pandas.DataFrame(pandas.read_json('bike/'+list_file[287]+'.json'))

dataA_list = (dataA["parkingBikeTotCnt"])
dataB_list = (dataB["parkingBikeTotCnt"])

b=dataB_list-dataA_list



Totaldata_list =[0for i in range(0,1390)]
a=0

add_list =[0for i in range(0,1390)]

max = [0,0,0]

for i in range(1,143):
    dataA = pandas.DataFrame(pandas.read_json('bike/' + list_file[i-1] + '.json'))
    dataB = pandas.DataFrame(pandas.read_json('bike/' + list_file[i] + '.json'))
    dataA_list = (dataA["parkingBikeTotCnt"])
    dataB_list = (dataB["parkingBikeTotCnt"])

    for j in range(0,1390):
        add_list[j] = int(dataB_list[j]-dataA_list[j])
    for z in range(0,1390):
        a=Totaldata_list[z]+add_list[z]
        Totaldata_list[z] = a
print(Totaldata_list)

for i in range(0,1390):
    if max[0]<Totaldata_list[i]:
        max[0] = Totaldata_list[i]
    elif max[1] < Totaldata_list[i]:
        max[1] = Totaldata_list[i]
    elif max[2] < Totaldata_list[i]:
        max[2] = Totaldata_list[i]


print(max[0])
print("\n")
print(max[1])
print("\n")
print(max[2])

max1=max[0]
max2=max[1]
max3=max[2]
m1=0
m2=0
m3=0
for i in range(0,1390):
    if max1 ==Totaldata_list[i]:
        m1 = i
        print(i)
        print("\n")
    if max2 == Totaldata_list[i]:
        m2 = i
        print(i)
        print("\n")
    if max3 == Totaldata_list[i]:
        m3 = i
        print(i)
        print("\n")
display(dataA.iloc[m1][4])
display(dataA.iloc[m1][5])
print("\n")
display(dataA.iloc[m2][4])
display(dataA.iloc[m2][5])
print("\n")
display(dataA.iloc[m3][4])##4,5
display(dataA.iloc[m3][5])
