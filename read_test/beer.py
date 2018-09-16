from random import randint
word = "bottles"
for num in range(randint(1, 100), -1, -1):
    if num >= 1:
        print('',num, word, 'of beer on the wall\n',num, word, 'of beer\n','Take one down, pass it around\n',num-1, word, 'of beer on the wall...')
    if num == 2:
        word = 'bottle'
    if num == 0:
        print(' No more bottles of beer on the wall,\n no more bottles of beer.\n Go to the store and buy some more')
