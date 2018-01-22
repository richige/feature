# Utility package -- use pip install cvutils to install
#import cvutils
# OpenCV bindings
import cv2
# To performing path manipulations
import csv
import matplotlib.pyplot as plt
import json

#1:1349
#2:660
#3:1859
#4:1349

#P1:77385
#P2:80370

#特徴量読み込み(1)
with open("/home/ubuntu/data/feature/no_team/features1.json", 'r') as f:
    f1_data = json.load(f)

#絶対値の最大値(初期値)
max_a_x=abs(f1_data['1']['average_X'])
max_a_y=abs(f1_data['1']['average_Y'])
max_d_x=abs(f1_data['1']['dispersion_X'])
max_d_y=abs(f1_data['1']['dispersion_Y'])

#f1_data内でソート
for i in range(int(len(f1_data))):
    frameNumber = i + 1
    if f1_data[str(frameNumber)]['average_X']!=None:
        if abs(f1_data[str(frameNumber)]['average_X'])>max_a_x:
            max_a_x=abs(f1_data[str(frameNumber)]['average_X'])
    if f1_data[str(frameNumber)]['average_Y']!=None:
        if abs(f1_data[str(frameNumber)]['average_Y'])>max_a_y:
            max_a_y=abs(f1_data[str(frameNumber)]['average_Y'])
    if f1_data[str(frameNumber)]['dispersion_X']!=None:
        if abs(f1_data[str(frameNumber)]['dispersion_X'])>max_d_x:
            max_d_x=abs(f1_data[str(frameNumber)]['dispersion_X'])
    if f1_data[str(frameNumber)]['dispersion_Y']!=None:
        if abs(f1_data[str(frameNumber)]['dispersion_Y'])>max_d_y:
            max_d_y=abs(f1_data[str(frameNumber)]['dispersion_Y'])

#特徴量読み込み(2)
with open("/home/ubuntu/data/feature/no_team/features2.json", 'r') as f:
    f2_data = json.load(f)

#f2_data内でソート
for i in range(int(len(f2_data))):
    frameNumber = i + 1
    if f2_data[str(frameNumber)]['average_X']!=None:
        if abs(f2_data[str(frameNumber)]['average_X'])>max_a_x:
            max_a_x=abs(f2_data[str(frameNumber)]['average_X'])
    if f2_data[str(frameNumber)]['average_Y']!=None:
        if abs(f2_data[str(frameNumber)]['average_Y'])>max_a_y:
            max_a_y=abs(f2_data[str(frameNumber)]['average_Y'])
    if f2_data[str(frameNumber)]['dispersion_X']!=None:
        if abs(f2_data[str(frameNumber)]['dispersion_X'])>max_d_x:
            max_d_x=abs(f2_data[str(frameNumber)]['dispersion_X'])
    if f2_data[str(frameNumber)]['dispersion_Y']!=None:
        if abs(f2_data[str(frameNumber)]['dispersion_Y'])>max_d_y:
            max_d_y=abs(f2_data[str(frameNumber)]['dispersion_Y'])

#特徴量読み込み(3)
with open("/home/ubuntu/data/feature/no_team/features3.json", 'r') as f:
    f3_data = json.load(f)

#f3_data内でソート
for i in range(int(len(f3_data))):
    frameNumber = i + 1
    if f3_data[str(frameNumber)]['average_X']!=None:
        if abs(f3_data[str(frameNumber)]['average_X'])>max_a_x:
            max_a_x=abs(f3_data[str(frameNumber)]['average_X'])
    if f3_data[str(frameNumber)]['average_Y']!=None:
        if abs(f3_data[str(frameNumber)]['average_Y'])>max_a_y:
            max_a_y=abs(f3_data[str(frameNumber)]['average_Y'])
    if f3_data[str(frameNumber)]['dispersion_X']!=None:
        if abs(f3_data[str(frameNumber)]['dispersion_X'])>max_d_x:
            max_d_x=abs(f3_data[str(frameNumber)]['dispersion_X'])
    if f3_data[str(frameNumber)]['dispersion_Y']!=None:
        if abs(f3_data[str(frameNumber)]['dispersion_Y'])>max_d_y:
            max_d_y=abs(f3_data[str(frameNumber)]['dispersion_Y'])

#特徴量読み込み(4)
with open("/home/ubuntu/data/feature/no_team/features4.json", 'r') as f:
    f4_data = json.load(f)

