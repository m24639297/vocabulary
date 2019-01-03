from vocData import update, _default_path, clear, initialize
from random import sample, randrange, shuffle
from queue import Queue
from itertools import zip_longest

def continue_msg():
    input('Press ENTER to continue...')

def safe_input(question, choice, exception='', _clear = True):
    while True:
        if _clear: clear()
        x = input(question).strip()
        if x in choice:
            return x
        if exception != '':
            print(exception)
            continue_msg()

def get_hint(_words, _target):
    # print('Input: {}, {}'.format(_words,_target))
    words = _words.copy()
    target = _target
    prefix = ''
    try:
        if target not in words: raise ValueError('target({}) should be in words({})'.format(target,words))
    except TypeError:
        raise TypeError('words is not iterable!')

    words.remove(target)
    if not words: return target[0]
    num = 0
    for i in zip_longest(*words):
        if target[num] in i:
            prefix += target[num]
            num += 1
        else:
            prefix += target[num]
            break
    return prefix





def list_all(data):
    clear()
    N = len(data['eng'])
    print('\n','{:<14}'.format('English'),'{:<15}'.format('Chinese'),'Synonym','\n',sep='')
    if N == 0: print('\n\n------- No words yet !! --------\n');return;
    
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
    continue_msg()


def quiz(data):
    N = len(data['eng'])
    m = safe_input('\nSelect quiz mode  (multiple choices(m), synonyms(sym), spelling(s), exit(e)): \n ',['m','s','e','sym'])
    
    if m == 'e': return
    
    ##### Number of question #####
    clear()
    while(True):
        try: num = int(input('\n Number of words: '))
        except ValueError:
            print('Invalid Number')
            continue
        if num <= 0: print('Invalid number')
        else: break
    if num > N:
        print('Number is too large, all words will be used once')
        input('Press ENTER to continue')
        num = N

    ##### Generating questions #####
    question = Queue()
    for i in sample(range(0,N),num): question.put(i)
    correct = set()
    only_correct = ''
    correct_list = []
    summary = ''

    while(len(correct)<num):
        clear()
        index = question.get()
        data['rec'][index][0] += 1

        ###### 問題 & 正解 ######
        ques_string = ''
        correct_ans = []

        if m=='s':
            clear()
            ques_string = '\n '+data['chn'][index]
            correct_ans.append(data['eng'][index])
            for x in data['syn'][index]:
                correct_ans.append(x)
            only_correct = sample(correct_ans,1)[0]
            hint = get_hint(correct_ans,only_correct)
            ques_string += ' ({}-):\n'.format(hint)


        if m == 'm':
            ques_string += ('\n'+data['chn'][index]+':\n\n')
            only_correct = sample([data['eng'][index]]+data['syn'][index],1)[0]
            choice = set([only_correct])
            while(len(choice)<5):
                tmp = randrange(0,N)
                if tmp == index: continue
                choice.add(sample([data['eng'][tmp]]+data['syn'][tmp],1)[0])

            alp = ord('A')
            while(len(choice)>0):
                cc = choice.pop()
                ques_string += ('  ({}) {}\n\n'.format(chr(alp),cc))
                if cc == only_correct: correct_ans = [chr(alp),chr(alp+32)]
                alp += 1

        # if m == 'syn':
        #     print('\n  To be added...')
        #     break
        #     return data

        print(ques_string)

        ##### 回答與處理 ######
        reply = input('  Answer: ')

        if reply in correct_ans:
            correct.add(index)
            correct_list.append((only_correct,data['chn'][index]))
            data['rec'][index][1] += 1
        else:
            question.put(index)
            print('\n  Correct answer: ({}) {} \n\n\n'.format(correct_ans[0].upper(),only_correct))
            continue_msg()

    ##### 總結 #######
    clear()
    print('\n Summary: \n')
    
    for i in sorted(correct_list):
        print('  {:<12}: '.format(i[0]) + '{:<12}'.format(i[1])+'\n')
    print('\n\n')
    continue_msg()

    return data










    # if m == 's':
    #     clear()
    #     while(True):
    #         try: num = int(input('\nNumber of words: '))
    #         except ValueError: 
    #             print('Invalid number')
    #             continue
    #         if not num > 0: print('Invalid number')
    #         else: break
    #     if num > N:
    #         print('Number is too large, all words will be used once')
    #         input('Press ENTER to continue')
    #         num = N
        
    #     question = set(sample(range(0,N),num))
    #     correct = set()
    #     while(len(correct)<num):
    #         clear()
    #         index = question.pop()
    #         reply = input('\n'+data['chn'][index]+': ')
    #         data['rec'][index][0] += 1
    #         if reply == data['eng'][index]:
    #             correct.add(index)
    #             data['rec'][index][1] += 1
    #         else: 
    #             question.add(index)
    #             print('\nCorrect answer: '+data['eng'][index]+'\n\n\n')
    #             continue_msg()
    #     clear()
    #     print('\n Summary: \n')
        
    #     for i in sorted(correct,key=lambda i: data['eng'][i]):
    #         print('  {:<15}: '.format(data['eng'][i])+data['chn'][i]) 
    #     print('\n\n')
    #     continue_msg()

    # if m == 'm':
    #     clear()
    #     while(True):
    #         try: num = int(input('\nNumber of words: '))
    #         except ValueError: 
    #             print('Invalid number')
    #             continue
    #         if not num > 0: print('Invalid number')
    #         else: break
    #     if num > N:
    #         print('Number is too large, all words will be used once')
    #         input('Press ENTER to continue')
    #         num = N
        
    #     question = set(sample(range(0,N),num))
    #     correct = set()
        
    #     while(len(correct) < num):
    #         clear()
    #         index = question.pop()
    #         data['rec'][index][0] += 1
    #         print('\n'+data['chn'][index]+':\n\n')
    #         choice = set([data['eng'][index]])
            
    #         while(len(choice)<5):
    #             tmp = randrange(0,N)
    #             if tmp == index: continue
    #             choice.add(data['eng'][tmp])
    #         alp = ord('A')
    #         ans = ''
    #         while(len(choice)>0):
    #             cc = choice.pop()
    #             print('  ({}) {}\n'.format(chr(alp),cc))
    #             if cc == data['eng'][index]: ans = alp
    #             alp += 1
    #         reply = input('\n Answer: ').upper()

    #         if reply == chr(ans):
    #             correct.add(index)
    #             data['rec'][index][1] += 1
    #         else:
    #             print('\nCorrect answer: {}\n'.format(chr(ans)))
    #             continue_msg()
    #             question.add(index)
    #     clear()
    #     print('\n Summary: \n')
    #     for i in sorted(correct,key=lambda i: data['eng'][i]):
    #         print('  {:<15}: '.format(data['eng'][i])+data['chn'][i]+'\n') 
    #     continue_msg()
    # update(data)
    # return initialize()

    

def add_word(data, path=_default_path):
    clear()
    while True:
        x = None
        tmp_eng = input('\nEnglish (Press ENTER to finish): ').strip()
        if tmp_eng == '': break
        if tmp_eng in data['eng']:
            x = safe_input('Word "{}" has existed, replace(r), add(a), or skip(s): '.format(tmp_eng),['r','a','s'])
        if x == 's':
            clear()
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
    print('\n')
    continue_msg()
