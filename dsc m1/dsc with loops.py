import os
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#fix font to 14 and make it so it's editable PDF
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size'] = 14

#%% detecting file
filename = 'dsc with loops.csv'
for f in os.listdir(r'C:/Users/konar/.spyder-py3'):
    if f == filename:
        print('the file exists')
        break
    else:
        print('file not found')

#%%

df = pd.read_csv(filename)

xi = df['index'].dropna()

ximin_hot, ximax_hot = 2140, 4547
ximin_cool, ximax_cool = 6031, 8440 

sample_number = int(input("enter number of samples: ")) #3
samples = np.arange(1,sample_number+1)

names = [str(x) for x in input('Enter list of numbers seperated by commas: ').split(',')]
        #['pcm','sp4','sp6']

lines = [
        (0, (1, 5)), #loosely dotted
        (0, (1, 2)),  #dotted
        (0, (1, 1)),  #densely dotted
            
        (0, (5, 10)), #loosely dashed
        (0, (5, 5)),  #dashed
        (0, (5, 1)),  #densely dashed

        (0, (3, 10, 1, 10)), #loosely dash-dotted
        (0, (3, 5, 1, 5)),   #dash-dotted
        (0, (3, 1, 1, 1)),   #densely dash-dotted

        (0, (3, 10, 1, 10, 1, 10)), #loosely dash-dot-dotted
        (0, (3, 5, 1, 5, 1, 5)),    #dash-dot-dotted 
        (0, (3, 1, 1, 1, 1, 1)),    #densely dash-dot-dotted
        
        (0,()) #solid
        ]

list_x = []
list_y = []

for sample in samples:
    
    x_sample = 'x'+str(sample)
    x_sample = df[x_sample].dropna()
    list_x.append(x_sample)
    
    y_sample = 'y'+str(sample)
    y_sample = df[y_sample].dropna()
    list_y.append(y_sample)

list_dict_x = []
list_dict_y = []

for sample in samples:
    
    x_dic = 'dict_'+str(sample)+'x'
    x_dic = dict(zip(xi,list_x[sample-1]))
    list_dict_x.append(x_dic)
    
    y_dic = 'dict_'+str(sample)+'y'
    y_dic = dict(zip(xi,list_y[sample-1]))
    list_dict_y.append(y_dic)

list_hot_x = []
list_cool_x = []

list_hot_y = []
list_cool_y = []

for sample in samples:
    
    x_hot = 'hot_x'+str(sample)
    x_hot = []
    list_hot_x.append(x_hot)
    
    x_cool = 'cool_x'+str(sample)
    x_cool = []
    list_cool_x.append(x_cool)
    
    for key,value in list_dict_x[sample-1].items():
        if ximin_hot < key < ximax_hot:
            list_hot_x[sample-1].append(value)
        elif ximin_cool < key < ximax_cool:
            list_cool_x[sample-1].append(value)
    
    y_hot = 'hot_y'+str(sample)
    y_hot = []
    list_hot_y.append(y_hot)
    
    y_cool = 'cool_y'+str(sample)
    y_cool = []
    list_cool_y.append(y_cool)
    
    for key,value in list_dict_y[sample-1].items():
        if ximin_hot < key < ximax_hot:
            list_hot_y[sample-1].append(value)
        elif ximin_cool < key < ximax_cool:
            list_cool_y[sample-1].append(value)
    
    names[sample-1], = plt.plot(list_hot_x[sample-1],list_hot_y[sample-1],
                                     label = names[sample-1],
                                     marker = 's', markersize = 0,
                                     c = 'black', linestyle = lines[sample-1])
    
    plt.plot(list_hot_x[sample-1],list_hot_y[sample-1],
             c = 'r', linestyle = lines[sample-1])
    
    plt.plot(list_cool_x[sample-1],list_cool_y[sample-1],
             c = 'b', linestyle = lines[sample-1])
                
#%%

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=False, left=False, right=False)
plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=False, left=False, right=False)
plt.tick_params(labelbottom=True, labeltop=False, labelleft=False, labelright=False)

#%%

red_patch = mpatches.Patch(color='red', label='heating')
blue_patch = mpatches.Patch(color='blue', label='cooling')
leg1 = plt.legend(handles =[red_patch, blue_patch], bbox_to_anchor =(1,0.75))
plt.gca().add_artist(leg1)

plt.legend(bbox_to_anchor =(1,0.5))

plt.xlabel('Temperature ($^o$C)')
plt.ylabel('Heat flow (J/g.s)')

plt.savefig('dsc with loops.png', dpi=300,bbox_inches="tight")





 
