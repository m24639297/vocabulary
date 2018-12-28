
####### THIS FILE IS NOT IN USED !!!!!!!!! #########

#from basic import word
import os

_default_path = './../data/'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_file(file_name):
    try:
        f = open(file_name,'r')
        content = f.readlines()
        f.close()

    except FileNotFoundError:
        g = open(file_name,'w')
        content = []
        g.close()
    return content

def initialize():
    data = {}
    for i in ['eng', 'chn', 'syn', 'rec']:   
        data[i] = check_file('./../data/%s.txt' % i)

    data['eng'] = [i.strip() for i in data['eng']] 
    data['chn'] = [i.strip() for i in data['chn']] 
    data['syn'] = [[j.strip() for j in i.split(',')] for i in data['syn']]
    data['rec'] = [[int(j.strip()) for j in i.split(',')] for i in data['rec']]
    print('hi')
    for i in range(len(data['syn'])):
        print(data['syn'][i])
        if data['syn'][i][0]=='': data['syn'][i]==[]

    return data
