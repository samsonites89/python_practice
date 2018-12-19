# A simple while python program
# function takes an input and then prints the number in iteration


def while_practice(data):
    while data > 0:
        print(data)
        data -= 1


while_practice(int(input("Input a number: ")))

for n in [2, 3, 4]:
    print("--{0}--단".format(n))  # 숫자를 써서 position을 뜻한다
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("{0}*{1}={2}".format(n, i, n * i))

#######################################################################
# for loops with break
L = [1, 2, 3, 4, 5, 6, 7, 8]
for i in L:
    if i == 5:
        break
    print("{0}".format(i))

# for loop with continue
L = [1, 2, 3, 4, 5, 6, 7, 8]
for i in L:
    if i == 5:
        continue
    print("{0}".format(i))

print([i ** 2 for i in L if L.index(i) < 3])


# Filter


def get_bigger_than_20(i):
    return i > 20


L = [10, 25, 40]  # this is a list
IterL = filter(get_bigger_than_20, L)
for item in IterL:
    print(item)
print("##################################\n")
IterL = filter(lambda lam: lam > 20, L)
for item in IterL:
    print(item)
