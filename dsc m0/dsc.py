import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#fix font to 14 and make it so it's editable PDF
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size'] = 14

#%% detecting file
filename = 'dsc.csv'
for f in os.listdir(r'C:/Users/konar/.spyder-py3'):
    if f == filename:
        print('the file exists')
        break
    else:
        print('file not found')
        
#%% grab data
df = pd.read_csv(filename)

xi = df['index'].dropna()
ximin_hot, ximax_hot = 2140, 4547
ximin_cool, ximax_cool = 6031, 8440 


x1 = df['pcm_t'].dropna() 
y1 = df['pcm_h'].dropna()

x2 = df['SP4_t'].dropna()
y2 = df['SP4_h'].dropna()

x3 = df['SP6_t'].dropna()
y3 = df['SP6_h'].dropna()

#%% noob method

# plt.plot(x1,y1)
# plt.plot(x2,y2)
# plt.plot(x3,y3)
# plt.show()

#%% will work if thermal cycle is free of loops

# dict_1 = dict(zip(x1,y1))
# hot_x1 = []
# hot_y1 = []
# for key,value in dict_1.items():
#     if value <= -0.8:
#         hot_y1.append(value)
#         hot_x1.append(key)

# plt.plot(hot_x1, hot_y1, c='r')

# cool_x1 = []
# cool_y1 = []
# for key,value in dict_1.items():
#     if value >= 1:
#         cool_y1.append(value)
#         cool_x1.append(key)

# plt.plot(cool_x1, cool_y1, c='b')
# plt.show()

#%% pcm 

dict_1t = dict(zip(xi,x1))
dict_1h = dict(zip(xi,y1))

dict_2t = dict(zip(xi,x2))
dict_2h = dict(zip(xi,y2))

dict_3t = dict(zip(xi,x3))
dict_3h = dict(zip(xi,y3))

#%%

hot_x1 = []
cool_x1 = []
for key,value in dict_1t.items():
    if ximin_hot < key < ximax_hot:
        hot_x1.append(value)
    elif ximin_cool < key < ximax_cool:
        cool_x1.append(value)

hot_y1 = []
cool_y1 = []
for key,value in dict_1h.items():
    if ximin_hot < key < ximax_hot:
        hot_y1.append(value)
    elif ximin_cool < key < ximax_cool:
        cool_y1.append(value)

PCM, = plt.plot(hot_x1,hot_y1,label = 'PCM', marker = 's', markersize = 0, c = 'black', linestyle = ':')
plt.plot(hot_x1,hot_y1,c='r', linestyle = ':')
plt.plot(cool_x1,cool_y1,c='b', linestyle = ':')

# SP4
hot_x2 = []
cool_x2 = []
for key,value in dict_2t.items():
    if ximin_hot < key < ximax_hot:
        hot_x2.append(value)
    elif ximin_cool < key < ximax_cool:
        cool_x2.append(value)

hot_y2 = []
cool_y2 = []
for key,value in dict_2h.items():
    if ximin_hot < key < ximax_hot:
        hot_y2.append(value)
    elif ximin_cool < key < ximax_cool:
        cool_y2.append(value)

SP4, = plt.plot(hot_x2,hot_y2,label = 'SP4', marker = 's', markersize = 0, c = 'black', linestyle = '-.')
plt.plot(hot_x2,hot_y2,c='r', linestyle = '-.')
plt.plot(cool_x2,cool_y2,c='b', linestyle = '-.')

# SP6
hot_x3 = []
cool_x3 = []
for key,value in dict_3t.items():
    if ximin_hot < key < ximax_hot:
        hot_x3.append(value)
    elif ximin_cool < key < ximax_cool:
        cool_x3.append(value)

hot_y3 = []
cool_y3 = []
for key,value in dict_3h.items():
    if ximin_hot < key < ximax_hot:
        hot_y3.append(value)
    elif ximin_cool < key < ximax_cool:
        cool_y3.append(value)

SP6, = plt.plot(hot_x3,hot_y3,label = 'SP6', marker = 's', markersize = 0, c = 'black')
plt.plot(hot_x3,hot_y3,c='r')
plt.plot(cool_x3,cool_y3,c='b')

#%%

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=False, left=True, right=False)
plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=False, left=True, right=False)
plt.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False)

#first auto legend
red_patch = mpatches.Patch(color='red', label='heating')
blue_patch = mpatches.Patch(color='blue', label='cooling')
leg1 = plt.legend(handles =[red_patch, blue_patch], bbox_to_anchor =(1,0.75))
plt.gca().add_artist(leg1)

plt.legend((PCM,SP4,SP6),['PCM','SP4','SP6'], bbox_to_anchor =(1,0.5))

plt.xlabel('Temperature ($^o$C)')
plt.ylabel('Heat flow (J/g.s)')

plt.savefig('dsc.png', dpi=300,bbox_inches="tight")



