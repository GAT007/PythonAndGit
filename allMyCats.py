catNames = []
while True:
    name = raw_input(('Enter the name of cat' + str(len(catNames) + 1) ) + (' Or Enter nothing to stop : '))
    if name == '':
        break
    catNames = catNames + [name]

print('The cat names are : ')
for name in catNames :
    print ("Name : " + name)