from initialize import _default_path, clear
#from vocData import update

def list_all(data):
    clear()
    print('\n','{:<14}'.format('English'),'{:<10}'.format('Chinese'),'Synonym','\n')
    
    for i in range(len(data['eng'])):
        syn_data = ''
        for j in data['syn'][i]:
            syn_data += (j+', ')
        if len(data['syn'][i])==1 and data['syn'][i][0]=='':
            syn_data = 'X'
        else :
            syn_data = syn_data[:-2]
        
        print('{:<14}'.format(data['eng'][i]),\
              '{:<10}'.format(data['chn'][i]),\
              syn_data)
    print('\n\n')
    input('Press ENTER to continue')



def quiz(data):
    True


def add_word(data, path=_default_path):
   True 

