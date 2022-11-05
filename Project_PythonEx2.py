import csv
import numpy as np
import re

f = open('10월역별.csv', 'r', encoding = 'UTF8')
data = csv.reader(f)

sub_num_on = []
sub_num_off = []
idx_num_on = []
asc_num_on = []
idx_num_off = []
asc_num_off = []
station_name = []
ipt_num = 0

next(data)

for row in data:
        sub_num_on.append(int(row[4]))
        sub_num_off.append(int(row[5]))
        station_name.append(row[3])

idx_num_on = np.argsort(np.array(sub_num_on))[::-1]
asc_num_on = np.sort(np.array(sub_num_on))[::-1]

idx_num_off = np.argsort(np.array(sub_num_off))[::-1]
asc_num_off = np.sort(np.array(sub_num_off))[::-1]

print("1. 승하차량 1위 보기,  2. 특정 역의 승차순위,  3. 특정 역의 하차순위")
while ipt_num != "1" and ipt_num != "2" and ipt_num != "3":
        ipt_num = input("1 ~ 3 중 하나를 입력해주세요 : ")

        if ipt_num == "1":
                print("승차량 1위: ", asc_num_on[0] ,station_name[idx_num_on[0]])
                print("하차량 1위: ", asc_num_off[0] ,station_name[idx_num_off[0]])
        elif ipt_num == "2":
                ipt_stname = input("역 이름을 입력해주세요 : ")
                for i in range(0, len(station_name)):
                        if ipt_stname != station_name[idx_num_on[i]]:
                                continue

                        else:      
                               print(ipt_stname, " : ", i + 1 ,"/" ,len(station_name), "위, ", asc_num_on[i], "명")
                               break
        elif ipt_num == "3":
                ipt_stname = input("역 이름을 입력해주세요 : ")
                for i in range(0, len(station_name)):
                        if ipt_stname != station_name[idx_num_off[i]]:
                                continue
                        else:
                                print(ipt_stname, " : ", i + 1, "/" , len(station_name),
                                      "위, ", asc_num_off[i], "명")
                                break
                        
        else:
                print("잘못된 입력입니다.")
                
