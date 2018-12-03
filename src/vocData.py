from initialize import _default_path

def update(data, path = _default_path):
    eng,chn,syn,rec = '','','',''
    for i in data['eng']:
        eng += (str(i)+'\n')
    for i in data['chn']:
        chn += (str(i)+'\n')
    for i in data['syn']:
        for j in i:
            syn += (str(j)+',')
        syn = syn[:-1]
        syn += '\n'
    for i in data['rec']:
        rec += (str(i[0])+','+str(i[1])+'\n')

    
    s_write = {'eng':eng, 'chn':chn, 'syn':syn, 'rec':rec}

    for i in ['eng','chn','syn','rec']:
        f=  open(path+'{}.txt'.format(i),'w')
        f.write(s_write[i])
        f.close()

