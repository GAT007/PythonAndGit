import random
messages = ['It is certain',
            'It is decidedly so',
            'Reply hazy try again',
            'Ask again later',
            'Outlook not so good',
            'Very doubtful',
            'My reply is no',
            'Concentrate and ask again',
            'Yes Definitely']
while True :
    print("What is your question chela? : ")
    question = raw_input()
    if(question==''):
        break
    print( "Your answer to the question is : ")
    print(messages[random.randint(0, len(messages) - 1)])
