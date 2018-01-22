# Utility package -- use pip install cvutils to install
#import cvutils
# OpenCV bindings
import numpy as np
import cv2
# To performing path manipulations
import csv
import matplotlib.pyplot as plt
import json
from progressbar import ProgressBar

#11:Red 12:Blue
#21:visible ball 22:unvisible ball_X
#31:Scrum 32:Lineout 33:Maul 34:Ruck
#P1:frame=77385, frame/set=1548, N=50
#P2:frame=80370, frame/set=1610, N=50
dt=31
movie=2
frame=80370

#選手位置読み込み
data = []
with open('/home/ubuntu/data/workspace/panasonic_estimate'+str(movie)+'/panasonic'+str(movie)+'_map_player_pos.csv', 'r') as f:
    for line in f:
        tmp = line.rstrip().split()
        data.append({
            'image': tmp[0],
            'value': int(tmp[2].replace("+AC0","")),
            'X': float(tmp[3]),
            'Y': float(tmp[4]),
            'ID':int(tmp[5]),
        })

#フレームごとの選手データ(区別なし)
player_data={}

for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1
    player_data[str(frameNumber)]={}
for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1
    player_data[str(frameNumber)]['X']=np.array([])
    player_data[str(frameNumber)]['Y']=np.array([])
    player_data[str(frameNumber)]['value']=np.array([])
    player_data[str(frameNumber)]['ID']=np.array([])

n=1
for d in data: #P1:N=0~48→1548 N=49→1532 #P2:1610
    if int(d['image'])==n and (int(d['value'])==11 or int(d['value'])==12):
        player_data[d['image']]['X']=np.append(player_data[d['image']]['X'],d['X'])
        player_data[d['image']]['Y']=np.append(player_data[d['image']]['Y'],d['Y'])
        player_data[d['image']]['value']=np.append(player_data[d['image']]['value'],d['value'])
        player_data[d['image']]['ID']=np.append(player_data[d['image']]['ID'],d['ID'])
    else :
        n=int(d['image'])

#選手平均位置
average_X={}
average_Y={}

for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1

    if float(len(player_data[str(frameNumber)]['X']))!=0.0:
        average_X[str(frameNumber)]=float(np.sum(player_data[str(frameNumber)]['X']))/float(len(player_data[str(frameNumber)]['X']))
    if float(len(player_data[str(frameNumber)]['Y']))!=0.0:
        average_Y[str(frameNumber)]=float(np.sum(player_data[str(frameNumber)]['Y']))/float(len(player_data[str(frameNumber)]['Y']))
    if float(len(player_data[str(frameNumber)]['X']))==0.0:
        average_X[str(frameNumber)]=None
    if float(len(player_data[str(frameNumber)]['Y']))==0.0:
        average_Y[str(frameNumber)]=None

#選手分散
dispersion_X={}
dispersion_Y={}
for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1

    if float(len(player_data[str(frameNumber)]['X']))!=0.0:
        dispersion_X[str(frameNumber)]=float(np.var(player_data[str(frameNumber)]['X']))
    if float(len(player_data[str(frameNumber)]['Y']))!=0.0:
        dispersion_Y[str(frameNumber)]=float(np.var(player_data[str(frameNumber)]['Y']))
    if float(len(player_data[str(frameNumber)]['X']))==0.0:
        dispersion_X[str(frameNumber)]=None
    if float(len(player_data[str(frameNumber)]['Y']))==0.0:
        dispersion_Y[str(frameNumber)]=None


#フレームごとの選手データ(区別あり)
br_data={}

for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1
    br_data[str(frameNumber)]={}
for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1
    br_data[str(frameNumber)]['bX']=np.array([])
    br_data[str(frameNumber)]['bY']=np.array([])
    br_data[str(frameNumber)]['rX']=np.array([])
    br_data[str(frameNumber)]['rY']=np.array([])
    br_data[str(frameNumber)]['bID']=np.array([])
    br_data[str(frameNumber)]['rID']=np.array([])

