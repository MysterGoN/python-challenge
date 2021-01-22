# Start page: http://www.pythonchallenge.com/pc/def/linkedlist.php


from urllib import request

FIRST_STRAT_NUMBER = 12345
SECOND_START_NUMBER = 8022

url_tpl = ''


number = SECOND_START_NUMBER
while True:
    res = request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={number}')

    if res.getcode() == 200:
        text = res.read().decode('utf-8')
        print(text)
        try:
            number = int(text.split(' ')[-1])
        except ValueError:
            break

        continue
    break
