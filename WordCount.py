import re

def longestWord():
     with open(r'Text.txt', 'r+') as f:
        users_text = f.read()
        longest = max(users_text.split(), key=len)
        count_longest = str(len(longest))
        print('The longest word in the file is: ' + longest)
        print('Thats a total of '+count_longest+' letters!')

def writeWord():
    with open(r'Text.txt', 'w') as f:
        users_text = input('Enter your desired text to continue. \n: ')
        cleanText = re.sub('[^a-zA-Z0-9 \n\.]', ' ', users_text)
        f.write(cleanText)
        with open(r'Text.txt', 'r') as clean:
            print('\nRemoved any illegal characters. Here is your text:\n\n' + cleanText + '\n')
        f.close()

while True:
    print("""
Welcome to Skies word text counter!
====================================================
""")
    writeWord()
    longestWord()
    userDecide = input("""
====================================================
Would you like to enter new text and repeat?
Type 'yes' to continue else program will terminate.
====================================================
: """)
    if not userDecide.lower == 'yes':
        print('Application closing...')
        exit()
