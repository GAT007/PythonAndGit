import random,sys,os,math


def hello():
    print('Howdy!')
    print('How do you do?')
    print('Put her there')

def hello(name):
    actualName = str(name)
    print("Hello " + actualName)

hello("Amith")
hello(2)

hello(11.11)

while True:
    response=raw_input('Type exit to exit : ')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')


