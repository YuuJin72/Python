import csv
import numpy as np
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

f = open('10월시간대별.csv', 'r', encoding = 'UTF8')
data = csv.reader(f)

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#오전 승하차데이터 변수 선언
morning_geton = []
morning_getoff = []

#오후 승하차데이터 변수 선언
evening_geton = []
evening_getoff = []
station_name = []

item = 0
plt_Moron = []
plt_Station_Moron = []
plt_Moroff = []
plt_Station_Moroff = []
plt_Eveon = []
plt_Station_Eveon = []
plt_Eveoff = []
plt_Station_Eveoff = []

next(data)
next(data)


for row in data:
        #오전 승차
        for i in range(4, 15, 2):
                item = item + int(row[i])       
        morning_geton.append(item)
        item = 0

        #오전 하차
        for i in range(5, 16, 2):
                item = item + int(row[i])       
        morning_getoff.append(item)
        item = 0

        #오후 승차
        for i in range(32, 35, 2):
                item = item + int(row[i])       
        evening_geton.append(item)
        item = 0

        #오후 하차
        for i in range(33, 38, 2):
                item = item + int(row[i])       
        evening_getoff.append(item)
        item = 0

        #역이름 배열
        station_name.append(row[3])



#데이터 정렬을 위한 인덱스 작성(numpy 사용)
idx_morning_geton = np.argsort(np.array(morning_geton))[::-1]
idx_morning_getoff = np.argsort(np.array(morning_getoff))[::-1]
idx_evening_geton = np.argsort(np.array(evening_geton))[::-1]
idx_evening_getoff = np.argsort(np.array(evening_getoff))[::-1]

#데이터 내림차순 정렬(numpy 사용)
asc_morning_geton = np.sort(np.array(morning_geton))[::-1]
asc_morning_getoff = np.sort(np.array(morning_getoff))[::-1]
asc_evening_geton = np.sort(np.array(evening_geton))[::-1]
asc_evening_getoff = np.sort(np.array(evening_getoff))[::-1]

print("1. 아침 승차, 2. 아침 하차, 3. 저녁 승차, 4. 저녁 하차")
num = input("1 ~ 4중 하나를 입력하세요. : ")

if num == "1":
        for i in range(0,10):
                print(asc_morning_geton[i], station_name[idx_morning_geton[i]])
                plt_Moron.append(asc_morning_geton[i])
                plt_Station_Moron.append(station_name[idx_morning_geton[i]])
        plt.title('아침 승차인구')
        plt.bar(plt_Station_Moron, plt_Moron)
        plt.xlabel('Station')
        plt.ylabel('Number')
        plt.show()
        
elif num == "2":
        for i in range(0,10):
                print(asc_morning_getoff[i], station_name[idx_morning_getoff[i]])
                plt_Moroff.append(asc_morning_getoff[i])
                plt_Station_Moroff.append(station_name[idx_morning_getoff[i]])
        plt.title('아침 하차인구')
        plt.bar(plt_Station_Moroff, plt_Moroff)
        plt.xlabel('Station')
        plt.ylabel('Number')
        plt.show()
                
elif num == "3":
        for i in range(0,10):
                print(asc_evening_geton[i], station_name[idx_evening_geton[i]])
                plt_Eveon.append(asc_evening_geton[i])
                plt_Station_Eveon.append(station_name[idx_evening_geton[i]])
        plt.title('저녁 승차인구')
        plt.bar(plt_Station_Eveon, plt_Eveon)
        plt.xlabel('Station')
        plt.ylabel('Number')
        plt.show()

elif num == "4":
        for i in range(0,10):
                print(asc_evening_getoff[i], station_name[idx_evening_getoff[i]])
                plt_Eveoff.append(asc_evening_getoff[i])
                plt_Station_Eveoff.append(station_name[idx_evening_getoff[i]])
        plt.title('저녁 하차인구')
        plt.bar(plt_Station_Eveoff, plt_Eveoff)
        plt.xlabel('Station')
        plt.ylabel('Number')
        plt.show()
else:
        print('잘못 입력하셨습니다')