n=1
for d in data: #P1:N=0~48→1548 N=49→1532 #P2:1610
    if int(d['image'])==n:
        if int(d['value'])==11:
            br_data[d['image']]['rX']=np.append(br_data[d['image']]['rX'],d['X'])
            br_data[d['image']]['rY']=np.append(br_data[d['image']]['rY'],d['Y'])
            br_data[d['image']]['rID']=np.append(br_data[d['image']]['rID'],d['ID'])
        if int(d['value'])==12:
            br_data[d['image']]['bX']=np.append(br_data[d['image']]['bX'],d['X'])
            br_data[d['image']]['bY']=np.append(br_data[d['image']]['bY'],d['Y'])
            br_data[d['image']]['bID']=np.append(br_data[d['image']]['bID'],d['ID'])
    else :
        n=int(d['image'])

#選手平均速度
#チーム区別あり（右下方向正）
b_dx={}
b_s_dx={}
b_dy={}
b_s_dy={}
r_dx={}
r_s_dx={}
r_dy={}
r_s_dy={}

#チーム区別なし（絶対値)
abs_b_s_dx={}
abs_r_s_dx={}
dx={}
abs_b_s_dy={}
abs_r_s_dy={}
dy={}

#青・赤チーム人数カウント
b_c={}
r_c={}

pbar = ProgressBar(frame)
for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1
    rdx=0.0
    rdy=0.0
    abs_rdx=0.0
    abs_rdy=0.0
    rc=0

    if frameNumber>=1+int(dt/2) and frameNumber<frame-int(dt/2):
        r_a=len(br_data[str(frameNumber+int(dt/2))]['rID'])
        r_b=len(br_data[str(frameNumber-int(dt/2))]['rID'])

        if r_a==0:
            rdx=0.0
            rdy=0.0
            abs_rdx=0.0
            abs_rdy=0.0
            rc=0
        elif r_b==0:
            rdx=0.0
            rdy=0.0
            abs_rdx=0.0
            abs_rdy=0.0
            rc=0

        elif (r_b<=r_a):
            for j in range(r_a):
                for k in range(r_b):
                    if (br_data[str(frameNumber-int(dt/2))]['rID'][k]==br_data[str(frameNumber+int(dt/2))]['rID'][k]):
                        rc+=1
                        rdx+=float(br_data[str(frameNumber+int(dt/2))]['rX'][k]-br_data[str(frameNumber-int(dt/2))]['rX'][k])
                        rdy+=float(br_data[str(frameNumber+int(dt/2))]['rX'][k]-br_data[str(frameNumber-int(dt/2))]['rX'][k])
                        abs_rdx+=abs(float(br_data[str(frameNumber+int(dt/2))]['rX'][k]-br_data[str(frameNumber-int(dt/2))]['rX'][k]))
                        abs_rdy+=abs(float(br_data[str(frameNumber+int(dt/2))]['rX'][k]-br_data[str(frameNumber-int(dt/2))]['rX'][k]))
        elif (r_b>r_a):
            for k in range(r_b):
                for j in range(r_a):
                    if (br_data[str(frameNumber-int(dt/2))]['rID'][j]==br_data[str(frameNumber+int(dt/2))]['rID'][j]):
                        rc+=1
                        rdx+=float(br_data[str(frameNumber+int(dt/2))]['rX'][j]-br_data[str(frameNumber-int(dt/2))]['rX'][j])
                        rdy+=float(br_data[str(frameNumber+int(dt/2))]['rX'][j]-br_data[str(frameNumber-int(dt/2))]['rX'][j])
                        abs_rdx+=abs(float(br_data[str(frameNumber+int(dt/2))]['rX'][j]-br_data[str(frameNumber-int(dt/2))]['rX'][j]))
                        abs_rdy+=abs(float(br_data[str(frameNumber+int(dt/2))]['rX'][j]-br_data[str(frameNumber-int(dt/2))]['rX'][j]))
    r_c[str(frameNumber)]=rc
    r_s_dx[str(frameNumber)]=rdx
    r_s_dy[str(frameNumber)]=rdy
    abs_r_s_dx[str(frameNumber)]=abs_rdx
    abs_r_s_dy[str(frameNumber)]=abs_rdy
    pbar.update(i + 1)