#f4_data内でソート
for i in range(int(len(f4_data))):
    frameNumber = i + 1
    if f4_data[str(frameNumber)]['average_X']!=None:
        if abs(f4_data[str(frameNumber)]['average_X'])>max_a_x:
            max_a_x=abs(f4_data[str(frameNumber)]['average_X'])
    if f4_data[str(frameNumber)]['average_Y']!=None:
        if abs(f4_data[str(frameNumber)]['average_Y'])>max_a_y:
            max_a_y=abs(f4_data[str(frameNumber)]['average_Y'])
    if f4_data[str(frameNumber)]['dispersion_X']!=None:
        if abs(f4_data[str(frameNumber)]['dispersion_X'])>max_d_x:
            max_d_x=abs(f4_data[str(frameNumber)]['dispersion_X'])
    if f4_data[str(frameNumber)]['dispersion_Y']!=None:
        if abs(f4_data[str(frameNumber)]['dispersion_Y'])>max_d_y:
            max_d_y=abs(f4_data[str(frameNumber)]['dispersion_Y'])

#特徴量読み込み(5)
with open("/home/ubuntu/data/feature/no_team/features5.json", 'r') as f:
    f5_data = json.load(f)

#f5_data内でソート
for i in range(int(len(f5_data))):
    frameNumber = i + 1
    if f5_data[str(frameNumber)]['average_X']!=None:
        if abs(f5_data[str(frameNumber)]['average_X'])>max_a_x:
            max_a_x=abs(f5_data[str(frameNumber)]['average_X'])
    if f5_data[str(frameNumber)]['average_Y']!=None:
        if abs(f5_data[str(frameNumber)]['average_Y'])>max_a_y:
            max_a_y=abs(f5_data[str(frameNumber)]['average_Y'])
    if f5_data[str(frameNumber)]['dispersion_X']!=None:
        if abs(f5_data[str(frameNumber)]['dispersion_X'])>max_d_x:
            max_d_x=abs(f5_data[str(frameNumber)]['dispersion_X'])
    if f5_data[str(frameNumber)]['dispersion_Y']!=None:
        if abs(f5_data[str(frameNumber)]['dispersion_Y'])>max_d_y:
            max_d_y=abs(f5_data[str(frameNumber)]['dispersion_Y'])

#特徴量読み込み(6)
with open("/home/ubuntu/data/feature/no_team/features6.json", 'r') as f:
    f6_data = json.load(f)

#f6_data内でソート
for i in range(int(len(f6_data))):
    frameNumber = i + 1
    if f6_data[str(frameNumber)]['average_X']!=None:
        if abs(f6_data[str(frameNumber)]['average_X'])>max_a_x:
            max_a_x=abs(f6_data[str(frameNumber)]['average_X'])
    if f6_data[str(frameNumber)]['average_Y']!=None:
        if abs(f6_data[str(frameNumber)]['average_Y'])>max_a_y:
            max_a_y=abs(f6_data[str(frameNumber)]['average_Y'])
    if f6_data[str(frameNumber)]['dispersion_X']!=None:
        if abs(f6_data[str(frameNumber)]['dispersion_X'])>max_d_x:
            max_d_x=abs(f6_data[str(frameNumber)]['dispersion_X'])
    if f6_data[str(frameNumber)]['dispersion_Y']!=None:
        if abs(f6_data[str(frameNumber)]['dispersion_Y'])>max_d_y:
            max_d_y=abs(f6_data[str(frameNumber)]['dispersion_Y'])


#n1_dataに特徴量挿入
n1_data={}
for i in range(int(len(f1_data))):
    frameNumber = i + 1
    n1_data[str(frameNumber)] = {}

for i in range(int(len(f1_data))):
    frameNumber = i + 1
    if f1_data[str(frameNumber)]['average_X']!=None:
        n1_data[str(frameNumber)]['average_X']=float(f1_data[str(frameNumber)]['average_X'])/float(max_a_x)
    else:
        n1_data[str(frameNumber)]['average_X']=None

    if f1_data[str(frameNumber)]['average_Y']!=None:
        n1_data[str(frameNumber)]['average_Y']=float(f1_data[str(frameNumber)]['average_Y'])/float(max_a_y)
    else:
        n1_data[str(frameNumber)]['average_Y']=None

    if f1_data[str(frameNumber)]['dispersion_X']!=None:
        n1_data[str(frameNumber)]['dispersion_X']=float(f1_data[str(frameNumber)]['dispersion_X'])/float(max_d_x)
    else:
        n1_data[str(frameNumber)]['dispersion_X']=None

    if f1_data[str(frameNumber)]['dispersion_Y']!=None:
        n1_data[str(frameNumber)]['dispersion_Y']=float(f1_data[str(frameNumber)]['dispersion_Y'])/float(max_d_y)
    else:
        n1_data[str(frameNumber)]['dispersion_Y']=None

    n1_data[str(frameNumber)]['dx']=f1_data[str(frameNumber)]['dx']
    n1_data[str(frameNumber)]['dy']=f1_data[str(frameNumber)]['dx']

