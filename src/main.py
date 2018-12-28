from functions import list_all, quiz, add_word, history
from vocData import update, initialize, _default_path, clear

data = initialize()
eng = data['eng']
chn = data['chn']
syn = data['syn']
rec = data['rec']


while(True):
    clear()
    # print(data)
    mode = input('\nPlease select mode (v: view all, q: quiz, a: add words, h: history, e: exit)\n')
    if mode not in ['v','q','a','e','h']:
        clear()
        continue
    if mode == 'e' or mode == 'E':
        clear()
        update(data)
        print('\n  Bye~'+'\n'*10)
        break
    if mode == 'v' or mode == 'V':
        list_all(data)
    if mode == 'q' or mode == 'Q':
        data = quiz(data)
    if mode == 'a' or mode == 'A':
        data = add_word(data, path=_default_path)
    if mode == 'h' or mode == 'H':
        history(data)
