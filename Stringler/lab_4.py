import re
import string
import random
def findUpper(s):
    
    slower=''.join(re.findall(r'[a-z]',s))
    supper=''.join(re.findall(r'[A-Z]',s))
    if len(supper) == 0:
        print('The entered word(s) are made up of lowercase letters.')
    else:
        print('Word(s) has capital letters')

if __name__ == "__main__":
    length = 10
    s = ''.join(random.choices(string.ascii_letters, k=length))
    # print(s)
    findUpper(s)