file = open("/home/ubuntu/data/feature_n/no_team/features1.json", 'w')
json.dump(n1_data, file, indent=4)
file.close()

#n2_dataに特徴量挿入
n2_data={}
for i in range(int(len(f2_data))):
    frameNumber = i + 1
    n2_data[str(frameNumber)] = {}

for i in range(int(len(f2_data))):
    frameNumber = i + 1
    if f2_data[str(frameNumber)]['average_X']!=None:
        n2_data[str(frameNumber)]['average_X']=float(f2_data[str(frameNumber)]['average_X'])/float(max_a_x)
    else:
        n2_data[str(frameNumber)]['average_X']=None

    if f2_data[str(frameNumber)]['average_Y']!=None:
        n2_data[str(frameNumber)]['average_Y']=float(f2_data[str(frameNumber)]['average_Y'])/float(max_a_y)
    else:
        n2_data[str(frameNumber)]['average_Y']=None

    if f2_data[str(frameNumber)]['dispersion_X']!=None:
        n2_data[str(frameNumber)]['dispersion_X']=float(f2_data[str(frameNumber)]['dispersion_X'])/float(max_d_x)
    else:
        n2_data[str(frameNumber)]['dispersion_X']=None

    if f2_data[str(frameNumber)]['dispersion_Y']!=None:
        n2_data[str(frameNumber)]['dispersion_Y']=float(f2_data[str(frameNumber)]['dispersion_Y'])/float(max_d_y)
    else:
        n2_data[str(frameNumber)]['dispersion_Y']=None

    n2_data[str(frameNumber)]['dx']=f2_data[str(frameNumber)]['dx']
    n2_data[str(frameNumber)]['dy']=f2_data[str(frameNumber)]['dx']

file = open("/home/ubuntu/data/feature_n/no_team/features2.json", 'w')
json.dump(n2_data, file, indent=4)
file.close()

#n3_dataに特徴量挿入
n3_data={}
for i in range(int(len(f3_data))):
    frameNumber = i + 1
    n3_data[str(frameNumber)] = {}

for i in range(int(len(f3_data))):
    frameNumber = i + 1
    if f3_data[str(frameNumber)]['average_X']!=None:
        n3_data[str(frameNumber)]['average_X']=float(f3_data[str(frameNumber)]['average_X'])/float(max_a_x)
    else:
        n3_data[str(frameNumber)]['average_X']=None

    if f3_data[str(frameNumber)]['average_Y']!=None:
        n3_data[str(frameNumber)]['average_Y']=float(f3_data[str(frameNumber)]['average_Y'])/float(max_a_y)
    else:
        n3_data[str(frameNumber)]['average_Y']=None

    if f3_data[str(frameNumber)]['dispersion_X']!=None:
        n3_data[str(frameNumber)]['dispersion_X']=float(f3_data[str(frameNumber)]['dispersion_X'])/float(max_d_x)
    else:
        n3_data[str(frameNumber)]['dispersion_X']=None

    if f3_data[str(frameNumber)]['dispersion_Y']!=None:
        n3_data[str(frameNumber)]['dispersion_Y']=float(f3_data[str(frameNumber)]['dispersion_Y'])/float(max_d_y)
    else:
        n3_data[str(frameNumber)]['dispersion_Y']=None

    n3_data[str(frameNumber)]['dx']=f3_data[str(frameNumber)]['dx']
    n3_data[str(frameNumber)]['dy']=f3_data[str(frameNumber)]['dx']

file = open("/home/ubuntu/data/feature_n/no_team/features3.json", 'w')
json.dump(n3_data, file, indent=4)
file.close()

#n4_dataに特徴量挿入
n4_data={}
for i in range(int(len(f4_data))):
    frameNumber = i + 1
    n4_data[str(frameNumber)] = {}

