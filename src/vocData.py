import os

_default_path = './../data/'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_file(file_name):
    try:
        f = open(file_name, 'r')
        content = f.readlines()
        f.close()

    except FileNotFoundError:
        g = open(file_name, 'w')
        content = []
        g.close()
    return content


def initialize():
    data = {}
    for i in ['eng', 'chn', 'syn', 'rec', 'index_type', 'type']:
        data[i] = check_file('./../data/%s.txt' % i)

    data['eng'] = [i.strip() for i in data['eng']]
    data['chn'] = [i.strip() for i in data['chn']]
    data['syn'] = [[j.strip() for j in i.split(',')] for i in data['syn']]
    data['rec'] = [[int(j.strip()) for j in i.split(',')] for i in data['rec']]
    data['index_type'] = [i.strip().split() for i in data["index_type"]]
    if data['index_type'] == []:
        data['index_type'].append(["0", 'notclassified'])
    data['type'] = [i.strip() for i in data['type']]
    return data


def update(data, path=_default_path):
    eng, chn, syn, rec, _type, index_type = '', '', '', '', '', ''
    for i in data['eng']:
        eng += (str(i) + '\n')
    for i in data['chn']:
        chn += (str(i) + '\n')
    for i in data['syn']:
        for j in i:
            syn += (str(j) + ',')
        syn = syn[:-1]
        syn += '\n'
    for i in data['rec']:
        rec += (str(i[0]) + ',' + str(i[1]) + '\n')
    for i in data['type']:
        _type += (str(i) + '\n')
    for i in data['index_type']:
        index_type += (str(i[0]) + ' ' + str(i[1]) + '\n')

    s_write = {'eng': eng, 'chn': chn, 'syn': syn, 'rec': rec, 'type': _type, 'index_type': index_type}

    for i in ['eng', 'chn', 'syn', 'rec', 'type', 'index_type']:
        f = open(path + '{}.txt'.format(i), 'w')
        f.write(s_write[i])
        f.close()

