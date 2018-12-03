from initialize import initialize, _default_path, clear
from functions import list_all, quiz, add_word


data = initialize()
eng = data['eng']
chn = data['chn']
syn = data['syn']
rec = data['rec']

while(True):
    clear()
    mode = input('\nPlease select mode (v: view all, q: quiz, a: add words, e: exit)\n')
    if mode not in ['v','q','a','e']:
        clear()
        continue
    if mode == 'e' or mode == 'E':
        clear()
        print('\nBye'+'\n'*10)
        break
    if mode == 'v' or mode == 'V':
        list_all(data)
    if mode == 'q' or mode == 'Q':
        quiz(data)
    if mode == 'a' or mode == 'A':
        add_word(data, path=_default_path)