for i in range(int(len(f4_data))):
    frameNumber = i + 1
    if f4_data[str(frameNumber)]['average_X']!=None:
        n4_data[str(frameNumber)]['average_X']=float(f4_data[str(frameNumber)]['average_X'])/float(max_a_x)
    else:
        n4_data[str(frameNumber)]['average_X']=None

    if f4_data[str(frameNumber)]['average_Y']!=None:
        n4_data[str(frameNumber)]['average_Y']=float(f4_data[str(frameNumber)]['average_Y'])/float(max_a_y)
    else:
        n4_data[str(frameNumber)]['average_Y']=None

    if f4_data[str(frameNumber)]['dispersion_X']!=None:
        n4_data[str(frameNumber)]['dispersion_X']=float(f4_data[str(frameNumber)]['dispersion_X'])/float(max_d_x)
    else:
        n4_data[str(frameNumber)]['dispersion_X']=None

    if f4_data[str(frameNumber)]['dispersion_Y']!=None:
        n4_data[str(frameNumber)]['dispersion_Y']=float(f4_data[str(frameNumber)]['dispersion_Y'])/float(max_d_y)
    else:
        n4_data[str(frameNumber)]['dispersion_Y']=None

    n4_data[str(frameNumber)]['dx']=f4_data[str(frameNumber)]['dx']
    n4_data[str(frameNumber)]['dy']=f4_data[str(frameNumber)]['dx']

file = open("/home/ubuntu/data/feature_n/no_team/features4.json", 'w')
json.dump(n4_data, file, indent=4)
file.close()

#n5_dataに特徴量挿入
n5_data={}
for i in range(int(len(f5_data))):
    frameNumber = i + 1
    n5_data[str(frameNumber)] = {}

for i in range(int(len(f5_data))):
    frameNumber = i + 1
    if f5_data[str(frameNumber)]['average_X']!=None:
        n5_data[str(frameNumber)]['average_X']=float(f5_data[str(frameNumber)]['average_X'])/float(max_a_x)
    else:
        n5_data[str(frameNumber)]['average_X']=None

    if f5_data[str(frameNumber)]['average_Y']!=None:
        n5_data[str(frameNumber)]['average_Y']=float(f5_data[str(frameNumber)]['average_Y'])/float(max_a_y)
    else:
        n5_data[str(frameNumber)]['average_Y']=None

    if f5_data[str(frameNumber)]['dispersion_X']!=None:
        n5_data[str(frameNumber)]['dispersion_X']=float(f5_data[str(frameNumber)]['dispersion_X'])/float(max_d_x)
    else:
        n5_data[str(frameNumber)]['dispersion_X']=None

    if f5_data[str(frameNumber)]['dispersion_Y']!=None:
        n5_data[str(frameNumber)]['dispersion_Y']=float(f5_data[str(frameNumber)]['dispersion_Y'])/float(max_d_y)
    else:
        n5_data[str(frameNumber)]['dispersion_Y']=None

    n5_data[str(frameNumber)]['dx']=f5_data[str(frameNumber)]['dx']
    n5_data[str(frameNumber)]['dy']=f5_data[str(frameNumber)]['dx']


file = open("/home/ubuntu/data/feature_n/no_team/features5.json", 'w')
json.dump(n5_data, file, indent=4)
file.close()

#n6_dataに特徴量挿入
n6_data={}
for i in range(int(len(f6_data))):
    frameNumber = i + 1
    n6_data[str(frameNumber)] = {}

for i in range(int(len(f6_data))):
    frameNumber = i + 1
    if f6_data[str(frameNumber)]['average_X']!=None:
        n6_data[str(frameNumber)]['average_X']=float(f6_data[str(frameNumber)]['average_X'])/float(max_a_x)
    else:
        n6_data[str(frameNumber)]['average_X']=None

    if f6_data[str(frameNumber)]['average_Y']!=None:
        n6_data[str(frameNumber)]['average_Y']=float(f6_data[str(frameNumber)]['average_Y'])/float(max_a_y)
    else:
        n6_data[str(frameNumber)]['average_Y']=None

    if f6_data[str(frameNumber)]['dispersion_X']!=None:
        n6_data[str(frameNumber)]['dispersion_X']=float(f6_data[str(frameNumber)]['dispersion_X'])/float(max_d_x)
    else:
        n6_data[str(frameNumber)]['dispersion_X']=None

    if f6_data[str(frameNumber)]['dispersion_Y']!=None:
        n6_data[str(frameNumber)]['dispersion_Y']=float(f6_data[str(frameNumber)]['dispersion_Y'])/float(max_d_y)
    else:
        n6_data[str(frameNumber)]['dispersion_Y']=None

    n6_data[str(frameNumber)]['dx']=f6_data[str(frameNumber)]['dx']
    n6_data[str(frameNumber)]['dy']=f6_data[str(frameNumber)]['dx']


file = open("/home/ubuntu/data/feature_n/no_team/features6.json", 'w')
json.dump(n6_data, file, indent=4)
file.close()
