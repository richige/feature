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

dt=31
N=4

#選手位置読み込み
data = []
with open('/home/ubuntu/data/workspace/annotate/result/NTTcom'+str(N)+'/2field.csv', 'r') as f:
    for line in f:
        tmp = line.split(',')
        data.append({
            'image': tmp[0],
            'value': tmp[1],
            'ID':tmp[2],
            'X': tmp[3],
            'Y': tmp[4],
        })


#separate_dataに選手位置挿入
separate_data={}

for d in data:
    separate_data[str(int(d['image'][4:8]))]=[]

for d in data:
    if (int(d['value'])!=0):
       separate_data[str(int(d['image'][4:8]))].append({
                                'image': str(int(d['image'][4:8])),
                                'value': d['value'],
                                'ID': d['ID'],
                                'X': d['X'],
                                'Y': d['Y'],
                                'count':0.0,
                                'average_X':0.0,
                                'average_Y':0.0,
                                'dispersion_X':0.0,
                                'dispersion_Y':0.0,
                                'b_dx':0.0,
                                'b_dy':0.0,
                                'r_dx':0.0,
                                'r_dy':0.0,
                                'dx':0.0,
                                'dy':0.0,

       })

#選手の数、選手位置、ボール位置、密集位置をカウント
count = {}
player_sum_x={}
player_sum_y={}
average_X={}
average_Y={}

for i in range(int(len(separate_data))):
    frameNumber = i + 1
    count_data = separate_data[str(frameNumber)]
    c=0.0
    sum_x=0.0
    sum_y=0.0
    for cd in count_data :
        if int(cd['value'])==11 or int(cd['value'])==12:
           sum_x+=float(cd['X'])
           sum_y+=float(cd['Y'])
           c+=1.0
        count[str(frameNumber)]=c
        player_sum_x[str(frameNumber)]=sum_x
        player_sum_y[str(frameNumber)]=sum_y

#separate_dataに選手数、平均位置挿入
for i in range(int(len(separate_data))):
    frameNumber = i + 1
    count_data = separate_data[str(frameNumber)]
    for cd in count_data :
        cd['count']=count[str(frameNumber)]
        cd['average_X']=float(player_sum_x[str(frameNumber)])/float(count[str(frameNumber)])
        average_X[str(frameNumber)]=cd['average_X']
        cd['average_Y']=float(player_sum_y[str(frameNumber)])/float(count[str(frameNumber)])
        average_Y[str(frameNumber)]=cd['average_Y']


#分散の算出
sum_dx={}
sum_dy={}
dispersion_X={}
dispersion_Y={}

for i in range(int(len(separate_data))):
    frameNumber = i + 1
    count_data = separate_data[str(frameNumber)]
    sum_xi_xi=0.0
    sum_yi_yi=0.0

    for cd in count_data :
        if int(cd['value'])==11 or int(cd['value'])==12:
           xi_x=float(cd['X'])-float(cd['average_X'])
           yi_y=float(cd['Y'])-float(cd['average_Y'])
           sum_xi_xi+=xi_x*xi_x
           sum_yi_yi+=yi_y*yi_y
        sum_dx[str(frameNumber)]=sum_xi_xi
        sum_dy[str(frameNumber)]=sum_yi_yi

#separate_dataに分散挿入
for i in range(int(len(separate_data))):
    frameNumber = i + 1
    count_data = separate_data[str(frameNumber)]
    for cd in count_data :
        cd['dispersion_X']=float(sum_dx[str(frameNumber)])/float(count[str(frameNumber)])
        dispersion_X[str(frameNumber)]=cd['dispersion_X']
        cd['dispersion_Y']=float(sum_dy[str(frameNumber)])/float(count[str(frameNumber)])
        dispersion_Y[str(frameNumber)]=cd['dispersion_Y']

#速度平均
#区別あり
b_dx={}
b_s_dx={}
b_dy={}
b_s_dy={}
r_dx={}
r_s_dx={}
r_dy={}
r_s_dy={}
#区別なし
abs_b_s_dx={}
abs_r_s_dx={}
dx={}
abs_b_s_dy={}
abs_r_s_dy={}
dy={}

#青・赤チーム人数カウント
b_c={}
r_c={}