for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1
    bdx=0.0
    bdy=0.0
    abs_bdx=0.0
    abs_bdy=0.0
    bc=0.0

    if frameNumber>=1+int(dt/2) and frameNumber<frame-int(dt/2):
        b_a=len(br_data[str(frameNumber+int(dt/2))]['bID'])
        b_b=len(br_data[str(frameNumber-int(dt/2))]['bID'])

        if b_a==0:
            bdx=0.0
            bdy=0.0
            abs_bdx=0.0
            abs_bdy=0.0
            bc=0
        elif b_b==0:
            bdx=0.0
            bdy=0.0
            abs_bdx=0.0
            abs_bdy=0.0
            bc=0

        elif (b_b<=b_a):
            for j in range(b_a):
                for k in range(b_b):
                    if (br_data[str(frameNumber-int(dt/2))]['bID'][k]==br_data[str(frameNumber+int(dt/2))]['bID'][k]):
                        bc+=1
                        bdx+=float(br_data[str(frameNumber+int(dt/2))]['bX'][k]-br_data[str(frameNumber-int(dt/2))]['bX'][k])
                        bdy+=float(br_data[str(frameNumber+int(dt/2))]['bX'][k]-br_data[str(frameNumber-int(dt/2))]['bX'][k])
                        abs_bdx+=abs(float(br_data[str(frameNumber+int(dt/2))]['bX'][k]-br_data[str(frameNumber-int(dt/2))]['bX'][k]))
                        abs_bdy+=abs(float(br_data[str(frameNumber+int(dt/2))]['bX'][k]-br_data[str(frameNumber-int(dt/2))]['bX'][k]))
        elif (b_b>b_a):
            for k in range(b_b):
                for j in range(b_a):
                    if (br_data[str(frameNumber-int(dt/2))]['bID'][j]==br_data[str(frameNumber+int(dt/2))]['bID'][j]):
                        bc+=1
                        bdx+=float(br_data[str(frameNumber+int(dt/2))]['bX'][j]-br_data[str(frameNumber-int(dt/2))]['bX'][j])
                        bdy+=float(br_data[str(frameNumber+int(dt/2))]['bX'][j]-br_data[str(frameNumber-int(dt/2))]['bX'][j])
                        abs_bdx+=abs(float(br_data[str(frameNumber+int(dt/2))]['bX'][j]-br_data[str(frameNumber-int(dt/2))]['bX'][j]))
                        abs_bdy+=abs(float(br_data[str(frameNumber+int(dt/2))]['bX'][j]-br_data[str(frameNumber-int(dt/2))]['bX'][j]))
    b_c[str(frameNumber)]=bc
    b_s_dx[str(frameNumber)]=bdx
    b_s_dy[str(frameNumber)]=bdy
    abs_b_s_dx[str(frameNumber)]=abs_bdx
    abs_b_s_dy[str(frameNumber)]=abs_bdy

for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
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

ball_X={}
ball_Y={}

#ボール位置読み込み
ball_data={}
for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1
    ball_data[str(frameNumber)]={}

for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1
    ball_data[str(frameNumber)]['image']=0
    ball_data[str(frameNumber)]['value']=0
    ball_data[str(frameNumber)]['X']=0.0
    ball_data[str(frameNumber)]['Y']=0.0


with open('/home/ubuntu/data/workspace/panasonic_estimate'+str(movie)+'/panasonic'+str(movie)+'_map_ball_pos.csv', 'r') as f:
    for line in f:
        tmp = line.rstrip().split()
        ball_data[str(tmp[0])]['image']=int(tmp[0])
        ball_data[str(tmp[0])]['value']=int(tmp[2].replace("+AC0",""))
        ball_data[str(tmp[0])]['X']=float(tmp[3])
        ball_data[str(tmp[0])]['Y']=float(tmp[4])

