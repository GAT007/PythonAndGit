spam1 = ['cat', 'mat', 'bat', 'rat']
print(spam1[1])
spam2 = [['mat', 'bat'], [10, 12, 14, 16, 18]]
print(spam2[0][1], spam2[1][2])
print(spam2[-1][-1])
print(spam1[1:-1])
print(spam2[:])
def isNullList(list):
    if len(list) > 0:
        return True
    else:
        return False
if isNullList(spam1):
    print("Hooray! There are elements in the list!")
    print(len(spam1))
    print("Let's change some values")
    print("Value of spam2[0][1]: " + spam2[0][1])
    spam2[0][1] = "elephant"
    print("Value of spam2[0][1]: " + spam2[0][1])
    spam2 = spam2[0] + ["cat"]
    print("Value of spam2[0][2]: " + spam2[0][2])
    print(spam2)
