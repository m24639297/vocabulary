from initialize import _default_path, clear
from vocData import update
from random import sample

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
    N = len(data['eng'])
    while(True):
        clear()
        m = input('\nSelect quiz mode  (multiple choices(m), synonyms(sym), spelling(s), exit(e)): \n ')
        if m in ['m','s','e','sym']: break
    if m == 'e': return 
    if m == 's':
        clear()
        while(True):
            try: num = int(input('\nNumber of words: '))
            except ValueError: 
                print('Invalid number')
                continue
            if not num > 0: print('Invalid number')
            else: break
        if num > N:
            print('Number is too large, all words will be used once')
            input('Press ENTER to continue')
            num = N
        
        question = set(sample(range(0,N),num))
        correct = set()
        while(len(correct)<num):
            clear()
            index = question.pop()
            reply = input('\n'+data['chn'][index]+': ')
            data['rec'][index][0] += 1
            if reply == data['eng'][index]:
                correct.add(index)
                data['rec'][index][1] += 1
            else: 
                question.add(index)
                input('\nCorrect answer: '+data['eng'][index]\
                +'\n\n\nPress ENTER to continue')
        clear()
        print('\n Summary: \n')
        for i in correct:
            print('  '+data['eng'][i]+': '+data['chn'][i]) 
        input('\n\nPress ENTER to continue')
    
    if m == 'm':
        clear()
        while(True):
            try: num = int(input('\nNumber of words: '))
            except ValueError: 
                print('Invalid number')
                continue
            if not num > 0: print('Invalid number')
            else: break
        if num > N:
            print('Number is too large, all words will be used once')
            input('Press ENTER to continue')
            num = N
        
        question = set(sample(range(0,N),num))
        correct = set()
        while(len(correct)<num):
            print('To be added')
            break





def add_word(data, path=_default_path):
    clear()
    while True:
        x = None
        tmp_eng = input('\nEnglish (Press ENTER to finish): ').strip()
        if tmp_eng == '': break
        if tmp_eng in data['eng']:
            while True:
                x = input('Word has existed, replace(r) or ignore(i): ').strip()
                if x == 'r' or x == 'i': break
                else: print('Invalid input\n')
        tmp_chn = input('Chinese: ').strip()
        tmp_syn = input('Synonyms (Separate by comma): ').strip()
        
        if x == None or x == 'i':
            data['eng'].append(tmp_eng)
            data['chn'].append(tmp_chn)
            data['syn'].append([ii.strip() for ii in tmp_syn.split(',')])
            data['rec'].append([0,0])
        else :
            index = data['eng'].index(tmp_eng)
            data['chn'][index] = tmp_chn
            data['syn'][index] = [ii.strip() for ii in tmp_syn.split(',')]
            data['rec'][index] = [0,0]
    
    update(data)



