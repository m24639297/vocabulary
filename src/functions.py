from vocData import update, _default_path, clear, initialize
from random import sample, randrange, shuffle
from queue import Queue
from itertools import zip_longest

def continue_msg():
    input('Press ENTER to continue...')

def safe_input(question, choice, exception='', _clear = True):
    while True:
        if _clear:
            clear()
        x = input(question).strip()
        if x in choice:
            return x
        if exception != '':
            print(exception)
            continue_msg()

def get_hint(_words, _target):
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
    if data['eng'] ==[]:
        print("\nThere is no word yet\n")
    else:
        indexlist = []
        for k in range(len(data['index_type'])):
            indexlist.append(str(k))
        print('\n Please choose word type to view\n'
              '\n #  Type\n')
        for k in range(len(data["index_type"])):
            print('%2d  '%k, data['index_type'][k][1], sep = '')
        i = str(input('\n Type number: ')).strip()
        if i == '':
            i ='0'
        while i not in indexlist:
            print(" Type not found, please enter again")
            i = str(input()).strip()
        while True:
            if i =="0":
                wordlist = []
                for k in range(len(data['type'])):
                    if data['type'][k] == data['index_type'][int(i)][0]:
                        wordlist.append(data['eng'][k])
                if wordlist ==[]:
                    i = str(input(" No word under this type, please enter again\n").strip())
                else:
                    break
            else:
                wordlist = []
                for k in range(len(data['type'])):
                    if data['type'][k] == data['index_type'][int(i)][0]:
                        wordlist.append(data['eng'][k])
                break
        wordlist.sort()
        clear()
        print('\n',' {:<14}'.format('English'),'{:<15}'.format('Chinese'),'Synonym','\n',sep='')
        for i in range(len(wordlist)):
            syn = ', '.join(data['syn'][data['eng'].index(wordlist[i])])
            print(' {:<14}'.format(wordlist[i]),\
              data['chn'][data['eng'].index(wordlist[i])],' '*(15-2*(len(data['chn'][data['eng'].index(wordlist[i])]))),\
              syn,sep='')
        print('\n')
    continue_msg()


def quiz(data):
    # for x in data: print(x,len(data[x]))
    # print(data)
    # input()

    N = len(data['eng'])
    m = safe_input('\nSelect quiz mode  (multiple choices(m), spelling(s), exit(e)): \n ',
                   ['m', 's', 'e']).lower()

    if m == 'e': return data

    ##### Number of question #####
    clear()
    while (True):
        try:
            num = int(input('\n Number of words: '))
        except ValueError:
            print('Invalid Number')
            continue
        if num <= 0:
            print('Invalid number')
        else:
            break
    if num > N:
        print('Number is too large, all words will be used once')
        input('Press ENTER to continue')
        num = N

    ##### Generating questions #####
    question = Queue()
    for i in sample(range(0, N), num): question.put(i)

    print(question.qsize())

    correct = set()
    only_correct = ''
    correct_list = []
    summary = ''

    while (len(correct) < num):
        clear()
        index = question.get()
        data['rec'][index][0] += 1

        ###### 問題 & 正解 ######
        ques_string = ''
        correct_ans = []

        if m == 's':
            clear()
            ques_string = '\n ' + data['chn'][index]
            correct_ans.append(data['eng'][index])
            for x in data['syn'][index]:
                if x == '': break
                correct_ans.append(x)
            only_correct = sample(correct_ans, 1)[0]
            hint = get_hint(correct_ans, only_correct)
            ques_string += ' ({}-):\n'.format(hint)

        if m == 'm':
            ques_string += ('\n' + data['chn'][index] + ':\n\n')
            only_correct = sample([data['eng'][index]] + data['syn'][index]*(data['syn'][index]!=['']), 1)[0]
            choice = set([only_correct])
            while (len(choice) < 5):
                tmp = randrange(0, N)
                if tmp == index: continue
                choice.add(sample([data['eng'][tmp]] + data['syn'][tmp]*(data['syn'][tmp]!=['']), 1)[0])

            alp = ord('A')
            while (len(choice) > 0):
                cc = choice.pop()
                ques_string += ('  ({}) {}\n\n'.format(chr(alp), cc))
                if cc == only_correct: correct_ans = [chr(alp), chr(alp + 32)]
                alp += 1

        # if m == 'syn':
        #     print('\n  To be added...')
        #     break
        #     return data

        print(ques_string)

        ##### 回答與處理 ######
        reply = input('  Answer: ').lower()

        if reply in correct_ans:
            correct.add(index)
            correct_list.append((only_correct, data['chn'][index]))
            data['rec'][index][1] += 1
        else:
            question.put(index)
            if m == 'm': print('\n  Correct answer: ({}) {} \n\n\n'.format(correct_ans[0].upper(), only_correct))
            if m == 's': print('\n  Correct answer: {} \n\n\n'.format(only_correct))
            continue_msg()

    ##### 總結 #######
    clear()
    print('\n Summary: \n')

    for i in sorted(correct_list):
        print('  {:<12}: '.format(i[0]) + '{:<12}'.format(i[1]) + '\n')
    print('\n\n')
    continue_msg()

    return data

