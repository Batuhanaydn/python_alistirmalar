import re
s = input('Type a word: ')
slower=''.join(re.findall(r'[a-z]',s))
supper=''.join(re.findall(r'[A-Z]',s))
if len(supper) == 0:
    print('The entered word(s) are made up of lowercase letters.')
else:
    print('Word(s) has capital letters')
