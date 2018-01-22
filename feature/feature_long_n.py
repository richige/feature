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
with open("/home/ubuntu/data/feature/long/features1.json", 'r') as f:
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
with open("/home/ubuntu/data/feature/long/features2.json", 'r') as f:
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

    n1_data[str(frameNumber)]['l_dx']=f1_data[str(frameNumber)]['l_dx']
    n1_data[str(frameNumber)]['l_dy']=f1_data[str(frameNumber)]['l_dy']
    n1_data[str(frameNumber)]['r_dx']=f1_data[str(frameNumber)]['r_dx']
    n1_data[str(frameNumber)]['r_dy']=f1_data[str(frameNumber)]['r_dy']

    n1_data[str(frameNumber)]['ball_X']=f1_data[str(frameNumber)]['ball_X']
    n1_data[str(frameNumber)]['ball_Y']=f1_data[str(frameNumber)]['ball_Y']
    n1_data[str(frameNumber)]['crowd_X']=f1_data[str(frameNumber)]['crowd_X']
    n1_data[str(frameNumber)]['crowd_Y']=f1_data[str(frameNumber)]['crowd_Y']


file = open("/home/ubuntu/data/feature_n/long/features1.json", 'w')
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

    n2_data[str(frameNumber)]['l_dx']=f2_data[str(frameNumber)]['l_dx']
    n2_data[str(frameNumber)]['l_dy']=f2_data[str(frameNumber)]['l_dy']
    n2_data[str(frameNumber)]['r_dx']=f2_data[str(frameNumber)]['r_dx']
    n2_data[str(frameNumber)]['r_dy']=f2_data[str(frameNumber)]['r_dy']

    n2_data[str(frameNumber)]['ball_X']=f2_data[str(frameNumber)]['ball_X']
    n2_data[str(frameNumber)]['ball_Y']=f2_data[str(frameNumber)]['ball_Y']
    n2_data[str(frameNumber)]['crowd_X']=f2_data[str(frameNumber)]['crowd_X']
    n2_data[str(frameNumber)]['crowd_Y']=f2_data[str(frameNumber)]['crowd_Y']

file = open("/home/ubuntu/data/feature_n/long/features2.json", 'w')
json.dump(n2_data, file, indent=4)
file.close()