def add_word(data, path=_default_path):
    clear()
    while True:
        x = None
        tmp_eng = input('\n English (Press ENTER to finish): ').strip()
        if tmp_eng == '': break
        if tmp_eng in data['eng']:
            x = safe_input(' Word "{}" has existed, add(a), or skip(s): '.format(tmp_eng), ['a', 's'])
        if x == 's':
            clear()
            print('\n--Skipped--\n')
            continue
        print("\n Please choose the type (enter the number).\n"
              'or enter new type name to add a new type.\n'
              "If you don't want to classify this word, just left it blank\n"
              "(press enter to continue)\n\n"
              "<type index>")
        for k in range(len(data["index_type"])-1):
            print(data['index_type'][k+1][1],data['index_type'][k+1][0])
        t = str(input()).strip()
        n = True
        for k in range(len(data["index_type"])):
            if data["index_type"][k][0] == t:
                tt = int(data["index_type"][k][0])
                n = False
        if t != '' and n == True:
            data['index_type'].append([str(len(data["index_type"])), t])
            tt = len(data['index_type']) - 1
        elif t == "":
            tt = 0
        tmp_chn = input('Chinese: ').strip()
        tmp_syn = input('Synonyms (Separate by comma): ').strip()
        
        if x == None or x == 'a':
            data['eng'].append(tmp_eng)
            data['chn'].append(tmp_chn)
            data['syn'].append([ii.strip() for ii in tmp_syn.split(',')])
            data['rec'].append([0,0])
            data['type'].append(str(tt))
    update(data)
    return initialize()

def history(data):
    N = len(data['eng'])
    clear()
    print('\n(Word: (correct, wrong))\n')
    for i in sorted(range(N), key = lambda i: data['eng'][i]):
        print('{:<14}: ({}, {})'.format(data['eng'][i],data['rec'][i][1],data['rec'][i][0]-data['rec'][i][1]))
    input('\nPress ENTER to continue')

def edit(data):
    if data['eng'] ==[]:
        print("\nThere is no word yet\n")
        continue_msg()
    else:
        indexlist = []
        for k in range(len(data['index_type'])):
            indexlist.append(str(k))
        clear()
        print('\nPlease choose word type to edit\n'
              'To show unclassified words, press enter to continue\n'
              '\n #   type')

        for k in range(len(data["index_type"])):
            print('%2d  '%k, data['index_type'][k][1])
        i = str(input('\n Select type: ')).strip()
        if i == '':
            i ='0'
        while True:
            if i =="0":
                wordlist = []
                for k in range(len(data['type'])):
                    if data['type'][k] == data['index_type'][int(i)][0]:
                        wordlist.append(data['eng'][k])
                if wordlist ==[]:
                    i = str(input("No word in this type, please choose another type.\n").strip())
                else:
                    break
            elif i != 0 and i not in indexlist:
                print("Word not found, please enter again")
                i = str(input()).strip()
            else:
                wordlist = []
                for k in range(len(data['type'])):
                    if data['type'][k] == data['index_type'][int(i)][0]:
                        wordlist.append(data['eng'][k])
                break
        clear()
        print('\n Please choose the word to edit')
        print('\nclass<',data['index_type'][int(i)][1],'>:\n')
        wordlist = []
        for k in range(len(data['type'])):
            if data['type'][k]== data['index_type'][int(i)][0]:
                wordlist.append(data['eng'][k])
        wordlist.sort()
        number = []
        for i in range(len(wordlist)):
            print(i+1,wordlist[i])
            number.append(str(i+1))
        r = input()
        while r not in number:
            print('Please enter the right index again')
            r = input()
        print(r)
        r = int(r)
        b = wordlist[r-1]
        clear()
        print("\n%s\n"%b)
        f = input(" Which part of the word do you want to edit? \n (e: english, c: chinese, s: synonym, r: remove)\n ")
        if f == 'e':
            print(' Original English:',b)
            new = input(' New: ')
            sure = input(" Are you sure to change English of '%s' ? (y/n) "%b).lower()
            if sure in ['y','']:
                i = data['eng'].index(b)
                data['eng'][i] = new
                continue_msg()
            else:
                continue_msg()
        if f == 'c':
            print(' Original Chinese:',data['chn'][data['eng'].index(b)])
            new = input('New: ')
            sure = input(" Are you sure to change Chinese of '%s' ? (y    /n) "%b).lower()
            if sure in ['y','']:
                data['chn'][data['eng'].index(b)] = new
                continue_msg()
            else:
                continue_msg()

        if f == 's':
            print(' Enter new synonyms (separated by comma)')
            syn = ' '.join(data['syn'][data['eng'].index(b)])
            print(' Original synonyms:',syn)
            a= input(' New synonyms: ').strip()
            a = a.split(',')
            print('\n\n')
            sure = input(" Are you sure to change the synonyms of '%s'? (y/n) "%b).lower()
            if sure in ['y','']:
                data['syn'][data['eng'].index(b)] = a
                print('\n\n')
                continue_msg()
            else:
                continue_msg()
        if f =='r':
            print('\n\n')
            sure = input(" Are you sure to delete '%s'? (y/n) "%b)
            if sure in ['y', '']:
                place = data['eng'].index(b)
                data['eng'].pop(place)
                data['chn'].pop(place)
                data['syn'].pop(place)
                data['rec'].pop(place)
                data['type'].pop(place)
                print(" The word '%s' has been deleted\n" % b)
                for i in range(1,len(data['index_type'])):
                    if str(i) not in data['type']:
                        data['index_type'].pop(i)
                continue_msg()
            else:
                continue_msg()
        update(data)
        return data