for i in range(int(len(separate_data))):
    frameNumber = i + 1
    rdx=0.0
    rdy=0.0
    abs_rdx=0.0
    abs_rdy=0.0
    rc=0
    bdx=0.0
    bdy=0.0
    abs_bdx=0.0
    abs_bdy=0.0
    bc=0.0
    if frameNumber>=1+int(dt/2) and frameNumber<int(len(separate_data))-int(dt/2):
        before_data = separate_data[str(frameNumber-int(dt/2))]
        after_data = separate_data[str(frameNumber+int(dt/2))]
        for a_d in after_data:
            for b_d in before_data:
                if b_d['ID']==a_d['ID']:
                    if int(a_d['value'])==11:
                        rc+=1
                        rdx+=float(a_d['X'])-float(b_d['X'])
                        rdy+=float(a_d['Y'])-float(b_d['Y'])
                        abs_rdx+=abs(float(a_d['X'])-float(b_d['X']))
                        abs_rdy+=abs(float(a_d['Y'])-float(b_d['Y']))

                    if int(a_d['value'])==12:
                        bc+=1
                        bdx+=float(a_d['X'])-float(b_d['X'])
                        bdy+=float(a_d['Y'])-float(b_d['Y'])
                        abs_bdx+=abs(float(a_d['X'])-float(b_d['X']))
                        abs_bdy+=abs(float(a_d['Y'])-float(b_d['Y']))
    r_c[str(frameNumber)]=rc
    r_s_dx[str(frameNumber)]=rdx
    r_s_dy[str(frameNumber)]=rdy
    abs_r_s_dx[str(frameNumber)]=abs_rdx
    abs_r_s_dy[str(frameNumber)]=abs_rdy
    b_c[str(frameNumber)]=bc
    b_s_dx[str(frameNumber)]=bdx
    b_s_dy[str(frameNumber)]=bdy
    abs_b_s_dx[str(frameNumber)]=abs_bdx
    abs_b_s_dy[str(frameNumber)]=abs_bdy


for i in range(int(len(separate_data))):
    frameNumber = i + 1
    if float(r_c[str(frameNumber)])!=0.0:
        r_dx[str(frameNumber)]=float(r_s_dx[str(frameNumber)])/(float(r_c[str(frameNumber)])*float(dt))
        r_dy[str(frameNumber)]=float(r_s_dy[str(frameNumber)])/(float(r_c[str(frameNumber)])*float(dt))
    if float(b_c[str(frameNumber)])!=0.0:
        b_dx[str(frameNumber)]=float(b_s_dx[str(frameNumber)])/(float(b_c[str(frameNumber)])*float(dt))
        b_dy[str(frameNumber)]=float(b_s_dy[str(frameNumber)])/(float(b_c[str(frameNumber)])*float(dt))
    if float(r_c[str(frameNumber)])==0.0:
        r_dx[str(frameNumber)]=None
        r_dy[str(frameNumber)]=None
    if float(b_c[str(frameNumber)])==0.0:
        b_dx[str(frameNumber)]=None
        b_dy[str(frameNumber)]=None
    if float(r_c[str(frameNumber)]+b_c[str(frameNumber)])!=0.0:
        dx[str(frameNumber)]=float(abs_r_s_dx[str(frameNumber)]+abs_b_s_dx[str(frameNumber)])/(float(r_c[str(frameNumber)]+b_c[str(frameNumber)])*float(dt))
        dy[str(frameNumber)]=float(abs_r_s_dy[str(frameNumber)]+abs_b_s_dy[str(frameNumber)])/(float(r_c[str(frameNumber)]+b_c[str(frameNumber)])*float(dt))
    if float(r_c[str(frameNumber)]+b_c[str(frameNumber)])==0.0:
        dx[str(frameNumber)]=None
        dy[str(frameNumber)]=None


#field_dataに特徴量挿入
field_data={}
for i in range(int(len(separate_data))):
    frameNumber = i + 1
    count_data = separate_data[str(frameNumber)]
    for cd in count_data :
        field_data[cd['image']]={}

for i in range(int(len(separate_data))):
    frameNumber = i + 1
    count_data = separate_data[str(frameNumber)]
    for cd in count_data :
        #field_data[cd['image']]['count']=count[str(frameNumber)]
        field_data[cd['image']]['average_X']=average_X[str(frameNumber)]
        field_data[cd['image']]['average_Y']=average_Y[str(frameNumber)]
        field_data[cd['image']]['dispersion_X']=dispersion_X[str(frameNumber)]
        field_data[cd['image']]['dispersion_Y']=dispersion_Y[str(frameNumber)]
        #field_data[str(frameNumber)]['l_dx']=r_dx[str(frameNumber)]
        #field_data[str(frameNumber)]['l_dy']=r_dy[str(frameNumber)]
        #field_data[str(frameNumber)]['r_dx']=b_dx[str(frameNumber)]
        #field_data[str(frameNumber)]['r_dy']=b_dy[str(frameNumber)]
        field_data[str(frameNumber)]['dx']=dx[str(frameNumber)]
        field_data[str(frameNumber)]['dy']=dy[str(frameNumber)]



#file = open("/home/ubuntu/data/ichige_team/data/features"+str(N)+".json", 'w')
file = open("/home/ubuntu/data/ichige_no_team/data/features"+str(N)+".json", 'w')

json.dump(field_data, file)
file.close()
print(len(field_data))
print(field_data['57'])