for i in range(frame):
    frameNumber = i + 1
    if int(ball_data[str(frameNumber)]['value'])==21 or int(ball_data[str(frameNumber)]['value'])==22:
        bx=float(ball_data[str(frameNumber)]['X'])
        by=float(ball_data[str(frameNumber)]['Y'])

    else:
        bx=None
        by=None

    ball_X[str(frameNumber)]=bx
    ball_Y[str(frameNumber)]=by


crowd_X={}
crowd_Y={}

#密集位置読み込み
crowd_data={}
for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1
    crowd_data[str(frameNumber)]={}

for i in range(frame): #P1:N=0~48→1548 N=49→1532 #P2:1610
    frameNumber = i + 1
    crowd_data[str(frameNumber)]['image']=0
    crowd_data[str(frameNumber)]['value']=0
    crowd_data[str(frameNumber)]['X']=0.0
    crowd_data[str(frameNumber)]['Y']=0.0

with open('/home/ubuntu/data/workspace/panasonic_estimate'+str(movie)+'/panasonic'+str(movie)+'_map_crowd_pos.csv', 'r') as f:
    for line in f:
        tmp = line.rstrip().split()
        crowd_data[str(tmp[0])]['image']=int(tmp[0])
        crowd_data[str(tmp[0])]['value']=int(tmp[2].replace("+AC0",""))
        crowd_data[str(tmp[0])]['X']=float(tmp[3])
        crowd_data[str(tmp[0])]['Y']=float(tmp[4])

for i in range(frame):
    frameNumber = i + 1
    if int(crowd_data[str(frameNumber)]['value'])==31 or int(crowd_data[str(frameNumber)]['value'])==32 or int(crowd_data[str(frameNumber)]['value'])==33 or int(crowd_data[str(frameNumber)]['value'])==34:
        c_x=float(crowd_data[str(frameNumber)]['X'])
        c_y=float(crowd_data[str(frameNumber)]['Y'])

    else:
        c_x=None
        c_y=None

    crowd_X[str(frameNumber)]=c_x
    crowd_Y[str(frameNumber)]=c_y


#field_dataに特徴量挿入
field_data={}
for i in range(frame):
    frameNumber = i + 1
    field_data[str(frameNumber)]={}

for i in range(frame):
    frameNumber = i + 1

    field_data[str(frameNumber)]['average_X']=average_X[str(frameNumber)]
    field_data[str(frameNumber)]['average_Y']=average_Y[str(frameNumber)]
    field_data[str(frameNumber)]['dispersion_X']=dispersion_X[str(frameNumber)]
    field_data[str(frameNumber)]['dispersion_Y']=dispersion_Y[str(frameNumber)]
    #field_data[str(frameNumber)]['l_dx']=b_dx[str(frameNumber)]
    #field_data[str(frameNumber)]['l_dy']=b_dy[str(frameNumber)]
    #field_data[str(frameNumber)]['r_dx']=r_dx[str(frameNumber)]
    #field_data[str(frameNumber)]['r_dy']=r_dy[str(frameNumber)]
    field_data[str(frameNumber)]['dx']=dx[str(frameNumber)]
    field_data[str(frameNumber)]['dy']=dy[str(frameNumber)]
    #field_data[str(frameNumber)]['ball_X']=ball_X[str(frameNumber)]
    #field_data[str(frameNumber)]['ball_Y']=ball_Y[str(frameNumber)]
    #field_data[str(frameNumber)]['crowd_X']=crowd_X[str(frameNumber)]
    #field_data[str(frameNumber)]['crowd_Y']=crowd_Y[str(frameNumber)]

#file = open("/home/ubuntu/data/ichige_long/data/features"+str(movie)+".json", 'w')
#file = open("/home/ubuntu/data/ichige_team/data/features"+str(movie+4)+".json", 'w')
file = open("/home/ubuntu/data/ichige_no_team/data/features"+str(movie+4)+".json", 'w')

json.dump(field_data, file)
file.close()
print(len(field_data))
print(field_data['57'])
