import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import os
import subprocess
import pandas as pd
import numpy as np

files = os.listdir("./x1")

for i in files:
    if i[-3:] == "jpg":
        os.remove("./x1/"+i)
        print("./x1/"+i + " Removed ... ")


import random

pos = [[0.,100.]]
xs0 = []
ys0 = []

xs1 = [1.0]
ys1 = [50.]

gtx = []
gty = []

gtx1 = []
gty1 = []


# print(pos)
x0 = 0.
y0 = 50.

x1 = 0.
y1 = 50.


signx = 1.0
signy = 1.0


width = 500
height = 100

ok = True
n = 0
speedIndex = 0
speeds = np.random.uniform(0.2, 2.0, 50).tolist()
speed = 0.5
speedsign = 1
while ok:
    n+=1
    if x1 > width:
        break
        signx = -1.0

    if y1 > height:
        signy = -1.0

    if x1 < 0:
        signx = 1.0

    if y1 < 0 :
        signy = 1.0

    if float(n) %50.0 == 0:
        speedIndex+=1



    x0  =  float(2*n) + random.normalvariate(0., 2.)
    y0 =  50+ random.normalvariate(0., 2.0)
    fig, ax = plt.subplots(2, 1, figsize=(5, 1.75))
    xs0.append(x0)
    ys0.append(y0)

    gtx.append(2.*n)
    gty.append(50.0)
    ax[0].cla()
    ax[0].set_xlim(0, 500)
    ax[0].set_ylim(25, 75)

    ax[0].plot(xs0, ys0, color="black", alpha=0.8, linewidth=1.0)
    ax[0].plot(gtx, gty, color="red", linewidth=1.0)
    # ax[0].text(0, 100, "  x : mu = 0, sigma: 2.0\n  y: mu=  0.0, sigma = 2.0")
    p0 = mpatches.Circle((x0,y0), radius=2, color="red")
    ax[0].add_patch(p0)



    x1  =  xs1[-1]+ speeds[speedIndex] + random.normalvariate(0., 2.)
    y1 =  50+ random.normalvariate(0., 2.0)
    xs1.append(x1)
    ys1.append(y1)

    gtx1.append(xs1[-1]+ speeds[speedIndex])
    gty1.append(50.0)
    ax[1].cla()
    ax[1].set_xlim(0, 500)
    ax[1].set_ylim(25, 75)

    ax[1].plot(xs1, ys1, color="black", alpha=0.8, linewidth=1.0)
    ax[1].plot(gtx1, gty1, color="red", linewidth=1.0)
    # ax[1].text(0, 100, "  x : mu = 0, sigma: 2.0\n  y: mu=  0.0, sigma = 2.0")
    p1 = mpatches.Circle((x1,y1), radius=2, color="red")
    ax[1].add_patch(p1)


    fig.savefig('./x1/'+"{:03d}".format(n)+".jpg")
n = []

files = os.listdir("./x1")
for i in files:
    if i[-3:] == "gif":
        try:
            n.append(int(i.split(".")[0][-3:]))
        except:
            print( " no n ... ")


p = subprocess.Popen(["convert", "-delay", "3", "-loop", "0", "./x1/*.jpg", "./x1/image"+"{:03d}".format(max(n)+1)+".gif"])
p.wait()


print(files)
for i in files:
    if i[-3:] == "jpg":
        os.remove("./x1/"+i)
        print("./x1/"+i + " Removed ... ")


d = {"x":xs1, "y":ys1}

df = pd.DataFrame(d)
df.to_csv("./x1/df.csv", index=False)
print(df)