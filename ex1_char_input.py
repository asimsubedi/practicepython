username = input('what is your name?')
userage = int(input('what is your age?'))
centuryin = 100 - userage
loopmsg = int(input('How Many times to display?'))
for i in range(loopmsg):
    print('Hello Mr. ' + username +'. You will be 100 after ' + str(centuryin) + ' years \n')
