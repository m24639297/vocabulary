from initialize import _default_path, clear, initialize
from vocData import update
from random import sample, randrange, shuffle

def list_all(data):
    clear()
    N = len(data['eng'])
    print('\n','{:<14}'.format('English'),'{:<15}'.format('Chinese'),'Synonym','\n',sep='')
    
    for i in sorted(range(N), key = lambda i: data['eng'][i]):
        syn_data = ''
        for j in data['syn'][i]:
            syn_data += (j+', ')
        if len(data['syn'][i])==1 and data['syn'][i][0]=='':
            syn_data = 'X'
        else :
            syn_data = syn_data[:-2]
        
        print('{:<14}'.format(data['eng'][i]),\
              data['chn'][i],' '*(15-2*(len(data['chn'][i]))),\
              syn_data,sep='')
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
        
        for i in sorted(correct,key=lambda i: data['eng'][i]):
            print('  {:<15}: '.format(data['eng'][i])+data['chn'][i]) 
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
        
        while(len(correct) < num):
            clear()
            index = question.pop()
            data['rec'][index][0] += 1
            print('\n'+data['chn'][index]+':\n\n')
            choice = set([data['eng'][index]])
            
            while(len(choice)<5):
                tmp = randrange(0,N)
                if tmp == index: continue
                choice.add(data['eng'][tmp])
            alp = ord('A')
            ans = ''
            while(len(choice)>0):
                cc = choice.pop()
                print('  ({}) {}\n'.format(chr(alp),cc))
                if cc == data['eng'][index]: ans = alp
                alp += 1
            reply = input('\n Answer: ').upper()

            if reply == chr(ans):
                correct.add(index)
                data['rec'][index][1] += 1
            else:
                print('\nCorrect answer: {}\n'.format(chr(ans)))
                input('Press ENTER to continue')
                question.add(index)
        clear()
        print('\n Summary: \n')
        for i in sorted(correct,key=lambda i: data['eng'][i]):
            print('  {:<15}: '.format(data['eng'][i])+data['chn'][i]) 
        input('\n\nPress ENTER to continue')
    update(data)
    return initialize()

def add_word(data, path=_default_path):
    clear()
    while True:
        x = None
        tmp_eng = input('\nEnglish (Press ENTER to finish): ').strip()
        if tmp_eng == '': break
        if tmp_eng in data['eng']:
            while True:
                x = input('Word has existed, replace(r), add(a), or skip(s): ').strip()
                if x in ['r','a','s']: break
                else: clear; print('Invalid input\n')
        if x == 's':
            print('\n--Skipped--\n')
            continue
        tmp_chn = input('Chinese: ').strip()
        tmp_syn = input('Synonyms (Separate by comma): ').strip()
        
        if x == None or x == 'a':
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
    return initialize()

def history(data):
    N = len(data['eng'])
    clear()
    print('\n(Word: (correct, wrong))\n')
    for i in sorted(range(N), key = lambda i: data['eng'][i]):
        print('{:<14}: ({}, {})'.format(data['eng'][i],data['rec'][i][1],data['rec'][i][0]-data['rec'][i][1]))
    input('\nPress ENTER to continue')

