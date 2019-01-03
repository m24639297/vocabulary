from functions import list_all, quiz, add_word, history,edit
from vocData import update, initialize, _default_path, clear

data = initialize()
eng = data['eng']
chn = data['chn']
syn = data['syn']
rec = data['rec']
index_type = data['index_type']
type_ = data['type']
while(True):
    clear()
    mode = input('\nPlease select mode (v: view all, q: quiz, a: add words, h: practice history, ed: edit, e: exit)\n')
    mode = mode.lower()
    if mode not in ['v','q','a','e','h',"ed"]:
        clear()
        continue
    if mode == 'e':
        clear()
        print("Are you sure to exit ?")
        sure = input('(enter y or n)\n').lower()
        if sure == 'y':
            update(data)
            print('\nBye'+'\n'*10)
            break
        else:
            pass
    if mode == 'v':
        list_all(data)
    if mode == 'q':
        data = quiz(data)
    if mode == 'a':
        data = add_word(data, path=_default_path)
    if mode == 'h':
        history(data)
    if mode == 'ed':
        data = edit(data)