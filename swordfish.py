import random

for i in range(10, 0, -2):
    print(random.randint(1, 20))


while True:
    print("Who are you?")
    name = raw_input()
    if name != "Joe":
        continue
    password =raw_input("Hello Joe. What is the password ? Hint : Tis a fish")
    if password == "swordfish":
        print("Congratulation Joe, you've unleashed armageddon upon earth!")
        break


print("My name is : " + name)
for i in range(5):
    print(str(i) + " Frankie four fingers is out to get " + name)